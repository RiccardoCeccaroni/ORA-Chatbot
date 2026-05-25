---
id: emissioni-ghg-per-settore-nace-italia-2024
type: data
attribution: eurostat
quality_tier: D1
title: "Emissioni di gas serra per settore NACE, Italia, 2024 (industries + famiglie)"
data_metric: "Decomposizione delle emissioni GHG italiane per settore economico NACE Rev. 2 + final demand delle famiglie (residenza Eurostat)"
data_period: "2024 (provvisorio); serie 2008-2024"
source_url: "https://ec.europa.eu/eurostat/databrowser/view/env_ac_ainah_r2"
source_doc: "Eurostat — env_ac_ainah_r2 Air emissions accounts by NACE Rev. 2"
date_published: "2026 (con dato 2024 provvisorio)"
date_scraped: "2026-05-12"
content_hash: 48c864a5f596cf316a420643cc4a73410f44f3b2981d9ff4285d44960aa99eea
tags: [energia-ambiente-sostenibilita, sviluppo-economico-politica-industriale, infrastrutture-trasporti-mobilita, agricoltura]
description: "Italia 2024 (Eurostat NACE): manifatturiero (C) 84 Mt CO2eq, energia (D) 53 Mt, trasporti (H) 41 Mt. Decomposizione del peso settoriale per orientare le politiche di decarbonizzazione."
---

# Emissioni di gas serra per settore NACE, Italia, 2024 (industries + famiglie)

## Decomposizione settoriale 2024 (Eurostat env_ac_ainah_r2)

| Settore (NACE Rev. 2) | GHG 2024 (Mt CO2eq) | % industries | Variazione vs 2008 |
|---|---|---|---|
| **C — Manifatturiero** | **84,2** | 30% | −46% (da 154,8 → 84,2) |
| **D — Fornitura energia elettrica, gas, vapore** | **53,2** | 19% | −62% (da 139,0 → 53,2) |
| **H — Trasporto e magazzinaggio** | **41,0** | 15% | −20% (da 50,9 → 41,0) |
| A — Agricoltura, silvicoltura, pesca | ~25-30 | ~10% | −10% (relativamente stabile) |
| F — Costruzioni | ~5-7 | ~2% | −60% (calo strutturale settore) |
| G+I+J+K+L+M+N — Servizi | ~25-30 | ~10% | −20% |
| Altri (B+E+O+P+Q+R+S) | ~30-35 | ~12% | mix |
| **TOTAL industries** | **282,7** | **100%** | **−39%** |
| TOTAL_HH (famiglie: riscaldamento + trasporto privato) | ~80 | — | — |
| **TOTAL economia (NACE + HH)** | **~363** | — | — |

## Lettura: dove l'Italia ha tagliato — e dove no

**Settori in forte calo (>40%):**
- **D Energia (−62%):** il phase-out del carbone + crescita rinnovabili ha trasformato il settore elettrico italiano. È il successo più visibile della transizione.
- **C Manifatturiero (−46%):** combinazione di deindustrializzazione strutturale + efficientamento + delocalizzazione export-related. Lettura ambigua: parte del taglio è virtuoso (efficienza), parte è perdita di capacità produttiva.

**Settori a calo modesto (<25%):**
- **H Trasporto e magazzinaggio (−20%):** il settore meno migliorato. Italia rimane molto dipendente dal trasporto su gomma. Elettrificazione veicolare ancora marginale.
- **A Agricoltura (−10%):** strutturalmente difficile da decarbonizzare (CH4 zootecnia, N2O fertilizzanti). Calo modesto.
- **Servizi (−20%):** beneficio da elettrificazione + efficientamento edifici, ma terziario è meno energivoro per definizione.

**Famiglie (TOTAL_HH ~80 Mt):** include riscaldamento residenziale (gas naturale dominante in Italia) + trasporto privato (auto). Politiche più importanti: efficientamento edifici (Superbonus + sostituzioni successive), elettrificazione mobilità privata.

## Implicazioni politiche

Il **target Effort Sharing Regulation 2030 per Italia** (−43,7% vs 2005 per settori non-ETS) è particolarmente focalizzato su:
- **Trasporti** (settore non-ETS, escluso aviazione internazionale)
- **Edilizia / Famiglie** (riscaldamento residenziale)
- **Agricoltura** (escluso da ETS)
- **Industria non-ETS** (piccole imprese, alcune filiere specifiche)

L'**ETS** (Emission Trading System UE) copre gli emettitori grandi della categoria D (elettricità, gas) e C (acciaio, cemento, chimica) — settori dove il taglio è già stato massiccio.

**Conclusione strategica:** il prossimo decennio di decarbonizzazione italiana si gioca **fuori dall'ETS** — su trasporti, edifici, agricoltura.

## Confronto sectoral Italia vs UE-27 (qualitativo, basato su Eurostat statistiche explained)

- **Energia (D):** Italia ha un mix elettrico relativamente meno "sporco" della media UE-27 (perché il carbone è in phase-out e gas è meno emissivo del carbone). Settore D italiano ha tagliato −62% dal 2008, in linea con media UE.
- **Manifatturiero (C):** Italia ha tagliato −46%; UE-27 media −35-40%. Italia ha tagliato di più ma anche per ragioni di deindustrializzazione che non sono "virtuose".
- **Trasporti (H):** Italia ha tagliato −20%; UE-27 ~−15-20%. Italia è in linea con UE; nessun paese UE è riuscito a tagliare molto i trasporti.
- **Agricoltura (A):** Italia −10%; UE-27 −5-10%. Italia simile, settore strutturalmente difficile.

## Caveat e note di lettura

- **Eurostat env_ac_ainah_r2 = principio di residenza, non territorio.** Per il dato territoriale UNFCCC (che è quello che conta per i target Paris/Fit-for-55) usare ISPRA NID 2026 (in raw archive). I due numeri sono diversi; vedi card `emissioni-ghg-pro-capite-intensita-italia-2024` per la differenza.
- **TOTAL industries Eurostat (282,7 Mt) ≠ TOTAL UNFCCC (363 Mt).** La differenza (~80 Mt) è il TOTAL_HH_FD (famiglie) — non un errore.
- **Dato 2024 = "estimated"** (suffisso `e` nei raw). Possibili revisioni in cicli successivi.
- **Decomposizione sub-NACE possibile**: env_ac_ainah_r2 ha codici NACE a 2 cifre (~21 settori). Per dettagli più fini (es. C24 acciaio, C23 cemento, H49 trasporto su gomma): filtrare specifico NACE code nel TSV.
- **CO2 puro vs GHG totali**: env_ac_ainah_r2 ha viste sia GHG (tutti i gas serra ponderati AR5) sia CO2 puro. Per gestione climatica usare GHG. Per analisi energetiche specifiche, talvolta solo CO2.
- **Calo C −46% è ambiguo politicamente:** parte è efficientamento autentico (Industry 4.0, sostituzione combustibili), parte è perdita capacità produttiva (delocalizzazioni, chiusure storiche). Il calo "virtuoso" è probabilmente metà del totale.
- **TOTAL_HH_FD non disaggregato in questa card** — per dettaglio (riscaldamento residenziale vs trasporto privato), Eurostat ha viste finer ma richiedono filtro aggiuntivo nel TSV.

## Sorgente raw

- Primaria: `_raw/energia-ambiente-sostenibilita/EUROSTAT_GHG_INTENSITY/env_ac_ainah_r2_raw.tsv.gz` (19 MB compressi — database completo NACE × paese × inquinante × tempo)
- Righe Italia industries TOTAL: `A,GHG,TOTAL,THS_T,IT`
- Righe Italia per settore: `A,GHG,<NACE>,THS_T,IT` (NACE codes: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U)
- Companion quarterly: `_raw/energia-ambiente-sostenibilita/EUROSTAT_GHG_INTENSITY/env_ac_aigg_q_raw.tsv.gz`
- Territorial benchmark (UNFCCC): `_raw/energia-ambiente-sostenibilita/ISPRA_GHG_INVENTORY/ISPRA_NID_2026_Italy_GHG_1990-2024.pdf`
