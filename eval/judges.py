"""Language-model judges used by the evaluation.

Two judges, kept separate on purpose, because they fail differently:

  faithfulness  Is every claim in the answer supported by the context the
                system actually retrieved? This catches the dangerous failure:
                a fluent answer that the corpus does not support.

  correctness   Does the answer convey the reference answer? This catches the
                ordinary failure: retrieval found the wrong thing.

An answer can be faithful and wrong (it correctly reports an irrelevant
passage) or unfaithful and right (it guessed the right number from training
data). Reporting one number would hide both cases, so both are reported.

The judge runs at temperature 0 and sees only what it needs. It is not a
perfect oracle: spot-check a sample by hand before you quote the figure
anywhere that matters.
"""

from __future__ import annotations

from shared.config import settings
from shared.providers import get_provider, parse_json_response

FAITHFULNESS_SYSTEM = """You check whether an answer is supported by its sources.

You are given CONTEXT (the passages the system retrieved) and an ANSWER.

Decide whether every factual claim in the ANSWER is supported by the CONTEXT.
A claim is unsupported if the context does not state it, even if you believe it
is true in general. Numbers must match the context exactly to count as
supported. Ignore citation markers like [2] when judging wording.

If the answer is exactly NOT_COVERED, treat it as faithful: declining to answer
invents nothing.

Reply with JSON only:
{"faithful": true, "unsupported_claims": []}

Never use em dashes."""

CORRECTNESS_SYSTEM = """You check whether an answer matches a reference answer.

You are given a QUESTION, a REFERENCE answer known to be correct, and an
ANSWER produced by a system.

Judge whether the ANSWER conveys the substance of the REFERENCE. Wording may
differ freely. Extra correct detail is fine. The answer is incorrect if it
states a different figure, omits the key figure or step the reference turns on,
contradicts the reference, or declines to answer when the reference has one.

Reply with JSON only:
{"correct": true, "reason": "one short sentence"}

Never use em dashes."""


def judges_available() -> bool:
    """The fake provider cannot judge anything. Say so rather than emit noise."""
    return settings.provider != "fake"


def judge_faithfulness(context: str, answer: str) -> tuple[bool, list[str]]:
    raw = get_provider().chat(
        FAITHFULNESS_SYSTEM,
        f"CONTEXT:\n{context}\n\nANSWER:\n{answer}",
        json_mode=True,
    )
    try:
        result = parse_json_response(raw)
    except Exception:
        return False, ["judge output unreadable"]
    claims = result.get("unsupported_claims") or []
    if not isinstance(claims, list):
        claims = [str(claims)]
    return bool(result.get("faithful", False)), [str(c) for c in claims][:5]


def judge_correctness(question: str, reference: str, answer: str) -> tuple[bool, str]:
    raw = get_provider().chat(
        CORRECTNESS_SYSTEM,
        f"QUESTION:\n{question}\n\nREFERENCE:\n{reference}\n\nANSWER:\n{answer}",
        json_mode=True,
    )
    try:
        result = parse_json_response(raw)
    except Exception:
        return False, "judge output unreadable"
    return bool(result.get("correct", False)), str(result.get("reason", ""))[:200]
