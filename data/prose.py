"""Prose templates used to expand the fact base into full documents.

Real policy documents are substantially boilerplate wrapped around a small
core of specific facts, and this mirrors that. Every template is substituted
with topic-specific values, so no two documents read identically, and every
chunk carries its document title and section heading as a prefix.

The golden question set only ever targets the specific facts, procedures and
troubleshooting entries, never this surrounding prose.
"""

from __future__ import annotations

PURPOSE = [
    "This document sets out how {company} manages {subject}. It applies to every "
    "employee, contractor and third party who uses {company} systems, regardless of "
    "location or working pattern. The {owner} team owns this document and is "
    "accountable for keeping it accurate.",

    "The controls described here exist to keep the {category} estate predictable, "
    "auditable and supportable. Where this document conflicts with a local practice "
    "that has grown up inside a single team, this document takes precedence until a "
    "formal exception has been recorded.",

    "{system} is the primary platform referenced throughout. Any change to that "
    "platform that alters the behaviour described here must be raised through change "
    "management before it is applied, and this document must be updated in the same "
    "change record.",

    "Readers who only need to resolve a specific problem should go straight to the "
    "troubleshooting section. Readers approving a request should read the service "
    "parameters and the procedures that follow them.",
]

SCOPE_IN = [
    "In scope: all managed endpoints, all {company} identities, and all production "
    "instances of {system}.",
    "Also in scope: contractor and temporary accounts, which follow the same rules "
    "with a shorter review interval.",
    "Out of scope: isolated laboratory environments that hold no production data and "
    "have no route to the corporate network. Those are governed separately.",
]

ROLES = [
    "**{owner}** owns the service, maintains this document, and is the escalation "
    "point for anything the service desk cannot resolve within its own authority.",

    "**The Service Desk** is the single point of contact for users. Agents resolve "
    "what falls inside the documented procedures below and escalate anything else to "
    "{owner} rather than improvising a workaround.",

    "**Line managers** approve access and equipment requests for their direct reports "
    "and are responsible for notifying IT of joiners, movers and leavers in good time.",

    "**Information Security** reviews exceptions, sets the risk thresholds referenced "
    "in this document, and may suspend access without notice where there is evidence "
    "of compromise.",

    "**Users** are responsible for following the procedures here, for reporting "
    "problems promptly through {portal} or {service_desk}, and for not attempting to "
    "work around a control they find inconvenient.",

    "**Internal Audit** samples records produced under this document at least once a "
    "year and reports findings to the technology risk committee.",
]

PRINCIPLE_INTROS = [
    "The reasoning behind this is straightforward.",
    "In practice this means the following.",
    "This is enforced technically wherever the platform allows it.",
    "Agents should treat this as non-negotiable.",
    "There is a documented exception route, described later in this document.",
    "This has been the standing position since the last review.",
]

PRINCIPLE_TAILS = [
    "Where the control cannot be enforced technically, {owner} monitors for breaches "
    "and follows up with the individual and their line manager.",

    "Requests to vary this must go through the exception process rather than being "
    "agreed informally with an engineer.",

    "The service desk should record the relevant detail against the ticket so that "
    "the audit trail stands up without anyone needing to reconstruct it later.",

    "Repeated breaches are treated as a line management matter rather than a "
    "technical one, and are reported through the usual route.",

    "{owner} reviews compliance with this statement as part of the quarterly service "
    "review and reports exceptions to Information Security.",
]

PARAM_INTRO = (
    "The parameters below are the operative numbers for this service. They are the "
    "values the service desk should quote to users, and they are what {owner} "
    "configures in {system}. Any value that differs from this table in a running "
    "system is a defect and should be raised as such."
)

PARAM_TAIL = [
    "These values are reviewed at each annual review of this document, and may be "
    "changed sooner if Information Security revises the underlying risk assessment.",
    "Users occasionally ask for these to be relaxed for convenience. The answer is "
    "the exception process, not an informal adjustment by an engineer.",
    "Where a figure here is expressed in business hours, that means {hours} local "
    "time on working days, excluding public holidays in the user's country.",
]

PROC_INTRO = (
    "The procedures in this section are the supported way to carry out common tasks "
    "against this service. Follow them in order. If a step cannot be completed as "
    "written, stop and escalate to {owner} rather than skipping it."
)

PROC_NOTES = [
    "Record the ticket reference against each step that changes a production "
    "configuration, so the change can be traced afterwards.",
    "If the request came in by email or chat rather than through {portal}, raise a "
    "ticket first. Work carried out without a ticket cannot be audited.",
    "Where approval is required, the approval must be captured in the ticket. A "
    "verbal approval is not sufficient on its own.",
    "Expect this to take longer the first time. Agents new to the service should "
    "pair with a colleague for their first few requests.",
]

TROUBLE_INTRO = (
    "This section covers the faults the service desk sees most often against this "
    "service. Each entry gives the symptom as the user is likely to describe it, the "
    "underlying cause, and the resolution. If the symptom matches but the resolution "
    "does not work, escalate to {owner} with the diagnostic output attached rather "
    "than retrying the same steps."
)

TROUBLE_TAILS = [
    "If this recurs for the same user more than twice in a month, raise a problem "
    "record rather than another incident.",
    "Capture the exact wording of any on-screen message before you change anything. "
    "It is frequently the fastest route to the cause.",
    "Confirm with the user that the issue is resolved before closing the ticket. A "
    "ticket closed on assumption usually reopens.",
    "Check whether other users are reporting the same symptom before treating it as "
    "an individual fault. A cluster usually means a platform change.",
]

ESCALATION = [
    "First line is the service desk, reachable through {portal} or {service_desk}. "
    "Agents work to the priority matrix in the service level policy.",

    "Second line is {owner}, engaged through the ticket rather than by direct "
    "message, so that the work remains visible and the clock on the service level "
    "target keeps running against the right queue.",

    "Third line is the vendor for {system}, engaged by {owner} only. The service desk "
    "should not open vendor cases directly, because the entitlement is held centrally "
    "and a duplicate case slows the real one down.",

    "Major incidents follow the security incident response runbook instead of this "
    "escalation path, and are declared by the duty incident manager.",
]

COMPLIANCE = [
    "Records produced under this document are retained for the period set out in the "
    "data classification policy for the relevant tier.",

    "Exceptions must be requested in writing through {portal}, must carry a named "
    "business owner and an end date, and are approved by Information Security. An "
    "exception without an end date will not be approved.",

    "Approved exceptions are logged in the exception register and reviewed at expiry. "
    "A lapsed exception reverts to the standard control automatically.",

    "{owner} produces a compliance report each quarter showing the number of "
    "exceptions open, the number of breaches detected, and the mean time to close.",

    "Where a control in this document cannot be met for a specific system, the "
    "compensating control must be documented in the exception record and reviewed at "
    "the same cadence.",
]

RELATED = [
    "Service Desk Service Level Policy",
    "Data Classification Policy",
    "Change Management Policy",
    "Security Incident Response Runbook",
    "Password and Multi-Factor Authentication Policy",
]
