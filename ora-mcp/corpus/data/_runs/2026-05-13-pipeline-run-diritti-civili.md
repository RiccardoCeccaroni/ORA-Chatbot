---
folder: diritti-civili
pipeline_run_date: 2026-05-13
mode: autonomous
wishlist_voci: 5
shortlist_candidates: 4 ISTAT dataflows + 1 PDF report (5 raw artifacts)
downloads: 5 (all HTTP 200)
cards_written: 2
voci_status:
  voce_1_unioni_civili: covered
  voce_2_consumo_droghe_illecite: gap — fonte attesa AVQ_209 si è rivelata "consumo di farmaci" (medicines), non droghe illecite — ISTAT non rileva direttamente uso di stupefacenti
  voce_3_sex_work_eno: covered (via PDF report ISTAT, non via SDMX)
  voce_4_strutture_cure_palliative: gap — STRSANDISTR_1 si ferma al 2013 e non espone hospice come tipologia separata
  voce_5_opinioni_pubbliche_diritti_civili: gap (atteso) — zero D1 hits, deferred a D2 (Eurobarometer / Eurispes)
---

# Pipeline run — `diritti-civili` — 2026-05-13

## Esito sintetico

**2 stat-card** scritte in `memory/corpus/data/diritti-civili/`:

1. **`unioni-civili-italia-2024.md`** — 2.936 unioni civili 2024 (1.608 M-M, 1.328 F-F; rate 5,0/100k); serie 2018-2024 con dip Covid e recupero post-2022. ~17.500 unioni cumulate 2018-2024 = 1,9% dei matrimoni annui.
2. **`economia-non-osservata-prostituzione-italia-2022.md`** — €4,0 mld VA + €4,7 mld consumi 2022 (Report ISTAT 18 ott 2024). **Verifica esatta del claim numerico citato dalla tesi 05** §Sex Work. Composizione attività illegali totali: droga 76%, prostituzione 20%, contrabbando 4%.

## Dataset scartati (rejected — con motivazione)

- **`ISTAT : 83_63_DF_DCCV_AVQ_PERSONE_209`** ("Use of drugs / Consumo di farmaci", 248 KB in `_raw/diritti-civili/DCCV_AVQ_PERSONE_209/`): **scartato per equivoco di traduzione**. Il titolo inglese "Use of drugs" suggerisce uso di stupefacenti, ma il titolo italiano corretto è **"Consumo di farmaci"** = uso di medicinali (pharmaceuticals), confermato dai valori (88% per uomini over 75 — impossibile per droghe illecite, coerente per farmaci con prescrizione). Indicatore unico: `0_DRUGS_D` = "persons who consumed drugs for the last two days" → in realtà "persone che hanno consumato farmaci negli ultimi 2 giorni". **Non risponde alla voce 2 della wishlist** (consumo cannabis / sostanze stupefacenti). Raw conservato per audit / future card "consumo farmaci" eventuale in `salute-servizi-sanitari`.
  
  **Nota tecnica per future run**: l'**etichetta inglese "drugs" nei dataflow ISTAT** va sempre verificata contro l'italiano. ISTAT spesso traduce "farmaci" → "drugs" creando ambiguità. La regola pratica: se la prevalenza è >>5% per popolazione generale, non sono stupefacenti.

- **`ISTAT : 43_237_DF_DCIS_STRSANDISTR_1`** ("Tipologia strutture sanitarie distrettuali", 153 KB in `_raw/diritti-civili/DCIS_STRSANDISTR_1/`): **scartato per duplice motivo**:
  1. **Serie storica stale**: solo 2010-2013 (4 anni), nessun aggiornamento da oltre 10 anni — viola la regola "≥2020" della pipeline.
  2. **Nessuna disaggregazione hospice**: la dimensione `FACILITY_TYPE` ha 4 valori (ambulatorio, altro ambulatoriale, semi-residenziale, residenziale) — gli hospice sono aggregati nella generica "residential health care" senza split. Non risponde alla voce 4 (capacità rete cure palliative).
  
  Raw conservato per audit. **La voce 4 (copertura cure palliative) resta gap D1**: per il dato hospice + posti letto cure palliative serve attingere al **Ministero della Salute / Annuario Statistico SSN** (tier D2 italiano) o **OECD Health Statistics Resources** (tier D1 ma in agency code OECD.ELS.HD non ancora validato per il pilota). Deferred a iterazione futura.

## Voci wishlist con gap D1 confermato (per backlog futuro)

| Voce wishlist | Tipo gap | Fonte D2/D3 alternativa | Routing |
|---|---|---|---|
| **2** Consumo droghe illecite Italia | D1 non rileva uso autoriportato di stupefacenti illegali | EMCDDA/EUDA European Drug Report (D2 UE); CNR-IFC IPSAD (D3 italiana citata anche da ISTAT come fonte per la stima ENO droga) | Deferred a D2 batch droghe |
| **4** Rete hospice / cure palliative | ISTAT STRSANDISTR_1 stale (2013) + nessuna granularità hospice | Min. Salute Annuario SSN (D2 IT); Annuario Statistico SSN — Tavole strutture residenziali; possibilmente OECD.ELS.HD se dataflow esposto | Deferred a iterazione cure palliative |
| **5** Opinioni pubbliche su diritti civili | Zero hits ISTAT/OECD | Eurobarometro Discrimination Survey (D2 UE); Eurispes Rapporto Italia annuale (D4 bias-tagged) | Deferred a D2 batch sondaggi |
| Persone trans — rettifiche anagrafiche / terapie ormonali | Nessuna fonte D1; dati sparpagliati tra tribunali e ASL regionali | Min. Giustizia (statistiche civili); regioni / SSN per terapie | Deferred (probabile D2 IT + D4 ricerche) |

## Note tecniche emerse durante il run

1. **AVQ-PERSONE traduzioni inglesi inaffidabili** — il caso "drugs / farmaci" è un classico falso amico. Per dataset ISTAT futuri della famiglia AVQ verificare sempre il titolo italiano contro l'inglese del catalogo prima di scaricare.

2. **STRSANDISTR_1 è stale dal 2013** — sospetto che ISTAT abbia *dismesso* l'aggiornamento di questo dataflow specifico e migrato i dati a una struttura diversa (forse `124_722_DF_DCAR_CONTECON_ASLAO_1` che è più orientato a economia ASL). Per future run su strutture sanitarie, evitare 43_237 e cercare prima `124_722` o equivalenti.

3. **Report PDF ISTAT — alternative SDMX-less**: per il dato voce 3 (sex work) il claim della tesi non era ricavabile da SDMX. Buon test della *carve-out PDF*: gli ENO report ISTAT sono pubblicati annualmente, hanno URL stabile, tabelle estraibili. Per dati "report-only" come questo, registrare nel "Sorgente raw" sia il PDF locale sia l'URL upstream — il chatbot deve sapere che il dato non è in API ma è verificabile contro PDF citato.

4. **OECD code agency probing** — per `diritti-civili` non sono stati interrogati agency code OECD esterni a NAD/STP/GIP (cache esistente). I temi della tesi 05 (civil rights, drug policy, end-of-life, sex work) sono coperti più da agenzie tipo **OECD.ELS** (Employment, Labour, Social) o **WHO** (cure palliative) che da gov-finance. **TODO non bloccante per iterazioni future**: probare `OECD.ELS.HD` (Health Division) per palliative care; probare `OECD.ELS.SAE` (Social Affairs) per LGBTQ family policy. Entrambi appaiono nella lista 404-prone del prompt — necessario test puntuale, non standing.

5. **Voce 1 ben coperta, ridondanza UNIONICIT_1 + UNIONIND_1 utile** — i due dataflow si complementano (assoluti vs tassi normalizzati) e sono stati collassati in una sola card senza perdita. Il dataflow "Indicatori" (UNIONIND_1) è essenziale per il rate per 100k che dà il senso della scala.

## Sample headline numbers (per cross-check rapido)

| Card | Numero chiave | Anno | Note |
|---|---|---|---|
| `unioni-civili-italia-2024.md` | 2.936 unioni civili (5,0 per 100k) | 2024 | Record post-Covid, dip 2020 |
| `unioni-civili-italia-2024.md` | 17.500 unioni cumulate | 2018-2024 | 1,9% dei matrimoni annui |
| `economia-non-osservata-prostituzione-italia-2022.md` | €4,0 mld VA + €4,7 mld consumi prostituzione | 2022 | Verifica esatta claim tesi 05 §Sex Work |
| `economia-non-osservata-prostituzione-italia-2022.md` | €19,8 mld VA attività illegali totali (1,1% PIL) | 2022 | Droga 76% + prostituzione 20% + sigarette 4% |

## Per Riccardo — flag

- **La tesi 05 è "data-povera" per costruzione** (giuridica/valoriale): solo 1 numero esplicito (i €4 mld sex work), che la pipeline ha confermato. Le card 1 e 2 forniscono il *contesto numerico* per *State / Project / Justify* sulle altre 4 sub-aree (matrimonio egualitario, persone trans, cure palliative, cannabis) senza claim della tesi da verificare puntualmente.
- **Gap D1 strutturali**: cure palliative + opinioni + persone trans + uso stupefacenti — tutti destinati a un futuro batch D2/D3. Non è una sconfitta della pipeline, è la natura della tesi 05.
- **Nessuna delle 4 condizioni di blocco** è scattata. La pipeline è completa.
