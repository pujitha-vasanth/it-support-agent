"""The planner and the three sub-agents, as LangGraph nodes.

Each node takes the state and returns only the keys it changed. Every node
appends one entry to the trace, so the human approver can see what the system
did and why, rather than being handed a reply with no provenance.
"""

from __future__ import annotations

import json
from typing import Any

from agent import taxonomy
from agent.state import TriageState
from agent.tools import asset_tool, knowledge_tool, summarise_asset
from shared.providers import get_provider, parse_json_response


def _trace(node: str, **detail: Any) -> list[dict]:
    return [{"node": node, **detail}]


def _ticket_text(state: TriageState) -> str:
    return f"Subject: {state.get('subject', '')}\n\n{state.get('body', '')}"


# ---------------------------------------------------------------------------
# Planner
# ---------------------------------------------------------------------------

PLANNER_SYSTEM = """You are the planner for an IT service desk agent.

You decide which tools are needed to handle a ticket. You do not answer it.

Two tools are available:

  knowledge  Searches the company's IT policy and runbook corpus. Use it when
             the ticket asks how something works, what a rule or limit is, how
             to do something, or reports a fault that is likely documented.

  asset      Looks up the device assigned to the person who raised the ticket:
             model, age, operating system, warranty end, location, licensed
             software. Use it when the ticket is about the requester's own
             device or entitlements, or when answering needs a detail that is
             specific to their machine.

Both, one, or neither may be needed. Prefer calling a tool over guessing.

Reply with JSON only:
{"needs_knowledge": true, "needs_asset": false, "reason": "one short sentence"}

Never use em dashes."""


def planner(state: TriageState) -> dict:
    raw = get_provider().chat(PLANNER_SYSTEM, _ticket_text(state), json_mode=True)
    try:
        plan = parse_json_response(raw)
    except Exception:
        plan = {"needs_knowledge": True, "needs_asset": False, "reason": "planner output unreadable, defaulting to knowledge"}

    needs_knowledge = bool(plan.get("needs_knowledge", True))
    needs_asset = bool(plan.get("needs_asset", False))
    reason = str(plan.get("reason", ""))[:300]

    return {
        "needs_knowledge": needs_knowledge,
        "needs_asset": needs_asset,
        "plan_reason": reason,
        "trace": _trace(
            "planner",
            needs_knowledge=needs_knowledge,
            needs_asset=needs_asset,
            reason=reason,
        ),
    }


# ---------------------------------------------------------------------------
# Sub-agent 1: classification
# ---------------------------------------------------------------------------

CLASSIFIER_SYSTEM = f"""You classify IT service desk tickets.

Choose exactly one category from this list:
{", ".join(taxonomy.CATEGORIES)}

Choose exactly one priority using this guide:
{taxonomy.PRIORITY_GUIDE}

Also judge whether the ticket requires IT to perform an action, meaning work
someone in IT must carry out, such as provisioning an account, granting access,
ordering or shipping hardware, or changing a configuration. A ticket that is
fully answered by telling the person something is NOT an IT action.

Give a confidence between 0 and 1 for your category choice. Be honest: use a
low value when the ticket is vague or could sit in two categories.

Reply with JSON only:
{{"category": "...", "priority": "P3", "requires_it_action": false,
  "confidence": 0.0, "reason": "one short sentence"}}

Never use em dashes."""


def classify(state: TriageState) -> dict:
    raw = get_provider().chat(CLASSIFIER_SYSTEM, _ticket_text(state), json_mode=True)
    try:
        result = parse_json_response(raw)
    except Exception:
        result = {}

    category = str(result.get("category", "")).strip().lower()
    if category not in taxonomy.CATEGORIES:
        category = "service-management"

    priority = str(result.get("priority", "P3")).strip().upper()
    if priority not in taxonomy.PRIORITIES:
        priority = "P3"

    try:
        confidence = float(result.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    confidence = min(max(confidence, 0.0), 1.0)

    requires_action = bool(result.get("requires_it_action", False))

    return {
        "category": category,
        "priority": priority,
        "confidence": confidence,
        "requires_it_action": requires_action,
        "trace": _trace(
            "classify",
            category=category,
            priority=priority,
            confidence=confidence,
            requires_it_action=requires_action,
            reason=str(result.get("reason", ""))[:300],
        ),
    }


# ---------------------------------------------------------------------------
# Sub-agent 2: knowledge, grounded in the RAG service
# ---------------------------------------------------------------------------

def knowledge(state: TriageState) -> dict:
    question = _ticket_text(state)
    result = knowledge_tool(question)

    citations = getattr(result, "_remote_citations", None) or result.citations
    retrieved_owner = ""
    if result.chunks:
        # The owner of the top reranked chunk is the best routing signal we have.
        retrieved_owner = result.chunks[0].owner

    return {
        "knowledge_answer": result.text,
        "knowledge_covered": bool(result.covered),
        "citations": citations,
        "retrieved_owner": retrieved_owner,
        "trace": _trace(
            "knowledge",
            covered=bool(result.covered),
            sources=[c["document"] for c in citations][:5],
            retrieved_owner=retrieved_owner,
        ),
    }


# ---------------------------------------------------------------------------
# Sub-agent 3: asset lookup and reply drafting
# ---------------------------------------------------------------------------

def asset(state: TriageState) -> dict:
    record = asset_tool(state.get("requester_email", ""))
    summary = summarise_asset(record)
    return {
        "asset_found": record is not None,
        "asset_record": record or {},
        "asset_summary": summary,
        "trace": _trace("asset", found=record is not None, asset_tag=(record or {}).get("asset_tag")),
    }


DRAFTER_SYSTEM = """You draft the reply a service desk agent will send to the
person who raised an IT ticket.

Rules:
1. Use only the evidence provided. If the knowledge extract says NOT_COVERED,
   do not answer the question from your own knowledge. Instead write a short
   holding reply saying the ticket has been passed to the named team.
2. Quote figures exactly as the evidence gives them.
3. Write to the person, not about them. Plain language, no internal jargon,
   no ticket system field names.
4. Three short paragraphs at most. Lead with the answer or the action.
5. Do not promise a timescale unless the evidence states one.
6. No greeting line with a name you were not given. Start with "Hello," and
   sign off with "IT Service Desk".
7. Never use em dashes.

Reply with the message body only."""


def draft(state: TriageState) -> dict:
    evidence_parts = []
    if state.get("knowledge_answer"):
        evidence_parts.append(
            f"Knowledge extract (covered={state.get('knowledge_covered')}):\n"
            f"{state['knowledge_answer']}"
        )
    if state.get("asset_summary"):
        evidence_parts.append(f"Asset record:\n{state['asset_summary']}")
    evidence = "\n\n".join(evidence_parts) or "No evidence was retrieved."

    queue = taxonomy.resolve_queue(
        state.get("category", ""), state.get("retrieved_owner") or None
    )

    prompt = (
        f"{_ticket_text(state)}\n\n"
        f"Evidence:\n{evidence}\n\n"
        f"This ticket is routed to: {queue}\n\n"
        f"Draft the reply."
    )
    reply = get_provider().chat(DRAFTER_SYSTEM, prompt).strip()

    grounded = bool(state.get("knowledge_covered")) or bool(state.get("asset_found"))
    confidence = float(state.get("confidence", 0.0))
    requires_action = bool(state.get("requires_it_action", False))
    category = state.get("category", "")
    priority = state.get("priority", "P3")

    reasons = []
    if not grounded:
        reasons.append("no grounded evidence was retrieved")
    if confidence < taxonomy.AUTO_RESOLVE_CONFIDENCE_FLOOR:
        reasons.append(f"classifier confidence {confidence:.2f} is below the floor")
    if requires_action:
        reasons.append("the ticket requires IT to perform an action")
    if category in taxonomy.NEVER_AUTO_RESOLVE_CATEGORIES:
        reasons.append(f"category '{category}' always needs a human reader")
    if priority in taxonomy.NEVER_AUTO_RESOLVE_PRIORITIES:
        reasons.append(f"priority {priority} always needs a human reader")

    auto_resolvable = not reasons

    return {
        "queue": queue,
        "draft_reply": reply,
        "auto_resolvable": auto_resolvable,
        "hold_reason": "; ".join(reasons),
        "trace": _trace(
            "draft",
            queue=queue,
            auto_resolvable=auto_resolvable,
            hold_reason="; ".join(reasons),
        ),
    }
