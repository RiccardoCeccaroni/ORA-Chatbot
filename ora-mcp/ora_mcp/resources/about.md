# ORA! — chi siamo

> Read this resource first when an AI assistant connects via this MCP server.
> It explains who ORA! is, what the server exposes, and how to use the tools well.

## In sintesi

**ORA!** (ex *Movimento Drin Drin*) è un partito politico italiano fondato nel
2024–2025 dall'economista **Michele Boldrin** (segretario) e dall'imprenditore
**Alberto Forchielli** (presidente). Si definisce di **centro pragmatico** —
Boldrin parla di **«estremo centro»** — con un'identità dichiaratamente
anti-ideologica, fondata sui dati. Slogan: **«Il Coraggio dell'Ovvio»**.
Sede legale: Via Cavour 104, 40026 Imola (BO). Aderenti dichiarati al lancio:
oltre 14.500.

## Cronologia essenziale

- **7 luglio 2024** — Diretta YouTube fondativa («Drin-Drin»).
- **6 settembre 2024** — Statuto del *Movimento del Drin Drin*.
- **4 luglio 2025** — Costituzione formale del partito.
- **10–12 ottobre 2025** — 1° Congresso fondativo (Abano Terme).

## Governance

- Segretario: **Michele Boldrin**.
- Presidente: **Alberto Forchielli**.
- Vicepresidente: **Marco Becattini**.
- Assemblea: 100 membri eletti al congresso fondativo.
- Comunità: gruppi tematici su Discord, *position paper* versionati su GitHub.

## Posizionamento

Centro liberal-democratico ed europeista. Concorrenza/dialogo con Azione,
Italia Viva, +Europa, PLD. Posizioni anti-establishment su spesa pubblica,
sussidi, sistema pensionistico. Esplicitamente filo-Ucraina, pro-difesa
europea integrata, pro-completamento Unione Bancaria e dei Capitali.

## I sei nodi che ORA! identifica come prioritari

1. Deficit di produttività e innovazione.
2. Welfare non sostenibile.
3. Crisi demografica e migratoria.
4. Sistema formativo inadeguato.
5. Burocrazia e giustizia paralizzanti.
6. Minacce ed emergenze internazionali.

## I quattro obiettivi dell'MCP

Questo server è progettato per supportare quattro tipi di domande:

1. **Stato (State)** — *qual è la posizione di ORA! su X?*
2. **Proiezione (Project)** — *cosa farebbe ORA! se Y?*
3. **Giustificazione (Justify)** — *su quali dati ORA! basa la posizione Z?*
4. **Confronto (Compare)** — *in cosa ORA! si differenzia da partito W?*

## Gerarchia di affidabilità del corpus

Il corpus è organizzato in **livelli di fiducia**. L'assistente AI dovrebbe
sempre rispettare questa gerarchia quando recupera e cita.

### A1 — Voce ufficiale del partito (sempre la prima scelta)

- `A1a` — **tesi** del manifesto (21 documenti, posizione canonica).
- `A1b` — **comunicati** ufficiali (eventi correnti).
- `A1c` — sezioni di **newsletter** del partito.
- `A1c-event` — distillati di eventi del partito.
- `A1-identity`, `A1-statuto`, `A1-fondamenti`, `A1-codice-etico`,
  `A1-contacts` — documenti identitari e di governance.

Quando l'utente chiede *«cosa pensa ORA! di X?»*, recuperare prima da A1.
Attribution value nel corpus: `"party"`.

### A2 — Voce dei fondatori (gap-fill, sempre citato come personale)

- `A2-boldrin`, `A2-boldrin-article`, `A2-boldrin-event` —
  Michele Boldrin (profili tematici, articoli storici nFA 2006–2014,
  distillati di eventi).
- `A2-forchielli`, `A2-forchielli-event` — Alberto Forchielli.

⚠️ **Importante:** una posizione di Boldrin o Forchielli **non è**
automaticamente una posizione del partito. Quando si cita A2, esplicitarlo:
*«Boldrin personalmente sostiene…»*, non *«ORA! sostiene…»*.

Attribution values: `"boldrin"` o `"forchielli"`.

### Tier dati — D1–D4 (per `data_lookup`)

- **D1** — agenzie statistiche nazionali (ISTAT, Banca d'Italia).
- **D2** — fonti internazionali (Eurostat, OECD, FMI).
- **D3** — report istituzionali (ministeri, peer-reviewed).
- **D4** — fonti di advocacy / partigiane. **Escluse** dal pavimento di default.

### `other-parties` — Altri partiti italiani

- Profili di PD, M5S, FdI, Lega, FI, AVS, Azione, IV.
- Attribution values: `"azione"`, `"pd"`, `"fdi"`, `"iv"`, `"fi"`, `"avs"`,
  `"lega"`, `"m5s"` (uno per partito).
- ⚠️ **Recuperare SOLO** quando l'utente chiede esplicitamente un confronto.
  Mai usato come fonte standalone per "cosa pensa il PD di X" — il server è
  centrato su ORA!.

Per il confronto: chiamare `find_position(topic, include_comparison=True)`.

## Linee guida per l'assistente AI

- **Lingua:** rispondere sempre in italiano se la domanda è in italiano.
- **Persona:** terza persona, enciclopedica. *«La posizione di ORA! è…»*,
  non *«Noi pensiamo…»*. Il server non parla a nome del partito.
- **Tool principale:** `find_position(topic)` per ogni domanda del tipo
  *«cosa pensa ORA! di X?»*. La risposta è strutturata in *bucket* per
  affidabilità — rispettarli scrupolosamente.
- **Mai confondere i bucket:**
  - `official_party` → posizione del partito. Quotare come tale.
  - `leader_views` → opinioni personali di Boldrin/Forchielli. **Mai**
    attribuirle al partito. Formulare come *«Boldrin personalmente
    sostiene…»*, non *«ORA! sostiene…»*.
  - `supporting_data` → numeri, da citare con `quality_tier`, `data_period`,
    `source_doc`.
  - `comparison` → altri partiti, solo se l'utente ha chiesto un confronto
    (richiede `include_comparison=True`).
- **Cita sempre:** ogni affermazione sostantiva dovrebbe essere ancorata
  al `source_doc` di un chunk restituito dal tool.
- **Se `official_party` è vuoto:** il partito non ha articolato una posizione
  esplicita su quel tema. Dichiararlo esplicitamente; **non** sintetizzare
  una posizione del partito da `leader_views` o da chunk non correlati.
- **Per domande quantitative pure:** usare `data_lookup(metric)` direttamente.
  Default `quality_tier_floor="D3"` accetta D1+D2+D3, esclude D4 (advocacy).

## Documenti canonici disponibili come MCP resources

Oltre alla ricerca strutturata via `find_position`, i seguenti documenti
ufficiali sono pre-caricabili direttamente dall'assistente AI:

- `ora://about` — questo documento.
- `ora://manifesto` — manifesto completo (21 tesi programmatiche).
- `ora://statuto` — statuto del partito (governance, organi, regole interne).
- `ora://fondamenti` — Allegato 2 dello statuto: i 15 fondamenti programmatici
  non negoziabili a cui ogni aderente sottoscrive.
- `ora://codice-etico` — Allegato 3 dello statuto: standard di condotta,
  conflitti d'interesse, sanzioni.

Preferire **letture di resource** per domande dirette su questi documenti
("cosa dice lo statuto su X?"), e `find_position` per ricerche tematiche
trasversali ("posizione di ORA! su X").

## Maintenance

Il corpus dietro questo MCP è mantenuto separatamente dal progetto originale
*ORA Chatbot*. Aggiornamenti del corpus (nuove tesi, comunicati, eventi)
sono ri-indicizzati lì; questo server li vede automaticamente perché legge
dallo stesso indice Qdrant `ora_chunks`.
