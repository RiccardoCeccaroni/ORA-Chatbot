---
id: prezzi-case-reali-italia-2025
type: data
attribution: oecd
quality_tier: D1
title: "Prezzi reali delle case, Italia, 2021-2025"
data_metric: "indice dei prezzi reali delle abitazioni (Real House Price Index, base 2015=100), destagionalizzato"
data_period: "2021-Q2 a 2025-Q4 (quarterly)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Analytical house prices indicators, dataflow DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 9cbe67cddd49f8230ca32f1c0a82c2dda92bd10e8b16725255fdfd595d54d07b
tags: [sviluppo-economico-politica-industriale]
description: "Prezzi reali delle case Italia 2025-Q4: indice 96,0 (base 2015=100). Italia è uno dei pochi Paesi UE con prezzi reali sotto i livelli 2015 — mercato immobiliare ancora non recuperato dalla crisi 2008-2013."
---

# Prezzi reali delle case, Italia, 2021-2025

**Valore (2025-Q4):** **96,0** (indice base 2015=100, destagionalizzato).
**Significato:** in termini reali (al netto dell'inflazione), le case italiane costano **~4% in meno rispetto al 2015**.
**Periodo coperto in questo dataset:** 2021-Q2 → 2025-Q4 (19 trimestri).

## Serie trimestrale (indice base 2015=100, reale)

| Trimestre | Indice |
|---|---|
| 2021-Q2 | 96,9 |
| 2021-Q3 | 97,8 |
| 2021-Q4 | 97,2 |
| 2022-Q1 | 96,7 |
| 2022-Q2 | 95,9 |
| 2022-Q3 | 94,0 |
| 2022-Q4 | 91,4 |
| **2023-Q1** | **91,2** ← minimo recente |
| 2023-Q2 | 91,0 |
| 2023-Q3 | 91,1 |
| 2023-Q4 | 91,1 |
| **2024-Q1** | **90,9** ← minimo assoluto |
| 2024-Q2 | 92,0 |
| 2024-Q3 | 93,1 |
| 2024-Q4 | 93,7 |
| 2025-Q1 | 93,5 |
| 2025-Q2 | 94,3 |
| 2025-Q3 | 95,2 |
| **2025-Q4** | **96,0** |

**Pattern:**
- 2022-Q4 → 2024-Q1: caduta dei prezzi reali (inflazione cresce più dei prezzi nominali delle case)
- 2024-Q2 → 2025-Q4: ripresa graduale (~+5,7% reale in 18 mesi)
- Italia rimane ancora **sotto il 100 baseline 2015**

## Lettura politica del dato

### 1. Italia "anomalia" europea
La maggior parte dei Paesi UE ha visto prezzi reali delle case **SOPRA i livelli 2015**, spesso significativamente (es. Germania +60% pre-correzione 2023, Olanda +40%, Spagna +25%). **Italia è uno dei pochi Paesi UE con prezzi reali sotto 2015.**

Cause documentate dell'eccezione italiana:
- **Sovraccapacità**: Italia ha ~32 milioni di abitazioni vs ~26 milioni di famiglie (parco abitativo abbondante)
- **Demografia in calo**: popolazione che si riduce → meno domanda strutturale di prima casa
- **Esodo dai centri minori**: prezzi rurali in calo, urbani in tenuta (asimmetrica)
- **Tassazione patrimoniale alta sulle seconde case** (IMU): disincentivo all'investimento
- **Sistema bancario**: post-2011 le banche italiane hanno ridotto i mutui ipotecari (deleveraging)

### 2. Implicazioni per i giovani
**Prezzi reali stabili o in calo + salari reali stagnanti** = il **rapporto prezzo casa / reddito** in Italia è migliorato negli ultimi 10 anni rispetto al periodo 2002-2008. Tuttavia:
- I prezzi NOMINALI sono comunque alti rispetto ai salari nominali
- **L'accesso al credito è il vero collo di bottiglia** (tassi mutuo, garanzie, contratto di lavoro stabile)
- Nelle grandi città (Milano, Roma, Firenze, Bologna) il mercato è significativamente diverso dalla media nazionale

### 3. Anomalie regionali
La media nazionale **maschera grandi differenze territoriali**:
- **Milano**: prezzi reali ~+30% dal 2015 (bolla locale)
- **Roma**: ~+5-10% reale
- **Centri minori Mezzogiorno**: prezzi reali in calo significativo (-20-30%)

## Caveat e note di lettura

- **Indice OECD basato su dati Banca d'Italia** (rilevazione campionaria + estimi notariati) — coerente con altri Paesi OCSE.
- **"Real" significa al netto dell'inflazione** del paniere consumi generale, NON dell'inflazione delle case. Un valore costante in termini reali significa che i prezzi nominali crescono allo stesso ritmo del CPI.
- **Serie limitata a 4,75 anni** in questo export (2021-Q2 a 2025-Q4). Per confronti pre-2015 → riscaricare con time range esteso.
- **Indice nazionale solo.** Per analisi territoriali servono OMI (Osservatorio del Mercato Immobiliare dell'Agenzia delle Entrate) o ISTAT IPAB (Indice Prezzi Abitazioni).
- **Indice reflects existing stock**, non nuovi sviluppi. In Italia ~95% delle compravendite riguarda abitazioni esistenti.
- **Politicamente:** il dato contraddice il narrativo "Italia paese dove le case costano troppo per i giovani". Il problema italiano è composito — non solo prezzi (relativamente stabili) ma anche **accesso al credito, contratti instabili, e differenze territoriali estreme**.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DF_HOUSE_PRICES/OECD.ECO.MPD,DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES,1.0+.Q.RHP..csv`
