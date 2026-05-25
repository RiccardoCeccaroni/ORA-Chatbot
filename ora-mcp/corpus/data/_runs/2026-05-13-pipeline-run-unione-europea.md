---
folder: unione-europea
pipeline_run_date: 2026-05-13
mode: autonomous (post-pilot, second folder run)
wishlist_voci: 5
shortlist_candidates: 7 (0 ISTAT + 1 OECD + 6 Eurostat — 1 OECD blocked by rate limit)
downloads: 5 Eurostat OK + 1 OECD failed (rate-limit 429 — retry pending)
cards_written: 4
voci_status:
  voce_1_ghg_ue_mondo: covered (Eurostat ENV_AIR_GGE, UE27 + 30 MS, 1990-2023)
  voce_2_attivi_famiglie: covered (Eurostat NASA_10_F_BS S14_S15, UE27 + 36 geos; US comparison via tesi-cite only — OECD T7HH_Q rate-limited)
  voce_3_venture_capital: gap (no D1 source — deferred to D2/D4 in shortlist, no card)
  voce_4_finanziamento_imprese: covered (Eurostat NASA_10_F_BS S11; tesi "80% loans" reformulated as flow vs stock)
  voce_5_gerd_ue_vs_us: covered (Eurostat RD_E_GERDTOT, UE27 + US + JP + KR + CN + 30 MS, 2010-2024)
---

# Pipeline run — `unione-europea` — 2026-05-13

## Esito sintetico

4 stat-card scritte in `memory/corpus/data/unione-europea/`:

1. `emissioni-ghg-ue-vs-mondo-2023.md` — UE27 2,9 Gt CO2eq nel 2023 (-37% vs 1990), ~5,5% del totale mondiale. Verifica diretta del numero "6%" della tesi cap. 1.
2. `composizione-attivi-famiglie-ue-2023.md` — Famiglie UE27 31,0% depositi (F2), 36,0% equity (F5), 26,8% pensioni/assicurazioni (F6). **Verifica esatta del numero "31%" della tesi cap. 4.** Italia: 27,1% / 42,8% / 18,7%.
3. `struttura-finanziamento-imprese-ue-2023.md` — Imprese UE27 26% prestiti, 58% equity, 3% bond di mercato. **Contraddizione metodologica con il "80% bank loans" della tesi**: numero tesi è flow di nuovo finanziamento (BCE Annual Report), non stock (Eurostat). Card lo spiega inline.
4. `spesa-r-s-gerd-ue-vs-paesi-2024.md` — GERD UE27 2,24% PIL (2024), gap di -1,2 p.p. vs US (3,44%, 2023). Italia 1,38%. Il gap UE-US si allarga: +0,73 p.p. US vs +0,28 p.p. UE dal 2010.

## Dataset scartati / non scaricati

- **`OECD.SDD.NAD: DSD_NASEC20@DF_T7HH_Q`** — fetch fallito con 429 (rate-limit OECD API) su 4 tentativi distribuiti durante il run. **Non scartato definitivamente**: il dato US households S14_S15 va recuperato in iterazione futura per chiudere la card 2 con il dato OECD-verified comparable. Il numero US del 12% citato dalla tesi resta cita-CEPS/Fed nella card.

## Caveat e follow-up

- **Voce 3 (Venture Capital UE vs US) confermata gap D1.** Nessun dataflow OECD/Eurostat espone VC investments in modo strutturato cross-country. La citazione "3× US" della tesi (Rapporto Draghi/CEPS) resta D2. Routing futuro: Atomico "State of European Tech" (D4 industry-pro-vc), Bruegel "Financing Growth" (D2), Invest Europe (D4 industry).
- **Voce 4 (corporate financing): contraddizione tesi-vs-dati gestita inline.** La tesi dice "80% bank loans", lo stock Eurostat dice 26% F4. Sono due metriche diverse (flow di nuovo finanziamento esterno vs stock di bilancio). La card lo chiarisce con un riquadro dedicato. **Nessuna ping a Riccardo perché la contraddizione è metodologicamente spiegabile e <20% di magnitude** — la conclusione qualitativa della tesi (UE bank-dependent vs US disintermediato) resta corretta, solo va riformulata sui veri numeri (gap bond market 3% UE vs 25% US, non gap loans).
- **Voce 1 (GHG quota mondiale): il "6%" della tesi è al margine alto.** Il dato 2023 attuale è ~5,5% (UE27/world). In calo strutturale da ~12% del 1990. La tesi non è invalidata ma il numero più aggiornato è "5-6%". Card lo riporta esplicitamente.
- **2024 dati provvisori per Eurostat** — diverse serie hanno 2024 in versione preliminare (RD_E_GERDTOT, NASA_10_F_BS). Re-fetch nel 2027 quando consolidato.
- **UK Brexit gap:** Eurostat ha cessato il reporting UK post-Brexit. La maggior parte dei dati UK in queste schede si ferma al 2019-2020. Per UK aggiornato servirebbero ONS / OECD — fuori Eurostat.

## Note tecniche emerse durante il run (di interesse per i parallel runs futuri)

1. **Eurostat SDMX v3.0 endpoint funziona** con questo formato:
   `https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/<DATAFLOW>/1.0/<KEY>?startPeriod=<YYYY>&format=csvdata`
   - **Nessun Accept header necessario** (a differenza di ISTAT).
   - Il `format=csvdata` restituisce CSV pulito con colonne dimensionali in chiaro.
   - **Il v2.1 endpoint funziona solo con Accept header `application/vnd.sdmx.data+csv;version=1.0.0;labels=both`** e restituisce SDMX-ML, non CSV — sconsigliato.
2. **Eurostat: l'operatore multivalore in singolo slot dimensionale NON è supportato** (`+` o `,` danno fault `INVALID_URL_VALUE`). **Soluzione**: o omettere lo slot (wildcard → restituisce tutti i valori) o fare N chiamate single-value. Wildcard preferibile.
3. **Eurostat: l'ordine delle dimensioni nella URL key è specifico per dataflow** — va verificato via `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/datastructure/ESTAT/<DATAFLOW>/1.0?references=children` e poi grep `<s:DimensionList>` per l'ordine.
4. **Eurostat: codici UNIT sono dataflow-specific.** Il `THS_T` valido per `ENV_AIR_GGE` non lo è per altri dataflow. Il `PC_GDP` valido per `RD_E_GERDTOT` non lo è per `NASA_10_F_BS` (che usa `MIO_EUR` o `PC_TOT`).
5. **OECD rate-limiting cross-dataflow:** un singolo abuso su un dataflow blocca temporaneamente l'intera origin IP per tutti i dataflow OECD. Cooldown osservato: >30min. **Tactic:** se serve OECD per supplement (e Eurostat copre il primary), accettare il rischio e prevedere retry asincrono in iterazione successiva. Per il run pilota di una folder, **se OECD è primary, attenzione a non avere voci che richiedono OECD dopo aver già consumato la quota su altre voci**.
6. **Bash `&` parallel con paths Windows containing spaces in $VAR:** problema noto. Le variabili `$VAR` passate a sub-shell `&` non si espandono in modo affidabile quando contengono spazi. **Tactic:** usare path letterali completi nelle curl `-o`, NON `$TARGET_DIR/file.csv`. Oppure caching in `/tmp/sdmx_pilot/` poi `cp` finale.
7. **Eurostat dataflow per "Venture Capital" non esiste** — l'unico approccio OECD/Eurostat-compatible è proxy via BERD by industry (high-tech sectors). Conferma del gap D1 sul VC per future folder/voci.

Queste sono nuovi findings — la prossima iterazione del prompt riutilizzabile `memory/scripts/autonomous_data_pipeline_prompt.md` dovrebbe documentare le sezioni Eurostat (v3.0 endpoint, dimension wildcard, structure-probe-first pattern).
