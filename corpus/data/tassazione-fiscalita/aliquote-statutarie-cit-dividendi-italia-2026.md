---
id: aliquote-statutarie-cit-dividendi-italia-2026
type: data
attribution: oecd
quality_tier: D1
title: "Aliquote statutarie di legge — IRES e tassazione dei dividendi, Italia, 2026"
data_metric: "Aliquote statutarie combinate di imposta sui redditi societari (CIT) e ritenuta su dividendi distribuiti, per un'azienda residente e socio persona fisica residente"
data_period: "2026 (snapshot di legge)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Corporate Tax Statistics, dataflow DSD_TAX_CIT@DF_CIT_DIVD_INCOME"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: a42283d4701944a18584d6553f4eedb0a1105628aa9401aee49f90c450b0e408
tags: [tassazione-fiscalita]
description: "Aliquote di legge italiane sui redditi societari e dividendi 2026 — IRES 24%, ritenuta sui dividendi 26%, carico combinato 43,76%."
---

# Aliquote statutarie — IRES e tassazione dei dividendi, Italia, 2026

**Sistema italiano:** **classical system (CL)** — i dividendi sono tassati **due volte**, prima a livello societario (IRES) e poi a livello del socio (ritenuta sostitutiva o IRPEF).

## Le quattro aliquote da ricordare

| Aliquota | Valore 2026 | Cosa misura |
|---|---|---|
| **IRES (CIT_DP)** | **24,0%** | Aliquota nominale dell'imposta sui redditi delle società |
| **Ritenuta dividendi (FWHT)** | **26,0%** | Ritenuta a titolo d'imposta sui dividendi distribuiti a persone fisiche residenti |
| **Carico combinato (CPITCIT)** | **43,76%** | Imposta totale (società + socio) come % del profitto distribuito lordo |
| **Profitto lordo necessario (PTDP)** | **131,58%** | Profitto pre-tasse necessario per consegnare €100 netti al socio finale |

## Come si compone il 43,76%

Partendo da **€100 di profitto societario lordo**:

1. **IRES 24%** → la società versa €24, restano €76 di profitto netto distribuibile.
2. **Ritenuta 26% sui dividendi** → al momento della distribuzione, ulteriori €19,76 vanno allo Stato (26% × 76).
3. **Risultato al socio:** €56,24 netti.
4. **Carico fiscale totale:** €43,76 su €100 = **43,76%** (matematicamente: 24 + (100-24)×26%).

**Inversamente:** per consegnare €100 netti al socio servono **€131,58 di profitto lordo pre-tasse**.

## Confronto con peer dell'Unione Europea (2026)

| Paese | Carico combinato CIT + dividendi |
|---|---|
| 🇮🇹 **Italia** | **43,76%** |
| 🇪🇸 Spagna | 47,50% |
| 🇩🇪 Germania | 48,56% |
| 🇳🇱 Paesi Bassi | 48,80% |
| 🇵🇹 Portogallo | 49,24% |
| 🇫🇷 Francia | 58,74% |

**L'Italia è tra i paesi UE con carico combinato CIT + dividendi più basso**, sotto Germania (-4,8 p.p.), Paesi Bassi (-5 p.p.) e Francia (-15 p.p.). Questo è un dato spesso poco noto nel dibattito interno (concentrato sulla pressione fiscale aggregata, vedi [[entrate-fiscali-totali-italia-2024]]).

**Caveat sul confronto:** alcuni paesi (UK, Belgio, Norvegia) usano sistemi di **partial inclusion** o **partial imputation**, con regole più complesse. L'Italia + Germania + Francia + Spagna + Olanda + Portogallo usano tutti il **classical system** → il confronto è metodologicamente pulito.

## Aliquota effettiva ≠ aliquota statutaria

**Importante:** il 24% di IRES è l'aliquota di **legge**. L'aliquota **effettiva** (cosa pagano realmente le aziende dopo deduzioni, crediti d'imposta, ACE/super-ACE, perdite riportabili) è generalmente **più bassa** — stime OECD/IBFD indicano per l'Italia un'aliquota effettiva CIT intorno al 21-23%.

Per il confronto statutario vs effettivo (Effective Average Tax Rate, Effective Marginal Tax Rate) servirebbe il dataset OECD `DSD_CTS_ETR@DF_CTS_ETR`, non ancora scaricato in questo batch.

## Coerenza con il diritto italiano

Le cifre 2026 da OECD riflettono il quadro IRES + ritenuta vigente:

- **IRES 24%** invariato dal 2017 (riforma Renzi, scesa da 27,5%).
- **Ritenuta dividendi 26%** invariata dal 2014 (la ritenuta sostitutiva è salita dal 12,5% al 20% nel 2012 e al 26% dal 2014 — perfetta uguaglianza con la tassazione sui capital gains).
- **IRAP** non entra in questa metrica (è un'imposta regionale sulla produzione, contabilizzata separatamente — vedi [[imposte-produzione-d29-italia-2025]]). Se inclusa, il carico effettivo italiano salirebbe di ulteriori 3-4 punti.

## Categorie di socio non coperte

Il 43,76% si applica a **persone fisiche residenti che percepiscono dividendi da partecipazioni non qualificate** (quota inferiore al 20-25% del capitale). Casi NON coperti dal calcolo standard OECD:

- **Soci con partecipazione qualificata** (>25% del capitale): dal 2018 anche loro sono soggetti alla ritenuta 26%, ma il regime transitorio aveva regole diverse fino al 2022.
- **Soci persone giuridiche (società):** i dividendi percepiti da società hanno esenzione del 95% (PEX/participation exemption sui dividendi) → carico minimo, ~1,2% sull'utile distribuito.
- **Soci non residenti:** ritenuta al 26% in via generale, salvo convenzioni contro le doppie imposizioni che la abbassano a 15% / 10% / 5% / 0%.

## Metodologia

Framework: **OECD Corporate Tax Statistics** — pubblicazione annuale. Le aliquote sono raccolte da OECD direttamente con le amministrazioni fiscali nazionali (per l'Italia: Agenzia delle Entrate + Dipartimento Finanze MEF). Si tratta di **aliquote di legge**, non di tassi effettivi calcolati su dati di gettito.

- **MEASURE codes principali:**
  - `CIT_DP`: aliquota CIT sui profitti distribuiti = 24% (IRES)
  - `FWHT`: ritenuta a titolo d'imposta sui dividendi = 26%
  - `NPT`: tax netto personale = 26% (= FWHT in regime classical)
  - `PITGUD`: imposta personale sul dividendo grossed-up = 26%
  - `CPITCIT`: carico combinato finale = 43,76%
  - `PTDP`: profitto pre-tasse necessario per €100 netti = 131,58%
  - `PITPITCIT`: quota personale del carico totale = 45,16%
  - `CITPITCIT`: quota societaria del carico totale = 54,84%

## Caveat e note di lettura

- **Single-year snapshot, NON serie storica.** Questo dataset OECD pubblica solo l'anno corrente (2026). Per ricostruire l'evoluzione storica delle aliquote IRES italiane (era 27,5% pre-2017, 33% prima del 2008…) serve consultare la versione precedente del dataset o documentazione MEF.
- **Il combined rate 43,76% è teorico** — vale solo se l'utile è effettivamente distribuito al socio persona fisica residente non-qualificato. Per utili reinvestiti, ceduti tramite quote/azioni, o distribuiti a soggetti diversi, il carico è diverso (vedi sezione precedente).
- **L'Italia ha la PEX al 95%** per i dividendi tra società → la doppia tassazione vale solo all'ultimo step (società → persona fisica), non agli step intermedi.
- **Confronto con paesi non-classical:** alcuni paesi che NON usano il classical system (UK, Norvegia, Australia) hanno meccanismi di imputazione/credito → il loro "combined rate" non è direttamente paragonabile al numero italiano.

## Sorgente raw

`_raw/tassazione-fiscalita/DF_CIT_DIVD_INCOME/OECD.CTP.TPS,DSD_TAX_CIT@DF_CIT_DIVD_INCOME,2.0+.A........csv`

Dataset: OECD `DSD_TAX_CIT@DF_CIT_DIVD_INCOME(2.0)` — Combined corporate and shareholder statutory tax rates on dividend income. 320 righe (40 paesi × 8 measures), 9 righe Italia (tutte per anno 2026).
