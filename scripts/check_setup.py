"""Check everything this project needs, and say plainly what is missing.

    python scripts/check_setup.py

Run this first, and run it again whenever something behaves oddly. It checks
in dependency order and keeps going after a failure so you see the whole
picture rather than one error at a time.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

OK = "  ok   "
BAD = " FAIL  "
WARN = " warn  "

results: list[tuple[str, str, str]] = []


def record(status: str, name: str, detail: str = "") -> None:
    results.append((status, name, detail))
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))


def check_python() -> None:
    version = sys.version_info
    text = f"{version.major}.{version.minor}.{version.micro}"
    if version >= (3, 11):
        record(OK, "Python version", text)
    else:
        record(BAD, "Python version", f"{text}, this project needs 3.11 or newer")


def check_packages() -> None:
    required = {
        "psycopg": "psycopg[binary]",
        "pgvector": "pgvector",
        "dotenv": "python-dotenv",
        "fastapi": "fastapi",
        "langgraph": "langgraph",
    }
    optional = {
        "openai": "openai (needed unless PROVIDER=fake)",
        "sentence_transformers": "sentence-transformers (needed unless RERANK_TOP_K=0)",
    }
    for module, package in required.items():
        try:
            importlib.import_module(module)
            record(OK, f"package {package}")
        except ImportError:
            record(BAD, f"package {package}", "run: pip install -r requirements.txt")
    for module, package in optional.items():
        try:
            importlib.import_module(module)
            record(OK, f"package {package.split(' ')[0]}")
        except ImportError:
            record(WARN, f"package {package}", "not installed")


def check_env() -> None:
    if not (ROOT / ".env").exists():
        record(BAD, ".env file", "copy .env.example to .env and add your key")
        return
    record(OK, ".env file")

    from shared.config import settings

    record(OK, "provider", settings.provider)
    if settings.provider == "fake":
        record(WARN, "OpenAI key", "not needed, PROVIDER=fake")
        return
    if not settings.openai_api_key or settings.openai_api_key.startswith("sk-replace"):
        record(BAD, "OpenAI key", "OPENAI_API_KEY is not set in .env")
    else:
        record(OK, "OpenAI key", f"set, ends {settings.openai_api_key[-4:]}")


def check_models() -> None:
    from shared.config import settings

    if settings.provider == "fake":
        return
    if not settings.openai_api_key or settings.openai_api_key.startswith("sk-replace"):
        return
    try:
        from openai import OpenAI

        client = OpenAI(api_key=settings.openai_api_key)
        available = {m.id for m in client.models.list().data}
    except Exception as exc:  # noqa: BLE001
        record(BAD, "OpenAI reachable", str(exc)[:120])
        return

    record(OK, "OpenAI reachable", f"{len(available)} models visible to this key")

    for label, name in (
        ("chat model", settings.chat_model),
        ("embedding model", settings.embedding_model),
    ):
        if name in available:
            record(OK, label, name)
        else:
            close = sorted(m for m in available if m.startswith(name.split("-")[0]))[:6]
            record(
                BAD,
                label,
                f"'{name}' is not available to your key. Options your key can "
                f"use include: {', '.join(close) if close else 'see platform.openai.com'}",
            )


def check_database() -> None:
    try:
        from shared.db import check_connection, table_counts
    except ImportError as exc:
        record(BAD, "database module", str(exc)[:100])
        return

    try:
        version = check_connection()
    except RuntimeError as exc:
        hint = next(
            (line.strip() for line in str(exc).splitlines()
             if "docker compose" in line),
            "start the database with: docker compose up -d",
        )
        record(BAD, "database connection", hint)
        return
    record(OK, "database connection", version.split(" on ")[0])

    try:
        from shared.db import get_connection

        with get_connection() as conn:
            row = conn.execute(
                "SELECT extversion FROM pg_extension WHERE extname = 'vector'"
            ).fetchone()
        if row:
            record(OK, "pgvector extension", f"version {row[0]}")
        else:
            record(BAD, "pgvector extension", "not installed in this database")
    except Exception as exc:  # noqa: BLE001
        record(BAD, "pgvector extension", str(exc)[:120])
        return

    counts = table_counts()
    if counts.get("documents", -1) < 0:
        record(WARN, "schema", "tables not created yet, run: python -m knowledge.ingest")
        return
    record(OK, "schema", ", ".join(f"{k}={v}" for k, v in counts.items()))
    if counts.get("chunks", 0) == 0:
        record(WARN, "corpus indexed", "no chunks, run: python -m knowledge.ingest")


def check_data() -> None:
    from shared.config import CORPUS_DIR, DATA_DIR

    docs = list(CORPUS_DIR.glob("*.md")) if CORPUS_DIR.exists() else []
    if docs:
        words = sum(len(p.read_text(encoding="utf-8").split()) for p in docs)
        record(OK, "corpus files", f"{len(docs)} documents, about {words // 450} pages")
    else:
        record(WARN, "corpus files", "none, run: python -m data.generate")

    for name in ("golden_set.json", "tickets.json", "assets.csv"):
        path = DATA_DIR / name
        record(OK if path.exists() else WARN, f"data/{name}",
               "" if path.exists() else "run: python -m data.generate")


def main() -> int:
    print("Checking setup ...\n")
    check_python()
    check_packages()
    check_env()
    check_database()
    check_models()
    check_data()

    failures = [r for r in results if r[0] == BAD]
    warnings = [r for r in results if r[0] == WARN]
    print("\n" + "-" * 60)
    if failures:
        print(f"{len(failures)} problem(s) to fix before this will run:")
        for _, name, detail in failures:
            print(f"  - {name}: {detail}")
        return 1
    if warnings:
        print(f"Ready, with {len(warnings)} thing(s) worth noting above.")
    else:
        print("Everything checks out.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
