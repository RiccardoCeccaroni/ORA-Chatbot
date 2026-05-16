---
id: inflows-foreign-population-italia-2012-2023
type: data
attribution: oecd
quality_tier: D1
title: "Inflows of foreign population — serie storica Italia, 2012-2023"
data_metric: "afflussi annui di popolazione straniera in Italia (definizione armonizzata OECD)"
data_period: "2012-2023 (annuale)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — International Migration Database, dataflow DSD_MIG@DF_MIG (MEASURE=B11, Inflows of foreign population)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 829f8bcd88f3737bb922197fd74cb2a82d62649cb7a211b1ed9b99ea0f0ec0ec
tags: [immigrazione]
description: "Afflussi annui di popolazione straniera in Italia 2012-2023 (OECD, definizione armonizzata): 378.372 nel 2023 (picco), 191.766 nel 2020 (minimo Covid), con forte rimbalzo post-pandemico (+97% dal 2020 al 2023)."
---

# Inflows of foreign population — serie storica Italia, 2012-2023

**Afflussi di popolazione straniera in Italia (OECD MEASURE=B11):**

| Anno | Afflussi stranieri | Variazione vs anno precedente |
|---|---|---|
| 2012 | 321.305 | — |
| 2013 | 279.021 | −13,2% |
| 2014 | 248.360 | −11,0% |
| 2015 | 250.026 | +0,7% |
| 2016 | 262.929 | +5,2% |
| 2017 | 301.071 | +14,5% |
| 2018 | 285.500 | −5,2% |
| 2019 | 264.571 | −7,3% |
| **2020** | **191.766** | **−27,5%** (shock Covid) |
| 2021 | 243.607 | +27,0% |
| 2022 | 336.495 | +38,1% |
| **2023** | **378.372** | **+12,4% (picco serie)** |

## Lettura politica

### Tre fasi nella migrazione verso l'Italia (2012-2023)
1. **2012-2014 — Riassorbimento post-crisi**: i flussi calano da 321k a 248k (mercato del lavoro contratto post-2011, debole attrazione economica).
2. **2015-2019 — Stabilità intorno ai 260-300k/anno**: l'Italia si normalizza come destinazione "media" UE (sotto Germania, Francia, Spagna).
3. **2020 — Shock Covid (-27%)**: 191k, minimo storico decennale.
4. **2021-2023 — Forte rimbalzo**: da 191k (2020) a 378k (2023), **quasi raddoppio** in tre anni. Picco di serie 2023.

### Cosa spiega il picco 2022-2023
- **Effetto Ucraina**: ~170k cittadini ucraini accolti in Italia (gennaio 2022-gennaio 2023, dati Ministero Interno) — ma solo parte iscritta in anagrafe e quindi catturata da B11.
- **Recupero post-Covid del ricongiungimento familiare** (canali ordinari riaperti, ambasciate operative).
- **Domanda di lavoro** in agricoltura, logistica, sanità (decreti flussi 2022-2023 ampliati).

### Confronto con la card ISTAT
- OECD 2023 (B11 armonizzato): **378.372**
- ISTAT 2023 (iscrizioni anagrafiche stranieri, dataflow 28_185): ~340.000 (stima sulla base di proporzioni 2024)
- ISTAT 2025 (provv.): **383.465 stranieri** (= 440k totali − 56k italiani di ritorno) → coerente con la crescita 2022→2025.

**OECD e ISTAT non sono identici** ma raccontano la stessa storia: post-Covid l'Italia è tornata ad attrarre stranieri in modo sostenuto, con un picco superiore a tutti gli anni 2010.

### Per la posizione ORA
Il dato sfida due narrative opposte:
- L'idea che "in Italia non viene nessuno": il 2023 è il picco assoluto della serie OECD, con 378k afflussi.
- L'idea di una "invasione recente improvvisa": gli stranieri arrivano in Italia a ritmi simili da 15 anni (eccetto crisi e shock). Il 2023 supera il 2012 solo del 18%.

## Metodologia

Fonte: **OECD International Migration Database**, dataflow `DSD_MIG@DF_MIG`.
Misura: **B11 — Inflows of foreign population** (afflussi annui di popolazione straniera, definizione OCSE armonizzata).
Universo: popolazione straniera (definita per cittadinanza non-IT, BIRTH_PLACE = _T, CITIZENSHIP = W per "world").
Unità: persone.

La definizione **OECD-armonizzata** è più ampia delle iscrizioni anagrafiche ISTAT: include persone con permessi di soggiorno di lunga durata anche se non immediatamente registrate. Garantisce confronto internazionale.

## Caveat e note di lettura

- **Serie ferma al 2023** in questo export (OECD aggiornamenti annuali con ~12-18 mesi di lag).
- I dati OCSE possono **differire dai dati ISTAT** per definizioni armonizzate, conversioni metodologiche, revisioni retrospettive. Le card ISTAT (`immigrati-italia-2025.md`) e OECD si **leggono insieme**: ISTAT per il dato italiano nativo + dettaglio per cittadinanza/origine, OECD per il confronto internazionale e la serie storica armonizzata.
- "Inflows of foreign population" **non distingue per canale d'ingresso** (lavoro, famiglia, asilo, ecc.) — vedi card `inflows-permanenti-categoria-italia-2024.md`.
- I numeri **non includono italiani di ritorno** (per definizione: solo cittadini stranieri).
- Confronto temporale: dato 2012 e 2023 sono comparabili nella definizione OECD ma possono riflettere lievi revisioni metodologiche.

## Sorgente raw

- `_raw/immigrazione/DF_MIG/OECD.ELS.IMD,DSD_MIG@DF_MIG,1.0+.W.A.B11._T....csv`
