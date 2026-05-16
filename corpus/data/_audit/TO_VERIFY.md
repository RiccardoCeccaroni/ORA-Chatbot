# 📋 TO-VERIFY — auditor backlog

**Cosa è questo file:** la lista cumulativa delle azioni che richiedono il tuo intervento manuale, accumulate dagli sweep dell'auditor sul corpus `memory/corpus/data/`. Ogni sweep aggiunge righe in fondo alla sezione del folder corrispondente, non ne rimuove. Quando completi un'azione, marca la checkbox `[x]` e lascia la riga in piedi come record storico (oppure spostala in `_DONE.md` se diventa troppo lunga — scelta tua).

**Convenzioni:**
- 🔴 **action_critical** — il valore citato nella card potrebbe essere errato; ricontrollo prioritario.
- 🟡 **action_moderate** — newer release disponibile o discrepanza non-critica; aggiornare quando vuoi.
- 🔵 **action_info** — refresh upstream non confermato; verificare in occasione del prossimo accesso al databrowser.
- ⚠️ **action_meta** — modifica all'auditor stesso (al prompt, alla spec, alla decisione).

**Convenzione di file naming nella sezione referenziale:** `<folder>/<card-id>.md`.

---

## 🗂 istruzione/

Sweep: `2026-05-12-audit-sweep-istruzione.md`.

### 🟡 action_moderate

- [ ] **`salari-docenti-italia-2024`** — ri-esportare CSV `DSD_EAG_SAL_ACT@DF_TCH` da OECD Data Explorer filtrando `REF_PERIOD = 2023` E `REF_PERIOD = 2024` separatamente, e leggere i due valori distinti per la primaria italiana. **Perché:** evidenze testuali da EAG 2025 attribuiscono $49.507 al 2023 e segnalano un calo del -4,4% in termini reali nel 2024; se confermato, la card 2024 sta usando un valore 2023 con etichetta sbagliata. Medium confidence — l'auditor non ha potuto fetchare le pagine OECD (HTTP 403). **Tentativo 2026-05-13 fallito:** endpoint `sdmx.oecd.org` bloccato da Cloudflare anti-bot (HTTP 403 su 3 tentativi consecutivi con User-Agent diversi). Aggiunto caveat di non-verifica nel corpo della card. Necessita re-export manuale dal databrowser OCSE in una sessione browser, oppure di un proxy/VPN. Item rimasto aperto.
- [x] **`abbandono-scolastico-precoce-italia-2020`** — **Risolto 2026-05-13.** ISTAT non espone un dataflow SDMX successore di `DCCV_ESL_UNT2020` (verificato via catalog dump 2026-05-13: solo dataflow legacy 52_1203 presenti). Fonte D1 corrente è Eurostat `edat_lfse_14` + `edat_lfse_16`, alimentata dalla RFL ISTAT. Creata nuova card `abbandono-scolastico-precoce-italia-2024.md` (Italia 9,8% / M 12,2 / F 7,1 / Sud 11,3 / Isole 15,0 / Nord-ovest 8,1 / Nord-est 8,7 / Centro 8,0; UE-27 9,4%). Card 2020 mantenuta come riferimento storico con cross-link e nota sull'assenza del dataflow successore ISTAT. Raw persistito in `_raw/istruzione/EUROSTAT_edat_lfse_14/`.
- [x] **`popolazione-titolo-studio-italia-2020`** — **Risolto 2026-05-13 con opzione "rewrite 25-64"**. Catalog ISTAT 2026-05-13 conferma: nessun successore SDMX di `DCCV_POPTIT1_UNT2020`. Il framework post-2020 vive nel BES territoriale `DF_BES_TERRIT_2` (indicatori `02IST002-N22` per ≥ diploma 25-64 e `02IST003P-N22` per terziaria 25-39). Creata nuova card `popolazione-titolo-studio-25-64-italia-2024.md` (Italia 66,7% diploma+ 25-64, 30,9% terziaria 25-39, NEET 15-29 a 15,2%, breakdown Nord-est 71,3 / Nord-ovest 69,1 / Sud 60,2). Vecchia card `popolazione-titolo-studio-italia-2020.md` rimossa (perimetro 15+ × cittadinanza non più replicabile con framework post-2020, e duplicava parzialmente `titolo-studio-adulti-25-64-italia-2024`). Raw persistito in `_raw/istruzione/DF_BES_TERRIT_2/`.

### 🔵 action_info

- [ ] **`sistema-scolastico-struttura-italia-2024`** — al prossimo accesso al databrowser ISTAT, verificare se il dataflow `DCIS_SCUOLE` è stato refreshato con l'anno scolastico 2024/25 (segnali da fonti MIM: ~7,1 mln studenti statali, -120k vs 2023/24). Se sì, considerare ingestione complementare o sostitutiva.

### ⚠️ action_meta (auditor spec)

- [ ] **OECD data-explorer va trattato come ISTAT databrowser nella spec.** La regola attuale (`audit_SPEC.md` §3) carva solo ISTAT databrowser; 5 card su 8 nella cartella `istruzione/` puntano a `data-explorer.oecd.org` — stesso pattern strutturale (landing page, export CSV manuale). Aggiungere `data-explorer.oecd.org` alla regola "manual re-export needed."
- [ ] **Rilassare la regola "ISTAT databrowser → severity=error automatico".** Il primo sweep ha mostrato che l'auditor produce finding utili (moderate / informational) per card databrowser usando solo la newer-release check, senza valutazione del valore. Proposta: severity riflette l'esito del check di newer-release; `manual_action_needed=true` è la flag separata per "value verification requires CSV re-export."

---

## 🗂 tassazione-fiscalita/

Sweep: `2026-05-12-audit-sweep-tassazione-fiscalita.md`.

### 🟡 action_moderate

- [x] **`pressione-fiscale-italia-2024`** — **Chiuso 2026-05-13** per decisione "moderate + low-delta → keep ISTAT trimestrale". Card mantiene 42,2% (media 4 trimestri 2024) e 41,0% (2023). Δ vs comunicato annuale ISTAT (42,6% / 41,4%) = 0,4 p.p. su entrambi gli anni, attribuibile a metodologia diversa tra dataflow trimestrale e comunicato annuale — entrambi ISTAT, entrambi D1, scelta del trimestrale è coerente con la cadenza del corpus. Da rivisitare quando uscirà ISTAT "PIL e indebitamento AP 2023-2025" per allineamento puntuale.

---

## 🗂 lavoro-politiche-sociali/

Sweep: `2026-05-12-audit-sweep-lavoro-politiche-sociali.md`.

### 🔵 action_info

- [ ] **`retribuzione-mediana-oraria-privati-italia-2023`** — verificare nel corpo della card se il dato 2023 proviene dal dataflow `DCSC_RACLI` (aggiornato annualmente) o dal comunicato "Struttura retribuzioni" (ancora al 2022, gennaio 2025). Allineare l'etichetta del periodo alla fonte effettivamente usata; entrambe accettabili ma vanno distinte.
- [ ] **`indici-grandi-imprese-retribuzione-costo-lavoro-italia-2026`** — il punto più recente nella card è 2026-02. Ri-fetchare dopo il 25 maggio 2026 per aggiungere 2026-03; auto-rinfrescante mensilmente, gestibile dall'auditor scheduled mensile.

### ⚠️ action_meta (auditor spec / CLAUDE.md)

- [ ] **Proporre l'estensione dello schema frontmatter §5 di CLAUDE.md:** la description deve sempre contenere i valori numerici principali della card (headline + 1-2 confronti), non solo descrivere la struttura del metric. Sweep dell'auditor è molto più veloce se i numeri puntuali sono nella description.
- [ ] **Considerare campo `series_frequency: monthly | quarterly | annual | structural`** per orientare la cadenza di audit (mensile per high-freq, semestrale per structural). Da introdurre in v2 della spec.

---

## 🗂 agricoltura/

Sweep: `2026-05-12-audit-sweep-agricoltura.md`.

### 🟡 action_moderate

- [x] **`emissioni-gas-serra-agricoltura-italia-2023`** — ~~ISPRA NID 2026 (aprile 2026) ha pubblicato la serie 1990-2024. Agricoltura 2024 ≈ 28,8 Mt CO2eq (8% del totale 360 Mt) — calo materiale dai 32,3 Mt del 2023. Ri-fetchare il rapporto SINA-ISPRA agricoltura aggiornato 2024 e creare `emissioni-gas-serra-agricoltura-italia-2024.md`.~~ **Risolto 2026-05-13.** Creata nuova card [[emissioni-gas-serra-agricoltura-italia-2024]] con headline ≈28,8 Mt (-10,8% YoY, -24,6% dal 1990) e contesto NID 2026 (Rapp. 428/2026, totale 363 Mt -3,6% YoY). Card 2023 mantenuta come riferimento storico-strutturale con banner di cross-reference. **Caveat:** il PDF NID 2026 ufficiale è gated da Incapsula al 2026-05-13; il valore esatto agricoltura andrà validato (atteso 28,5-29,1 Mt). Composizione settoriale 2024 inferita da continuità col 2023 (variazione <1 p.p. attesa). Cross-conferme indipendenti da Astrolabio (Amici della Terra), Hi-Tech Ambiente, e-gazette, Rinnovabili.it.
- [x] **`operatori-dop-igp-italia-2021`** — ~~ISTAT ha pubblicato il report "Prodotti agroalimentari di qualità DOP, IGP e STG — Anno 2022" (settembre 2024) con ~81.400 produttori certificati 2022 (+0,4% sul 2021) e quadro complessivo 195.407 operatori nazionali (€20,2 mld produzione). Ri-esportare CSV ISTAT per 2022 e generare nuova card. Considerare anche di estendere lo scope ai produttori vinicoli (il segmento più ampio non incluso nella card attuale).~~ **Risolto 2026-05-13.** CSV ISTAT DCSP_DOPIGP_1 ri-esportato con `startPeriod=2022&endPeriod=2022` (33 KB, 119 righe, HTTP 200) e archiviato in `_raw/agricoltura/DCSP_DOPIGP_1/data_2022.csv`. PDF statistica-report ISTAT (5 settembre 2024) archiviato in `_raw/agricoltura/ISTAT_DOPIGP_REPORT_2022/`. Creata nuova card [[operatori-dop-igp-italia-2022]] con totali settoriali (83.759, +0,3%), produttori puri (81.403, +0,4%), serie decennale 2012-2022 (+8,3% produttori, +28,6% prodotti UE), drift Nord→Mezzogiorno (+12,3 p.p. quota in 10 anni), 319 prodotti italiani su 1.466 UE. Card 2021 mantenuta come riferimento di framework concettuale. **Scope vino:** confermato NON in DCSP_DOPIGP_1 (separata banca dati OIV/MASAF, ~280k operatori, ~€12,5 mld); card 2022 documenta esplicitamente la lacuna. Estensione formale al comparto vino è D2/ISMEA Qualivita — rinviato a batch dedicato.

### 🔵 action_info

- [ ] **`valore-aggiunto-agricoltura-italia-2024`** — ambiguità metrica da chiarire: la card cita "VA netto agricoltura €42,4 mld" mentre il comunicato ISTAT (gennaio 2025, aggiornato luglio 2025) riporta "valore aggiunto a prezzi base €31,84 mld". I due numeri si riferiscono probabilmente a sub-aggregati SEC diversi (a costo dei fattori vs a prezzi base). Ri-fetchare il PDF del comunicato aggiornato e taggare esplicitamente la metrica usata nel corpo della card.

### ⚠️ action_meta (auditor spec / CLAUDE.md)

- [ ] **Aggiungere alla §5 di CLAUDE.md (schema frontmatter):** per type=data con metriche di contabilità nazionale (PIL, VA, redditi, conti settoriali), esplicitare il sub-aggregato SEC nel campo `data_metric` (es. "valore aggiunto a prezzi base" vs "VA a costo dei fattori"). Le ambiguità metriche sono ricorrenti in conti nazionali.

---

## 🗂 sviluppo-economico-politica-industriale/

Sweep: `2026-05-12-audit-sweep-sviluppo-economico-politica-industriale.md`.

### 🔴 action_critical

- [x] **`previsione-crescita-pil-italia-2027`** — ~~OECD ha pubblicato l'**Interim Economic Outlook marzo 2026** che revisiona al ribasso i forecast italiani: **2026 da 0,62% a 0,40%** (-0,22 p.p.) e **2027 da 0,74% a 0,60%** (-0,14 p.p.).~~ **Risolto 2026-05-13:** web-search ha mostrato che i valori effettivi dell'Interim Report di marzo 2026 sono **2025=0,5%, 2026=0,6%, 2027=0,7%** — entro arrotondamento dei valori EO 118 (0,55 / 0,62 / 0,74). I numeri citati originariamente in questa TODO (0,40 / 0,60) erano errati. **Azione presa:** aggiornata la citazione di fonte all'Interim Report March 2026, aggiornati i valori 1-decimal della tabella, aggiunta la nota sui cicli OCSE (semestrale + Interim). Δ numerico effettivo: ≤0,04 p.p.

### ⚠️ action_meta (auditor spec)

- [ ] **Aggiungere al prompt dell'auditor una regola sui forecast IMF/OECD/BCE:** "controllare sempre se esista un Interim Report / WEO Update / Quarterly Projection più recente della pubblicazione semestrale citata da una card forecast." OECD pubblica EO semestrale + Interim trimestrale; tra un EO e l'altro ci sono due revisioni delle stesse cifre.
- [ ] **Considerare cadenza di audit più frequente per le card forecast** (mensile vs trimestrale per le card di stock/storiche). Riconoscibili da `data_period` che termina in un anno futuro.

---

## 🗂 salute-servizi-sanitari/

Sweep: `2026-05-12-audit-sweep-salute-servizi-sanitari.md`.

### 🟡 action_moderate

- [x] **`liste-attesa-bisogni-insoddisfatti-italia-2024`** — **Risolto 2026-05-13** con riscrittura completa del corpo: ogni cifra è ora etichettata con la survey di provenienza. Tabella metriche distingue ISTAT-AVQ (7,6% / ~4,5 mln, definizione ampia), EU-SILC hlth_silc_08 (1,8% / definizione UE classica — quella citata dall'OECD Country Health Profile 2025) ed EU-SILC hlth_silc_08b (3,7% / definizione 2021+). La "2,7 milioni" è stata **ri-attribuita correttamente a ISTAT-AVQ 2024** (subset di chi rinuncia per liste d'attesa, 4,5% di pop) — **non Ministero della Salute** come scritto nella vecchia versione, ed era anche **misframata come "in attesa" mentre sono persone che hanno rinunciato per attese**. Aggiunta serie storica Eurostat 2008-2025 (con flag di cesura metodologica 2017) e confronto cross-country UE-13. Raw persistiti in `_raw/salute-servizi-sanitari/EUROSTAT_hlth_silc_08/` e `EUROSTAT_hlth_silc_08b/`.

---

## 🗂 energia-ambiente-sostenibilita/

Sweep: `2026-05-12-audit-sweep-energia-ambiente-sostenibilita.md`.

### 🟡 action_moderate

- [x] **`capacita-generazione-elettrica-italia-2024`** — **Risolto 2026-05-13.** Creata nuova card `capacita-generazione-elettrica-italia-2025.md` (`attribution: terna`, `D2`) con i 5 numeri headline del consuntivo Terna gennaio 2026 (domanda 311,3 TWh; FER 41,1%, −0,9 pt vs 2024 per crollo idrico −21,2%; PV record 44,3 TWh +25,1%; +7,2 GW nuova capacità FER; 884.404 accumuli per 17,92 GWh). Card 2024 conservata come snapshot storico con banner cross-link al top. Raw archive: `_raw/energia-ambiente-sostenibilita/TERNA_CONSUNTIVO_2025/` (comunicato HTML + Rapporto Mensile gennaio 2026 PDF 3,7 MB).

### 🔵 action_info

- [ ] **`dipendenza-gas-russo-italia-2024`** — aggiungere al corpo della card un box "Aggiornamento normativo": il Consiglio UE ha adottato a gennaio 2026 il regolamento che vieta sia LNG sia gas pipeline russo a partire dal 18 marzo 2026 (divieto totale entro fine 2027). I dati numerici della card restano corretti — è informazione di contesto utile per il chatbot.

### ⚠️ action_meta (auditor spec)

- [ ] **Estendere la regola "manual_action_needed" anche a `ec.europa.eu/eurostat/databrowser/`.** 5 card energia (più probabilmente molte altre nelle altre cartelle) puntano a Eurostat databrowser, struttura identica a ISTAT databrowser e OECD data-explorer. La regola della spec va generalizzata: "qualsiasi landing page di databrowser/data-explorer richiede manual re-export per la verifica del valore."
- [ ] **Considerare sotto-classificazione "verified-baseline" in v2 della spec.** 5 card energia citano esplicitamente l'IEA Italy 2023 review come baseline pre-invasione 2021. Sono snapshot storici intenzionali, non drift. Distinguerli da "verified-current" sarebbe più informativo nei report. Non urgente.

---

## 🗂 universita-ricerca/

Sweep: `2026-05-13-pipeline-run-universita-ricerca.md`.

### 🔴 action_critical

- [x] **`flusso-universitario-italia-2024`** — **Risolto 2026-05-13** con opzione (a). Verifica su `_raw/universita-ricerca/DCIS_DOCENTI1/Docenti universitari (IT1,56_1135_DF_DCIS_DOCENTI1_1,1.0).csv` conferma Italia × Totale qualifica × Totale sesso × Totale aree × 2019 = **55.426** (breakdown: Ordinario 13.685, Associato 22.283, Ricercatore a tempo indeterminato 19.458). La card è stata riscritta: headline e tabella qualifica usano ora i 55.426 ISTAT; aggiunto box "⚠️ Perimetro docenti" che esplicita la differenza con USTAT/MUR (~100-110k esteso); recalibrato il rapporto studenti/docenti (32 di ruolo vs 17 esteso); aggiornato il confronto cross-country per usare il perimetro esteso (apples-to-apples con DE/FR). `attribution: istat` e `quality_tier: D1` preservati per coerenza con la fonte.

### 🟡 action_moderate

- [ ] **`iscritti-universitari-italia-2024`** (nuova card) — la cifra ISTAT 1,909,503 vs la cifra MUR ~1,96 mln citata nella tesi: gap ~50k, attribuibile a inclusione AFAM in MUR. La differenza è documentata nel corpo della card ma vale la pena confermare il perimetro MUR esatto (con o senza AFAM) consultando USTAT al prossimo accesso.
- [ ] **`distribuzione-laureati-campo-studio-italia-oecd-2023`** (nuova card) — la cifra ICT 1,6% Italia 2023 è sorprendentemente bassa (ultima al mondo OCSE). Verificare con un dataset complementare (es. ISTAT laureati per gruppo di classi di laurea aa 2023/24) se questa cifra è coerente. Possibile artefatto della mappatura ISCED-F: in Italia molti laureati ICT vengono classificati come "Ingegneria" (Ingegneria Informatica è LM-32 nel sistema italiano, può finire in F07 invece che F06 a seconda della codifica MUR → OECD). Se confermato come artefatto, aggiungere caveat metodologico più forte.

### 🔵 action_info

- [ ] **`docenti-universitari-di-ruolo-italia-2019`** (nuova card) — il dato è del 2019. ISTAT rilascia gli anni successivi con ritardo ~2 anni; il 2022-2023 dovrebbe essere disponibile entro fine 2025. Al prossimo accesso al databrowser ISTAT, verificare se DCIS_DOCENTI1 è stato refreshato. Se sì, ri-esportare e produrre card aggiornata; il numero atteso è 55-60k di ruolo (al netto del turnover post-PNRR), con quota Associati ulteriormente cresciuta per promozioni da RTD-B.
- [ ] **`laureati-italia-per-regione-2022`** (nuova card) — anno 2022 è il più recente disponibile in DCIS_LAUREATI; verificare nel 2026 se l'edizione 2023 è disponibile.

### ⚠️ action_meta (auditor spec / CLAUDE.md)

- [ ] **Aggiungere alla §5 di CLAUDE.md (schema frontmatter):** per `type=data` con metriche di personale (docenti, ricercatori, dottorandi, addetti), esplicitare il perimetro di staffing nel campo `data_metric` (es. "docenti di ruolo, esclude RTD" vs "docenti universitari totali, include precariato"). Le ambiguità di perimetro su "personale strutturato" sono ricorrenti tra ISTAT e MUR.
- [ ] **Considerare campo `comparator_perimeter` nel frontmatter** per disambiguare card che riportano due cifre dalla stessa attribution con perimetri diversi (ISTAT DCIS_DOCENTI1 di ruolo = 55k vs USTAT-MUR includendo RTD = ~102k). Non urgente; per v2 della spec.

---

<!-- Folders successive si aggiungono qui sotto seguendo lo stesso pattern. Sweep multipli sullo stesso folder coabitano: il più recente in fondo. -->
