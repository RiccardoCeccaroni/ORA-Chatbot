---
id: spesa-pubblica-pil-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Spesa pubblica della PA rispetto al PIL, Italia, 2024"
data_metric: "uscite totali delle Amministrazioni Pubbliche (S13) rispetto al PIL — totale + al netto degli interessi sul debito"
data_period: "2024 (media dei 4 trimestri); serie quarterly 2023-Q1 / 2025-Q4"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Conti economici trimestrali AAPP, dataflow DCCN_FPQ indicatori OTE_R_GDP + OTEXD41_R_GDP"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 3e986a787215520009804336caf3e0f8ebd07cabb0e5db4e9020a90f4a11b251
tags: [spesa-pubblica]
description: "Spesa pubblica Italia 2024: ~50,3% del PIL (totale) e ~47,4% al netto degli interessi sul debito. In calo significativo dal 53,5% del 2023 (uscita misure straordinarie Covid/bonus edilizi)."
---

# Spesa pubblica della PA rispetto al PIL, Italia, 2024

**Valori annuali 2024 (media aritmetica dei 4 trimestri):**

- **Uscite totali della PA / PIL: ~50,3%**
- **Uscite al netto degli interessi sul debito / PIL: ~47,4%**
- **Interessi sul debito impliciti: ~2,9% del PIL** (differenza tra le due metriche)

**Crescita post-Covid significativa:** la spesa pubblica era ~48,5% del PIL nel 2019; salita oltre 60% nel 2020 (Covid); ora in normalizzazione.

## Serie storica — quarterly + medie annue

### Uscite totali / PIL (OTE_R_GDP, %)

| Trimestre | 2023 | 2024 | 2025 |
|---|---|---|---|
| Q1 | 51,4% | 48,8% | 50,2% |
| Q2 | 50,6% | 49,5% | 49,8% |
| Q3 | 50,4% | 47,7% | 48,2% |
| Q4 | 61,4% | 55,2% | 56,0% |
| **Media annua** | **~53,5%** | **~50,3%** | **~51,1%** |

⚠️ **Forte stagionalità Q4** — concentrazione di mensilità aggiuntive (13a stipendi pubblici), saldi annuali di programmi, transferimenti.

### Uscite al netto interessi / PIL (OTEXD41_R_GDP, %)

Italy Q4 2024: 51,5%. Differenza con uscite totali ~3,7 punti (interessi sul debito).

## Cosa include la spesa pubblica AAPP

L'aggregato "**Uscite totali delle PA**" comprende:

1. **Spese correnti**: stipendi, pensioni, sanità, beni e servizi, trasferimenti correnti
2. **Spese in conto capitale**: investimenti fissi, contributi agli investimenti, altri trasferimenti capitale
3. **Interessi passivi sul debito pubblico**

Il perimetro è **S13 General Government** (SEC2010), che include: Stato + Regioni + Province + Comuni + Enti previdenziali (INPS, INAIL) + altri enti pubblici.

## Composizione per funzione (riferimento COFOG, non in questo file)

Composizione approssimativa della spesa pubblica italiana (~€1.100 mld nel 2024):

| Funzione | Quota approssimativa |
|---|---|
| **Protezione sociale** (pensioni + assistenza + ammortizzatori) | ~37% (€407 mld) |
| **Sanità** (SSN) | ~14% (€155 mld) — vedi card `spesa-sanitaria-pil-italia-2024.md` |
| **Pubblica Amministrazione generale** | ~14% |
| **Istruzione** | ~9% |
| **Affari economici** (incl. investimenti infrastrutturali) | ~8% |
| **Difesa + ordine pubblico + sicurezza** | ~6% |
| **Servizi pubblici per la collettività** | ~5% |
| **Cultura, tempo libero, religione** | ~2% |
| **Ambiente** | ~2% |
| **Abitazioni e assetto territoriale** | ~3% |

**Pensioni dominano** la spesa italiana — è la voce singola più grande dello Stato.

## Confronto internazionale (orientativo)

**Media UE-27 2024:** spesa pubblica ~49-50% del PIL. **Italia in linea con UE**, ma il mix è diverso (più pensioni, meno LTC vs Germania/Francia che hanno più spesa per assistenza a lungo termine).

- **Francia 2024:** ~57% del PIL (spesa pubblica più alta UE)
- **Belgio:** ~55%
- **Italia:** ~50%
- **Germania:** ~49%
- **Spagna:** ~46%
- **Irlanda:** ~24% (atipica per PIL gonfiato)

**Italia è nella mediana dell'UE** — non "Paese a spesa pubblica eccezionale". Il vincolo italiano non è la dimensione complessiva ma:
1. **Servizio del debito (~3% del PIL annuo)** — Italia paga interessi più alti per via del debito/PIL al 137%
2. **Spesa per protezione sociale eccessiva** rispetto a spesa per investimenti / istruzione / R&S
3. **Bassa efficienza** in molte voci (mobilità ospedaliera, evasione, opere pubbliche con costi unitari alti)

## Caveat e note di lettura

- **Dato quarterly con stagionalità.** Il valore Q4 (~55-61%) NON è la spesa annuale.
- **Bonus edilizi e Covid emergenziali**: nel 2020-2023 la spesa pubblica italiana è stata gonfiata da:
  - misure Covid (~€80 mld in 2 anni)
  - Superbonus 110% (~€140 mld cumulativi 2020-2024) — registrato come spesa pubblica nei conti SEC2010
- **2025 dato provvisorio** — revisione possibile fino a 2026.
- **Confronto con anni precedenti viziato** dalla riclassificazione contabile dei bonus edilizi (Eurostat ha imposto la classificazione nel 2023 con effetti retroattivi).
- **Spesa pubblica non corrisponde direttamente a indebitamento netto**: spese correnti + capitale formano i deflussi, ma il deficit dipende anche dalle entrate (vedi card complementare `indebitamento-netto-italia-2024.md` e `pressione-fiscale-italia-2024.md`).

## Sorgente raw

`_raw/spesa-pubblica/DCCN_FPQ/Indicatori (in rapporto al PIL) (IT1,95_42_DF_DCCN_FPQ_2,1.0).csv` (indicatori in rapporto al PIL)
`_raw/spesa-pubblica/DCCN_FPQ/Conto economico (IT1,95_42_DF_DCCN_FPQ_1,1.0).csv` (valori assoluti AAPP)
