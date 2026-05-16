---
run_type: content-refresh
target: salute-servizi-sanitari/liste-attesa-bisogni-insoddisfatti-italia-2024.md
date: 2026-05-13
trigger: TO_VERIFY § salute-servizi-sanitari 🟡 action_moderate
---

# Content refresh — Liste d'attesa e bisogni insoddisfatti (salute-servizi-sanitari)

## Scope
Surgical fix di una singola card. Disambiguazione di due metriche miscelate senza etichetta + verifica fonte di un dato sospetto.

## Metriche disambiguate

| Indicatore | Fonte autoritativa | Italia 2023 | Etichettatura nella nuova card |
|---|---|---|---|
| Rinuncia a prestazioni sanitarie | **ISTAT-AVQ / Rapporto BES 2023 (aprile 2024)** | **7,6%** (~4,5 mln) | "ISTAT AVQ — rinuncia a prestazioni sanitarie" |
| Unmet medical needs (definizione classica) | **Eurostat EU-SILC `hlth_silc_08`** | **1,8%** | "EU-SILC hlth_silc_08, motivazioni TOOEFW" — quella citata da OECD Country Health Profile 2025 |
| Unmet medical needs (definizione 2021+) | **Eurostat EU-SILC `hlth_silc_08b`** | **3,7%** | "EU-SILC hlth_silc_08b, motivazioni TXP/TFAR/WLIST" — versione più estesa |

Aggiunto messaggio esplicito nel corpo card: i tre numeri (7,6% / 1,8% / 3,7%) **non si contraddicono** — misurano fenomeni progressivamente più stretti. Survey nazionale italiana (ampia) → survey UE armonizzata classica (stretta) → survey UE armonizzata revisionata (intermedia).

## Fonte del "2,7 milioni" — verifica e correzione

**Vecchia card:** attribuiva "2,7 milioni in lista d'attesa" a "Ministero della Salute (2024)".

**Verifica web (WebSearch):** il dato proviene dal **Rapporto BES ISTAT 2023 (aprile 2024)**, sezione su rinuncia alle cure. Il Country Health Profile 2025 lo cita esplicitamente come "ISTAT, 2024".

**Doppia correzione applicata:**
1. **Attribuzione corretta:** ISTAT-AVQ 2024 (non Ministero della Salute). Il Ministero compare solo nella sezione PNGLA come fonte normativa, non come fonte numerica.
2. **Framing corretto:** i 2,7 mln **non sono persone "attualmente in attesa di una prestazione"** — sono persone che hanno **rinunciato** a prestazioni sanitarie a causa di liste d'attesa nei 12 mesi precedenti (subset del 4,5% sul totale popolazione 18+). Lo specifica chiaramente la nuova card in due punti (Headline + Caveat).

Anche segnalato che il dato sottostante "totale rinuncia per qualsiasi causa" è 7,6% / **4,5 milioni** (non 4,5 milioni come "categoria parallela" — sono il totale di cui i 2,7 mln sono subset, con sovrapposizione parziale tra motivi liste d'attesa e motivi economici).

## Sources citate nella nuova card

1. ISTAT, Rapporto BES 2023 (aprile 2024), indagine "Aspetti della vita quotidiana" — fonte primaria 7,6% e 2,7 mln.
2. Eurostat EU-SILC `hlth_silc_08` — fonte primaria 1,8%, serie storica 2008-2025, confronto cross-country.
3. Eurostat EU-SILC `hlth_silc_08b` — fonte secondaria 3,7% e breakdown per fasce reddito.
4. OECD/European Observatory, State of Health in the EU — Italy Country Health Profile 2025 (dicembre 2025) — fonte per PNGLA, disparità socioeconomica 2,6× vs UE 1,6×, ostacoli pre-trattamento 60%, tempi chirurgici 74gg.
5. OECD Health at a Glance 2025 — tempi chirurgici elettivi.

## Raw persistiti

Nuovi file in `_raw/salute-servizi-sanitari/`:
- `EUROSTAT_hlth_silc_08/it_2023_all_reasons.json` (Italia 2023, tutte le motivazioni e fasce d'età/sesso/quintile)
- `EUROSTAT_hlth_silc_08/it_2008_2025_TOOEFW.json` (serie storica IT, motivazione TXP/TFAR/WLIST, 16+ T TOTAL)
- `EUROSTAT_hlth_silc_08/eu_peers_2023_TOOEFW.json` (cross-country 2023)
- `EUROSTAT_hlth_silc_08b/it_2023_all_breakdowns.json` (Italia 2023, definizione estesa, breakdown rischio povertà)

Tutti via Eurostat statistics REST API v1.0 (JSON), HTTP 200.

## Confronto vs vecchia card

| Aspetto | Vecchia | Nuova |
|---|---|---|
| `attribution` frontmatter | `oecd_eu_observatory` | `istat_eurostat_oecd` (più accurato — ISTAT è la fonte primaria delle cifre principali) |
| `data_metric` | "% rinuncia + tempi attesa + disuguaglianze" (vago) | "rinuncia a prestazioni sanitarie (ISTAT AVQ/BES) + bisogni medici insoddisfatti (Eurostat EU-SILC) + tempi di attesa (OECD)" (esplicita le 3 fonti) |
| `source_url` | `health.ec.europa.eu/state-health-eu/country-health-profiles_en` | `ec.europa.eu/eurostat/databrowser/view/hlth_silc_08/` (link primario all'1,8%) |
| Headline 2,7 mln | "2,7 milioni in lista d'attesa" (errato) | "2,7 milioni hanno rinunciato per liste d'attesa" (corretto, subset del 4,5%) |
| Etichettatura cifre | Nessuna disambiguazione | Tabella esplicita di tre metriche con definizione e perimetro |
| Serie storica EU-SILC | Assente | Presente 2008-2025 con flag cesura 2017 |
| Confronto cross-country | Assente | Tabella UE-13 (DE 0,2% → EE 12,9%) |
| Lettura politica | Generica | Citazioni testuali Tesi 16 + mappatura empirica (raddoppio 2019→2023 attese vs stabilità motivi economici → diagnosi organizzativa, non monetaria) |

## Hash aggiornato

`content_hash: "sha256:2e6096f03c88d77fd5d7905ff90f7ae285debcb0f775f38619b216f5cb61cd1a"` (via `/tmp/restructure_scope_a.py`).

## Caveat / follow-up potenziali (non bloccanti)

- L'1,8% storico EU-SILC potrebbe essere aggiornato al 2025 (2,5%) in un audit successivo se rilevante; per ora la card mostra 2023 come anno principale per coerenza col 7,6% ISTAT-AVQ.
- Card `mobilita-sanitaria-interregionale-italia-2023` referenziata via wikilink — coerenza Nord-Sud delegata a quella card.
- Tesi 16 wikilink usa il nome `16-salute-servizi-sanitari` (verificato esistente).

## Stato finale

- Card aggiornata e hashata.
- Raw persistiti.
- TO_VERIFY marcato `[x]` con sintesi inline.
- Nessuno dei tre block conditions attivato (no failure 3+, 2,7 mln sourcato, nessuna divergenza >20%).
