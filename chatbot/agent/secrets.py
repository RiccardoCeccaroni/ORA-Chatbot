"""Load API credentials from .secrets/api keys.txt + environment.

Expected file format (build/.secrets/api keys.txt):
    cluster: <qdrant-api-key>
    end point: <qdrant-url>
    voyage: <voyage-api-key>
    anthropic: <optional, also taken from $ANTHROPIC_API_KEY>
"""

from __future__ import annotations

import os
from pathlib import Path

SECRETS_FILE = Path(__file__).resolve().parent.parent / "build" / ".secrets" / "api keys.txt"


def load_secrets() -> dict[str, str]:
    """Returns {qdrant_url, qdrant_key, voyage_key, anthropic_key}."""
    out: dict[str, str] = {}

    if SECRETS_FILE.is_file():
        for line in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, _, value = line.partition(":")
            normalized = key.strip().lower().replace(" ", "_")
            out[normalized] = value.strip()

    # Allow env-var override / supplement
    if "ANTHROPIC_API_KEY" in os.environ:
        out["anthropic"] = os.environ["ANTHROPIC_API_KEY"]

    # Accept both "anthropic:" and "anthropic key:" forms in the secrets file.
    anthropic_key = out.get("anthropic") or out.get("anthropic_key") or ""
    postgres_dsn = out.get("postgres") or out.get("postgres_dsn") or os.environ.get("POSTGRES_DSN", "")

    return {
        "qdrant_url": out.get("end_point") or out.get("endpoint") or "",
        "qdrant_key": out.get("cluster") or "",
        "voyage_key": out.get("voyage") or out.get("voyage_key") or "",
        "anthropic_key": anthropic_key,
        "postgres_dsn": postgres_dsn,
    }


def require(secrets: dict[str, str], *keys: str) -> None:
    """Raise RuntimeError if any of the named keys are empty."""
    missing = [k for k in keys if not secrets.get(k)]
    if missing:
        raise RuntimeError(
            f"Missing required credentials: {', '.join(missing)}.\n"
            f"Add to {SECRETS_FILE} or set ANTHROPIC_API_KEY env var."
        )
