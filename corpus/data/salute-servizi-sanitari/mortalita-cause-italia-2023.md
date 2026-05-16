---
id: mortalita-cause-italia-2023
type: data
attribution: istat
quality_tier: D1
title: "Decessi per causa iniziale di morte, Italia, 2023"
data_metric: "numero di decessi per causa iniziale di morte (European Short List), totale e principali categorie"
data_period: "2023; serie 2003-2023"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Decessi e cause di morte, dataflow DCIS_CMORTE1_EV (39_493)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 3c9d28876c1aebac22e6401759a022627940382f4b97cd0dfc93b70adf1c42b2
tags: [salute-servizi-sanitari]
description: "666.131 decessi in Italia nel 2023 (-7,7% sul 2022). Cause principali: malattie circolatorie (206k, 31%), tumori (175k, 26%), respiratorie (53k), nervose (31k)."
---

# Decessi per causa iniziale di morte, Italia, 2023

**Totale decessi 2023:** **666.131**
**Variazione 2022 → 2023:** **-55.843 morti (-7,7%)** — calo significativo dopo l'eccesso 2022.

## Top cause di morte 2023

| Codice ESL | Causa | Decessi 2023 | % del totale |
|---|---|---|---|
| 7 | **Malattie del sistema circolatorio** | **206.119** | **30,9%** |
| 2 | **Tumori** (maligni + benigni) | **175.147** | **26,3%** |
| 8 | Malattie del sistema respiratorio | 52.925 | 7,9% |
| 6 | Malattie del sistema nervoso e organi di senso | 31.023 | 4,7% |
| 5 | Disturbi psichici e comportamentali | 26.718 | 4,0% |
| 17 | Cause esterne (incidenti, suicidi, omicidi) | 26.115 | 3,9% |
| 9 | Malattie dell'apparato digerente | 24.022 | 3,6% |
| 1 | Malattie infettive e parassitarie (incl. AIDS, sepsi) | 17.719 | 2,7% |
| 12 | Malattie genitourinarie | 16.242 | 2,4% |
| **20** | **Covid-19 (codice separato)** | **15.895** | **2,4%** |
| 11 | Sist. osteomuscolare/tessuto connettivo | 4.062 | 0,6% |
| 3 | Malattie del sangue/disturbi immunitari | 3.847 | 0,6% |
| 10 | Cute e tessuto sottocutaneo | 1.777 | 0,3% |
| 15 | Malformazioni congenite | 1.415 | 0,2% |
| 14 | Condizioni perinatali | 641 | 0,1% |

**Cause 1+2+7+8 = 67% del totale decessi**. Le malattie cardiovascolari sono **la prima causa**, seguite dai tumori — pattern tipico di un Paese ad alto reddito con popolazione anziana.

## Confronto 2022 vs 2023

| Causa | 2022 | 2023 | Δ |
|---|---|---|---|
| Totale decessi | 721.974 | **666.131** | **-55.843** |
| Circolatorio | 222.717 | 206.119 | -16.598 |
| Tumori | 174.566 | 175.147 | +581 |
| Respiratorio | 50.686 | 52.925 | +2.239 |
| Covid-19 | 51.630 | 15.895 | **-35.735** ← driver principale del calo |
| Cause esterne | 27.581 | 26.115 | -1.466 |

Il **calo dei decessi 2023** è guidato principalmente dal **ritirarsi della pandemia Covid-19** (da 51.630 a 15.895 morti, -69%). I tumori restano essenzialmente stabili.

## Cosa misura — "Causa iniziale di morte"

La **causa iniziale di morte** è la **malattia o evento che ha innescato la catena di condizioni morbose** che ha portato alla morte (definizione OMS, classificazione ICD-10).

**Esempio:** una persona con diabete che sviluppa insufficienza renale e muore di sepsi: la causa iniziale è il **diabete**, NON la sepsi (anche se la sepsi è la causa immediata).

La codifica ISTAT usa la **European Short List (ESL)** — versione armonizzata della classificazione ICD-10 per confronti internazionali. La cella `Indicatore = DEATH` indica conteggi puri (non tassi).

## Caveat e note di lettura

- **Solo "Italia" in questo file.** Nonostante il filename "Causa - prov.", il filtro di esportazione è stato impostato a livello nazionale. Per le **province/regioni** servirebbe ri-scaricare con filtro REF_AREA = tutti i livelli.
- **Conta solo morti registrate**, esclude italiani deceduti all'estero non rimpatriati.
- **Tumori 2_1 (maligni) = 164.937 nel 2022.** Per la sopravvivenza tumori 5y (politicamente più rilevante delle morti), serve dataset diverso (OECD HCQO 5-year survival, non in questo batch).
- **Cardiovascolare è la causa-leader storica italiana**, ma il share è in **declino strutturale** (~35% nel 2000, 31% nel 2023) grazie a: statine, prevenzione cardiovascolare, controllo ipertensione, calo del fumo. I tumori hanno share in crescita perché la popolazione invecchia.
- **Cause esterne (26k = ~4%)** include: incidenti stradali (~3.000 morti/anno — ISTAT separato), suicidi (~3.500/anno), omicidi (~300/anno), incidenti domestici/lavorativi. Sono cause potenzialmente prevenibili — vedi card complementare sui ricoveri evitabili.
- **Mortalità per Covid-19 dal 2020:** in 4 anni la pandemia ha causato in Italia ~225.000 morti registrate come Covid-19 (codice 20), con eccesso di mortalità totale ancora maggiore (~250.000-280.000 stimati ISTAT 2020-2023).
- **Differenze regionali** non in questo file — Sud strutturalmente con maggior mortalità per cause cardiovascolari e diabetiche.

## Sorgente raw

`_raw/salute-servizi-sanitari/DCIS_CMORTE1_EV/Causa - prov. (IT1,39_493_DF_DCIS_CMORTE1_EV_1,1.0).csv`
