# Vercel — frontend / Next.js / agentic serverless platform

- **Tags:** hosting, nextjs, serverless, edge, cdn, ai-sdk, v0, agents
- **Verified as of:** 2026-09-09
- **Sources:**
  - https://vercel.com
  - https://vercel.com/pricing
  - https://vercel.com/docs/fluid-compute
  - https://vercel.com/docs/agent-resources/vercel-plugin

## Кратко

**Vercel** — платформа авторов **Next.js**. Git push → превью на каждый PR → прод на глобальном CDN. Считается **функциями** (Fluid compute: платишь за active CPU, не за простой), не за всегда включённый контейнер. Сильна фронтом, ISR, edge, AI SDK / AI Gateway / v0 / Sandbox. Слаба как «один ящик для API + Postgres + воркера» — БД с маркетплейса (Neon, Upstash, Blob), долгие процессы и произвольный Docker исторически не её история (Dockerfile на Vercel появился, но это не Railway).

## What it actually is

Company: Vercel Inc. Product: Git-connected deployments + **Vercel Functions** on a global network. Default compute path since **2025-04-23**: **Fluid compute**.

Good at:

- Next.js App Router, React, static sites, preview URLs
- Image optimization, ISR, WAF, DDoS
- AI apps: **AI SDK**, **AI Gateway** (many models, one API), **v0** (UI generator, paid add-on), **Vercel Sandbox** (Firecracker microVMs for untrusted/agent code), Workflows / Queues (some Beta)

Not a replacement for a VPS: no first-class always-on worker with a local disk like Railway volumes. Postgres is **Neon (marketplace)**, Redis **Upstash**, files **Blob**.

### Agent surface

```bash
npx plugins add vercel/vercel-plugin
# then in Claude Code / Codex / Cursor / Copilot / Grok Build / Kimi:
/vercel-plugin:nextjs
/vercel-plugin:ai-sdk
/vercel-plugin:deploy prod
```

Needs Node 18+ and **Bun**. Session context auto-injects only in empty dirs or detected Next/Vercel projects.

Classic CLI (user machine):

```bash
npm i -g vercel
vercel login
vercel          # preview
vercel --prod
vercel env pull
```

### Pricing (official page, 2026-09-09)

| Plan | Price | Shape |
| --- | --- | --- |
| **Hobby** | **$0 / mo** | Personal. 1M edge requests, 100 GB Fast Data Transfer, 4 h Fluid CPU, 1M function invocations, 1 GB Blob, … |
| **Pro** | **$20 / mo** | Includes **$20 usage credit**. Team: **$20 / developer seat / month**, unlimited viewers. Flat-rate CDN, spend management, custom domain included |
| Enterprise | custom | SLA 99.99%, SCIM, multi-region failover |

Overage examples (Pro, list rates): Fluid CPU from **$0.128 / hour**, memory from **$0.0106 / GB-hr**, invocations from **$0.60 / 1M**. Set **Spend Management** or Hobby can pause and Pro can surprise.

v0 = paid add-on. Vercel Agent (beta) billed in tokens.

## How agents should use it

Choose Vercel when the user is shipping **Next.js / frontend / marketing site / AI chat UI** and wants preview deploys for every PR.

1. `npx create-next-app` (or existing Next repo).
2. They connect GitHub on vercel.com/new **or** `vercel` CLI on their laptop.
3. Use Server Actions / Route Handlers for light backend. Heavy jobs → Queue / Workflow / external worker (Railway, etc.).
4. DB: `vercel install` marketplace (Neon/Upstash) rather than inventing a container.
5. Bind nothing; Vercel sets the HTTP entry. Do **not** start a long `node server.js` listen loop unless using the newer container/Dockerfile path on purpose.

On **Arena**: live preview here ≠ a Vercel preview URL. To ship, the user must log into Vercel. You can still generate a correct Next.js app and a `vercel.json` if needed.

## Pitfalls

- **Serverless limits**: max duration, no sticky local filesystem, cold starts (Fluid reduces them; Pro “cold start prevention”).
- **Per-seat** on Pro ($20 × developers) vs Railway Pro unlimited seats.
- Bandwidth / image optimization / ISR writes are separate meters — read the pricing table before promising “it’s free”.
- Hobby is **not** for a company product (ToS / commercial limits historically; confirm current Hobby commercial policy if they ask).
- `vercel-plugin` wants **Bun**; missing Bun → install fails.
- Do not put secrets in the client bundle; use `vercel env`.
