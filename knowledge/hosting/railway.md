# Railway — container PaaS for apps, DBs, and workers

- **Tags:** hosting, paas, docker, postgres, redis, agents, cli
- **Verified as of:** 2026-09-09
- **Sources:**
  - https://railway.com
  - https://railway.com/pricing
  - https://docs.railway.com/cli
  - https://railway.com/agents
  - https://docs.railway.com/agents

## Кратко

**Railway** — облако «подключил репо / Docker — крутится». Контейнеры (не serverless-функции): API, воркеры, cron, **Postgres / MySQL / Redis / Mongo** в одном проекте, приватная сеть, тома. Билинг **по факту CPU/RAM/диска/egress за секунду**, плюс подписка с кредитом. Для агентов: `curl -fsSL agents.railway.com | sh`, CLI `railway up`, MCP, skills. Это **не** Vercel и **не** CDN для Next.js.

Домен сейчас **railway.com** (раньше railway.app).

## What it actually is

Heroku-shaped PaaS: visual canvas of services, GitHub autodeploy, CLI upload, templates.

Build order of preference:

1. **Dockerfile** if present
2. Else **Railpack** (Railway’s current default builder; Nixpacks is the older Railway-made builder, maintenance-mode upstream)

Runtime is a **long-lived container**. Good for WebSockets, queues, bots, SSH into the box (`railway ssh`). Not an edge CDN. No GPU SKU on the public plans.

### Agent / CLI surface

```bash
# installs CLI + wires detected coding agents
curl -fsSL agents.railway.com | sh

# CLI only
bash <(curl -fsSL railway.com/install.sh)
# or: npm i -g @railway/cli   |   brew install railway
```

Useful commands:

```bash
railway login                 # --browserless in SSH
railway up -y                 # first-run friendly for agents
railway add --database postgres
railway variable set KEY=value
railway logs
railway ssh
railway usage
```

CI: `RAILWAY_TOKEN=… railway up`. Remote MCP: docs at `docs.railway.com/ai/remote-mcp-server`. Skills: `github.com/railwayapp/railway-skills`.

### Pricing (official page, 2026-09-09)

Meter: **Memory** `$0.00000386 / GB / sec` (~$10/GB-month if always on), **CPU** `$0.00000772 / vCPU / sec` (~$20/vCPU-month), **volumes** `$0.00000006 / GB / sec`, **egress** `$0.05 / GB`, object storage `$0.015 / GB-month`.

| Plan | Floor | Included usage credit | After trial shape |
| --- | --- | --- | --- |
| Trial | $0, 30 days | $5 one-shot | then falls to Free |
| **Free** | **$1 / month** | tiny | 1 vCPU / 0.5 GB RAM / 0.5 GB volume, 1 project |
| **Hobby** | **$5 / month** | $5 | up to 48 vCPU / 48 GB RAM, 5 GB volume, 1 developer workspace |
| **Pro** | **$20 / month** | $20 | unlimited seats, much higher caps, 30-day logs |
| Enterprise | custom | custom | SSO, HIPAA BAA, dedicated VMs, BYOC |

The $5 / $20 is a **credit against usage**, not a cap. A 1 vCPU + 1 GB RAM always-on box is ~$30 of *resources* before the subscription credit. Set hard spend limits.

## How agents should use it

Pick Railway when the user needs **any** of: a real database next to the app, a worker/cron, Docker, a non-JS backend (Go, Python, Rails, …), persistent disks, private `.railway.internal` DNS.

Typical first deploy:

1. Confirm they have (or will create) a Railway account. **Do not** run `curl | sh` inside Arena unless they asked — that hits *their* laptop, not this sandbox.
2. `railway login` on their machine → `railway up -y` from the app directory.
3. `railway add --database postgres` and inject `DATABASE_URL` (Railway variable references).
4. Bind the HTTP server to `0.0.0.0` and `$PORT` (Railway sets `PORT`).
5. Custom domain on Hobby+ (Free after trial: **0 custom domains**).

On **Arena**: generate the app here, give the user the Railway commands. Do not expect `railway login` to work in this sandbox without their token.

## Pitfalls

- Sleeping / tiny Free caps after trial — not a production host.
- Always-on RAM is the bill. Idle still costs if the replica is up (unlike Vercel Fluid idle).
- Egress $0.05/GB adds up if you dump artifacts.
- Cron on **Free** is trial-only (pricing table).
- Railpack ≠ Nixpacks ≠ Docker. If the build is weird, add a Dockerfile.
- `railway delete` deletes the **project**, not one service — read the prompt.
