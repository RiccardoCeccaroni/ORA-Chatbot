---
id: personale-straniero-sanitario-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Personale sanitario di formazione estera, Italia, 2024"
data_metric: "% di infermieri e medici formati all'estero sul totale della professione (foreign-trained share)"
data_period: "2024 (provvisorio); serie 2020-2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Health workforce migration, dataflow DSD_HEALTH_WFMI@DF_HEALTH_WFMI"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 288b50e7003c549ba4b6aefcf92bddfc915ae58de48143a6b43b3ed7149b98cd
tags: [salute-servizi-sanitari, immigrazione, lavoro-politiche-sociali]
description: "Personale sanitario di formazione estera in Italia (2024): 5,02% degli infermieri e 1,15% dei medici — quote modeste vs UK (>25%), ma in crescita."
---

# Personale sanitario di formazione estera, Italia, 2024

**Valori (2024, provvisori):**
- **Infermieri di formazione estera: 5,02%** del totale infermieri praticanti
- **Medici di formazione estera: 1,15%** del totale medici praticanti

L'Italia ha **quote modeste** di personale formato all'estero rispetto ai grandi Paesi anglosassoni (UK, Canada, Australia) che superano il 25-30%.

## Serie storica

### Infermieri stranieri (MINU)

| Anno | % |
|---|---|
| 2020 | 4,98% |
| 2021 | 5,21% |
| 2022 | 5,22% |
| 2023 | 5,22% |
| 2024 | 5,02% |

Quota **sostanzialmente stabile** intorno al 5%. Il lieve calo 2024 può riflettere normative restrittive sui riconoscimenti dei titoli o ritorni nei Paesi di origine post-Covid.

### Medici stranieri (PHYS)

| Anno | % |
|---|---|
| 2020 | 0,90% |
| 2021 | 0,94% |
| 2022 | 0,97% |
| 2023 | 1,03% |
| 2024 | **1,15%** |

**Crescita del +28% in 4 anni**. I medici stranieri sono **ancora marginali in valore assoluto** (~3.600 su 315.000 totali) ma il **trend è chiaramente in salita** — riflesso della crisi di reclutamento interno (vedi card `medici-italia-2023.md`, MMG in deficit).

## Cosa misura — "Foreign-trained"

L'indicatore è **lo stock di lavoratori con titolo di studio professionale conseguito all'estero**, espresso come **% del totale dei lavoratori praticanti della stessa professione** in Italia.

**Origine geografica** = "World" (W) — l'indicatore aggrega tutte le origini estere senza distinguere UE/extra-UE.

Include:
- italiani nati all'estero che si sono laureati all'estero
- stranieri laureati nel Paese di origine e migrati in Italia
- stranieri laureati in altri Paesi UE/extra-UE

Esclude:
- stranieri laureati IN Italia (sono italiani per titolo di studio)
- italiani laureati in Italia ma con genitori stranieri

## Confronto internazionale (orientativo, da verificare con web search)

L'Italia ha quote MOLTO modeste rispetto ai pari OCSE che reclutano sistematicamente all'estero:

| Paese | Medici stranieri | Infermieri stranieri |
|---|---|---|
| **Italia 2024** | **1,15%** | **5,02%** |
| Germania | ~13% | ~10% |
| Francia | ~12% | ~3% |
| Spagna | ~10% | ~3% |
| UK | ~30%+ | ~21% |
| Svizzera | ~37% | ~28% |
| Norvegia | ~13% | ~9% |

**L'Italia è strutturalmente un Paese che NON reclutta medici e infermieri stranieri** (a differenza di UK e CHE che vi fanno affidamento per sostenere il SSN). Questo dato:

- Riflette barriere all'ingresso (riconoscimento titoli ammette EU-only fast track, Paesi terzi molto lenti)
- Rispecchia stipendi italiani non competitivi per attirare personale dell'UE (medici tedeschi/francesi guadagnano significativamente di più)
- Significa che il SSN dipende **quasi al 100% dalla formazione interna**, e ogni crisi del numero chiuso in medicina/Scienze infermieristiche si ribalta direttamente sui carichi di lavoro

## Carenza vs immigrazione di personale

Il dibattito italiano sulla "fuga dei medici" all'estero è **asimmetrico** rispetto a questi dati:

- **Italiani che lasciano l'Italia per esercitare all'estero:** quote significative (Germania, UK, Svizzera, Emirati). Stima ~10.000-15.000 medici italiani all'estero (FNOMCeO).
- **Stranieri che entrano in Italia:** ~3.600 medici (1,15%) + ~21.000 infermieri (5,02%).

**Il saldo migratorio del personale sanitario italiano è probabilmente negativo** (più uscite che ingressi). Per quantificarlo servirebbe il flusso (non lo stock) che NON è in questo dataset.

## Caveat e note di lettura

- **% sullo stock totale, NON flusso annuale.** Il 5,02% di infermieri stranieri = persone che lavorano in Italia E hanno formazione estera, indipendentemente da quando sono arrivati.
- **"Stranieri" = formati all'estero**, NON nazionalità. Un italiano formato all'estero rientra in questo conteggio.
- **Dati 2024 provvisori** (status "P" nel CSV) — possibili revisioni.
- **Settore RSA/badanti completamente escluso** — la componente "personale di cura informale stranier@" (badanti) è grandissima in Italia ma fuori dall'indicatore (sono lavoratori non-clinici, settore Q87 piuttosto che Q86).
- **Composizione per origine non rivelata:** sappiamo solo "estero" aggregato. Per Romania, Albania, India, Filippine — origini tipiche degli infermieri stranieri in Italia — serve dataset diverso (Eurostat per migrazione professionale).

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_HEALTH_WFMI/OECD.ELS.HD,DSD_HEALTH_WFMI@DF_HEALTH_WFMI,1.0+.A..PT_WR_PRF_HLTH....csv`
