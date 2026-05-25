# Demo — questions that show what the MCP is good for

A set of example queries covering the four objectives of the assistant (State / Project / Justify / Compare) and showcasing what the curated corpus adds over a "generic" AI answer that has no MCP attached.

**How to use:** in Claude Desktop or claude.ai with the `ora` MCP connected, ask the questions below and observe that responses cite real `source_doc` entries from the corpus. Queries are in Italian because the corpus is Italian; rough English glosses are included.

---

## 1. State — what is ORA!'s position on X?

> **«Qual è la posizione di ORA! sulla riforma del sistema pensionistico?»**
> *(What is ORA!'s position on pension-system reform?)*

*Expected:* the assistant calls `find_position("riforma pensioni")`, reads the `official_party` bucket (chunks from the pensions thesis in the manifesto, A1a), quotes verbatim. If `leader_views.boldrin` adds nuance, it's flagged as *"Boldrin personally argues…"*.

> **«Cosa propone ORA! sulla tassazione e fiscalità?»**
> *(What does ORA! propose on taxation and fiscal policy?)*

*Expected:* retrieval from thesis 19 (`19-tassazione-fiscalita.md`), citation of the programmatic points.

> **«Che posizione ha ORA! sull'immigrazione?»**
> *(What is ORA!'s position on immigration?)*

*Expected:* thesis 10 — distinction between integration, *ius scholae*, and flow management.

---

## 2. Project — what would ORA! do if Y?

> **«Se ORA! entrasse al governo, cosa farebbe nei primi 100 giorni sulla spesa pubblica?»**
> *(If ORA! came to power, what would it do in the first 100 days on public spending?)*

*Expected:* the assistant combines thesis 17 (public spending) with the programmatic objectives, making explicit that the projection is a synthesis of the party's positions.

> **«Cosa farebbe ORA! sull'energia se dovesse decidere domani?»**
> *(What would ORA! do on energy if it had to decide tomorrow?)*

*Expected:* `find_position("energia")`, `official_party` bucket (thesis 06 energy-environment-sustainability) plus any recent communications returned in the same bucket.

---

## 3. Justify — what data does ORA! base its position on?

> **«ORA! sostiene che il welfare italiano sia insostenibile. Su quali dati si basa?»**
> *(ORA! argues that Italian welfare is unsustainable. What data does this rest on?)*

*Expected:* `find_position("welfare sostenibilità")` — the `supporting_data` bucket automatically returns the relevant ISTAT / Eurostat figures alongside `official_party` with the thesis. One call is enough. (`data_lookup` is optional if you want a specific metric.)

> **«Quali sono i numeri ISTAT sulla disoccupazione giovanile che ORA! richiama?»**
> *(What ISTAT numbers on youth unemployment does ORA! cite?)*

*Expected:* `data_lookup("tasso disoccupazione giovanile", quality_tier_floor="D1")`. Returns stat-cards with `quality_tier=D1` (ISTAT) and the relevant period.

---

## 4. Compare — how does ORA! differ from X?

> **«In cosa ORA! si differenzia da Azione sulla politica industriale?»**
> *(How does ORA! differ from Azione on industrial policy?)*

*Expected:* a single call `find_position("politica industriale", include_comparison=True)`. The `official_party` bucket has ORA!'s thesis 18; the `comparison` bucket has Azione's position. The assistant produces a balanced comparison.

> **«Differenze fra ORA! e Italia Viva sulla riforma fiscale?»**
> *(Differences between ORA! and Italia Viva on fiscal reform?)*

*Expected:* same pattern, both sides made explicit.

---

## 5. Edge case — correct handling of "I don't know"

> **«Qual è la posizione di ORA! sulle politiche di adozione per coppie omogenitoriali?»**
> *(What is ORA!'s position on adoption policy for same-sex couples?)*

*Expected:* `find_position("adozione coppie omogenitoriali")` returns `official_party=[]` (empty bucket). The assistant **states the absence** instead of inferring from the `leader_views` bucket. This shows that the MCP doesn't force the AI to invent when the official source is silent.

---

## What NOT to ask (anti-demo)

- Purely factual questions about Italian history — the MCP isn't a general encyclopedia; the AI will use its own knowledge.
- Personal questions about Boldrin or Forchielli outside their political activity — the corpus is scoped to the party.
- *"What do you think about X?"* — the bot doesn't speak in the first person.
