"""Score the triage agent against the 50 labelled tickets.

    python -m eval.agent_eval
    python -m eval.agent_eval --limit 10

Metrics:

  category accuracy     did the classification sub-agent pick the right one of
                        13 categories.
  priority accuracy     exact match, and within-one-level, because P2 against
                        P3 on a judgement call is not the same failure as P4
                        against P1.
  routing accuracy      did the ticket reach the right queue. Queue is resolved
                        from the retrieved document's owner, so this measures
                        retrieval and classification together.
  auto-resolve rate     share of tickets the agent was willing to resolve
                        without a human.
  false auto-resolve    share of auto-resolved tickets that the labels say
                        needed a human. This is the number that matters. A
                        high auto-resolve rate is easy to get and worthless if
                        this is not near zero, so never quote one without the
                        other.
  asset tool recall     of tickets that can only be answered from the asset
                        inventory, how many did the planner actually call the
                        asset tool for.

Results are written to eval_results/agent_eval.json.
"""

from __future__ import annotations

import argparse
import json
import time

from agent.graph import run_triage
from shared.config import DATA_DIR, EVAL_DIR, settings

PRIORITY_INDEX = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}


def load_tickets(limit: int | None = None) -> list[dict]:
    path = DATA_DIR / "tickets.json"
    if not path.exists():
        raise RuntimeError("No tickets.json. Run `python -m data.generate` first.")
    tickets = json.loads(path.read_text(encoding="utf-8"))
    return tickets[:limit] if limit else tickets


def evaluate(tickets: list[dict]) -> dict:
    records = []
    started = time.time()

    for position, ticket in enumerate(tickets, start=1):
        state = run_triage(ticket)
        nodes_run = [step["node"] for step in state.get("trace", [])]

        record = {
            "ticket_id": ticket["ticket_id"],
            "subject": ticket["subject"],
            "expected_category": ticket["expected_category"],
            "predicted_category": state.get("category"),
            "expected_priority": ticket["expected_priority"],
            "predicted_priority": state.get("priority"),
            "expected_queue": ticket["expected_queue"],
            "predicted_queue": state.get("queue"),
            "expected_auto_resolvable": ticket["expected_auto_resolvable"],
            "predicted_auto_resolvable": bool(state.get("auto_resolvable")),
            "needs_asset_lookup": ticket["needs_asset_lookup"],
            "asset_tool_called": "asset" in nodes_run,
            "knowledge_tool_called": "knowledge" in nodes_run,
            "knowledge_covered": state.get("knowledge_covered"),
            "confidence": state.get("confidence"),
            "hold_reason": state.get("hold_reason"),
            "nodes_run": nodes_run,
        }
        record["category_correct"] = record["expected_category"] == record["predicted_category"]
        record["queue_correct"] = record["expected_queue"] == record["predicted_queue"]
        record["priority_correct"] = record["expected_priority"] == record["predicted_priority"]
        exp = PRIORITY_INDEX.get(record["expected_priority"], 0)
        got = PRIORITY_INDEX.get(record["predicted_priority"], 0)
        record["priority_within_one"] = abs(exp - got) <= 1
        records.append(record)

        marks = "".join([
            "C" if record["category_correct"] else ".",
            "Q" if record["queue_correct"] else ".",
            "P" if record["priority_correct"] else ".",
        ])
        print(f"  [{position:>2}/{len(tickets)}] {ticket['ticket_id']}  {marks}  "
              f"auto={'Y' if record['predicted_auto_resolvable'] else 'N'}"
              f"(exp {'Y' if record['expected_auto_resolvable'] else 'N'})")

    return summarise(records, time.time() - started)


def summarise(records: list[dict], elapsed: float) -> dict:
    total = len(records)

    def rate(predicate) -> float:
        return sum(1 for r in records if predicate(r)) / total if total else 0.0

    auto = [r for r in records if r["predicted_auto_resolvable"]]
    false_auto = [r for r in auto if not r["expected_auto_resolvable"]]
    should_auto = [r for r in records if r["expected_auto_resolvable"]]
    caught_auto = [r for r in should_auto if r["predicted_auto_resolvable"]]

    asset_needed = [r for r in records if r["needs_asset_lookup"]]
    asset_called = [r for r in asset_needed if r["asset_tool_called"]]
    asset_false_calls = [
        r for r in records if r["asset_tool_called"] and not r["needs_asset_lookup"]
    ]

    return {
        "config": {
            "provider": settings.provider,
            "chat_model": settings.chat_model,
            "rerank_top_k": settings.rerank_top_k,
        },
        "n": total,
        "category_accuracy": rate(lambda r: r["category_correct"]),
        "queue_accuracy": rate(lambda r: r["queue_correct"]),
        "priority_accuracy": rate(lambda r: r["priority_correct"]),
        "priority_within_one": rate(lambda r: r["priority_within_one"]),
        "auto_resolve_rate": len(auto) / total if total else 0.0,
        "false_auto_resolve_rate": len(false_auto) / len(auto) if auto else 0.0,
        "auto_resolve_recall": len(caught_auto) / len(should_auto) if should_auto else 0.0,
        "asset_tool_recall": len(asset_called) / len(asset_needed) if asset_needed else 0.0,
        "asset_tool_false_calls": len(asset_false_calls),
        "seconds": round(elapsed, 1),
        "records": records,
    }


def print_report(summary: dict) -> None:
    def pct(value: float) -> str:
        return f"{value * 100:5.1f}%"

    print("\n" + "=" * 72)
    print("TRIAGE AGENT EVALUATION")
    print("=" * 72)
    print(f"Provider {summary['config']['provider']}  |  "
          f"chat {summary['config']['chat_model']}  |  {summary['n']} tickets")
    print()
    print(f"  Category accuracy          {pct(summary['category_accuracy'])}")
    print(f"  Routing (queue) accuracy   {pct(summary['queue_accuracy'])}")
    print(f"  Priority accuracy (exact)  {pct(summary['priority_accuracy'])}")
    print(f"  Priority within one level  {pct(summary['priority_within_one'])}")
    print()
    print(f"  Auto-resolve rate          {pct(summary['auto_resolve_rate'])}")
    print(f"  False auto-resolve rate    {pct(summary['false_auto_resolve_rate'])}"
          f"   <- the one that matters")
    print(f"  Auto-resolve recall        {pct(summary['auto_resolve_recall'])}")
    print()
    print(f"  Asset tool recall          {pct(summary['asset_tool_recall'])}")
    print(f"  Asset tool false calls     {summary['asset_tool_false_calls']}")
    print(f"\nCompleted in {summary['seconds']}s")

    bad = [r for r in summary["records"]
           if r["predicted_auto_resolvable"] and not r["expected_auto_resolvable"]]
    if bad:
        print(f"\nFalse auto-resolves ({len(bad)}) - these would have reached a user:")
        for r in bad:
            print(f"  {r['ticket_id']}  {r['subject'][:60]}")

    miscat = [r for r in summary["records"] if not r["category_correct"]]
    if miscat:
        print(f"\nCategory errors ({len(miscat)}):")
        for r in miscat[:12]:
            print(f"  {r['ticket_id']}  expected {r['expected_category']:<18} "
                  f"got {r['predicted_category']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the triage agent.")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    tickets = load_tickets(args.limit)
    print(f"Triaging {len(tickets)} tickets ...")
    summary = evaluate(tickets)
    print_report(summary)

    EVAL_DIR.mkdir(parents=True, exist_ok=True)
    out = EVAL_DIR / "agent_eval.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nFull results: {out}")


if __name__ == "__main__":
    main()
