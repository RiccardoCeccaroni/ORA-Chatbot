"""data_lookup — retrieves D1-D4 stat-cards from the data tier (decision 17).

Internally the same retrieval pipeline as corpus_retrieve, but scoped to
`doc_type=data` and ordered by `quality_tier` preference. Returns stat-cards
with their `data_metric`, `data_period`, `quality_tier`, and `source_doc`.
"""

from __future__ import annotations

from typing import Any

import voyageai
from qdrant_client import QdrantClient

from agent.constants import DATA_TOP_K_FINAL
from agent.tools.corpus_retrieve import corpus_retrieve


# Default tier preference: D1 (national statistical) > D2 (international) > D3 (institutional) > D4 (advocacy)
TIER_RANK = {"D1": 0, "D2": 1, "D3": 2, "D4": 3, None: 4}


def data_lookup(
    metric: str,
    *,
    qdrant: QdrantClient,
    voyage: voyageai.Client,
    period: str | None = None,
    quality_tier_floor: str = "D3",   # exclude anything weaker than this by default
    top_k: int = DATA_TOP_K_FINAL,
) -> list[dict[str, Any]]:
    """Find stat-cards matching `metric` (Italian, free-text), optionally
    scoped by `period`. Filters out cards below `quality_tier_floor`.
    """
    # Build a query that includes period if specified
    query_text = metric if not period else f"{metric} {period}"

    # Retrieve from the data tier only
    chunks = corpus_retrieve(
        query_text,
        qdrant=qdrant,
        voyage=voyage,
        doc_type_filter=["data"],
        exclude_data=False,
        top_k=top_k * 2,  # over-fetch so we can quality-filter
    )

    # Apply quality_tier floor
    accepted_tiers = {"D1", "D2", "D3", "D4"}
    floor_rank = TIER_RANK[quality_tier_floor]
    filtered: list[dict[str, Any]] = []
    for c in chunks:
        extras = c.get("extras") or {}
        qt = extras.get("quality_tier")
        if qt not in accepted_tiers:
            continue
        if TIER_RANK.get(qt, 99) > floor_rank:
            continue
        filtered.append(c)

    # Re-sort by (quality_tier_rank ascending, rerank_score descending)
    filtered.sort(
        key=lambda c: (
            TIER_RANK.get((c.get("extras") or {}).get("quality_tier"), 99),
            -float(c.get("_rerank_score") or 0),
        )
    )

    return filtered[:top_k]
