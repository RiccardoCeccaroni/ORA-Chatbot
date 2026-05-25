---
id: indici-grandi-imprese-retribuzione-costo-lavoro-italia-2026
type: data
attribution: istat
quality_tier: D1
title: "Indici retribuzione e costo del lavoro — Grandi imprese (500+ dipendenti), Italia, 2025-2026"
data_metric: "indici GI: retribuzione lorda media e costo del lavoro per ora lavorata (base 2021=100)"
data_period: "Dati mensili grezzi, ultimo: 2026-02"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Grandi Imprese: retribuzioni e costo del lavoro (dataflow DCSC_GI_RE 535_194 e DCSC_GI_COS 536_193)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: 94da3178b6829fcbafe40ec5bd690a3cd74967eae940686a319cc0ddb1aed3e3
tags: [lavoro-politiche-sociali]
description: "Indici mensili (base 2021=100) delle retribuzioni lorde e del costo del lavoro per ora lavorata nelle imprese con almeno 500 dipendenti, industria e servizi escl. O e P, Italia."
---

# Indici retribuzione e costo del lavoro — Grandi Imprese, Italia, 2025-2026

**Universo:** imprese con **almeno 500 dipendenti**, settore **Industria e Servizi (B-S, escluse O e P)**. **Esclude dirigenti**. Dati **grezzi (non destagionalizzati)**, base **2021 = 100**.

## Indici a confronto, ultime osservazioni (febbraio 2026)

| Indice | Totale dipendenti (PROF=10) | Operaio/apprendista (PROF=5) | Impiegato (PROF=4) |
|---|---|---|---|
| **Retribuzione lorda per ora lavorata** (DCSC_GI_RE) | 101,1 | 103,0 | 100,5 |
| **Costo del lavoro per ora lavorata** (DCSC_GI_COS) | 104,2 | 108,4 | 102,6 |

Entrambi gli indici sono di **~1-4% sopra la base 2021** nei mesi non stagionali.

## ⚠️ Forte stagionalità mensile (dati grezzi)

I valori mensili oscillano in modo marcato per via di tredicesime (dicembre) e premi mid-year. Esempi, indice retribuzione lorda totale dipendenti DCSC_GI_RE:

| Mese | Indice |
|---|---|
| 2025-02 | 96,7 |
| 2025-06 | 135,3 ← quattordicesima/premi stagionali |
| 2025-12 | **175,6** ← tredicesima |
| 2026-01 | 102,9 |
| 2026-02 | 101,1 |

Lo stesso pattern si ripete sul **costo del lavoro** (DCSC_GI_COS), con picchi a giugno e dicembre dovuti alle stesse componenti (mensilità aggiuntive, premi, TFR).

**Per il trend di fondo serve la versione destagionalizzata** (non in questo batch) o una media mobile 12 mesi.

## Differenza fra retribuzione e costo del lavoro

- **Retribuzione lorda** (DCSC_GI_RE) = quanto lordo riceve il dipendente (continuativa + saltuaria/premi/straordinari/arretrati). Esclude contributi previdenziali e TFR.
- **Costo del lavoro** (DCSC_GI_COS) = retribuzione lorda **+ contributi sociali (obbligatori e volontari) + welfare al personale + TFR**. È il costo totale per l'impresa.
- Lo spread fra i due indici riflette l'andamento del **cuneo fiscale** sul lavoro: se il costo del lavoro cresce più della retribuzione, il cuneo si allarga (peggiorando la competitività di costo e/o il netto in busta paga).

## Metodologia

Fonte: **ISTAT — Indici GI (Grandi Imprese)**.
- `DCSC_GI_RE` (535_194): Indice retribuzione lorda media per ora lavorata.
- `DCSC_GI_COS` (536_193): Indice costo del lavoro medio per ora lavorata.
Base: **2021 = 100**.
Frequenza: **mensile**, dati **grezzi** (non destagionalizzati).
Universo: imprese con **almeno 500 dipendenti**, settore B-S esclusi O (Pubblica Amministrazione) e P (Istruzione).
Esclusi: **dirigenti**, settori P.A. e istruzione, microimprese e PMI.

## Caveat e note di lettura

- L'**universo Grandi Imprese (500+ dipendenti)** rappresenta una **piccola frazione del tessuto produttivo italiano** (l'Italia è uno dei paesi UE con la più alta quota di microimprese). Questi indici NON sono rappresentativi dell'intera economia o dei lavoratori italiani in media.
- Il segmento GI è però **strutturalmente più produttivo, più sindacalizzato, e meglio retribuito** rispetto alla media. Le sue dinamiche tendono a anticipare quelle del resto dell'economia (specie su contrattazione e costo del lavoro).
- I **dati grezzi mensili sono dominati dalla stagionalità** (vedere tabella sopra). Per inferenze di breve termine, usare la versione destagionalizzata; per il trend annuale, usare DCSC_RETRCONTR1C (vedere card `indice-retribuzione-contrattuale-italia-2025.md`).
- L'**esclusione dei dirigenti** sottostima il salario "medio" del segmento, che sarebbe più alto se i dirigenti fossero inclusi.
- Settori esclusi (O, P): la **Pubblica Amministrazione e l'Istruzione** hanno dinamiche retributive diverse (legate ai rinnovi contrattuali pubblici) e vanno guardate con altri dataflow.

## Sorgente raw

`_raw/istat/DCSC_GI_RE/Dati grezzi (base 2021) (IT1,535_194_DF_DCSC_GI_RE_9,1.0).csv` (retribuzioni)
`_raw/istat/DCSC_GI_COS/Dati grezzi (base 2021) (IT1,536_193_DF_DCSC_GI_COS_9,1.0).csv` (costo del lavoro)
