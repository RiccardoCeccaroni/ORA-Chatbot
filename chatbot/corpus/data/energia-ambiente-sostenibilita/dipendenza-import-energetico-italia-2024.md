---
id: dipendenza-import-energetico-italia-2024
type: data
attribution: eurostat
quality_tier: D1
title: "Dipendenza energetica dell'Italia dalle importazioni, totale e per fonte, 2024"
data_metric: "Energy imports dependency rate = (net imports) / (gross inland consumption + bunkers), espressa in %. Per fonte (TOTAL, gas, petrolio, solidi)."
data_period: "2024; serie 1990-2024"
source_url: "https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_id"
source_doc: "Eurostat — nrg_ind_id Energy imports dependency"
date_published: "2026 (con dato 2024)"
date_scraped: "2026-05-12"
content_hash: b072b6d2e5cc342b9ee49a4cb98558079c123ca1bd56a50138323bf4fe8b568d
tags: [energia-ambiente-sostenibilita, esteri-relazioni-internazionali, sviluppo-economico-politica-industriale, difesa]
description: "Italia 2024 totale dipendenza energia import: 73,9% (massimo storico 79,5% nel 2022, calo dopo phase-out gas russo). Gas: 95,2%. Italia è uno degli importatori netti più strutturalmente esposti dell'UE."
---

# Dipendenza energetica dell'Italia dalle importazioni, totale e per fonte, 2024

## Valori 2024

| Fonte | Quota netta import / consumo lordo, 2024 |
|---|---|
| **Totale energia (tutte le fonti)** | **73,88%** |
| **Gas naturale** | **95,19%** |
| Petrolio (stima storica) | ~85-90% |
| Combustibili solidi (carbone) | ~100% (Italia non produce carbone) |

## Traiettoria 2020-2024 (totale)

| Anno | Quota import netto / lordo |
|---|---|
| 2020 | 73,45% (calo per Covid: meno consumo, meno import) |
| 2021 | 73,42% |
| **2022** | **79,49%** (picco crisi gas: import LNG aumentato per sostituire gas russo) |
| 2023 | 75,36% (parziale rientro) |
| **2024** | **73,88%** (ritorno verso il livello pre-crisi) |

**Lettura:** la dipendenza energetica italiana è **strutturalmente alta** (~70-75% storica). Il picco 2022 è dovuto a:
- aumento netto delle importazioni LNG per rimpiazzare il gas russo;
- contemporanea contrazione del consumo lordo (efficientamenti + razionamento) — ma il numeratore (import) è cresciuto più del denominatore.

Il rientro 2023-2024 è dovuto a:
- consolidamento delle nuove rotte di approvvigionamento (TAP, LNG diversificato);
- crescita della produzione rinnovabile domestica (solare PV in particolare).

## Confronto Italia vs UE-27 e peers

- **Media UE-27 2024**: ~58% (Italia è 16 punti sopra).
- **Paesi UE meno dipendenti**: Estonia (~5-10%), Romania (~30%) — risorse domestiche.
- **Paesi UE più dipendenti**: Cipro (~95%), Malta (~95%), Lussemburgo (~95%), Irlanda (~75%), Belgio (~80%), Italia (~74%).
- **Germania 2024**: ~65%.
- **Francia 2024**: ~45-50% (basso per la quota nucleare domestica).
- **Spagna 2024**: ~70%.

**Posizione di Italia tra i grandi consumatori UE:** secondo importatore netto in valore assoluto dopo la Germania, ma più dipendente in quota.

## Composizione: dove importa l'Italia, 2024

- **Gas (95% import dipendenza, ~70 bcm import 2024):** Algeria (~40%), Azerbaijan (~15%), LNG diversificato (Qatar, USA, Egitto, ~25%), Norvegia (~5%), Russia residuo (~9%, calo da 41% nel 2021).
- **Petrolio (~85-90% import dipendenza, ~60 Mt crude oil + prodotti):** Azerbaijan, Iraq, Libia, Arabia Saudita, Kazakistan (mix multi-origine post-2022).
- **Carbone (~100% import):** in calo strutturale per il phase-out coal-power Italia entro il 2025 (escluso Sardegna 2028).
- **Elettricità (saldo netto importatore, ~14% del consumo elettrico):** Svizzera, Francia, Slovenia.

## Implicazioni per le politiche energetiche

**1. Sicurezza energetica.** Una dipendenza al 74% espone l'Italia a shock geopolitici (cf. invasione Ucraina 2022). Le politiche di sicurezza energetica si concentrano su: diversificazione delle origini, espansione storage, produzione domestica rinnovabile, efficientamento.

**2. Bilancia dei pagamenti.** L'import netto energetico italiano vale ~€60-90 mld/anno (2022-23 al picco prezzi; €40-50 mld in regime normale). Una riduzione strutturale tramite rinnovabili migliora il saldo corrente.

**3. Target UE.** L'UE non ha un target esplicito di import dependency (l'obiettivo è espresso come quota rinnovabili), ma REPowerEU 2022 e Net-Zero Industry Act 2023 puntano implicitamente a una riduzione coordinata della dipendenza dai fossili → riduzione automatica della dipendenza da import per i fossili.

## Caveat e note di lettura

- **Definizione metodologica:** dipendenza energia = (Import netti) / (Consumo interno lordo + Bunker marittimi internazionali). Per fonte singola, lo stesso rapporto applicato solo a quella fonte.
- **Valori >100% sono possibili** se il consumo netto è zero o negativo (es. paesi esportatori netti durante una crisi). L'Italia è stabilmente importatore netto.
- **L'import netto include il transito**: il gas che attraversa l'Italia verso altri paesi UE (es. Slovenia, Austria) non è consumo italiano, ma fattore "Imports" nel calcolo. Per il consumo italiano effettivo, depurare via Snam (bilanci fisici).
- **Dipendenza al 95% sul gas non significa "rischio gas al 95%"** — Italia ha ~3 bcm di produzione domestica + ~200 TWh di storage strategico (secondo solo a Germania in UE) + LNG flessibile + diversificazione delle origini. La resilienza operativa è ben superiore al numero sintetico.
- **Sintesi di stock vs flow:** la dipendenza misura il flow annuale, non lo stock di sicurezza (storage + diversificazione contrattuale). Per dibattito su sicurezza energetica serve sempre confronto con storage levels (AGSI+) e fonti diversificate (Snam, IEA Country Profile).

## Sorgente raw

- Primaria: `_raw/energia-ambiente-sostenibilita/EUROSTAT_IMPORT_DEPENDENCY/nrg_ind_id_raw.tsv.gz` (+ `.tsv` decompressa)
- Riga TOTAL: `A,TOTAL,PC,IT`
- Riga Gas: `A,G3000,PC,IT`
- Companion energy balances (per analisi più fini): `_raw/energia-ambiente-sostenibilita/EUROSTAT_RES_SHARE/nrg_bal_c_raw.tsv.gz`
