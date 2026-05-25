# Deploy & demo runbook

> ⚠️ **Superseded by D33 (2026-05-24).** The current production deploy is
> Fly.io with OAuth — live at `https://ora-mcp-claudeai.fly.dev`. See
> `OWNER.md` for the operational runbook, and `DECISIONS.md` D33 for the
> rationale. The Cloudflare-Tunnel path described below was an interim
> demo solution that is no longer in use; the Fly section at the bottom
> of this file is closer to the current setup but also out of date in
> detail (always-warm `min_machines_running=1`, no `auto_stop_machines`).
> This file is kept for historical reference.

---

Operational guide for the maintainer: how to expose the ORA! MCP server to a
public URL using Cloudflare Tunnel, and how to prepare a demo kit.

The Fly.io artifacts (`fly.toml`, `Dockerfile`) are retained as a fallback
for stable hosting.

---

## TL;DR

```powershell
# 1. Server (in one PowerShell window, leave running)
python -m ora_mcp.server

# 2. Tunnel (in a second window, leave running)
cloudflared tunnel --url http://localhost:8000

# Cloudflare prints a URL like: https://blue-cat-123.trycloudflare.com
# 3. Substitute that URL into the demo kit before sending — see below.
```

---

## One-time setup

### Install `cloudflared`

**Windows:**

```powershell
winget install --id Cloudflare.cloudflared
```

(Alternative: download the `.exe` from
[cloudflare's GitHub releases](https://github.com/cloudflare/cloudflared/releases)
and put it on PATH.)

**macOS:**

```bash
brew install cloudflared
```

**Linux:** see Cloudflare's docs.

No Cloudflare account required for the `trycloudflare` mode used here.

---

## Per-demo workflow

### 1. Make sure the MCP server is running locally

In one PowerShell window:

```powershell
python -m ora_mcp.server
```

Wait for `Uvicorn running on http://0.0.0.0:8000`. Leave this window open.

Verify:

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:8000/health -UseBasicParsing
```

Expected: `200 OK` with body `ok`.

### 2. Start the Cloudflare Tunnel

In a **second** PowerShell window:

```powershell
cloudflared tunnel --url http://localhost:8000
```

Cloudflare connects, then prints output ending with something like:

```
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
|  https://blue-cat-123.trycloudflare.com                                                    |
+--------------------------------------------------------------------------------------------+
```

**Copy that URL.** That is your public URL for this session. Leave the
tunnel window open for the entire demo period.

### 3. Verify the public URL works

In a browser (or a third PowerShell):

```powershell
Invoke-WebRequest -Uri https://<YOUR_TUNNEL_URL>/health -UseBasicParsing
```

Expected: `200 OK` / `ok`.

Then open `https://<YOUR_TUNNEL_URL>/` in a browser — you should see the
landing page with the ORA! logo and the (correctly URL-substituted) Claude
Desktop config snippet. The landing page derives the URL dynamically from
the request, so it always shows the right snippet.

### 4. Prepare the demo kit to send

The committed files in `demo/` use `<URL_DEL_SERVER>` as a placeholder.
Substitute your real tunnel URL into copies for sending:

```powershell
# From the repo root:
$url = "https://blue-cat-123.trycloudflare.com"
$outDir = "demo/out"
New-Item -ItemType Directory -Force $outDir | Out-Null
(Get-Content demo/README.md -Raw).Replace('<URL_DEL_SERVER>', $url) `
  | Set-Content "$outDir/README.md" -Encoding utf8
(Get-Content demo/claude_desktop_config.json -Raw).Replace('<URL_DEL_SERVER>', $url) `
  | Set-Content "$outDir/claude_desktop_config.json" -Encoding utf8
Write-Output "Kit ready in $outDir"
```

The `demo/out/` directory (gitignored) now contains the kit ready to send.

### 5. Send to management

Attach `demo/out/README.md` (or paste inline) and `demo/out/claude_desktop_config.json`
in an email. Include the public URL in the email body — when they click it,
the Cloudflare-edge unfurl + the OpenGraph meta tags on the landing page
produce a preview card with the ORA! logo.

---

## Keeping the demo alive

While the demo period is active:

- **Don't close** the server window or the tunnel window.
- **Don't let the PC sleep.** Open *Power & sleep* settings → set
  "When plugged in, PC goes to sleep after" to **Never**, at least for the
  demo window.
- **Don't lose Wi-Fi.** Wired connection is more reliable if available.

If any of the above happens, the tunnel dies and the public URL stops
working. Just restart the tunnel (`cloudflared tunnel --url
http://localhost:8000`) — but the **URL will change** and you'll need to
re-send the kit. See "Stable URLs" below for the long-term fix.

---

## URL stability and Cloudflare account modes

`trycloudflare` mode (what this runbook uses) is the zero-account,
zero-config path — at the cost of an ephemeral random URL each restart.

For a **stable URL** that survives tunnel restarts, you'd need:

1. A free Cloudflare account.
2. A domain managed via Cloudflare DNS (yours, or one you buy — Cloudflare
   sells domains at registrar cost, ~$10/year for `.com`).
3. A *named tunnel* attached to a hostname on that domain, e.g.
   `mcp.your-domain.com`.

The setup is documented at
[developers.cloudflare.com/cloudflare-one/connections/connect-networks](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/).
Once configured, this guide's "start the tunnel" step becomes a single
named-tunnel `cloudflared tunnel run ora-mcp` and the URL is permanent.

If ORA! adopts the project and provides a `mcp.ora-italia.it` subdomain,
this is the natural next step. For the initial demo, `trycloudflare` is
sufficient.

---

## Troubleshooting

**`cloudflared` command not found after install (Windows).** Close and
reopen PowerShell so it picks up the updated PATH.

**Tunnel starts but the public URL returns 502 / Bad Gateway.** Your local
server isn't running (or isn't on port 8000). Check that
`Invoke-WebRequest http://127.0.0.1:8000/health` returns `ok`.

**Claude Desktop says "connection refused" with the public URL.** Confirm
the URL in `claude_desktop_config.json` includes `/mcp` at the end and
matches the tunnel's current URL (it changes on every restart).

**Voyage `RateLimitError` during demo.** Single-user demo traffic is far
under the 2M TPM cap. If you somehow hit it, wait ~60 seconds; the limit
is a rolling window.

---

## Fallback path: Fly.io

If you ever want stable hosting that survives your PC going off — without
buying a domain — the `fly.toml` and `Dockerfile` in the repo are ready.
See DECISIONS D11 for the rationale and the prior copy of the deploy
sequence (note: Fly removed their no-credit-card free tier in late 2024,
so a payment method is required; per-month cost for this config is small,
typically under $2 with auto-stop enabled).
