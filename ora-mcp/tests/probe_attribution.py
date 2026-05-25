"""Probe Qdrant: what `attribution` values actually exist in the index?

Run from project root with .env present:
    python tests/probe_attribution.py
"""
from __future__ import annotations

import os
from collections import Counter
from pathlib import Path


def _load_env(path: Path = Path(".env")) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


def main() -> None:
    _load_env()
    from qdrant_client import QdrantClient

    from ora_mcp.constants import COLLECTION_NAME

    client = QdrantClient(url=os.environ["QDRANT_URL"], api_key=os.environ["QDRANT_API_KEY"], timeout=60)

    info = client.get_collection(COLLECTION_NAME)
    print(f"Collection: {COLLECTION_NAME}")
    print(f"  vectors: {info.points_count}")
    print()

    # Scroll a sample and tally the distinct values of attribution, tier, doc_type
    attrib = Counter()
    tiers = Counter()
    doc_types = Counter()
    offset = None
    seen = 0
    while True:
        batch, offset = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=500,
            with_payload=True,
            with_vectors=False,
            offset=offset,
        )
        for pt in batch:
            p = pt.payload or {}
            attrib[p.get("attribution") or "<missing>"] += 1
            tiers[p.get("tier") or "<missing>"] += 1
            doc_types[p.get("doc_type") or "<missing>"] += 1
        seen += len(batch)
        if offset is None:
            break

    print(f"Scanned {seen} chunks.\n")
    print("=== attribution values ===")
    for v, c in attrib.most_common():
        print(f"  {c:5d}  {v}")
    print("\n=== tier values ===")
    for v, c in tiers.most_common():
        print(f"  {c:5d}  {v}")
    print("\n=== doc_type values ===")
    for v, c in doc_types.most_common():
        print(f"  {c:5d}  {v}")


if __name__ == "__main__":
    main()
