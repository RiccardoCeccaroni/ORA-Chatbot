---
id: previsione-crescita-pil-italia-2027
type: data
attribution: oecd
quality_tier: D1
title: "Previsione di crescita reale del PIL, Italia, 2023-2027"
data_metric: "tasso di crescita annuale del PIL reale (in volume, prezzi 2020) — % anno su anno"
data_period: "2023-2027 (storico + previsione OECD Economic Outlook Interim Report, marzo 2026)"
source_url: "https://www.oecd.org/en/publications/oecd-economic-outlook-interim-report-march-2026_d4623013-en.html"
source_doc: "OECD — Economic Outlook Interim Report 'Testing Resilience', March 2026. Conferma e raffina i forecast dell'EO No. 118 (dicembre 2025), valori espressi in 1-decimale come da pubblicazione Interim."
date_published: "2026-03"
date_scraped: "2026-05-13"
content_hash: 7609933fee6c2b97875916bb0c87a36d2f29039e04f2c7219abd513685da02fa
tags: [sviluppo-economico-politica-industriale]
description: "Crescita PIL reale Italia: 0,98% (2023), 0,69% (2024), 0,5% (2025 prov.), 0,6% (2026 prev.), 0,7% (2027 prev.). Stagnazione strutturale — uno dei tassi di crescita più bassi UE."
---

# Previsione di crescita reale del PIL, Italia, 2023-2027

**Tassi di crescita PIL reale Italia (OECD Economic Outlook Interim Report, marzo 2026):**

| Anno | Crescita PIL reale (%) | Status |
|---|---|---|
| **2023** | **+0,98%** | Storico (ISTAT) |
| **2024** | **+0,69%** | Storico (ISTAT) |
| **2025** | **+0,5%** | Provvisorio |
| **2026** | **+0,6%** | Previsione OECD |
| **2027** | **+0,7%** | Previsione OECD |

**Quinquennio 2023-2027:** **crescita media reale ~0,7% all'anno** — tra i tassi più bassi UE. L'Interim Report di marzo 2026 raffina al ribasso di pochi centesimi i valori dell'EO No. 118 (dicembre 2025), confermando il quadro di stagnazione strutturale.

## Lettura politica

### Stagnazione strutturale conferma
La crescita italiana **non riesce a superare l'1% all'anno** nelle previsioni dell'OCSE. Confronto con la media UE-27 ~1,3-1,7% nello stesso periodo.

**Conseguenze macro:**
- Il **rapporto debito/PIL** non scende significativamente (debito ~135% / crescita PIL ~3% nominale ≈ debito stabile)
- Le **entrate fiscali crescono lentamente**, vincolando lo spazio per riduzioni di tasse o aumenti di spesa
- Il **gap di PIL pro capite con Germania/Francia si amplia** (vedi card `pil-pro-capite-italia-2024.md`)

### Confronto con dinamica recente
**Crescita 2021-2022 (rimbalzo post-Covid):**
- 2021: +8,3% (effetto base, rebound dal -9% del 2020)
- 2022: +4,7%

**Il "ritorno alla normalità" post-rimbalzo coincide con la stagnazione di lungo periodo italiana**, che era già pre-Covid (2015-2019: +1,0% media annua).

### Cause della stagnazione (documentate OECD/Banca d'Italia)
1. **Bassa produttività** (vedi card `costo-lavoro-unitario-italia-2025.md` e `pil-pro-capite-italia-2024.md`)
2. **Demografia in declino**: forza lavoro che si riduce
3. **Investimenti privati frenati** da: nanismo imprenditoriale, mercato del capitale sotto-sviluppato
4. **Burocrazia + tempi giustizia civile**: vincoli all'attività d'impresa
5. **Debito pubblico** che assorbe risorse via interessi (~3,8% PIL annui)

## Confronto internazionale (orientativo)

**Crescita PIL reale media 2024-2027 (previsione OECD EO 118):**
- **USA:** ~2,0%
- **Germania:** ~0,9% (Italia simile)
- **Francia:** ~1,1%
- **Spagna:** ~2,2%
- **UE-27:** ~1,3-1,5%
- **Italia:** ~0,7%
- **OECD totale:** ~1,8%

Italia + Germania sono **i grandi Paesi UE a crescita più lenta**, ma per ragioni diverse:
- Germania: shock energetico, transizione industriale, perdita di mercati cinesi
- Italia: stagnazione strutturale di lungo periodo, demografica, bassa produttività

## Cosa misura — definizione

**GDPV_ANNPCT** = **Gross Domestic Product, Volume, Growth, Annual Percentage**.

- "Volume" = in **volumi (prezzi costanti)**, al netto dell'inflazione — la crescita REALE
- "Annual percentage" = variazione anno su anno
- "Prezzi 2020" = base anno 2020 per la rivalutazione

⚠️ **NON** è la crescita nominale (che include l'inflazione). Per i valori nominali del PIL → vedi card `pil-italia-2024.md`.

## Caveat e note di lettura

- **Previsioni OECD aggiornate due volte l'anno** via Economic Outlook (maggio/novembre o autunno) e **due volte l'anno via Interim Report** (marzo/settembre). Tra una pubblicazione e l'altra ci sono quindi *due revisioni* delle stesse cifre. I dati qui sono dall'Interim Report di marzo 2026 ("Testing Resilience"), che conferma e raffina il quadro dell'EO No. 118 (dicembre 2025) con scostamenti di pochi centesimi di punto.
- **Le previsioni sono incerte.** Range di confidenza tipicamente ±0,5 punti. Le revisioni storiche su EO sono comuni: i numeri 2025-2027 potrebbero cambiare significativamente nelle prossime edizioni.
- **2024 storico ISTAT vs previsione OECD**: potrebbero differire di decimi (revisioni metodologiche).
- **Crescita potenziale** (output potenziale di lungo periodo) per Italia stimata da OECD/Banca d'Italia: ~0,5-0,8%. Le previsioni quindi indicano crescita **AL livello potenziale**, non sopra. Nessun catch-up vs UE.
- **PNRR e crescita**: l'effetto del PNRR sulla crescita italiana è stato stimato OCSE/MEF in +0,3-0,5 punti aggiuntivi/anno nel 2022-2026. Senza PNRR, la crescita italiana sarebbe stata ancora più debole.
- **Shock geopolitici** (Medio Oriente, Cina-USA, Ucraina): possono rivedere significativamente le previsioni in pochi mesi.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DF_EO/OECD.ECO.MAD,DSD_EO@DF_EO,1.4+.GDPV_ANNPCT.A.csv`
