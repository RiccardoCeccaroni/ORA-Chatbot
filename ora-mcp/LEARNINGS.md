# Learnings from building the ORA! MCP server

Notes for the project creator on the architectural decisions behind this
codebase. Each section captures the **principle** that generalizes — the
goal is to be able to explain the reasoning in conversation (or replicate
it elsewhere) without re-reading the code.

For the full audit trail with alternatives and code references, see
`DECISIONS.md` (D01–D32). This document is the distilled "what I'd
remember a year from now".

---

## 1. When MCP makes more sense than a chatbot

A chatbot **generates utterances** on behalf of someone. An MCP server
**exposes data and tools** to whatever AI the user is already using. The
risk surface is dramatically smaller — your software never speaks. For
an organization that cares about being misquoted (a political party,
a brand, a legal department), this matters a lot.

When the chatbot for ORA! was rejected by management, the value of the
work (curated corpus, retrieval logic, chunking pipeline) didn't go
away. We just changed the consumer: instead of *our* synthesizer reading
the chunks, *Claude Desktop's user* reads them through Claude. ~60-70%
of the original project's infrastructure carried over without changes.

**Generalizable principle.** If the user already has a great AI
assistant, you don't need to ship one. Ship *capabilities* to their
assistant via MCP. Smaller scope, smaller risk, broader audience (Claude,
Cursor, ChatGPT-with-MCP — you don't pick a client).

---

## 2. Tool design: one structured tool > several overlapping tools

Our first iteration had two tools: a generic `corpus_retrieve` (flat
ranked list) and a more opinionated `find_position` (structured buckets).
When you give an LLM two tools that could *both* answer "what does ORA!
think about X?", the model picks inconsistently across users — sometimes
the flat list, sometimes the structured one. Output quality degrades.

We collapsed to a single `find_position` tool whose return *shape*
enforces the trust hierarchy: separate dict keys for the party's
official voice, leaders' personal opinions, supporting data, and
(optional) other-party comparisons. The AI cannot accidentally conflate
them because they were never in the same list.

**Generalizable principle.** When designing tools for LLMs, enforce
invariants via *response shape*, not docstring instructions. Two
overlapping tools is a documented failure mode — collapse them. A second
tool is only justifiable when its trigger is unambiguous (e.g. our
`data_lookup` takes a metric name, not a topic — no plausible query
routes to both).

---

## 3. Retrieval pattern: dense ANN + cross-encoder rerank, organized by trust tier

The pipeline is the modern RAG default: embed the query once, do
approximate nearest-neighbor search in Qdrant to fetch ~50 candidates,
then rerank with Voyage's cross-encoder. The rerank step is where the
quality comes from — ANN is fast but noisy.

What's specific to this project: we don't return a flat top-10. We
**bucket by attribution** (party / leader Boldrin / leader Forchielli /
supporting data / optionally other parties). This guarantees each tier
gets fair representation — a flat top-10 could easily be 10× party voice
with zero leader content, defeating the trust hierarchy. The same query
vector is reused across buckets; only the payload filter changes.

**Generalizable principle.** Retrieval quality on a corpus with
mixed-trust sources isn't just "top-k similar". It's "balanced
representation across the structural categories the consumer cares
about". Encode those categories in metadata at ingest time, filter at
query time.

---

## 4. Async parallelization for I/O-bound calls

The first version of `find_position` ran four retrieval pipelines
sequentially. ~10–15s per pipeline × 4 = ~60s end-to-end. Claude
Desktop's tool-call timeout is ~60s. Live demos failed.

The fix: `asyncio.gather` over the four pipelines. Same total Voyage
cost, but compressed into the time of the slowest single pipeline (~15s
instead of 60s). Because Qdrant and Voyage SDKs are sync, we wrap each
call in `asyncio.to_thread` so they run on the asyncio thread pool while
the event loop stays free.

```python
qvec = await asyncio.to_thread(_embed, topic)  # do once, reuse across buckets
results = await asyncio.gather(
    asyncio.to_thread(_bucket, ["party"]),
    asyncio.to_thread(_bucket, ["boldrin"]),
    asyncio.to_thread(_bucket, ["forchielli"]),
    asyncio.to_thread(_data_lookup, ...),
)
```

**Generalizable principle.** For I/O-bound work (network calls), the
right primitive is `asyncio.gather` over `asyncio.to_thread`-wrapped
sync calls. You don't need to migrate to an async SDK to get
parallelism. **One caveat we discovered the hard way:** be aware of
upstream rate limits. Compressing the same total cost into a shorter
time window can trigger TPM/RPM throttling that sequential code would
never hit. Our 105-test acceptance suite went from 0 red to 45 red
after parallelization, all rate-limit errors — production single-user
traffic was fine, but the bulk test loop hit Voyage's 2M-tokens-per-minute cap.

---

## 5. Tool docstrings are the AI's interface contract

When an MCP client connects, it pulls the tool docstrings and passes
them verbatim to the host AI as part of the tool schema. **That's the
only instruction surface you have** — you can't inject a system prompt.
So docstrings need to do more work than "describe the function":

- State the trust hierarchy ("⚠️ NEVER attribute leader_views to the party")
- Describe each bucket's epistemic status
- Give a typical answer pattern ("1. report official, 2. mention leaders as personal, ...")
- State what to do when results are empty ("the party hasn't articulated a position — say so explicitly")

**Generalizable principle.** When designing for LLM consumers, the
docstring isn't documentation — it's the prompt. Write it like one.
Verbose, explicit, opinionated. ~600 tokens per tool is reasonable.

---

## 6. Resources vs tools

MCP exposes two surfaces: **tools** (dynamic, parameterized — "search
the corpus for X") and **resources** (static documents — "the
manifesto"). The discipline: ship a resource when the AI might want to
quote the whole thing verbatim; ship a tool when the answer depends on
what was asked.

We ship the full manifesto (~575 KB) as a resource because the AI might
be asked "what does the manifesto say about Y?" and direct quotation
beats paraphrased chunks. We ship search as a tool because no one is
going to pre-load the full corpus into context.

**Generalizable principle.** If it's small enough to fit in context
*and* you'd want the AI to quote rather than paraphrase, it's a
resource. Otherwise it's a tool.

---

## 7. Auth: open + rate-limited

We didn't add API keys. Rate limit: 30 req/min/IP via a 30-line
in-memory sliding-window middleware. Reasoning:

- The audience is "anyone using a modern AI assistant" — gating with
  keys reduces reach for a public-good service.
- Adding API keys creates a key-management surface (issuance, rotation,
  revocation) the demo doesn't justify.
- If abuse becomes a problem, keys can be added later without breaking
  the public-URL contract.

**Generalizable principle.** Scope auth to actual risk. For a read-only
public service, rate limit is enough. API keys are a one-way door of
operational complexity — defer until needed.

---

## 8. Hosting trade-offs: Docker + Fly.io vs. Cloudflare Tunnel

Two hosting models, two trade-offs:

- **Docker + Fly.io.** Professional URL (`ora-mcp.fly.dev`), survives
  laptop being off, auto-restart on crash. Requires credit card + small
  ongoing cost (~$0–2/month for our config with `auto_stop_machines`).
- **Cloudflare Tunnel.** Free, no card, ~30-second setup. URL is
  ephemeral (`*.trycloudflare.com`) and the service is only up while the
  laptop is on and the tunnel daemon is running.

We pivoted from Fly to Cloudflare Tunnel for the demo (D32). For
production, the Docker image is portable to any host.

**Generalizable principle.** For a demo, optimize for friction (zero
setup, zero cost). For production, optimize for resilience (managed
host, supervised process, monitoring). The decision is about *audience*
and *time horizon*, not technology — the same Docker image runs on both.

---

## 9. The `mcp-remote` bridge

Claude Desktop's config schema only accepts MCPs that launch as stdio
subprocesses — there's no native "HTTP MCP URL" field. Our server is
HTTP-transport (Fly-friendly, public-friendly).

The bridge: a tiny npm package called `mcp-remote` that acts as a
stdio↔HTTP adapter. Claude Desktop launches it as a subprocess; it
connects to our HTTP server. From the user's perspective, it just works.

```json
"ora": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://your-mcp-url/mcp"]
}
```

**Generalizable principle.** When client A and server B can't talk
natively, find the standard adapter — don't write your own. Look for
npm / PyPI / etc. packages that bridge transports. Saves you a custom
client and gets you the maintenance for free.

---

## 10. Real bugs and what they taught

**Bug A — attribution string mismatch.** We assumed Qdrant payloads
tagged ORA!'s official chunks with `attribution = "ora"`. The actual
value was `"party"`. Every smoke test for "what does ORA think about
X?" returned an empty `official_party` bucket. The fix was trivial
(look up the actual value, define a constant, use it). The lesson:
when porting code that filters on string-valued metadata, **probe the
live data** for the actual values before trusting any constant in the
source. Comments rot; data is ground truth.

**Bug B — FastMCP lifespan not forwarded when mounted.** When we
mounted the FastMCP sub-app inside a parent Starlette app (to add a
landing page + health endpoint), every request to `/mcp` returned
`500: Task group is not initialized`. Cause: Starlette doesn't
propagate sub-app lifespans automatically. The fix is a 4-line context
manager that wraps and re-yields the sub-app's lifespan. The lesson:
framework integrations have **hidden contracts**. When a sub-app fails
on its first request with an error mentioning "task group" or "not
initialized", check whether the framework expects you to wire
lifespan/startup events through manually.

**Bug C — Fly HA load-balancing breaks in-memory MCP sessions.** With
`min_machines_running >= 1` + `auto_stop_machines = "stop"`, Fly's
default is to provision **two** machines per app for zero-downtime
deploys. Requests are round-robined across both. The MCP streamable HTTP
transport keeps **session state in process memory**: the first POST
creates session ID X on machine A; the follow-up POST may land on
machine B which has never heard of session X → 404 "Session not found".
The client (Claude Desktop / claude.ai) sees an endless 404 loop. The
fix that was right for us: `fly scale count 1` (single machine, accept
~5s downtime per deploy). The general fix: shared session storage
(Redis, etc.) or sticky sessions. The lesson: any **stateful protocol
with in-memory state** is incompatible with naive load-balancing; check
your hosting provider's HA defaults before deploying a session-heavy
service.

**Bug D — `mcp-remote` SSE fallback can silently fail.** Without
`--transport http-only` in `mcp-remote`'s args, it tries Server-Sent
Events transport first, then falls back to streamable HTTP. FastMCP
serves the latter, not SSE. The initial SSE attempt fails and — in
some Claude Desktop versions — surfaces as a generic "Couldn't reach
the MCP server" error before the fallback even runs. Add `--transport
http-only` to skip SSE entirely. The lesson: when a bridge/adapter
supports multiple transports, **explicitly pin the one your server
implements** — autodetection can produce confusing error messages
during the failed-attempt phase.

**Bug E — splatting routes loses middleware.** When we removed
`Mount("/mcp", _mcp_app)` and instead spread `*_mcp_app.routes` into the
parent Starlette to put OAuth routes at root (see Bug F below), the
sub-app's `AuthenticationMiddleware(BearerAuthBackend(...))` did not
come along — it was attached to the sub-app, not to its routes. Every
authenticated request landed without `scope["user"]` set, so
`RequireAuthMiddleware` returned 401 even for valid tokens. The fix:
re-attach the middleware on the parent Starlette manually. The lesson:
in Starlette, **middleware belongs to the app, routes belong to the
router** — they're separate structures. Composing apps by splatting
routes is convenient but you have to consciously bring middleware
along too.

**Bug F — OAuth metadata advertised endpoints that didn't exist there.**
With `auth_server_provider` configured, FastMCP auto-registers
`/.well-known/oauth-authorization-server`, `/authorize`, `/token`,
`/register` inside its sub-app **at root level**. The metadata it
returns advertises those endpoints with root-level URLs
(`https://host/authorize`, etc.). When the sub-app is `Mount`ed under
`/mcp`, the actual routes live at `/mcp/authorize` etc. — but the
metadata still says `/authorize`. claude.ai's connector flow follows
the metadata, gets 404, and reports "Couldn't reach the MCP server"
even though the server is up. Fix: don't mount the sub-app; splat its
routes into the parent so reality matches the metadata. The lesson:
when a framework generates **self-describing metadata** (well-known
endpoints, OpenAPI specs, etc.), the metadata's URLs assume a deployment
topology. If you change the topology (mount paths, reverse proxy
rewrites), the metadata becomes a lie. Always verify
`metadata.url == request.url` round-trip after any mount/prefix change.

**Generalizable principle.** Six real bugs in this project, three from
today alone. None would have been caught by unit tests because they're
all **integration-shaped**: framework × transport × hosting-provider ×
client. The takeaway isn't "test more" — it's that running **a real
query end-to-end against real infrastructure with the real client**
(here: claude.ai's connector flow, not a curl smoke test) catches the
bugs that any number of mocks would miss. Smoke tests are not optional;
neither is testing with the actual production client.

---

## What I'd reuse in another project

- The **single-structured-tool** pattern (Section 2)
- The **dense-ANN + rerank + bucketed-by-attribution** retrieval shape (Section 3)
- The **`asyncio.gather + asyncio.to_thread`** recipe for parallelizing sync SDK calls (Section 4)
- The **verbose-docstring-as-prompt** approach for any LLM-consumable interface (Section 5)
- The **"tunnel for demos, real host for production"** framing (Section 8)
- The **"probe before trusting"** rule for any port of code that depends on data shape (Section 10, Bug A)
- The **"middleware vs routes are separate when composing Starlette apps"** trap (Section 10, Bug E)
- The **"self-describing metadata vs deployment topology"** trap (Section 10, Bug F)
- The **"check your hosting HA defaults for stateful services"** rule (Section 10, Bug C)

---

## Things this project intentionally does NOT do

Worth remembering — these were *active* decisions, not omissions:

- **No CI/CD pipeline.** Premature optimization before adoption.
- **No unit tests.** Retrieval quality is not a unit-test concern; the
  105-test acceptance suite produces a human-readable PDF instead.
- **No structured logging / metrics backend.** Stdout to Fly logs is
  enough for a demo.
- **No verifier / synthesizer / agent runtime.** Generation belongs to
  the host AI, not the MCP.
- **No web_search tool.** Host AIs already have web search.
- **No API keys.** Rate limit is sufficient for a read-only public
  service.

The pattern in all of these: **scope to the demo, leave the production
path open**. Every "no" above has a clear "when ORA! adopts, add this"
follow-up in `DECISIONS.md`.
