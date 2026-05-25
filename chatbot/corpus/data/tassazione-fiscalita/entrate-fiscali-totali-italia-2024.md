---
id: entrate-fiscali-totali-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Entrate fiscali totali, Italia, 2024"
data_metric: "entrate fiscali totali (accrual, OECD Revenue Statistics) — valore assoluto e composizione per categoria"
data_period: "2024 (provvisorio); serie 2015-2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Revenue Statistics, dataflow DSD_REV_OECD@DF_REVITA (Italy detailed table)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 79f6e94cecb02a6248c5de065797207a338bce0260136db22ac4bc81c46f149c
tags: [tassazione-fiscalita, spesa-pubblica]
description: "Entrate fiscali totali dell'Amministrazione Generale italiana — 940 mld EUR nel 2024, composizione per categoria (imposte dirette, contributi sociali, indirette)."
---

# Entrate fiscali totali, Italia, 2024

**Valore totale (2024, provvisorio):** **940,4 mld EUR** (entrate fiscali totali su base accrual, settore S13 General Government).
**Variazione 2023 → 2024:** +50,7 mld EUR (+5,7%).
**Variazione 2015 → 2024:** +225,8 mld EUR (+31,6% nominale).

## Serie storica — entrate fiscali totali (T_AB, mld EUR accrual)

| Anno | Totale (mld EUR) | Δ vs anno prec. |
|---|---|---|
| 2015 | 714,6 | — |
| 2016 | 719,1 | +0,6% |
| 2017 | 730,7 | +1,6% |
| 2018 | 741,0 | +1,4% |
| 2019 | 763,4 | +3,0% |
| **2020** | **712,3** | **-6,7%** ← shock Covid |
| 2021 | 776,5 | +9,0% |
| 2022 | 839,4 | +8,1% |
| 2023 | 889,7 | +6,0% |
| **2024** | **940,4** | **+5,7%** |

## Composizione 2024 per categoria OECD

| Codice | Categoria | Valore (mld EUR) | Quota |
|---|---|---|---|
| T_1000 | Imposte su redditi e capital gains (persone + società) | 330,3 | **35,1%** |
| T_2000 | Contributi sociali (SSC) | 274,4 | **29,2%** |
| T_3000 | Imposte su salari e forza lavoro (payroll) | 0,0 | 0,0% |
| T_4000 | Imposte su patrimonio (property) | 49,5 | 5,3% |
| T_5000 | Imposte su beni e servizi | 253,8 | **27,0%** |
| T_6000 | Altre imposte | 32,4 | 3,4% |
| **Totale (T_AB)** | | **940,4** | 100% |

## Dettaglio dei due pilastri principali

**Imposte sul lavoro + SSC (T_1000 + T_2000):** **604,7 mld** = **64,3% del gettito totale**. L'Italia è strutturalmente sopra la media OCSE come share di entrate da lavoro/contributi.

**Composizione dei contributi sociali 2024 (T_2000 = 274,4 mld):**
- Datore di lavoro (T_2200): **188,6 mld — 68,7% del totale SSC**
- Lavoratore dipendente (T_2100): 42,3 mld — 15,4%
- Autonomi/non occupati (T_2300): 43,5 mld — 15,9%

Il **68,7% dei contributi sociali è a carico del datore di lavoro** — caratteristica strutturale italiana e principale componente del cuneo fiscale.

**IVA (T_5111) — la singola imposta più importante sul lato consumi:**

| Anno | Gettito IVA (mld EUR) |
|---|---|
| 2019 | 111,5 |
| 2020 | 99,7 |
| 2021 | 121,0 |
| 2022 | 138,5 |
| 2023 | 140,1 |
| **2024** | **145,2** |

L'IVA da sola = **15,4% del gettito fiscale italiano** nel 2024 (145 su 940 mld).

## T_3000 = 0 — non è un errore

L'Italia **non utilizza** la categoria "imposte su salari e forza lavoro" (T_3000, tipo payroll tax USA). La tassazione del lavoro avviene tramite (a) IRPEF (T_1100, dentro T_1000) e (b) contributi sociali (T_2000). Per questo T_3000 è zero costantemente.

## Pressione fiscale (% PIL) — riferimento

Il dato OECD Revenue Statistics più citato in dibattito politico è la **pressione fiscale = Entrate fiscali totali / PIL**.

**Per l'Italia 2023:** ~42-43% del PIL (orientativo — verificare con web search la cifra precisa OECD/ISTAT più recente).
**Per la media OECD:** ~34%.
**Per la media UE-22:** ~40-41%.

L'Italia è strutturalmente tra i 5-6 paesi OCSE con pressione fiscale più alta. **Questo dataset (REVITA) fornisce solo il numeratore (entrate fiscali assolute)**: per ottenere la pressione fiscale come % del PIL serve un dataset OECD parallelo (`DSD_REV_OECD@DF_REV` con UNIT_MEASURE=PT_B1GQ), non incluso in questo batch.

## Metodologia

Framework: **OECD Revenue Statistics** — armonizzato su tutti i paesi OCSE per consentire confronti internazionali. Riconcilia la tassonomia OECD (T_1000…T_6000) con i codici fiscali nazionali italiani (IRPEF, IRES, IRAP, IVA, IMU, accise, ecc.).

- **Settore:** S13 General Government (Stato + Enti locali + Sicurezza sociale).
- **Base:** accrual (competenza). Esiste anche una versione cash (T_AA) leggermente diversa.
- **Definizione di "tassa":** versamenti obbligatori e senza corrispettivo allo Stato (esclude prezzi pubblici, royalty di concessione, multe).
- **Anno fiscale = anno solare** in Italia.

## Caveat e note di lettura

- **Il dato 2024 è provvisorio.** Le entrate fiscali totali sono soggette a revisioni annuali — la cifra finale può variare di 1-2 mld in entrambe le direzioni.
- **Il dato OECD può differire leggermente da quello MEF.** Il MEF (Documento di Economia e Finanza, Bollettino Entrate) pubblica entrate proprie con perimetro talora diverso (incluso/escluso di partite di giro, crediti d'imposta trattati diversamente). Per cifre ufficiali italiane di gettito specifico (es. "quanto ha incassato l'IRPEF nel 2024") la fonte primaria è il MEF, non OECD. OECD è la fonte primaria per **confronti internazionali**.
- **Crediti d'imposta:** la categoria T_AE distingue il diverso trattamento dei crediti d'imposta nei conti nazionali — rilevante per Italia 2021-2024 (Superbonus 110% e simili).
- **Composizione vs livello.** La quota imposte dirette/SSC/indirette è relativamente stabile nel tempo; il livello assoluto cresce con l'inflazione e la crescita del PIL nominale.

## Sorgente raw

`_raw/tassazione-fiscalita/DF_REVITA/OECD.CTP.TPS,DSD_REV_OECD@DF_REVITA,2.1+..S13....A.csv`

Dataset: OECD `DSD_REV_OECD@DF_REVITA(2.1)` — Italy: tax revenues. 1939 righe, 10 anni × ~190 categorie (76 standard OECD + ~115 codici country-specific italiani L_*).
