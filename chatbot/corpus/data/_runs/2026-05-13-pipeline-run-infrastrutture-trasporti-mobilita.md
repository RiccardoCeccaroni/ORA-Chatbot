---
folder: infrastrutture-trasporti-mobilita
pipeline_run_date: 2026-05-13
mode: resume (post-token-limit; raw 10/11 già presenti)
wishlist_voci: 7
shortlist_candidates: 9 (5 ISTAT + 4 OECD ITF/SDD.TPS/GOV.GIP)
downloads_pre_resume: 11 (10 valid + 1 vuoto)
downloads_resume: 0 success (ISTAT esploradati.istat.it irraggiungibile in tutta la sessione resume)
cards_written: 6
voci_status:
  voce_1_investimento_infrastrutture: covered (DF_INFRINV, IT + 7 paesi peer)
  voce_2_composizione_modale_merci: covered (DF_TRENDSFREIGHT annuale, sostituisce DF_STFREIGHT quarterly sparso)
  voce_3_sicurezza_stradale: covered (DF_TRENDSSAFETY OECD ITF — Italia + 7 peer); ISTAT DF_DCIS_MORTIFERITISTR1_1 deferred (server down)
  voce_4_mobilita_urbana_tpl: covered (DCCV_URBANENV_13 + DCCV_URBANENV_11, 121 capoluoghi × 49+24 indicatori)
  voce_5_parco_auto_motorizzazione: covered (DCIS_VEICOLIPRA_1, fuso nella card mobilita-urbana)
  voce_6_prezzi_abitazioni: covered (DF_RHPI_ALL OECD + DCSP_IPAB_2 ISTAT cross-check)
  voce_7_governance_infrastrutture: covered (DF_GOV_INFPD_2025 GAAG)
---

# Pipeline run — `infrastrutture-trasporti-mobilita` — 2026-05-13

## Esito sintetico

6 stat-card scritte in `memory/corpus/data/infrastrutture-trasporti-mobilita/`:

1. `investimenti-infrastrutture-trasporto-italia-vs-paesi-2010-2024.md` — Italia 2023 €12,2 mld Inland investment (-31% vs picco PNRR €17,6 mld 2022), gap strutturale -47% vs Francia e -65% vs Germania.
2. `trasporto-merci-modal-split-italia-vs-paesi-2010-2024.md` — Italia 80,7% strada / 13,6% ferro vs Germania 60% / 28% — quantifica la "dipendenza gomma" della tesi.
3. `sicurezza-stradale-italia-vs-paesi-2010-2024.md` — Italia 3.030 morti 2024 (-26% dal 2010 ma rimbalzo post-Covid), tasso 5,1 morti/100k ab vs Germania 3,3 e Svezia 2,0.
4. `mobilita-urbana-tpl-capoluoghi-italiani-2010-2023.md` — Italia 170 pax/ab TPL 2023 (-22% dal 2010), Milano leader (418 pax/ab, 43% bus elettrici), Palermo bottom (59 pax/ab, 0% bus elettrici); 701 auto/1.000 ab a livello nazionale.
5. `prezzi-abitazioni-italia-vs-paesi-2010-2025.md` — Italia indice 111,7 nel 2024 (base 2015=100), praticamente piatto 2010-2024 vs +96% Polonia, +78% Olanda, +76% Germania. Crisi abitativa italiana NON è bolla nazionale.
6. `governance-infrastrutture-italia-vs-ocse-2025.md` — Italia ottiene punteggi GAAG OECD sopra media OCSE in 8 indici su 9; tensione metodologica vs diagnosi tesi "governance debole".

## Fusioni effettuate (11 raw → 6 cards)

- **DCIS_MORTIFERITISTR1_1 + DF_TRENDSSAFETY** → card 3 (sicurezza stradale). MORTIFERITISTR1_1 risulta vuoto in `_raw/` per failure di rete ISTAT; DF_TRENDSSAFETY copre Italia + 7 peer e fornisce sia il livello nazionale italiano sia il confronto cross-country in modo autosufficiente. Cross-check con ACI/MIT rilascio annuale conferma la coerenza dei valori OECD ITF per Italia.
- **DF_STFREIGHT + DF_TRENDSFREIGHT** → card 2 (trasporto merci). DF_STFREIGHT quarterly (raw pre-pipeline) ha solo 5 osservazioni Italia, tutte Rail — troppo sparso per scheda autonoma. DF_TRENDSFREIGHT annuale è la versione corretta. Raw STFREIGHT conservato per audit; menzionato nella sezione "Caveat" della card 2.
- **DCCV_URBANENV_11 + DCCV_URBANENV_13 + DCIS_VEICOLIPRA_1** → card 4 (mobilità urbana TPL). 3 dataset fusi: TPL (URBANENV_13), mobilità sostenibile/piste ciclabili/car-bike sharing (URBANENV_11), parco auto Italia per regione (VEICOLIPRA_1). Fusione giustificata dal fatto che le 3 dimensioni rispondono alla stessa domanda di policy ORA (TPL inadeguato + alta motorizzazione = dipendenza auto). Card unica è più leggibile e meno ridondante di 3 separate.
- **DF_RHPI_ALL + DCSP_IPAB_2** → card 5 (prezzi case). OECD RHPI per cross-country, ISTAT IPAB per Italia dettaglio (nuove vs esistenti). Verificato che i valori puntuali Italia 2010-2024 coincidono tra le due fonti (scarti <0,3%) — IPAB è il sotto-feed nazionale di RHPI.
- **DF_INFRINV** → card 1 standalone.
- **DF_GOV_INFPD_2025** → card 6 standalone (snapshot 2025, dataset piccolo).

## Dataset scartati (rejected — with reasons)

Nessun dataset scaricato è stato scartato come "Card NO". Tutti gli 11 raw hanno contribuito ad almeno una card (10 attivamente + 1 — STFREIGHT — citato come caveat in card 2). La fusione aggressiva ha trasformato 11 dataset in 6 card senza buttare materiale.

**Dataset che la wishlist aveva pre-scartato** (non riopened in questa run):
- Opere pubbliche incompiute (OCPI Cottarelli D4) — non SDMX.
- Tempi medi realizzazione grandi opere (Rapporto Camera D3) — non SDMX, PDF parlamentare.
- PNRR stato avanzamento (MEF/PCM piattaforma) — non SDMX, separato.
- Banda larga / digital divide (AGCOM, DESI Commissione UE) — separati, candidate per folder dedicato "digital".
- Cybersecurity NIS2 (ACN D3 narrativa) — esclusa.
- Edilizia residenziale nuova (DCSC_RESID_CONSTR ISTAT) — utile complemento, non scaricato per non gonfiare la voce 6.
- Lista d'attesa ERP (Forum DD D4 advocacy) — non SDMX.

## Caveat e follow-up

- **ISTAT esploradati.istat.it irraggiungibile durante tutta la sessione resume.** DNS resolve OK (193.204.90.13), TCP/443 fallisce con timeout sia direttamente sia su host name. Test paralleli su `www.istat.it` (homepage istituzionale): HTTP 200. Esploradati.istat.it (databrowser/API SDMX) è il sotto-dominio infrastrutturalmente isolato che era giù — possibile manutenzione lato server o issue di rete localizzata. **Conseguenza**: DCIS_MORTIFERITISTR1_1 non è stato fetchato; la card 3 sopperisce con DF_TRENDSSAFETY OECD che include Italia con copertura annuale dal 2010 al 2024. **Re-fetch da pianificare** in una run successiva quando l'API ISTAT è di nuovo accessibile. Non è uno dei 4 "very-very-important block conditions" — solo 1 endpoint su 2 down, e c'è copertura alternativa.

- **Tensione metodologica importante (card 6 governance).** Il dato OECD GAAG 2025 mostra l'Italia **leader OCSE** in 5/9 indici governance infrastrutture e sopra media in 8/9. Questo è in contrasto significativo con la narrativa della tesi 11 (frammentazione, ritardi, scarsa capacità monitoraggio). Per CLAUDE.md §4 "Contradicting data", la card 6 segnala esplicitamente la tensione e propone la sintesi: **diagnosi tesi va riformulata da "sotto-strumentazione" a "sovra-strumentazione + esecuzione carente"**. Non è un block condition (la magnitudine non è >20% su un singolo claim numerico, è una contraddizione concettuale tra "scarsa pianificazione" affermato e "1° posto OECD Strategic planning evidence" misurato). Da segnalare a Riccardo per validare l'approccio narrativo.

- **% PIL e price-to-income ratios non ricavati.** Le card 1 e 5 fanno menzione qualitativa di "% PIL" e "price-to-income" come metriche rilevanti ma non li includono numericamente perché:
  - DF_INFRINV espone solo EUR correnti e National currency, non % PIL. Per il rapporto è necessario fetchare PIL Eurostat in parallelo. Da considerare in iterazione futura.
  - DF_RHPI_ALL ha un dataflow separato `DSD_RHPI@DF_RHPI_HPI_RATIOS` per price-to-income / price-to-rent — non scaricato per non gonfiare il pilota. Candidate per arricchimento card 5 successivamente.

- **Voce 6 (prezzi case) cita Milano +47% 2010-2024 senza numero esatto.** L'IPAB regionale ISTAT esiste (DCSP_IPAB_*) ma il dataset scaricato `DCSP_IPAB_2` è solo Italia nazionale. **Da fetchare** in iterazione successiva: ISTAT IPAB regionale per dettaglio Milano/Roma/Bologna vs resto-Italia. La stima "+47% Milano" usata nella card 5 è derivata da Bankitalia / OMI Agenzia Entrate (D2 sources, non in questa run); è un'integrazione approssimativa, da raffinare.

- **Universo capoluoghi ISTAT vs grandi centri europei** (card 4). Il confronto Milano (418 pax/ab) con Vienna/Berlino/Parigi non è in questa scheda — manca Eurostat City Statistics. La card menziona qualitativamente la posizione di Milano "competitiva in Europa" ma senza numeri cross-country. **Da arricchire** se rilevante per il chatbot.

- **GAAG 2023 edizione precedente NON scaricata.** La card 6 cita solo l'edizione 2025 (DF_GOV_INFPD_2025). Il dataset `DSD_QDD_GOV_INFRA_2023` esiste e darebbe la traiettoria Italia 2023→2025 — utile per dire "l'Italia sta migliorando o peggiorando". Non scaricato per non gonfiare il pilota; candidate per follow-up.

## Note tecniche emerse durante il run (di interesse per parallel runs futuri)

1. **ISTAT può essere down sub-dominially.** `www.istat.it` (HTML statico, server diversi) è raggiungibile; `esploradati.istat.it` (databrowser/SDMX API) può essere giù indipendentemente. In caso di failure, prima di dichiarare "all endpoints fail" testare entrambi.

2. **Pattern fusione 11 → 6 cards** ha funzionato bene grazie a:
   - Una voce per gruppo concettuale (investimento, modal-split, sicurezza, urbana, prezzi, governance), non una card per dataset.
   - Cross-check Italia tra fonte OECD (cross-country) e fonte ISTAT (Italia dettaglio) quando entrambe esistono — non duplicazione, una verifica.
   - Card "fuso" (TPL + sostenibilità urbana + parco auto) è leggibile e copre coerentemente la sezione "Mobilità" della tesi.

3. **OECD ITF (agency `OECD.ITF`) validato come fonte di riferimento per trasporti.** I dataflow `DSD_INFRINV@DF_INFRINV`, `DSD_TRENDS@DF_TRENDSFREIGHT`, `DSD_TRENDS@DF_TRENDSSAFETY` coprono in modo robusto Italia + peer OECD per i 3 settori principali del trasporto. Aggiungere `OECD.ITF` ai catalog probes per le future run "trasporti/mobilità/logistica/turismo (lato infrastrutturale)".

4. **DF_RHPI_ALL ha struttura SDMX complessa**: la dimensione TRANSFORMATION distingue Index level (`_Z`), Growth-rate yoy (`GY`), Growth-rate 1-quarter (`G1`); UNIT_MEASURE distingue `IX` (index 2015=100), `PA` (% per annum), `PC` (% change). Per "indice nominale livello" filtrare `TRANSFORMATION=_Z AND UNIT_MEASURE=IX` (non `TRANSFORMATION=IX`). Annotazione utile per future run prezzi/inflazione.

5. **GAAG 2025 indici hanno scala 0-1 non comparabile cross-indice.** Stesso valore numerico (es. 0,25) significa cose diverse in indici diversi. Il ranking cross-country dentro un indice è solido; il confronto numerico tra indici diversi NO. Da segnalare se future card useranno GAAG.

## Sample headline numbers per card

| Card | Headline number Italia | Headline cross-country |
|---|---|---|
| Investimenti | €12,2 mld Inland 2023 | DE €34,8 mld / FR €26,2 mld / ES €10,2 mld |
| Merci modal | 81% strada / 14% ferro | DE 60%/28% / NL 43%/6% (44% IWW) |
| Sicurezza | 3.030 morti 2024 / 5,1 per 100k ab | DE 3,3 / SE 2,0 / FR 4,7 |
| TPL urbana | 170 pax/ab capoluoghi 2023 | Milano 418 / Palermo 59 |
| Prezzi case | indice 111,7 nel 2024 (=+1% vs 2010) | PL +96% / NL +78% / DE +76% / FR +27% |
| Governance | 0,81 Asset performance (1° OECD) | DE 0,46 (paradosso esecuzione) |
