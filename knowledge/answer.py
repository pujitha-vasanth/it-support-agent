"""Turn retrieved chunks into a grounded, cited answer.

This module is the knowledge service proper. The FastAPI route and the agent's
knowledge tool both call `answer_question`, so there is one code path and one
prompt to maintain rather than two that drift apart.

The prompt does three things that matter:
  1. It numbers the sources and requires inline [n] markers, so a citation can
     be checked rather than taken on trust.
  2. It forbids outside knowledge. A model that answers a policy question from
     its own training data is worse than useless here, because it will be
     confidently wrong about this company's specific numbers.
  3. It requires an explicit "not covered" response, which is what makes the
     agent's escalation path work. Without it the model invents something
     plausible and the ticket gets auto-resolved wrongly.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from knowledge.retrieval import RetrievedChunk, search
from shared.providers import get_provider

NOT_COVERED = "NOT_COVERED"

SYSTEM_PROMPT = """You are the IT knowledge assistant for Meridian Group.

You answer strictly from the numbered sources provided. Follow these rules:

1. Use only the sources. Never use outside knowledge about how VPNs, Windows,
   Intune or any other product normally works. This company's documented
   figures override anything you have seen elsewhere.
2. Cite every factual claim with the source number in square brackets, like
   [2]. A sentence stating a figure, a threshold or a step must carry a marker.
3. Quote specific figures exactly as the sources give them. Do not round,
   convert units, or summarise a number into a vaguer phrase.
4. If the sources do not contain the answer, reply with exactly NOT_COVERED and
   nothing else. Do not guess, and do not offer a general best practice answer
   as a substitute.
5. Be brief and practical. A service desk agent is reading this mid-call.
   Give the answer first, then the steps if there are any.
6. Never use em dashes."""


@dataclass
class Answer:
    question: str
    text: str
    chunks: list[RetrievedChunk] = field(default_factory=list)
    covered: bool = True

    @property
    def citations(self) -> list[dict]:
        return [
            {
                "n": i,
                "document": c.title,
                "section": c.section,
                "page": c.page_approx,
                "source_path": c.source_path,
            }
            for i, c in enumerate(self.chunks, start=1)
        ]

    @property
    def documents_used(self) -> list[str]:
        seen: list[str] = []
        for c in self.chunks:
            if c.source_path not in seen:
                seen.append(c.source_path)
        return seen

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.text,
            "covered": self.covered,
            "citations": self.citations,
        }


def build_context(chunks: list[RetrievedChunk]) -> str:
    blocks = []
    for i, chunk in enumerate(chunks, start=1):
        blocks.append(
            f"[{i}] Document: {chunk.title}\n"
            f"    Section: {chunk.section} (page {chunk.page_approx})\n"
            f"{chunk.body}"
        )
    return "\n\n".join(blocks)


def answer_question(question: str, top_k: int | None = None) -> Answer:
    chunks = search(question, top_k=top_k)
    if not chunks:
        return Answer(question=question, text=NOT_COVERED, chunks=[], covered=False)

    context = build_context(chunks)
    user_prompt = (
        f"Sources:\n\n{context}\n\n"
        f"Question: {question}\n\n"
        f"Answer using only the sources above, with [n] citations."
    )
    raw = get_provider().chat(SYSTEM_PROMPT, user_prompt).strip()
    covered = NOT_COVERED not in raw.upper()

    return Answer(question=question, text=raw, chunks=chunks, covered=covered)
