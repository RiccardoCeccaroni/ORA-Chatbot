---
folder: cultura-sport-turismo
date: 2026-05-13
phase: pipeline-run completo (resume from token-limit interruption)
wishlist_voci: 5
shortlist_dataflows: 6
downloads_attempted: 6
downloads_successful: 6
cards_written: 4
---

# Pipeline run — cultura-sport-turismo (2026-05-13)

Run completato dopo riprese da interruzione token-limit della sessione precedente. Wishlist + shortlist erano già approvati. Downloads parziali (4 ISTAT OK; 2 OECD avevano fallito per rate-limit OECD API). In questa ripresa: re-download OECD con key filter (REF_AREA limitato a Italia + peer turistici), deep-read di tutti i 6 dataset, judgment, scrittura cards.

## Status per voce wishlist

| # | Voce | Dataflow | Status |
|---|------|----------|--------|
| 1 | Turismo flussi e capacità ricettiva | ISTAT DCSC_TUR_7 + DCSC_TUR_5 | **coperta ✓** (fused in `flussi-turistici-italia-2024.md`) |
| 2 | Turismo contributo economico | OECD KEY_IND_PC + ENT_EMP | **coperta ✓** (fused in `contributo-economico-turismo-italia-2023.md`) |
| 3 | Turismo overtourism comunale | (collassata in voce 1 già in shortlist) | **parziale ⚠️** — concentrazione documentata solo a livello regionale, dato comunale richiede DCSC_TUR_OCCUPCOLLE (scartato in shortlist). Caveat documentato nella card flussi. |
| 4 | Sport pratica fisica | ISTAT AVQ_PERSONE_100 | **coperta ✓** (`pratica-sportiva-italia-2024.md`) |
| 5 | Cultura musei | ISTAT DCIS_MUSVIS_1 | **coperta ✓ con caveat** (`musei-italia-2015.md`) — dato fermo al 2015 nel dataflow SDMX, caveat di freschezza documentato esplicitamente |

**Bilancio finale:** 5 voci → 4 card scritte (fusioni applicate come previsto in shortlist). Bilanciamento tematico: 2 turismo + 1 sport + 1 cultura.

## Riepilogo download

| Dataflow | Agenzia | Size finale | Status |
|----------|---------|-------------|--------|
| `122_54_DF_DCSC_TUR_7` | ISTAT | 142 MB CSV | OK (download originario) |
| `122_54_DF_DCSC_TUR_5` | ISTAT | 17 MB CSV | OK (download originario) |
| `83_63_DF_DCCV_AVQ_PERSONE_100` | ISTAT | 1,3 MB CSV | OK (download originario) |
| `60_195_DF_DCIS_MUSVIS_1` | ISTAT | 4,9 MB CSV | OK (download originario) |
| `DSD_TOURISM_KEY@DF_KEY_IND_PC` | OECD.CFE.TOU | 90 KB CSV | **OK dopo re-download con key filter** (originario era 281 byte = rate-limit error message) |
| `DSD_TOURISM_ENT_EMP@DF_ENT_EMP` | OECD.CFE.TOU | 353 KB CSV | **OK dopo re-download con key filter** (originario era 281 byte) |

OECD rate-limit (HTTP 200 con body "You have exceeded the number of requests for data downloads or very large data ranges...") era la causa del fallimento iniziale. Soluzione: chiamata con key `ITA+FRA+ESP+DEU+GRC+AUT+PRT+GBR+USA` (per KEY_IND_PC) e simile per ENT_EMP — limita il volume a ~90-350 KB invece del pull integrale.

**Dimensioni di ENT_EMP scoperte durante deep-read:** 4 dimensioni (REF_AREA.MEASURE.UNIT_MEASURE.ACTIVITY) — aggiunge ACTIVITY rispetto a KEY_IND_PC. Documentato nei caveat delle card.

## Sample headline numbers per card

### `flussi-turistici-italia-2024.md`
- 466,2 mln presenze totali 2024 (record storico, +4,2% YoY, +6,7% vs 2019)
- 139,6 mln arrivi 2024
- Quota stranieri 54,5% delle presenze (era 52,4% nel 2023, "52,44%" della tesi confermato)
- Germania = 25,7% degli stranieri (65,3 mln notti)
- Concentrazione estiva: 55,4% in giu-set, 44,9% in lug-ago
- Nord-Est = 36% delle presenze; Veneto prima regione (73,5 mln)
- Top-5 regioni concentrano 55%, top-10 il 79%

### `contributo-economico-turismo-italia-2023.md`
- 5,0% del PIL 2023 (5,4% GVA); 8,5% dell'occupazione totale
- 2.101.109 occupati turistici (coerente con "2 mln" della tesi ISTAT-CST)
- Food&beverage = 54% dell'occupazione settoriale (1,13 mln addetti)
- Italia 2° in Europa per occupazione assoluta (dopo Spagna 2,98 mln)
- Produttività relativa turismo IT = 0,64x media nazionale (vs Austria 2,8x)
- Microimprese: 262.568 esercizi short-term accommodation per 348.000 addetti = ~1,3 addetti/esercizio (conferma "90% microimprese" tesi)

### `pratica-sportiva-italia-2024.md`
- 33,2% popolazione 3+ "nessuno sport né attività" 2024 (≈19,1 mln persone)
- 28,6% pratica continuativa (era 22,8% nel 2010 → +5,8 p.p. in 14 anni; 30,3% nel 2025 provv.)
- Picco pratica continuativa: 6-10 anni (68,1%) e 11-14 anni (66,2%) — segmento scolare
- Crollo a 6,0% over-75 (61,7% sedentari completi)
- Gap di genere: M 33,1% continuativa vs F 24,3% (-8,8 p.p.)

### `musei-italia-2015.md`
- 4.976 istituzioni museali (4.158 musei + 282 aree archeologiche + 536 monumenti)
- 110,6 mln visitatori 2015
- Stato gestisce 439 strutture (9%) ma cattura 43% dei visitatori
- Lazio + Toscana = 43% dei visitatori nazionali (47 mln su 110)
- Mezzogiorno 25% delle istituzioni, 19% dei visitatori → "deserti culturali" quantificati
- **⚠️ Freshness flag**: dato 2015 è ultima rilevazione disponibile nel dataflow SDMX (rilevazioni 2018 e 2023 esistono come PDF/Excel ISTAT non-SDMX)

## Datasets rejected o non scaricati (rispetto a wishlist)

Già scartati in shortlist (decisi durante sessione precedente):
- ISTAT TUR_1/2/3/4/8-13 (varianti viste di TUR_7, ridondanti)
- ISTAT DCSC_TUR_OCCUPCOLLE (comunale, troppo grande)
- ISTAT AVQ_PERSONE_101/102/103 (cross-tab età × education / regione / professione — over-granular per stat-card sintetica)
- ISTAT MUSVIS_2/3/4/5 (sotto-rilevazioni di MUSVIS_1)
- ISTAT DCIS_MUSVIS_COM_1 (comunale — non scaricato, cartella vuota nel raw, non rilevante per v1)
- ISTAT DCIS_BIBLIOT_1 (biblioteche statali — limitata numerosità)
- ISTAT DCSP_AGRITURISMO (afferente a agricoltura)
- OECD DSD_TOURISM_DOM/INTER/EXP/RECEIPTS (ridondanti con KEY_IND_PC + ISTAT)
- BES_TERRIT_9 (meta-aggregato BES, opaco)

Non scartati ma volutamente non approfonditi:
- Dimensione **OECD aggregate (`OECD`)** assente in KEY_IND_PC (l'aggregato OECD non è precalcolato in questo dataflow specifico — testato durante deep-read).

## Caveat strutturali da segnalare al chatbot in fase di RAG

1. **MUSVIS_1 fermo al 2015.** Sul "quanti musei oggi" il chatbot deve esibire il dato 2015 SDMX ma triangolare con web-research su pubblicazioni ISTAT 2018/2023 non-SDMX. Non è un bug della card ma una limitazione strutturale della pipeline SDMX-first di v1.
2. **Concentrazione comunale citata dalla tesi (41,6% in 50 comuni)** non quantificabile dal batch corrente — è un dato Banca d'Italia/CDP/Touring che vive fuori dai dataflow SDMX qui usati. La card flussi cita il dato come "non ricavabile da TUR_7" e suggerisce live-search per risposte specifiche.
3. **Definizioni di "sedentarietà" non univoche.** La tesi cita "quasi metà degli adulti non pratica attività fisica" ma il dato preciso varia 25-65% a seconda della definizione (no sport / no attività / né sport né attività; quale fascia di età). La card pratica-sportiva documenta esplicitamente questa ambiguità.
4. **Filiera "allargata" del turismo.** I dati OECD KEY_IND_PC misurano direct contribution; la cifra ORA di "2 mln di occupati industria turistica allargata" è ambigua — direct OECD = 2,10 mln, mentre la "allargata" (con indotto) sarebbe ~3,5-4 mln. Il chatbot deve usare il numero diretto e non sovra-interpretare la "allargata" senza fonti.

## Follow-up / Deferred

- **MUSVIS aggiornamento 2018/2023 in SDMX.** Quando ISTAT pubblicherà la nuova edizione in formato SDMX (atteso 2026-2027), ripetere il pull e rifare la card aggiornata.
- **TUR_OCCUPCOLLE per overtourism comunale.** Considerare in v2 (richiede aggregazione su 7.896 comuni — costoso per stat-card sintetica, meglio una pagina-strumento).
- **OECD CFE.TOU agency code validato** — già documentato in shortlist e nel pool funzionante (OECD.CFE.TOU si aggiunge a OECD.SDD.NAD, OECD.STI.STP, OECD.GOV.GIP). Pattern di key per quel dataflow: dimensioni REF_AREA.MEASURE.UNIT_MEASURE (3 dim per KEY_IND_PC; 4 per ENT_EMP che aggiunge ACTIVITY).
- **Filtro key OECD esplicito è un requisito non opzionale** quando il dataflow è "popoloso" — l'errore "You have exceeded the number of requests" può capitare anche su dataflow non enormi se sommato a parallele attive. Documentato.

## Cards finali nel folder

```
memory/corpus/data/cultura-sport-turismo/
├── flussi-turistici-italia-2024.md
├── contributo-economico-turismo-italia-2023.md
├── pratica-sportiva-italia-2024.md
└── musei-italia-2015.md
```

Nessun blocco "very-very-important" è stato attivato durante il run. Le quattro condizioni:
1. ✗ No tesi — tesi `03-cultura-sport-turismo.md` presente.
2. ✗ Tutte le ricerche catalog senza candidati — copertura D1 per turismo/sport/cultura confermata.
3. ✗ Nessuna contraddizione >20% con cards esistenti — folder era vuoto, nessun cross-folder.
4. ✗ Tutti i download falliti — solo 2 falliti per rate-limit, risolti con re-download.
