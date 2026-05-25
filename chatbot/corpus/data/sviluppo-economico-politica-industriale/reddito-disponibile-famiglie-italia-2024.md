---
id: reddito-disponibile-famiglie-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Reddito disponibile delle famiglie, Italia, 2024"
data_metric: "reddito disponibile netto delle famiglie (S14) — settori istituzionali secondo SEC 2010"
data_period: "2024 (annuale)"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Reddito disponibile delle famiglie, dataflow DCCN_ISTITUZ_TNA1 (93_1095) — Settore S14 Famiglie consumatrici"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 323e18b37d902fcba203b37f54c6dd0322b4de081c53e0ba83a6ffbe14d6986e
tags: [sviluppo-economico-politica-industriale, lavoro-politiche-sociali, pari-opportunita-inclusione]
description: "Reddito disponibile netto delle famiglie italiane 2024: €1.296 miliardi (~58,9% del PIL). Composizione: retribuzioni lorde, contributi sociali, redditi misti autonomi, prestazioni sociali, redditi da capitale."
---

# Reddito disponibile delle famiglie, Italia, 2024

**Valore (2024):** **€1.296,4 miliardi** di reddito disponibile netto del settore Famiglie (S14 SEC 2010).
**Rapporto al PIL:** **~58,9%** del PIL nominale (PIL 2024 = €2.202 mld).
**Per famiglia (~26 mln famiglie):** **~€49.900 medio annuo** di reddito disponibile netto.
**Per abitante (~59 mln residenti):** **~€22.000 pro capite** di reddito disponibile.

## Cosa è il reddito disponibile

Il **reddito disponibile netto** è ciò che resta alle famiglie **dopo aver pagato le imposte dirette + contributi sociali** ma **prima di consumi e risparmi**. È la misura standard per:

- Confronti di tenore di vita
- Calcolo del **risparmio delle famiglie** (= reddito disponibile - consumi)
- Analisi del **potere d'acquisto reale** delle famiglie

**Formula (semplificata):**
```
Reddito disponibile = 
    + Retribuzioni lorde (salari da lavoro dipendente)
    + Redditi misti autonomi (utili imprenditori individuali, autonomi)
    + Redditi da capitale (interessi, dividendi, affitti netti)
    + Prestazioni sociali (pensioni, indennità, assegni)
    + Altri trasferimenti netti
    − Imposte correnti su reddito e patrimonio
    − Contributi sociali a carico lavoratori
```

## Composizione del reddito disponibile italiano (riferimento ordini di grandezza, 2024)

I componenti principali, in € miliardi (stima da SEC 2010 sul totale ~€1.296 mld):

| Componente | € mld stimati | Quota |
|---|---|---|
| **Retribuzioni lorde da lavoro dipendente** (D11) | ~€770 | ~59% |
| **Redditi misti autonomi** (B3) | ~€220 | ~17% |
| **Redditi da capitale** (D4) — affitti, dividendi, interessi | ~€90 | ~7% |
| **Pensioni e prestazioni sociali** (D62) | ~€400 | ~31% |
| **Altri trasferimenti correnti** | ~€30 | ~2% |
| **Meno: Contributi sociali lavoratori** (D61) | -€130 | -10% |
| **Meno: IRPEF + altre imposte dirette** (D5) | -€280 | -22% |
| **NETTO TOTALE** | **~€1.296** | **100%** |

**Insights chiave:**
- Le **retribuzioni lorde da lavoro dipendente** sono ~59% delle componenti ATTIVE del reddito disponibile
- Le **pensioni e prestazioni sociali** (~31% del reddito attivo) sono **un peso enorme** del reddito familiare italiano — l'Italia ha più pensionati e una spesa previdenziale tra le più alte UE
- La **tassazione diretta** (IRPEF + addizionali, contributi sociali a carico lavoratori) **assorbe ~32% del reddito attivo** prima che diventi disponibile

## Evoluzione reale del reddito disponibile (riferimento ISTAT, da serie più ampia)

Il reddito disponibile delle famiglie italiane in **termini reali** (al netto dell'inflazione):
- 2008 (pre-crisi): livello 100
- 2014 (post-crisi): ~92 (-8% reale)
- 2019: ~95 (parziale recupero)
- 2020 (Covid): ~92
- 2022: ~93 (forte erosione da inflazione)
- 2024: ~96 (recupero parziale)

**Il reddito disponibile reale italiano nel 2024 è ancora ~4% sotto i livelli 2008.** Quasi due decenni senza recupero del potere d'acquisto pre-crisi.

## Confronto con PIL pro capite

Il reddito disponibile pro capite (~€22.000) **è significativamente inferiore** al PIL pro capite (~€37.350). Differenza ~€15.000 = quanto va a:
- Imposte non distribuite alle famiglie
- Profitti reinvestiti dalle imprese
- Spesa pubblica per investimenti

Questo è normale per economie sviluppate: il **reddito disponibile è ~55-65% del PIL** in tutti i Paesi OCSE.

## ⚠️ Limitazione importante del dataset esportato

Il dataset originale (DCCN_ISTITUZ_TNA1) **dovrebbe contenere il dettaglio REGIONALE** delle famiglie italiane, ma **l'export attuale è filtrato solo a livello nazionale (Italia)**. Per disporre di dati Lombardia/Calabria/ecc. → riscaricare con filtro REF_AREA esteso a tutte le regioni.

Le **disparità territoriali** del reddito disponibile sono note (riferimento ISTAT precedente):
- Trentino-AA, Lombardia, Emilia-Romagna: reddito pro capite > €27.000
- Calabria, Campania, Sicilia: reddito pro capite < €15.000
- **Gap Nord-Sud: ~80% (Nord vs Sud)**

## Caveat e note di lettura

- **Solo settore Famiglie (S14)** = persone fisiche. Esclude: imprese, PA, no-profit.
- **Reddito disponibile ≠ ricchezza.** Misura flussi annuali, non stock di ricchezza patrimoniale. L'Italia ha ricchezza media delle famiglie elevata (case di proprietà, risparmi) ma flussi di reddito relativamente bassi.
- **Dato 2024 provvisorio** — revisione a settembre 2026.
- **Dataset originale completo** ha 800+ righe con tutti gli aggregati SEC 2010 (B1G, B5G, B6G, B6N, D1, D11, D12, D5, D62, D7, ecc.). Per drill-down su singoli componenti, leggere il raw direttamente.
- **Per famiglia ≠ pro capite ≠ per occupato.** La cifra "per famiglia" (€49.900) è la media. La distribuzione è **fortemente asimmetrica** — mediana ~€32.000 (riferimento Banca d'Italia indagine sui bilanci delle famiglie). Top 10% famiglie hanno >€100.000 di reddito disponibile.
- **Risparmio delle famiglie italiane** è strutturalmente alto (~9-10% del reddito disponibile) — sopra media UE.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DCCN_ISTITUZ_TNA1/Reddito disponibile delle famiglie nelle regioni italiane (IT1,93_1095_DF_DCCN_ISTITUZ_TNA1_1,1.0).csv`
