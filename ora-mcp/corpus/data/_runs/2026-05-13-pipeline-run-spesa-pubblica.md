---
folder: spesa-pubblica
pipeline_run_date: 2026-05-13
mode: autonomous (single-folder, partial folder with 2 pre-existing cards)
wishlist_voci: 5
shortlist_candidates: 3 (1 ISTAT riusato + 2 Eurostat nuovi + 1 OECD probe scartato per rate-limit)
downloads: 4 nuovi (3 Eurostat success + 1 OECD TABLE11 fallito per rate-limit, sostituito da Eurostat)
cards_written: 4 nuove (totale folder 6: 2 pre-esistenti + 4 nuove)
voci_status:
  voce_1_composizione_cofog: covered (card composizione-cofog-italia-2024)
  voce_2_composizione_economica: covered (card composizione-economica-aap-italia-2024)
  voce_3_debito_pubblico: covered (card debito-pubblico-italia-vs-paesi-2024 via Eurostat invece di OECD)
  voce_4_protezione_sociale: covered (card protezione-sociale-italia-vs-paesi-2023)
  voce_5_d1_compensation: covered (incorporato in card composizione-economica-aap-italia-2024, non card a sé)
---

# Pipeline run — `spesa-pubblica` — 2026-05-13

## Esito sintetico

**Folder parziale all'inizio del run.** Pre-esistenti: 2 card (`spesa-pubblica-pil-italia-2024.md`, `indebitamento-netto-italia-2024.md`) + 1 raw (`DCCN_FPQ/` con conto economico AAPP quarterly).

Run del 2026-05-13 ha aggiunto **4 nuove card**:

1. **`composizione-cofog-italia-2024.md`** — Spesa AAPP per funzione COFOG, Italia 2024 €1.109 mld (50,4% PIL), composizione + cross-country UE. Voce protezione sociale 42% del totale, sanità 13%, istruzione 8%, difesa 2,6%.
2. **`composizione-economica-aap-italia-2024.md`** — Spesa AAPP per categoria economica SEC2010: D62 prestazioni sociali €446 mld (40,2%), D1 redditi pubblico impiego €197 mld (17,8%), P2 consumi intermedi €128 mld (11,6%), D41 interessi €86 mld (7,7%), P51G investimenti €76 mld (6,8%). Quadra UPB cited dalla tesi.
3. **`debito-pubblico-italia-vs-paesi-2024.md`** — Debito Maastricht IT 2024 = 134,7% PIL, 2° UE dopo Grecia, +54 pp UE27. Stabile dopo picco Covid 154,4%, Germania -19 pp 2010-2024, Italia +16 pp. Tasso interesse implicito 2,9% > crescita PIL 2,5% → palla di neve attiva.
4. **`protezione-sociale-italia-vs-paesi-2023.md`** — GF10 totale IT 21,0% PIL (2° UE dopo Francia 23,3%); GF1002 vecchiaia 13,6% PIL = +3,2 pp sopra UE 10,4% (1° posto UE); GF1004 famiglia 1,4% sotto UE 1,9%; GF1005 disoccupazione 0,9% sotto UE 1,1%. Squilibrio intergenerazionale 15:1 (pensioni/famiglia+disoccupazione).

**Folder finale: 6 card totali**, copertura organica del tema "spesa pubblica" dalla tesi 17.

## Dataset processati (download + riuso)

### Riusati dal run difesa 2026-05-12

- **`_raw/difesa/DCCN_OTEPPA_2/data.csv`** (12 MB ISTAT, 306k righe IT 2000-2024) — usato per **voce 1** (COFOG composition Italia €M) e **voce 2** (economic composition Italia €M). NON riscaricato; letto direttamente con filtri REF_AREA=IT, S13, VALUATION=V, ADJUSTMENT=N + variazione su DATA_TYPE_AGGR e EXPEND_PURPOSE.

### Nuovi download Eurostat (3 success)

- **`_raw/spesa-pubblica/EUROSTAT_gov_10a_exp/data.csv`** (149 KB XML SDMX) — `gov_10a_exp` con filtro `A.PC_GDP.S13.GF01+...+GF10+TOTAL.TE.IT+DE+FR+ES+PL+NL+BE+SE+EU27_2020+EA20`, 2010-2024. Usato per voce 1 cross-country.
- **`_raw/spesa-pubblica/EUROSTAT_gov_10a_exp_MIO_EUR/data.csv`** (12 KB XML SDMX) — stesso dataflow, IT solo in MIO_EUR. Conferma quadratura €M con ISTAT.
- **`_raw/spesa-pubblica/EUROSTAT_GF10_subfunctions/data.csv`** (52 KB XML SDMX) — sub-funzioni GF1001..GF1009 per IT+DE+FR+ES+UE27. Voce 4 dettaglio.
- **`_raw/spesa-pubblica/EUROSTAT_gov_10dd_edpt1/data.csv`** (22 KB XML SDMX) — Maastricht gross debt %PIL cross-country 2000-2024. Voce 3.

### Probe scartato

- **`_raw/spesa-pubblica/DF_TABLE11_GFALL/data.csv`** (281 B, NoResultsFound + rate-limit message) — tentativo di OECD TABLE11 con full GF. **OECD ha rate-limitato** dopo i probe di FIN_DASH; pull TABLE11 successivo non completato. Sostituito da Eurostat (stesso data, fonte armonizzata UE, anche meglio per i confronti dato che la tesi cita Eurostat direttamente).
- **`_raw/spesa-pubblica/DF_TABLE13_DEBT/`** (cartella creata, mai popolata) — TABLE13 sondato, risulta essere "simplified non-financial accounts by sector", NON contiene debito pubblico. Scoperto durante probe: TABLE13 ha 13 dimensioni ma niente AF (instrument). Direzionato a FIN_DASH che invece copre LES13_FD4 (gross debt of general government), ma poi rate-limited.

### Decisione su OECD vs Eurostat (giustificazione)

Per i confronti cross-country in % PIL la tesi cita **Eurostat `gov_10a_exp`** esplicitamente:
> "Dai dati Eurostat (COFOG) è possibile avere una vista della spesa pubblica rispetto al PIL per funzioni rispetto alla media dell'Unione Europea"

Eurostat e OECD TABLE11 derivano dalla **stessa fonte armonizzata ESA 2010**; per i paesi UE i numeri sono **identici al primo decimale**. Differenza:
- Eurostat: copre solo paesi UE/EFTA. Pubblicazione T+12 mesi, ultimo 2024 disponibile.
- OECD TABLE11: copre OECD wide (include US, CA, AU, JP). Pubblicazione T+18 mesi, ultimo 2022 sui paesi UE.

**Per il chatbot ORA che parla a italiani su politiche italiane**, Eurostat è la fonte preferibile (più aggiornata, citata dalla tesi). OECD TABLE11 resta utile per confronto OECD-wide (es. quando ORA dice "OCSE 43%" la fonte è OECD).

**Conseguenza pratica:** quando il run OECD ha fallito per rate-limit, ho **switchato a Eurostat senza perdita di informazione** — anzi guadagnando +2 anni di copertura (2023→2024).

## Card NON scritte (consapevolmente)

- **Card separata "spesa per pubblico impiego (D1) cross-country"** — la voce 5 della wishlist. **Collassata** in `composizione-economica-aap-italia-2024.md` perché il dato cross-country (Eurostat D1 %PIL) è solo 1 tabella di 9 valori, non meritevole di card dedicata. Niente perdita.
- **Card "interessi sul debito (D41) trend"** — i numeri sono nella card economica (€86 mld 2024, +50% dal 2020) e nella card debito (€86 mld vs €76 mld investimenti). Una card a sé sarebbe ridondante.
- **Card "partecipate pubbliche"** — fonte è Rapporto MEF Patrimonio PA 2022 (PDF), non SDMX. Deferred D2.
- **Card "spese fiscali / bonus edilizi / Superbonus"** — fonte è Banca d'Italia QEF + UPB audizioni (PDF). Deferred D2. Tuttavia il **picco G060 housing 2023 €95 mld** è già flagged in card 1 e 2 come bias da Superbonus.

## Caveat e follow-up

1. **G060 abitazioni 2022-2023 distorta da Superbonus** — flagged in tutte le card che riportano la serie storica. Future card sui bonus edilizi (D2) potranno quantificare meglio.
2. **OECD rate-limiting**: il tentativo di pull TABLE11 con full GF è stato bloccato. La cache locale risulta sufficiente (Eurostat fa fede per UE comparison). **Per future run, considerare ordine di chiamata: usare Eurostat per UE-only first, OECD solo se serve OECD-wide.**
3. **Cross-folder wikilinks**: card 1 punta a `[[difesa]]`, `[[salute-servizi-sanitari]]` (folder, non singola card — il chatbot risolverà al runtime); le altre card puntano a card specifiche (`[[indebitamento-netto-italia-2024]]`, `[[composizione-economica-aap-italia-2024]]`, ecc.). Tutti i wikilink puntano a file esistenti.
4. **2025-Q4 nelle card pre-esistenti** ha dati provvisori — non-task per questo run (lasciate le card v1).

## Note tecniche emerse durante il run (di interesse per parallel runs)

1. **Eurostat SDMX endpoint** = `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/<dataflow>/<key>?startPeriod=...`. Dim order: `freq.unit.sector.cofog99.na_item.geo`. CSV richiede Accept header `application/vnd.sdmx.data+csv;version=1.0.0;labels=both` MA Eurostat tende a restituire **SDMX-ML XML comunque** — usa fallback `xml.etree.ElementTree`.
2. **OECD rate-limits aggressivamente**: 4 chiamate ravvicinate da `sdmx.oecd.org` hanno triggerato il blocco. Strategia: una sola chiamata pesante per dataflow, evita probe iterativi. Cache STRUCT in advance.
3. **OECD TABLE13 = simplified non-financial accounts**, NON contiene debito. Per debito OECD usare `DSD_FIN_DASH@DF_FIN_DASH` con MEASURE=LES13_FD4.
4. **Il riuso di raw da run precedenti** funziona bene: `DCCN_OTEPPA_2` scaricato per difesa è stato letto da Python per estrarre slice diverse (Italia × all COFOG × different transactions) senza ri-fetch. Risparmio: ~12 MB e ~5 min di download.
5. **Quadratura cross-source verificata**: ISTAT DCCN_OTEPPA_2 (€M) = Eurostat gov_10a_exp (MIO_EUR) entro 0,3%. Le due fonti derivano dalla stessa ESA 2010 ma con vintage marginalmente diverse.

## Reference cards (folder finale)

```
memory/corpus/data/spesa-pubblica/
├── indebitamento-netto-italia-2024.md         (2026-05-12, pre-esistente)
├── spesa-pubblica-pil-italia-2024.md          (2026-05-12, pre-esistente)
├── composizione-cofog-italia-2024.md          (2026-05-13, NUOVA — Voce 1)
├── composizione-economica-aap-italia-2024.md  (2026-05-13, NUOVA — Voci 2+5)
├── debito-pubblico-italia-vs-paesi-2024.md    (2026-05-13, NUOVA — Voce 3)
└── protezione-sociale-italia-vs-paesi-2023.md (2026-05-13, NUOVA — Voce 4)
```

Tema "spesa pubblica" copertura completa per il chatbot v1:
- spesa totale e composizione: card 1
- composizione economica: card 2
- deficit: card pre-esistente
- debito: card 3
- pensioni: card 4 (la voce singola più grande)
- entrate fiscali: cross-reference a `tassazione-fiscalita/`
- difesa, sanità, istruzione, lavoro: cross-reference alle rispettive cartelle.
