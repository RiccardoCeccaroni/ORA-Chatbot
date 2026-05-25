# Demo — domande per mostrare il valore dell'MCP

Insieme di domande pensate per la presentazione alla direzione di ORA!. Coprono
i quattro obiettivi dell'assistente (Stato / Proiezione / Giustificazione /
Confronto) e mettono in evidenza il valore unico del corpus curato vs. una
risposta "generica" dell'AI senza MCP.

**Modalità d'uso:** in Claude Desktop con l'MCP `ora` collegato, fare le domande
seguenti e mostrare che le risposte citano `source_doc` reali del corpus.

---

## 1. Stato — qual è la posizione di ORA! su X?

> **«Qual è la posizione di ORA! sulla riforma del sistema pensionistico?»**

*Atteso:* l'assistente chiama `find_position("riforma pensioni")`, legge il
bucket `official_party` (chunk dalla tesi pensionistica del manifesto, A1a),
cita testualmente. Se `leader_views.boldrin` aggiunge una sfumatura, viene
riportato come "Boldrin personalmente sostiene…".

> **«Cosa propone ORA! sulla tassazione e fiscalità?»**

*Atteso:* recupero dalla tesi 19 (`19-tassazione-fiscalita.md`), citazione
dei punti programmatici.

> **«Che posizione ha ORA! sull'immigrazione?»**

*Atteso:* tesi 10, distinzione fra integrazione, *ius scholae*, gestione dei
flussi.

---

## 2. Proiezione — cosa farebbe ORA! se Y?

> **«Se ORA! entrasse al governo, cosa farebbe nei primi 100 giorni
> sulla spesa pubblica?»**

*Atteso:* l'assistente combina la tesi 17 (spesa pubblica) con gli obiettivi
programmatici, esplicitando che la proiezione è una sintesi delle posizioni
del partito.

> **«Cosa farebbe ORA! sull'energia se dovesse decidere domani?»**

*Atteso:* `find_position("energia")`, bucket `official_party` (tesi 06
energia-ambiente-sostenibilità) + eventuali comunicati recenti restituiti
nello stesso bucket.

---

## 3. Giustificazione — su quali dati ORA! basa la posizione?

> **«ORA! sostiene che il welfare italiano sia insostenibile. Su quali
> dati si basa?»**

*Atteso:* `find_position("welfare sostenibilità")` — il bucket
`supporting_data` restituisce automaticamente le cifre ISTAT/Eurostat
rilevanti, accanto a `official_party` con la tesi. Una sola chiamata
basta. (`data_lookup` esplicito è opzionale se si vuole una metrica
specifica.)

> **«Quali sono i numeri ISTAT sulla disoccupazione giovanile che ORA!
> richiama?»**

*Atteso:* `data_lookup("tasso disoccupazione giovanile", quality_tier_floor="D1")`.
Mostra stat-cards con `quality_tier=D1` (ISTAT) e periodo.

---

## 4. Confronto — in cosa ORA! si differenzia da X?

> **«In cosa ORA! si differenzia da Azione sulla politica industriale?»**

*Atteso:* una sola chiamata `find_position("politica industriale",
include_comparison=True)`. Il bucket `official_party` ha la tesi 18 di
ORA!; il bucket `comparison` ha la posizione di Azione. Confronto
bilanciato dall'assistente.

> **«Differenze fra ORA! e Italia Viva sulla riforma fiscale?»**

*Atteso:* stesso pattern, due lati esplicitati.

---

## 5. Edge case — gestione corretta del "non lo so"

> **«Qual è la posizione di ORA! sulle politiche di adozione per
> coppie omogenitoriali?»**

*Atteso:* `find_position("adozione coppie omogenitoriali")` ritorna
`official_party=[]` (bucket vuoto). L'assistente **dichiara l'assenza**
invece di inferire dai bucket `leader_views`. Mostra che l'MCP non
costringe l'AI a inventare quando manca la fonte ufficiale.

---

## Domande NON da fare (anti-demo)

- Domande puramente fattuali sulla storia italiana (l'MCP non è
  un'enciclopedia generale, l'AI userà conoscenze sue).
- Domande personali su Boldrin o Forchielli al di fuori della loro
  attività politica (il corpus è scoped sul partito).
- *«Cosa pensi tu di X?»* — il bot non parla in prima persona.
