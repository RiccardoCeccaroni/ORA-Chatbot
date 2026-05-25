---
folder: pari-opportunita-inclusione
pipeline_run_date: 2026-05-13
mode: autonomous (resumed after prior token-limit interruption)
wishlist_voci: 6
shortlist_candidates: 7 (4 ISTAT + 3 OECD; 1 explicit gap on voce 4 disabilità)
downloads: 7 attempted; 6 OK; 1 failed (OECD DF_LFS rate-limit / NoResults — non-blocking)
cards_written: 2
voci_status:
  voce_1_occupazione_femminile: covered (in card 1 — TAXOCCU1 nazionale + macroregionale 2015-2025)
  voce_2_gender_wage_gap: covered (in card 1 — OECD GENDER_WAGE_GAP cross-country 2010-2024)
  voce_3_part_time_involontario: partial (in card 1 — PT incidence Italia 2015-2024; il segmento "involontario" specifico richiede Eurostat lfsa_eppgai, fuori D1-SDMX-OECD batch)
  voce_4_occupazione_disabili: deferred (zero hits in ISTAT SDMX catalog, gap noto a shortlist)
  voce_5_ivg: covered (card 2 — IVG_5 standardized rate nazionale + 20 regioni + 5 macroaree, 2010-2024)
  voce_6_asimmetria_lavoro_cura: rejected (ASIMMETRIA_1 ultimo anno disponibile 2013, fallisce filtro recency ≥2020)
---

# Pipeline run — `pari-opportunita-inclusione` — 2026-05-13

## Esito sintetico

2 stat-card scritte in `memory/corpus/data/pari-opportunita-inclusione/`:

1. **`gender-gap-lavoro-italia-2024.md`** — *fusion card* su tre fronti del gap di genere nel lavoro:
   - Tasso di occupazione 15-64 per sesso e macroregione (ISTAT TAXOCCU1, 2015-2025).
   - Gender wage gap mediano cross-country (OCSE GENDER_WAGE_GAP, 9 paesi + media OCSE, 2024).
   - Incidenza part-time per sesso (OCSE FTPT_INC_GEN, Italia 2015-2024).
   - **Headline numbers:** F 53,3% vs M 71,1% (gap 17,8 pp); Mezzogiorno F 37,2% (gap 26 pp con Nord-Est); GWG mediano IT 5,1% vs OCSE 10,3%; PT donne 76,5%.
   - Risolve il **paradosso del GWG basso italiano** spiegandolo con effetto di selezione delle occupate.

2. **`ivg-rate-italia-2024.md`** — Tasso di abortività e variabilità regionale (ISTAT IVG_CARATTDON_5, 2010-2024).
   - **Headline numbers:** 5,85 IVG per 1.000 donne 15-49 nel 2024; -25% dal 2010; rapporto Liguria/Abruzzo 1,85×.
   - **Gap noto e segnalato:** % obiettori di coscienza per regione sta nella Relazione 194 del Ministero della Salute, **non in SDMX** → il chatbot rinvia a Tier-3.

## Fusion executive

La direttiva del prompt era "fondere aggressivamente". Risultato:

- 3 dataset (TAXOCCU1 + GENDER_WAGE_GAP + FTPT_INC_GEN) → **1 card "gender gap lavoro"** invece di 3 schede separate. Motivo: il lettore della tesi 15 deve ricevere il pacchetto narrativo unitario (partecipazione + retribuzione + part-time) — separarli avrebbe perso la chiave di lettura del "paradosso del GWG basso".
- 2 dataset IVG (IVG_5 standardized rate + IVG_1 absolute counts) → **1 card "IVG"**, perché IVG_1 non ha aggregati totali utilizzabili come headline (vedi caveat); il dato del volume IVG si ricava dalla Relazione 194 in Tier-3.
- ASIMMETRIA_1 scartata e citata come caveat dentro la card 1.

Risultato finale: **2 schede dense** invece di 5-6 schede frammentate. In linea con "5 voci → 4 card è normale; 6 voci → 6 card è sospetto."

## Dataset scartati (rejected — with reasons)

- **`ISTAT:174_65_DF_DCCV_ASIMMETRIA_1`** (570 KB CSV in `_raw/pari-opportunita-inclusione/DCCV_ASIMMETRIA_1/`): ultimo anno disponibile **2013** — la rilevazione "Famiglie e soggetti sociali" / "Uso del tempo" è quinquennale e dal 2013 non è stata ripubblicata in SDMX. Fallisce il filtro recency ≥2020 esplicito nel prompt e ribadito in shortlist. **Scartato.** Il dato (indice di asimmetria del lavoro domestico nelle coppie italiane 70,7% nel 2013) è citato come caveat nella card 1. Raw conservato come archivio.
- **`ISTAT:42_70_DF_DCIS_IVG_CARATTDON_1`** (16,7 MB CSV in `_raw/pari-opportunita-inclusione/DCIS_IVG_CARATTDON_1/`): contiene 46.200 righe di breakdown cross-tab (età × stato civile × storia riproduttiva × numero casi precedenti, ecc.). **Non utilizzato per headline** perché non esiste una riga aggregata "totale Italia" recuperabile senza doppio conteggio attraverso le dimensioni. Citato come archivio nella card 2 "Sorgente raw"; il dato del volume IVG annuale (~60-70k) viene dalla Relazione 194 Ministero Salute (D1 PDF, non SDMX).
- **`OECD:DSD_LFS@DF_LFS`** (failed download, 281 byte error response): tentativo iniziale ha incontrato un *rate-limit* OECD; secondo tentativo con key filter ridotto ha restituito `NoResultsFound`. **Non bloccante**: il dato di occupazione era già coperto da ISTAT TAXOCCU1_3 (più granulare per il caso italiano, con macroregioni). Il confronto cross-country sull'occupazione femminile resta inseribile via tesi-citata Eurostat 70,2% nella narrativa della card. **Non riprovato** per evitare ulteriori rate-limit; se serve dato cross-country LFS più rigoroso, future runs.

## Voce esplicitamente deferred

- **Voce 4 — occupazione persone con disabilità.** Confermata fuori D1 SDMX (zero hits in catalogo ISTAT su keyword "disabili" intersecato "occup/lavoro/forze"). Il dato citato in tesi (32,5% disabili 15-64 occupati nel 2022) viene dal *Rapporto ISTAT "Conoscere il mondo della disabilità"* — pubblicato come release tematica PDF annuale, non come dataflow SDMX. Routing futuro:
  1. Ingestione del PDF ISTAT come D1 raw_doc, oppure
  2. Tentativo via Eurostat `hlth_dlm010` (population by limitation) — non in batch v1.
  3. Per ora il chatbot risponde a domande su occupazione disabili **citando la tesi 15** (che riporta il dato 32,5%, fonte ISTAT 2022) e segnalando la fonte ufficiale.

## Caveat e follow-up

- **Part-time involontario.** Il claim della tesi 15 che "l'Italia ha la percentuale più alta di occupazione part-time involontaria in Europa" non è stato verificato in questo batch perché il dataflow OCSE `DF_FTPT_INC_GEN` non separa voluntary/involuntary. La fonte target è **Eurostat `lfsa_eppgai`** (involuntary part-time as % of total part-time). Da aggiungere a future runs o esposto al chatbot come gap (Tier-3 search su Eurostat).
- **Obiezione di coscienza per regione.** Gap noto e dichiarato. Tier-3 (web search) deve risolvere la query "% medici obiettori IVG per regione" via Ministero Salute Relazione 194 annuale. Non in scope SDMX/v1.
- **Donne in posizioni apicali, violenza di genere, rappresentanza parlamentare.** Esclusioni consapevoli a livello di wishlist (vedere il file wishlist) — non sono fallimenti di questa pipeline ma scelte di scope.
- **GWG paradosso italiano.** La narrativa della card 1 esplicita un punto sensibile per il chatbot: il GWG mediano italiano è basso (5,1%) **per effetto di selezione**, non per parità raggiunta. Il chatbot deve **rifiutare** una lettura semplicistica "Italia ha quasi parità retributiva" — è centrale per evitare un misuse del dato in dibattito politico avversariale. La card cita Banca d'Italia QEF 539 (2019) come fonte per misure correttive del gap effettivo.

## Headline numbers di riferimento (per audit indice)

- **Tasso occupazione femminile IT 15-64, 2024:** 53,3% (vs maschi 71,1%, gap 17,8 pp).
- **Tasso occupazione femminile Mezzogiorno 2024:** 37,2% (vs 63,3% Nord-Est).
- **Gender wage gap mediano IT 2024:** 5,1% (vs OCSE 10,3%, Germania 13,5%).
- **Incidenza part-time femminile IT 2024:** 76,5% (delle donne occupate part-time — quota stabile da 10 anni).
- **Tasso abortività standardizzato IT 2024:** 5,85 per 1.000 donne 15-49 (in calo -25% dal 2010).
- **Variabilità regionale IVG 2024:** Liguria 8,60 / Abruzzo 4,65 (rapporto 1,85×).

## Note tecniche emerse durante il run

1. **OECD.ELS.SAE è una nuova agency validated** (precedentemente non in lista prompt). HTTP 200 confermato per due dataflow (`DSD_EARNINGS@GENDER_WAGE_GAP`, `DSD_FTPT@DF_FTPT_INC_GEN`). Backfillare nel prompt.
2. **Il dataflow OECD `DSD_LFS@DF_LFS` ha 6 dimensioni** (REF_AREA, MEASURE, UNIT_MEASURE, SEX, AGE, LABOUR_FORCE_STATUS) ma diverse combinazioni di key ritornano `NoResultsFound`. Probabilmente richiede pattern di key specifici (whitelist combinations); il probe a freddo è inefficiente. Per future ingestion: usare il *databrowser* OECD per costruire l'URL della query e copiarlo.
3. **ISTAT TAXOCCU1_3 non ha "TOTAL" sentinel implicito** per education level: il filtro `EDU_LEV_HIGHEST=99` esiste come riga reale (totale già aggregato da ISTAT), bisogna passare quel codice esplicitamente. Discoperto al secondo passaggio dell'analisi.
4. **ISTAT IVG_CARATTDON_1 e simili dataflow ad alta dimensionalità non hanno riga "totale puro"**: anche cercando `AGE=TOTAL` + tutti gli altri a totale, il prodotto cartesiano dei totali non corrisponde a una singola riga aggregata (un caso registrato con multiple combinazioni storia-riproduttiva × numero-casi viene contato più volte). Per il volume totale annuo: usare un dataflow con riga aggregata pre-calcolata (in questo caso CARATTDON_5 fornisce direttamente i tassi, e i volumi assoluti vanno cercati altrove — Relazione 194).
5. **ASIMMETRIA family (DCCV_ASIMMETRIA_1, _2, ecc.)** copre indagini multi-annuali ISTAT: ultimo anno SDMX 2013. Per dati 2020+ probabilmente vanno usate release tematiche più recenti (rapporto "Tempi e attività" o "Famiglie e soggetti sociali") in PDF — non SDMX. Update di wishlist/voce 6 raccomandato per il prossimo batch.

Queste note possono confluire come update marginale nel prompt riutilizzabile (in particolare il punto 1 su `OECD.ELS.SAE`).
