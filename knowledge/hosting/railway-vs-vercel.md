# Railway vs Vercel — which one an agent should pick

- **Tags:** hosting, railway, vercel, comparison
- **Verified as of:** 2026-09-09
- **Sources:** [railway.md](railway.md), [vercel.md](vercel.md) (official pricing/docs cited there)

## Кратко

**Фронт / Next.js / превью PR / CDN → Vercel.**  
**Бэкенд + Postgres + воркер / Docker / любой язык / всегда живой процесс → Railway.**  
Частый прод-паттерн 2026: **Vercel (UI) + Railway (API/DB/jobs)**. Не пихать всё на одну платформу «потому что так в шортсе».

## Decision table

| Need | Pick |
| --- | --- |
| Next.js marketing site or App Router SaaS UI | **Vercel** |
| Preview URL on every PR with almost zero config | **Vercel** |
| Global CDN + image optimization | **Vercel** |
| AI SDK / AI Gateway / v0 UI | **Vercel** |
| FastAPI / Go / Rails / Discord bot / queue worker | **Railway** |
| Postgres + Redis in the same project, private DNS | **Railway** |
| Dockerfile, cron, SSH into the box, persistent volume | **Railway** |
| WebSockets / long-lived TCP | **Railway** (Vercel functions are request-scoped) |
| Solo hobby, $0 | **Vercel Hobby** (Railway Free after trial is $1 and tiny) |
| Team of 5 shipping Next only | Vercel Pro seats add up ($20 × devs) |
| Team of 5 shipping API+DB | **Railway Pro** (unlimited seats, $20 credit + usage) |

## Cost intuition (not a quote)

- Vercel: **seat + request/CPU meters**. Cheap at low traffic on Hobby; Pro is $20/user plus usage. Spikes = function/bandwidth/ISR.
- Railway: **subscription credit + always-on RAM/CPU**. A forgotten 1 GB replica is ~$10/mo RAM even at zero RPS. Idle Vercel Fluid is closer to $0.

Always set spend caps on both.

## How agents should use it

Ask one question: **is the unit of compute a request or a process?**

- Request (SSR, API route, webhook < 1 min) → Vercel is simpler.
- Process (bot, worker, DB, GPU-less model server) → Railway.

If the user says “задеплой” without a target, default:

1. Pure frontend/Next → Vercel.
2. Anything with a database or a worker → Railway.
3. Both → split.

Do not run either CLI inside Arena without the user’s token. Generate the app, print the exact commands for **their** machine.
