# Audit report — 2026-05-12 — folder: `sviluppo-economico-politica-industriale/`

**Modalità:** manuale.

**Cards swept:** 9 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** **critical 1** · moderate 0 · informational 0 · verified 8 · error 0

---

## Critical (1)

### `sviluppo-economico-politica-industriale/previsione-crescita-pil-italia-2027.md` — critical (high confidence)

La stat-card riporta le previsioni di crescita del PIL reale italiano da OECD Economic Outlook No. 118 (rilasciato dicembre 2025): **0,98% (2023), 0,69% (2024), 0,55% (2025 prov.), 0,62% (2026 prev.), 0,74% (2027 prev.)**. La verifica web rileva che OECD ha pubblicato a **marzo 2026 l'Interim Economic Outlook**, che ha rivisto al ribasso le previsioni italiane per shock energetico e conflitto in Medio Oriente:

| Anno | EO 118 (dic 2025, citato dalla card) | Interim Outlook (mar 2026, corrente) | Δ |
|---|---|---|---|
| 2026 | **0,62%** | **0,40%** | **-0,22 p.p.** |
| 2027 | **0,74%** | **0,60%** | **-0,14 p.p.** |

La revisione è materiale: -0,22 p.p. sul 2026 cambia la narrazione "stagnazione lieve" in "stagnazione più marcata, prossima allo stallo." Il 2027 è meno colpito ma comunque revisionato. La card sta usando la pubblicazione precedente di OECD; quella corrente è l'Interim Report marzo 2026.

**Si suggerisce:** aggiornare i valori 2026 e 2027 della tabella nel corpo della card alla revisione marzo 2026 (0,4% e 0,6%), citando come fonte "OECD Economic Outlook Interim Report — March 2026" anziché "OECD Economic Outlook No. 118 (December 2025)". Si suggerisce inoltre di aggiungere una breve nota nel corpo: "i valori sono soggetti a frequenti revisioni in funzione delle pubblicazioni semestrali (giugno/dicembre) e degli Interim Report (marzo/settembre)." La card può lasciare 2023-2024-2025 invariati (storici / consuntivi). I valori revised mantengono la narrazione strutturale del PIL italiano: stagnazione cronica, una delle crescite più lente dell'UE.

- Source URL: https://data-explorer.oecd.org/ (landing page)
- Newer release: **OECD Economic Outlook Interim Report March 2026** — supersedes EO 118 per i forecast 2026-2027.
- Evidence snippet: *"The interim Economic Outlook estimates for Italy a GDP growth of 0.4% in 2026 (against +0.6% in the Economic Outlook published last December) and 0.6% in 2027, from +0.7% in December. These revisions reflect the impact of the Middle East conflict and energy price shocks that occurred after the December forecast."* — OECD, marzo 2026 (riportato da Il Sole 24 Ore)
- Tool calls used: 1

---

## Verified (8)

### Allineate con pubblicazioni ISTAT correnti (settembre 2025)

- **`pil-italia-2024.md`** — card: PIL 2024 €2.202 mld (nominale). ISTAT Conti economici nazionali 2023-2024 (rilascio settembre 2025) definitivo: €2.199,6 mld (+2,7% nominale, +0,7% volume). Discrepanza di €2,4 mld (0,1%) — entro la tolleranza degli arrotondamenti, presumibilmente la card è leggermente in anticipo (stima preliminare) o include una piccola revisione successiva. La crescita 2024 +0,7% volume è confermata. Si suggerisce minor cleanup al prossimo aggiornamento per allineare al definitivo €2.199,6 mld; non urgente.
- **`investimenti-fissi-lordi-italia-2024.md`** — card: €473,7 mld investimenti fissi lordi 2024 = 21,5% del PIL. Coerente con la quota 21-22% riportata dai conti nazionali ISTAT 2024.
- **`pil-pro-capite-italia-2024.md`** — card: €37.350 PIL pro capite 2024, produttività €48,4/ora. Coerente con €2.199,6 mld / 58,99M popolazione = €37.288. Match (rounding sotto 0,2%).
- **`reddito-disponibile-famiglie-italia-2024.md`** — card: €1.296 mld reddito disponibile delle famiglie 2024 = 58,9% del PIL. Quota coerente con i conti settori istituzionali ISTAT.

### Allineate con OECD data-explorer correnti

- **`inflazione-cpi-italia-2025.md`** — card: 1,68% CPI YoY marzo 2026. Today: maggio 2026. Il dato aprile 2026 potrebbe essere stato rilasciato a metà maggio (lag tipico ~15 giorni). La card resta correntemente accurata; minor staleness di 1-2 mesi prevedibile per dati CPI mensili.
- **`costo-lavoro-unitario-italia-2025.md`** — card: ULC +3,2% YoY Q4 2025, produttività -0,3% YoY Q4 2025. Q1 2026 non ancora rilasciato (lag tipico ~2 trimestri). La card è correntemente al punto più recente disponibile.
- **`prezzi-case-reali-italia-2025.md`** — card: Real House Price Index 96,0 al Q4 2025 (base 2015=100). Q1 2026 non ancora rilasciato (lag tipico ~1-2 trimestri). Card correntemente al punto più recente.
- **`struttura-imprese-manifatturiero-italia-2022.md`** — card: 358.488 imprese manifatturiere 2022, 99,6% PMI, 0,4% grandi imprese al 46% fatturato. Dataflow SBS OECD con lag tipico 3-4 anni → 2022 è il dato più recente disponibile a maggio 2026. Pattern del "nanismo" imprenditoriale italiano confermato strutturalmente.

---

## Calibration notes

1. **OECD Economic Outlook ha cadenza più frequente delle pubblicazioni annuali.** EO si pubblica due volte l'anno (giugno + dicembre) e produce due Interim Report l'anno (marzo + settembre). Quindi tra una EO formale e la successiva ci sono **due revisioni delle stesse cifre**. L'auditor deve riconoscere il pattern: una card che cita EO N (anche se è la più recente pubblicazione formale) può essere superseduta da un Interim 3 mesi dopo. Si propone di aggiungere alla spec del prompt una regola specifica: "per forecast IMF/OECD/BCE, controllare sempre se esista un Interim Report/WEO Update/Quarterly Projection più recente della pubblicazione semestrale citata."

2. **PIL definitivo vs preliminare: discrepanze sub-1% sono normali e non sono critical.** Card `pil-italia-2024` con €2.202 mld vs ISTAT definitivo €2.199,6 mld è 0,11% — sotto la soglia di una vera revisione. L'auditor non dovrebbe alzarlo a moderate; verified con minor cleanup suggerito è corretto.

3. **Le card di forecast time-sensitive sono il caso d'uso più valuable per l'auditor.** Una previsione di crescita del PIL è esattamente il tipo di dato che invecchia rapidamente, dove il chatbot potrebbe citare numeri obsoleti a un utente in modo imbarazzante. Si propone, in v2 della spec, di consigliare cadenza di audit più frequente (mensile) per le card categorizzate come "forecast" / "previsione" (riconoscibili da `data_period` che termina in un anno futuro).

---

## Skipped (0)

Prima esecuzione.
