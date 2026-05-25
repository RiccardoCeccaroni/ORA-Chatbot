---
id: indebitamento-netto-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Indebitamento netto (deficit) e saldo primario della PA, Italia, 2024"
data_metric: "indebitamento netto delle Amministrazioni Pubbliche e saldo primario, espressi in % del PIL"
data_period: "2024 (media dei 4 trimestri); serie quarterly 2023-Q1 / 2025-Q4"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Conti economici trimestrali AAPP, dataflow DCCN_FPQ indicatori B9_R_GDP + B9P_R_GDP"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 81dea94c7d842c4263bf1068767fdf478912424fe702e17bb56db73dec9a2422
tags: [spesa-pubblica, tassazione-fiscalita]
description: "Deficit Italia 2024: ~3,5% del PIL (in calo significativo dal 7,2% del 2023). Saldo primario ~0,3% — primo positivo dal 2019. Convergenza verso il 3% Maastricht."
---

# Indebitamento netto (deficit) e saldo primario della PA, Italia, 2024

**Valori annuali 2024 (media aritmetica dei 4 trimestri):**

- **Indebitamento netto / PIL: ~-3,5%** (deficit di bilancio)
- **Saldo primario / PIL: ~+0,3%** (avanzo primario tornato positivo)
- **Servizio del debito implicito: ~3,8% del PIL** (deficit complessivo - saldo primario)

**Significato:** dopo anni di deficit primario (dal 2020 alla 2023), nel 2024 lo Stato italiano **incassa più di quanto spende al netto degli interessi**. **Tutto il deficit è dovuto al servizio del debito pubblico.**

## Serie storica quarterly

### Indebitamento netto / PIL (B9_R_GDP, %)

| Trimestre | 2023 | 2024 | 2025 |
|---|---|---|---|
| Q1 | -11,0% | -8,1% | -8,4% |
| Q2 | -4,9% | -3,7% | -2,7% |
| Q3 | -6,3% | -2,8% | -3,2% |
| Q4 | -6,5% | **+0,6%** | **+1,4%** |
| **Media annua** | **~-7,2%** | **~-3,5%** | **~-3,2%** |

⚠️ **Q4 strutturalmente meglio degli altri trimestri** per via di concentrazione entrate fiscali (IVA, IRES, conguaglio IRPEF). Q1 strutturalmente peggio.

### Saldo primario / PIL (B9P_R_GDP, %)

| Trimestre | 2023 | 2024 | 2025 |
|---|---|---|---|
| Q1 | -7,9% | -4,6% | -4,7% |
| Q2 | -0,7% | +0,8% | +1,6% |
| Q3 | -2,9% | +1,2% | +0,5% |
| Q4 | -2,7% | **+4,4%** | **+5,1%** |
| **Media annua** | **~-3,6%** | **~+0,3%** | **~+0,6%** |

Il **passaggio del saldo primario in positivo nel 2024** è un evento politicamente significativo: l'Italia ha **fermato l'accumulo di debito al netto degli interessi**.

## Cosa significano questi indicatori

### Indebitamento netto (B9)
È il **deficit di bilancio** della PA, secondo definizione SEC2010 = (Entrate totali) − (Uscite totali). Quando negativo, lo Stato si indebita; quando positivo, accumula riserve.

**Regola Maastricht/Patto Stabilità UE**: limite del 3% del PIL. Italia tipicamente sopra negli anni 2010s, ora rientrata.

### Saldo primario (B9P)
È il **deficit AL NETTO degli interessi sul debito**. Misura quanto la gestione corrente dello Stato è in equilibrio.

**Saldo primario positivo + interessi sul debito > saldo primario** = il debito CRESCE in valore nominale (perché paghiamo interessi che ricicliamo emettendo nuovi titoli).

**Saldo primario positivo + interessi sul debito < saldo primario** = il debito SCENDE in valore nominale.

Italia 2024: saldo primario ~+0,3% del PIL, interessi ~3,8% del PIL → debito ancora in crescita nominale, ma a ritmo molto inferiore rispetto al passato.

## Dinamica della riduzione del deficit 2023 → 2024

**Deficit 2023: -7,2% del PIL.** Era gonfiato da:
- Superbonus 110% (€80+ mld registrati come spesa nel 2023 anche se contratti pregressi)
- Crediti d'imposta edilizi vari
- Energia: sussidi alle famiglie, taglio accise carburanti

**Deficit 2024: -3,5%.** Riduzione di **3,7 punti percentuali** in un solo anno — uno dei consolidamenti fiscali più rapidi della storia repubblicana. Cause:
- Phase-out del Superbonus (la coda contabile si è esaurita)
- Fine dei sussidi energetici emergenziali
- Crescita delle entrate fiscali (vedi card `entrate-fiscali-totali-italia-2024.md`)

## Confronto internazionale (orientativo)

**Deficit / PIL UE-27 2024:** ~-3,2% (media ponderata)
- **Francia 2024:** ~-5,5% (sopra Maastricht)
- **Italia 2024:** ~-3,5% (vicino Maastricht)
- **Germania 2024:** ~-2,5% (sotto Maastricht)
- **Spagna 2024:** ~-3,0%
- **Olanda 2024:** ~-1,8%

L'Italia è **rientrata vicino al 3% Maastricht** nel 2024-2025, dopo anni sopra.

## Confronto con debito pubblico (riferimento esterno)

Il deficit annuale **alimenta lo stock di debito pubblico**. Italia 2024:
- **Debito pubblico / PIL: ~135-137%** (riferimento Banca d'Italia, non in questo dataset)
- Italia ha **il secondo debito pubblico più alto UE** dopo la Grecia
- Stock debito ~€2.950 mld nel 2024

Un deficit del 3,5% del PIL aumenta il debito di ~€77 mld/anno. Con PIL nominale che cresce del 2-3% all'anno, il **rapporto debito/PIL tende a stabilizzarsi** ai livelli attuali (135-137%) — non ancora in discesa marcata.

## Caveat e note di lettura

- **Dato quarterly con stagionalità marcata.** Q4 spesso positivo per concentrazione entrate fiscali. Non interpretare un Q4 positivo come "avanzo strutturale".
- **Bonus edilizi**: la classificazione SEC2010 di Superbonus è stata cambiata da Eurostat nel 2023, con effetti retroattivi su 2020-2022. Confronti diretti con anni precedenti vanno verificati per coerenza contabile.
- **2025 dato provvisorio.** Revisioni possibili fino al settembre 2026 (validazione Eurostat).
- **Indebitamento netto ≠ fabbisogno di cassa.** Il deficit SEC2010 è su base "competenza"; il fabbisogno del settore statale (Tesoro) usa criterio "cassa". Possono differire di alcuni decimi.
- **Stock debito ≠ flusso deficit cumulato.** Il debito pubblico cresce anche per: rivalutazione titoli, copertura passività garantite, riclassificazioni Eurostat. Non è solo "somma dei deficit annuali".

## Sorgente raw

`_raw/spesa-pubblica/DCCN_FPQ/Indicatori (in rapporto al PIL) (IT1,95_42_DF_DCCN_FPQ_2,1.0).csv` (B9_R_GDP + B9P_R_GDP)
