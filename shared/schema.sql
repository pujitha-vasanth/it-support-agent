-- Schema for both projects. {EMBEDDING_DIM} is substituted at runtime from .env.

CREATE EXTENSION IF NOT EXISTS vector;

-- One row per source document in the corpus.
CREATE TABLE IF NOT EXISTS documents (
    id           SERIAL PRIMARY KEY,
    source_path  TEXT UNIQUE NOT NULL,
    title        TEXT NOT NULL,
    doc_type     TEXT NOT NULL,          -- policy | runbook | faq
    category     TEXT NOT NULL,          -- access, hardware, network, ...
    owner        TEXT NOT NULL DEFAULT '',  -- team that owns the document, used for routing
    word_count   INTEGER NOT NULL DEFAULT 0,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- One row per retrievable chunk. Holds both the dense vector and the
-- lexical tsvector, which is what makes the search hybrid.
CREATE TABLE IF NOT EXISTS chunks (
    id           SERIAL PRIMARY KEY,
    document_id  INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index  INTEGER NOT NULL,
    section      TEXT,
    page_approx  INTEGER,
    content      TEXT NOT NULL,
    embedding    vector({EMBEDDING_DIM}),
    tsv          tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
    UNIQUE (document_id, chunk_index)
);

CREATE INDEX IF NOT EXISTS chunks_tsv_idx ON chunks USING GIN (tsv);
CREATE INDEX IF NOT EXISTS chunks_document_idx ON chunks (document_id);

-- Asset inventory, used by the asset-lookup sub-agent in project 2.
CREATE TABLE IF NOT EXISTS assets (
    id            SERIAL PRIMARY KEY,
    asset_tag     TEXT UNIQUE NOT NULL,
    user_email    TEXT NOT NULL,
    user_name     TEXT NOT NULL,
    device_type   TEXT NOT NULL,
    model         TEXT NOT NULL,
    os_version    TEXT NOT NULL,
    purchase_date DATE,
    warranty_end  DATE,
    status        TEXT NOT NULL,
    location      TEXT NOT NULL,
    software      TEXT NOT NULL DEFAULT ''
);

CREATE INDEX IF NOT EXISTS assets_email_idx ON assets (lower(user_email));

-- Every triage run is persisted so the human approval step has something
-- to approve, and so you can show an audit trail in a demo.
CREATE TABLE IF NOT EXISTS triage_runs (
    id               SERIAL PRIMARY KEY,
    ticket_id        TEXT NOT NULL,
    subject          TEXT NOT NULL,
    body             TEXT NOT NULL,
    requester_email  TEXT,
    category         TEXT,
    priority         TEXT,
    queue            TEXT,
    auto_resolvable  BOOLEAN NOT NULL DEFAULT false,
    confidence       REAL,
    draft_reply      TEXT,
    citations        JSONB NOT NULL DEFAULT '[]'::jsonb,
    asset_summary    TEXT,
    trace            JSONB NOT NULL DEFAULT '[]'::jsonb,
    approval_status  TEXT NOT NULL DEFAULT 'pending',   -- pending | approved | rejected
    approved_by      TEXT,
    decision_note    TEXT,
    decided_at       TIMESTAMPTZ,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS triage_status_idx ON triage_runs (approval_status);

-- One row per API request that touched a model: what it cost, how long it
-- took and how it ended. This is what the /dashboard page reads.
CREATE TABLE IF NOT EXISTS request_log (
    id             SERIAL PRIMARY KEY,
    endpoint       TEXT NOT NULL,              -- ask | search | triage
    provider       TEXT NOT NULL,
    model          TEXT NOT NULL,
    latency_ms     INTEGER NOT NULL,
    input_tokens   INTEGER NOT NULL DEFAULT 0,
    output_tokens  INTEGER NOT NULL DEFAULT 0,
    cost_usd       DOUBLE PRECISION NOT NULL DEFAULT 0,
    outcome        TEXT NOT NULL,              -- answered | not_covered | auto_resolvable | held | error
    created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS request_log_created_idx ON request_log (created_at);
