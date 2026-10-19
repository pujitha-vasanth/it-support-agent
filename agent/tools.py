"""The tools the sub-agents can call.

Two tools, deliberately. The knowledge tool is the RAG service built in the
knowledge package, called in-process. The asset tool is a plain SQL lookup.

Calling the knowledge service in-process rather than over HTTP keeps the
default setup to one running thing. Set KNOWLEDGE_SERVICE_URL in .env if you
want the agent to call it across the network instead, which is what you would
do if the two were deployed separately.
"""

from __future__ import annotations

import os
from datetime import date

from knowledge.answer import Answer, answer_question
from shared.db import get_connection

KNOWLEDGE_SERVICE_URL = os.getenv("KNOWLEDGE_SERVICE_URL", "").strip()


def knowledge_tool(question: str, top_k: int | None = None) -> Answer:
    """Ask the knowledge service. Returns a grounded answer with citations."""
    if not KNOWLEDGE_SERVICE_URL:
        return answer_question(question, top_k=top_k)

    import httpx

    response = httpx.post(
        f"{KNOWLEDGE_SERVICE_URL.rstrip('/')}/knowledge/ask",
        json={"question": question, "top_k": top_k},
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    result = Answer(question=question, text=payload["answer"], chunks=[])
    result.covered = payload["covered"]
    result._remote_citations = payload["citations"]  # type: ignore[attr-defined]
    return result


def asset_tool(email: str) -> dict | None:
    """Look up the device assigned to a user. None if there is no record."""
    if not email:
        return None
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT asset_tag, user_name, user_email, device_type, model,
                   os_version, purchase_date, warranty_end, status, location, software
            FROM assets
            WHERE lower(user_email) = lower(%s)
            LIMIT 1
            """,
            (email,),
        ).fetchone()
    if not row:
        return None

    (
        asset_tag, user_name, user_email, device_type, model, os_version,
        purchase_date, warranty_end, status, location, software,
    ) = row

    today = date.today()
    in_warranty = warranty_end is not None and warranty_end >= today
    age_years = round((today - purchase_date).days / 365.25, 1) if purchase_date else None

    return {
        "asset_tag": asset_tag,
        "user_name": user_name,
        "user_email": user_email,
        "device_type": device_type,
        "model": model,
        "os_version": os_version,
        "purchase_date": str(purchase_date) if purchase_date else None,
        "warranty_end": str(warranty_end) if warranty_end else None,
        "in_warranty": in_warranty,
        "age_years": age_years,
        "status": status,
        "location": location,
        "software": software,
    }


def summarise_asset(record: dict | None) -> str:
    if not record:
        return "No device record found for this user in the asset inventory."
    warranty = (
        f"in warranty until {record['warranty_end']}"
        if record["in_warranty"]
        else f"out of warranty since {record['warranty_end']}"
    )
    return (
        f"{record['user_name']} is assigned asset {record['asset_tag']}, a "
        f"{record['model']} ({record['device_type']}) running {record['os_version']}, "
        f"purchased {record['purchase_date']} ({record['age_years']} years old), "
        f"{warranty}. Status: {record['status']}. Location: {record['location']}. "
        f"Licensed software: {record['software']}."
    )
