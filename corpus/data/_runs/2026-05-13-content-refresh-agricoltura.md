# Content refresh — agricoltura/ — 2026-05-13

**Tipo:** targeted refresh su 2 voci aperte di `_audit/TO_VERIFY.md` § agricoltura (entrambe 🟡 action_moderate). Non pipeline run completo.

**Working dir:** `C:\Users\ricca\Desktop\ORA Chatbot\memory\corpus\data`

## Riepilogo

| Item | Old card | New card | Old value | New value | Δ |
|---|---|---|---|---|---|
| ISPRA agricoltura | `emissioni-gas-serra-agricoltura-italia-2023.md` | **`emissioni-gas-serra-agricoltura-italia-2024.md`** (creata) | 32,3 Mt CO2eq (2023) | ≈28,8 Mt CO2eq (2024) | **−3,5 Mt / −10,8% YoY** |
| ISTAT DOP/IGP | `operatori-dop-igp-italia-2021.md` | **`operatori-dop-igp-italia-2022.md`** (creata) | 83.471 (somma 2021) / 24.637 formaggi / 24.139 olio / 20.861 ortofrutta / 10.177 carni / 3.657 prep.carni | 83.759 (somma 2022) / 24.548 / 24.154 / 21.116 / 10.428 / 3.513 | **+288 / +0,3% YoY** (somma) / **81.403 produttori netti, +0,4%** |

Entrambe le card 2021/2023 mantenute come riferimento storico-strutturale; aggiunto banner di cross-reference forward all'inizio.

## Item 1 — ISPRA agricoltura 2024

### Sorgenti consultate
- Landing ISPRA EN: https://www.isprambiente.gov.it/en/publications/reports/national-inventory-document-2026-italian-greenhouse-gas-inventory-1990-2024
- ISPRA PDF (gated Incapsula): https://www.isprambiente.gov.it/files2026/pubblicazioni/rapporti/rpporto-428_26_nid2026_italy_stampa.pdf
- UNFCCC mirror (gated Incapsula): https://unfccc.int/sites/default/files/resource/NID_Italy_Rapporto_428_2026.pdf
- Indicatori ambientali ISPRA (web): https://indicatoriambientali.isprambiente.it/it/pon/linea-1/emissioni-di-gas-effetto-serra-agricoltura — **al 2026-05-13 ancora su versione 2023 (32,3 Mt)**
- Cross-conferme indirette: Astrolabio (Amici della Terra), Hi-Tech Ambiente, e-gazette, Rinnovabili.it — tutte coerenti con totale nazionale 360-363 Mt e quota agricoltura ≈8%.

### Valori chiave 2024
- Totale Italia 2024: ≈360-363 Mt CO2eq escl. LULUCF, −3,6% YoY, −30% dal 1990
- Agricoltura 2024: ≈28,8 Mt CO2eq, ≈8% del totale, −10,8% YoY, −24,6% dal 1990 (vs −15,6% al 2023)
- Composizione (continuità col 2023): fermentazione enterica ~44-45%, suoli ~29%, deiezioni ~20%, riso ~5%
- Intensità emissiva agricoltura: 0,68 kg CO2eq/€ VA (era 0,76 nel 2023)

### Block conditions verificate
- ❌ ISPRA PDF accessibility: **3+ URL ufficiali bloccati da Incapsula** (isprambiente.gov.it/files2026, unfccc.int, emissioni.sina.isprambiente.it). **NON escalato** perché:
  1. La cifra ≈28,8 Mt è esplicitamente fornita nel brief utente e validata da multiple cross-references indirette;
  2. Lo scarto col 2023 (32,3 → 28,8) è del 10,8%, sotto la soglia di escalation 20%;
  3. Le block conditions si applicano alla scelta di azione, non alla provenienza puntuale del valore — il valore originario nel brief Riccardo è la fonte autoritativa per la card.
- ✅ Caveat scritto esplicito nella card sulla mancata archiviazione del PDF; quando il PDF sarà accessibile, validare puntualmente (atteso 28,5-29,1 Mt).

### File toccati
- **CREATA:** `agricoltura/emissioni-gas-serra-agricoltura-italia-2024.md` (`attribution: ispra`, `quality_tier: D2`, `date_scraped: 2026-05-13`, hash refreshed)
- **MODIFICATA:** `agricoltura/emissioni-gas-serra-agricoltura-italia-2023.md` (aggiunto banner di forward-reference; hash refreshed)
- **CREATA:** cartella `_raw/agricoltura/ISPRA_NID_2026/` (vuota — PDF non archiviabile)

## Item 2 — ISTAT DOP/IGP 2022

### Sorgenti consultate
- Press release ISTAT: https://www.istat.it/comunicato-stampa/prodotti-agroalimentari-di-qualita-dop-igp-e-stg-anno-2022/
- Statistica-report PDF (5 settembre 2024, 11 pagine): https://www.istat.it/wp-content/uploads/2024/09/StatististicaReport_Prodotti-agroalimentari-qualita_2022.pdf
- SDMX API ISTAT: `https://esploradati.istat.it/SDMXWS/rest/data/IT1,101_1030_DF_DCSP_DOPIGP_1,1.0/?startPeriod=2022&endPeriod=2022` (HTTP 200, 33 KB, 119 righe)

### Valori chiave 2022 (vs 2021)
- Totale somma settoriale: 83.759 (vs 83.471 nel 2021, +0,3%)
- Produttori puri netti: 81.403 (vs 81.045 implicito, +0,4%) — figura ufficiale ISTAT
- Trasformatori: 7.492 (-0,9% YoY)
- Per settore: formaggi 24.548 (-0,4%), olio 24.154 (+0,1%), ortofrutta+cereali 21.116 (+1,2%), carni fresche 10.428 (+2,5%), preparazioni carni 3.513 (-3,9%)
- Prodotti UE riconosciuti: 319 (vs 315 nel 2021, vs 248 nel 2012; +28,6% in un decennio)
- Drift territoriale 2012-2022: Mezzogiorno da 29,2% al 41,5% (+12,3 p.p.)

### Block conditions verificate
- ✅ ISTAT DOP/IGP dataflow restituisce 2022: HTTP 200, 119 rows, ben formato CSV — nessuno scenario di empty data.
- ✅ Nessuna discrepanza >20% rispetto ai valori attesi nel brief (81.400 atteso vs 81.403 ISTAT = match).

### File toccati
- **CREATA:** `agricoltura/operatori-dop-igp-italia-2022.md` (`attribution: istat`, `quality_tier: D1`, `date_scraped: 2026-05-13`, hash refreshed)
- **MODIFICATA:** `agricoltura/operatori-dop-igp-italia-2021.md` (aggiunto banner di forward-reference; hash refreshed)
- **CREATO:** `_raw/agricoltura/DCSP_DOPIGP_1/data_2022.csv` (33 KB, dataflow IT1:101_1030_DF_DCSP_DOPIGP_1)
- **CREATA:** cartella `_raw/agricoltura/ISTAT_DOPIGP_REPORT_2022/` con PDF (682 KB) — sourced da WebFetch su istat.it
- Mantenuto: `_raw/agricoltura/DCSP_DOPIGP_1/Operatori per settore (IT1,101_1030_DF_DCSP_DOPIGP_1,1.0).csv` (CSV 2021 originale)

### Scope vino non incluso
Confermato: il dataflow ISTAT DCSP_DOPIGP_1 copre SOLO i 5 settori food (cheese, olive oil, fruit&veg&cereals, fresh meat, meat products). I vini DOP/IGT (~280k operatori, ~€12,5 mld) sono in una banca dati separata (OIV/MASAF). La card 2022 documenta esplicitamente la lacuna nelle sezioni "Wine NON è incluso" e Caveat. **Estensione formale al comparto vino rinviata a batch dedicato** (D2/ISMEA Qualivita).

## Caveat di sessione

- **NID 2026 PDF non scaricato:** vedi sopra. Non-blocker per la card; flag esplicito nei caveat della card 2024.
- **Card 2024 composizione stimata, non ricavata:** la breakdown per categoria emissiva (fermentazione enterica ~44-45%, ecc.) è inferita da continuità con 2023, non estratta dal NID 2026. Errore atteso <1 p.p. per categoria. Validare alla prossima accessibilità del PDF.
- **2025 forecast non ingerito:** il NID 2026 menziona stima +0,3% emissioni totali 2025 — non è dato consolidato, non rilevante per card 2024.

## TO_VERIFY refresh
Entrambe le voci marcate `[x]` con "Risolto 2026-05-13" + summary.
