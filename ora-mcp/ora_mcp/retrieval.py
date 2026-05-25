"""Retrieval over the ORA corpus — dense ANN (Qdrant) + Voyage cross-encoder rerank.

Two public functions, both exposed as MCP tools by `server.py`:

- `find_position(topic, ...)` — structured retrieval that organizes results into
  trust-hierarchy buckets (official_party / leader_views / supporting_data /
  optionally comparison). This is the primary tool — see DECISIONS D05 for why
  we replaced the flat-list `corpus_retrieve` with this.

- `data_lookup(metric, ...)` — unchanged from the original chatbot. Stat-card
  retrieval scoped to the data tier, ordered by source quality (D1–D4).

The low-level search (`_search_with_vec`) is private and reused by both. We
embed the query *once* per `find_position` call and reuse the vector across
all bucket-specific Qdrant queries — only the payload filter changes.
"""

from __future__ import annotations

import asyncio
from typing import Any

from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchAny,
    MatchValue,
    Range,
)

from ora_mcp.clients import get_qdrant, get_voyage
from ora_mcp.constants import (
    COLLECTION_NAME,
    DATA_TOP_K_FINAL,
    EMBEDDING_MODEL,
    OTHER_PARTIES_ATTRIBUTIONS,
    PARTY_ATTRIBUTION,
    RERANK_MODEL,
    RETRIEVE_TOP_K_INITIAL,
)


# ----------------------------------------------------------------------------
# Internal: filter construction and search primitives
# ----------------------------------------------------------------------------

def _build_filter(
    *,
    tier_filter: list[str] | None = None,
    attribution_filter: list[str] | None = None,
    doc_type_filter: list[str] | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    exclude_data: bool = True,
) -> Filter | None:
    must: list[FieldCondition] = []
    if tier_filter:
        must.append(FieldCondition(key="tier", match=MatchAny(any=tier_filter)))
    if attribution_filter:
        must.append(FieldCondition(key="attribution", match=MatchAny(any=attribution_filter)))
    if doc_type_filter:
        must.append(FieldCondition(key="doc_type", match=MatchAny(any=doc_type_filter)))
    if date_from or date_to:
        rng: dict[str, Any] = {}
        if date_from:
            rng["gte"] = date_from
        if date_to:
            rng["lte"] = date_to
        must.append(FieldCondition(key="date_published", range=Range(**rng)))

    must_not: list[FieldCondition] = []
    if exclude_data:
        must_not.append(FieldCondition(key="doc_type", match=MatchValue(value="data")))

    if not must and not must_not:
        return None
    kw: dict[str, Any] = {}
    if must:
        kw["must"] = must
    if must_not:
        kw["must_not"] = must_not
    return Filter(**kw)


def _search_with_vec(
    query_text: str,
    query_vec: list[float],
    *,
    payload_filter: Filter | None,
    top_k: int,
    initial_k: int = RETRIEVE_TOP_K_INITIAL,
) -> list[dict[str, Any]]:
    """Run a Qdrant ANN search using a pre-computed query vector, then rerank."""
    qdrant = get_qdrant()
    voyage = get_voyage()

    search_result = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vec,
        query_filter=payload_filter,
        limit=initial_k,
        with_payload=True,
    )
    candidates = list(search_result.points)
    if not candidates:
        return []

    candidate_texts = [pt.payload.get("text", "") for pt in candidates]
    rerank_result = voyage.rerank(
        query=query_text,
        documents=candidate_texts,
        model=RERANK_MODEL,
        top_k=min(top_k, len(candidates)),
    )

    out: list[dict[str, Any]] = []
    for item in rerank_result.results:
        pt = candidates[item.index]
        payload = dict(pt.payload)
        payload["_rerank_score"] = round(float(item.relevance_score), 4)
        payload.pop("_dense_score", None)
        out.append(payload)
    return out


def _embed(query: str) -> list[float]:
    voyage = get_voyage()
    result = voyage.embed(texts=[query], model=EMBEDDING_MODEL, input_type="query")
    return result.embeddings[0]


# ----------------------------------------------------------------------------
# Public: find_position — the primary MCP tool
# ----------------------------------------------------------------------------

async def find_position(
    topic: str,
    *,
    top_k_per_bucket: int = 5,
    include_comparison: bool = False,
    include_leaders: bool = True,
    date_from: str | None = None,
    date_to: str | None = None,
) -> dict[str, Any]:
    """Structured retrieval of ORA's position on a topic, organized by trust tier.

    Returns a dict with these keys:

      - `official_party`: chunks from the party voice (manifesto, comunicati,
        identity docs, statuto, fondamenti, etc.). ALWAYS the primary source
        when reporting "ORA's position".
      - `leader_views`: dict with `boldrin` and `forchielli` keys, each a list
        of chunks from that leader's personal output. ⚠️ Cite as personal,
        NOT as party position. (Omitted if `include_leaders=False`.)
      - `supporting_data`: empirical stat-cards relevant to the topic. Use to
        ground quantitative claims; cite the `data_metric` / `data_period` /
        `quality_tier` from each card's `extras`.
      - `comparison`: other-parties chunks (PD, M5S, FdI, Lega, FI, AVS,
        Azione, IV). Only present if `include_comparison=True`.

    The query embedding is computed once and reused across buckets, so cost
    scales linearly in the number of buckets, not in `top_k_per_bucket`.
    Bucket pipelines run concurrently via asyncio.gather — see DECISIONS D31.
    """
    qvec = await asyncio.to_thread(_embed, topic)

    def _bucket(attribution_values: list[str]) -> list[dict[str, Any]]:
        f = _build_filter(
            attribution_filter=attribution_values,
            date_from=date_from,
            date_to=date_to,
            exclude_data=True,  # data has its own bucket
        )
        return _search_with_vec(topic, qvec, payload_filter=f, top_k=top_k_per_bucket)

    keys: list[str] = ["official_party"]
    coros: list = [asyncio.to_thread(_bucket, [PARTY_ATTRIBUTION])]

    if include_leaders:
        keys.extend(["_boldrin", "_forchielli"])
        coros.append(asyncio.to_thread(_bucket, ["boldrin"]))
        coros.append(asyncio.to_thread(_bucket, ["forchielli"]))

    keys.append("supporting_data")
    coros.append(asyncio.to_thread(
        _data_lookup_with_vec, topic, query_vec=qvec, top_k=top_k_per_bucket
    ))

    if include_comparison:
        keys.append("comparison")
        coros.append(asyncio.to_thread(_bucket, OTHER_PARTIES_ATTRIBUTIONS))

    results = await asyncio.gather(*coros)
    by_key = dict(zip(keys, results))

    out: dict[str, Any] = {"official_party": by_key["official_party"]}
    if include_leaders:
        out["leader_views"] = {
            "boldrin": by_key["_boldrin"],
            "forchielli": by_key["_forchielli"],
        }
    out["supporting_data"] = by_key["supporting_data"]
    if include_comparison:
        out["comparison"] = by_key["comparison"]
    return out


# ----------------------------------------------------------------------------
# data_lookup — secondary MCP tool, kept distinct (see DECISIONS D05)
# ----------------------------------------------------------------------------

_TIER_RANK = {"D1": 0, "D2": 1, "D3": 2, "D4": 3, None: 4}


def _data_lookup_with_vec(
    metric: str,
    *,
    query_vec: list[float],
    quality_tier_floor: str = "D3",
    top_k: int = DATA_TOP_K_FINAL,
) -> list[dict[str, Any]]:
    """Internal helper: data-tier search with a pre-computed query vector."""
    f = _build_filter(doc_type_filter=["data"], exclude_data=False)
    chunks = _search_with_vec(
        metric, query_vec, payload_filter=f, top_k=top_k * 2  # over-fetch for quality filter
    )

    accepted = {"D1", "D2", "D3", "D4"}
    floor_rank = _TIER_RANK[quality_tier_floor]
    filtered: list[dict[str, Any]] = []
    for c in chunks:
        extras = c.get("extras") or {}
        qt = extras.get("quality_tier")
        if qt not in accepted:
            continue
        if _TIER_RANK.get(qt, 99) > floor_rank:
            continue
        filtered.append(c)

    filtered.sort(
        key=lambda c: (
            _TIER_RANK.get((c.get("extras") or {}).get("quality_tier"), 99),
            -float(c.get("_rerank_score") or 0),
        )
    )
    return filtered[:top_k]


def data_lookup(
    metric: str,
    *,
    period: str | None = None,
    quality_tier_floor: str = "D3",
    top_k: int = DATA_TOP_K_FINAL,
) -> list[dict[str, Any]]:
    """Look up empirical stat-cards by metric name (Italian free-text).

    Use when the user asks a quantitative question. Returns stat-cards ordered
    by quality_tier (D1 first), then rerank relevance.
    """
    query_text = metric if not period else f"{metric} {period}"
    qvec = _embed(query_text)
    return _data_lookup_with_vec(
        metric=query_text,
        query_vec=qvec,
        quality_tier_floor=quality_tier_floor,
        top_k=top_k,
    )
