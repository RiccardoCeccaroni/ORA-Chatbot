---
id: abbandono-scolastico-precoce-italia-2020
type: data
attribution: istat
quality_tier: D1
title: "Abbandono scolastico precoce (ESL) 18-24 anni, Italia, 2020"
data_metric: "Early School Leavers (ESL) — % di giovani 18-24 anni con al massimo licenza media e non in formazione (regolamento precedente, metodologia pre-2020)"
data_period: "2020 (snapshot — regolamento legacy fino al 2020)"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — dataflow DCCV_ESL_UNT2020 (52_1203) — Giovani che abbandonano prematuramente gli studi (regolamento precedente)"
date_published: "2021"
date_scraped: "2026-05-13"
content_hash: 22d27f16db95cdc226e5c0f9319b9385021d84fa39448225e67460dcce2d16cd
tags: [istruzione, lavoro-politiche-sociali]
description: "Abbandono scolastico precoce in Italia 2020: 13,1% dei 18-24 (M 15,6 / F 10,4). Dato secondo metodologia pre-2020 — riferimento storico. Per il valore corrente vedi card 2024."
---

# Abbandono scolastico precoce (ESL) — Italia, 2020

> ⚠️ **Riferimento storico — regolamento ESL legacy (dataflow ISTAT `DCCV_ESL_UNT2020`).** Il valore 13,1% (2020) è l'ultimo punto della serie pre-Regolamento UE 2019/1700.
>
> **Per il dato corrente (2024 = 9,8%) consultare la card [[abbandono-scolastico-precoce-italia-2024]]**, basata su Eurostat `edat_lfse_14` (post-2020 framework). I due valori non sono direttamente comparabili — breakpoint metodologico stimato ~0,3-0,5 p.p.
>
> Nota: ISTAT non ha mai esposto un dataflow SDMX successore di `DCCV_ESL_UNT2020`. La serie post-2020 vive su Eurostat (alimentata dalla RFL ISTAT) — è quella la fonte D1 effettiva per il dato corrente.

## Headline 2020

**Italia totale (18-24 anni con al massimo licenza media e non in formazione): 13,1%.**

| Categoria | Tasso ESL 2020 |
|---|---|
| Maschi | **15,6%** |
| Femmine | **10,4%** |
| Gap di genere | 5,2 punti percentuali (a sfavore dei maschi) |

L'abbandono scolastico precoce italiano del 2020 è di **circa 3 punti percentuali sopra l'obiettivo UE 2020** (10%) e sopra la media UE (~9,9% nel 2020). Il **gap di genere a sfavore dei maschi è strutturale** in Italia.

## Distribuzione territoriale — Italia 2020 (Totale M+F)

| Area | ESL 2020 (%) |
|---|---|
| **Mezzogiorno** | **16,3%** ← più alto |
| Centro | 11,5% |
| Nord-ovest | 11,8% |
| **Nord-est** | **9,9%** ← unica macro-area sotto target UE 10% |
| Nord (aggregato) | 11,0% |
| **Italia** | **13,1%** |

**Il dato è dominato dal divario territoriale Nord-Sud.** Il Mezzogiorno (16,3%) è di **6,4 punti sopra il Nord-est** (9,9%). Le regioni meridionali concentrano il problema.

## Definizione precisa dell'indicatore ESL

**Early School Leavers (ESL)** = percentuale di giovani 18-24 anni che:
- hanno conseguito **al massimo la licenza di scuola media** (ISCED 0, 1, 2 — fino alla terza media),
- **AND** non sono **in alcun percorso di istruzione o formazione** nelle 4 settimane precedenti all'intervista.

Numeratore: 18-24enni con livello istruzione ≤ ISCED 2 + non in formazione.
Denominatore: tutti i 18-24enni.

Fonte: **Rilevazione sulle Forze di Lavoro (RFL) ISTAT**, definizione armonizzata Eurostat (LFS).

## Cosa cambia tra UNT2020 e versione attuale

Il regolamento UE 2019/1700 ha modificato la **EU Labour Force Survey** dal 2021, cambiando:
- Definizione esatta di "in formazione" (estesa o ristretta per certe formazioni informali).
- Misurazione della condizione di occupazione (concetti ILO aggiornati).
- Trattamento statistico dei casi misti.

→ **I valori pre-2020 (UNT2020) NON sono direttamente comparabili con i valori post-2021.** Le serie ISTAT/Eurostat hanno breakpoint sul 2020-2021.

L'effetto sul dato Italia è stato modesto (~0,3-0,5 punti), ma rilevante per analisi su trend.

## Caveat e note di lettura

- **Snapshot single-year.** Il dataflow DCCV_ESL_UNT2020 contiene la serie storica fino al 2020, ma il file scaricato in questo batch ha **solo l'ultimo anno (2020)**. Per il trend storico (es. 1995 quando l'ESL era ~30%, declino costante fino al 2020) serve un re-export con range temporale esteso.
- **Effetto COVID 2020.** Il 2020 è stato il primo anno di pandemia. L'effetto sull'ESL è stato AMBIGUO: la DAD può aver ridotto l'abbandono (più studenti formalmente iscritti) ma aumentato la dispersione "implicita" (studenti iscritti ma non realmente attivi).
- **ESL ≠ NEET.** L'ESL guarda al *livello di istruzione raggiunto + non in formazione*. Il NEET guarda al *non lavorare e non studiare*, indipendentemente dal livello di istruzione. Sono indicatori complementari, non sostitutivi.
- **Comparazione internazionale 2020:** Italia 13,1% vs UE media 9,9%, Germania 10,5%, Francia 8,0%, Spagna 16,0%. Italia è strutturalmente sopra UE-27 ma sotto Spagna.

## ORA — perché la cifra è politicamente rilevante

L'ESL è uno degli indicatori chiave Europa 2020 / Europa 2030 sull'istruzione. **L'Italia non ha mai raggiunto il target UE-2020 del 10%** (rimasta intorno al 13-14% per tutto il decennio 2010-2020). Il target UE-2030 è 9%. La discussione politica italiana sull'istruzione tocca regolarmente:

- Il divario Nord-Sud (sociale, economico, scolastico).
- Il gap di genere a sfavore dei maschi (15,6% vs 10,4%).
- L'efficacia degli istituti tecnici e professionali (dove l'abbandono Sec II è concentrato).
- Il legame ESL → mercato del lavoro precario / NEET / esclusione sociale.

## Sorgente raw

`_raw/istruzione/DCCV_ESL_UNT2020/Giovani dai 18 ai 24 anni d'età che abbandonano prematuramente gli studi - regolamento precedente (fino al 2020) - Principali dati (IT1,52_1203_DF_DCCV_ESL_UNT2020_1,1.0).csv`

Dataflow ISTAT 52_1203 — vista `_1`. 84 righe (28 territori × 3 sesso). Dimensione: Territorio × Sesso × Cittadinanza × Tempo.

**To-update path:** ri-scaricare `DCCV_ESL` (dataflow successore) per la serie post-2021.
