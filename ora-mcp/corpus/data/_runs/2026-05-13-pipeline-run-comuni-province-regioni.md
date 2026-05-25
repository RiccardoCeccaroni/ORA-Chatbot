---
folder: comuni-province-regioni
pipeline_run_date: 2026-05-13
mode: autonomous-flow (per autonomous_data_pipeline_prompt.md)
wishlist_voci: 7
shortlist_candidates: 7 (4 ISTAT + 3 OECD)
downloads: 7 (5 HTTP 200 on first try; 2 OECD endpoints required key-dim retry)
cards_written: 4
voci_status:
  voce_1_struttura_amministrativa: partial — GOV_LEVEL angle covered; "numero comuni" fuori scope SDMX
  voce_2_digitalizzazione_pa: covered (OECD DGOGD)
  voce_3_personale_enti_locali: gap — RGS Conto Annuale fuori SDMX
  voce_4_settore_costruzioni: covered (OECD TABLE6)
  voce_5_consumo_di_suolo: gap — rinviato a ISPRA D2
  voce_6_procedimenti_civili: gap — ISTAT SDMX serie ferma al 2014 (stale)
  voce_7_overtourism: covered con caveat (ISTAT TUR_8 — solo italiani; stranieri da ingerire separatamente)
---

# Pipeline run — `comuni-province-regioni` — 2026-05-13

## Esito sintetico

4 stat-card scritte in `memory/corpus/data/comuni-province-regioni/`:

1. **`peso-settore-costruzioni-italia-2024.md`** — Costruzioni ISIC F = €116,8 mld nel 2024 = 5,94% del VA totale italiano (era 4,21% nel 2018; picco 2023 a 6,06%). Confronto cross-country 8 paesi UE-OCSE: Italia 4°, sopra Francia (5,59%) e Germania (4,93%), sotto Polonia (7,04%).
2. **`digitalizzazione-pa-italia-vs-paesi-2022.md`** — Italia Digital Government Index OECD 0,58 nel 2022 (4° su 8 peer UE: dietro UK 0,78, FR 0,66, ES 0,60; sopra PL 0,57, NL 0,56, BE 0,54, SE 0,52). OURdata 0,48 (5° su 9). Tutti i sub-indicatori italiani tra 0,08 e 0,11.
3. **`spesa-pubblica-per-livello-governo-italia-2022.md`** — Enti locali italiani (S1313) gestiscono 24,76% spesa AP totale e 49,18% degli investimenti pubblici. 12° su 42 paesi OECD per quota S1313; sopra media UE (21,13%) ma sotto modello nordico (DK 64%, SE 49%). 74% del procurement pubblico è a livello sub-statale (S13M).
4. **`concentrazione-presenze-turistiche-italia-2024.md`** — 212,2 milioni di presenze italiane in Italia 2024 (livello pre-COVID 2019). 5 regioni assorbono 48% del totale (ER 13,5%, VE 10,2%, TO 9,2%, LA 8,0%, LO 7,5%). Molise 0,2%, 70× meno di Emilia-Romagna. ⚠️ Solo residenti italiani — gap stranieri da colmare con TUR_3 o TUR_4 in pipeline futura.

## Dataset scartati (rejected — with reasons)

- **ISTAT `60_130_DF_DCCV_ICT_5`** (754 KB scaricato in `_raw/comuni-province-regioni/DCCV_ICT_5/`): "ICT — Famiglie e individui". **Scartato** perché il dataflow non espone l'indicatore "uso servizi PA online" (sub-indicatori sono: posta, ricerca info, e-commerce, banking, partecipazione politica, ecc., ma non "richiesta certificati / pagamento tasse / iscrizione anagrafe / SPID-CIE"). Per la digitalizzazione PA lato cittadino servirebbe `DCCV_ICT_3` o un'altra sub-tabella ICT. Raw conservato.
- **ISTAT `11_111_DF_DCSC_RESID_CONSTR_1`** (4,7 MB in `_raw/comuni-province-regioni/DCSC_RESID_CONSTR_1/`): "Fabbricati residenziali nuovi — province e classi di comune". **Scartato** perché TUTTI gli OBS_VALUE sono vuoti e l'OBS_STATUS è `J: Test value` — il dataflow è uno scaffold senza dati reali. Risultato strutturale già visto in pipeline difesa (cfr. `DCSP_SBSNAZ_14` ATECO 30.40 — confidenzialità diversa, ma same effect: dataset esposto dal catalogo, ma vuoto). **Pattern emergente:** verificare sempre OBS_STATUS dopo il download, anche su HTTP 200 + size>0.
- **ISTAT `72_155_DF_DCAR_NUM_PROC_CIV_1`** (23 KB in `_raw/comuni-province-regioni/DCAR_NUM_PROC_CIV_1/`): "Procedimenti civili — movimento". **Scartato per staleness**: serie ferma al **2010–2014** (5 anni di dati). La tesi 02 cita un dato 2022 (+4,8% vs 2021) che non è ricavabile via SDMX — quel numero ISTAT è probabilmente da una pubblicazione narrativa (Annuario o report tematico) non in formato dataflow. Per la metrica "domanda di giustizia civile" servirebbe attingere alle statistiche Cassazione/Ministero della Giustizia/CIVI — fuori scope SDMX. Raw conservato.

## Voci wishlist non coperte

- **Voce 1 (numero comuni e frammentazione).** L'angolo "decentralizzazione spesa" è coperto da card 3. Il **numero di comuni per classe di ampiezza** non è esposto come dataflow SDMX (è derivato dal censimento permanente e dall'anagrafe). Per quella metrica si dovrebbe attingere a "Elenco amministrazioni pubbliche" o "Annuario ISTAT" — fuori scope SDMX, in scope per una pipeline non-SDMX futura.
- **Voce 3 (personale enti locali).** RGS pubblica il "Conto annuale del personale PA" solo in Excel, non in SDMX. Voce non coperta — collassata implicitamente in voce 1 (decentralizzazione strutturale). Per il dato puntuale serve scaricare i tabulati RGS dal sito mef.gov.it.
- **Voce 5 (consumo di suolo).** ISPRA è la fonte autoritativa italiana ma è D2 nella tassonomia v1, non D1. Rinviato a un'eventuale futura ingestione D2 con explicit web-research authorization. Per il chatbot, le risposte su consumo di suolo passeranno per il momento via live web-search della ricerca ISPRA "Rapporto Consumo di Suolo 2024".

## Caveat e follow-up

- **Voce 7 (turismo) ha caveat strutturale.** La card 4 documenta solo le presenze di residenti italiani in Italia. I 250+ M presenze straniere annuali (probabilmente più concentrate su Roma/Venezia/Firenze) non sono nella card. Per coprire il fenomeno overtourism completo serve un'estrazione gemella su `DCSC_TUR_4` (granularità comunale) o `DCSC_TUR_3` (mensile). Marcato come **follow-up** in pipeline successiva su `cultura-sport-turismo` o estensione di questa scheda.
- **Tesi cita una cifra D3 (€99,3 mld VA costruzioni 2023 da Intesa-SRM).** La card 1 confronta con il dato OECD 2023 di €116,7 mld — gap del 17% per differenze metodologiche. **Non un'invalidazione della tesi** (l'ordine di grandezza ~5% PIL regge), ma la stat-card OECD diventa la fonte D1 primaria che il chatbot dovrebbe usare per qualsiasi domanda quantitativa.
- **Tesi cita "procedimenti civili +4,8% nel 2022".** Numero non ri-verificabile via SDMX (vedi rejection sopra). Il chatbot dovrà appoggiarsi a fonte web Live (Ministero Giustizia / Cassazione) per qualsiasi domanda quantitativa su contenzioso civile post-2014. La cifra della tesi va trattata come citazione testuale di ISTAT — accettata, ma non rinforzata da nessuna stat-card.

## Note tecniche emerse durante il run (di interesse per i parallel runs futuri)

1. **OECD `DSD_GOV_LEVEL@DF_GOV_LEVEL_2025` version=1.0**, non 1.1 come riportato nel catalogo XML cached (la `<Ref version="1.1">` nel catalogo era il riferimento al DataStructure, non al Dataflow). Lezione: per OECD agency-codes, fare prima un test fetch con `version=1.0` se la `version=1.1` ritorna 404.
2. **OECD `DSD_NAMAIN10@DF_TABLE6` v2.0 ha 12 dimensioni** nella `key`. Schema:
   `FREQ.REF_AREA.SECTOR.COUNTERPART_SECTOR.TRANSACTION.INSTR_ASSET.ACTIVITY.EXPENDITURE.UNIT_MEASURE.PRICE_BASE.TRANSFORMATION.TABLE_IDENTIFIER`.
   Il dataflow è classificato come `NonProductionDataflow` nel catalogo (annotation) ma di fatto funziona — non saltare i dataflow "non-production" senza un test fetch.
3. **OBS_STATUS = `J: Test value`** è il pattern di un dataflow esposto ma senza dati reali. Verificare sempre OBS_STATUS dopo il download. Pattern già visto su scheda PROC_CIV (stale): è il segnale "il dataflow esiste ma il rilascio è vecchio o sospeso".
4. **ISTAT `DCCV_ICT_5` ha 18 indicatori — nessuno è "uso servizi PA"**. Per la metrica PA-citizen serve scendere a un altro indicizzo della famiglia ICT (forse `_3` o `_6`). Non ho probato — il bisogno è coperto da OECD DGOGD lato offerta, e nel pilot questa scelta è esplicita.
5. **TUR_8 — `COUNTRY_RES_GUESTS` è la nazionalità del turista, NON la regione di provenienza in senso geografico**. Solo IT (residenti italiani) e sub-regioni IT_xxx (residenti per regione di residenza italiana). Per dati su turisti stranieri serve un altro dataflow della famiglia TUR.

## Sample headline numbers (per chatbot retrieval test)

- **Costruzioni Italia 2024:** 5,94% del VA totale italiano (€116,8 mld su €1.966 mld). Era 4,21% nel 2018 → +1,73 p.p. in 6 anni (effetto Superbonus+PNRR).
- **Digital Government Italy 2022:** 0,58 (OECD scala 0-1). Composito di 6 sub-indicatori tutti tra 0,08 e 0,11.
- **Open Data Italy 2022:** 0,48 — 5° tra 9 peer; sotto Francia 0,83, Polonia 0,79, Spagna 0,75.
- **Enti locali Italia 2022:** 24,76% spesa AP totale, 49,18% degli investimenti pubblici, 74% del procurement pubblico (a livello sub-statale S13M).
- **Turismo italiani in Italia 2024:** 212,2 milioni presenze. 5 regioni = 48% del totale. ER è 70x Molise.
