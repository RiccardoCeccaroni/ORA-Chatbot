"""Singleton Qdrant + Voyage clients, env-driven.

In production (Fly.io), env vars are injected via `fly secrets set`.
Locally, populate `.env` from `.env.example` and load via the shell or a
dotenv loader of your choice — this module only reads `os.environ`.
"""

from __future__ import annotations

import os
from functools import lru_cache

import voyageai
from qdrant_client import QdrantClient


def _require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            f"See .env.example for the full list."
        )
    return value


@lru_cache(maxsize=1)
def get_qdrant() -> QdrantClient:
    return QdrantClient(
        url=_require("QDRANT_URL"),
        api_key=_require("QDRANT_API_KEY"),
        timeout=30,
    )


@lru_cache(maxsize=1)
def get_voyage() -> voyageai.Client:
    return voyageai.Client(api_key=_require("VOYAGE_API_KEY"))
