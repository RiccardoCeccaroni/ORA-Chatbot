# ORA! MCP — technical decisions

> **Purpose of this document.** When the original ORA chatbot was built, every
> architectural fork was recorded in `decisions/01_*.md` … `decisions/25_*.md`.
> This MCP server is a smaller project, so all the decisions are consolidated
> into a single document — but the same principle holds: every non-trivial
> choice is recorded with its alternatives and rationale, so a future
> maintainer (or the ORA technical team taking ownership) can understand
> *why* the code looks the way it does.
>
> Status of every decision below: **DECIDED** as of 2026-05-24 (v0.1.0).
> D31–D33 were finalized on 2026-05-24; D32 was reversed by D33 the same day.

---

## D01 — Why an MCP server at all

**Context.** The original project was an Agentic-RAG chatbot intended to be
embedded on `ora-italia.it`. ORA! management rejected that form factor but
expressed openness to an MCP server.

**Decision.** Build a publicly hosted MCP server that exposes ORA!'s corpus
to third-party AI clients (Claude Desktop, Cursor, ChatGPT with MCP, etc.).

**Why.**
- The party never "speaks" — risk surface is dramatically smaller than a
  chatbot that generates utterances.
- The audience is anyone using a modern AI assistant, not just sito visitors.
- No website integration required — useful given we don't have access to
  `ora-italia.it`.
- The expensive infrastructure of the original project (corpus curation,
  3,665-chunk Qdrant index, retrieval tools) transfers ~60–70% intact.

**Alternative considered.** Pivot to a website widget that uses MCP under
the hood. Rejected — that's still a chatbot with extra steps.

---

## D02 — Separate repository from the chatbot

> **Reversed 2026-05-25 (monorepo merge).** The two projects were later
> consolidated into a single monorepo at `RiccardoCeccaroni/ORA-Chatbot`
> with `chatbot/` and `ora-mcp/` as sibling subdirs. Riccardo's
> preference was a single workspace over two siblings; the handover
> story is recoverable by re-extracting `ora-mcp/` to its own repo when
> needed. The decision below describes the *original* rationale, kept
> for the audit trail.

**Decision (original).** New folder `C:\Users\ricca\Desktop\ora-mcp\`, sibling to the
original `ORA Chatbot - presentation/`. Independent git history.

**Why.**
- The chatbot project's `decisions/` audit trail is valuable but
  chatbot-specific. Lifting it wholesale would create archaeological
  confusion.
- The MCP project has a different stakeholder narrative ("we pivoted")
  and benefits from a clean `git log`.
- The retrieval pipeline (`build/`) stays in the original project as the
  source of truth for corpus maintenance. This MCP server is a read-only
  consumer.

**Coupling that remains.** Both projects point at the **same Qdrant
collection** (`ora_chunks`). Re-indexing happens in the original project;
this server picks up changes automatically.

---

## D03 — Transport: streamable HTTP, not stdio

**Decision.** Expose the MCP server over **streamable HTTP transport** at
`/mcp`. No stdio transport.

**Why.**
- The goal is a publicly accessible server. stdio is for local/desktop
  process spawning, not internet hosting.
- Streamable HTTP is the 2025+ MCP standard (replaced the older HTTP+SSE
  transport); supported by all major MCP clients.
- A single deployable Docker image handles every client.

**Alternative considered.** SSE transport. Rejected — superseded by
streamable HTTP in the official MCP spec.

---

## D04 — Server framework: FastMCP + Starlette mount

> **Topology revised by D33 (2026-05-24).** The "wrap in parent Starlette"
> framing below is still right, but the mechanism changed: we no longer
> `Mount("/mcp", _mcp_app)` — we splat `*_mcp_app.routes` into the parent
> so OAuth metadata's root-level endpoints (`/authorize`, `/token`, etc.)
> match reality. See D33 for the reason; LEARNINGS Bug F for the failure
> mode this avoids.

**Decision.** Use `FastMCP` from the official `mcp` Python SDK. Wrap its
`streamable_http_app()` in a parent Starlette app to add a landing page
and a health endpoint.

**Why.**
- `FastMCP` provides the ergonomic decorator API (`@mcp.tool()`,
  `@mcp.resource()`) and handles all transport / schema negotiation.
- Mounting at `/mcp` keeps the public surface namespaced — `/` is free
  for the landing page (so a human visitor sees something), `/health`
  is free for Fly.io's checker.
- Single ASGI app means single process to run under uvicorn — no
  multi-process orchestration.

**Code reference.** `ora_mcp/server.py` lines 220–235.

---

## D05 — Two tools, five resources (revised 2026-05-23)

**Decision (current).** Expose exactly two tools:
- `find_position(topic, ...)` — **primary tool**. Structured retrieval that
  returns trust-hierarchy buckets (`official_party`, `leader_views`,
  `supporting_data`, optionally `comparison`).
- `data_lookup(metric, ...)` — empirical stat-card retrieval, distinct trigger
  (metric-driven, quality-tier filtered).

And five resources:
- `ora://about` — meta document about ORA! and the trust hierarchy.
- `ora://manifesto` — full manifesto (21 thesis files, ~575 KB).
- `ora://statuto` — party bylaws (~57 KB).
- `ora://fondamenti` — 15 policy fundamentals, Allegato 2 (~10 KB).
- `ora://codice-etico` — code of ethics, Allegato 3 (~4 KB).

**Why `find_position` replaced `corpus_retrieve` (reversed 2026-05-23).**
The first version exposed `corpus_retrieve(query, tier_filter, attribution_filter,
doc_type_filter, ...)` — a generic ranked-list search. A briefly-considered
intermediate version added `find_position` as a *third* tool alongside it.
Both versions were rejected for a known failure mode: when two MCP tools have
overlapping purpose, the host AI picks inconsistently across users and the
output quality degrades. The current single-tool design forces the AI to
make the obvious choice and enforces the trust hierarchy in the response
**shape**, not just in docstring guidance — much harder for the AI to ignore
or invert the official/personal/data distinction.

**Why `data_lookup` stays a separate tool.** Its trigger is unambiguous (the
first argument is a metric name, not a topic) and its filtering logic
(quality_tier_floor) doesn't fit the position-bucket abstraction. Keeping it
distinct avoids the overlap problem because no plausible query routes to both.

**Why the three governance resources (statuto, fondamenti, codice-etico) were
added.** Small, stable, the kind of document a journalist or researcher
wants quoted verbatim rather than paraphrased from a search.

**Explicitly dropped from the original chatbot.**
- `web_search` — host AIs already have web search; not the MCP's value.
- `verify_answer` — verifier of generated text; this MCP doesn't generate.
- `emit_refusal` — chatbot persona; not the MCP's job.
- A "summarize position" tool that would synthesize a single answer — would
  recreate the chatbot risk surface management rejected.
- A `compare_with_party(topic, party)` tool — `find_position` with
  `include_comparison=True` covers this without duplicating surface area.

**Why.**
- These four artifacts cover all four objectives the original chatbot was
  designed for: State, Project, Justify, Compare.
- Adding more tools (e.g., `compare_parties`, `find_quote`) creates
  surface area without unique value — the host AI can compose
  `corpus_retrieve` calls itself.
- Two resources (instead of e.g. one per thesis) means the host AI gets
  the full manifesto in one read — no orchestration logic needed on
  the client side.

---

## D06 — Retrieval logic: lifted unchanged

**Decision.** `ora_mcp/retrieval.py` is a near-verbatim merge of
`agent/tools/corpus_retrieve.py` and `agent/tools/data_lookup.py` from the
original project.

**Changes vs. the original.**
1. Clients (`QdrantClient`, `voyageai.Client`) are fetched from a
   module-level singleton (`clients.py`) instead of passed in by callers.
2. `_dense_score` is stripped from the public return — the rerank score
   is the meaningful signal; raw similarity is internal.
3. `_rerank_score` is rounded to 4 decimals (cleaner payloads).

**Why no logic change.**
- The Explore agent (Phase 1 of the plan) confirmed zero hidden coupling
  to the original orchestrator. Tools were already stateless.
- Behavioral parity with the chatbot is desirable — if a future ORA
  technical team A/B-tests the MCP vs. the original system, divergence
  should be in presentation, not retrieval quality.

**Code reference.** `ora_mcp/retrieval.py`.

---

## D07 — Tool docstrings as instructions to the host AI

**Decision.** Tool docstrings in `server.py` are long, structured, and
written *to the host AI*. They explain the trust hierarchy, which
filters to use when, and the meaning of each tier.

**Why.**
- MCP clients pass tool docstrings verbatim to the host AI as the tool
  description. This is the **only** instruction surface available — the
  MCP can't inject a system prompt.
- Without explicit guidance, the host AI doesn't know to prefer
  `attribution=ora` over `attribution=boldrin`, or that `other-parties`
  should only be retrieved on explicit comparison.

**Trade-off.** The docstrings count against the host AI's tool-schema
context budget. They're ~600 tokens each. Acceptable for the demo;
revisit if a client complains.

---

## D08 — Resources for ground-truth, tools for search

**Decision.** The `ora://manifesto` resource ships the **full manifesto
verbatim** (575 KB, all 21 thesis files concatenated). `ora://about`
ships the trust-hierarchy guide.

**Why this division.**
- **Resources** = stable, canonical documents the host AI might pre-load.
- **Tools** = dynamic search that returns chunks based on the user's query.
- The manifesto is *ground truth* — when the host AI needs to quote ORA!'s
  position on a topic, it should be able to reach the literal manifesto
  text, not a paraphrase from a chunk.
- 575 KB is large but well within Claude's 200K-token context window.

**Alternative considered.** Ship only a summary, force tool calls for
everything. Rejected — increases hallucination risk on direct-quote
questions.

---

## D09 — Authentication: open + rate-limited

**Decision.** No API keys. Rate limit: 30 requests per minute per IP on
the `/mcp` endpoint. Implemented via custom in-memory sliding-window
middleware.

**Why open.**
- ORA! is a political party that benefits from exposure. Gating reduces
  reach.
- Adding API keys creates a key-management surface (issuance, rotation,
  revocation) that the demo doesn't justify.
- If abuse becomes a problem, API keys can be added later without
  breaking the public-URL contract.

**Why custom rate-limit instead of `slowapi`.**
- `slowapi`'s primary API is per-route decorators on FastAPI/Starlette
  routes. The MCP routes are mounted from FastMCP — we don't have direct
  access to decorate them.
- A 30-line sliding-window middleware does the job without adding a
  dependency.
- In-memory state is acceptable for single-instance deploys (Fly.io's
  shared-cpu-1x). For horizontal scaling, swap to Redis.

**Code reference.** `RateLimitMiddleware` in `ora_mcp/server.py`.

---

## D10 — Secrets: env-vars only, no secrets file

**Decision.** `ora_mcp/clients.py` reads `QDRANT_URL`, `QDRANT_API_KEY`,
`VOYAGE_API_KEY` from `os.environ`. No secrets file.

**Why.**
- The original project's secrets file (`build/.secrets/api keys.txt`) is
  a convenience for local development. Production needs env vars anyway
  (Fly.io's `fly secrets set` injects them).
- Single source of truth — no risk of file/env mismatch.
- `.env` files for local dev are loaded by the developer's shell or
  whatever tool they prefer; the server itself doesn't need to know.

**Migration path for the ORA team.** When they take ownership, they may
prefer a secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager).
Wrapping `os.environ.get()` in a thin abstraction would suffice — no
caller change needed.

---

## D11 — Hosting target: Fly.io (recommended for the demo)

**Decision.** First deploy target is Fly.io. Frankfurt region (`fra`) for
proximity to Italian users.

**Why Fly.io.**
- Free tier covers demo traffic easily.
- Docker-based deploy → identical image runs anywhere later (Render,
  Railway, ORA's own infra).
- Automatic HTTPS with a `*.fly.dev` URL — professional enough for a demo,
  trivially replaceable with a custom domain when ORA! adopts the project.
- Frankfurt has ~30ms latency from Italy, vs. ~150ms for US East.

**Alternatives considered.**
- Cloudflare Workers: rejected. Python on Workers (Pyodide) is limited;
  Qdrant + Voyage clients may not work cleanly. Would require rewriting
  in TypeScript.
- Self-hosted VPS: rejected for demo. Adds TLS, reverse proxy, process
  supervisor ops with no benefit for v1.

**Portability guarantee.** The only Fly-specific file is `fly.toml`. The
Dockerfile is host-agnostic.

---

## D12 — Frankfurt region (not Milan)

**Decision.** Fly.io region `fra` (Frankfurt), not `mxp` (Milan).

**Why.** Fly.io has no Italian region. Frankfurt is the closest, with
sub-30ms latency to most of Italy. Listed in `fly.toml`.

---

## D13 — Docker base: `python:3.12-slim`

**Decision.** `python:3.12-slim`, not `python:3.12-alpine` or a
distroless image.

**Why.**
- `qdrant-client` and `voyageai` depend on libraries with C extensions.
  Slim/Debian-based images have glibc; Alpine uses musl, which has
  occasional binary-wheel issues.
- Distroless would shave MB but complicates the `HEALTHCHECK` (no python
  in distroless without explicit copy).
- Demo-grade trade-off: prefer reliability over image size.

---

## D14 — In-memory rate limit state (vs. Redis)

**Decision.** Rate-limit state lives in a process-local dict.

> **Updated 2026-05-24.** The deploy was switched to always-warm
> (`min_machines_running = 1`, `auto_stop_machines = false`) for the
> demo to avoid cold-start latency. The in-memory rate-limit decision
> still applies — state still resets, just on Fly redeploys rather than
> on auto-stop cycles.

**Why.**
- Single-machine deploy (Fly.io `shared-cpu-1x`, `min_machines_running=0`
  in the original auto-stop config; `min_machines_running=1` in the
  current always-warm config).
- Fly.io's `auto_stop_machines=stop` policy (the original choice) meant the process restarts
  cold occasionally. Rate-limit state resets — acceptable for the demo,
  since the limit is 30/min/IP, not a hard usage quota.

**Migration path.** When ORA! scales beyond one machine, swap the dict
for Redis. The middleware contract doesn't change.

---

## D15 — Project layout: flat package (reversed 2026-05-23)

**Decision (current).** Source code lives at `ora_mcp/`, at the project
root. No `src/` wrapper.

**Why (reversed).** The original choice was a `src/`-layout (industry
default for libraries: prevents accidental imports from the working
directory, encourages install-before-test). For this project that
reasoning was outweighed by:

- Three layers (`ora-mcp/src/ora_mcp/`) felt noisy for a single-package
  application — author preference for the simpler `ora-mcp/ora_mcp/`.
- The project is an application (deployed as a Docker image), not a
  library that ships to PyPI — the `src/` safety properties matter less.
- The flat layout is what every contributor will see first; reducing
  surprise is worth more than a marginal best-practice gain.

**Trade-off accepted.** If you `cd` into `ora-mcp/` and run `python`,
`import ora_mcp` will work without installing (because the package is at
the cwd). That's the bug `src/` was meant to prevent. In practice, the
Dockerfile and `pip install -e .` flow both go through proper install,
so the risk is small.

---

## D16 — Landing page at `/`

**Decision.** A static HTML landing page at `GET /` of the MCP server.
Explains what the server is, lists the tools, shows the connection
snippet.

**Why.**
- An MCP server URL looks like an API endpoint, not a human destination.
  When ORA! shares the URL with members or journalists, some will paste
  it into a browser. A 404 there hurts the demo.
- 50 lines of HTML, no JS — zero ops cost.

**Code reference.** `_LANDING_HTML` in `ora_mcp/server.py`.

---

## D17 — Health endpoint at `/health`

**Decision.** `GET /health` returns `200 OK` with body `"ok"`. Used by
Fly.io's checker (`fly.toml [[http_service.checks]]`) and Docker's
`HEALTHCHECK`.

**Why.** Standard requirement for orchestrated deploys.

---

## D18 — No CI/CD pipeline (for the demo)

**Decision.** No GitHub Actions, no automated testing, no auto-deploy.

**Why.**
- The demo is short-lived (weeks). The deploy is one `fly deploy` away.
- Adding CI before the project is approved by ORA! is premature
  optimization.

**When to revisit.** As soon as ORA! adopts the project. CI is worth
adding the day a second person can deploy.

---

## D19 — Logging: stdout, no structured backend

**Decision.** Uvicorn's default logging to stdout. No Loki, no Datadog,
no Postgres logging table.

**Why.**
- Fly.io captures stdout and exposes it via `fly logs`.
- The original chatbot's Postgres chat-log was for QA review of
  generated answers. This MCP doesn't generate — there's nothing to
  review beyond access logs.

**When to revisit.** If usage patterns become important to the party
(traffic, popular queries), add structured logging then.

---

## D20 — What lives where: source-of-truth map (reversed 2026-05-23)

**Original decision.** The MCP project was a thin read-only consumer; the
corpus and build pipeline stayed in the parent chatbot project.

**Current decision.** ora-mcp is now self-contained. The corpus and the
maintenance scripts live here too — the parent chatbot folder is no
longer required for any operation.

| Asset | Lives in (now) | Modified how? |
|-------|----------------|---------------|
| Corpus markdown files | `ora-mcp/corpus/` (810 files, ~103 MB) | Hand-edit + `build/youtube_pipeline/` |
| Chunked JSONL | `ora-mcp/build/chunks.jsonl` | `python build/chunk_corpus.py --apply` |
| Qdrant index | Qdrant Cloud, collection `ora_chunks` | `python build/ingest_qdrant.py --apply` |
| MCP server code | `ora-mcp/ora_mcp/` | Edit + `fly deploy` |
| Resource content | `ora-mcp/ora_mcp/resources/` | Edit + `fly deploy` |

**Implication unchanged.** A corpus update needs no MCP redeploy (both
operations read/write the same Qdrant collection). An MCP behavior
change needs no corpus rebuild.

**What was NOT copied from the parent project.**
- `agent/` — the chatbot runtime (orchestrator, persona, verifier, CLI).
  Replaced by `ora_mcp/server.py`.
- `build/run_eval.py` — chatbot eval harness; imports from `agent.*`.
- `build/render_docx.py` — chatbot eval output rendering.
- `build/postgres_schema.sql` — chatbot conversation logging.
- `decisions/*.md` — 25 original decision docs. Summary lives in this
  file; the originals stay in the parent project as historical record.

**Coupling that remains with the parent project.** None at the file level.
The two projects share the same Qdrant collection (`ora_chunks`) and the
same external services (Voyage AI). Either project can update the index
and the other sees the change.

---

## D21 — Build deps as optional extras

**Decision.** Dependencies needed only by the build pipeline (`pyyaml`,
`tiktoken`, `anthropic`, `openai`, `imageio-ffmpeg`) are declared as
optional extras in `pyproject.toml`:

```bash
pip install .            # MCP server runtime only
pip install ".[build]"   # + chunk_corpus.py, ingest_qdrant.py, audit_frontmatter.py
pip install ".[youtube]" # + youtube_pipeline (Whisper transcription, AI distillation)
pip install ".[dev]"     # + pytest, httpx
```

**Why.**
- The MCP server runtime is small (~6 deps). Forcing every install to pull
  the heavy ML libraries would bloat the Docker image needlessly.
- The deploy target (Fly.io) installs `pip install .` only, so the
  production image stays slim.
- A future ORA maintainer can install just the parts they need.

**Reference.** `pyproject.toml [project.optional-dependencies]`.

---

## D22 — Two secrets surfaces (intentional duplication)

**Decision.** Credentials live in two places inside `ora-mcp/`:

1. `ora-mcp/.env` — env-var format. Read by `ora_mcp/clients.py` at
   runtime via `os.environ`. The MCP server uses this.
2. `ora-mcp/build/.secrets/api keys.txt` — legacy `key: value` format.
   Read by `build/ingest_qdrant.py` and the `youtube_pipeline` scripts.

**Why two.** The build scripts were written for the parent chatbot
project, which used a custom secrets file. Rewriting them to read from
`os.environ` would be touched on five files for minimal gain. The
duplication is contained (both files are gitignored, both have the same
secret values).

**Migration path.** If the ORA team takes ownership and wants a single
secrets surface, refactor the build scripts to call a helper that reads
from `os.environ` first, falling back to the legacy file. Then delete the
legacy file. Estimated effort: 30 minutes.

---

## D23 — `.dockerignore` excludes corpus + build

**Decision.** `.dockerignore` excludes `corpus/`, `build/`, `demo/`, and
`tests/` from the Docker build context.

**Why.** The runtime server doesn't need any of these. Including them
would bloat the Fly.io image by >100 MB (mostly `corpus/other-parties/`),
slow deploys, and waste container storage.

**Reference.** `.dockerignore` at the `ora-mcp/` root (path is relative
to the MCP project, not the monorepo root).

---

## Open questions for the ORA technical team (if adopted)

1. **Hosting** — keep on Fly.io, or migrate to ORA-controlled infra?
   The Docker image is portable; either works.
2. **Domain** — keep `ora-mcp-claudeai.fly.dev`, or move to `mcp.ora-italia.it`?
   Custom domain via Fly.io is `fly certs add`.
3. **Manifesto resource** — should `ora://manifesto` ship the full text
   (575 KB, current default) or a curated summary plus a `manifesto_thesis`
   tool that fetches by ID?
4. **Rate limit** — 30/min/IP is a guess for demo traffic. Tune once we
   see actual usage.
5. **Logging / analytics** — does the party want to know what people ask?
   This has political-sensitivity implications.

---

## Appendix — file inventory

```
ora-mcp/
├── pyproject.toml              # deps: mcp[cli], qdrant-client, voyageai, starlette, uvicorn
├── README.md                   # two-section: party-first, then devs
├── DECISIONS.md                # this file
├── CLAUDE.md                   # AI-collaboration scaffolding (gitignored)
├── Dockerfile                  # python:3.12-slim + pip install + uvicorn
├── fly.toml                    # Fly.io app config (region fra, 512mb)
├── .env.example                # template for QDRANT_*, VOYAGE_API_KEY
├── .gitignore                  # excludes .env, CLAUDE.md, build artifacts
├── ora_mcp/
│   ├── __init__.py
│   ├── server.py               # FastMCP app, tools, resources, rate limit, landing
│   ├── constants.py            # pruned copy of agent/constants.py
│   ├── clients.py              # env-driven Qdrant + Voyage singletons
│   ├── retrieval.py            # merged corpus_retrieve + data_lookup
│   └── resources/
│       ├── about.md            # ORA! identity + trust hierarchy guide
│       ├── manifesto_full.md   # 21 thesis files concatenated
│       ├── statuto.md          # governance bylaws
│       ├── fondamenti.md       # 15 policy fundamentals (Allegato 2)
│       └── codice-etico.md     # code of ethics (Allegato 3)
├── corpus/                     # 810 source markdown files (~103 MB)
│   ├── ora-party/              # 220 files — party voice
│   ├── leaders/                # 212 files — Boldrin & Forchielli
│   ├── other-parties/          # 217 files — comparison corpus
│   └── data/                   # 161 files — ISTAT / Eurostat / OECD stat-cards
├── build/                      # maintenance pipeline (optional install)
│   ├── chunk_corpus.py         # corpus → chunks.jsonl (~6.9 MB output)
│   ├── ingest_qdrant.py        # chunks.jsonl → Qdrant collection ora_chunks
│   ├── audit_frontmatter.py    # corpus health-checks
│   ├── chunks.jsonl            # current chunked state (gitignored)
│   ├── youtube_pipeline/       # transcribe + distill YouTube → corpus
│   └── .secrets/               # legacy secrets file (gitignored)
├── tests/
│   ├── smoke_queries.py        # 6-question quick sanity check
│   ├── probe_attribution.py    # introspect live Qdrant payloads
│   ├── generate_report.py      # PDF report generator (smoke 6Q)
│   └── comprehensive_report.py # PDF report generator (105 tests)
└── demo/
    ├── claude_desktop_config.json
    └── demo_questions.md
```

---

## D24 — Attribution field values: `"party"`, not `"ora"` (bug found + fixed 2026-05-23)

**Context.** First end-to-end smoke test against the live retrieval pipeline
showed `official_party` bucket empty for every single query — a critical
failure mode where the LLM would have been forced to infer the party
position from leader-personal views, violating the trust hierarchy.

**Root cause.** Our retrieval code assumed `attribution_filter=["ora"]` would
match ORA's official voice and `attribution_filter=["other"]` would match
other parties. Direct introspection of the live Qdrant collection
(`tests/probe_attribution.py`) revealed the actual payload values:

| Bucket           | What we assumed   | What's really there                  |
|------------------|-------------------|--------------------------------------|
| Official party   | `"ora"`           | `"party"` (615 chunks)               |
| Boldrin          | `"boldrin"`       | `"boldrin"` (1 302) — already correct |
| Forchielli       | `"forchielli"`    | `"forchielli"` (192) — already correct |
| Other parties    | `"other"`         | `"azione"`, `"pd"`, `"fdi"`, `"iv"`, `"fi"`, `"avs"`, `"lega"`, `"m5s"` — each named individually |
| Data             | (filter by doc_type) | various source names — irrelevant since we filter by doc_type |

**Decision.** Lifted the actual values to constants in `ora_mcp/constants.py`
(`PARTY_ATTRIBUTION`, `LEADER_ATTRIBUTIONS`, `OTHER_PARTIES_ATTRIBUTIONS`)
and use them in `find_position`. Verified end-to-end with the 105-test
comprehensive suite — every official_party bucket now populates correctly.

**Why this matters for inspection.** The original chatbot's
`agent/tools/corpus_retrieve.py` passed `attribution_filter` straight through
to Qdrant without enforcing values — callers had to know the canonical
strings. This was implicit knowledge that didn't survive the port. Lesson:
when porting retrieval code that filters on string-valued metadata fields,
always probe the live index for the actual values before trusting any
constant.

---

## D25 — Forward FastMCP lifespan when mounted as sub-app

> **Code sample superseded by D33.** The `Mount("/mcp", app=_mcp_app)`
> pattern in the snippet below was replaced by route-splatting (D33,
> LEARNINGS Bug F). The lifespan-forwarding logic itself still applies
> — see current `ora_mcp/server.py`.


**Context.** When the server was first launched, every POST to `/mcp`
returned `500 Internal Server Error` with the trace:
`RuntimeError: Task group is not initialized. Make sure to use run().`

**Root cause.** FastMCP's `streamable_http_app()` returns a Starlette
sub-app whose session manager task group is initialized in its
**lifespan** handler. When this sub-app is `Mount()`ed inside a parent
Starlette app, Starlette does **not** automatically propagate the
sub-app's lifespan — the session manager never initializes, every request
fails.

**Decision.** Manually forward the lifespan in `server.py`:

```python
_mcp_app = mcp.streamable_http_app()

@asynccontextmanager
async def _lifespan(_):
    async with _mcp_app.router.lifespan_context(_mcp_app):
        yield

app = Starlette(routes=[..., Mount("/mcp", app=_mcp_app)], lifespan=_lifespan)
```

**Why this matters.** This is a Starlette + FastMCP integration trap that
is not documented in either project's quickstart. Any future inspection
finding "lifespan code" in `server.py` should understand it's load-bearing,
not boilerplate.

---

## D26 — `streamable_http_path="/"` to avoid double-mounting at `/mcp/mcp`

> **Superseded by D33 (2026-05-24).** Once we splatted routes into the
> parent (D33), there's no `Mount("/mcp", ...)` to compose with, so the
> `streamable_http_path` workaround is no longer needed. Current
> `ora_mcp/server.py` constructs `FastMCP("ORA!")` without the argument.


**Context.** FastMCP defaults `streamable_http_path = "/mcp"`. When the
sub-app is mounted at `/mcp` in the parent Starlette router, the actual
HTTP endpoint becomes `/mcp/mcp` — clients connecting to the documented
`/mcp` URL get 404.

**Decision.** Construct FastMCP with `streamable_http_path="/"` so the
sub-app's internal path is root, and the external URL is exactly `/mcp`
(courtesy of the `Mount("/mcp", ...)` in the parent).

**Reference.** `ora_mcp/server.py`: `mcp = FastMCP("ORA!", streamable_http_path="/")`.

---

## D27 — Server auto-loads `.env` at startup

**Context.** All retrieval requires `QDRANT_URL`, `QDRANT_API_KEY`, and
`VOYAGE_API_KEY` env vars. Test scripts loaded `.env` themselves. The
server didn't — relying on the launching shell to have exported them.
When Claude Desktop's `mcp-remote` subprocess spawned the server, it
inherited the parent's environment which lacked these vars → every tool
call failed with "missing VOYAGE_API_KEY".

**Decision.** `ora_mcp/server.py` now calls `_load_dotenv()` at import
time. The loader looks for `.env` in `cwd` and in the project root, and
uses `os.environ.setdefault()` so explicitly-exported values still win.

**Why not `python-dotenv`.** Adding a dependency for ~15 lines of code
was disproportionate. The minimal loader is in `server.py` and matches the
same logic the test scripts use, with no install surface.

**Note after monorepo move (2026-05-25).** With `ora_mcp/` now living
inside `ORA-Chatbot-monorepo/`, the `parent.parent / ".env"` lookup
resolves to `ora-mcp/.env`. The loader still finds the canonical MCP
.env there (where it was placed during the migration). Running the
server from anywhere other than `ora-mcp/` or the monorepo root may
miss the file — keep `python -m ora_mcp.server` invoked from `ora-mcp/`.

---

## D28 — Single primary tool (`find_position`) replacing both `corpus_retrieve` and an intermediate dual-tool design

**Context.** Initial design exposed two tools — a generic `corpus_retrieve`
and a possible additional `find_position`. We considered keeping both, with
`find_position` returning structured buckets and `corpus_retrieve` returning
a flat list. Reviewer challenge: two overlapping tools is a documented
failure mode for tool-using LLMs — the model picks inconsistently across
users, the output quality degrades, and the trust hierarchy collapses into
"whichever ranked list came back."

**Decision.** Collapse to **one** primary retrieval tool:

- `find_position(topic, top_k_per_bucket, include_comparison, include_leaders,
  date_from, date_to)` — structured retrieval, always returns four buckets:
  `official_party`, `leader_views`, `supporting_data`, and (optionally)
  `comparison`.

`data_lookup` is kept as a second tool because its trigger is unambiguous
(a metric name, not a topic) and its filtering (quality_tier_floor) does
not fit the position-bucket abstraction. Two tools, no overlap.

**Why response shape, not docstring guidance.** The trust hierarchy is now
enforced **structurally** by `find_position`'s return type — buckets keep
party voice and leader personal views in separate dict keys. The host AI
cannot accidentally conflate them because they were never in the same
list. This is strictly stronger than relying on docstring instructions.

**Reference.** `DECISIONS.md` D05 (revised) and `ora_mcp/retrieval.py`.

---

## D29 — Comprehensive 105-test acceptance suite

**Decision.** `tests/comprehensive_report.py` runs 105 automated tests
across 8 sections (manifesto topics, user-style phrasings, leader-specific
queries for both Boldrin and Forchielli, data lookups, party comparisons,
all 5 resources, edge cases including privacy probes and parameter
validation), produces a PDF report (`comprehensive_test_report.pdf`) with
green/yellow/red verdict per test and an executive summary.

> The PDF is a **generated artifact** — it is not committed to the
> repository (regenerate with `python tests/comprehensive_report.py`).
> Every reference to `comprehensive_test_report.pdf` in this document
> assumes you have produced it locally first.

**Why this rather than unit tests.** Retrieval quality is not a unit-test
concern. The right question is "would a competent LLM, receiving these
buckets, produce a defensible answer?" — that requires inspecting the
bucket contents per query, not asserting return shapes. The PDF gives a
human reviewer a one-shot acceptance signal before the demo.

**Methodology for verdict assignment.** Per-test logic in
`comprehensive_report.py`:

- *Party-position queries*: GREEN if `official_party` non-empty and top
  rerank score ≥ 0.55. YELLOW if non-empty but score 0.45–0.55. RED if
  empty.
- *Leader queries*: GREEN if the named leader's bucket has chunks with
  top score ≥ 0.45.
- *Data queries*: GREEN if top stat-card's `quality_tier` is D1 or D2;
  YELLOW for D3 or unknown.
- *Comparison queries*: verifies the named party's attribution value
  appears among the comparison bucket's chunks (not just any other-party).
- *Edge cases*: privacy-probe queries verify low `official_party` scores
  on private-life topics; off-policy queries verify the system doesn't
  fabricate; parameter queries verify `include_leaders=False` and
  `top_k_per_bucket=1` are honored.

**Result of the 2026-05-23 run.** 99 green, 6 yellow, 0 red. The full PDF
is in `comprehensive_test_report.pdf`; high-level summary in
`SESSION_NOTES.md`.

---

## D30 — Claude Desktop integration via `mcp-remote` stdio bridge

**Context.** Claude Desktop's `claude_desktop_config.json` accepts only
stdio-transport MCP entries (`command` + `args`). Our server is HTTP
(streamable HTTP transport, per D03). Two incompatible worlds.

**Decision.** Use `mcp-remote` (an `npm` package) as a stdio↔HTTP bridge:

```json
"ora": {
  "command": "cmd",
  "args": ["/c", "npx", "-y", "mcp-remote", "http://localhost:8000/mcp"]
}
```

Claude Desktop spawns `cmd /c npx -y mcp-remote URL` as a stdio
subprocess. `mcp-remote` then connects to our HTTP server and bridges
messages bidirectionally. From the user's perspective, `ora` appears
alongside other stdio MCPs in Claude Desktop with no UI difference.

**Why `cmd /c npx ...` instead of `npx ...` directly.** On Windows,
`npx` is a `.cmd` shim. Spawning it directly from Claude Desktop's
subprocess API does not resolve correctly — the standard fix is to
wrap in `cmd /c` which uses the shell's PATH resolution and shim
handling.

**Trade-off accepted.** First-time launch downloads `mcp-remote` via npx
(~5-15 seconds the first time). Subsequent launches are instant.

**Reference.** `demo/claude_desktop_config.json` and the actual user
config at `%APPDATA%\Claude\claude_desktop_config.json`.

---

## D31 — Parallelize `find_position` buckets with `asyncio.gather` (resolves Issue 1, 2026-05-24)

**Context.** The first version of `find_position` ran four independent
retrieval pipelines (`official_party`, `boldrin`, `forchielli`,
`supporting_data`, plus optional `comparison`) **sequentially**. Each
pipeline includes a Voyage rerank over 50 candidates and takes ~10–15 s.
End-to-end latency was ~45–60 s — sitting right on Claude Desktop's
~60 s tool-call timeout, so live demos failed with
*"Tool result could not be submitted."* See Known Issue 1 below (now
resolved).

**Decision.** Make `find_position` async and run the bucket pipelines
concurrently with `asyncio.gather`. Each pipeline is wrapped in
`asyncio.to_thread(...)` because the underlying Qdrant + Voyage clients
are sync. Only the initial `_embed(topic)` runs first (its output is
reused by all buckets); after that, all bucket searches and reranks fan
out in parallel.

```python
qvec = await asyncio.to_thread(_embed, topic)
# ... build coros for each bucket via asyncio.to_thread(_bucket, ...)
results = await asyncio.gather(*coros)
```

**Why `asyncio.to_thread` instead of `voyageai.AsyncClient`.** The Voyage
SDK exposes an async client in newer versions, but switching would
require migrating `clients.py`, both client singletons, and every call
site in `retrieval.py`. `asyncio.to_thread` is one-line per call and
works regardless of SDK version. Pipelines are network-bound, so the
thread pool is appropriate.

**Expected outcome.** End-to-end latency drops from ~max(sum of buckets)
to ~max(slowest single bucket) — roughly **~15 s** under typical
conditions. Cost (Voyage rerank API calls) is unchanged: the same four
reranks happen, they just happen concurrently.

**Async-first design decision (for technical-team review).** We chose to
make `find_position` canonically async — a single entry point — rather
than provide both a sync `find_position` (with `asyncio.run` inside) and
an async internal version. Rationale:

- One source of truth, no risk of the two versions diverging.
- FastMCP supports async tool handlers natively, so the MCP path is
  clean.
- The only sync callers were 3 test scripts (`smoke_queries.py`,
  `generate_report.py`, `comprehensive_report.py`, 6 call sites total),
  which were updated to wrap with `asyncio.run(...)`. Mechanical change,
  no behavioral risk.

If a future maintainer needs a sync entry point (e.g., for a script that
mixes ORA retrieval with other sync work), adding a sync `find_position`
shim that calls `asyncio.run(_find_position_async(...))` would take ~5
lines.

**Trade-off accepted.** A `lambda: asyncio.run(find_position(...))`
pattern in tests is slightly less ergonomic than the previous direct
call, but acceptable — these are reporting scripts, not hot paths.

**Code reference.** `ora_mcp/retrieval.py:find_position`; FastMCP wrapper
at `ora_mcp/server.py:find_position` (now `async`); test updates in
`tests/smoke_queries.py`, `tests/generate_report.py`,
`tests/comprehensive_report.py`.

**Verification plan.** Re-run `tests/comprehensive_report.py` to confirm
105-test correctness is preserved (the parallel pipelines produce the
same payloads as the sequential ones). Then re-test in Claude Desktop
with the previously-timing-out query
*"Qual è la posizione di ORA! sulla riforma del sistema pensionistico?"*
— expected response time under 20 s.

---

## D32 — Cloudflare Tunnel for the demo; Fly.io retained as a future option (2026-05-24)

> ⚠️ **REVERSED later same day by D33.** During end-to-end testing, the
> tunnel's "needs your laptop on" constraint proved incompatible with
> async management evaluation. We pivoted back to Fly.io and added OAuth
> there so claude.ai's web connector path could be used. The Cloudflare
> Tunnel was an interesting detour; the final state is Fly-only.

**Context.** D11 nominated Fly.io as the hosting target for the demo.
Fly.io removed their no-credit-card free tier in late 2024 — any deploy
now requires adding a payment method, and incurs small but non-zero
billing (~$0–2/month for this config). For a short-lived demo to ORA!
management, the maintainer preferred a zero-friction, zero-card free
path.

**Decision.** Expose the locally-running MCP server to a public HTTPS
URL via **Cloudflare Tunnel** (`cloudflared`), mode `trycloudflare`.

```powershell
python -m ora_mcp.server                      # window 1
cloudflared tunnel --url http://localhost:8000  # window 2 → prints public URL
```

The server is unchanged — it still listens on `localhost:8000`. The
tunnel forwards Cloudflare-edge traffic to it. From the demo recipient's
perspective, the URL behaves like any other public HTTPS endpoint.

**Why Cloudflare and not ngrok / localtunnel / etc.**
- Cloudflare's edge runs a large fraction of the public web — high trust
  signal for management.
- The CLI is one binary, one command; `trycloudflare` mode keeps zero
  state on disk and requires no Cloudflare account.
- ngrok's free tier has the same ephemeral-URL limitation but is more
  associated with developer-tool aesthetics.

**Trade-offs accepted.**
- **PC dependency.** The public URL works only while the maintainer's
  PC is on AND the tunnel process is running. Same constraint as
  Known Issue 2 (the local server is not supervised) — Cloudflare just
  exposes the same single point of failure to the internet.
- **Ephemeral URL.** `trycloudflare` assigns a random subdomain like
  `https://blue-cat-123.trycloudflare.com` per tunnel run. The URL
  changes on every restart. The demo kit (`demo/README.md` and
  `demo/claude_desktop_config.json`) was updated to use a
  `<URL_DEL_SERVER>` placeholder; a one-line PowerShell substitution
  produces the ready-to-send copies in `demo/out/` (see `DEPLOY.md`).
- **Less polished subdomain.** `*.trycloudflare.com` is not as
  brand-aligned as `ora-mcp.fly.dev` or `mcp.ora-italia.it`. Acceptable
  for a demo; the landing page itself carries the ORA! logo + OpenGraph
  card, which carries most of the professional signal.

**Fly.io artifacts retained.** `fly.toml`, `Dockerfile`, and the
provision-flow comments inside `fly.toml` are left in place untouched.
If ORA! adopts the project and wants stable hosting, the D11 path is one
`fly launch + fly secrets set + fly deploy` away — no code changes
required. The retention is intentional: the choice between Fly and
Cloudflare Tunnel is purely about hosting cost and operator preference,
not architecture.

**Path to a stable URL on Cloudflare** (for future maintenance, not the
initial demo): a named tunnel attached to a hostname on a
Cloudflare-managed domain produces a permanent URL like
`mcp.ora-italia.it`. Requires a Cloudflare account + a domain. See
`DEPLOY.md` "URL stability" section.

**Reference.** `DEPLOY.md` (operational runbook), `demo/README.md` and
`demo/claude_desktop_config.json` (recipient-facing kit, using
`<URL_DEL_SERVER>` placeholder).

---

## D33 — OAuth 2.1 added (this sibling project only) so claude.ai web's connector flow can connect (2026-05-24)

**Context.** D09 deliberately declined authentication for the original
`ora-mcp` project — the server is public, rate-limited, no API keys.
That decision was made when the demo target was Claude Desktop, which
uses the local `mcp-remote` stdio bridge to talk to our HTTP server
(no OAuth required).

Later experimentation revealed that **claude.ai/customize/connectors
(the web UI, plus iOS/Android Claude)** requires the MCP server to
expose OAuth 2.1 endpoints — `/.well-known/oauth-authorization-server`,
`/.well-known/oauth-protected-resource`, `/register` (Dynamic Client
Registration, RFC 7591), `/authorize`, `/token`. claude.ai's connector
flow performs OAuth discovery on the URL the user pastes; if those
endpoints 404, claude.ai shows "Couldn't reach the MCP server" even
though the server is perfectly healthy.

For management evaluation, claude.ai web is the most likely entry point
(no Claude Desktop install required, works on iPhone/iPad), so D09's
no-auth scope was too narrow.

**Decision (this sibling project only — `ora-mcp-claudeai/`).** Add a
**permissive** OAuth 2.1 provider that wires into FastMCP's
`auth_server_provider` and `auth=AuthSettings(...)` parameters. FastMCP
auto-registers the standard endpoints when these are configured. The
provider is "permissive": anyone can register a client, anyone can
complete the authorize → token exchange, no human consent UI, tokens are
long-lived (1 year). Same *effective* access as the no-auth design;
OAuth is pure protocol satisfaction for claude.ai's handshake
requirement.

**Why a sibling project instead of modifying `ora-mcp/`.** The original
project works end-to-end via Claude Desktop today. Adding OAuth there
would risk breaking a known-working demo path. Cloning to
`ora-mcp-claudeai/` insulates the OAuth experiment. If it succeeds,
demo materials switch to the new URL; if it fails, the original
project remains the demo and the sibling is a learning artifact.

**Implementation.**
- New module `ora_mcp/auth.py` (~170 lines) — `PermissiveOAuthProvider`
  implements the full 9-method `OAuthAuthorizationServerProvider`
  protocol with in-memory storage (`dict`s for clients, auth codes,
  access tokens, refresh tokens). PKCE validation, client secret
  authentication, and metadata generation are handled by the MCP SDK's
  built-in handlers — we only provide storage and the auto-approve
  redirect logic.
- `ora_mcp/server.py` adds `auth_server_provider` and `auth` to the
  FastMCP constructor; `transport_security.allowed_hosts` updated to
  include `ora-mcp-claudeai.fly.dev`.
- Deployed as Fly app `ora-mcp-claudeai` (`https://ora-mcp-claudeai.fly.dev`).

**Trade-offs accepted.**
- **In-memory state.** A Fly machine restart wipes all clients, codes,
  and tokens. Users would need to re-authorize (claude.ai typically
  does this transparently). Acceptable for demo traffic; document
  upgrading to a persistent store (SQLite, Redis) if usage scales.
- **No real authentication.** "Anyone with the URL can connect" is the
  *intended* model — same as today's open access. The OAuth dance is
  protocol theater. The corpus exposed is the party's public material;
  no confidential data is at risk.
- **Doubled hosting cost during co-existence** (resolved — see follow-up below).
  Two Fly apps (`ora-mcp` + `ora-mcp-claudeai`) ran simultaneously for
  ~hours = ~$6.40/mo total. The original `ora-mcp` app was destroyed once
  `ora-mcp-claudeai` was verified end-to-end.

**Reference.** `ora_mcp/auth.py` (provider), `ora_mcp/server.py` lines
near the `FastMCP(...)` constructor (wiring), `demo/README.md` (updated
recipient guidance), MCP SDK at `mcp/server/auth/provider.py` (the
protocol we implement).

**Follow-up executed 2026-05-24.** After end-to-end verification in
claude.ai web (all four demo queries passed, including the
"doesn't-invent" Mars edge case), the original `ora-mcp` Fly app was
destroyed via `fly apps destroy ora-mcp` (~$3.19/mo saved).

Later the same day, the user opted for full consolidation: the local
`C:\Users\ricca\Desktop\ora-mcp\` folder was **deleted** after moving
its three excluded-from-clone contents (`corpus/`,
`build/youtube_pipeline/`, `Distill YT info/`) into `ora-mcp-claudeai/`,
and after migrating the Claude Code memory directory from
`.claude/projects/C--Users-ricca-Desktop-ora-mcp/memory/` to
`.claude/projects/C--Users-ricca-Desktop-ora-mcp-claudeai/memory/`.

End state (2026-05-24): a single project folder at
`C:\Users\ricca\Desktop\ora-mcp-claudeai\` containing runtime code
(with OAuth), corpus source files, build pipeline, YouTube ingest
tools, and demo kit. A single live Fly app `ora-mcp-claudeai`. A
single Claude Code project memory directory keyed on the new path.
~$3.19/mo total Fly cost; ~$8/year if kept running through demo
period.

**Further consolidation 2026-05-25.** The standalone `ora-mcp-claudeai/`
folder was later merged into a single monorepo at
`C:\Users\ricca\Desktop\ORA Projects\ORA-Chatbot-monorepo\` (alongside
the chatbot project as `chatbot/`). The Fly app name (`ora-mcp-claudeai`),
public URL, and live state are unchanged — only the local folder path
moved. See D02's reversal note for the rationale.

---

# Known issues (open as of 2026-05-23 end of session)

## Issue 1 — `find_position` latency (~60 seconds) exceeds Claude Desktop's tool timeout  ✅ RESOLVED 2026-05-24 (see D31)

**Symptom.** When called from Claude Desktop, `find_position` queries
hit the client's tool-call timeout (~60 seconds) before completing.
Claude Desktop shows: *"Failed to call tool 'find_position'. Tool result
could not be submitted. The request may have expired or the connection
was interrupted."*

**Root cause.** `find_position` performed **four sequential pipelines**
(official_party, boldrin, forchielli, supporting_data), and each pipeline
runs a Voyage rerank over 50 candidate chunks (`RETRIEVE_TOP_K_INITIAL`).
Per-rerank latency on `voyage-rerank-2.5` is ~10-15 seconds. Total:
~45-60 seconds per call, plus MCP-remote stdio bridge overhead. With
`include_comparison=True` it added another rerank (~75 seconds total).

**Why our smoke tests didn't catch this.** The Python smoke harness has
no client timeout. The 60-second tool calls ran to completion and
produced correct results — which is why the 105-test acceptance suite is
all green. The timeout only surfaces when the client (Claude Desktop) is
in the loop.

**Resolution (D31, 2026-05-24).** Parallelized the four bucket queries
with `asyncio.gather` + `asyncio.to_thread`. The bucket pipelines are
independent (same query vector, different payload filter) so they fan
out concurrently after the single shared embed step. `find_position`
is now async; FastMCP awaits it directly; the 6 sync test call sites
were updated to wrap with `asyncio.run(...)`. Full rationale and
trade-offs in D31 above. Expected end-to-end latency: ~15 s.

**Secondary mitigations still available (not applied).** Lower
`RETRIEVE_TOP_K_INITIAL` from 50 to 25 (halves rerank cost). Switch to
`voyage-rerank-2.5-lite` if available (marginal precision loss for ~3×
speedup). Stream partial results via MCP progress notifications (more
complex, but Anthropic's own MCPs use this). Defer until/unless the
parallelized version still feels slow in practice.

**Severity (post-fix).** No longer a blocker. Re-verify with
`tests/comprehensive_report.py` and a live Claude Desktop call before
the next demo.

## Issue 2 — Server process is not supervised

**Symptom.** Server runs as a foreground Python process. Computer reboot,
PowerShell close, or accidental Ctrl+C all kill it. Once dead,
`mcp-remote` keeps failing with ECONNREFUSED until manually restarted.

**Planned fix.** Wrap with Windows Task Scheduler (auto-restart on
failure) or `nssm` to run as a Windows service. For Fly.io deploy this
is automatic (Fly's process manager restarts crashed containers).

**Severity.** Operational, not a blocker for a short demo, but pre-demo
prep should include re-verifying server is up.

## Issue 3 — One privacy probe returned high-score leader chunks

**Symptom.** Test `Boldrin moglie figli vita privata famiglia` in section
H returned `leader_views.boldrin` chunks with top score 0.84 — high
enough that the LLM would treat them as relevant.

**Investigation needed.** Open `comprehensive_test_report.pdf`, expand
the test, read the actual chunks. If the content is public-domain
biography (career, founding date, etc.) — acceptable. If it contains
private family information that was scraped without consent — the
corpus must be cleaned via `build/audit_frontmatter.py` + selective
exclusion before any external demo.

**Severity.** Reputational risk if not investigated before demo.

```
