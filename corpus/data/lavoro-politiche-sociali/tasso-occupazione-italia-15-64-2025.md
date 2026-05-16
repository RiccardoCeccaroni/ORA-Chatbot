---
id: tasso-occupazione-italia-15-64-2025
type: data
attribution: istat
quality_tier: D1
title: "Tasso di occupazione, Italia, 15-64 anni, 2025"
data_metric: "tasso di occupazione 15-64 anni"
data_period: "2025 (annuale, provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Rilevazione sulle Forze di Lavoro (RFL), dataflow DCCV_TAXOCCU1 (150_915)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: 9cb7dd94c1af58e0553c32c09fa5a9f495ebcdb8db0e585b56712413eee564a4
tags: [lavoro-politiche-sociali]
description: "Tasso di occupazione 15-64 anni in Italia, dato annuo 2025 (provvisorio), con serie trimestrale 2023Q4-2025Q4 e ripartizione per classe di età."
---

# Tasso di occupazione, Italia, 15-64 anni, 2025

**Valore (2025, dato annuale provvisorio):** **62,5%**
**Variazione su 2024 (62,2%, definitivo):** **+0,3 p.p.**
**Ultimo dato trimestrale (2025-Q4):** 62,4%

## Serie trimestrale recente (15-64, dati destagionalizzati)

| Trimestre | Tasso di occupazione |
|---|---|
| 2023-Q4 | 62,1% |
| 2024-Q1 | 61,6% |
| 2024-Q2 | 62,3% |
| 2024-Q3 | 62,6% |
| 2024-Q4 | 62,3% |
| 2025-Q1 | 62,5% |
| 2025-Q2 | 62,7% |
| 2025-Q3 | 62,5% |
| 2025-Q4 | 62,4% |

## Ripartizione per classe di età (dato annuale 2025)

| Fascia | Tasso di occupazione |
|---|---|
| 15-24 anni | 17,9% |
| 15-29 anni | 33,1% |
| 25-34 anni | 68,5% |
| 35-44 anni | 76,9% |
| 45-54 anni | 77,7% |
| 55-64 anni | 61,2% |
| **15-64 anni (headline italiano)** | **62,5%** |
| 20-64 anni (target Europa 2030) | 67,6% |

## Metodologia

Fonte: **Rilevazione sulle Forze di Lavoro (RFL)** — ISTAT.
Definizione armonizzata Eurostat (LFS — Labour Force Survey, definizione ILO).
Popolazione di riferimento: residenti 15-64 anni in Italia.
Dataflow: `DCCV_TAXOCCU1` (ID 150_915).

**Dati 2025 provvisori**, soggetti a revisione nel prossimo Rapporto Annuale ISTAT.

## Caveat e note di lettura

- Il dato medio nazionale nasconde **divari regionali significativi** (Nord ~70%, Sud ~50%). Questa view non include la disaggregazione territoriale — è disponibile nello stesso dataflow ma non è in questo batch.
- Le **componenti per età mostrano dinamiche divergenti**: forte crescita over-50 (+2,2 p.p. nella fascia 55-64 fra 2024 e 2025), stabilità per 35-54 anni, **calo per i giovani 15-24** (-1,8 p.p.).
- Il **target europeo Europa 2030** si riferisce alla fascia 20-64 (67,6% in Italia nel 2025; target UE = 78%).
- Il valore italiano 15-64 resta circa 7-9 p.p. sotto la media UE-27 (riferimento Eurostat).
- **Questa view non contiene la disaggregazione per sesso**: in questo dataflow il `_1` (Classe di età) mostra solo il dato aggregato `Sesso = Totale`. Per il gap di genere serve un altro view dello stesso dataflow (non in questo batch).

## Sorgente raw

`_raw/istat/DCCV_TAXOCCU1/Classe di età (IT1,150_915_DF_DCCV_TAXOCCU1_1,1.0).csv`
