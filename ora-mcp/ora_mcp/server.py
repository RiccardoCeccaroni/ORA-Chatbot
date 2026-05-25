"""ORA! MCP server.

Exposes the ORA! party's curated corpus to AI assistants via the Model
Context Protocol (streamable HTTP transport). Two tools and five resources:

Tools
-----
- find_position(topic, ...): structured retrieval, returns trust-hierarchy
  buckets (official_party / leader_views / supporting_data / comparison).
- data_lookup(metric, ...): empirical stat-card lookup, quality-tiered.

Resources
---------
- ora://about         — identity card + trust hierarchy guide
- ora://manifesto     — full party manifesto (21 thesis documents)
- ora://statuto       — party bylaws
- ora://fondamenti    — 15 policy fundamentals (Allegato 2)
- ora://codice-etico  — code of ethics (Allegato 3)

Run locally:
    python -m ora_mcp.server

The MCP endpoint is mounted at /mcp; a human-readable landing page lives
at / for visitors who hit the URL in a browser.
"""

from __future__ import annotations

import os
import time
from collections import deque
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any


def _load_dotenv(path: Path = Path(".env")) -> None:
    """Minimal .env loader so the server works whether launched from a shell
    that exported the vars, or as a subprocess (e.g. by Claude Desktop via
    mcp-remote) that didn't. os.environ values already set win."""
    candidates = [Path.cwd() / path, Path(__file__).resolve().parent.parent / path]
    for p in candidates:
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())
        return


_load_dotenv()

from mcp.server.auth.middleware.auth_context import AuthContextMiddleware
from mcp.server.auth.middleware.bearer_auth import BearerAuthBackend
from mcp.server.auth.provider import ProviderTokenVerifier
from mcp.server.auth.settings import AuthSettings, ClientRegistrationOptions
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse
from starlette.routing import Mount, Route

from ora_mcp.auth import PermissiveOAuthProvider
from ora_mcp.retrieval import data_lookup as _data_lookup
from ora_mcp.retrieval import find_position as _find_position


# ----------------------------------------------------------------------------
# MCP server: tools + resources
# ----------------------------------------------------------------------------

# IMPORTANT: we DO NOT set streamable_http_path here (default is "/mcp") and
# we DO NOT Mount the FastMCP sub-app under a prefix below. Reason: when the
# auth_server_provider is configured, FastMCP registers the OAuth metadata
# endpoints (`/.well-known/oauth-authorization-server`,
# `/.well-known/oauth-protected-resource`, `/authorize`, `/token`,
# `/register`) at root level in the sub-app's router, and the metadata it
# returns advertises them at root level (e.g. `issuer = https://host/`,
# `authorization_endpoint = https://host/authorize`). If we Mount the sub-app
# under `/mcp`, the actual endpoints land at `/mcp/authorize` etc. while
# the metadata still claims they're at root -- claude.ai's connector handshake
# follows the metadata, gets 404, and reports "Couldn't reach the MCP server".
# To keep metadata and reality consistent, we leave FastMCP unmounted: its
# routes are added to the parent Starlette app at the top level. See D33.
#
# transport_security: FastMCP defaults to DNS-rebinding protection that
# rejects any Host header not in a small built-in allowlist (localhost
# only). Must explicitly allow the public deployment hostname.
#
# auth_server_provider + auth: enables OAuth 2.1 so claude.ai's custom
# connector flow can complete the handshake. See D33 and ora_mcp/auth.py.
_auth_provider = PermissiveOAuthProvider()
_token_verifier = ProviderTokenVerifier(_auth_provider)

mcp = FastMCP(
    "ORA!",
    transport_security=TransportSecuritySettings(
        allowed_hosts=[
            "localhost",
            "localhost:8000",
            "127.0.0.1",
            "127.0.0.1:8000",
            "ora-mcp-claudeai.fly.dev",
        ],
    ),
    auth_server_provider=_auth_provider,
    auth=AuthSettings(
        issuer_url="https://ora-mcp-claudeai.fly.dev",
        resource_server_url="https://ora-mcp-claudeai.fly.dev",
        client_registration_options=ClientRegistrationOptions(enabled=True),
        required_scopes=[],
    ),
)


@mcp.tool()
async def find_position(
    topic: str,
    top_k_per_bucket: int = 5,
    include_comparison: bool = False,
    include_leaders: bool = True,
    date_from: str | None = None,
    date_to: str | None = None,
) -> dict[str, Any]:
    """Find ORA!'s position on a topic, organized by trust hierarchy.

    ORA! is the Italian centrist party founded by Michele Boldrin and
    Alberto Forchielli. This is the PRIMARY tool for any question of the
    form "what does ORA think about X?" — use it whenever the user wants
    the party's stance on any policy area, current event, or value.

    The response is a dict with structured buckets, NOT a flat ranked list.
    Each bucket has a different epistemic status — please respect it when
    answering the user:

      official_party : Party voice. The authoritative answer. Quote these
                       chunks when reporting "ORA's position is…".
                       Sourced from manifesto, comunicati, statuto,
                       fondamenti, codice etico, newsletter, party events.

      leader_views   : Personal views of Boldrin and Forchielli, organized
                       per leader. ⚠️ NEVER attribute to the party — these
                       are gap-fill personal opinions. Phrase as
                       "Boldrin personalmente sostiene…", not "ORA dice…".

      supporting_data: Empirical stat-cards from ISTAT, Eurostat, OECD,
                       and similar institutional sources. Use to ground
                       quantitative claims. Cite quality_tier
                       (D1=ISTAT/Banca d'Italia, D2=international, D3=other
                       institutional) and the data_period.

      comparison     : (Only if include_comparison=True.) Positions of
                       the 8 other Italian parties indexed in the corpus
                       (azione, pd, fdi, lega, fi, avs, iv, m5s). Each
                       chunk's `attribution` field names the party. Set
                       include_comparison=True ONLY when the user
                       explicitly asks for a comparison.

    Each chunk is a dict with: text, source_doc, tier, attribution,
    doc_type, date_published, chunk_id, parent_id, _rerank_score, extras.

    Typical answer pattern:
      1. Report the official party position from `official_party`, citing
         source_doc.
      2. If `leader_views` adds nuance, mention it explicitly as a personal
         leader view.
      3. If a quantitative claim is involved, cite `supporting_data`.
      4. If the user asked for comparison, contrast with `comparison`.

    If `official_party` is empty for a topic, the party hasn't articulated
    a position — say so explicitly rather than synthesizing one from leader
    views or unrelated chunks.
    """
    return await _find_position(
        topic=topic,
        top_k_per_bucket=top_k_per_bucket,
        include_comparison=include_comparison,
        include_leaders=include_leaders,
        date_from=date_from,
        date_to=date_to,
    )


@mcp.tool()
def data_lookup(
    metric: str,
    period: str | None = None,
    quality_tier_floor: str = "D3",
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Look up empirical stat-cards from ORA!'s data tier.

    Use this for quantitative questions: "How much does Italy spend on
    pensions?", "What is the youth unemployment rate?", "Italian GDP
    growth 2023". The data tier is curated from ISTAT, Eurostat, OECD,
    Banca d'Italia, and equivalent institutional sources.

    Quality tiers (filter via `quality_tier_floor`):
      - D1 — national statistical agencies (ISTAT, Banca d'Italia). Highest.
      - D2 — international (Eurostat, OECD, IMF, World Bank).
      - D3 — institutional reports (ministries, think tanks, peer-reviewed).
      - D4 — advocacy / partisan sources. EXCLUDED by default.
      The default floor "D3" accepts D1+D2+D3, rejects D4.

    `metric` is free-text Italian (e.g., "tasso di disoccupazione giovanile",
    "spesa pensionistica"). `period` is optional (e.g., "2023", "Q4 2024").

    Returns stat-cards ordered by quality tier (D1 first) then relevance.
    Each card includes data_metric, data_period, quality_tier, source_doc
    in `extras`.
    """
    return _data_lookup(
        metric=metric,
        period=period,
        quality_tier_floor=quality_tier_floor,
        top_k=top_k,
    )


# ----------------------------------------------------------------------------
# Resources: ground-truth documents the host AI can pre-load
# ----------------------------------------------------------------------------

_RESOURCES_DIR = Path(__file__).resolve().parent / "resources"
_LOGO_PATH = _RESOURCES_DIR / "logo.png"


def _read_resource(filename: str) -> str:
    return (_RESOURCES_DIR / filename).read_text(encoding="utf-8")


@mcp.resource("ora://about")
def about() -> str:
    """ORA! — who they are, the four objectives, the trust hierarchy.

    Read this first to understand the party and how to use the tools well.
    """
    return _read_resource("about.md")


@mcp.resource("ora://manifesto")
def manifesto() -> str:
    """ORA!'s full manifesto — the 21 thesis documents.

    The canonical, ground-truth statement of the party's positions. Quote
    verbatim when answering "what does ORA think about X?".
    """
    return _read_resource("manifesto_full.md")


@mcp.resource("ora://statuto")
def statuto() -> str:
    """ORA!'s statuto — the party's governance bylaws.

    Defines how the party is structured, how officers are elected, how
    decisions are made, and members' rights and duties. Quote verbatim for
    questions about governance and internal rules.
    """
    return _read_resource("statuto.md")


@mcp.resource("ora://fondamenti")
def fondamenti() -> str:
    """ORA!'s fondamenti — the 15 policy fundamentals (Allegato 2 dello statuto).

    The non-negotiable policy commitments every member subscribes to. A more
    compact statement of identity than the full manifesto; useful to anchor
    "what does ORA stand for at minimum?".
    """
    return _read_resource("fondamenti.md")


@mcp.resource("ora://codice-etico")
def codice_etico() -> str:
    """ORA!'s codice etico — the code of ethics (Allegato 3 dello statuto).

    Conduct standards for members and officers, conflict-of-interest rules,
    sanctions. Quote verbatim for ethics / accountability questions.
    """
    return _read_resource("codice-etico.md")


# ----------------------------------------------------------------------------
# Rate limiting: simple in-memory sliding window per IP
# ----------------------------------------------------------------------------

_RATE_LIMIT = int(os.environ.get("RATE_LIMIT_PER_MINUTE", "30"))
_WINDOW_SECONDS = 60
_ip_hits: dict[str, deque[float]] = {}


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Sliding-window per-IP rate limit on the /mcp endpoint.

    Resource reads and the landing page are not rate-limited.
    """

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if path.startswith("/mcp"):
            ip = request.client.host if request.client else "unknown"
            now = time.monotonic()
            hits = _ip_hits.setdefault(ip, deque())
            cutoff = now - _WINDOW_SECONDS
            while hits and hits[0] < cutoff:
                hits.popleft()
            if len(hits) >= _RATE_LIMIT:
                return JSONResponse(
                    {"error": "rate_limited", "limit_per_minute": _RATE_LIMIT},
                    status_code=429,
                )
            hits.append(now)
        return await call_next(request)


# ----------------------------------------------------------------------------
# Landing page + health check
# ----------------------------------------------------------------------------

_LANDING_HTML = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>ORA! MCP server</title>
<link rel="icon" type="image/png" href="/logo.png">
<meta property="og:title" content="ORA! — MCP server">
<meta property="og:description" content="MCP server che espone il corpus curato del partito ORA! agli assistenti AI (Claude, Cursor, ChatGPT con MCP).">
<meta property="og:image" content="__BASE_URL__/logo.png">
<meta property="og:url" content="__BASE_URL__">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="__BASE_URL__/logo.png">
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         max-width: 720px; margin: 3rem auto; padding: 0 1rem; line-height: 1.55;
         color: #222; }
  .hero { text-align: center; margin-bottom: 1.5rem; }
  .hero img { max-width: 180px; height: auto; border-radius: 12px;
              box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
  h1 { font-size: 1.8rem; text-align: center; margin: 0.5rem 0 2rem; }
  code, pre { background: #f4f4f6; padding: 0.1rem 0.35rem; border-radius: 4px;
              font-size: 0.92rem; }
  pre { padding: 0.8rem 1rem; overflow-x: auto; }
  .pill { display: inline-block; background: #eef; color: #224; padding: 0.1rem 0.5rem;
          border-radius: 999px; font-size: 0.8rem; margin-right: 0.4rem; }
  footer { margin-top: 3rem; color: #666; font-size: 0.85rem; }
</style>
</head>
<body>
  <div class="hero">
    <img src="/logo.png" alt="ORA!">
  </div>
  <h1>ORA! &mdash; MCP server</h1>
  <p>
    <span class="pill">MCP</span>
    <span class="pill">streamable HTTP</span>
    <span class="pill">italiano</span>
  </p>
  <p>
    Questo server espone il corpus curato del partito <strong>ORA!</strong>
    (posizioni ufficiali, manifesto, viste dei fondatori, dati ISTAT) agli
    assistenti AI che parlano il protocollo MCP &mdash; per esempio Claude
    Desktop, Cursor, o ChatGPT con plugin MCP.
  </p>
  <h2>Cosa offre</h2>
  <p><strong>Tool:</strong></p>
  <ul>
    <li><code>find_position(topic)</code> &mdash; posizione di ORA! su un tema,
        organizzata in <em>buckets</em> per affidabilità: voce ufficiale del
        partito, viste personali dei leader, dati a supporto, opzionalmente
        confronto con altri partiti.</li>
    <li><code>data_lookup(metric)</code> &mdash; schede statistiche
        (ISTAT, Eurostat, OECD), ordinate per qualità della fonte.</li>
  </ul>
  <p><strong>Resources:</strong></p>
  <ul>
    <li><code>ora://about</code> &mdash; carta d'identità del partito.</li>
    <li><code>ora://manifesto</code> &mdash; manifesto completo (21 tesi).</li>
    <li><code>ora://statuto</code> &mdash; statuto del partito.</li>
    <li><code>ora://fondamenti</code> &mdash; 15 fondamenti programmatici.</li>
    <li><code>ora://codice-etico</code> &mdash; codice etico.</li>
  </ul>
  <h2>Come collegarsi a Claude Desktop</h2>
  <p>Apri <code>claude_desktop_config.json</code>
     (<em>Settings &rarr; Developer &rarr; Edit Config</em>) e aggiungi
     il blocco corrispondente al tuo sistema operativo:</p>

  <p><strong>macOS / Linux:</strong></p>
  <pre>{
  "mcpServers": {
    "ora": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "__BASE_URL__/mcp", "--transport", "http-only"]
    }
  }
}</pre>

  <p><strong>Windows:</strong></p>
  <pre>{
  "mcpServers": {
    "ora": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-remote", "__BASE_URL__/mcp", "--transport", "http-only"]
    }
  }
}</pre>

  <p>Salva e riavvia Claude Desktop. I tool <code>find_position</code> e
     <code>data_lookup</code> appariranno nell'elenco dei tool disponibili
     e potrai chiedere <em>"Qual &egrave; la posizione di ORA! su X?"</em>.</p>
  <footer>
    Demo MCP per il partito ORA! &mdash; <a href="/health">/health</a> &middot;
    <a href="https://modelcontextprotocol.io">protocollo MCP</a>
  </footer>
</body>
</html>
"""


async def landing(request: Request) -> HTMLResponse:
    base_url = str(request.base_url).rstrip("/")
    return HTMLResponse(_LANDING_HTML.replace("__BASE_URL__", base_url))


async def health(_: Request) -> PlainTextResponse:
    return PlainTextResponse("ok")


async def logo(_: Request) -> FileResponse:
    return FileResponse(_LOGO_PATH, media_type="image/png")


# ----------------------------------------------------------------------------
# Starlette ASGI app: include FastMCP routes at root + add landing/health/logo
# ----------------------------------------------------------------------------

# Build the FastMCP sub-app once so we can forward its lifespan into the
# parent app. Without forwarding, Starlette does NOT trigger the sub-app's
# lifespan handlers, which leaves FastMCP's session manager uninitialized and
# every POST to /mcp blows up with "Task group is not initialized". See D25.
_mcp_app = mcp.streamable_http_app()


@asynccontextmanager
async def _lifespan(_):
    async with _mcp_app.router.lifespan_context(_mcp_app):
        yield


# Compose routes: our landing/health/logo at the top, then ALL of FastMCP's
# routes at root level. FastMCP's routes include the MCP endpoint at /mcp,
# the OAuth endpoints (/authorize, /token, /register, /.well-known/*), and
# resource endpoints — all already root-relative. See D33 for why we do
# this instead of Mount("/mcp", _mcp_app).
# Auth middleware: when FastMCP builds its own sub-app it attaches these to
# its Starlette() automatically (see mcp.server.fastmcp.server.streamable_http_app
# lines ~978-985 in the SDK). Because we splat _mcp_app.routes into our parent
# Starlette without using the sub-app directly, we must re-attach the same
# middleware on the parent — otherwise the Bearer token in the Authorization
# header never becomes a `scope["user"]`, `RequireAuthMiddleware` sees no user,
# and every authenticated /mcp call returns 401 even with a valid token.
app = Starlette(
    debug=False,
    routes=[
        Route("/", landing),
        Route("/health", health),
        Route("/logo.png", logo),
        *_mcp_app.routes,
    ],
    middleware=[
        Middleware(RateLimitMiddleware),
        Middleware(AuthenticationMiddleware, backend=BearerAuthBackend(_token_verifier)),
        Middleware(AuthContextMiddleware),
    ],
    lifespan=_lifespan,
)


def main() -> None:
    """Entry point for `python -m ora_mcp.server`."""
    import uvicorn

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
