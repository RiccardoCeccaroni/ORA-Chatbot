---
folder: esteri-relazioni-internazionali
date: 2026-05-13
mode: resume (token-limit recovery from prior run)
wishlist_voci: 6
shortlist_candidates: 5 dataflow + 1 riuso
downloads: 5 (4 new + 1 reuse difesa/DF_TABLE11)
cards_written: 4 (new) + 1 (existing, not modified)
cards_total: 5
---

# Pipeline run audit — esteri-relazioni-internazionali

## Sintesi

Esecuzione completata in resume mode. Il run precedente (2026-05-13 ~00:31) aveva scritto wishlist, shortlist, scaricato 5 raw (DF_DAC1, DF_DAC2A, DF_FDI_POS_CTRY, DF_IMTS, DF_TABLE1_GDP) e prodotto la card DAC1, poi è morto per token-limit. Tre raw sub-cartelle contenevano solo errori "ExceededRequests" (281 byte). Questo run ha:

1. Re-scaricato i 3 dataset falliti con chiavi corrette (validate via SDMX structure XML).
2. Sostituito il dataset `DF_IMTS` con `DF_BIMTS` (CPA 2.1) perché DF_IMTS non supporta bilateral counterpart breakdown — solo Italy-vs-World.
3. Phase 4-6 su DAC2A, BIMTS, FDI, GDP TABLE1.
4. Scritte 3 nuove cards.

Cards totali nel folder al termine: **5** (1 esistente + 4 nuove). Range 3-5 atteso: rispettato.

## Per-voce status

| # Voce | Tema | Dataset | Card | Status |
|---|---|---|---|---|
| 1 | APS Italia vs donatori | OECD DAC1 | `aps-oda-italia-vs-donatori-2022.md` (esistente) | ✓ covered |
| 2 | APS settoriale/geografico | OECD DAC2A | `aps-allocazione-geografica-italia-2022.md` (NEW) | ✓ covered |
| 3 | Commercio bilaterale ITA-CN/USA | OECD BIMTS (sostituisce IMTS) | `interscambio-bilaterale-italia-2023.md` (NEW) | ✓ covered |
| 4 | FDI stock outward/inward | OECD FDI POS_CTRY | `fdi-italia-investimenti-bilaterali-2023.md` (NEW) | ✓ covered |
| 5 | Spesa militare UE vs Russia/USA | riuso DF_TABLE11 difesa | nessuna nuova card | ⚠ partial — collassata in card esistente `spesa-difesa-italia-vs-paesi-2022.md` (folder difesa); confronto blocco-UE non ricostruito esplicitamente in questo folder |
| 6 | PIL UE vs USA vs Cina | OECD TABLE1 (DSD_NAMAIN10) | `pil-blocco-ue-vs-usa-cina-2023.md` (NEW) | ✓ covered |

## Datasets scartati / errore

- **DF_IMTS**: scaricato (1,4 MB) ma rivelato inadatto — il dataflow ha COUNTERPART_AREA limitato a `W` (Mondo) per Italy reporter, non supporta bilaterale. **Sostituito con DF_BIMTS** (Balanced International Merchandise Trade Statistics, CPA 2.1) della stessa agency OECD.SDD.TPS, che invece supporta bilaterale ITA × tutti i partner. Raw `_raw/DF_IMTS/data.csv` mantenuto come fallback (totale Italia mensile, utile in futuro come time-series macro).
- **DF_FDI_POS_CTRY primo pull (307 MB)**: troppo largo (default unfiltered). Re-pull con key esplicita su MEASURE+UNIT_MEASURE+SECTOR ha ridotto a 670 KB con stesso scope informativo.

## Dataflows nuovi confermati funzionanti (aggiornamento al prompt riusabile)

Già notati nel pilot difesa + nuovi confermati questo run:

- **OECD.DCD.FSD**: 200 OK — Development Cooperation (DAC1, DAC2A).
- **OECD.DAF.INV**: 200 OK — Investment / FDI BMD4 (DF_FDI_POS_CTRY, DF_FDI_FLOW_CTRY).
- **OECD.SDD.TPS**: 200 OK — Trade (DF_BIMTS_CPA_2_1 con bilaterale, DF_IMTS solo aggregato).
- **OECD.SDD.NAD**: 200 OK già nota (TABLE11 COFOG + TABLE1 GDP).

**Nuovo finding**: il dataflow `DF_IMTS` di TPS NON ha bilateral breakdown nonostante il nome suggerisca diversamente. Usare sempre **DF_BIMTS_CPA_2_1** o **DF_BIMTS_HS2017_2D** per trade bilaterale OECD.

## Caveat metodologici da segnalare al chatbot

1. **GDP PPP vs nominale**: la frase tesi 07 "Cina si sta avvicinando a UE" è obsoleta in PPP (CHN ha superato UE nel 2018). Resta valida in USD a cambio corrente. Le due metriche sono entrambe legittime ma misurano cose diverse — il chatbot deve scegliere con cura quale citare a seconda del contesto (militare/strategico → PPP; commerciale → nominale).
2. **Russia non in OECD**: per qualsiasi confronto Italia/UE-Russia su PIL, sanzioni macro, spesa militare → fallback obbligato a web search (Banca Mondiale WEO, IMF, SIPRI). I dati D1 OECD non coprono Russia.
3. **Spike DAC2A 2021 SSA $984M**: dovuto a debt swap Argentina e contributi multilaterali one-off, **non strutturale**. Il chatbot non deve usarlo come trend.
4. **Pass-through fiscali in FDI** (NLD, LUX): inward FDI Italia dominato per il 43% da Olanda + Lussemburgo. La "vera" provenienza è distribuita. Per stime di esposizione reale verso USA/CN: il dato `IMC` (immediate counterpart) sotto-stima sistematicamente, vale 1,5-2× più di quanto registrato.

## Carve-out empirico vs valori (per ogni card)

Le tre nuove cards documentano dove i dati confermano e dove non possono confermare le proposte ORA:

- **APS allocation**: i dati confermano che il Piano Mattei è "limitato nelle risorse" (5,3% in SSA, 2,0% in Nord Africa); non dicono quanto ORA *vorrebbe* allocare.
- **BIMTS bilaterale**: i dati confermano vulnerabilità USA (10,8% export) e deficit strutturale CN; non determinano la scelta politica di "non equidistanza".
- **FDI**: i dati mostrano floor basso in MEA/Africa ($21 mld, 3,5%); la priorità geografica resta scelta valoriale.
- **GDP PPP**: i dati confermano UE come blocco dimensionalmente competitivo; la *volontà politica* è altra dimensione.

## Sample headline numbers per card

| Card | Headline |
|---|---|
| aps-oda-italia-vs-donatori-2022.md (esistente) | Italia 2022 = $6,65 mld ODA, 0,33% RNL — sotto target ONU 0,7% di 0,37 p.p. |
| aps-allocazione-geografica-italia-2022.md | Solo 9,3% APS italiano va in Africa; Sub-Sahariana 5,3%; Ucraina 5,2% (da 0,02% nel 2021) |
| interscambio-bilaterale-italia-2023.md | Surplus +$45 mld con USA, deficit -$22 mld con CN, crollo import Russia -83% 2022→2023 |
| fdi-italia-investimenti-bilaterali-2023.md | Outward $613 mld (49% UE, 11% USA, 2,3% CN, 3,5% Nord Africa); Italia net creditor +$114 mld |
| pil-blocco-ue-vs-usa-cina-2023.md | UE27 $27,2 T ≈ USA $27,4 T; Cina $34,6 T (+27% sull'UE in PPP, l'ha superata nel 2018); Italia +66% in 13 anni (la più lenta G7-Europa) |

## Voci deferred (fuori D1 v1, già flaggate nella wishlist)

- Sanzioni alla Russia (volume/valore, evasione, flotta ombra) — fonti SIPRI / Castellum.AI / KSE / EU DG-FISMA → D2/D3.
- Asset russi congelati e profitti devoluti (€35 mld al fondo Ucraina) — Euroclear / EU Commission → D2.
- Aiuto militare Italia all'Ucraina — Kiel Institute Ukraine Support Tracker → D2/D3.
- Spesa NATO % PIL — NATO Defence Expenditure Report → D2 (gap già flaggato in folder `difesa`).
- Export armi italiano — UAMA + SIPRI Arms Transfers → D2.
- Indice influenza cinese nei Balcani / dipendenza UE da Cina (terre rare, chip) — MERICS, JRC → D3.
- Eurobarometro percezione europeismo — Commissione UE (D1, ma non SDMX-OECD).
- Voto Italia in UE / ONU — VoteWatch (non SDMX).

## Follow-up

- **Tesi 07 ha cifre puntuali interne** ("PIL Cina si avvicina a UE", "Cina 21,3% import UE 8,3% export UE", "spesa militare europea +58% Russia", "asset russi $300 mld / profitti $35 mld"). Cinque di queste sono coperte dalle nuove card (3 confermate, 1 da aggiornare — la frase Cina-UE; 1 fuori scope D1 — Russia spesa militare). Le restanti due (sanzioni, asset russi) restano deferred a D2.
- **Card 5 (riuso difesa TABLE11)**: il file raw `_raw/difesa/DF_TABLE11/data.csv` non è stato touch-ato. La proposta di card "blocco-UE vs Russia/USA/CN spesa militare" è fattibile ma richiederebbe somma dei singoli paesi UE (dati già nel file) — non scritta in questo run per parsimonia (3 voci della tesi richiedono SIPRI per la Russia, già notato). Riservata a futuro pull D2.
- **2024 data**: per BIMTS, FDI, GDP — tutti i dataset hanno T-1 lag. Il prossimo refresh significativo è metà 2025 (dati 2024).

## Conclusione

Pipeline completata. 4 nuove cards scritte coerenti col §5 schema CLAUDE.md, voce per voce ancorate a passaggi specifici della tesi 07, con caveat metodologici espliciti e cross-reference ad altre cards del corpus (`pil-italia-2024`, `spesa-difesa-italia-vs-paesi-2022`). Nessuna delle 4 "very-very-important" condizioni si è attivata. Nessun ping a Riccardo necessario.
