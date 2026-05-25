# OWNER.md — operational reference

A scan-able quick-reference for Riccardo, designed for picking back up
after a long pause. For the architectural reasoning behind decisions,
see `DECISIONS.md`. For lessons that generalize, see `LEARNINGS.md`.

---

## What you have

| | |
|---|---|
| Public URL | `https://ora-mcp-claudeai.fly.dev` |
| MCP endpoint | `https://ora-mcp-claudeai.fly.dev/mcp` |
| Fly app | `ora-mcp-claudeai` (Frankfurt, single machine) |
| Admin console | `https://fly.io/apps/ora-mcp-claudeai` |
| Monthly cost | ~$3.19 (compute) — bandwidth and storage negligible |
| Demo recipients | Denis Pagotto + Sirio Papa (sent 2026-05-24) |

---

## Is it up?

```powershell
curl https://ora-mcp-claudeai.fly.dev/health
```

Expected: `ok`. Anything else → check the logs (next section).

## Watch the logs (real-time)

```powershell
fly logs --app ora-mcp-claudeai
```

Useful when a recipient says *"I tried it and it didn't work"* — you can
see exactly which OAuth step or which tool call hit the server. A
healthy flow looks like:

```
POST /register             201 Created
GET  /authorize            302 Found
POST /token                200 OK
POST /mcp                  200 OK   # session created
POST /mcp                  202 Accepted   # initial messages
ListToolsRequest
CallToolRequest find_position   # the actual query
```

If you see lots of `401 Unauthorized` on `/mcp` after a `POST /token 200`,
that's the "in-memory token store reset after deploy" pattern — users
just need to re-authorize their claude.ai connector.

## Cost so far this month

```powershell
fly billing show
```

Or open `https://fly.io/dashboard/personal/billing`. Expected:
~$3.19/month flat. If higher, sanity check:

```powershell
fly scale show --app ora-mcp-claudeai     # should be: 1 machine, shared-cpu-1x, 512 MB
```

---

## Common situations

### "I added the connector but it doesn't work"

In decreasing likelihood:

1. **They forgot to enable the connector for the chat.** claude.ai
   requires per-chat toggle even after the connector is added globally.
   Tell them to look for the tools/connectors picker in the chat input
   area, then enable `ora`.
2. **They have to approve each tool call.** claude.ai shows an "Allow"
   prompt the first time each tool is called. Tell them to look for
   it and click Allow (or "Always allow").
3. **Their token expired** (only happens after a redeploy or Fly
   restart). Tell them to disconnect the connector in
   `claude.ai/customize/connectors` and re-add it.

Use `fly logs` to confirm what's reaching the server.

### Need to redeploy after a code change

```powershell
cd "C:\Users\ricca\Desktop\ORA Projects\ora-mcp-claudeai"
fly deploy --app ora-mcp-claudeai
```

Takes 2–4 minutes. The single machine restarts; in-memory OAuth state
is lost. claude.ai usually re-auths transparently on next use.

### Server crashes mid-demo

Fly's machine manager auto-restarts crashed processes. If unreachable
for >30 seconds:

```powershell
fly status --app ora-mcp-claudeai
fly logs --app ora-mcp-claudeai | tail -n 50
```

Force a restart: `fly machine restart <machine-id>` (get the ID from
`fly status`).

### Update the corpus

Edit files in `corpus/` (or add new ones via the YouTube pipeline in
`build/youtube_pipeline/`), then re-ingest into Qdrant Cloud:

```powershell
pip install ".[build]"                   # one-time
python build/chunk_corpus.py --apply
python build/ingest_qdrant.py --apply
```

No MCP redeploy needed — the server reads from Qdrant Cloud and picks
up the updated index automatically.

---

## End of demo

### If ORA says "yes, let's adopt this"

1. Hand over the Fly app to their org (Fly supports org transfers via
   support ticket).
2. Transfer the Qdrant Cloud subscription, or have them create their own
   account and re-ingest the corpus (~20 min).
3. Transfer the Voyage API key, or same — have them create their own.
4. Push the codebase to a GitHub repo under their org.
5. Document the handover as a new `D##` entry in `DECISIONS.md`.

### If ORA says "interesting but not for us"

```powershell
fly apps destroy ora-mcp-claudeai
```

That's the only thing costing money. The local folder, the Qdrant Cloud
account, the Voyage account — all independent and unaffected. Keep
`LEARNINGS.md` — it's the most reusable artifact for future projects.

---

## Quick-recovery checklist (if you forget everything)

1. Open this folder in Claude Code:
   `C:\Users\ricca\Desktop\ORA Projects\ora-mcp-claudeai\`
2. Read `CLAUDE.md` for architectural context.
3. Read `LEARNINGS.md` Section 10 for the bugs we hit (you'll save a day).
4. Run `fly status --app ora-mcp-claudeai` to confirm the deploy is alive.
5. Run `curl https://ora-mcp-claudeai.fly.dev/health` for the round-trip check.
6. If everything's healthy, you're good. If not, `fly logs` is the
   first place to look.

---

## Contacts

- **Riccardo Ceccaroni** (you) — `riccardoceccaroni02@gmail.com`
- **Denis Pagotto** — demo recipient
- **Sirio Papa** — demo recipient; explicitly suggested the MCP form
  factor in his May 16 rejection of the chatbot proposal

Full email thread: search Gmail for `siriopapa` or `pagottodenis`.
