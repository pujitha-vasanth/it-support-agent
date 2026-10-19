"""Single place where every setting is read.

Everything comes from the .env file in the project root. Nothing is hardcoded
in the application modules, so you change behaviour by editing .env only.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CORPUS_DIR = DATA_DIR / "corpus"
EVAL_DIR = PROJECT_ROOT / "eval_results"

load_dotenv(PROJECT_ROOT / ".env")


def _int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return int(raw)


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    embedding_model: str
    embedding_dimensions: int
    chat_model: str
    database_url: str
    vector_top_k: int
    keyword_top_k: int
    rerank_top_k: int
    rerank_model: str
    provider: str

    @property
    def reranking_enabled(self) -> bool:
        return self.rerank_top_k > 0

    def require_api_key(self) -> None:
        """Fail early and clearly instead of deep inside an HTTP call."""
        if self.provider == "fake":
            return
        if not self.openai_api_key or self.openai_api_key.startswith("sk-replace"):
            raise RuntimeError(
                "No OpenAI API key found.\n"
                "  1. Copy .env.example to .env\n"
                "  2. Put your real key in OPENAI_API_KEY\n"
                "Or set PROVIDER=fake in .env to run without a key."
            )


def load_settings() -> Settings:
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        embedding_dimensions=_int("EMBEDDING_DIMENSIONS", 1536),
        chat_model=os.getenv("CHAT_MODEL", "gpt-4o-mini"),
        database_url=os.getenv(
            "DATABASE_URL",
            "postgresql://itsupport:itsupport@localhost:5433/itsupport",
        ),
        vector_top_k=_int("VECTOR_TOP_K", 20),
        keyword_top_k=_int("KEYWORD_TOP_K", 20),
        rerank_top_k=_int("RERANK_TOP_K", 5),
        rerank_model=os.getenv("RERANK_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2"),
        provider=os.getenv("PROVIDER", "openai").strip().lower(),
    )


settings = load_settings()
