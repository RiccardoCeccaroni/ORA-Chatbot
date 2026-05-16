---
folder: giustizia
pipeline_run_date: 2026-05-13
mode: production
wishlist_voci: 6
shortlist_candidates: 7 (5 ISTAT + 2 OECD)
downloads: 7 (all HTTP 200)
cards_written: 3
voci_status:
  voce_1_durata_civile: gap (CEPEJ-only, no D1 cross-country for trial duration)
  voce_2_durata_penale: partial (Italia 2017 ISTAT pre-dibattimentale, cross-country via WJP proxy)
  voce_3_sovraffollamento_carceri: covered (full)
  voce_4_movimento_procedimenti: gap (ISTAT NUM_PROC_* series stale at 2014)
  voce_5_magistrati_per_100k: gap (CEPEJ-only, no D1)
  voce_6_fiducia_giustizia: covered (OECD Trust Survey + WJP indices)
---

# Pipeline run — `giustizia` — 2026-05-13

## Esito sintetico

3 stat-card scritte in `memory/corpus/data/giustizia/`:

1. **`sovraffollamento-carceri-italia-2024.md`** — Italia 2024: 120,56% occupancy. Trend a U: 151% (2010) → 105% (2014/2020) → 121% (2024). 19/22 regioni sopra capienza; Puglia 148%, Lombardia 144%, Friuli-Venezia Giulia 142%. Serie storica 2010-2024.
2. **`fiducia-qualita-giustizia-italia-2024.md`** — Italia 42,5% trust in courts (2023, OECD), penultima nel peer set UE+G7 (sopra solo Spagna 45,1%). Quality of civil justice 0,57/1 (2024, WJP) — la più bassa nel peer set. Indipendenza dal governo 0,67 — meglio della retorica della tesi.
3. **`durata-procedimenti-penali-italia-2017.md`** — Italia 2017: 26 mesi medi tra iscrizione e decisione PM. Eterogeneità estrema: Roma 34 mesi, Trento 12 mesi; mafia/terrorismo 100+ mesi, frodi 1 mese. **STALE — ultimo dato 2017**, ma rilevante come unica fonte D1 ISTAT su durata penale. Esplicita disclosure di non-equivalenza con tabella tesi (CEPEJ-based).

## Dataset scartati (rejected — with reasons)

- **`ISTAT:72_155_DF_DCAR_NUM_PROC_CIV_1`** (23 KB in `_raw/giustizia/NUM_PROC_CIV_1/`): "Movimento procedimenti civili". **Scartato per staleness** — serie ferma al 2014 (10 anni di silenzio statistico). ISTAT ha evidentemente migrato/discontinuato questo dataflow. Raw conservato per audit; menzionato nel caveat della voce 4 della wishlist.
- **`ISTAT:73_160_DF_DCAR_NUM_PROC_PEN_1`** (49 KB in `_raw/giustizia/NUM_PROC_PEN_1/`): "Procedimenti penali — movimento". **Scartato per staleness** — serie ferma al 2014, stesso pattern di NUM_PROC_CIV_1.
- **`ISTAT:74_171_DF_DCAR_PROC_AMM_1`** (2,2 MB in `_raw/giustizia/PROC_AMM_1/`): "Procedimenti di giustizia amministrativa". **Scartato per staleness** — serie ferma al 2015 (9 anni di silenzio). La tesi 08 tratta la magistratura amministrativa (Consigli di Stato, conflitti d'interesse) ma D1 ISTAT non offre dati attuali; per future iterazioni servirà fonte alternativa (Consiglio di Stato relazioni annuali, D2).
- **`OECD.GOV.GIP:DSD_GOV_INT@DF_GOV_SPS_2025`** (103 KB in `_raw/giustizia/DF_GOV_SPS_2025/`): "Satisfaction with public services". **Non scartato ma collassato** nella card 2 (fiducia+qualità) insieme a TDG. Le misure WJP (RLCJ_Q, EFJ_RLCJ_FGI, AJ_AACJ) sono integrate lì.

## Caveat e follow-up

- **Voce 1 (durata processi civili Italia vs Europa) = GAP D1.** Il tabella tesi `540gg vs 239gg` è CEPEJ-based. CEPEJ non è in D1 SDMX e OECD non ha un'agenzia giustizia (`OECD.JUS`, `OECD.GOV.JUS` → 404). Per coprire serve aggiungere CEPEJ a D2 — proposta esplicita per future ingestioni.
- **Voce 2 (durata penale Italia vs Europa) = PARZIALE D1.** Italia coperta via PROCEEDCRIME_A_11 (con caveat di non-equivalenza con CEPEJ), cross-country via WJP "Quality of civil justice" (proxy non perfetto, riguarda civile non penale). Per dato puro CEPEJ servirebbe stessa fonte D2.
- **Voce 4 (movimento procedimenti) = GAP per staleness ISTAT.** Le 3 serie ISTAT DCAR (NUM_PROC_CIV, NUM_PROC_PEN, PROC_AMM) sono tutte ferme al 2014-2015. Sono dataflow discontinuati. Per dati aggiornati su pendenza/sopravvenienze/definiti serve Ministero della Giustizia "Monitoraggio civile e penale" (D2/D3, già citato nelle fonti della tesi 08).
- **Voce 5 (magistrati per 100.000 abitanti) = GAP D1.** Nessuna fonte ISTAT/OECD pubblica una serie cross-country organica di "magistrati per capita". CEPEJ ha quel dato (4,2 judges/100k Italia vs 21,4 Germania) — D2, non in v1.
- **Sotto-tema admin/CSM:** la tesi attacca specificamente la magistratura amministrativa e il CSM ("99,3% promossi nelle valutazioni"). Nessuna fonte D1 ha quei dati. Per coprire serve attingere a relazioni CSM (D2) o Consiglio di Stato (D2). Defer.
- **Cittadinanza:** la tesi tratta ius scholae/matrimonii ma il dato di flusso naturalizzazioni è già coperto in `immigrazione/naturalizzazioni-italia-2024.md`. No duplicazione.

## Sintesi voci coperte

| Voce | Status | Card di riferimento | Note |
|---|---|---|---|
| 1. Durata processi civili IT vs EU | gap | — | CEPEJ-only (D2 not in v1) |
| 2. Durata processi penali IT vs EU | partial | `durata-procedimenti-penali-italia-2017.md` | IT pre-dibattimentale 2017; EU via proxy WJP |
| 3. Sovraffollamento carceri | covered | `sovraffollamento-carceri-italia-2024.md` | full series 2010-2024 + regional |
| 4. Movimento procedimenti | gap | — | ISTAT DCAR series discontinued at 2014-15 |
| 5. Magistrati per 100k | gap | — | CEPEJ-only (D2 not in v1) |
| 6. Fiducia nella giustizia | covered | `fiducia-qualita-giustizia-italia-2024.md` | OECD TRUST_CL + WJP indices |

3 voci coperte (2 covered, 1 partial); 3 voci gap. Tasso di copertura D1: 50% delle voci proposte. Le 3 gap sono **strutturali** (D2 CEPEJ/Min. Giustizia/CSM richiesti) non risolvibili in D1 v1.

## Note tecniche emerse durante il run

1. **ISTAT DCAR series stale.** I dataflow `72_155`, `73_160`, `74_171` (DCAR — Statistiche giudiziarie) sembrano essere stati discontinuati al 2014-2015. Il catalog SDMX non li marca come deprecated, ma de facto lo sono. **Implicazione:** in future ricerche su temi giustizia/sicurezza, verificare staleness *prima* di scaricare. (Aggiungere al prompt riutilizzabile.)
2. **PROCEEDCRIME_A_11 è 193 MB.** Per future ingestioni di metriche aggregate (all-Italy, all-districts), usare un key filter SDMX per ridurre il payload (es. `IT.ALL.99.....` per ottenere solo le righe Italia/tutti distretti). Lo scoreboard `DSD_DCCV_PROCEEDCRIME_A` ha 14 dimensioni, dispiegate completamente generano cross-tab di centinaia di migliaia di righe.
3. **OECD GIP è la giusta agency per giustizia.** Conferma del prompt riutilizzabile: `OECD.GOV.GIP` contiene le misure WJP/Trust che servono. `OECD.JUS`, `OECD.GOV.JUS` (probate) tornano 404 e non vanno usate.
4. **WJP Rule of Law re-pubblicato in OECD GoG 2025.** Trattare come D1 con citazione doppia (WJP origin + OECD redistribution). Non è una promozione D3→D1 arbitraria: è il fatto che il dato sia stato selezionato per la pubblicazione ufficiale OECD a renderlo D1.

Queste note saranno riflesse nella prossima edit del prompt riutilizzabile, se il volume di occorrenze giustifica modifiche permanenti.

## Headline numbers riferimento per il chatbot

- Carceri: **120,56%** occupancy 2024 (Italia); picco Puglia 148%, minimo Valle d'Aosta 78%.
- Trust: **42,5%** italiani 2023 (OECD), vs NL 72,2%, SE 63,5%, DE 57,6%; ITA penultima del peer set.
- Quality of civil justice: **0,57/1** (WJP 2024), ultima nel peer set OCSE; gap di 0,25 con SE/NL/DE.
- Durata penale (PM phase): **26 mesi** media nazionale 2017 (ultimo D1 disponibile); 34 mesi Roma, 12 mesi Trento.
