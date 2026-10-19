"""The object that flows through the graph.

LangGraph merges each node's returned dict into this state, so a node only
returns the keys it actually changed. Every node also appends to `trace`,
which is what gets persisted and shown to the human approver: without it,
an approver is asked to sign off on a reply with no view of how it was reached.
"""

from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class TriageState(TypedDict, total=False):
    # Input
    ticket_id: str
    subject: str
    body: str
    requester_email: str

    # Planner output
    needs_knowledge: bool
    needs_asset: bool
    plan_reason: str

    # Classification sub-agent
    category: str
    priority: str
    confidence: float
    requires_it_action: bool

    # Knowledge sub-agent
    knowledge_answer: str
    knowledge_covered: bool
    citations: list[dict]
    retrieved_owner: str

    # Asset sub-agent
    asset_found: bool
    asset_summary: str
    asset_record: dict

    # Draft and decision
    queue: str
    draft_reply: str
    auto_resolvable: bool
    hold_reason: str

    # Audit
    trace: Annotated[list[dict], operator.add]
