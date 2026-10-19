"""Build the corpus, the golden question set, the ticket set and the asset
inventory from data/topics.py.

Run with:  python -m data.generate

Everything is deterministic: the same fact base always produces the same
corpus and the same evaluation sets, so an eval score moves only when the
system changes, never because the data shifted underneath it.
"""

from __future__ import annotations

import csv
import json
import random
import re
from pathlib import Path

from data import prose
from data.topics import COMPANY, DOMAIN, PORTAL, SERVICE_DESK, TOPICS

DATA_DIR = Path(__file__).resolve().parent
CORPUS_DIR = DATA_DIR / "corpus"
WORDS_PER_PAGE = 450

FIRST_NAMES = [
    "amara", "rohan", "elena", "tobias", "priya", "marcus", "nadia", "finn",
    "yusuf", "clara", "dmitri", "leila", "oscar", "ingrid", "samir", "beatrix",
    "kwame", "hana", "lucas", "mira", "arjun", "sofia", "tariq", "noor",
    "viktor", "imogen", "paulo", "renu", "jonas", "aisha",
]
LAST_NAMES = [
    "okafor", "mehta", "vasquez", "lindqvist", "chaudhry", "bell", "haddad",
    "oconnell", "demir", "novak", "sorensen", "farouk", "whitfield", "kaur",
    "moreau", "bergmann", "santos", "iyer", "kowalski", "nakamura",
]
DEVICE_MODELS = [
    ("laptop", "Dell Latitude 7450", "Windows 11 23H2"),
    ("laptop", "Dell Latitude 7440", "Windows 11 22H2"),
    ("laptop", "MacBook Pro 14 M3", "macOS 14.6"),
    ("laptop", "MacBook Air 13 M2", "macOS 13.6"),
    ("desktop", "Dell OptiPlex 7010", "Windows 11 23H2"),
    ("laptop", "Lenovo ThinkPad T14 Gen 4", "Windows 11 23H2"),
    ("tablet", "iPad Air 11 M2", "iPadOS 17.5"),
    ("phone", "iPhone 15", "iOS 17.5"),
    ("phone", "Samsung Galaxy S24", "Android 14"),
]
LOCATIONS = ["London HQ", "Manchester", "Dublin", "Rotterdam", "Singapore", "Remote"]
SOFTWARE_SETS = [
    "Microsoft 365, Slack, Zoom",
    "Microsoft 365, Slack, Salesforce",
    "Microsoft 365, SAP GUI, Power BI",
    "Microsoft 365, Zoom, Adobe Acrobat",
    "Microsoft 365, Slack, Zoom, Visual Studio Code",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def subject_of(topic: dict) -> str:
    """A natural-language noun phrase for the thing the document governs."""
    title = topic["title"]
    for suffix in (" Policy", " Runbook", " Services Runbook"):
        if title.endswith(suffix):
            title = title[: -len(suffix)]
            break
    # Keep acronyms (VPN, MFA, SSO, VDI, BYOD, CRM, ERP) in capitals.
    words = [w if (w.isupper() and len(w) > 1) else w.lower() for w in title.split()]
    return " ".join(words)


def fmt(text: str, topic: dict) -> str:
    return text.format(
        company=COMPANY,
        owner=topic["owner"],
        system=topic["system"],
        category=topic["category"],
        subject=subject_of(topic),
        portal=PORTAL,
        service_desk=SERVICE_DESK,
        hours="08:00 to 18:00",
    )


def slugless(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# ---------------------------------------------------------------------------
# Document sections
# ---------------------------------------------------------------------------

def _purpose(topic: dict, rng: random.Random) -> str:
    paras = [fmt(p, topic) for p in prose.PURPOSE]
    scope = " ".join(fmt(s, topic) for s in prose.SCOPE_IN)
    return "\n\n".join(paras) + "\n\n" + scope


def _definitions(topic: dict, rng: random.Random) -> str:
    lines = []
    for term, meaning in topic["definitions"]:
        lines.append(
            f"**{term}**  \n{meaning[0].upper()}{meaning[1:]}. The term is used "
            f"consistently in this sense throughout {COMPANY} documentation, and "
            f"agents should use it rather than a local synonym when writing up a ticket."
        )
    lines.append(
        f"**Service owner**  \nThe team accountable for the availability and "
        f"correctness of the service, in this case {topic['owner']}. The service "
        f"owner approves changes to the parameters in this document."
    )
    lines.append(
        f"**Exception**  \nA time-bound, written agreement that a specific control "
        f"in this document will not apply to a named system or user, approved by "
        f"Information Security and recorded in the exception register."
    )
    return "\n\n".join(lines)


def _roles(topic: dict, rng: random.Random) -> str:
    return "\n\n".join(fmt(r, topic) for r in prose.ROLES)


def _principles(topic: dict, rng: random.Random) -> str:
    out = []
    intros = rng.sample(prose.PRINCIPLE_INTROS, k=len(topic["policy_statements"]))
    tails = [rng.choice(prose.PRINCIPLE_TAILS) for _ in topic["policy_statements"]]
    for i, (statement, intro, tail) in enumerate(
        zip(topic["policy_statements"], intros, tails), start=1
    ):
        out.append(
            f"### {i}. {statement}\n\n"
            f"{intro} {_expand_statement(statement, topic, rng)} "
            f"{fmt(tail, topic)}"
        )
    return "\n\n".join(out)


def _expand_statement(statement: str, topic: dict, rng: random.Random) -> str:
    owner, system = topic["owner"], topic["system"]
    variants = [
        f"{owner} configures {system} to enforce this wherever the platform exposes "
        f"the setting, and audits the remainder by sampling. The service desk does "
        f"not have the authority to waive it on a user's request.",

        f"A user who believes this control blocks legitimate work should raise the "
        f"case through {PORTAL} with their line manager copied in. {owner} will "
        f"either confirm the control applies or sponsor an exception, usually within "
        f"a few working days.",

        f"Evidence that the control is operating is collected automatically from "
        f"{system} and retained for audit. Agents do not need to collect it manually "
        f"unless the automated report has gaps.",

        f"This statement has been tested against the current configuration of "
        f"{system}. Where a platform change makes it unenforceable, {owner} raises a "
        f"risk acceptance rather than quietly dropping the control.",
    ]
    return rng.choice(variants)


def _parameters(topic: dict, rng: random.Random) -> str:
    rows = ["| Parameter | Value |", "| --- | --- |"]
    for label, value in topic["facts"]:
        rows.append(f"| {label[0].upper()}{label[1:]} | {value} |")

    detail = []
    for label, value in topic["facts"]:
        detail.append(
            f"**{label[0].upper()}{label[1:]}.** The {label} is {value}. "
            + rng.choice(
                [
                    f"This is configured centrally in {topic['system']} and is not "
                    f"adjustable per user or per team.",
                    f"{topic['owner']} set this figure in consultation with "
                    f"Information Security, and it is reviewed annually.",
                    f"Agents should quote this figure directly to users rather than "
                    f"estimating, because an incorrect estimate generates a repeat contact.",
                    f"Where a user asks for a different figure, the answer is the "
                    f"exception process described later in this document.",
                ]
            )
        )

    return (
        fmt(prose.PARAM_INTRO, topic)
        + "\n\n"
        + "\n".join(rows)
        + "\n\n"
        + "\n\n".join(detail)
        + "\n\n"
        + " ".join(fmt(t, topic) for t in prose.PARAM_TAIL)
    )


def _procedures(topic: dict, rng: random.Random) -> str:
    out = [fmt(prose.PROC_INTRO, topic)]
    for proc in topic["procedures"]:
        steps = "\n".join(f"{i}. {s}" for i, s in enumerate(proc["steps"], start=1))
        out.append(
            f"### {proc['name']}\n\n"
            f"This procedure is carried out by the service desk unless a step says "
            f"otherwise. Before starting, confirm the requester is who they say they "
            f"are and that a ticket exists.\n\n"
            f"{steps}\n\n"
            f"{fmt(rng.choice(prose.PROC_NOTES), topic)}"
        )
    return "\n\n".join(out)


def _troubleshooting(topic: dict, rng: random.Random) -> str:
    out = [fmt(prose.TROUBLE_INTRO, topic)]
    for entry in topic["troubleshooting"]:
        code = entry.get("error_code") or ""
        code_line = f"\n\n**Error code:** {code}" if code else ""
        out.append(
            f"### Symptom: {entry['symptom']}\n"
            f"{code_line}\n\n"
            f"**Cause.** {entry['cause']}.\n\n"
            f"**Resolution.** {entry['resolution']}\n\n"
            f"**Before escalating.** Capture the device name, the signed-in account, "
            f"the exact time of the failure and any on-screen message. "
            f"{fmt(rng.choice(prose.TROUBLE_TAILS), topic)}"
        )
    return "\n\n".join(out)


def _worked_examples(topic: dict, rng: random.Random) -> str:
    examples = []
    for entry in topic["troubleshooting"][:3]:
        requester = f"{rng.choice(FIRST_NAMES)}.{rng.choice(LAST_NAMES)}@{DOMAIN}"
        examples.append(
            f"### Example: {entry['symptom'][:70]}\n\n"
            f"A user at {rng.choice(LOCATIONS)} contacts the service desk reporting "
            f"that {entry['symptom'][0].lower()}{entry['symptom'][1:]}. The agent "
            f"confirms the identity of the requester, checks whether anyone else has "
            f"reported the same symptom in the last hour, and finds no cluster.\n\n"
            f"The agent recognises the pattern: {entry['cause']}. Following the "
            f"documented resolution, {entry['resolution'][0].lower()}"
            f"{entry['resolution'][1:]}\n\n"
            f"The agent records the diagnosis against the ticket, confirms with "
            f"{requester} that the problem is resolved, and closes the ticket within "
            f"the service level target. No escalation to {topic['owner']} was needed."
        )
    proc = topic["procedures"][0]
    examples.append(
        f"### Example: {proc['name'].lower()}\n\n"
        f"A line manager raises a request through {PORTAL}. The agent checks the "
        f"request carries the approvals this document requires, then works through "
        f"the documented steps in order, recording the ticket reference against each "
        f"step that changes a production configuration.\n\n"
        f"The most common reason this procedure stalls is a missing approval rather "
        f"than a technical fault. Agents should check that first rather than opening "
        f"a vendor case. Once complete, the agent confirms the outcome with the "
        f"requester and closes the ticket."
    )
    return "\n\n".join(examples)


def _architecture(topic: dict, rng: random.Random) -> str:
    return (
        f"{topic['system']} is the system of record for this service. It integrates "
        f"with the corporate directory for identity, with the service management "
        f"platform for ticketing, and with the logging platform for audit. A failure "
        f"in any of those three dependencies will present to users as a failure of "
        f"this service, so agents should check dependency status before diagnosing "
        f"an individual fault.\n\n"
        f"Changes to {topic['system']} follow the change management policy. Standard "
        f"changes are pre-approved and can be applied inside the normal maintenance "
        f"window. Anything that alters a parameter published in this document is a "
        f"normal change and requires review, because the published figure and the "
        f"running configuration must not diverge.\n\n"
        f"{topic['owner']} maintains a runbook for recovering the service after a "
        f"platform outage. That runbook is held separately because it contains "
        f"credentials references and is restricted to the on-call rota. The service "
        f"desk does not need it; during a platform outage the service desk follows "
        f"the major incident communications process instead.\n\n"
        f"Capacity for this service is reviewed monthly against the parameters above. "
        f"Where usage is trending towards a published limit, {topic['owner']} raises "
        f"the increase through change management ahead of the limit being reached, "
        f"rather than waiting for users to hit it. Capacity requests raised "
        f"reactively, after a limit has already been reached, are treated as "
        f"incidents rather than changes, and are reported as such in the monthly "
        f"service review so that the underlying planning gap stays visible."
    )


def _metrics(topic: dict, rng: random.Random) -> str:
    return (
        f"The following measures are reported monthly to the technology leadership "
        f"team for this service.\n\n"
        f"- Volume of contacts to the service desk relating to {subject_of(topic)}, "
        f"split by the troubleshooting categories in this document.\n"
        f"- Proportion resolved at first line without escalation to {topic['owner']}.\n"
        f"- Mean time to resolve, measured against the priority assigned at the point "
        f"the ticket was raised.\n"
        f"- Number of open exceptions against the controls in this document, and the "
        f"age of the oldest.\n"
        f"- Count of configuration drift findings, meaning cases where the running "
        f"state of {topic['system']} did not match the published parameters.\n\n"
        f"A sustained rise in first line contact volume for a single symptom is "
        f"treated as a signal that either the control is poorly understood or the "
        f"user guidance is wrong. In either case the remedy is to fix the "
        f"documentation rather than to absorb the contact volume indefinitely.\n\n"
        f"Where a measure misses target for two consecutive months, {topic['owner']} "
        f"produces an improvement plan with named actions and dates, and reports "
        f"progress at the quarterly service review."
    )


def _faqs(topic: dict, rng: random.Random) -> str:
    body = "\n\n".join(f"**{q}**\n\n{a}" for q, a in topic["faqs"])
    tail = (
        f"**Who do I contact if my question is not answered here?**\n\n"
        f"Raise a ticket through {PORTAL} or email {SERVICE_DESK}. Include the "
        f"system you were using, what you expected to happen, and what actually "
        f"happened. If a question comes up often enough to be worth answering "
        f"here, {topic['owner']} will add it at the next review of this document.\n\n"
        f"**Can the service desk make an exception for me?**\n\n"
        f"No. The service desk operates the controls in this document but does not "
        f"own them. Exceptions are requested in writing, carry a named business "
        f"owner and an end date, and are approved by Information Security. An agent "
        f"who agrees an informal variation creates a finding at the next audit, so "
        f"please do not ask them to."
    )
    return body + "\n\n" + tail


def _escalation(topic: dict, rng: random.Random) -> str:
    return "\n\n".join(fmt(e, topic) for e in prose.ESCALATION)


def _compliance(topic: dict, rng: random.Random) -> str:
    return "\n\n".join(fmt(c, topic) for c in prose.COMPLIANCE)


def _appendices(topic: dict, rng: random.Random) -> str:
    agent_checks = "\n".join(
        f"- [ ] {s}" for proc in topic["procedures"] for s in proc["steps"][:2]
    )
    user_lines = "\n".join(f"- {q} {a}" for q, a in topic["faqs"])
    return (
        f"### Appendix A: service desk checklist\n\n"
        f"Use this when handling a contact about {subject_of(topic)}. It is a "
        f"shortened form of the procedures above and is not a substitute for them.\n\n"
        f"- [ ] Confirm the identity of the requester.\n"
        f"- [ ] Confirm a ticket exists and is in the correct queue.\n"
        f"- [ ] Check whether the symptom matches a known entry in the "
        f"troubleshooting section.\n"
        f"{agent_checks}\n"
        f"- [ ] Record the outcome and confirm resolution with the user before closing.\n\n"
        f"### Appendix B: user-facing guidance\n\n"
        f"The text below can be pasted into a reply to a user without modification. "
        f"It has been reviewed for tone and for accuracy against the parameters in "
        f"this document.\n\n"
        f"{user_lines}\n\n"
        f"### Appendix C: related documents\n\n"
        + "\n".join(f"- {r}" for r in prose.RELATED if r != topic["title"])
        + f"\n\n### Appendix D: revision history\n\n"
        f"| Version | Date | Author | Change |\n| --- | --- | --- | --- |\n"
        f"| 1.0 | 2024-03-11 | {topic['owner']} | First published version. |\n"
        f"| 1.1 | 2024-11-02 | {topic['owner']} | Parameters reviewed, no change to control intent. |\n"
        f"| 2.0 | 2025-06-18 | {topic['owner']} | Restructured to the standard template; "
        f"troubleshooting section added. |\n"
        f"| 2.1 | 2026-02-09 | {topic['owner']} | Annual review; figures confirmed "
        f"against the running configuration of {topic['system']}. |"
    )



def _diagnostics(topic: dict, rng: random.Random) -> str:
    """Per-symptom diagnostic steps. Written separately from the resolution so
    an agent can gather evidence before changing anything."""
    blocks = [
        f"Diagnostics are gathered before any change is made. The sequence below "
        f"produces enough evidence for {topic['owner']} to take an escalation "
        f"without coming back for more detail, which is the usual reason an "
        f"escalated ticket bounces."
    ]
    for entry in topic["troubleshooting"]:
        code = entry.get("error_code") or "no code reported"
        blocks.append(
            f"### Diagnostics for: {entry['symptom'][:70]}\n\n"
            f"Reference: {code}.\n\n"
            f"1. Record the exact time of the failure and the time zone the user is in.\n"
            f"2. Capture the device name, serial or asset tag, and the signed-in account.\n"
            f"3. Confirm whether the symptom reproduces on a second device for the "
            f"same user, and on the same device for a second user. That pair of "
            f"checks separates an account problem from a device problem faster than "
            f"anything else.\n"
            f"4. Check the status of {topic['system']} and its directory and logging "
            f"dependencies before treating this as an individual fault.\n"
            f"5. Collect the relevant log bundle and attach it to the ticket rather "
            f"than pasting fragments into the ticket notes.\n\n"
            f"If all five checks are clean and the symptom persists, escalate to "
            f"{topic['owner']} citing the reference above."
        )
    return "\n\n".join(blocks)


def _misconceptions(topic: dict, rng: random.Random) -> str:
    facts = topic["facts"]
    lines = [
        f"The following come up repeatedly in contacts about {subject_of(topic)}. "
        f"Correcting them early in a conversation shortens the call and reduces "
        f"repeat contacts."
    ]
    for label, value in facts[:4]:
        lines.append(
            f"**Misconception: the {label} is flexible or negotiable per user.**\n\n"
            f"It is not. The {label} is {value}, it is set centrally, and the "
            f"service desk cannot vary it. A user who needs a different figure "
            f"should be directed to the exception process rather than being told "
            f"that it might be possible. Setting that expectation accurately at "
            f"first contact is the difference between one ticket and three."
        )
    lines.append(
        f"**Misconception: {topic['owner']} can be asked directly over chat.**\n\n"
        f"Work requested outside a ticket is invisible to reporting, does not "
        f"accrue against a service level target, and cannot be audited. Agents "
        f"should route the request through {PORTAL} even when they have a direct "
        f"line to the engineer concerned."
    )
    return "\n\n".join(lines)


def _interfaces(topic: dict, rng: random.Random) -> str:
    return (
        f"This service does not operate in isolation, and several common faults "
        f"are actually faults in an adjacent service presenting here.\n\n"
        f"**Identity.** Account state, group membership and multi-factor "
        f"registration all originate in the identity platform. If a user cannot "
        f"authenticate to {topic['system']}, confirm the account is enabled and "
        f"the required group membership is present before investigating further.\n\n"
        f"**Endpoint management.** Device compliance state, patch level and "
        f"encryption status are owned by End User Computing. Where a control in "
        f"this document depends on device posture, the authoritative source is "
        f"the endpoint management console, not what the user reports.\n\n"
        f"**Networking.** Connectivity, name resolution and certificate "
        f"distribution are owned by Network Operations. A symptom that affects "
        f"one office and not another is almost always a network matter.\n\n"
        f"**Service management.** Ticket routing, priority assignment and service "
        f"level measurement are owned by the Service Management Office. Queue "
        f"names referenced in this document are maintained there, and a queue "
        f"rename is a change that must be reflected in this document.\n\n"
        f"**Information Security.** Risk thresholds, exception approval and "
        f"incident declaration sit with Information Security. {topic['owner']} "
        f"implements the thresholds but does not set them."
    )


def _risk(topic: dict, rng: random.Random) -> str:
    return (
        f"The controls in this document address a small number of specific risks. "
        f"Stating them makes it easier to judge an exception request on its merits "
        f"rather than on how urgently it is asked for.\n\n"
        f"**Unauthorised access to corporate data.** The access controls and "
        f"approval routes described above exist to make sure that access is "
        f"granted deliberately, by someone accountable, and removed when it is no "
        f"longer needed. An exception that removes the approval step does not "
        f"reduce this risk, it transfers it.\n\n"
        f"**Loss of availability.** The parameters in this document are chosen so "
        f"that the service stays within its supported operating envelope. Raising "
        f"a published limit for one team without a capacity review moves the risk "
        f"to every other user of the service.\n\n"
        f"**Inability to demonstrate control.** Several requirements here exist "
        f"because the control must be evidenced to an auditor, not only operated. "
        f"Work done outside a ticket may be perfectly correct and still fail an "
        f"audit, because there is nothing to sample.\n\n"
        f"**Configuration drift.** Where the running state of {topic['system']} "
        f"diverges from the parameters published here, users receive inconsistent "
        f"answers and the service desk loses credibility. Drift is tracked as a "
        f"defect with a named owner, not as an acceptable variation.\n\n"
        f"Residual risk after these controls is accepted by the service owner, "
        f"{topic['owner']}, and reviewed annually with Information Security."
    )


def _training(topic: dict, rng: random.Random) -> str:
    return (
        f"Service desk agents are expected to be competent in the procedures and "
        f"troubleshooting entries in this document before taking contacts about "
        f"{subject_of(topic)} unsupervised.\n\n"
        f"Competency is demonstrated by working through the procedures with an "
        f"experienced colleague, handling a small number of live contacts under "
        f"observation, and being able to quote the service parameters without "
        f"looking them up. The last of those matters more than it sounds: an "
        f"agent who hesitates on a published figure invites the user to negotiate "
        f"it.\n\n"
        f"{topic['owner']} runs a refresher whenever a parameter changes, whenever "
        f"a new troubleshooting entry is added, and at least once a year. "
        f"Attendance is recorded against the agent's training record.\n\n"
        f"New entries are added to the troubleshooting section when a symptom has "
        f"been seen three times and the resolution is stable. Adding an entry "
        f"after the first occurrence tends to enshrine a workaround that later "
        f"turns out to be wrong."
    )


SECTIONS = [
    ("Purpose and scope", _purpose),
    ("Definitions", _definitions),
    ("Roles and responsibilities", _roles),
    ("Operating principles", _principles),
    ("Service parameters", _parameters),
    ("Risk rationale", _risk),
    ("Architecture and dependencies", _architecture),
    ("Interfaces with other services", _interfaces),
    ("Procedures", _procedures),
    ("Troubleshooting", _troubleshooting),
    ("Diagnostics", _diagnostics),
    ("Worked examples", _worked_examples),
    ("Common misconceptions", _misconceptions),
    ("Measurement and reporting", _metrics),
    ("Training and competency", _training),
    ("Frequently asked questions", _faqs),
    ("Escalation", _escalation),
    ("Compliance, exceptions and audit", _compliance),
    ("Appendices", _appendices),
]


def build_document(topic: dict) -> str:
    rng = random.Random(topic["slug"])
    parts = [
        "---",
        f"title: {topic['title']}",
        f"doc_type: {topic['doc_type']}",
        f"category: {topic['category']}",
        f"owner: {topic['owner']}",
        "version: 2.1",
        "review_date: 2027-02-09",
        "---",
        "",
        f"# {topic['title']}",
        "",
        f"Owner: {topic['owner']} | System of record: {topic['system']} | "
        f"Classification: Internal",
        "",
    ]
    for heading, builder in SECTIONS:
        parts.append(f"## {heading}")
        parts.append("")
        parts.append(builder(topic, rng))
        parts.append("")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Asset inventory
# ---------------------------------------------------------------------------

def build_assets(rng: random.Random, count: int = 60) -> list[dict]:
    people: list[tuple[str, str]] = []
    for first in FIRST_NAMES:
        for last in LAST_NAMES:
            people.append((first, last))
    rng.shuffle(people)

    assets = []
    for i in range(count):
        first, last = people[i]
        device_type, model, os_version = DEVICE_MODELS[i % len(DEVICE_MODELS)]
        purchase_year = 2022 + (i % 4)
        purchase_month = (i % 12) + 1
        warranty_years = 3 if device_type in ("laptop", "desktop") else 2
        assets.append(
            {
                "asset_tag": f"MG-{10000 + i}",
                "user_email": f"{first}.{last}@{DOMAIN}",
                "user_name": f"{first.capitalize()} {last.capitalize()}",
                "device_type": device_type,
                "model": model,
                "os_version": os_version,
                "purchase_date": f"{purchase_year}-{purchase_month:02d}-14",
                "warranty_end": f"{purchase_year + warranty_years}-{purchase_month:02d}-13",
                "status": "in service" if i % 11 else "in repair",
                "location": LOCATIONS[i % len(LOCATIONS)],
                "software": SOFTWARE_SETS[i % len(SOFTWARE_SETS)],
            }
        )
    return assets


# ---------------------------------------------------------------------------
# Golden question set
# ---------------------------------------------------------------------------

def _fact_question(topic: dict, label: str, rng: random.Random) -> str:
    subject = subject_of(topic)
    subject_words = {w.lower() for w in subject.split()}
    label_words = {w.lower() for w in label.split()}
    if subject_words & label_words:
        # The label already names its own subject area, so it stands alone.
        return f"What is the {label}?"
    return f"For {subject}, what is the {label}?"


def build_golden_set(rng: random.Random) -> list[dict]:
    items: list[dict] = []

    # 26 fact questions, spread across topics so no topic dominates.
    fact_topics = TOPICS[:26]
    for i, topic in enumerate(fact_topics):
        label, value = topic["facts"][i % len(topic["facts"])]
        items.append(
            {
                "id": f"G{len(items) + 1:03d}",
                "type": "fact",
                "question": _fact_question(topic, label, rng),
                "reference_answer": f"The {label} is {value}.",
                "expected_doc": topic["slug"],
                "expected_section": "Service parameters",
            }
        )

    # 12 troubleshooting questions, half keyed on the error code.
    for i, topic in enumerate(TOPICS[2:14]):
        entry = topic["troubleshooting"][i % len(topic["troubleshooting"])]
        code = entry.get("error_code") or ""
        if code and i % 2 == 0:
            question = f"What does error code {code} mean and how do we resolve it?"
        else:
            question = (
                f"A user reports this: {entry['symptom'][0].lower()}"
                f"{entry['symptom'][1:]}. What is the cause and what should we do?"
            )
        items.append(
            {
                "id": f"G{len(items) + 1:03d}",
                "type": "troubleshooting",
                "question": question,
                "reference_answer": (
                    f"Cause: {entry['cause'].rstrip('.')}. "
                    f"Resolution: {entry['resolution']}"
                ),
                "expected_doc": topic["slug"],
                "expected_section": "Troubleshooting",
            }
        )

    # 12 procedure questions.
    for i, topic in enumerate(TOPICS[14:26]):
        proc = topic["procedures"][i % len(topic["procedures"])]
        items.append(
            {
                "id": f"G{len(items) + 1:03d}",
                "type": "procedure",
                "question": f"What are the steps for {proc['name'][0].lower()}{proc['name'][1:]}?",
                "reference_answer": " ".join(
                    f"{n}. {s}" for n, s in enumerate(proc["steps"], start=1)
                ),
                "expected_doc": topic["slug"],
                "expected_section": "Procedures",
            }
        )

    assert len(items) == 50, f"expected 50 golden questions, built {len(items)}"
    return items


# ---------------------------------------------------------------------------
# Ticket set
# ---------------------------------------------------------------------------

SECURITY_CATEGORIES = {"security"}
OUTAGE_WORDS = ("whole office", "nobody", "everyone", "all users")


def _priority_for(topic: dict, kind: str) -> str:
    if kind == "escalation":
        return "P1"
    if topic and topic["category"] in SECURITY_CATEGORIES:
        return "P2"
    if kind == "request":
        return "P4"
    return "P3"


def _user_voice(symptom: str, rng: random.Random) -> str:
    openers = [
        "Hi, hoping someone can help.",
        "Morning. Having a problem since yesterday.",
        "Hello, this has been going on for a couple of days now.",
        "Hi team, not sure who to send this to.",
        "Raising this as it is blocking me.",
        "Sorry to bother you, quick one.",
    ]
    closers = [
        "I have already tried restarting. Thanks.",
        "Let me know if you need anything from my side.",
        "I am working from home today if that matters.",
        "This is slowing me down quite a bit, any help appreciated.",
        "Happy to jump on a call if that is easier.",
        "No rush but it would be good to get it sorted this week.",
    ]
    return (
        f"{rng.choice(openers)} {symptom[0].upper()}{symptom[1:]}. "
        f"{rng.choice(closers)}"
    )


def build_tickets(assets: list[dict], rng: random.Random) -> list[dict]:
    tickets: list[dict] = []
    emails = [a["user_email"] for a in assets]

    def next_id() -> str:
        return f"T{len(tickets) + 1:03d}"

    # 30 troubleshooting tickets, one per topic.
    for i, topic in enumerate(TOPICS):
        entry = topic["troubleshooting"][i % len(topic["troubleshooting"])]
        tickets.append(
            {
                "ticket_id": next_id(),
                "subject": entry["symptom"][:80],
                "body": _user_voice(entry["symptom"], rng),
                "requester_email": emails[i % len(emails)],
                "expected_category": topic["category"],
                "expected_priority": _priority_for(topic, "incident"),
                "expected_queue": topic["owner"],
                "expected_auto_resolvable": True,
                "expected_doc": topic["slug"],
                "needs_asset_lookup": False,
            }
        )

    # 8 tickets that cannot be answered without the asset inventory.
    asset_templates = [
        ("Is my laptop still under warranty?", "Can you tell me when the warranty on my laptop runs out? I want to know before I report a fault."),
        ("What device am I currently assigned?", "I need the model and asset tag of the machine assigned to me for an expenses form."),
        ("Replacement charger request", "The charger for my assigned laptop has stopped working. Can you send a replacement for the right model?"),
        ("Am I due a refresh?", "My machine is getting slow. Can you check how old it is and whether I am due a refresh yet?"),
        ("Which operating system version am I on?", "Security asked me what OS version my device is running. Can you look it up rather than me hunting for it?"),
        ("Is my device recorded in the right office?", "I moved office last month. Can you check which location my device is registered to?"),
        ("What software is licensed to me?", "Finance are asking which licensed applications are assigned to my account. Can you confirm?"),
        ("My device shows as in repair", "I was told my machine is flagged as in repair but it is sitting on my desk working. Can you check the record?"),
    ]
    for i, (subject, body) in enumerate(asset_templates):
        tickets.append(
            {
                "ticket_id": next_id(),
                "subject": subject,
                "body": body,
                "requester_email": emails[(i * 7) % len(emails)],
                "expected_category": "hardware",
                "expected_priority": "P4",
                "expected_queue": "Desktop Support",
                "expected_auto_resolvable": True,
                "expected_doc": None,
                "needs_asset_lookup": True,
            }
        )

    # 7 service requests that need routing and approval rather than an answer.
    request_topics = [t for t in TOPICS if t["procedures"]][:7]
    for i, topic in enumerate(request_topics):
        proc = topic["procedures"][0]
        tickets.append(
            {
                "ticket_id": next_id(),
                "subject": proc["name"],
                "body": (
                    f"Hi, I need to get this done for a member of my team: "
                    f"{proc['name'][0].lower()}{proc['name'][1:]}. "
                    f"Can you tell me what you need from me to start it, and who has "
                    f"to approve it? They start on the first of next month."
                ),
                "requester_email": emails[(i * 5 + 3) % len(emails)],
                "expected_category": topic["category"],
                "expected_priority": _priority_for(topic, "request"),
                "expected_queue": topic["owner"],
                "expected_auto_resolvable": False,
                "expected_doc": topic["slug"],
                "needs_asset_lookup": False,
            }
        )

    # 5 tickets that must escalate and must not be auto-resolved.
    escalations = [
        ("No internet in the Manchester office", "Nobody in the Manchester office can reach anything. The whole floor is down. This started about twenty minutes ago.", "network", "Network Operations"),
        ("I think I entered my password on a fake site", "I clicked a link in an email that looked like our sign-in page and typed my password before I realised. I am worried.", "security", "Information Security"),
        ("Customer data may have been emailed externally", "A colleague thinks a spreadsheet with customer records went to an external address by mistake this morning.", "security", "Information Security"),
        ("Production database is returning errors to customers", "Our customer portal is throwing errors on checkout and it looks like a database problem. Revenue impacting.", "data", "Data Platform Engineering"),
        ("Several people cannot sign in at all", "At least six people on my team cannot sign in to anything this morning. It is not just me.", "access", "Identity and Access Management"),
    ]
    for i, (subject, body, category, queue) in enumerate(escalations):
        tickets.append(
            {
                "ticket_id": next_id(),
                "subject": subject,
                "body": body,
                "requester_email": emails[(i * 11 + 2) % len(emails)],
                "expected_category": category,
                "expected_priority": "P1",
                "expected_queue": queue,
                "expected_auto_resolvable": False,
                "expected_doc": None,
                "needs_asset_lookup": False,
            }
        )

    assert len(tickets) == 50, f"expected 50 tickets, built {len(tickets)}"
    return tickets


# ---------------------------------------------------------------------------
# Optional: rewrite ticket bodies into natural user voice
# ---------------------------------------------------------------------------

PARAPHRASE_SYSTEM = (
    "You rewrite IT support tickets into the words a real non-technical employee "
    "would use. Keep the underlying problem identical. Remove jargon and product "
    "error codes unless an ordinary user would genuinely have copied them in. Do "
    "not add facts. Do not use em dashes. Reply with the rewritten body only, two "
    "or three sentences."
)


def paraphrase_tickets(tickets: list[dict]) -> list[dict]:
    """Rewrite ticket bodies with the language model so they do not share
    wording with the corpus.

    Worth doing before you quote an evaluation number. Template-generated
    tickets reuse the corpus phrasing, which flatters retrieval: the system
    looks better than it would on real tickets. This costs roughly one cent.
    """
    from shared.providers import get_provider

    provider = get_provider()
    for ticket in tickets:
        rewritten = provider.chat(
            PARAPHRASE_SYSTEM,
            f"Subject: {ticket['subject']}\n\nBody: {ticket['body']}",
        ).strip()
        if rewritten and not rewritten.upper().startswith("FAKE PROVIDER"):
            ticket["body"] = rewritten
            ticket["paraphrased"] = True
    return tickets


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(paraphrase: bool = False) -> None:
    rng = random.Random(20261008)

    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    for stale in CORPUS_DIR.glob("*.md"):
        stale.unlink()

    total_words = 0
    for topic in TOPICS:
        text = build_document(topic)
        total_words += len(text.split())
        (CORPUS_DIR / f"{topic['slug']}.md").write_text(text, encoding="utf-8")

    assets = build_assets(rng)
    with (DATA_DIR / "assets.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(assets[0].keys()))
        writer.writeheader()
        writer.writerows(assets)

    golden = build_golden_set(rng)
    (DATA_DIR / "golden_set.json").write_text(
        json.dumps(golden, indent=2), encoding="utf-8"
    )

    tickets = build_tickets(assets, rng)
    if paraphrase:
        print("Paraphrasing ticket bodies with the language model ...")
        tickets = paraphrase_tickets(tickets)
    (DATA_DIR / "tickets.json").write_text(
        json.dumps(tickets, indent=2), encoding="utf-8"
    )

    print(f"Corpus      : {len(TOPICS)} documents, {total_words:,} words, "
          f"about {total_words // WORDS_PER_PAGE} pages")
    print(f"Assets      : {len(assets)} rows -> data/assets.csv")
    print(f"Golden set  : {len(golden)} questions -> data/golden_set.json")
    print(f"Tickets     : {len(tickets)} tickets -> data/tickets.json"
          + (" (paraphrased)" if paraphrase else ""))
    print("\nNext step: python -m knowledge.ingest")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate the corpus and eval sets.")
    parser.add_argument(
        "--paraphrase",
        action="store_true",
        help="Rewrite ticket bodies with the language model so they do not reuse "
             "corpus wording. Recommended before quoting an eval number.",
    )
    args = parser.parse_args()
    main(paraphrase=args.paraphrase)
