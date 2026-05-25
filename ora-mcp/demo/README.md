# ORA! MCP — guida rapida

**ORA!** è un partito politico italiano fondato da Michele Boldrin e Alberto
Forchielli. Questo **MCP server** permette a Claude e ad altri assistenti AI
compatibili con il protocollo MCP di consultare in tempo reale il corpus
curato del partito — manifesto, comunicati, viste dei fondatori, dati ISTAT —
quando l'utente fa una domanda.

In pratica: invece di rispondere *«su X il partito ORA! probabilmente pensa…»*,
l'assistente cita testualmente la posizione ufficiale, distinguendo fra voce
del partito, viste personali dei fondatori e dati a supporto.

**URL del server:** `https://ora-mcp-claudeai.fly.dev`

---

## Opzione 1 (raccomandata): claude.ai sul browser

Funziona su desktop e mobile. Niente da installare.

1. Vai a **`https://claude.ai/customize/connectors`**.
2. Clicca **"Add custom connector"** (o "Aggiungi connettore personalizzato").
3. Incolla questo URL:
   ```
   https://ora-mcp-claudeai.fly.dev/mcp
   ```
4. Salva. Claude ti mostrerà una schermata di autorizzazione OAuth — conferma
   (un clic).
5. Apri una nuova chat. Sotto al campo di input, attiva il connettore `ora`.
6. Prova: *«qual è la posizione di ORA! sull'università?»*

Tempo totale: ~1 minuto. Funziona in qualsiasi browser e nelle app
claude.ai per iOS / Android / Mac / Windows.

---

## Opzione 2: Claude Desktop (app locale)

Per chi preferisce l'app installata sul proprio computer.

### 1. Apri il file di configurazione

In Claude Desktop: **Settings → Developer → Edit Config**.

Si aprirà il file `claude_desktop_config.json`.

### 2. Aggiungi il blocco per il tuo sistema operativo

**macOS / Linux:**

```json
{
  "mcpServers": {
    "ora": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://ora-mcp-claudeai.fly.dev/mcp", "--transport", "http-only"]
    }
  }
}
```

**Windows:**

```json
{
  "mcpServers": {
    "ora": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-remote", "https://ora-mcp-claudeai.fly.dev/mcp", "--transport", "http-only"]
    }
  }
}
```

> Se hai già altri MCP configurati, aggiungi solo la voce `"ora": {...}`
> dentro `"mcpServers"`, senza sostituire l'intero blocco.

### 3. Salva e riavvia Claude Desktop

Chiudi completamente l'app (system tray → Quit su Windows) e riaprila.

### 4. Verifica

Apri una nuova chat. In basso vedrai l'icona **"Search and tools"**.
Cliccandoci, dovresti vedere `ora` nell'elenco, con i tool
`find_position` e `data_lookup` disponibili.

---

## Domande da provare

Per vedere il valore dell'MCP, prova queste quattro domande:

**1. Posizione del partito su un tema specifico**

> *«Qual è la posizione di ORA! sulla riforma del sistema pensionistico?»*

Risposta attesa: citazione testuale dalla tesi pensionistica del manifesto,
con riferimento alla fonte.

**2. Domanda quantitativa con dati istituzionali**

> *«Quali numeri ISTAT richiama ORA! sulla disoccupazione giovanile?»*

Risposta attesa: stat-cards con `quality_tier=D1` (ISTAT), periodo
specificato, fonte indicata.

**3. Confronto strutturato con un altro partito**

> *«In cosa ORA! si differenzia da Azione sulla politica industriale?»*

Risposta attesa: due lati esplicitati — posizione di ORA! e di Azione —
in modo bilanciato.

**4. Caso limite: il sistema NON inventa**

> *«Qual è la posizione di ORA! sulla colonizzazione di Marte?»*

Risposta attesa: l'assistente **dichiara esplicitamente** che il partito
non ha articolato una posizione, invece di inventarne una. È una proprietà
chiave del design — l'MCP non costringe l'AI a sintetizzare quando manca
la fonte ufficiale.

---

## Cosa l'MCP fa (e cosa NON fa)

✅ **Fa:**
- Restituisce chunk testuali del corpus, organizzati per affidabilità
  (voce del partito / leader / dati / confronto)
- Lascia all'assistente AI la composizione della risposta, citando le
  fonti
- Funziona con qualsiasi client MCP — claude.ai, Claude Desktop, Cursor,
  ChatGPT con MCP, ecc.

❌ **Non fa:**
- Non parla a nome del partito — il server fornisce solo le fonti
- Non risponde a domande personali sui fondatori al di fuori della
  loro attività politica
- Non sostituisce il sito ufficiale `ora-italia.it`

---

## Per disinstallare

- **claude.ai:** vai a `claude.ai/customize/connectors`, trova `ora`,
  clicca per rimuoverlo.
- **Claude Desktop:** rimuovi il blocco `"ora": {...}` da
  `claude_desktop_config.json` e riavvia l'app.

Nessun file viene lasciato sul tuo sistema.

---

## Domande tecniche?

Contatta **Riccardo Ceccaroni** — `riccardoceccaroni02@gmail.com`.
