"""Start the app on a hosted server.

Creates the tables, loads the corpus the first time only (the database keeps
it after that), then runs the API on the port the host gives us.

    python scripts/start.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import uvicorn  # noqa: E402

from knowledge import ingest  # noqa: E402
from shared.db import init_schema, table_counts  # noqa: E402


def main() -> None:
    init_schema()
    if table_counts().get("chunks", 0) <= 0:
        print("Empty database: loading the corpus (one time) ...")
        ingest.main()
    else:
        print("Corpus already loaded, starting the API.")

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app:app", host="0.0.0.0", port=port, proxy_headers=True,
                forwarded_allow_ips="*")


if __name__ == "__main__":
    main()
