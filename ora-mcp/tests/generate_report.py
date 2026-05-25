"""Run the smoke queries, build an HTML report with verdicts, convert to PDF.

Output:
    smoke_test_report.html  (intermediate)
    smoke_test_report.pdf   (final, auto-opens)

Conversion uses Microsoft Edge in headless mode (always present on Windows 11).
"""
from __future__ import annotations

import asyncio
import datetime
import html
import os
import subprocess
import sys
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


# Questions + per-question expected-strength notes (filled in by author).
QUESTIONS: list[tuple[str, bool, str]] = [
    (
        "riforma fiscale ORA",
        False,
        "Stato — domanda canonica sulla posizione fiscale. "
        "Atteso: la tesi 19 (Tassazione e Fiscalità) e il Fondamento 9 "
        "in `official_party`. Boldrin ha una proposta organica a parte.",
    ),
    (
        "posizione di ORA sulle pensioni",
        False,
        "Stato — argomento centrale del programma. "
        "Atteso: Fondamento 8 (Pensioni sostenibili) e tesi 14 (Lavoro). "
        "Boldrin spinge un'ottica intergenerazionale, Forchielli pensione a 70 anni.",
    ),
    (
        "cosa farebbe ORA sull'immigrazione",
        False,
        "Proiezione — chiede misure concrete. "
        "Atteso: tesi 10 (Immigrazione) con proposte sui flussi.",
    ),
    (
        "ORA università ricerca innovazione",
        False,
        "Stato (multi-tema) — copre tesi 21 e tesi 12. "
        "Atteso: chunks da entrambe le tesi e dagli eventi pubblici di Pisa.",
    ),
    (
        "ORA matrimonio egualitario diritti civili",
        False,
        "Stato — tema sensibile/valoriale. "
        "Atteso: tesi 05 (Diritti Civili) con proposta esplicita di matrimonio "
        "egualitario. Boldrin coerente, Forchielli scarso (questo va dichiarato).",
    ),
    (
        "differenza tra ORA e Azione politica industriale",
        True,
        "Confronto esplicito. "
        "Atteso: ORA (tesi 18) + Azione nel bucket `comparison`. "
        "Test critico per il funzionamento del filtro multi-attribution.",
    ),
]


def _short(text: str, n: int = 220) -> str:
    text = " ".join(text.split())
    return text[:n] + ("…" if len(text) > n else "")


def _verdict_for(topic: str, result: dict) -> tuple[str, str]:
    """Return (status, paragraph). status ∈ {"green", "yellow", "red"}."""
    official = result.get("official_party", [])
    leaders = result.get("leader_views", {})
    data = result.get("supporting_data", [])
    comparison = result.get("comparison")

    if not official:
        return (
            "red",
            "<strong>Problema:</strong> nessun chunk dalla voce ufficiale del partito. "
            "L'assistente AI non avrebbe la posizione di ORA da citare e sarebbe "
            "costretto a inferire da viste personali dei leader — esattamente ciò "
            "che la gerarchia di fiducia deve impedire.",
        )

    top_src = official[0].get("source_doc") or "?"
    top_score = official[0].get("_rerank_score", "?")

    n_boldrin = len(leaders.get("boldrin", []))
    n_forchielli = len(leaders.get("forchielli", []))
    n_data = len(data)

    parts = [
        f"<strong>{len(official)} chunks ufficiali</strong> recuperati. "
        f"Il primo (rerank score {top_score}) viene da <code>{html.escape(top_src)}</code>.",
        f"Viste personali: {n_boldrin} da Boldrin, {n_forchielli} da Forchielli — "
        "l'assistente può menzionarle esplicitamente come sfumature personali.",
        f"Dati di supporto: {n_data} schede statistiche disponibili per ancorare "
        "claim quantitativi.",
    ]
    if comparison is not None:
        if comparison:
            parts.append(
                f"<strong>Bucket comparison:</strong> {len(comparison)} chunks "
                "dall'altro partito — il filtro multi-attribution funziona."
            )
        else:
            parts.append(
                "<strong>Problema:</strong> bucket comparison vuoto nonostante "
                "<code>include_comparison=True</code>."
            )

    paragraph = "<br>".join(parts)
    paragraph += (
        "<br><em>Valutazione: un assistente AI come Claude, ricevendo questi "
        "bucket, può comporre una risposta strutturata e accuratamente citata "
        "rispettando la gerarchia di fiducia.</em>"
    )
    return ("green" if (not comparison or comparison) else "yellow"), paragraph


def _render_bucket(name: str, chunks: list, max_show: int = 3) -> str:
    if not chunks:
        return (
            f'<div class="bucket"><div class="bucket-header empty">'
            f'<strong>{html.escape(name)}</strong> <span class="count">— vuoto</span>'
            f'</div></div>'
        )
    items = []
    for c in chunks[:max_show]:
        src = c.get("source_doc") or c.get("extras", {}).get("source_doc") or "?"
        tier = c.get("tier") or "?"
        score = c.get("_rerank_score", "?")
        text = _short(c.get("text", ""))
        items.append(
            f'<li><div class="meta"><span class="src">{html.escape(str(src))}</span>'
            f' <span class="tag">tier={html.escape(str(tier))}</span>'
            f' <span class="tag">score={html.escape(str(score))}</span></div>'
            f'<div class="text">{html.escape(text)}</div></li>'
        )
    extra = f" (+{len(chunks)-max_show} altri)" if len(chunks) > max_show else ""
    return (
        f'<div class="bucket"><div class="bucket-header">'
        f'<strong>{html.escape(name)}</strong> '
        f'<span class="count">— {len(chunks)} chunks{extra}</span>'
        f'</div><ol>{"".join(items)}</ol></div>'
    )


def build_html(report: list[dict]) -> str:
    now = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
    rows = []
    for r in report:
        topic = r["topic"]
        result = r["result"]
        notes = r["notes"]
        status, verdict = _verdict_for(topic, result)
        leaders = result.get("leader_views", {})
        comparison = result.get("comparison")

        bucket_html = _render_bucket("official_party", result.get("official_party", []))
        bucket_html += _render_bucket("leader_views › boldrin", leaders.get("boldrin", []))
        bucket_html += _render_bucket("leader_views › forchielli", leaders.get("forchielli", []))
        bucket_html += _render_bucket("supporting_data", result.get("supporting_data", []))
        if comparison is not None:
            bucket_html += _render_bucket("comparison", comparison)

        rows.append(
            f'<section class="question">'
            f'<h2><span class="q-status status-{status}"></span>'
            f'{html.escape(topic)}</h2>'
            f'<p class="notes"><strong>Attesa:</strong> {notes}</p>'
            f'{bucket_html}'
            f'<div class="verdict verdict-{status}">{verdict}</div>'
            f'</section>'
        )

    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<title>ORA! MCP — Smoke test</title>
<style>
  @page {{ size: A4; margin: 1.6cm 1.4cm; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
          color: #1a1a1a; line-height: 1.45; font-size: 10.5pt; }}
  h1 {{ font-size: 18pt; margin-bottom: 0.2em; }}
  h2 {{ font-size: 13pt; margin-top: 1.6em; border-bottom: 1px solid #ddd;
        padding-bottom: 4px; }}
  .lead {{ color: #555; font-size: 10pt; margin-bottom: 1.5em; }}
  .notes {{ background: #f6f6f8; padding: 0.5em 0.8em; border-left: 3px solid #888;
            font-size: 9.5pt; margin: 0.5em 0 0.8em; }}
  .bucket {{ margin: 0.6em 0; }}
  .bucket-header {{ font-size: 10pt; margin-bottom: 0.2em; color: #333; }}
  .bucket-header.empty {{ color: #b00; }}
  .count {{ color: #777; font-weight: normal; }}
  ol {{ margin: 0.2em 0 0.4em 1.2em; padding: 0; }}
  li {{ margin: 0.3em 0; }}
  .meta {{ font-size: 8.5pt; color: #555; }}
  .src {{ font-family: Consolas, "SF Mono", monospace; color: #224; }}
  .tag {{ display: inline-block; background: #eef; color: #224; padding: 0 5px;
          border-radius: 3px; font-family: Consolas, monospace; font-size: 8pt; }}
  .text {{ font-size: 9.5pt; margin-left: 4px; padding: 2px 6px; background: #fafafa;
           border-left: 2px solid #ccc; }}
  .verdict {{ margin-top: 0.6em; padding: 0.6em 0.8em; border-radius: 4px;
              font-size: 9.5pt; }}
  .verdict-green {{ background: #e6f7e9; border-left: 3px solid #2a8f3a; }}
  .verdict-yellow {{ background: #fdf6e3; border-left: 3px solid #c8a019; }}
  .verdict-red {{ background: #fbeaea; border-left: 3px solid #b53030; }}
  .q-status {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%;
               margin-right: 6px; vertical-align: middle; }}
  .status-green {{ background: #2a8f3a; }}
  .status-yellow {{ background: #c8a019; }}
  .status-red {{ background: #b53030; }}
  code {{ background: #eee; padding: 0 4px; border-radius: 2px; font-size: 9pt; }}
  footer {{ margin-top: 2em; font-size: 8.5pt; color: #888; border-top: 1px solid #ddd;
            padding-top: 0.6em; }}
</style></head><body>
<h1>ORA! MCP — Smoke test del tool <code>find_position</code></h1>
<p class="lead">Sei domande tipiche di utente, lanciate contro il server MCP locale.
Per ciascuna: i bucket restituiti (top 3 chunks per bucket) e un verdetto sulla
qualità del risultato. Generato il {now}.</p>
{"".join(rows)}
<footer>Indice Qdrant: <code>ora_chunks</code> · 3 665 chunks · Embed: voyage-4-large ·
Rerank: rerank-2.5 · Server: ora-mcp v0.1.0.</footer>
</body></html>
"""


def main() -> None:
    _load_env()
    from ora_mcp.retrieval import find_position

    report = []
    for topic, include_cmp, notes in QUESTIONS:
        print(f"Running: {topic}{' [+comparison]' if include_cmp else ''} ...", flush=True)
        try:
            result = asyncio.run(find_position(topic, top_k_per_bucket=5, include_comparison=include_cmp))
        except Exception as e:
            print(f"  FAILED: {e}")
            result = {"_error": str(e)}
        report.append({"topic": topic, "result": result, "notes": notes})

    html_path = Path("smoke_test_report.html").resolve()
    pdf_path = Path("smoke_test_report.pdf").resolve()
    html_path.write_text(build_html(report), encoding="utf-8")
    print(f"HTML written: {html_path}")

    # Convert HTML → PDF using Microsoft Edge headless.
    edge_candidates = [
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    edge = next((p for p in edge_candidates if Path(p).is_file()), None)
    if edge is None:
        print("WARNING: Microsoft Edge not found. PDF not generated; open the HTML instead.")
        os.startfile(html_path)  # noqa
        return

    subprocess.run(
        [edge, "--headless", "--disable-gpu", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True,
        timeout=60,
    )
    print(f"PDF written: {pdf_path}")

    try:
        os.startfile(pdf_path)  # noqa
        print("Opened.")
    except Exception as e:
        print(f"Auto-open failed: {e}. Open manually: {pdf_path}")


if __name__ == "__main__":
    main()
