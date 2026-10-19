"""Routing taxonomy for the triage agent.

Categories are the labels the classification sub-agent chooses between.
Queues are the teams a ticket can be routed to.

Queue selection is deliberately NOT left to the language model. There are
twenty queues here and several pairs are not reliably distinguishable from a
ticket alone (Identity Operations against Identity and Access Management, for
instance). Asking a model to pick between them produces a number that looks
like accuracy but is mostly noise.

Instead the queue is resolved in this order:
  1. the owner of the document the knowledge sub-agent actually retrieved,
  2. failing that, the default queue for the predicted category.

That grounds routing in evidence rather than a guess, and it means adding a new
document automatically teaches the agent a new routing destination.

Edit this file to match your own service desk.
"""

from __future__ import annotations

CATEGORIES: list[str] = [
    "access",
    "applications",
    "data",
    "hardware",
    "infrastructure",
    "mobile",
    "network",
    "productivity",
    "security",
    "service-management",
    "software",
    "storage",
    "workplace",
]

DEFAULT_QUEUE_BY_CATEGORY: dict[str, str] = {
    "access": "Identity and Access Management",
    "applications": "Business Applications",
    "data": "Data Platform Engineering",
    "hardware": "Desktop Support",
    "infrastructure": "Infrastructure Services",
    "mobile": "End User Computing",
    "network": "Network Operations",
    "productivity": "Collaboration Services",
    "security": "Information Security",
    "service-management": "Service Management Office",
    "software": "IT Asset Management",
    "storage": "Infrastructure Services",
    "workplace": "Workplace Technology",
}

FALLBACK_QUEUE = "Service Desk"

PRIORITIES: list[str] = ["P1", "P2", "P3", "P4"]

PRIORITY_GUIDE = """
P1  Multiple users or a whole site are unable to work, or a live security
    compromise is suspected, or customer-facing revenue is affected.
P2  A single user is completely blocked with no workaround, or a security
    matter that is contained but needs same-day attention.
P3  A single user is impaired but can still work, or has a workaround.
    Most individual faults are P3.
P4  A request, a question, or anything with no current impact on work.
"""

AUTO_RESOLVE_DEFINITION = """
A ticket is auto-resolvable when the drafted reply fully answers the requester
and no further work is required from IT.

That means all of the following hold:
  - the reply is grounded in retrieved evidence (a cited document, or the
    asset record), not in the model's general knowledge,
  - the classifier's confidence is at or above the floor below,
  - the ticket does not require IT to perform an action, such as provisioning
    an account, ordering hardware, or granting access,
  - the category is not one that always needs a human reader,
  - the priority is not one that always needs a human reader.

Anything else is drafted and held for a human. The draft is still produced,
because a reviewed draft is still most of the work.
"""

# Categories where an automated reply is never sent without a human reading it,
# regardless of how confident the model is.
NEVER_AUTO_RESOLVE_CATEGORIES = {"security"}

# Priorities where the same applies.
NEVER_AUTO_RESOLVE_PRIORITIES = {"P1", "P2"}

AUTO_RESOLVE_CONFIDENCE_FLOOR = 0.6


def resolve_queue(category: str, retrieved_owner: str | None) -> str:
    """Owner of the retrieved document wins, then the category default."""
    if retrieved_owner:
        return retrieved_owner
    return DEFAULT_QUEUE_BY_CATEGORY.get(category, FALLBACK_QUEUE)
