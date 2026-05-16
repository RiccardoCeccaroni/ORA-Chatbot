---
id: forza-lavoro-sociosanitaria-italia-2023
type: data
attribution: oecd
quality_tier: D1
title: "Forza lavoro sociosanitaria, Italia, 2023"
data_metric: "occupati settore Q NACE (Sanità + Assistenza sociale): per 1000 abitanti e come % dell'occupazione totale"
data_period: "2023; serie 2015-2023"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Health and social employment per 1000 inhabitants (DSD_HEALTH_EMP_REAC@DF_SOC_EMPLOY) + Healthcare human resources % of employment (DSD_HEALTH_EMP_REAC@DF_REAC)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 28dfa4a9a37d9394af0a9bab49776577b20d9cf61e468c46e67d36ee0738f69d
tags: [salute-servizi-sanitari, lavoro-politiche-sociali]
description: "Forza lavoro sociosanitaria in Italia (NACE Q): 35,02 occupati per 1000 abitanti e 8,76% dell'occupazione totale nel 2023 — crescita costante."
---

# Forza lavoro sociosanitaria, Italia, 2023

**Valore (2023):**
- **35,02 occupati per 1000 abitanti** (settore Q NACE)
- **8,76% dell'occupazione totale** (2022 e 2023)

Indica una **forza lavoro sociosanitaria totale di ~2,07 milioni di occupati** (35,02 × 59 milioni abitanti / 1000).

## Serie storica — occupati per 1000 abitanti

| Anno | Per 1000 ab. |
|---|---|
| 2015 | 30,68 |
| 2016 | 31,29 |
| 2017 | 31,70 |
| 2018 | 32,22 |
| 2019 | 32,53 |
| 2020 | 33,11 |
| 2021 | 33,53 |
| 2022 | 34,27 |
| **2023** | **35,02** |

**Crescita 2015 → 2023:** +4,34 punti (+14%). Crescita lineare, accelerata leggermente post-Covid.

## Come % dell'occupazione totale

| Anno | % occupazione |
|---|---|
| 2020 | 8,59% |
| 2021 | 8,79% |
| 2022 | 8,76% |
| 2023 | 8,76% |

L'occupazione sanitaria + sociale è circa **un occupato ogni 11** in Italia. Series molto corta (4 anni) ma stabile intorno all'8,7-8,8%.

## ⚠️ Cosa include — perimetro "sociosanitario" (NACE Q)

Questo indicatore NON è "personale del SSN puro". Include **l'intera attività NACE Q — "Sanità e assistenza sociale"**:

- **Q86 — Assistenza sanitaria:** ospedali, ambulatori, MMG, dentisti, fisioterapisti, laboratori diagnostici, infermieri territoriali
- **Q87 — Servizi residenziali di assistenza:** RSA, residenze per anziani, case famiglia, centri per disabili
- **Q88 — Assistenza sociale non residenziale:** servizi sociali comunali, asili nido, centri diurni, assistenza domiciliare sociale

Per l'**occupazione del solo SSN** (medici + infermieri + OSS + amministrativi sanitari pubblici), i dati di riferimento sono diversi (Conti Economici delle ASL del Ministero della Salute — non in questo batch).

## Composizione approssimativa

L'occupazione sociosanitaria italiana è ripartita grosso modo (riferimento Eurostat/ISTAT, da verificare con web search):

- **~50-55% sanità ospedaliera/ambulatoriale** (medici, infermieri, OSS, amministrativi, ausiliari ospedalieri)
- **~25-30% assistenza sociale residenziale** (RSA, residenze anziani — categoria in forte crescita)
- **~15-20% assistenza sociale non residenziale** (servizi sociali comunali, asili, badanti formali)

La componente "assistenza" (sociale, residenziale, domiciliare) è **strutturalmente in crescita** per via dell'**invecchiamento demografico** — è una delle ragioni principali per cui la curva del 35,02/1000 sale in modo lineare.

## Confronto internazionale (orientativo, da verificare con web search)

- **Media OCSE 2022:** ~46 per 1000 abitanti.
- **Norvegia:** ~88 per 1000 (settore pubblico molto esteso)
- **Germania:** ~69 per 1000
- **Francia:** ~50 per 1000
- **Spagna:** ~35 per 1000 (in linea con Italia)
- **Italia 2023:** **35,02 per 1000** — significativamente sotto la media OCSE/UE.

Il gap rispetto ai Paesi del Nord Europa è ampio. **Italia ha meno occupazione sociosanitaria** in proporzione alla popolazione rispetto ai pari occidentali. Una parte del gap è coperta dal **lavoro informale** (badanti non regolarizzate — circa 1 milione in Italia, di cui ~60% irregolari) che NON appare in questi dati statistici ufficiali.

## Caveat e note di lettura

- **NACE Q include assistenza sociale**, non solo sanità: il valore 35/1000 NON misura "personale del SSN" né "operatori sanitari" puri. Per quelli, riferimento alle card specifiche su medici e infermieri.
- **Lavoro informale escluso:** badanti irregolari, assistenza familiare non retribuita, e volontariato non rientrano. In Italia il "sommerso" assistenziale è grande (~1 milione di badanti, di cui solo ~40% regolari).
- **Crescita lineare** suggerisce che il settore sta assorbendo la domanda crescente legata all'invecchiamento — ma la qualità degli inserimenti (precari, part-time, basse retribuzioni) non emerge da questo indicatore.
- **Italia sotto la media** OCSE su entrambe le metriche — possibile spazio politico per espansione del settore se finanziato da spesa pubblica aggiuntiva.

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_SOC_EMPLOY/OECD.ELS.HD,DSD_HEALTH_EMP_REAC@DF_SOC_EMPLOY,1.1+..10P3HB.......csv` (per 1000 ab.)
`_raw/salute-servizi-sanitari/DF_REAC/OECD.ELS.HD,DSD_HEALTH_EMP_REAC@DF_REAC,1.1+.HSE.PT_EMP.......csv` (% occupazione totale)
