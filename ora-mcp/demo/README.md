# ORA! MCP — quick start

**ORA!** is an Italian political party founded by Michele Boldrin and Alberto Forchielli. This **MCP server** lets Claude and any other MCP-compatible AI assistant pull from the party's curated corpus in real time — manifesto, official communications, founder profiles, ISTAT data — whenever a user asks a question.

In practice: instead of answering *"ORA! probably thinks X about Y…"*, the assistant quotes the official position verbatim, distinguishing between the party's voice, the founders' personal views, and supporting data.

**Server URL:** `https://ora-mcp-claudeai.fly.dev`

---

## Option 1 (recommended): claude.ai in the browser

Works on desktop and mobile. Nothing to install.

1. Go to **`https://claude.ai/customize/connectors`**.
2. Click **"Add custom connector"**.
3. Paste this URL:
   ```
   https://ora-mcp-claudeai.fly.dev/mcp
   ```
4. Save. Claude shows an OAuth authorization screen — confirm (one click).
5. Open a new chat. Under the input box, enable the `ora` connector.
6. Try: *«qual è la posizione di ORA! sull'università?»*

Total time: ~1 minute. Works in any browser and in the claude.ai apps for iOS / Android / Mac / Windows.

---

## Option 2: Claude Desktop (local app)

For users who prefer the installed desktop app.

### 1. Open the config file

In Claude Desktop: **Settings → Developer → Edit Config**.

The file `claude_desktop_config.json` opens.

### 2. Add the block for your OS

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

> If you already have other MCP servers configured, just add the `"ora": {...}` entry inside `"mcpServers"` — don't replace the whole block.

### 3. Save and restart Claude Desktop

Fully quit the app (system tray → Quit on Windows) and reopen it.

### 4. Verify

Open a new chat. At the bottom you'll see the **"Search and tools"** icon. Clicking it should list `ora` with the tools `find_position` and `data_lookup` available.

---

## Questions to try

To see what the MCP is good for, try these four queries (asked in Italian since the corpus is Italian):

**1. Party position on a specific topic**

> *«Qual è la posizione di ORA! sulla riforma del sistema pensionistico?»*
> *(What is ORA!'s position on pension-system reform?)*

Expected response: a verbatim quote from the pensions thesis in the manifesto, with a source reference.

**2. Quantitative question with institutional data**

> *«Quali numeri ISTAT richiama ORA! sulla disoccupazione giovanile?»*
> *(What ISTAT numbers does ORA! cite on youth unemployment?)*

Expected response: stat-cards with `quality_tier=D1` (ISTAT), specific period, source indicated.

**3. Structured comparison with another party**

> *«In cosa ORA! si differenzia da Azione sulla politica industriale?»*
> *(How does ORA! differ from Azione on industrial policy?)*

Expected response: two sides spelled out — ORA!'s position and Azione's — in a balanced way.

**4. Edge case: the system does NOT invent**

> *«Qual è la posizione di ORA! sulla colonizzazione di Marte?»*
> *(What is ORA!'s position on the colonization of Mars?)*

Expected response: the assistant **explicitly states** that the party hasn't articulated a position, instead of inventing one. This is a key design property — the MCP doesn't force the AI to synthesize when the official source is silent.

---

## To uninstall

- **claude.ai:** go to `claude.ai/customize/connectors`, find `ora`, click to remove.
- **Claude Desktop:** remove the `"ora": {...}` block from `claude_desktop_config.json` and restart the app.

Nothing is left on your system afterwards.

---

## Technical questions?

Contact **Riccardo Ceccaroni** — `riccardoceccaroni02@gmail.com`.
