"""Embedding and chat providers.

Two implementations behind one interface:

  openai  - the real thing, needs OPENAI_API_KEY
  fake    - deterministic, offline, free. Hash-based bag-of-words embeddings
            and a templated chat reply. Lets you prove the database, the
            retrieval SQL and the agent graph all work before spending a cent.

Switch with PROVIDER in .env.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from functools import lru_cache
from typing import Protocol

from shared.config import settings

_WORD_RE = re.compile(r"[a-z0-9]+")


class Provider(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]: ...
    def chat(self, system: str, user: str, json_mode: bool = False) -> str: ...


# --------------------------------------------------------------------------
# Fake provider
# --------------------------------------------------------------------------

class FakeProvider:
    """Offline stand-in. Embeddings are hashed term frequencies, which means
    retrieval still behaves sensibly for keyword-ish queries."""

    def __init__(self, dimensions: int) -> None:
        self.dimensions = dimensions

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._embed_one(t) for t in texts]

    def _embed_one(self, text: str) -> list[float]:
        vec = [0.0] * self.dimensions
        for token in _WORD_RE.findall(text.lower()):
            digest = hashlib.md5(token.encode()).digest()
            idx = int.from_bytes(digest[:4], "big") % self.dimensions
            sign = 1.0 if digest[4] % 2 == 0 else -1.0
            vec[idx] += sign
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]

    def chat(self, system: str, user: str, json_mode: bool = False) -> str:
        if json_mode:
            # Enough structure for the triage graph to keep moving offline.
            return json.dumps(
                {
                    "category": "access",
                    "priority": "P3",
                    "queue": "Service Desk",
                    "confidence": 0.5,
                    "needs_knowledge": True,
                    "needs_asset": False,
                    "requires_it_action": False,
                    "auto_resolvable": True,
                    "reason": "fake provider response",
                    "answer": "FAKE PROVIDER: set PROVIDER=openai in .env for a real answer.",
                    "citations": [],
                    "reply": "FAKE PROVIDER: set PROVIDER=openai in .env for a real reply.",
                }
            )
        return (
            "FAKE PROVIDER RESPONSE. The retrieval pipeline ran and returned "
            "context, but no language model was called. Set PROVIDER=openai "
            "in .env to generate a real answer."
        )


# --------------------------------------------------------------------------
# OpenAI provider
# --------------------------------------------------------------------------

class OpenAIProvider:
    def __init__(self) -> None:
        from openai import OpenAI  # imported lazily so `fake` needs no install

        settings.require_api_key()
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.embedding_model = settings.embedding_model
        self.chat_model = settings.chat_model

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Embed in batches. The API accepts many inputs per call, which is
        far cheaper and faster than one call per chunk."""
        out: list[list[float]] = []
        batch_size = 96
        for start in range(0, len(texts), batch_size):
            batch = [t.replace("\n", " ") for t in texts[start : start + batch_size]]
            response = self.client.embeddings.create(
                model=self.embedding_model, input=batch
            )
            out.extend(item.embedding for item in response.data)
        return out

    def chat(self, system: str, user: str, json_mode: bool = False) -> str:
        kwargs: dict = {
            "model": self.chat_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        response = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content or ""


@lru_cache(maxsize=1)
def get_provider() -> Provider:
    if settings.provider == "fake":
        return FakeProvider(settings.embedding_dimensions)
    return OpenAIProvider()


def parse_json_response(raw: str) -> dict:
    """Models occasionally wrap JSON in a code fence. Strip it and parse."""
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        text = re.sub(r"\n```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise
