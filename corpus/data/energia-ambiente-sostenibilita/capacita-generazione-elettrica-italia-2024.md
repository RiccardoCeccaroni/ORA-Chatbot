---
id: capacita-generazione-elettrica-italia-2024
type: data
attribution: terna
quality_tier: D2
title: "Generazione elettrica e capacità FER installata, Italia, 2024"
data_metric: "Generazione elettrica lorda per fonte (GWh); capacità installata solare PV (GW + numero impianti); quota rinnovabili nella generazione"
data_period: "2024; serie storica disponibile"
source_url: "https://www.terna.it/it/sistema-elettrico/statistiche/pubblicazioni-statistiche"
source_doc: "Terna SpA — Dati statistici sull'energia elettrica in Italia 2024 (sezioni 1, 5, 6); GSE — Rapporto Statistico Solare Fotovoltaico 2024 (settembre 2025)"
date_published: "2025-09 (GSE) / 2025 (Terna)"
date_scraped: "2026-05-12"
content_hash: 98f24418d8ca9d516f28a0f6b08a0f5cc431a07d6ee61cc5f14f5305f528937e
tags: [energia-ambiente-sostenibilita, innovazione-crescita, sviluppo-economico-politica-industriale]
description: "Italia 2024: produzione elettrica lorda 271 TWh (+2,4%); domanda 312 TWh (+2,2%); rinnovabili coprono 41,2% della domanda (record storico, +4,1 pt vs 2023). Solare 36 TWh, capacità installata 37,1 GW (+6,7 GW nel 2024)."
---

# Generazione elettrica e capacità FER installata, Italia, 2024

> **Snapshot storico — non più la card di riferimento corrente.** Per la fotografia del sistema elettrico italiano nell'ultimo anno disponibile vedere [[capacita-generazione-elettrica-italia-2025]] (consuntivo Terna pubblicato gennaio 2026: domanda 311,3 TWh, FER 41,1%, PV record +25,1%, +7,2 GW di nuova capacità, 18 GWh di accumuli). Questa card 2024 resta valida come riferimento per (i) il *picco idroelettrico post-siccità* (54,8 TWh, +30%) — paragone obbligato per leggere il calo idrico 2025; (ii) la traiettoria della capacità solare (37,1 GW → 43,5 GW in un anno).

## Generazione elettrica lorda Italia 2024 (Terna)

**Totale: 270.963 GWh (271 TWh)** — +2,4% vs 2023 (264.708 GWh).

| Fonte | GWh 2024 | Quota 2024 | GWh 2023 | Var. 2024 vs 2023 |
|---|---|---|---|---|
| **Termoelettrica** (gas, carbone, oil, bio) | **157.755** | **58,2%** | 168.280 | −6,3% |
| Idroelettrica | **54.757** | **20,2%** | 42.068 | **+30,2%** (rimbalzo da 2022-23 siccità) |
| Fotovoltaica | **35.993** | **13,3%** | 30.711 | **+17,2%** (boom installazioni 2024) |
| Eolica | **22.322** | **8,2%** | 23.641 | −5,6% (anno meno ventoso) |
| Accumulo stand-alone | 136 | 0,05% | 8 | +1500% (deployment iniziale) |

**Note:** Termo include 5.675 GWh di geotermico (Toscana, ~2,1% del mix) e biomassa.

**Rinnovabili totali 2024 (idro + FV + eolico + geo + bio) stimate ~118-120 TWh = ~44% della generazione lorda.** Terna pubblica anche la quota su DOMANDA elettrica nazionale (denominatore include import netti): **41,2% (RES su domanda 2024, record storico, +4,1 pt vs 2023 quando era 37,1%)**. Le due metriche divergono perché Italia importa ~14% del proprio consumo elettrico.

## Capacità solare PV installata (GSE Rapporto Statistico 2024)

- **Totale fine 2024: 37 GW** (37.000 MW) — record storico Italia.
- **Nuova capacità installata nel 2024: +6,7 GW** — secondo anno consecutivo di forte crescita.
- **Numero impianti operativi: 1,88 milioni di unità** — il parco PV italiano per numerosità è il più grande in UE in termini di impianti residenziali.

**Mix per collocazione (Italia, fine 2024):** circa 50/50 tra installazioni a terra (utility-scale + agrivoltaico) e installazioni su edifici/coperture (residenziale + terziario + industriale).

**Distribuzione regionale (densità per km²):** maggiore concentrazione in Puglia, Emilia-Romagna, Lombardia, Veneto. Italia meridionale è leader per ore equivalenti di utilizzazione (irraggiamento).

## Posizione di Italia nel sentiero PNIEC 2030

Il **Piano Nazionale Integrato per l'Energia e il Clima (NECP)** italiano fissa:
- Quota rinnovabili nei consumi finali lordi: **30% al 2030** (target nazionale; aggiornamento FF55 in negoziazione punta a ~37%).
- Quota rinnovabili nella generazione elettrica lorda: **55% al 2030** (target NECP), con possibile revisione al rialzo (Terna+Snam scenario aggiornato).
- Capacità rinnovabile aggiuntiva richiesta entro il 2030: **~70 GW** rispetto al 2021 (solo ~5 GW addizionali tra 2021 e 2022; ~3 GW nel 2023; ~6-7 GW nel 2024 — il ritmo è in accelerazione ma deve aumentare ulteriormente).

**Lettura politica:** con 6,7 GW solo di solare aggiunti nel 2024 (più altre fonti rinnovabili), il 2024 marca il primo anno in cui il ritmo italiano si avvicina al ritmo medio richiesto per il 2030. Tuttavia per i target FF55 il ritmo dovrebbe ulteriormente accelerare.

## Caveat e note di lettura

- **Generazione ≠ consumo (= "domanda" Terna).** L'Italia genera ~271 TWh ma la domanda elettrica nazionale 2024 è **312,3 TWh** (comunicato Terna 2024-12): la differenza (~41 TWh, ~13% della domanda) è coperta da **import elettrico netto** (Svizzera, Francia, Slovenia principalmente). La quota rinnovabili nel CONSUMO differisce da quella nella GENERAZIONE: **44% su generazione lorda, 41,2% su domanda** (Terna 2024 ufficiale).
- **Idro 2024 +30% vs 2023 è un effetto climatico** (rimbalzo da siccità 2022 + parziale 2023). Non assumere stessa crescita per il 2025. La variabilità interannuale dell'idro è strutturalmente alta.
- **Le quote percentuali del mix 2024 differiscono dalle quote IEA 2021** (vedi card `mix-elettrico-italia-2021`): il gas è sceso dal 50% al ~45% (stima da generazione termoelettrica netta 2024); le rinnovabili sono salite dal 40% al ~44%. **Il mix sta evolvendo rapidamente.**
- **GSE è D2** (società di servizi pubblici, non ufficio statistico). **Terna è D2** (TSO). Entrambe SISTAN. Per harmonizzazione UE usare Eurostat `nrg_ind_ren` (D1).
- **Capacità ≠ generazione.** Italia ha 24 GW di solare PV nominale (2022) → 37 GW (2024), ma il fattore di capacità del solare (~15% in Italia) significa che 37 GW producono ~50 TWh/anno teorici (di cui ~36 TWh effettivi nel 2024).
- **Dati Terna non sezione 2:** non incluse nel raw archivio le sezioni 02 BILANCIO (bilancio elettrico dettagliato), 03 IMPIANTI (parco di generazione), 04 OPERATORI (struttura del mercato), 07 MERCATO (PUN, zonal prices), 08 SCAMBIO ESTERO (import/export per paese), 09 QUALITÀ (continuità servizio). Per dettagli su questi temi: download dedicato da `terna.it/it/sistema-elettrico/statistiche/pubblicazioni-statistiche`.
- **Eolico 2024 −5,6%:** non è una contrazione strutturale ma un anno meno ventoso (variabilità climatica). La capacità eolica installata cresce — quel che cambia è il fattore di capacità annuo.

## Sorgente raw

- Terna: `_raw/energia-ambiente-sostenibilita/TERNA_2024/01_DATI_GENERALI_2024.pdf` (bilancio elettrico mensile 2024) + `05_PRODUZIONE_2024.pdf` (Tabella 25, produzione per fonte) + `06_CONSUMI_2024.pdf` (consumi settoriali).
- GSE: `_raw/energia-ambiente-sostenibilita/GSE_RENEWABLES/GSE_Solare_Fotovoltaico_2024.pdf` (capacità + impianti + mappe regionali) + `GSE_Energia_FER_Italia_2023.pdf` (rapporto FER generale 2023, ultima edizione disponibile a 2026-05; la 2024 in arrivo Q3 2026).
