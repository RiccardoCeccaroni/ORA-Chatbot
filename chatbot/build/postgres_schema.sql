-- ORA chatbot — Postgres schema for chat logs (decision 11.E + 15).
-- Append-only. No PII. Anonymous session hash, query + answer + retrieval metadata.
-- Run once against your database:
--   psql "$POSTGRES_DSN" -f memory/scripts/postgres_schema.sql

CREATE TABLE IF NOT EXISTS chat_logs (
    id                            UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- timing + session
    created_at                    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    session_hash                  TEXT        NOT NULL,
    latency_ms                    INTEGER     NOT NULL,

    -- query
    raw_query                     TEXT        NOT NULL,
    resolved_query                TEXT        NOT NULL,
    query_type                    TEXT,
    adversarial_flag              TEXT,
    is_empirical                  BOOLEAN,
    tier_filters                  TEXT[],
    comparison_parties            TEXT[],

    -- answer
    answer_text                   TEXT        NOT NULL,
    is_refusal                    BOOLEAN     NOT NULL DEFAULT FALSE,
    refusal_reason                TEXT,

    -- retrieval
    cited_chunk_ids               TEXT[],
    retrieved_chunk_ids           TEXT[],
    data_card_ids                 TEXT[],
    web_source_urls               TEXT[],

    -- verifier
    regen_count                   INTEGER     NOT NULL DEFAULT 0,
    verifier_faithfulness_passed  BOOLEAN,
    verifier_relevance_passed     BOOLEAN,
    verifier_relevance_score      REAL,
    verifier_issues               JSONB,

    -- auto-flags + model snapshot
    auto_flags                    TEXT[],
    model_versions                JSONB,
    cost_usd                      REAL
);

CREATE INDEX IF NOT EXISTS chat_logs_created_idx  ON chat_logs (created_at DESC);
CREATE INDEX IF NOT EXISTS chat_logs_session_idx  ON chat_logs (session_hash);
CREATE INDEX IF NOT EXISTS chat_logs_flags_idx    ON chat_logs USING gin (auto_flags);
CREATE INDEX IF NOT EXISTS chat_logs_refusal_idx  ON chat_logs (is_refusal) WHERE is_refusal;
