"""Chat logging per decision 11.E.

Writes one log row per agent turn. Always writes to JSONL (cheap, append-only,
zero dependencies). If `POSTGRES_DSN` is provided in secrets, ALSO inserts
into the `chat_logs` Postgres table.

No PII: session_hash is a rotating server-side hash, no IP, no user identifier.
"""

from __future__ import annotations

import hashlib
import json
import os
import secrets as pysecrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import psycopg
    _HAS_PG = True
except ImportError:
    _HAS_PG = False


JSONL_LOG_PATH = Path(__file__).resolve().parent.parent / "memory" / "chat_logs.jsonl"


def new_session_hash() -> str:
    """Generate an anonymous, rotating session identifier.

    sha256(random 16 bytes). No link to IP, name, or any user identifier.
    Rotates every session per decision 15 (30-min idle timeout / new convo button).
    """
    return hashlib.sha256(pysecrets.token_bytes(16)).hexdigest()[:32]


def _to_jsonable(obj: Any) -> Any:
    """Recursively make an object JSON-serializable."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_to_jsonable(v) for v in obj]
    return str(obj)


class ChatLogger:
    """Dual-sink logger: always JSONL, optionally also Postgres."""

    def __init__(self, jsonl_path: Path = JSONL_LOG_PATH, postgres_dsn: str | None = None):
        self.jsonl_path = jsonl_path
        self.jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        self._pg_dsn = postgres_dsn or None
        self._pg_disabled_reason: str | None = None

        if self._pg_dsn and not _HAS_PG:
            self._pg_disabled_reason = "psycopg not installed"
        elif self._pg_dsn:
            # Probe connection once at startup; disable PG if it fails.
            try:
                with psycopg.connect(self._pg_dsn, connect_timeout=5) as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT 1")
            except Exception as e:
                self._pg_disabled_reason = f"connect failed: {e!r}"

    @property
    def postgres_active(self) -> bool:
        return self._pg_dsn is not None and self._pg_disabled_reason is None

    @property
    def postgres_status_note(self) -> str:
        if self._pg_dsn is None:
            return "Postgres logging: DISABLED (no DSN provided)"
        if self._pg_disabled_reason is None:
            return "Postgres logging: ACTIVE"
        return f"Postgres logging: DISABLED ({self._pg_disabled_reason})"

    def log(self, event: dict[str, Any]) -> None:
        """Append `event` to JSONL and (if active) to Postgres.

        Expected event keys: see _to_pg_row() for the schema mapping.
        """
        # JSONL — always
        row = _to_jsonable(event)
        # Ensure timestamp
        row.setdefault("created_at", datetime.now(timezone.utc).isoformat())
        with self.jsonl_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

        # Postgres — best-effort, never raises
        if self.postgres_active:
            try:
                self._insert_pg(event)
            except Exception as e:
                # Log to JSONL but don't break the agent over a logging failure
                err_row = {
                    "_logging_error": True,
                    "error": str(e)[:500],
                    "created_at": row["created_at"],
                }
                with self.jsonl_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(err_row, ensure_ascii=False) + "\n")

    def _insert_pg(self, event: dict[str, Any]) -> None:
        assert _HAS_PG and self._pg_dsn
        sql = """
        INSERT INTO chat_logs (
            session_hash, latency_ms,
            raw_query, resolved_query, query_type, adversarial_flag,
            is_empirical, tier_filters, comparison_parties,
            answer_text, is_refusal, refusal_reason,
            cited_chunk_ids, retrieved_chunk_ids, data_card_ids, web_source_urls,
            regen_count, verifier_faithfulness_passed, verifier_relevance_passed,
            verifier_relevance_score, verifier_issues,
            auto_flags, model_versions, cost_usd
        ) VALUES (
            %(session_hash)s, %(latency_ms)s,
            %(raw_query)s, %(resolved_query)s, %(query_type)s, %(adversarial_flag)s,
            %(is_empirical)s, %(tier_filters)s, %(comparison_parties)s,
            %(answer_text)s, %(is_refusal)s, %(refusal_reason)s,
            %(cited_chunk_ids)s, %(retrieved_chunk_ids)s, %(data_card_ids)s, %(web_source_urls)s,
            %(regen_count)s, %(verifier_faithfulness_passed)s, %(verifier_relevance_passed)s,
            %(verifier_relevance_score)s, %(verifier_issues)s,
            %(auto_flags)s, %(model_versions)s, %(cost_usd)s
        )
        """
        params = {
            "session_hash":                  event.get("session_hash"),
            "latency_ms":                    int(event.get("latency_ms") or 0),
            "raw_query":                     event.get("raw_query") or "",
            "resolved_query":                event.get("resolved_query") or event.get("raw_query") or "",
            "query_type":                    event.get("query_type"),
            "adversarial_flag":              event.get("adversarial_flag"),
            "is_empirical":                  event.get("is_empirical"),
            "tier_filters":                  event.get("tier_filters") or [],
            "comparison_parties":            event.get("comparison_parties") or [],
            "answer_text":                   event.get("answer_text") or "",
            "is_refusal":                    bool(event.get("is_refusal")),
            "refusal_reason":                event.get("refusal_reason"),
            "cited_chunk_ids":               event.get("cited_chunk_ids") or [],
            "retrieved_chunk_ids":           event.get("retrieved_chunk_ids") or [],
            "data_card_ids":                 event.get("data_card_ids") or [],
            "web_source_urls":               event.get("web_source_urls") or [],
            "regen_count":                   int(event.get("regen_count") or 0),
            "verifier_faithfulness_passed":  event.get("verifier_faithfulness_passed"),
            "verifier_relevance_passed":     event.get("verifier_relevance_passed"),
            "verifier_relevance_score":      event.get("verifier_relevance_score"),
            "verifier_issues":               json.dumps(event.get("verifier_issues") or []),
            "auto_flags":                    event.get("auto_flags") or [],
            "model_versions":                json.dumps(event.get("model_versions") or {}),
            "cost_usd":                      event.get("cost_usd"),
        }
        with psycopg.connect(self._pg_dsn, connect_timeout=10) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
            conn.commit()
