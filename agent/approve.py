"""The human approval gate.

The graph never sends anything. It writes a draft with approval_status
'pending'. A person reads it here and decides. That is the whole control, and
it is deliberately boring: an approval step that can be bypassed by a flag is
not an approval step.

    python -m agent.approve list
    python -m agent.approve show 3
    python -m agent.approve approve 3 --by pujitha
    python -m agent.approve reject 3 --by pujitha --note "wrong team"
"""

from __future__ import annotations

import argparse
import json
import textwrap

from shared.db import get_connection

PENDING = "pending"
APPROVED = "approved"
REJECTED = "rejected"


def list_runs(status: str = PENDING, limit: int = 50) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, ticket_id, subject, category, priority, queue,
                   auto_resolvable, confidence, approval_status, created_at
            FROM triage_runs
            WHERE (%s = 'all' OR approval_status = %s)
            ORDER BY id DESC
            LIMIT %s
            """,
            (status, status, limit),
        ).fetchall()
    return [
        {
            "id": r[0], "ticket_id": r[1], "subject": r[2], "category": r[3],
            "priority": r[4], "queue": r[5], "auto_resolvable": r[6],
            "confidence": r[7], "approval_status": r[8], "created_at": str(r[9]),
        }
        for r in rows
    ]


def get_run(run_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT id, ticket_id, subject, body, requester_email, category,
                   priority, queue, auto_resolvable, confidence, draft_reply,
                   citations, asset_summary, trace, approval_status, approved_by,
                   decision_note, created_at
            FROM triage_runs WHERE id = %s
            """,
            (run_id,),
        ).fetchone()
    if not row:
        return None
    keys = [
        "id", "ticket_id", "subject", "body", "requester_email", "category",
        "priority", "queue", "auto_resolvable", "confidence", "draft_reply",
        "citations", "asset_summary", "trace", "approval_status", "approved_by",
        "decision_note", "created_at",
    ]
    record = dict(zip(keys, row))
    record["created_at"] = str(record["created_at"])
    return record


def decide(run_id: int, status: str, by: str, note: str = "") -> dict | None:
    if status not in (APPROVED, REJECTED):
        raise ValueError("status must be 'approved' or 'rejected'")
    with get_connection() as conn:
        row = conn.execute(
            """
            UPDATE triage_runs
               SET approval_status = %s, approved_by = %s,
                   decision_note = %s, decided_at = now()
             WHERE id = %s AND approval_status = 'pending'
         RETURNING id
            """,
            (status, by, note or None, run_id),
        ).fetchone()
    if not row:
        return None
    return get_run(run_id)


def _print_run(record: dict) -> None:
    print("=" * 78)
    print(f"Run {record['id']}  |  ticket {record['ticket_id']}  |  "
          f"{record['approval_status'].upper()}")
    print("=" * 78)
    print(f"Subject    : {record['subject']}")
    print(f"From       : {record['requester_email']}")
    print(f"Routed to  : {record['queue']}")
    print(f"Category   : {record['category']}   Priority: {record['priority']}   "
          f"Confidence: {record['confidence']:.2f}")
    print(f"Auto-resolvable: {record['auto_resolvable']}")
    if record.get("asset_summary"):
        print(f"\nAsset      : {textwrap.fill(record['asset_summary'], 74, subsequent_indent='             ')}")

    print("\n--- Original ticket " + "-" * 58)
    print(textwrap.fill(record["body"], 78))

    print("\n--- Draft reply " + "-" * 62)
    print(record["draft_reply"])

    citations = record.get("citations") or []
    if citations:
        print("\n--- Citations " + "-" * 64)
        for c in citations:
            print(f"  [{c['n']}] {c['document']}, {c['section']} (p. {c['page']})")

    trace = record.get("trace") or []
    if trace:
        print("\n--- Trace " + "-" * 68)
        for step in trace:
            detail = {k: v for k, v in step.items() if k != "node"}
            print(f"  {step['node']:<10} {json.dumps(detail, default=str)[:140]}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Review and approve drafted replies.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List runs awaiting a decision.")
    p_list.add_argument("--status", default=PENDING,
                        choices=[PENDING, APPROVED, REJECTED, "all"])

    p_show = sub.add_parser("show", help="Show one run in full.")
    p_show.add_argument("run_id", type=int)

    p_ok = sub.add_parser("approve", help="Approve and release a draft.")
    p_ok.add_argument("run_id", type=int)
    p_ok.add_argument("--by", required=True, help="Who is approving.")
    p_ok.add_argument("--note", default="")

    p_no = sub.add_parser("reject", help="Reject a draft.")
    p_no.add_argument("run_id", type=int)
    p_no.add_argument("--by", required=True)
    p_no.add_argument("--note", default="")

    args = parser.parse_args()

    if args.command == "list":
        runs = list_runs(args.status)
        if not runs:
            print(f"No runs with status '{args.status}'.")
            return
        print(f"{'id':>4}  {'ticket':<7} {'pri':<4} {'auto':<6} {'queue':<28} subject")
        print("-" * 100)
        for r in runs:
            print(f"{r['id']:>4}  {r['ticket_id']:<7} {r['priority']:<4} "
                  f"{str(r['auto_resolvable']):<6} {r['queue'][:28]:<28} {r['subject'][:34]}")
        print(f"\n{len(runs)} run(s). Use: python -m agent.approve show <id>")
        return

    if args.command == "show":
        record = get_run(args.run_id)
        if not record:
            print(f"No run with id {args.run_id}.")
            return
        _print_run(record)
        return

    status = APPROVED if args.command == "approve" else REJECTED
    record = decide(args.run_id, status, args.by, args.note)
    if not record:
        print(f"Run {args.run_id} is not pending, or does not exist. Nothing changed.")
        return
    print(f"Run {args.run_id} {status} by {args.by}.")
    if status == APPROVED:
        print("\nThe following reply is now cleared to send:\n")
        print(record["draft_reply"])


if __name__ == "__main__":
    main()
