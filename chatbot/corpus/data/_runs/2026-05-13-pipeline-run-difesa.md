---
folder: difesa
pipeline_run_date: 2026-05-13
mode: pilot (autonomous-flow design validation)
wishlist_voci: 6
shortlist_candidates: 8 (5 ISTAT + 3 OECD)
downloads: 8 (all HTTP 200; 2 returned XML instead of CSV — parsed via fallback)
cards_written: 4
voci_status:
  voce_1_spesa_militare_totale: covered (cross-country + Italia)
  voce_2_composizione_per_categoria: covered (in voce 1 OECD TABLE11 via TRANSACTION dim, complementary ISTAT angle in card 2)
  voce_3_r_s_militare: covered (OECD GBARD + ISTAT confirms)
  voce_4_cofog02_italia: covered (collapsed into voce 1 — same datasets)
  voce_5_industria_difesa: partial (ATECO 25.40 OK, 30.40 confidentiality-suppressed except numero imprese)
  voce_6_personale_ffaa: excluded (zero D1 hits, Riccardo's decision)
---

# Pipeline run — `difesa` — 2026-05-13

## Esito sintetico

4 stat-card scritte in `memory/corpus/data/difesa/`:

1. `spesa-difesa-italia-vs-paesi-2022.md` — €24,9 mld Italia 2022, contesto cross-country 10 paesi OCSE.
2. `composizione-spesa-difesa-italia-2024.md` — breakdown G0201-G0205 con R&D difesa a 0,4% del totale.
3. `r-s-difesa-italia-vs-paesi-2024.md` — Italia $132M vs Germania $4.856M (37×), Francia $2.162M (16×), US $97.121M (737×).
4. `industria-armi-munizioni-italia-2023.md` — ATECO 25.40 (113 imprese, €2,2 mld fatturato) + 30.40 monopolio (1 sola impresa).

## Dataset scartati (rejected — with reasons)

- **`OECD.SDD.NAD:DSD_NASEC10@DF_TABLE12_EXP`** (4,2 MB scaricato in `_raw/difesa/DF_TABLE12_EXP/`): per la composizione di spesa difesa per categoria economica (voce 2). **Scartato** perché TABLE11 ha già la cross-tab COFOG02 × TRANSACTION (i 460 record Italia GF02 includono D1 compensation, P2 intermediate, P5 capital, ecc.) — TABLE12_EXP è la stessa info su tutto il gov senza filtro COFOG, quindi ridondante. Raw conservato per audit.
- **`ISTAT:95_94_DF_DCCN_OTEPPA_2`** (76 MB in `_raw/difesa/DCCN_OTEPPA_2/`): "Voci di uscita per funzione COFOG". **Scartato** per ridondanza: OTEPPA_1 + TABLE11 coprono già la composizione difesa. Conservato per future estensioni di card 2.
- **`ISTAT:161_267_DF_DCSP_SBSNAZ_14`** (344 KB XML in `_raw/difesa/DCSP_SBSNAZ_14/`): "Numero di addetti e dipendenti" per ATECO. **Scartato** perché zero osservazioni per ATECO 2540 e 3040 (probabile confidenzialità SBS). Raw conservato; menzionato nel "Sorgente raw" della card 4.
- **`ISTAT:6_20_DF_DCSP_RS_2`** (38 KB XML in `_raw/difesa/DCSP_RS_2/`): GBARD Italia. **Non scartato ma collassato** in card 3 (OECD GBARD) — ISTAT mostra €78,07M nel 2024 e OECD mostra €79,10M, sono la stessa serie, OECD raccoglie da ISTAT. Citato come cross-check nella card 3.

## Caveat e follow-up

- **Voce 6 (personale FFAA) confermata fuori D1 v1.** Nessuna fonte ISTAT/OECD copre effettivi militari. Eventuale ingestione futura via D2 (NATO Defence Expenditure Report, RGS Conto Annuale, IISS Military Balance) — non oggetto di questa pipeline.
- **% PIL non ricavato.** OECD TABLE11 nella versione default espone solo XDC (valuta nazionale) — i confronti in % GDP usati nella narrativa NATO (target 2%, 5%) non sono in queste card. **Da fetchare in iterazione futura** con misura `XDC_R_B1GQ` o variante percentuale.
- **OECD ↔ NATO mismatch metodologico** evidenziato esplicitamente nelle card 1 e 2: la definizione COFOG 02 non coincide con la definizione NATO. Il chatbot deve disambiguare quando un utente cita "il 2% del PIL".
- **ATECO 30.40 confidenzialità.** Solo `numero imprese = 1` pubblicato; tutto il resto soppresso. Per ottenere fatturato/addetti del singolo produttore servono bilanci civilistici (D3, fuori scope).
- **Industria aerospaziale-difesa NON coperta.** ATECO 30.30 (aerospazio), 30.11 (cantieristica militare), 26.51/26.30 (elettronica difesa) non sono in questa pipeline. Candidate per una scheda futura "industria-aerospaziale-difesa-italia".

## Note tecniche emerse durante il run (di interesse per i parallel runs futuri)

1. **ISTAT richiede Accept header**, non `?format=csvfilewithlabels`. Senza header il server restituisce 200 OK con solo l'header del CSV (nessuna riga dati). Header da usare: `application/vnd.sdmx.data+csv;version=1.0.0;labels=both`.
2. **Quirk ISTAT residuo**: per alcuni dataflow specifici (`DCSP_SBSNAZ_14`, `DCSP_RS_2`) il server restituisce SDMX-ML (XML) invece di CSV anche con il giusto Accept header. Non è un bug riproducibile in modo affidabile — meglio fallback al parser XML (`xml.etree.ElementTree`) che tentare retry.
3. **OECD senza key filter su TABLE11 = 264 MB** (timeout dopo qualche minuto). Filtrare sempre per REF_AREA + dimensioni rilevanti (es. `GF02` per COFOG difesa).
4. **OECD agency codes validati**: `OECD.SDD.NAD`, `OECD.STI.STP`, `OECD.GOV.GIP`. Quelli che danno 404: `OECD.GOV`, `OECD.GOV.PAR`, `OECD.STI`, `OECD.STI.SAS`, `OECD.ELS.SAE`.
5. **Catalog browse via WebFetch è inaffidabile per ISTAT** (la summarizer truncate a ~300/1500 dataflow). Scaricare l'XML del catalogo localmente e grepparlo direttamente.

Queste sono già riflesse nel prompt riutilizzabile `memory/scripts/autonomous_data_pipeline_prompt.md`.
