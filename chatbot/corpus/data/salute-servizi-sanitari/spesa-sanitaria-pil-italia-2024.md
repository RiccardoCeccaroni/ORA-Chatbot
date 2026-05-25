---
id: spesa-sanitaria-pil-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Spesa sanitaria totale come % del PIL, Italia, 2024"
data_metric: "spesa sanitaria corrente totale come percentuale del PIL (framework SHA 2011)"
data_period: "2024 (provvisorio); serie 2015-2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Health expenditure and financing, dataflow DSD_SHA@DF_SHA"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 4d681dcc262c98ff327529b0ac0d70b2d1b19ffb01f1e0e5af445b05b58fd922
tags: [salute-servizi-sanitari, spesa-pubblica]
description: "Spesa sanitaria corrente totale (pubblica + privata + OOP, framework OCSE SHA) come % del PIL — Italia 8,44% nel 2024."
---

# Spesa sanitaria totale come % del PIL, Italia, 2024

**Valore (2024, provvisorio):** **8,44% del PIL**.
**Variazione 2023 → 2024:** +0,03 punti (stabile, dopo il calo post-Covid).
**Pre-pandemia (media 2015-2019):** ~8,7% del PIL.

## Serie storica

| Anno | % PIL |
|---|---|
| 2015 | 8,85 |
| 2016 | 8,72 |
| 2017 | 8,69 |
| 2018 | 8,66 |
| 2019 | 8,62 |
| **2020** | **9,56** ← picco Covid |
| 2021 | 9,28 |
| 2022 | 8,85 |
| 2023 | 8,41 |
| **2024** | **8,44** |

Il dato 2024 (8,44%) è **inferiore al livello pre-pandemia 2015 (8,85%)**. Dopo lo shock Covid che ha portato la spesa al 9,56% del PIL nel 2020, l'Italia è tornata sotto i livelli del decennio precedente.

## Cosa include (framework SHA 2011)

L'indicatore segue il **System of Health Accounts 2011** dell'OCSE. Include la spesa sanitaria corrente di **tutte le fonti**:

- spesa pubblica (SSN, finanziata da fiscalità generale)
- spesa privata obbligatoria (assicurazioni private compulsorie — quasi nulla in Italia)
- spesa privata volontaria (fondi sanitari integrativi, polizze)
- spesa **out-of-pocket** delle famiglie

**Esclude:** spesa in conto capitale (investimenti in strutture, attrezzature), che è classificata separatamente.

## Confronto internazionale — verificato OECD/EU Health Profile 2025

**Spesa sanitaria pro capite 2023:**
- **Italia: ~€3.104** (calcolato in EUR, PPP-adjusted)
- **Media UE: €3.832**
- **Differenza Italia: -19%** rispetto alla media UE

**Decomposizione della spesa Italia (2023):**
- **Spesa PUBBLICA pro capite: -27% sotto la media UE** — è qui che il gap è più ampio
- **Spesa PRIVATA pro capite: +8% sopra la media UE** — le famiglie italiane compensano in parte la minore copertura pubblica
- **Quota pubblica sul totale: 73%** — sotto la media UE
- **27% spesa privata, di cui ~90% out-of-pocket diretto**

**Spesa sanitaria come quota della spesa pubblica TOTALE italiana:**
- **2015-2019:** stabile intorno al 14%
- **2023:** scesa al **12% — minimo storico**
- La sanità ha perso peso relativo nel bilancio statale per via di: bonus edilizi (crediti d'imposta ristrutturazioni), aumento interessi sul debito pubblico, altre voci prioritarie.

**Dinamica recente Italia (spesa pubblica pro capite):**
- 2015-2019: crescita +0,7%/anno (vs UE +2,9%) — Italia rallentata
- 2019-2021: +9% reale (Covid spending)
- 2022: -3,5% reale
- 2023: -4,5% reale → **ritorno ai livelli pro capite del 2019**

L'Italia è uscita dall'emergenza Covid riportando la spesa pubblica sanitaria pro capite ai livelli pre-pandemici, ma è **sotto la traiettoria di crescita implicita pre-Covid**.

## Caveat e note di lettura

- **% PIL ≠ spesa pubblica.** L'8,44% include anche la spesa privata e l'out-of-pocket delle famiglie. Per la spesa pubblica isolata (SSN) serve un filtro diverso del DSD_SHA (FINANCING_SCHEME = HF1 = government schemes), non incluso in questo batch.
- **Italia è strutturalmente alta su OOP** (~22-24% del totale), il che significa che la quota pubblica è ancora più bassa del valore aggregato suggerisce. Per la spesa pubblica solo, l'Italia è intorno al **6,3-6,6% del PIL** (riferimento OCSE, da verificare con web search).
- Il declino post-2021 riflette: (a) ritiro dei finanziamenti emergenziali Covid, (b) crescita del PIL nominale post-pandemica più rapida della spesa sanitaria.
- I dati OCSE sono armonizzati ma le elaborazioni nazionali possono differire — i Conti AAPP ISTAT producono talora valori leggermente diversi per la spesa sanitaria pubblica.

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_SHA/OECD.ELS.HD,DSD_SHA@DF_SHA,1.0+.A.EXP_HEALTH.PT_B1GQ._T.._T.._T....csv`
