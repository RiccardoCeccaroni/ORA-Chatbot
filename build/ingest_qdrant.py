"""Embed all chunks with voyage-4-large and upsert to Qdrant Cloud.

One-shot ingestion script. Reads chunks.jsonl, embeds via Voyage API, upserts
to Qdrant with full payload (chunk_id, parent_id, doc_type, attribution, tier,
content_hash, source_url, date fields, extras).

Decisions backing this:
- #05 voyage-4-large (1024 dims, cosine distance)
- #06 Qdrant Cloud free tier, dense-only
- #04 chunks already produced by chunk_corpus.py

Usage:
    python build/ingest_qdrant.py             # dry-run, prints plan + counts only
    python build/ingest_qdrant.py --apply     # creates collection + embeds + upserts
    python build/ingest_qdrant.py --recreate  # wipes collection first (use carefully)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any

try:
    import voyageai
    from qdrant_client import QdrantClient
    from qdrant_client.models import (
        Distance,
        PointStruct,
        VectorParams,
    )
except ImportError as e:
    print(f"ERROR: missing dependency — {e}. Run: pip install voyageai qdrant-client",
          file=sys.stderr)
    sys.exit(1)


SCRIPT_DIR = Path(__file__).resolve().parent
SECRETS_FILE = SCRIPT_DIR / ".secrets" / "api keys.txt"
CHUNKS_FILE = SCRIPT_DIR / "chunks.jsonl"

COLLECTION_NAME = "ora_chunks"
EMBEDDING_MODEL = "voyage-4-large"
VECTOR_DIM = 1024
DISTANCE = Distance.COSINE
EMBED_BATCH = 100        # Voyage call batch
UPSERT_BATCH = 200       # Qdrant upsert batch


def load_secrets() -> dict[str, str]:
    """Parse the api keys.txt file: 'cluster: ...', 'end point: ...', 'voyage: ...'."""
    if not SECRETS_FILE.is_file():
        print(f"ERROR: secrets file not found at {SECRETS_FILE}", file=sys.stderr)
        sys.exit(1)
    out: dict[str, str] = {}
    for line in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        out[key.strip().lower().replace(" ", "_")] = value.strip()
    required = {"cluster", "end_point", "voyage"}
    missing = required - set(out.keys())
    if missing:
        print(f"ERROR: secrets file missing keys: {missing}", file=sys.stderr)
        sys.exit(1)
    return out


def load_chunks() -> list[dict[str, Any]]:
    if not CHUNKS_FILE.is_file():
        print(f"ERROR: chunks file not found at {CHUNKS_FILE}", file=sys.stderr)
        print("Run build/chunk_corpus.py first.", file=sys.stderr)
        sys.exit(1)
    chunks: list[dict[str, Any]] = []
    with CHUNKS_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chunks.append(json.loads(line))
    return chunks


def chunk_id_to_uuid(chunk_id: str) -> str:
    """Deterministic UUID5 from chunk_id — gives idempotent upserts.
    Qdrant requires point ids be int or UUID, not arbitrary string."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, chunk_id))


def build_payload(chunk: dict[str, Any]) -> dict[str, Any]:
    """Flatten chunk metadata into a Qdrant payload. Excludes the embedding vector
    and the raw text (text goes into payload too — needed at retrieval time).
    """
    return {
        "chunk_id": chunk["chunk_id"],
        "parent_id": chunk["parent_id"],
        "doc_type": chunk.get("doc_type"),
        "attribution": chunk.get("attribution"),
        "tier": chunk.get("tier"),
        "anchor": chunk.get("anchor"),
        "tokens": chunk.get("tokens"),
        "text": chunk["text"],
        "source_url": chunk.get("source_url"),
        "date_published": str(chunk.get("date_published") or "") or None,
        "content_hash": chunk.get("content_hash"),
        "extras": chunk.get("extras") or {},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Actually embed and upsert. Default dry-run prints plan only.")
    parser.add_argument("--recreate", action="store_true",
                        help="If the collection exists, delete it first. Otherwise upsert idempotently.")
    args = parser.parse_args()

    secrets = load_secrets()
    chunks = load_chunks()
    print(f"Loaded {len(chunks):,} chunks from {CHUNKS_FILE.name}")

    # ---------- Plan summary ----------
    total_tokens = sum(c.get("tokens") or 0 for c in chunks)
    n_batches_embed = (len(chunks) + EMBED_BATCH - 1) // EMBED_BATCH
    n_batches_upsert = (len(chunks) + UPSERT_BATCH - 1) // UPSERT_BATCH

    # Voyage-4-large: $0.12/MTok input
    est_cost = total_tokens / 1_000_000 * 0.12
    print()
    print(f"Plan:")
    print(f"  collection:       {COLLECTION_NAME}")
    print(f"  embedding model:  {EMBEDDING_MODEL} ({VECTOR_DIM} dims, cosine)")
    print(f"  endpoint:         {secrets['end_point']}")
    print(f"  total chunks:     {len(chunks):,}")
    print(f"  total tokens:     {total_tokens:,}")
    print(f"  embed batches:    {n_batches_embed} × up to {EMBED_BATCH}")
    print(f"  upsert batches:   {n_batches_upsert} × up to {UPSERT_BATCH}")
    print(f"  est. embed cost:  ${est_cost:.4f}  (voyage-4-large @ $0.12/MTok)")
    print(f"                    — covered by 200M-token free tier")
    print(f"  recreate flag:    {args.recreate}")
    print()

    if not args.apply:
        print("DRY RUN — pass --apply to execute.")
        return

    # ---------- Apply ----------
    print(f"Connecting to Qdrant: {secrets['end_point']}")
    client = QdrantClient(url=secrets["end_point"], api_key=secrets["cluster"], timeout=60.0)

    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME in existing:
        if args.recreate:
            print(f"  collection exists — deleting (--recreate)")
            client.delete_collection(COLLECTION_NAME)
            existing = []
        else:
            print(f"  collection exists — upserting idempotently (no --recreate)")

    if COLLECTION_NAME not in existing:
        print(f"  creating collection: {COLLECTION_NAME}")
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_DIM, distance=DISTANCE),
        )

    # Voyage embed
    voyage_client = voyageai.Client(api_key=secrets["voyage"])

    print(f"\nEmbedding {len(chunks):,} chunks in batches of {EMBED_BATCH} ...")
    t_start = time.time()
    all_embeddings: list[list[float]] = []
    for i in range(0, len(chunks), EMBED_BATCH):
        batch = chunks[i:i + EMBED_BATCH]
        texts = [c["text"] for c in batch]
        result = voyage_client.embed(
            texts=texts,
            model=EMBEDDING_MODEL,
            input_type="document",
        )
        all_embeddings.extend(result.embeddings)
        elapsed = time.time() - t_start
        print(f"  embedded {min(i + EMBED_BATCH, len(chunks)):>5}/{len(chunks)} "
              f"({elapsed:.1f}s elapsed)")
    print(f"All embeddings done in {time.time() - t_start:.1f}s")

    if len(all_embeddings) != len(chunks):
        print(f"ERROR: got {len(all_embeddings)} embeddings for {len(chunks)} chunks",
              file=sys.stderr)
        sys.exit(1)

    # Qdrant upsert
    print(f"\nUpserting {len(chunks):,} points in batches of {UPSERT_BATCH} ...")
    t_start = time.time()
    for i in range(0, len(chunks), UPSERT_BATCH):
        batch_chunks = chunks[i:i + UPSERT_BATCH]
        batch_embs = all_embeddings[i:i + UPSERT_BATCH]
        points = [
            PointStruct(
                id=chunk_id_to_uuid(c["chunk_id"]),
                vector=emb,
                payload=build_payload(c),
            )
            for c, emb in zip(batch_chunks, batch_embs)
        ]
        client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
        elapsed = time.time() - t_start
        print(f"  upserted {min(i + UPSERT_BATCH, len(chunks)):>5}/{len(chunks)} "
              f"({elapsed:.1f}s elapsed)")
    print(f"All upserts done in {time.time() - t_start:.1f}s")

    info = client.get_collection(COLLECTION_NAME)
    print(f"\nFinal collection state:")
    print(f"  vectors_count: {info.points_count}")
    print(f"  status:        {info.status}")


if __name__ == "__main__":
    main()
