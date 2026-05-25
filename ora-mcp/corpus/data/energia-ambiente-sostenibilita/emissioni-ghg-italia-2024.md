---
id: emissioni-ghg-italia-2024
type: data
attribution: ispra
quality_tier: D2
title: "Emissioni totali di gas serra, Italia, 2024"
data_metric: "Emissioni totali CO2-equivalenti (Mt CO2eq) escl. LULUCF; variazione vs 1990 e vs 2023; target di riduzione Effort Sharing Regulation 2030"
data_period: "2024; serie 1990-2024"
source_url: "https://www.isprambiente.gov.it/en/publications/reports/national-inventory-document-2026-italian-greenhouse-gas-inventory-1990-2024"
source_doc: "ISPRA — National Inventory Document 2026 — Italian Greenhouse Gas Inventory 1990-2024 (Rapporti 428/2026, ISBN 978-88-448-0348-3, aprile 2026)"
date_published: "2026-04"
date_scraped: "2026-05-12"
content_hash: af389e0dcfeca835f594a344d7a0c892bd875340f5992048e7480344cae5b05c
tags: [energia-ambiente-sostenibilita, sviluppo-economico-politica-industriale, unione-europea, infrastrutture-trasporti-mobilita, agricoltura]
description: "Emissioni totali Italia 2024: 363 Mt CO2eq (escl. LULUCF), -30% vs 1990, -3,6% vs 2023. Target Effort Sharing Regulation 2030 Italia: -43,7% vs 2005 per i settori non-ETS."
---

# Emissioni totali di gas serra, Italia, 2024

**Valore 2024 (esclusa LULUCF): 363 Mt CO2eq.**

**Variazioni:**
- vs 1990: **−30%** (baseline UNFCCC)
- vs 2023: **−3,6%** (calo accelerato anno-su-anno)

**Driver del calo recente** (per ISPRA NID 2026): crescente adozione di rinnovabili (idroelettrico + eolico in primis) e miglioramenti dell'efficienza energetica nella generazione elettrica e nei settori finali.

## Composizione settoriale (perimetro IPCC)

L'inventario ISPRA segue la classificazione IPCC 2006 (con revisioni 2019). I cinque macro-settori coperti, in ordine di peso storico nelle emissioni italiane:

1. **Energia** (combustione + fuggitive): trasporti, generazione elettrica, riscaldamento residenziale/terziario, industria manifatturiera, industria estrattiva. Storicamente ~70-75% delle emissioni totali.
2. **Industria e uso di prodotti (IPPU)**: processi industriali (cemento, acciaio, chimica), F-gas per refrigerazione.
3. **Agricoltura**: CH4 da fermentazione enterica (zootecnia), N2O da suoli (fertilizzanti), riso, gestione liquami.
4. **LULUCF** (Land Use, Land-Use Change and Forestry): generalmente un *sink* netto in Italia (foreste assorbono più di quanto suolo + cambiamenti d'uso emettono); riportato separatamente.
5. **Rifiuti**: discariche (CH4), trattamento acque reflue, incenerimento.

Per le **scomposizioni settoriali esatte 2024 in Mt CO2eq**, vedi capitolo "Trends in greenhouse gas emissions" del NID 2026 (raw archivio).

## Target europei e di Italia

**Effort Sharing Regulation (Reg (UE) 2023/857) — settori non-ETS (trasporti, edifici, agricoltura, rifiuti, industria non-ETS):**
- **Italia 2030: −43,7%** rispetto al 2005 — uno dei target più ambiziosi tra Stati membri UE.

**EU ETS (Trading System) — settori coperti (grande industria, generazione elettrica, aviazione):**
- **−62% UE-wide** rispetto al 2005 entro il 2030.

**LULUCF (Reg (UE) 839/2023):**
- Target 2030 Italia: assorbimento netto ≥ **35,8 Mt CO2eq** annui dal settore.

**Obiettivo complessivo UE (Fit for 55):**
- **−55% emissioni nette** rispetto al 1990 entro il 2030.

**2050:**
- Neutralità climatica (zero net GHG emissions) per UE inclusa Italia, ai sensi del Climate Law (Reg (UE) 2021/1119).

## Posizione di Italia rispetto al sentiero 2030

- **2024: −30% vs 1990.** Per arrivare al −55% UE-wide 2030, l'Italia (che è parte del target UE complessivo) deve **accelerare di +25 punti percentuali in 6 anni** — un ritmo di riduzione molto più rapido di quello del trentennio 1990-2024.
- Il calo annuo **2023→2024 = −3,6%** è il ritmo storicamente più rapido. Se mantenuto, l'Italia chiuderebbe il 2030 con emissioni ~85% del 1990 (= −15% addizionali su 6 anni) — **non sufficiente** per il target Fit-for-55, ma in linea con la traiettoria nazionale ESR.

## Caveat e note di lettura

- **LULUCF è esclusa dai 363 Mt 2024.** Includendola, l'Italia ha tipicamente uno *sink* netto di ~−30 Mt CO2eq/anno (le foreste assorbono più di quanto emettono i cambiamenti d'uso del suolo); l'emissione netta è quindi più bassa di circa 30 Mt.
- ISPRA è D2 (agenzia ambientale settoriale specializzata, non l'ufficio statistico nazionale). Per confronti UE armonizzati usare anche **Eurostat env_air_gge** (D1), companion nel raw archivio.
- L'aggiornamento del NID arriva ogni aprile per l'anno t-2 (NID 2026 = dati 1990-2024). I dati t-1 (= 2025) saranno disponibili NID 2027.
- Le revisioni metodologiche (es. NID 2026 incorpora per la prima volta il Reg (UE) 2024/1787 art. 12 sul settore oil & gas) **possono rivedere serie storiche** — confrontare sempre con la stessa edizione del NID quando si calcolano percentuali.
- L'**EU Comprehensive Review** del 2025 sotto la Governance Regulation fisserà le quote annuali (AEA) per Italia 2026-2030: questo definisce i vincoli operativi anno-per-anno e va monitorato come benchmark.
- Per emissioni pro capite o intensità su PIL (utili per confronto UE): non incluse direttamente nel NID; calcolare a partire da popolazione ISTAT e PIL nominale/reale Eurostat.

## Sorgente raw

- Primaria: `_raw/energia-ambiente-sostenibilita/ISPRA_GHG_INVENTORY/ISPRA_NID_2026_Italy_GHG_1990-2024.pdf` (ISBN 978-88-448-0348-3, 700+ pagine)
- Companion UE-harmonizzata: `_raw/energia-ambiente-sostenibilita/ISPRA_GHG_INVENTORY/eurostat_env_air_gge_raw.tsv.gz` (Eurostat env_air_gge bulk, fino al 2023 al momento)
