---
id: tasso-disoccupazione-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Tasso di disoccupazione, Italia, 15-64 anni, 2025"
data_metric: "tasso di disoccupazione 15-64 anni"
data_period: "2025 (annuale, provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Rilevazione sulle Forze di Lavoro (RFL), dataflow DCCV_TAXDISOCCU1 (151_914)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: 4c76a07b68af38483c0284721f33aeba80e2e728c91eaa89a5ce7a432678bc00
tags: [lavoro-politiche-sociali]
description: "Tasso di disoccupazione 15-64 anni in Italia, dato annuo 2025 (provvisorio), con tasso giovanile e serie trimestrale 2023Q4-2025Q4."
---

# Tasso di disoccupazione, Italia, 15-64 anni, 2025

**Valore (2025, annuale provvisorio):** **6,3%**
**Variazione su 2024 (6,6%, definitivo):** **−0,4 p.p.**
**Ultimo dato trimestrale (2025-Q4):** 5,7%

## Tasso di disoccupazione giovanile (15-24 anni)

**2025 annuale: 20,6%** — sostanzialmente stabile rispetto al 20,3% del 2024. Il divario rispetto al tasso aggregato (≈14 p.p.) è strutturale: una larga parte dei 15-24 è ancora in formazione, dunque il denominatore "forze di lavoro" è piccolo e il tasso resta alto anche con pochi disoccupati in valore assoluto.

## Serie trimestrale recente (15-64, dati destagionalizzati)

| Trimestre | Tasso di disoccupazione |
|---|---|
| 2023-Q4 | 7,7% |
| 2024-Q1 | 7,9% |
| 2024-Q2 | 6,8% |
| 2024-Q3 | 5,7% |
| 2024-Q4 | 6,2% |
| 2025-Q1 | 7,0% |
| 2025-Q2 | 6,7% |
| 2025-Q3 | 5,8% |
| 2025-Q4 | 5,7% |

## Ripartizione per classe di età (2025 annuale)

| Fascia | Tasso di disoccupazione |
|---|---|
| 15-24 anni | 20,6% |
| 15-29 anni | 14,4% |
| 25-34 anni | 9,0% |
| 35-44 anni | 5,8% |
| 45-54 anni | 4,5% |
| 55-64 anni | 3,6% |
| **15-64 anni (headline)** | **6,3%** |
| 20-64 anni | 6,1% |

## Metodologia

Fonte: **Rilevazione sulle Forze di Lavoro (RFL)** — ISTAT.
Definizione armonizzata Eurostat/ILO: disoccupato = persona 15+ non occupata che (a) ha cercato lavoro attivamente nelle ultime 4 settimane e (b) è disponibile a lavorare entro 2 settimane.
Tasso = disoccupati / forze di lavoro (NON sulla popolazione totale).
Dataflow: `DCCV_TAXDISOCCU1` (ID 151_914).

**Dati 2025 provvisori**, soggetti a revisione nel prossimo Rapporto Annuale ISTAT.

## Caveat e note di lettura

- Il **tasso aggregato 6,3% nasconde divari territoriali forti**: Sud Italia tipicamente 12-15%, Nord 4-5%. La disaggregazione regionale è nello stesso dataflow ma non in questo batch.
- Il **tasso di disoccupazione giovanile (20,6%) è un indicatore frequentemente citato ma spesso male interpretato**: si calcola sui 15-24 *attivi sul mercato*, non sulla popolazione 15-24 totale. Una misura alternativa più rappresentativa dei problemi giovanili è il tasso di occupazione 15-24 (17,9%, vedere card `tasso-occupazione-italia-15-64-2025`) o il tasso NEET.
- Il **trend 2024→2025 è di calo della disoccupazione** (-0,4 p.p.), in linea con la stabilità dell'occupazione (vedere card relativa) e la crescita degli inattivi over-50 che escono dalle forze di lavoro per pensionamento.
- Il **dato armonizzato Eurostat** può differire marginalmente da indicatori amministrativi italiani (es. iscritti NASPI / CPI), che usano definizioni differenti di "disoccupato".
- La disoccupazione di lungo periodo (>12 mesi) e il "tasso di disoccupazione esteso" (che include scoraggiati e part-time involontari) non sono in questa view.

## Indicatori complementari

- Tasso di occupazione 15-64 (2025): 62,5% → `tasso-occupazione-italia-15-64-2025.md`
- Disoccupati totali (2025): 1,58 milioni → `disoccupati-italia-2025.md`

## Sorgente raw

`_raw/istat/DCCV_TAXDISOCCU1/Classe di età (IT1,151_914_DF_DCCV_TAXDISOCCU1_1,1.0).csv`
