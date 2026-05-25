---
id: indice-retribuzione-contrattuale-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Indice della retribuzione contrattuale oraria, Italia, totale economia, 2025"
data_metric: "indice retribuzione contrattuale oraria (base dicembre 2021 = 100)"
data_period: "2025 (annuale)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Indagine sulle retribuzioni contrattuali, dataflow DCSC_RETRCONTR1C (155_318)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: 731bd8d8fd9723dc556212c5637ed8193304ccbb55cff6a22967f50ab40ef6f9
tags: [lavoro-politiche-sociali]
description: "Indice della retribuzione contrattuale oraria in Italia (base dicembre 2021 = 100), totale economia, dato annuo 2025 con serie 2005-2025 e ripartizione per profilo professionale."
---

# Indice della retribuzione contrattuale oraria, Italia, totale economia, 2025

**Valore (2025, totale dipendenti al netto dei dirigenti):** **110,2** (base dicembre 2021 = 100).
**Crescita nominale cumulata dal base (dic 2021):** **+10,2% in 4 anni**.
**Variazione 2024→2025:** **+3,1%** (da 106,9 a 110,2).

## Serie storica annuale (totale economia, totale dipendenti al netto dei dirigenti)

| Anno | Indice | YoY |
|---|---|---|
| 2015 | 95,0 | — |
| 2019 | 98,6 | +0,9% |
| 2020 | 99,1 | +0,5% |
| **2021** | **99,7** | — (anno base) |
| 2022 | 100,8 | +1,1% |
| 2023 | 103,7 | +2,9% |
| 2024 | 106,9 | +3,1% |
| **2025** | **110,2** | **+3,1%** |

Il triennio **2023-2025 ha visto la più forte accelerazione contrattuale del decennio** (~+10,5% cumulativo nominale), in parziale risposta all'ondata inflazionistica 2022-2023.

## Ripartizione per profilo professionale (2025 annuale)

| Profilo | Indice 2025 | Crescita dal 2021 |
|---|---|---|
| Operai | 110,6 | +11,0% |
| Quadri e impiegati | 109,9 | +10,1% |
| **Totale dipendenti (escl. dirigenti)** | **110,2** | **+10,5%** |

## Dato mensile più recente (DCSC_RETRATECO1)

Indice retribuzione contrattuale oraria, totale ATECO, totale dipendenti, dato grezzo mensile più recente:
**2026-03 = 112,1** (totale dipendenti netto dirigenti). Indica un'accelerazione marginale rispetto al dato 2025 (+1,7 punti in 3 mesi).

## Metodologia

Fonte: **ISTAT — Indagine sulle retribuzioni contrattuali**.
Dataflow principale: `DCSC_RETRCONTR1C` (155_318). Dataflow correlato (ATECO mensile): `DCSC_RETRATECO1` (155_358).
Definizione: indice della **retribuzione contrattuale lorda oraria** (NON effettiva), calcolata sulla base dei contratti collettivi nazionali in vigore. Esclude variazioni di fatto (premi aziendali, straordinari, voci accessorie non contrattuali).
Base: dicembre 2021 = 100.
Aggregato: totale economia (codice contratto Z3620), totale dipendenti al netto dei dirigenti (PROF=10).

## Caveat e note di lettura

- **L'indice misura le retribuzioni CONTRATTUALI**, non quelle effettivamente percepite. Le **retribuzioni di fatto** (premi, straordinari, scatti) crescono in modo non perfettamente parallelo — di solito un po' di più nei periodi di crescita economica e meno nelle recessioni.
- La **crescita nominale +10,5% (2021→2025) va confrontata con l'inflazione cumulativa**: l'IPCA italiano è cresciuto di ~17-18% nello stesso periodo. **In termini reali (potere d'acquisto), le retribuzioni contrattuali italiane sono ancora ~6-7 punti percentuali sotto il livello del 2021**.
- Il **divario rispetto alla media UE** è strutturalmente sfavorevole all'Italia: l'OECD documenta che dal 2008 le retribuzioni reali italiane sono cresciute meno della media UE-27. Per confronti internazionali, riferimento Eurostat "Compensation of employees per hour worked".
- **Differenza fra contrattuale e di fatto**: per la retribuzione effettiva mediana del settore privato, vedere card `retribuzione-mediana-oraria-privati-italia-2023.md` (€11,98/ora).
- **Non coperti in questa view:** retribuzioni del settore pubblico isolato; differenze territoriali; effettivi vs contrattuali; retribuzioni non monetarie (welfare aziendale, fringe benefits).

## Sorgente raw

`_raw/istat/DCSC_RETRCONTR1C/Retribuzioni contrattuali (base 2021) (IT1,155_318_DF_DCSC_RETRCONTR1C_4,1.0).csv` (annuale)
`_raw/istat/DCSC_RETRATECO1/Retribuzione oraria e per dipendente (base 2021) (IT1,155_358_DF_DCSC_RETRATECO1_7,1.0).csv` (mensile, ATECO)
