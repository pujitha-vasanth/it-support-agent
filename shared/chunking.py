"""Turning source documents into retrievable chunks.

Strategy, deliberately simple:
  1. Split the document on markdown headings, so a chunk never straddles
     two unrelated sections.
  2. Inside a long section, slide a fixed word window with overlap.
  3. Prefix every chunk with its document title and section heading. This
     costs a few tokens and measurably improves retrieval, because a chunk
     that says "Step 3: click Connect" is meaningless without "VPN runbook".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

WORDS_PER_PAGE = 450
DEFAULT_CHUNK_WORDS = 220
DEFAULT_OVERLAP_WORDS = 40

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass
class Chunk:
    chunk_index: int
    section: str
    page_approx: int
    content: str


@dataclass
class LoadedDocument:
    source_path: str
    title: str
    doc_type: str
    category: str
    owner: str
    text: str

    @property
    def word_count(self) -> int:
        return len(self.text.split())


def load_document(path: Path) -> LoadedDocument:
    """Read one file. Supports .md, .txt and .pdf.

    Document type and category come from the front matter if present, else
    they are guessed from the filename. Replace this function if your real
    corpus stores metadata elsewhere; nothing else needs to change.
    """
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        text = _read_pdf(path)
    else:
        text = path.read_text(encoding="utf-8", errors="replace")

    meta, body = _split_front_matter(text)
    title = meta.get("title") or _first_heading(body) or path.stem.replace("-", " ").title()
    doc_type = meta.get("doc_type") or _guess_doc_type(path.stem)
    category = meta.get("category") or "general"
    owner = meta.get("owner") or "Service Desk"

    return LoadedDocument(
        source_path=path.name,
        title=title,
        doc_type=doc_type,
        category=category,
        owner=owner,
        text=body,
    )


def _read_pdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    return "\n\n".join((page.extract_text() or "") for page in reader.pages)


def _split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, parts[2].lstrip("\n")


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        match = _HEADING_RE.match(line)
        if match:
            return match.group(2).strip()
    return None


def _guess_doc_type(stem: str) -> str:
    lowered = stem.lower()
    if "runbook" in lowered:
        return "runbook"
    if "faq" in lowered:
        return "faq"
    return "policy"


def _split_into_sections(text: str) -> list[tuple[str, str]]:
    """Return [(section_heading, section_body), ...] in document order."""
    sections: list[tuple[str, list[str]]] = []
    current_heading = "Introduction"
    current_lines: list[str] = []

    for line in text.splitlines():
        match = _HEADING_RE.match(line)
        if match:
            if current_lines:
                sections.append((current_heading, current_lines))
            current_heading = match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_heading, current_lines))

    return [(h, "\n".join(lines).strip()) for h, lines in sections if "\n".join(lines).strip()]


def chunk_document(
    doc: LoadedDocument,
    chunk_words: int = DEFAULT_CHUNK_WORDS,
    overlap_words: int = DEFAULT_OVERLAP_WORDS,
) -> list[Chunk]:
    chunks: list[Chunk] = []
    words_so_far = 0
    index = 0

    for heading, body in _split_into_sections(doc.text):
        words = body.split()
        if not words:
            continue

        step = max(1, chunk_words - overlap_words)
        for start in range(0, len(words), step):
            window = words[start : start + chunk_words]
            if len(window) < 25 and chunks:
                # Too small to stand alone; fold it into the previous chunk.
                chunks[-1].content += " " + " ".join(window)
                break

            page = (words_so_far + start) // WORDS_PER_PAGE + 1
            content = (
                f"[{doc.title} > {heading}]\n" + " ".join(window)
            )
            chunks.append(
                Chunk(
                    chunk_index=index,
                    section=heading,
                    page_approx=page,
                    content=content,
                )
            )
            index += 1
            if start + chunk_words >= len(words):
                break

        words_so_far += len(words)

    return chunks
