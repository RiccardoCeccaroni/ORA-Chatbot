# 04 — Chunking strategy

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **Option C (structure-aware per content type), with chunk schema designed so option D (parent expansion) can be bolted on later without re-chunking.**

- **Atomic unit inside profiles and tesi:** each `###` block is one chunk (one position = one claim, with its bullets/quote-citations attached). Plus a **whitelist of high-value `##` framing sections** as their own chunks: `## Sintesi` (profiles, identity), `## Contesto` (tesi), `## Evoluzione nel tempo` (profiles). Skip `## Problemi`, `## Quadri analitici`, `## Concordanze e divergenze`, `## Riferimenti`, `## Sorgente raw` from embedding.
- **Other doc types:** comunicato = 1 chunk per doc (paragraph-split if long); newsletter section = 1 chunk per section; data card = 1 chunk per `##` H2 (Snapshot / Table / Caveats); identity = per `##`.
- **Leader articles (131, flat prose):** paragraph-cluster split — group adjacent paragraphs to ~400–500 tokens, soft-break at paragraph boundaries.
- **Every chunk carries `parent_id`** pointing to the source `.md` file's frontmatter `id`. This is what makes D (parent expansion at generation time) a small future change rather than a re-chunk.

**Rationale (Riccardo, 2026-05-13):** The distillations (leader profiles, other-party profiles, tesi proposte) are deliberately authored one-atomic-claim-per-`###` with per-stance citations inline. A structure-aware chunker inherits that work directly — every retrieved chunk is already a self-contained, citable, attributable unit, which is what the chatbot's faithfulness + citation-pill UX needs. Fixed-size (A) and pure paragraph (B) would fragment the authored structure for no upside. Pure D up front adds engineering cost we can't yet justify without eval signal; same chunks under C, plus a stable `parent_id`, leaves D as a generation-time bolt-on. E (late chunking) would couple this decision to decision 05 (embedding model), which is still OPEN.

**Recommendation accepted as-is; no redirection on atomic-unit whitelist or article handling.**

## The question

Long source documents (manifesto sections, newsletters, YouTube transcripts of 1-hour shows) must be broken into smaller pieces ("chunks") before being indexed. **How are those pieces drawn?**

A chunk is the unit of retrieval: when the user asks a question, the system finds the most relevant chunks and stuffs them into the LLM's prompt. Too small → loses context. Too large → wastes prompt budget and dilutes relevance.

## Why it matters for the ORA chatbot

- The corpus is heterogeneous: tight manifesto sections (clear structure) sit next to hour-long unstructured podcast transcripts. One chunking rule will not fit all of them.
- Faithfulness depends on chunk integrity: if a chunk cuts mid-sentence between "ORA opposes" and "no, ORA supports — with the following conditions", the bot will misquote the party.
- Chunk size has direct cost implications: smaller chunks → more vectors → bigger index, more retrievals.

## Options

### A — Fixed-size with overlap (e.g., 500 tokens, 50-token overlap)
- Simple, fast to implement, standard baseline.
- Ignores semantic structure. Will cut across paragraphs, lists, list items.

### B — Sentence- or paragraph-based
- Splits on natural boundaries. Better readability of retrieved chunks.
- Variable chunk sizes can cause retrieval-score normalization issues.

### C — Structure-aware (per content type)
- Manifesto: one chunk per `###` heading.
- Comunicati: one chunk per press release, or per paragraph if long.
- Newsletter: one chunk per topical section (newsletters already have section markers).
- YouTube transcripts: chunk by topic-shift detected from cues (silences, speaker changes) or by fixed time windows.
- Best faithfulness; most engineering work.

### D — Hierarchical / parent–child ("small-to-big")
- Index small precise chunks (e.g., 1–2 sentences). On retrieval, return the *parent* document or surrounding context to the LLM.
- Combines precise retrieval with rich generation context. Modern best practice for high-faithfulness setups.
- More moving parts in the index.

### E — Late chunking
- Embed the whole document with a long-context embedding model, then chunk after embedding. Each chunk's embedding incorporates document-level context.
- Cutting-edge; depends on embedding model choice (decision 05).

## What we'd need to know to choose

- Are you willing to do per-content-type ingestion (option C/D), or do you want a single uniform pipeline?
- How important is "the retrieved chunk reads cleanly when shown as a citation"?
- What's the chosen embedding model's context window? (Decision 05 — they interact.)

## Reference

- KB concept: `06_chunking.md`
- KB concept: `05_the_rag_pipeline.md`

## Observations
- Manifesto files use `### Glossario`, `### Premessa`, `### Tesi`, etc. — strong structural anchors.
- Newsletters use date-headed sections and bullet lists.
- YouTube transcripts (`.txt` from `_vtt_to_txt.py`) are flat text without speaker turns or timestamps — would need re-processing for structure-aware chunking.
