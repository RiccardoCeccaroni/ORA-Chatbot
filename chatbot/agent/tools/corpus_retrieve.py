"""corpus_retrieve — dense ANN over Qdrant + Voyage cross-encoder rerank.

Decision sources:
- #06 Qdrant Cloud free tier, dense-only retrieval
- #07 dense + voyage-rerank-2.5, no query rewriting in v1
- #23 corpus_retrieve tool signature

Returns a list of Chunk dicts with text + full payload metadata for the
synthesis stage and citation pills.
"""

from __future__ import annotations

from typing import Any

import voyageai
from qdrant_client import QdrantClient
from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchAny,
    MatchValue,
    Range,
)

from agent.constants import (
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    RERANK_MODEL,
    RETRIEVE_TOP_K_FINAL,
    RETRIEVE_TOP_K_INITIAL,
)


def build_filter(
    tier_filter: list[str] | None,
    attribution_filter: list[str] | None,
    doc_type_filter: list[str] | None,
    date_from: str | None,
    date_to: str | None,
    exclude_data: bool,
) -> Filter | None:
    """Compose a Qdrant payload filter. Returns None if no conditions."""
    must: list[FieldCondition] = []

    if tier_filter:
        must.append(FieldCondition(key="tier", match=MatchAny(any=tier_filter)))
    if attribution_filter:
        must.append(FieldCondition(key="attribution", match=MatchAny(any=attribution_filter)))
    if doc_type_filter:
        must.append(FieldCondition(key="doc_type", match=MatchAny(any=doc_type_filter)))
    if date_from or date_to:
        rng_kwargs: dict[str, Any] = {}
        if date_from:
            rng_kwargs["gte"] = date_from
        if date_to:
            rng_kwargs["lte"] = date_to
        # Qdrant range works on payload strings if lexicographic. Our date_published
        # values are ISO YYYY-MM-DD so this works.
        must.append(FieldCondition(key="date_published", range=Range(**rng_kwargs)))

    must_not: list[FieldCondition] = []
    if exclude_data:
        must_not.append(FieldCondition(key="doc_type", match=MatchValue(value="data")))

    if not must and not must_not:
        return None
    kwargs: dict[str, Any] = {}
    if must:
        kwargs["must"] = must
    if must_not:
        kwargs["must_not"] = must_not
    return Filter(**kwargs)


def corpus_retrieve(
    query: str,
    *,
    qdrant: QdrantClient,
    voyage: voyageai.Client,
    tier_filter: list[str] | None = None,
    attribution_filter: list[str] | None = None,
    doc_type_filter: list[str] | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    top_k: int = RETRIEVE_TOP_K_FINAL,
    initial_k: int = RETRIEVE_TOP_K_INITIAL,
    exclude_data: bool = True,
) -> list[dict[str, Any]]:
    """Returns top-k chunks from the corpus, dense-retrieved then reranked.

    `exclude_data=True` (default) keeps the data tier out — use `data_lookup`
    for empirical questions. Set False to allow data chunks in the corpus pool.
    """
    # 1. Embed query
    embed_result = voyage.embed(
        texts=[query],
        model=EMBEDDING_MODEL,
        input_type="query",
    )
    query_vec = embed_result.embeddings[0]

    # 2. Qdrant dense ANN with optional pre-filter
    payload_filter = build_filter(
        tier_filter=tier_filter,
        attribution_filter=attribution_filter,
        doc_type_filter=doc_type_filter,
        date_from=date_from,
        date_to=date_to,
        exclude_data=exclude_data,
    )

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

    # 3. Rerank with voyage-rerank-2.5
    candidate_texts = [pt.payload.get("text", "") for pt in candidates]
    rerank_result = voyage.rerank(
        query=query,
        documents=candidate_texts,
        model=RERANK_MODEL,
        top_k=min(top_k, len(candidates)),
    )

    # 4. Build return list ordered by rerank score
    out: list[dict[str, Any]] = []
    for item in rerank_result.results:
        idx = item.index
        pt = candidates[idx]
        payload = dict(pt.payload)
        payload["_rerank_score"] = float(item.relevance_score)
        payload["_dense_score"] = float(pt.score) if pt.score is not None else None
        out.append(payload)

    return out
