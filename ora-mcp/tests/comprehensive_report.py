"""Comprehensive 100-test smoke of the ORA! MCP server.

Covers every kind of question a user (or an LLM acting on their behalf) could
ask — party positions across all 21 manifesto topics, leader-personal views
for both Boldrin and Forchielli, empirical data lookups across quality tiers,
inter-party comparisons against each of the 8 indexed parties, all 5
resources, and a final battery of edge cases / parameter checks.

Outputs:
    comprehensive_test_report.html  (intermediate)
    comprehensive_test_report.pdf   (final, auto-opens)

Run:
    python tests/comprehensive_report.py
"""

from __future__ import annotations

import asyncio
import datetime
import html
import os
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable


# ----------------------------------------------------------------------------
# Bootstrap
# ----------------------------------------------------------------------------

def _load_env(path: Path = Path(".env")) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


_load_env()


# ----------------------------------------------------------------------------
# Test infrastructure
# ----------------------------------------------------------------------------

VERDICT_GREEN = "green"
VERDICT_YELLOW = "yellow"
VERDICT_RED = "red"


@dataclass
class TestResult:
    section: str
    name: str
    expectation: str
    verdict: str               # green / yellow / red
    summary: str               # 1-3 sentence verdict text (HTML allowed)
    payload_html: str          # rendered buckets / content
    runtime_ms: int = 0
    error: str | None = None


@dataclass
class Section:
    code: str
    title: str
    intro: str
    tests: list[TestResult] = field(default_factory=list)


def _short(text: str, n: int = 200) -> str:
    text = " ".join((text or "").split())
    return text[:n] + ("…" if len(text) > n else "")


def _esc(x: Any) -> str:
    return html.escape(str(x))


def _render_chunks(label: str, chunks: list[dict], max_show: int = 3) -> str:
    if not chunks:
        return (
            f'<div class="bucket empty"><strong>{_esc(label)}</strong> '
            f'<span class="count">— vuoto</span></div>'
        )
    items = []
    for c in chunks[:max_show]:
        src = c.get("source_doc") or c.get("extras", {}).get("source_doc") or "?"
        tier = c.get("tier") or "?"
        attr = c.get("attribution") or "?"
        score = c.get("_rerank_score", "?")
        text = _short(c.get("text", ""))
        items.append(
            f'<li><div class="meta"><span class="src">{_esc(src)}</span>'
            f' <span class="tag">tier={_esc(tier)}</span>'
            f' <span class="tag">attr={_esc(attr)}</span>'
            f' <span class="tag">score={_esc(score)}</span></div>'
            f'<div class="text">{_esc(text)}</div></li>'
        )
    extra = f' <span class="count">(+{len(chunks)-max_show} altri)</span>' if len(chunks) > max_show else ""
    return (
        f'<div class="bucket"><strong>{_esc(label)}</strong>'
        f' <span class="count">— {len(chunks)} chunks{extra}</span>'
        f'<ol>{"".join(items)}</ol></div>'
    )


def _render_find_position(result: dict, include_comparison: bool, include_leaders: bool) -> str:
    parts = [_render_chunks("official_party", result.get("official_party", []))]
    if include_leaders:
        leaders = result.get("leader_views", {})
        parts.append(_render_chunks("leader_views › boldrin", leaders.get("boldrin", [])))
        parts.append(_render_chunks("leader_views › forchielli", leaders.get("forchielli", [])))
    parts.append(_render_chunks("supporting_data", result.get("supporting_data", [])))
    if include_comparison:
        parts.append(_render_chunks("comparison", result.get("comparison", [])))
    return "".join(parts)


# ----------------------------------------------------------------------------
# Verdict helpers
# ----------------------------------------------------------------------------

def _verdict_party_question(result: dict) -> tuple[str, str]:
    op = result.get("official_party", [])
    if not op:
        return (
            VERDICT_RED,
            "❌ <strong>Bucket `official_party` vuoto.</strong> "
            "L'LLM non avrebbe la posizione ufficiale e dovrebbe inferire — "
            "violazione della gerarchia di fiducia."
        )
    top_score = op[0].get("_rerank_score", 0)
    n_data = len(result.get("supporting_data", []))
    leaders = result.get("leader_views", {})
    n_lead = len(leaders.get("boldrin", [])) + len(leaders.get("forchielli", []))
    if top_score < 0.55:
        return (
            VERDICT_YELLOW,
            f"⚠️ Trovati {len(op)} chunks ufficiali ma il rerank score top è "
            f"basso ({top_score}). La rilevanza è marginale — la qualità "
            f"della risposta LLM potrebbe degradare. "
            f"({n_lead} chunks leader, {n_data} dati a supporto.)"
        )
    return (
        VERDICT_GREEN,
        f"✅ {len(op)} chunks ufficiali, top score {top_score}. "
        f"{n_lead} chunks da leader + {n_data} dati a supporto. "
        f"L'LLM ha tutto per comporre una risposta strutturata e citata."
    )


def _verdict_leader_question(result: dict, leader: str) -> tuple[str, str]:
    leaders = result.get("leader_views", {})
    chunks = leaders.get(leader, [])
    if not chunks:
        return (
            VERDICT_RED,
            f"❌ Nessun chunk per {leader} su questo tema. "
            "L'LLM non potrebbe rispondere alla domanda specifica sul leader."
        )
    top_score = chunks[0].get("_rerank_score", 0)
    if top_score < 0.45:
        return (
            VERDICT_YELLOW,
            f"⚠️ {len(chunks)} chunks ma score top basso ({top_score}). "
            f"Possibile gap nel corpus su questo specifico angolo."
        )
    return (
        VERDICT_GREEN,
        f"✅ {len(chunks)} chunks per {leader}, top score {top_score}. "
        "Sufficiente per una risposta personale-leader ben citata."
    )


def _verdict_data_lookup(chunks: list[dict], metric: str) -> tuple[str, str]:
    if not chunks:
        return (
            VERDICT_RED,
            f"❌ Nessuna stat-card per '{_esc(metric)}'. "
            "Per questa metrica l'LLM non avrebbe numeri da citare."
        )
    quality_tiers = []
    for c in chunks:
        qt = (c.get("extras") or {}).get("quality_tier")
        if qt:
            quality_tiers.append(qt)
    top_qt = quality_tiers[0] if quality_tiers else "?"
    if top_qt == "D1":
        return (
            VERDICT_GREEN,
            f"✅ {len(chunks)} stat-cards. Top = D1 (ISTAT/Banca d'Italia, max qualità)."
        )
    if top_qt == "D2":
        return (
            VERDICT_GREEN,
            f"✅ {len(chunks)} stat-cards. Top = D2 (Eurostat/OECD, ottima qualità)."
        )
    if top_qt == "D3":
        return (
            VERDICT_YELLOW,
            f"⚠️ {len(chunks)} stat-cards, ma top = D3 (istituzionale). "
            "Accettabile ma non l'ideale per claim quantitativi pesanti."
        )
    return (
        VERDICT_YELLOW,
        f"⚠️ {len(chunks)} stat-cards trovate ma il quality_tier è "
        f"sconosciuto/inatteso (top={_esc(top_qt)})."
    )


def _verdict_comparison_question(result: dict, expected_party: str) -> tuple[str, str]:
    comparison = result.get("comparison", [])
    if not comparison:
        return (
            VERDICT_RED,
            f"❌ Bucket `comparison` vuoto. Il filtro multi-party non ha trovato chunks "
            f"per {expected_party}."
        )
    # Check that the expected party appears in attribution of top chunks
    attributions = [c.get("attribution", "") for c in comparison]
    expected_lower = expected_party.lower()
    matches = sum(1 for a in attributions if a == expected_lower)
    op = result.get("official_party", [])
    if matches == 0:
        # Comparison populated but with wrong parties (unlikely but possible)
        return (
            VERDICT_YELLOW,
            f"⚠️ Bucket comparison ha {len(comparison)} chunks ma nessuno con "
            f"attribution='{expected_lower}' (top attribution: {_esc(attributions[0])}). "
            "L'LLM potrebbe confondere i partiti."
        )
    if not op:
        return (
            VERDICT_YELLOW,
            f"⚠️ Comparison OK ({matches}/{len(comparison)} chunks da {expected_party}), "
            "ma `official_party` è vuoto — manca il lato ORA del confronto."
        )
    return (
        VERDICT_GREEN,
        f"✅ Confronto bilanciato: {len(op)} chunks ORA + "
        f"{matches}/{len(comparison)} chunks da {expected_party}."
    )


def _verdict_resource(content: str, expected_min_size: int = 500) -> tuple[str, str]:
    if not content:
        return VERDICT_RED, "❌ Risorsa vuota."
    if len(content) < expected_min_size:
        return (
            VERDICT_YELLOW,
            f"⚠️ Risorsa molto corta ({len(content)} caratteri). "
            "Potrebbe mancare del contenuto."
        )
    return (
        VERDICT_GREEN,
        f"✅ {len(content):,} caratteri di contenuto. "
        f"Anteprima del primo paragrafo riportata sotto."
    )


# ----------------------------------------------------------------------------
# Test definitions
# ----------------------------------------------------------------------------

# Section A — Posizioni ufficiali del partito su temi del manifesto
SECTION_A: list[tuple[str, str]] = [
    ("ORA tassazione fiscalità riforma IRPEF", "Tesi 19 — Tassazione e fiscalità"),
    ("ORA pensioni sostenibilità riforma", "Tesi 14 / Fondamento 8 — Pensioni"),
    ("ORA immigrazione politiche flussi", "Tesi 10 — Immigrazione"),
    ("ORA università ricerca finanziamento", "Tesi 21 — Università e ricerca"),
    ("ORA innovazione crescita tecnologica", "Tesi 12 — Innovazione e crescita"),
    ("ORA diritti civili matrimonio egualitario", "Tesi 05 — Diritti civili"),
    ("ORA giustizia riforma processo", "Tesi 08 — Giustizia"),
    ("ORA difesa spesa militare NATO", "Tesi 04 — Difesa"),
    ("ORA energia ambiente transizione", "Tesi 06 — Energia, ambiente, sostenibilità"),
    ("ORA salute sanità servizio nazionale", "Tesi 16 — Salute e servizi sanitari"),
    ("ORA lavoro politiche occupazione", "Tesi 14 — Lavoro e politiche sociali"),
    ("ORA infrastrutture trasporti mobilità", "Tesi 11 — Infrastrutture e trasporti"),
    ("ORA sviluppo economico politica industriale", "Tesi 18 — Sviluppo economico"),
    ("ORA esteri relazioni internazionali Ucraina", "Tesi 07 — Esteri"),
    ("ORA Unione Europea integrazione", "Tesi 20 — Unione Europea"),
    ("ORA governance riforme istituzionali elettorali", "Tesi 09 — Governance"),
    ("ORA istruzione scuola dispersione", "Tesi 13 — Istruzione"),
    ("ORA pari opportunità inclusione donne", "Tesi 15 — Pari opportunità"),
    ("ORA cultura sport turismo", "Tesi 03 — Cultura, sport, turismo"),
    ("ORA comuni regioni autonomia territoriale", "Tesi 02 — Comuni, province, regioni"),
    ("ORA agricoltura politiche agricole", "Drill-down — Agricoltura"),
    ("ORA spesa pubblica deficit", "Tesi 17 — Spesa pubblica"),
    ("ORA burocrazia digitalizzazione PA", "Drill-down — Burocrazia"),
    ("ORA demografia natalità famiglie", "Drill-down — Demografia"),
    ("ORA identità del partito posizionamento centro", "Identity card — chi è ORA"),
]

# Section B — Domande tipiche utente (formulazioni varie)
SECTION_B: list[tuple[str, str]] = [
    ("Cosa pensa ORA della riforma fiscale", "Formulazione domanda diretta"),
    ("Quali sono le proposte di ORA sulle pensioni", "Formulazione 'quali sono'"),
    ("Posizione di ORA sull'immigrazione", "Formulazione nominale"),
    ("Cosa farebbe ORA al governo", "Formulazione condizionale/proiettiva"),
    ("Programma di ORA in sintesi", "Domanda di overview"),
    ("Valori fondanti di ORA", "Domanda valoriale"),
    ("Slogan di ORA il coraggio dell'ovvio", "Test su slogan/identità"),
    ("ORA è di destra o di sinistra", "Test posizionamento"),
    ("Differenza tra ORA e altri partiti centristi", "Test confronto generico"),
    ("Posizione di ORA sul governo Meloni", "Topic attuale"),
    ("ORA pensa che l'Italia debba uscire dall'euro", "Topic eurozone"),
    ("Posizione di ORA sulla NATO", "Topic geopolitico"),
    ("ORA aborto IVG legge 194", "Topic sensibile valoriale"),
    ("ORA reddito di cittadinanza", "Policy specifica"),
    ("ORA salario minimo", "Policy specifica"),
    ("ORA flat tax aliquota unica", "Policy specifica fiscale"),
    ("ORA cannabis legalizzazione", "Policy sensibile"),
    ("ORA eutanasia fine vita biotestamento", "Policy sensibile"),
    ("ORA giovani Italia emigrazione", "Topic generazionale"),
    ("ORA quota 100 quota 41 pensioni anticipate", "Policy concreta pensioni"),
]

# Section C — Boldrin personal views
SECTION_C: list[tuple[str, str]] = [
    ("Cosa pensa Boldrin del sistema pensionistico", "Pensioni"),
    ("Posizione di Boldrin sull'immigrazione", "Immigrazione"),
    ("Boldrin università ecosistema startup", "Università/innovazione"),
    ("Boldrin riforma fiscale proposta", "Fiscalità"),
    ("Boldrin Europa euro moneta unica", "Europa"),
    ("Boldrin produttività Italia declino", "Macroeconomia"),
    ("Boldrin spesa pubblica welfare clientelare", "Welfare/spesa"),
    ("Boldrin democrazia rappresentanza istituzioni", "Istituzioni"),
    ("Boldrin liberalismo destra centro", "Posizionamento"),
    ("Boldrin biografia carriera economista", "Bio"),
]

# Section D — Forchielli personal views
SECTION_D: list[tuple[str, str]] = [
    ("Forchielli politica industriale", "Industria"),
    ("Forchielli Cina relazioni economiche commercio", "Cina"),
    ("Forchielli pensione 70 anni proposta", "Pensioni (proposta tipica)"),
    ("Forchielli sanità finanziamento ticket", "Sanità"),
    ("Forchielli Europa investimenti", "Europa"),
    ("Forchielli sicurezza immigrazione ordine pubblico", "Immigrazione"),
    ("Forchielli ricerca università finanziamento", "Università"),
    ("Forchielli capitalismo imprese famiglie italiane", "Capitalismo"),
    ("Forchielli Sud Italia sviluppo Mezzogiorno", "Sud Italia"),
    ("Forchielli internazionalizzazione PMI", "PMI/export"),
]

# Section E — Data lookups
SECTION_E: list[tuple[str, str, str]] = [
    ("tasso disoccupazione giovanile Italia", None, "Disoccupazione giovani"),
    ("spesa pensionistica percentuale PIL", None, "Spesa pensioni"),
    ("PIL crescita Italia annuale", "2023", "PIL crescita"),
    ("debito pubblico Maastricht Italia", "2024", "Debito pubblico"),
    ("investimenti R&S percentuale PIL", None, "R&S su PIL"),
    ("popolazione immigrata Italia stock", None, "Stock immigrati"),
    ("tasso natalità denatalità", None, "Natalità"),
    ("abbandono scolastico precoce", None, "Dispersione scolastica"),
    ("produttività lavoro Italia stagnazione", None, "Produttività"),
    ("cuneo fiscale lavoro dipendente", None, "Cuneo fiscale"),
    ("donne in parlamento rappresentanza", None, "Donne in politica"),
    ("spesa sanitaria pubblica percentuale PIL", None, "Spesa sanità"),
    ("energia rinnovabile mix elettrico Italia", None, "Energia rinnovabile"),
    ("investimenti infrastrutture trasporto", None, "Infrastrutture"),
    ("occupazione stranieri vs italiani", None, "Lavoro stranieri"),
]

# Section F — Comparison queries
SECTION_F: list[tuple[str, str, str]] = [
    ("ORA vs PD politiche sociali welfare", "pd", "vs PD"),
    ("ORA vs FdI immigrazione sicurezza", "fdi", "vs FdI"),
    ("ORA vs Lega autonomia regionale", "lega", "vs Lega"),
    ("ORA vs Azione politica industriale", "azione", "vs Azione"),
    ("ORA vs Italia Viva riforme istituzionali", "iv", "vs IV"),
    ("ORA vs M5S reddito di cittadinanza", "m5s", "vs M5S"),
    ("ORA vs Forza Italia fiscalità impresa", "fi", "vs FI"),
    ("ORA vs AVS diritti civili LGBT", "avs", "vs AVS"),
    ("ORA partiti centristi alleanze", None, "Comparison generico"),
    ("Posizionamento di ORA tra i partiti italiani", None, "Comparison broad"),
]

# Section G — Resources
SECTION_G: list[tuple[str, str, str]] = [
    ("about.md", "ora://about", "Carta d'identità + gerarchia di fiducia"),
    ("manifesto_full.md", "ora://manifesto", "Manifesto completo (21 tesi)"),
    ("statuto.md", "ora://statuto", "Statuto del partito"),
    ("fondamenti.md", "ora://fondamenti", "15 Fondamenti programmatici"),
    ("codice-etico.md", "ora://codice-etico", "Codice etico"),
]

# Section H — Edge cases, out-of-scope, parameter tests
SECTION_H: list[tuple[str, dict, str, str]] = [
    # Out-of-scope (absent topics) — verifichiamo che il sistema non inventi
    ("posizione di ORA sulla colonizzazione di Marte", {}, "absent_topic",
     "Topic non presente nel corpus — testiamo che il sistema non inventi"),
    ("ORA criptovalute blockchain bitcoin", {}, "rare_topic",
     "Topic raro / forse assente"),
    ("ORA antisemitismo Israele Palestina Gaza", {}, "sensitive_geopolitical",
     "Topic geopolitico sensibile"),
    # Personal/private — verifichiamo che query private non scrapino contenuto policy
    ("Boldrin moglie figli vita privata famiglia", {}, "leader_private",
     "Vita privata leader — atteso: poco/niente, NON chunks di politica"),
    ("Forchielli passioni hobby tempo libero", {}, "leader_private",
     "Hobby leader — atteso: poco/niente, NON chunks di politica"),
    ("Boldrin religione fede cattolica preghiera", {}, "leader_private",
     "Convinzioni religiose personali — sensibile"),
    # Off-policy noise — verifichiamo che il bucket party sia vuoto o irrilevante
    ("ORA opinione sulla Juventus calcio serie A", {}, "off_policy",
     "Topic completamente off-policy"),
    ("ORA posizione su Vladimir Putin direttamente", {}, "geopolitical_namedrop",
     "Name-drop geopolitico specifico — verifica gestione"),
    # Parametri
    ("ORA tassazione fiscalità", {"include_leaders": False}, "param_no_leaders",
     "Parametro include_leaders=False — verifica che leader_views sia assente"),
    ("ORA pensioni", {"top_k_per_bucket": 1}, "param_top_k_1",
     "Parametro top_k_per_bucket=1 — verifica che ogni bucket abbia al massimo 1 chunk"),
]


# ----------------------------------------------------------------------------
# Runners
# ----------------------------------------------------------------------------

def _time(fn: Callable[[], Any]) -> tuple[Any, int]:
    t0 = time.monotonic()
    out = fn()
    return out, int((time.monotonic() - t0) * 1000)


def run_section_party(section: Section, items: list[tuple[str, str]]) -> None:
    from ora_mcp.retrieval import find_position
    for topic, expect in items:
        try:
            result, ms = _time(lambda: asyncio.run(find_position(topic, top_k_per_bucket=5)))
            verdict, summary = _verdict_party_question(result)
            payload = _render_find_position(result, include_comparison=False, include_leaders=True)
            section.tests.append(TestResult(section.code, topic, expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, topic, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {topic[:60]}")


def run_section_leader(section: Section, items: list[tuple[str, str]], leader: str) -> None:
    from ora_mcp.retrieval import find_position
    for topic, expect in items:
        try:
            result, ms = _time(lambda: asyncio.run(find_position(topic, top_k_per_bucket=5)))
            verdict, summary = _verdict_leader_question(result, leader)
            payload = _render_find_position(result, include_comparison=False, include_leaders=True)
            section.tests.append(TestResult(section.code, topic, expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, topic, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {topic[:60]}")


def run_section_data(section: Section, items: list[tuple[str, str | None, str]]) -> None:
    from ora_mcp.retrieval import data_lookup
    for metric, period, expect in items:
        try:
            chunks, ms = _time(lambda: data_lookup(metric, period=period))
            verdict, summary = _verdict_data_lookup(chunks, metric)
            payload = _render_chunks("data_lookup results", chunks, max_show=3)
            label = f"{metric}" + (f"  (period={period})" if period else "")
            section.tests.append(TestResult(section.code, label, expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, metric, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {metric[:60]}")


def run_section_comparison(section: Section, items: list[tuple[str, str | None, str]]) -> None:
    from ora_mcp.retrieval import find_position
    for topic, expected_party, expect in items:
        try:
            result, ms = _time(lambda: asyncio.run(find_position(topic, top_k_per_bucket=5, include_comparison=True)))
            if expected_party:
                verdict, summary = _verdict_comparison_question(result, expected_party)
            else:
                # broad comparison — just check non-empty
                cmp_chunks = result.get("comparison", [])
                if cmp_chunks:
                    verdict, summary = VERDICT_GREEN, f"✅ {len(cmp_chunks)} chunks comparison (broad)."
                else:
                    verdict, summary = VERDICT_YELLOW, "⚠️ Bucket comparison vuoto per query broad."
            payload = _render_find_position(result, include_comparison=True, include_leaders=True)
            section.tests.append(TestResult(section.code, topic, expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, topic, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {topic[:60]}")


def run_section_resources(section: Section, items: list[tuple[str, str, str]]) -> None:
    res_dir = Path(__file__).resolve().parent.parent / "ora_mcp" / "resources"
    for filename, uri, expect in items:
        t0 = time.monotonic()
        try:
            content = (res_dir / filename).read_text(encoding="utf-8")
            ms = int((time.monotonic() - t0) * 1000)
            verdict, summary = _verdict_resource(content)
            preview = _short(content, 350)
            payload = (
                f'<div class="bucket"><strong>URI:</strong> <code>{_esc(uri)}</code> '
                f'<span class="count">— {len(content):,} caratteri</span>'
                f'<div class="text">{_esc(preview)}</div></div>'
            )
            section.tests.append(TestResult(section.code, uri, expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, uri, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {uri}")


def run_section_edge(section: Section,
                     items: list[tuple[str, dict, str, str]]) -> None:
    from ora_mcp.retrieval import find_position
    for topic, kwargs, code, expect in items:
        try:
            kwargs_to_use = dict(kwargs)
            result, ms = _time(lambda: asyncio.run(find_position(topic, top_k_per_bucket=kwargs_to_use.pop("top_k_per_bucket", 5),
                                                     include_comparison=kwargs_to_use.pop("include_comparison", False),
                                                     include_leaders=kwargs_to_use.pop("include_leaders", True),
                                                     **kwargs_to_use)))
            # Verdict per edge code
            op = result.get("official_party", [])
            leaders = result.get("leader_views", {})
            if code == "absent_topic":
                if not op:
                    verdict, summary = VERDICT_GREEN, "✅ Bucket vuoto come atteso — il sistema non inventa una posizione su un topic assente."
                else:
                    top_score = op[0].get("_rerank_score", 0)
                    if top_score < 0.3:
                        verdict, summary = VERDICT_GREEN, f"✅ {len(op)} chunks ma score top molto basso ({top_score}) — l'LLM dovrebbe percepire la scarsa rilevanza."
                    else:
                        verdict, summary = VERDICT_YELLOW, f"⚠️ {len(op)} chunks con score top {top_score} su topic dichiaratamente assente — verificare manualmente."
            elif code == "rare_topic":
                if not op:
                    verdict, summary = VERDICT_GREEN, "✅ Topic raro non presente: bucket vuoto, comportamento corretto."
                else:
                    verdict, summary = VERDICT_YELLOW, f"⚠️ {len(op)} chunks trovati per topic atteso come raro — controllare se davvero rilevanti."
            elif code == "sensitive_geopolitical":
                # Just report what's there
                verdict = VERDICT_GREEN if op else VERDICT_YELLOW
                summary = f"ℹ️ {len(op)} chunks ufficiali su topic sensibile. Verificare manualmente che il contenuto sia bilanciato e non polarizzante."
            elif code == "leader_private":
                # Privacy test: official_party should be empty/very low (policy
                # chunks shouldn't surface for private queries). Leader buckets
                # may contain biographical chunks — OK if relevant.
                top_op_score = op[0].get("_rerank_score", 0) if op else 0
                bucket_chunks = leaders.get("boldrin", []) + leaders.get("forchielli", [])
                top_leader = bucket_chunks[0].get("_rerank_score", 0) if bucket_chunks else 0
                if top_op_score >= 0.5:
                    verdict, summary = VERDICT_YELLOW, f"⚠️ official_party ha {len(op)} chunks con top score {top_op_score} su query privata — rischio che policy emerga dove non dovrebbe."
                elif top_leader >= 0.6:
                    verdict, summary = VERDICT_YELLOW, f"⚠️ Top leader score {top_leader} — chunks biografici molto rilevanti recuperati. Da verificare manualmente che non siano contenuti sensibili."
                else:
                    verdict, summary = VERDICT_GREEN, f"✅ Privacy OK. official_party top {top_op_score}, leader top {top_leader} — il sistema non confonde query private con policy."
            elif code == "off_policy":
                if not op or op[0].get("_rerank_score", 0) < 0.4:
                    verdict, summary = VERDICT_GREEN, "✅ Bucket party vuoto o con score molto basso — il sistema riconosce off-policy."
                else:
                    verdict, summary = VERDICT_YELLOW, f"⚠️ {len(op)} chunks party recuperati su query off-policy (top {op[0].get('_rerank_score')}). Da verificare."
            elif code == "geopolitical_namedrop":
                # Putin name-drop — corpus could have some relevant content (esteri/Ucraina tesi)
                verdict = VERDICT_GREEN if op else VERDICT_YELLOW
                summary = f"ℹ️ {len(op)} chunks party + leader views su name-drop geopolitico. Verificare manualmente che il contenuto sia coerente con la posizione ufficiale ORA su Ucraina/Russia."
            elif code == "param_no_leaders":
                if "leader_views" in result:
                    verdict, summary = VERDICT_RED, "❌ `leader_views` presente nonostante include_leaders=False."
                else:
                    verdict, summary = VERDICT_GREEN, "✅ `leader_views` correttamente assente."
            elif code == "param_top_k_1":
                sizes = {
                    "official_party": len(op),
                    "boldrin": len(leaders.get("boldrin", [])),
                    "forchielli": len(leaders.get("forchielli", [])),
                    "supporting_data": len(result.get("supporting_data", [])),
                }
                if all(n <= 1 for n in sizes.values()):
                    verdict, summary = VERDICT_GREEN, f"✅ top_k_per_bucket=1 rispettato: {sizes}"
                else:
                    verdict, summary = VERDICT_RED, f"❌ top_k_per_bucket=1 violato: {sizes}"
            else:
                verdict, summary = VERDICT_YELLOW, f"ℹ️ Edge case '{code}' — review manuale."
            payload = _render_find_position(result,
                                            include_comparison=False,
                                            include_leaders=kwargs.get("include_leaders", True))
            section.tests.append(TestResult(section.code, f"{topic} [{code}]", expect, verdict, summary, payload, ms))
        except Exception as e:
            section.tests.append(TestResult(section.code, topic, expect, VERDICT_RED,
                                            f"❌ Eccezione: {type(e).__name__}: {e}", "", 0, str(e)))
        print(f"  [{section.code}] {topic[:60]}")


# ----------------------------------------------------------------------------
# HTML rendering
# ----------------------------------------------------------------------------

def render_executive_summary(sections: list[Section]) -> str:
    total = sum(len(s.tests) for s in sections)
    green = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_GREEN)
    yellow = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_YELLOW)
    red = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_RED)
    pct = lambda n: f"{(n/total*100 if total else 0):.0f}%"

    section_rows = ""
    for s in sections:
        sg = sum(1 for t in s.tests if t.verdict == VERDICT_GREEN)
        sy = sum(1 for t in s.tests if t.verdict == VERDICT_YELLOW)
        sr = sum(1 for t in s.tests if t.verdict == VERDICT_RED)
        st = len(s.tests)
        section_rows += (
            f'<tr><td><strong>{_esc(s.code)}</strong> {_esc(s.title)}</td>'
            f'<td class="num">{st}</td>'
            f'<td class="num g">{sg}</td>'
            f'<td class="num y">{sy}</td>'
            f'<td class="num r">{sr}</td></tr>'
        )

    red_list = []
    for s in sections:
        for t in s.tests:
            if t.verdict == VERDICT_RED:
                red_list.append(f'<li><strong>[{_esc(s.code)}]</strong> {_esc(t.name)}: {t.summary}</li>')
    yellow_list = []
    for s in sections:
        for t in s.tests:
            if t.verdict == VERDICT_YELLOW:
                yellow_list.append(f'<li><strong>[{_esc(s.code)}]</strong> {_esc(t.name)}: {t.summary}</li>')

    if red == 0 and yellow == 0:
        overall = '<div class="overall-banner banner-green">✅ Sistema pronto per la demo. Nessun problema rilevato.</div>'
    elif red == 0:
        overall = f'<div class="overall-banner banner-yellow">⚠️ Sistema funzionante con {yellow} avvertimenti (rilevanza marginale su alcuni temi). Demo possibile ma da rivedere prima di un uso intensivo.</div>'
    else:
        overall = f'<div class="overall-banner banner-red">❌ {red} test falliti criticamente. Da risolvere prima della demo.</div>'

    return f"""
<section class="exec-summary">
  <h2>Riepilogo esecutivo</h2>
  {overall}
  <div class="kpis">
    <div class="kpi"><div class="kpi-num">{total}</div><div class="kpi-lbl">test totali</div></div>
    <div class="kpi g"><div class="kpi-num">{green}</div><div class="kpi-lbl">passati ({pct(green)})</div></div>
    <div class="kpi y"><div class="kpi-num">{yellow}</div><div class="kpi-lbl">avvertimenti ({pct(yellow)})</div></div>
    <div class="kpi r"><div class="kpi-num">{red}</div><div class="kpi-lbl">falliti ({pct(red)})</div></div>
  </div>
  <table class="section-tbl">
    <thead><tr><th>Sezione</th><th>Test</th><th>✅</th><th>⚠️</th><th>❌</th></tr></thead>
    <tbody>{section_rows}</tbody>
  </table>
  {"<h3>❌ Falliti critici</h3><ul>" + "".join(red_list) + "</ul>" if red_list else ""}
  {"<h3>⚠️ Avvertimenti da rivedere</h3><ul>" + "".join(yellow_list[:20]) + "</ul>" if yellow_list else ""}
  {f'<p class="more-warn">…e altri {len(yellow_list)-20} avvertimenti più sotto.</p>' if len(yellow_list) > 20 else ""}
</section>
"""


def render_section(section: Section) -> str:
    rows = []
    for t in section.tests:
        rows.append(
            f'<div class="test-card test-{t.verdict}">'
            f'<div class="test-head">'
            f'<span class="status-dot status-{t.verdict}"></span>'
            f'<strong>{_esc(t.name)}</strong>'
            f'<span class="exp">— {_esc(t.expectation)}</span>'
            f'<span class="rt">{t.runtime_ms} ms</span>'
            f'</div>'
            f'<div class="verdict">{t.summary}</div>'
            f'<details class="payload"><summary>buckets / contenuto</summary>{t.payload_html}</details>'
            f'</div>'
        )
    return f"""
<section class="section section-{section.code}">
  <h2>{_esc(section.code)} — {_esc(section.title)}</h2>
  <p class="section-intro">{_esc(section.intro)}</p>
  {"".join(rows)}
</section>
"""


def build_html(sections: list[Section]) -> str:
    now = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
    body = render_executive_summary(sections) + "\n".join(render_section(s) for s in sections)
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<title>ORA! MCP — Test esaustivo</title>
<style>
  @page {{ size: A4; margin: 1.4cm 1.2cm; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
          color: #1a1a1a; line-height: 1.4; font-size: 9.5pt; }}
  h1 {{ font-size: 16pt; margin: 0 0 0.2em; }}
  h2 {{ font-size: 12pt; margin-top: 1.4em; border-bottom: 1px solid #ccc;
        padding-bottom: 3px; }}
  h3 {{ font-size: 10.5pt; margin-top: 0.9em; }}
  .lead {{ color: #555; font-size: 9pt; margin-bottom: 0.5em; }}
  .section-intro {{ color: #555; font-size: 9pt; margin-bottom: 0.6em; }}

  /* Executive summary */
  .exec-summary {{ background: #f8f8fb; padding: 0.8em 1em; border-radius: 6px;
                   margin-bottom: 1em; }}
  .overall-banner {{ padding: 0.6em 0.8em; border-radius: 4px; margin: 0.6em 0;
                     font-size: 10pt; font-weight: 600; }}
  .banner-green {{ background: #e6f7e9; border-left: 4px solid #2a8f3a; }}
  .banner-yellow {{ background: #fdf6e3; border-left: 4px solid #c8a019; }}
  .banner-red {{ background: #fbeaea; border-left: 4px solid #b53030; }}
  .kpis {{ display: flex; gap: 0.6em; margin: 0.8em 0; }}
  .kpi {{ flex: 1; background: #fff; padding: 0.5em 0.7em; border-radius: 4px;
          border: 1px solid #e0e0e0; text-align: center; }}
  .kpi.g {{ border-color: #2a8f3a; }}
  .kpi.y {{ border-color: #c8a019; }}
  .kpi.r {{ border-color: #b53030; }}
  .kpi-num {{ font-size: 16pt; font-weight: 700; }}
  .kpi.g .kpi-num {{ color: #2a8f3a; }}
  .kpi.y .kpi-num {{ color: #c8a019; }}
  .kpi.r .kpi-num {{ color: #b53030; }}
  .kpi-lbl {{ font-size: 8.5pt; color: #555; }}
  .section-tbl {{ width: 100%; border-collapse: collapse; font-size: 9pt;
                  margin: 0.6em 0; }}
  .section-tbl th, .section-tbl td {{ padding: 0.3em 0.5em; border-bottom: 1px solid #eee;
                                       text-align: left; }}
  .section-tbl .num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .section-tbl .g {{ color: #2a8f3a; font-weight: 600; }}
  .section-tbl .y {{ color: #c8a019; font-weight: 600; }}
  .section-tbl .r {{ color: #b53030; font-weight: 600; }}

  /* Test cards */
  .test-card {{ background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
                padding: 0.5em 0.7em; margin: 0.4em 0; }}
  .test-green {{ border-left: 3px solid #2a8f3a; }}
  .test-yellow {{ border-left: 3px solid #c8a019; }}
  .test-red {{ border-left: 3px solid #b53030; }}
  .test-head {{ font-size: 9.5pt; display: flex; align-items: center;
                gap: 0.4em; flex-wrap: wrap; }}
  .status-dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}
  .status-green {{ background: #2a8f3a; }}
  .status-yellow {{ background: #c8a019; }}
  .status-red {{ background: #b53030; }}
  .exp {{ color: #777; font-size: 8.5pt; }}
  .rt {{ margin-left: auto; color: #888; font-size: 8pt;
         font-family: Consolas, monospace; }}
  .verdict {{ font-size: 9pt; margin-top: 0.3em; color: #333; }}
  details.payload {{ margin-top: 0.4em; font-size: 8.5pt; }}
  details.payload > summary {{ cursor: pointer; color: #555; font-size: 8.5pt; }}

  /* Buckets */
  .bucket {{ margin: 0.3em 0; padding: 0.2em 0; }}
  .bucket.empty {{ color: #b53030; }}
  .bucket .count {{ color: #888; font-weight: 400; }}
  .bucket ol {{ margin: 0.2em 0 0.2em 1.2em; padding: 0; }}
  .bucket li {{ margin: 0.2em 0; }}
  .meta {{ font-size: 7.5pt; color: #555; margin-bottom: 1px; }}
  .src {{ font-family: Consolas, monospace; color: #224; }}
  .tag {{ display: inline-block; background: #eef; color: #224; padding: 0 4px;
          border-radius: 3px; font-family: Consolas, monospace; font-size: 7.5pt;
          margin-right: 2px; }}
  .text {{ font-size: 8.5pt; padding: 2px 5px; background: #fafafa;
           border-left: 2px solid #ccc; margin: 1px 0; }}
  code {{ background: #eee; padding: 0 4px; border-radius: 2px; font-size: 8.5pt;
          font-family: Consolas, monospace; }}
  footer {{ margin-top: 1.5em; padding-top: 0.5em; border-top: 1px solid #ddd;
            font-size: 8pt; color: #888; }}
  .more-warn {{ font-style: italic; color: #888; }}
</style></head><body>
<h1>ORA! MCP — Test esaustivo</h1>
<p class="lead">100 test attraverso ogni funzionalità del server. Generato il {now}.
Per ciascun test: domanda, attesa, verdetto colorato, e (opzionalmente espandibile)
il contenuto restituito dal MCP all'LLM.</p>
{body}
<footer>Indice Qdrant <code>ora_chunks</code> (3 665 chunks) · embed
<code>voyage-4-large</code> · rerank <code>rerank-2.5</code> · server
<code>ora-mcp v0.1.0</code>.</footer>
</body></html>
"""


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> None:
    sections = [
        Section("A", "Posizioni del partito su temi del manifesto (25)",
                "Una query per ciascuna tesi del manifesto + drill-down su temi trasversali."),
        Section("B", "Domande tipiche dell'utente (20)",
                "Formulazioni diverse — diretta, condizionale, sensibile, di confronto generico."),
        Section("C", "Viste personali di Boldrin (10)",
                "Query mirate ad estrarre la posizione personale del segretario."),
        Section("D", "Viste personali di Forchielli (10)",
                "Query mirate ad estrarre la posizione personale del presidente."),
        Section("E", "data_lookup — schede statistiche (15)",
                "Test del tool quantitativo. Verifica che le stat-cards top siano D1/D2."),
        Section("F", "Confronti con altri partiti (10)",
                "find_position(include_comparison=True). Verifica che il bucket comparison contenga il partito richiesto."),
        Section("G", "Resources MCP (5)",
                "Lettura dei 5 documenti canonici esposti come MCP resources."),
        Section("H", "Edge cases & parametri (5)",
                "Topic assenti, parametri non-default, validation della logica del tool."),
    ]

    print("Section A — party positions...")
    run_section_party(sections[0], SECTION_A)
    print("Section B — user-style questions...")
    run_section_party(sections[1], SECTION_B)
    print("Section C — Boldrin views...")
    run_section_leader(sections[2], SECTION_C, "boldrin")
    print("Section D — Forchielli views...")
    run_section_leader(sections[3], SECTION_D, "forchielli")
    print("Section E — data lookups...")
    run_section_data(sections[4], SECTION_E)
    print("Section F — comparisons...")
    run_section_comparison(sections[5], SECTION_F)
    print("Section G — resources...")
    run_section_resources(sections[6], SECTION_G)
    print("Section H — edge cases...")
    run_section_edge(sections[7], SECTION_H)

    html_path = Path("comprehensive_test_report.html").resolve()
    pdf_path = Path("comprehensive_test_report.pdf").resolve()
    html_path.write_text(build_html(sections), encoding="utf-8")
    print(f"\nHTML written: {html_path}")

    edge_paths = [
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    edge = next((p for p in edge_paths if Path(p).is_file()), None)
    if edge is None:
        print("WARNING: Edge not found, opening HTML.")
        os.startfile(html_path)  # noqa
        return

    subprocess.run(
        [edge, "--headless", "--disable-gpu", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, timeout=120,
    )
    print(f"PDF written: {pdf_path}")

    # Print headline counts to stdout for the operator
    total = sum(len(s.tests) for s in sections)
    g = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_GREEN)
    y = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_YELLOW)
    r = sum(1 for s in sections for t in s.tests if t.verdict == VERDICT_RED)
    print(f"\n=== RESULTS: {total} total | green {g} | yellow {y} | red {r} ===")

    try:
        os.startfile(pdf_path)  # noqa
        print("PDF opened.")
    except Exception as e:
        print(f"Auto-open failed: {e}")


if __name__ == "__main__":
    main()
