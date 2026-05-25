---
id: capacita-ospedaliera-italia-2023
type: data
attribution: oecd
quality_tier: D1
title: "Capacità ospedaliera — posti letto e numero di ospedali, Italia, 2023"
data_metric: "posti letto ospedalieri (assoluti + per 1000 abitanti) e numero di ospedali (assoluti + per milione abitanti)"
data_period: "2023; serie 2015-2023"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Hospital beds by sector (DSD_HEALTH_REAC_HOSP@DF_BEDS_SECT) + Hospitals (DSD_HEALTH_REAC_HOSP@DF_HOSP)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 5f9fe5bdc627e0c3f0369018fb5107099acb93e93ca3bfc6fab67ad1b5ba781d
tags: [salute-servizi-sanitari]
description: "Capacità del sistema ospedaliero italiano: 179.372 posti letto (3,04 per 1000 abitanti) e 1.060 ospedali (17,97 per milione abitanti) nel 2023 — entrambi in declino strutturale."
---

# Capacità ospedaliera — posti letto e ospedali, Italia, 2023

**Posti letto (2023):**
- **179.372 totali** (settore B+D = pubblico + privato accreditato)
- **3,04 per 1000 abitanti**

**Numero di ospedali (2023):**
- **1.060 totali**
- **17,97 per milione di abitanti**

Entrambi gli indicatori sono in **declino strutturale di lungo periodo**.

## Posti letto — serie storica

| Anno | Posti letto (assoluti) | Per 1000 abitanti |
|---|---|---|
| 2015 | 194.065 | 3,22 |
| 2016 | 192.315 | 3,20 |
| 2017 | 192.548 | 3,21 |
| 2018 | 189.753 | 3,15 |
| 2019 | 188.909 | 3,16 |
| 2020 | 189.351 | 3,19 |
| 2021 | 184.724 | 3,12 |
| 2022 | 182.210 | 3,09 |
| **2023** | **179.372** | **3,04** |

**Variazione 2015 → 2023:** -14.693 posti letto in 8 anni (-7,6%). Il calo si è accelerato post-2020.

## Numero di ospedali — serie storica

| Anno | Ospedali | Per milione abitanti |
|---|---|---|
| 2015 | 1.115 | 18,51 |
| 2016 | 1.090 | 18,13 |
| 2017 | 1.063 | 17,72 |
| 2018 | 1.059 | 17,61 |
| 2019 | 1.056 | 17,68 |
| 2020 | 1.065 | 17,92 |
| 2021 | 1.060 | 17,93 |
| 2022 | 1.059 | 17,94 |
| **2023** | **1.060** | **17,97** |

**Variazione 2015 → 2023:** -55 ospedali (-4,9%). Il calo si è arrestato dal 2018 — la rete è stabilizzata intorno a ~1.060 ospedali totali.

## Confronto internazionale — verificato OECD/EU Health Profile 2025

- **Italia 2023: ~3 posti letto per 1000 abitanti**
- **Media UE 2023: ~5 posti letto per 1000**
- **Italia è circa il 40% SOTTO la media UE** sui posti letto ospedalieri (PDF Sezione 5.3)
- **Dimissioni ospedaliere Italia 2023: -36% rispetto alla media UE**

L'Italia è strutturalmente low-bed rispetto ai grandi Paesi UE — riflette la strategia di lungo periodo di **deospedalizzazione**.

## Occupazione dei letti e dinamica post-Covid

**Occupazione media posti letto Italia 2023: 75%** — in crescita rispetto al 68% del 2020 (minimo Covid) ma **ancora sotto il livello pre-pandemia di ~79%**.

**Volume dimissioni 2023: -6% rispetto al 2019** — non è ancora tornato ai livelli pre-Covid.

**40% dei ricoveri 2023 sono "day-stay" (1 giorno)** — potenzialmente trattabili in regime ambulatoriale. Indicatore di **inappropriatezza** dei ricoveri o **mancanza di alternative ambulatoriali** in alcune regioni.

**Case mix index** dei ricoveri acuti: **+15% dal 2013 al 2023** — gli ospedali concentrano sempre più sui **casi complessi**, mentre il resto si sposta verso ambulatoriale/day-hospital.

## Mobilità sanitaria interregionale — il dato politico

**Oltre 8% dei ricoveri acuti 2023 avviene fuori regione di residenza** — con tassi del **21% Calabria, 29% Basilicata, 32% Molise** verso il Nord. **€3 miliardi di flussi** finanziari interregionali, 668.145 ricoveri. Vedi card dedicata `mobilita-sanitaria-interregionale-italia-2023.md`.

## Cosa include la definizione OCSE

- **Posti letto:** disponibili regolarmente per ricovero, in ospedali pubblici E privati accreditati (esclusi posti letto in lungodegenza, hospice, RSA se classificati separatamente — la classificazione varia per Paese).
- **Ospedali:** strutture certificate, indipendentemente da posti letto. Include ospedali generali, specialistici, psichiatrici, pubblici e privati accreditati. Esclude RSA, hospice, ambulatori.

## Caveat e note di lettura

- **Il calo NON è automaticamente negativo.** Riflette in parte una **strategia di razionalizzazione**: i ricoveri ordinari calano (medicine progrediscono, day hospital + day surgery sostituiscono ricoveri) e la rete viene riorganizzata. Tuttavia il calo capacità ha anche un risvolto problematico: **liste di attesa lunghe**, **affollamento pronto soccorso**, **stress sul personale**.
- **Differenze territoriali interne molto marcate:** Lombardia ha capacità relativamente alta, Calabria/Molise/Basilicata sono fortemente sotto-dotate. La media nazionale 3,04 nasconde questa variabilità.
- Il numero di ospedali da solo è poco informativo: un ospedale può essere un grande policlinico universitario (1.000+ letti) o una piccola struttura locale (50 letti). La metrica **posti letto** è più indicativa della capacità reale.
- **Tasso di occupazione** non incluso in questo batch — è cruciale: posti letto fisicamente esistenti ≠ posti letto disponibili (vincoli di personale, attrezzature).

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_BEDS_SECT/OECD.ELS.HD,DSD_HEALTH_REAC_HOSP@DF_BEDS_SECT,1.1+..BD+10P3HB.._T.....csv` (posti letto)
`_raw/salute-servizi-sanitari/DF_HOSP/OECD.ELS.HD,DSD_HEALTH_REAC_HOSP@DF_HOSP,1.1+..HSPTL+10P6HB.._T.....csv` (ospedali)
