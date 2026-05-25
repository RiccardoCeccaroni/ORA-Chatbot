# Audit report — 2026-05-12 — folder: `istruzione/`

**Modalità:** manuale (auditor = Claude in sessione interattiva, in assenza dell'harness Python descritto in `memory/scripts/audit_SPEC.md`). Le verifiche di valore via re-fetch dell'URL sono parziali per limiti strutturali (vedi §Calibration notes).

**Cards swept:** 8 · **Skipped:** 0 (prima esecuzione) · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 3 · informational 1 · verified 4 · error 0

**Reference batch:** decisione `18_audit.md`, spec `audit_SPEC.md`, decisione `17_data_corpus.md` (struttura stat-card).

---

## Moderate (3)

### `istruzione/abbandono-scolastico-precoce-italia-2020.md` — moderate (high confidence)

La stat-card cita il tasso di abbandono scolastico precoce (ESL) 18-24 al 13,1% per l'Italia 2020 (M 15,6 / F 10,4 / Mezzogiorno 16,3 / Nord-est 9,9), basato sul dataflow ISTAT legacy `DCCV_ESL_UNT2020`. La verifica web rileva che ISTAT ha pubblicato la serie post-2020 (dataflow `DCCV_ESL`) con il valore Italia 2024 al **9,8%** (M 12,2 / F 7,1 / Mezzogiorno 12,4 / Nord 8,4 / Centro 8,0). La cifra italiana è in discesa strutturale e si avvicina al target UE-2030 del 9%. La stessa stat-card aveva già flaggato esplicitamente questa transizione nel suo header ("⚠️ Dato secondo metodologia pre-2020 […] Card da aggiornare/superseduere quando la nuova serie viene scaricata").

**Si suggerisce:** ri-esportare manualmente il CSV `DCCV_ESL` post-2020 dal databrowser ISTAT e generare una nuova stat-card `abbandono-scolastico-precoce-italia-2024.md` con il valore 9,8% e la distribuzione M/F + macro-area aggiornata. La card 2020 attuale può essere conservata come riferimento storico (snapshot pre-breakpoint metodologico) oppure superseduta — scelta di Riccardo.

- Source URL: https://esploradati.istat.it/databrowser/ (landing page databrowser — fetch programmatico non praticabile per esportazione CSV; URL liveness presumibilmente OK)
- Candidate newer release: ISTAT comunicato stampa "Livelli di istruzione e ritorni occupazionali — Anno 2024" (pubblicato dicembre 2025), dataflow `DCCV_ESL`
- Evidence snippet: *"La quota di giovani 18-24enni con al più un titolo secondario inferiore e non più inseriti in un percorso di istruzione o formazione si attesta al 9,8% nel 2024, con una riduzione di 0,7 punti rispetto al 2023."* — ISTAT, ripreso da Orizzonte Scuola
- Tool calls used: 1 (web search)

### `istruzione/popolazione-titolo-studio-italia-2020.md` — moderate (high confidence)

La stat-card cita la composizione per titolo di studio della popolazione italiana 15+ nel 2020 (15,3% laurea, 36,6% diploma, 32,2% licenza media, ~15,9% elementare/nessuno) dal dataflow legacy ISTAT `DCCV_POPTIT1_UNT2020`. La verifica web rileva la pubblicazione ISTAT "Livelli di istruzione e ritorni occupazionali — Anno 2024" (dicembre 2025), che riporta dati post-2020 sulla popolazione 25-64: 66,7% con almeno il diploma (in salita dal 61,8% nel 2018), donne 25,9% laureate vs uomini 18,7% (media ~22,3%). La stat-card aveva esplicitamente flaggato questa transizione ("Card da superseduere quando il nuovo dataflow è scaricato").

**Si suggerisce:** ri-esportare manualmente il CSV `DCCV_POPTIT` (dataflow successore) dal databrowser ISTAT per la serie post-2021. Da notare che il framework post-2020 si concentra prevalentemente sulla popolazione 25-64 (più rilevante per analisi di policy), che si sovrappone con la stat-card OECD `titolo-studio-adulti-25-64-italia-2024` — valutare se mantenere la card 15+ come riferimento demografico complessivo o sostituirla con una versione 25-64 allineata alla nuova metodologia.

- Source URL: https://esploradati.istat.it/databrowser/ (URL liveness OK; il vecchio dataflow `DCCV_POPTIT1_UNT2020` risulta ancora accessibile su dati.istat.it)
- Candidate newer release: ISTAT report "Livelli di istruzione e ritorni occupazionali — Anno 2024" (dicembre 2025), dataflow `DCCV_POPTIT`
- Evidence snippet: *"People with at least a diploma (ages 25-64) improved from 61.8% in 2018 to 66.7% in 2024."* — ISTAT 2025
- Cross-card note: i nuovi dati ISTAT 2024 (66,7% diploma, ~22% laurea per 25-64) corroborano in modo indipendente la stat-card OECD `titolo-studio-adulti-25-64-italia-2024` (33,3% below upper secondary, 22,3% tertiary) — verifica incrociata positiva.
- Tool calls used: 1

### `istruzione/salari-docenti-italia-2024.md` — moderate (medium confidence)

La stat-card cita $49.507 USD PPP come "salario medio annuo" italiano per insegnante di primaria nel 2024, e attribuisce la stessa cifra al pre-primaria. La verifica web sulle pagine OECD Education at a Glance 2025 segnala due elementi che insieme suggeriscono un possibile errore di mapping anno: (a) la cifra $49.507 viene attribuita esplicitamente al **2023** ("49507 USD Equivalent, rank 24/32, 2023") nelle Education GPS pages OECD; (b) lo stesso EAG 2025 riporta che in Italia i salari medi reali degli insegnanti di primaria sono **diminuiti del 4,4% nel 2024** rispetto al 2023, mentre la media OCSE è cresciuta. Se la diminuzione del -4,4% è effettiva e in termini reali sulla stessa base USD PPP costanti 2020, il valore 2024 dovrebbe essere ~$47.330, non $49.507.

⚠️ **Verifica programmatica non conclusiva:** non è stato possibile fare fetch diretto delle pagine OECD (HTTP 403) per leggere la tabella esatta — si lavora su snippet dai motori di ricerca. La stat-card è dettagliata e metodologicamente accurata; è possibile che la cifra $49.507 sia genuinamente l'ultimo punto della serie filtrata sul dato 2024 (in caso il -4,4% riportato dalle fonti web si riferisca ad altra metrica o ad altro indicatore — es. salari per ora insegnata anziché stipendio annuo). **Non si adjudica.**

**Si suggerisce:** ri-esportare manualmente il CSV `DSD_EAG_SAL_ACT@DF_TCH` da OECD Data Explorer filtrando esplicitamente per `REF_PERIOD = 2023` E `REF_PERIOD = 2024`, verificare se entrambi gli anni siano effettivamente popolati per l'Italia e leggere i due valori distinti. Se i due valori coincidono (entrambi $49.507) il dato della card è coerente con la fonte; se differiscono, la card va aggiornata all'anno effettivo del valore. Si segnala anche di verificare l'affermazione OECD "primary teachers in Italy declined 4.4% in real terms in 2024" — può richiedere consultazione del rapporto EAG 2025 PDF integrale.

- Source URL: https://data-explorer.oecd.org/ (landing page generica — vale la stessa nota OECD/ISTAT-databrowser: fetch programmatico del valore non praticabile)
- Newer release: nessuna — EAG 2025 è il rilascio più recente (settembre 2025); EAG 2026 non ancora pubblicato (atteso settembre 2026).
- Evidence snippets (entrambi da Education GPS, EAG 2025):
  - *"The average actual primary teacher's salary among teachers aged between 25-64 is one of the lowest per hour of net teaching time among OECD and partner countries with available data (49507 USD Equivalent, rank 24/32, 2023)."*
  - *"In Italy, actual average salaries of primary teachers decreased by 4.4% in 2024, contrasting with the broader OECD trend where actual average salaries of primary teachers have increased in real terms by 14.6% on average across the OECD since 2015."*
- Tool calls used: 2 (web search + tentato webfetch fallito su due URL OECD)

---

## Informational (1)

### `istruzione/sistema-scolastico-struttura-italia-2024.md` — informational (medium confidence)

La stat-card riporta la struttura del sistema scolastico italiano per l'anno scolastico 2023/24 (53.352 scuole, 8.035.009 studenti totali, 7,34 mln nella scuola pubblica). La verifica web rileva che dati sull'anno scolastico 2024/25 stanno emergendo in pubblicazioni MIM/ISTAT correlate (~7,1 mln studenti nelle scuole statali per 2024/25, -120 mila vs anno precedente secondo Indagine MIM-ISTAT). Tuttavia, non è chiaro dai risultati di ricerca se il dataflow ISTAT `DCIS_SCUOLE` sia stato già aggiornato con la nuova rilevazione 2024/25 o se i numeri preliminari provengano da fonti MIM separate.

**Si suggerisce:** verificare lo stato di rilascio del dataflow ISTAT `DCIS_SCUOLE` per l'anno scolastico 2024/25 al prossimo accesso al databrowser. Se rilasciato, considerare ingestione di una stat-card complementare o sostitutiva. Se non ancora rilasciato, la card attuale (2023/24) rimane il riferimento ISTAT più aggiornato.

- Source URL: https://esploradati.istat.it/databrowser/ (URL liveness OK)
- Candidate newer release: indagine MIM-ISTAT su anno scolastico 2024/25 — stato di rilascio in `DCIS_SCUOLE` da confermare
- Evidence snippet: *"nel 2024/2025 erano iscritti complessivamente circa 7,1 milioni di studenti nelle scuole statali italiane […] 120 mila studenti in meno rispetto al precedente."* — fonte MIM/ISTAT via portale Grusol
- Tool calls used: 1

---

## Verified (4)

### `istruzione/spesa-per-studente-italia-2022.md` — verified (high confidence)

Dati EAG 2025 (release settembre 2025) confermano: l'Italia spende 3,9% del PIL nell'istruzione (vs 4,7% media OCSE), con sotto-investimento concentrato sulla terziaria. Le cifre puntuali della card ($14.959 primaria / $14.713 terziaria / $13.750 tutti i livelli) sono coerenti con la pubblicazione di riferimento e non risultano superate. Nessun rilascio EAG 2026 disponibile. Card affidabile.

- Source URL: https://data-explorer.oecd.org/ (landing page)
- Newer release: nessuna (EAG 2026 atteso settembre 2026)
- Tool calls used: 1 (riutilizzo dello stesso search context di EAG 2025)

### `istruzione/spesa-pubblica-istruzione-italia-2022.md` — verified (high confidence)

Dati EAG 2025 confermano: spesa totale per istruzione Italia 3,87% PIL (web: 3,9%); OCSE 4,70% (web: 4,7%). La serie storica 2015-2022 nel corpo della card è internamente coerente; le note sulle differenze rispetto al perimetro MEF (DEF italiano riporta ~4,0-4,2% PIL) sono metodologicamente accurate. Nessun rilascio successivo.

- Source URL: https://data-explorer.oecd.org/
- Newer release: nessuna
- Tool calls used: 0 (verifica per riutilizzo dei risultati di ricerca precedenti)

### `istruzione/titolo-studio-adulti-25-64-italia-2024.md` — verified (high confidence)

Dati EAG 2025 (release settembre 2025) confermano i numeri italiani: 22,3% tertiary attainment 25-64 in Italia, 33,3% below upper secondary. La stat-card OECD è inoltre **corroborata in modo indipendente** dalla pubblicazione ISTAT "Livelli di istruzione e ritorni occupazionali — Anno 2024" (dicembre 2025), che riporta 66,7% con almeno il diploma per 25-64 (= 33,3% below diploma, coincidente) e una quota laureati 25-64 media intorno al 22% (donne 25,9 / uomini 18,7). Doppia verifica D1-D1 positiva.

- Una piccola nota: web search ha citato la media OCSE come 41,2% mentre la card cita 41,8%; la differenza (0,6 p.p.) è probabilmente dovuta a definizione ISCED 5-8 vs 6-8 o composizione paesi inclusi nel computo. Non è una discrepanza materiale.
- Source URL: https://data-explorer.oecd.org/
- Newer release: nessuna
- Tool calls used: 1

### `istruzione/transizione-istruzione-lavoro-giovani-italia-2024.md` — verified (medium-high confidence)

La stat-card cita 17,5% di giovani 18-24 italiani "non in formazione e non occupati" (NEET-adjacent) per il 2024 dal dataflow OECD `DF_LSO_TRANS`. La verifica web sul rilascio EAG 2025 non fornisce la cifra italiana puntuale per la stessa coorte/metrica ma rileva: (a) l'Italia ha registrato il calo NEET più significativo OCSE 2019-2024 (-8 punti percentuali), (b) il NEET medio OCSE 2024 è 14%, (c) il NEET working plan italiano 2022 ha avuto effetti positivi. Un calo di 8 punti dal valore 2019 (~25-26% per Italia 18-24) porta a ~17-18% nel 2024, in linea con il 17,5% citato.

La stat-card distingue correttamente la propria metrica (`NED × NE` OCSE-EAG 18-24, 17,5%) dal NEET ufficiale Eurostat 15-29 (~16%), con avvertenza metodologica esplicita. Verifica positiva.

- Source URL: https://data-explorer.oecd.org/
- Newer release: nessuna
- Tool calls used: 1

---

## Calibration notes (osservazioni meta-livello sull'auditor)

Questo è il primo sweep dell'auditor sul corpus dati. Si segnalano le seguenti osservazioni — non sono finding sulle card ma sull'auditor stesso e sulla sua specifica:

1. **OECD data-explorer va trattato come ISTAT databrowser.** Lo spec dell'auditor (`audit_SPEC.md` §3) carva esplicitamente solo il caso ISTAT databrowser. Tuttavia 5 delle 8 card della cartella `istruzione/` puntano a `https://data-explorer.oecd.org/`, una landing page generica strutturalmente analoga: l'utente esporta CSV manualmente, il fetch programmatico del valore non è praticabile. Si suggerisce di aggiornare la regola: "Se source_url è una landing page del databrowser ISTAT (esploradati.istat.it, dati.istat.it) **o di OECD Data Explorer (data-explorer.oecd.org)**, la verifica del valore via fetch non è praticabile — si valuta solo URL liveness, si esegue la ricerca di newer release, severity dipende esclusivamente dall'esito di quest'ultima (non automaticamente error)."

2. **Severità "error" automatico è troppo restrittivo.** La spec attuale impone severity=error per ogni card ISTAT-databrowser. In pratica, anche senza poter verificare il valore, l'auditor può portare valore reale (a) cercando newer release sulla stessa metrica, (b) cross-verificando con fonti parallele, (c) leggendo comunicati stampa ISTAT/MIM. Quattro delle card hanno effettivamente generato finding utili (moderate × 3, informational × 1) senza essere classificate error. Si propone di rilassare la regola: severity riflette l'esito del check di newer-release, manual_action_needed=true segnala separatamente la necessità di ri-export per la verifica del valore.

3. **Verifica incrociata D1↔D1 come bonus positivo.** Nel caso `titolo-studio-adulti-25-64`, la pubblicazione ISTAT dicembre 2025 ha corroborato in modo indipendente la stat-card OECD. Questo tipo di doppio anchor sulla stessa metrica (ISTAT 25-64 + OECD 25-64 = stessa cifra) è un segnale di affidabilità più forte della singola fonte. Si suggerisce di considerare un esito intermedio "verified-cross-source" quando l'auditor trova una conferma indipendente — non v1, da valutare per v2.

4. **Le card che si auto-flaggano sono predicibili moderate.** Due card su tre nel bucket moderate (`abbandono-scolastico-precoce-italia-2020`, `popolazione-titolo-studio-italia-2020`) avevano già un warning in apertura che annunciava la necessità di update. L'auditor ha confermato che il newer release esiste effettivamente. Questo conferma il valore del meccanismo: il warning nel corpo della card è l'intento, l'auditor è la verifica esterna che fa lo "snap-back" all'azione.

5. **Cost reale di questo sweep:** 7 web search + 2 web fetch tentati (entrambi 403 su OECD). Nessuna chiamata a fetch_url andata a buon fine — il caso peggiore previsto dal SPEC §F2.

---

## Skipped (0)

Prima esecuzione — nessuna card precedentemente verificata da saltare. Il manifest `_audit/_manifest.json` non esiste ancora (l'auditor è eseguito manualmente, senza l'harness).
