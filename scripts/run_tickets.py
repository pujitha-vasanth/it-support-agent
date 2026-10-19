"""Triage a batch of tickets into the approval queue, for a demo or a dry run.

    python scripts/run_tickets.py                # all tickets in data/tickets.json
    python scripts/run_tickets.py --limit 5
    python scripts/run_tickets.py --only T046    # one ticket by id

Each ticket goes through the graph and lands in the queue as 'pending'.
Nothing is sent. Review with: python -m agent.approve list
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agent.graph import run_triage  # noqa: E402
from shared.config import DATA_DIR  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Triage tickets into the approval queue.")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--only", default=None, help="A single ticket id, e.g. T046")
    args = parser.parse_args()

    tickets = json.loads((DATA_DIR / "tickets.json").read_text(encoding="utf-8"))
    if args.only:
        tickets = [t for t in tickets if t["ticket_id"] == args.only]
        if not tickets:
            print(f"No ticket with id {args.only}.")
            return
    if args.limit:
        tickets = tickets[: args.limit]

    print(f"Triaging {len(tickets)} ticket(s). Nothing will be sent.\n")
    held = 0
    for position, ticket in enumerate(tickets, start=1):
        state = run_triage(ticket)
        auto = state.get("auto_resolvable")
        held += 0 if auto else 1
        print(f"  [{position:>2}/{len(tickets)}] {ticket['ticket_id']}  "
              f"{state.get('priority')}  {str(state.get('queue'))[:26]:<26} "
              f"auto={'yes' if auto else 'no '}  {ticket['subject'][:38]}")

    print(f"\n{len(tickets)} drafted, {held} held for a human, "
          f"{len(tickets) - held} cleared as auto-resolvable.")
    print("All of them are pending approval. Review with:")
    print("  python -m agent.approve list")


if __name__ == "__main__":
    main()
