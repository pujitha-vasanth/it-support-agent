"""Token and cost tracking for one unit of work (one API request, one eval run).

    with track() as usage:
        answer_question("How long does a VPN session last?")
    usage.cost_usd, usage.input_tokens, usage.model_calls

The providers call `record_chat` and `record_embedding` after every model call.
Those land on whichever tracker is active, so no function in between has to
pass usage around. Outside a `track()` block the calls are simply ignored.

Cost is an estimate from the per-million-token prices in .env (PRICE_*). Check
them against the provider's current price list before quoting a figure.
"""

from __future__ import annotations

import threading
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Iterator

from shared.config import settings


@dataclass
class Usage:
    model_calls: int = 0
    embedding_calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    embedding_tokens: int = 0
    cost_usd: float = 0.0
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def to_dict(self) -> dict:
        return {
            "model_calls": self.model_calls,
            "embedding_calls": self.embedding_calls,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "embedding_tokens": self.embedding_tokens,
            "cost_usd": round(self.cost_usd, 6),
        }


# The agent runs some sub-agents in parallel threads. Each thread gets a copy
# of the context, but the copy points at the same Usage object, so every
# thread adds to one total. The lock keeps those additions safe.
_current: ContextVar[Usage | None] = ContextVar("usage", default=None)


@contextmanager
def track() -> Iterator[Usage]:
    usage = Usage()
    token = _current.set(usage)
    try:
        yield usage
    finally:
        _current.reset(token)


def record_chat(input_tokens: int, output_tokens: int) -> None:
    usage = _current.get()
    if usage is None:
        return
    cost = (input_tokens * settings.price_input_per_m
            + output_tokens * settings.price_output_per_m) / 1_000_000
    if settings.provider == "fake":
        cost = 0.0
    with usage._lock:
        usage.model_calls += 1
        usage.input_tokens += input_tokens
        usage.output_tokens += output_tokens
        usage.cost_usd += cost


def record_embedding(tokens: int) -> None:
    usage = _current.get()
    if usage is None:
        return
    cost = tokens * settings.price_embedding_per_m / 1_000_000
    if settings.provider == "fake":
        cost = 0.0
    with usage._lock:
        usage.embedding_calls += 1
        usage.embedding_tokens += tokens
        usage.cost_usd += cost


def rough_tokens(text: str) -> int:
    """About four characters per token in English. Only used by the fake
    provider, which has no tokenizer, so offline runs still show volume."""
    return max(1, len(text) // 4)
