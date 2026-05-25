---
id: dipendenza-gas-russo-italia-2024
type: data
attribution: bruegel
quality_tier: D3
title: "Dipendenza dell'Italia dal gas russo: il phase-out 2022-2024"
data_metric: "Quote di importazioni italiane di gas naturale dalla Russia; confronto con il baseline 2021 (IEA); flussi UE aggregati dalla Russia 2022-2026"
data_period: "2022-2026 (Bruegel weekly tracker); 2021 baseline da IEA Italy 2023 Energy Policy Review"
source_url: "https://www.bruegel.org/dataset/european-natural-gas-imports"
source_doc: "Bruegel — European Natural Gas Imports tracker (Week 17 2026 = 28/04/2026). Dati primari aggregati da: ENTSO-G, GIE, Eurostat, IEA, AGSI+"
date_published: "2026-04-28 (aggiornamento settimanale)"
date_scraped: "2026-05-12"
content_hash: 584100acc2a413d4fb4a0716b997b3b51d6b460545eff4f870c7fbf170dbf128
tags: [energia-ambiente-sostenibilita, esteri-relazioni-internazionali, sviluppo-economico-politica-industriale, difesa, unione-europea]
description: "Italia ha tagliato la quota di gas russo dal 41% del 2021 al ~7-9% nel 2024 (5,6 bcm su 65 bcm domanda, fonte Italgas CEO 2025). Phase-out via TAP, LNG, Algeria. Flussi UE-totali dalla Russia: -73% tra 2022 e 2025."
---

# Dipendenza dell'Italia dal gas russo: il phase-out 2022-2024

## Headline

- **2021 (baseline IEA):** **41%** delle importazioni italiane di gas naturale dalla Russia (~14 bcm/semestre, ~28 bcm/anno).
- **2024 (Italgas CEO statement 2025 + Statista verifica):** **~5,6 bcm di gas dalla Russia su ~65 bcm di domanda nazionale = 7-8% del fabbisogno**. Pipeline domina ma resta una quota residua via LNG dalla Russia (~0,2 bcm = 1,37% del totale LNG importato).
- **Italia 2024 mix imports gas (Statista/MASE):** 63% via pipeline, 37% via LNG (5 rigassificatori: Panigaglia, Adriatic LNG Cavarzere, OLT Livorno, Italis LNG Piombino, BW Singapore Ravenna).
- **Caduta:** dal 41% (2021) al ~7-8% (2024) = ~33 punti percentuali in tre anni — uno dei phase-out più rapidi nell'UE per un grande consumatore.

## Cosa ha sostituito il gas russo in Italia

L'IEA 2023 Energy Policy Review documenta la diversificazione iniziata già nel 2022:

- **TAP (Trans Adriatic Pipeline) — Azerbaijan:** quota import gas Italia dal 0% (2019) al 10% (2021) al ~14-16% (2023-24).
- **LNG (Adriatic LNG, Panigaglia, OLT Livorno + FSRU Piombino in linea fine 2022):** quota import LNG cresciuta significativamente nel 2022-23, ulteriore espansione con FSRU Ravenna prevista.
- **Algeria (Transmed, via Mazara del Vallo):** già 34% nel 2021, salita oltre il 40% nel 2023.
- **Norvegia, Qatar, USA (LNG):** flussi di diversificazione marginale ma significativi.

## Flussi UE-totali dalla Russia (dato Bruegel — non Italia-specific)

Media giornaliera flussi pipeline Russia → UE (somma di Nord Stream + Ukraine transit + Yamal + Turkstream + altri):

| Anno | Flusso medio giornaliero (unità Bruegel) | Variazione vs 2022 |
|---|---|---|
| 2022 | 186 | baseline (anno di shock + tagli) |
| 2023 | 75 | −60% |
| 2024 | 91 | −51% (lieve rimbalzo da Turkstream) |
| 2025 | 50 | −73% |
| 2026 (al 28/04) | 55 | −70% |

**Eventi rilevanti del periodo:**
- Settembre 2022: sabotaggio Nord Stream 1 e 2 — flusso azzerato.
- Gennaio 2025: cessazione del transito Ukraina (scadenza contratto Gazprom-Naftogaz, non rinnovato).
- 2025-2026: i flussi residui dalla Russia all'UE passano principalmente attraverso Turkstream (verso Ungheria, Slovacchia, Bulgaria).

## Posizione di Italia tra paesi UE

L'Italia è passata dall'essere uno dei più dipendenti dalla Russia (al pari di Germania e Austria) a uno dei più diversificati tra i grandi importatori UE entro il 2024. **Snam, ARERA e MASE** hanno coordinato:
- attivazione TAP a piena capacità
- installazione FSRU Piombino (operativa luglio 2023) e Ravenna (in linea 2024)
- aumento storage strategico (Italia detiene ~200 TWh di storage gas, secondo solo a Germania in UE).

## Caveat e note di lettura

- **Bruegel è D3** (aggregatore think-tank), non D1. I dati primari provengono da ENTSO-G + GIE + Eurostat + IEA + AGSI+. La citazione corretta è "Bruegel European Natural Gas Imports tracker, basato su [primaria]". Per dati più autoritativi su Italia-specific consultare **Snam** (Sistema gas italiano, bollettini mensili) o **ARERA** (relazione annuale).
- **Il dato Italia 9% H1 2024 viene da reporting Bruegel + sintesi giornalistica.** Il file `country_data_2026-04-28.xlsx` nel raw archivio (Bruegel ZIP) contiene la decomposizione Italia per origine ma è un Excel che richiede inspection separata per estrarre la serie esatta 2022-2024.
- **"Quota di import" ≠ "quota di consumo".** Italia consuma anche gas di produzione domestica (~3 bcm/anno, ~4% del consumo). Il dato 9% si riferisce alle importazioni pipeline, non al consumo totale.
- **Il gas russo via LNG (non pipeline)** è una via residua: l'UE non ha bandito il gas russo via LNG fino al 2027 (regolamento UE in negoziazione). L'Italia ha capacità LNG per ricevere ma le quote di LNG russo italiane sono storicamente basse (<2%).
- **Volatilità mensile alta:** una sola statistica annua media nasconde fluttuazioni operative (manutenzioni, livelli di storage). Per uso politico citare sempre il periodo di riferimento.
- I dati Bruegel sono in unità non standard (TWh? GWh? Bruegel pubblica metodologia nel file RTF allegato; verificare prima di citare valori assoluti). Le quote percentuali sono però robuste.

## Sorgente raw

- Primaria (Italia-specific): `_raw/energia-ambiente-sostenibilita/BRUEGEL_GAS_TRACKER/Bruegel_Gas_Tracker_week17_2026.zip` (contiene `country_data_2026-04-28.xlsx` con decomposizione Italia per origine)
- Baseline (2021): `_raw/energia-ambiente-sostenibilita/IEA_2023_REVIEW/Italy_2023_Energy_Policy_Review.pdf` (capitolo 8 "Natural gas")
- Per dato più recente / autoritativo: web search obbligatoria su Snam bollettini, ARERA Annual Report, IEA Country Profile Italy (frequente aggiornamento)
