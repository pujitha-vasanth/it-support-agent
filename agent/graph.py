"""The LangGraph graph: planner, fan-out to sub-agents, draft, hold for approval.

    planner ──► classify ──┬──► knowledge ──┐
                           ├──► asset ──────┼──► draft ──► persist ──► END
                           └────────────────┘

The fan-out after classify is a conditional edge that returns a list of node
names, so the knowledge and asset sub-agents run in parallel when the planner
asked for both. LangGraph waits for both before entering draft.

Nothing is ever sent from inside the graph. The final node writes the draft to
the database with approval_status 'pending'. Sending is a separate, human
action: see agent/approve.py.
"""

from __future__ import annotations

import json

from langgraph.graph import END, START, StateGraph

from agent.nodes import asset, classify, draft, knowledge, planner
from agent.state import TriageState
from shared.db import get_connection


def persist(state: TriageState) -> dict:
    """Write the run to the database and hold it for a human."""
    with get_connection() as conn:
        row = conn.execute(
            """
            INSERT INTO triage_runs
                (ticket_id, subject, body, requester_email, category, priority,
                 queue, auto_resolvable, confidence, draft_reply, citations,
                 asset_summary, trace, approval_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'pending')
            RETURNING id
            """,
            (
                state.get("ticket_id", ""),
                state.get("subject", ""),
                state.get("body", ""),
                state.get("requester_email"),
                state.get("category"),
                state.get("priority"),
                state.get("queue"),
                bool(state.get("auto_resolvable", False)),
                float(state.get("confidence", 0.0)),
                state.get("draft_reply", ""),
                json.dumps(state.get("citations", [])),
                state.get("asset_summary"),
                json.dumps(state.get("trace", [])),
            ),
        ).fetchone()
    return {"trace": [{"node": "persist", "run_id": row[0], "approval_status": "pending"}]}


def route_after_classify(state: TriageState) -> list[str]:
    """Conditional fan-out. Returning a list runs those nodes in parallel."""
    targets = []
    if state.get("needs_knowledge", True):
        targets.append("knowledge")
    if state.get("needs_asset", False):
        targets.append("asset")
    return targets or ["draft"]


def build_graph():
    graph = StateGraph(TriageState)
    graph.add_node("planner", planner)
    graph.add_node("classify", classify)
    graph.add_node("knowledge", knowledge)
    graph.add_node("asset", asset)
    graph.add_node("draft", draft)
    graph.add_node("persist", persist)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "classify")
    graph.add_conditional_edges(
        "classify", route_after_classify, ["knowledge", "asset", "draft"]
    )
    graph.add_edge("knowledge", "draft")
    graph.add_edge("asset", "draft")
    graph.add_edge("draft", "persist")
    graph.add_edge("persist", END)

    return graph.compile()


_compiled = None


def get_graph():
    global _compiled
    if _compiled is None:
        _compiled = build_graph()
    return _compiled


def run_triage(ticket: dict) -> TriageState:
    """Run one ticket through the whole graph."""
    initial: TriageState = {
        "ticket_id": ticket.get("ticket_id", ""),
        "subject": ticket.get("subject", ""),
        "body": ticket.get("body", ""),
        "requester_email": ticket.get("requester_email", ""),
        "trace": [],
    }
    return get_graph().invoke(initial)
