# AI_Stuff

Durable **knowledge library for AI agents**. Humans dump interesting tools and workarounds here; agents expand them into checkable notes so later sessions do not rediscover the same facts.

- Notes: [`knowledge/INDEX.md`](knowledge/INDEX.md)
- How agents should read/write this repo: [`AGENTS.md`](AGENTS.md)
- Helper tools: [`tools/`](tools/)

Пиши новые темы агенту обычным языком — он проверяет факты и кладёт карточку в `knowledge/`.

## Contents

| Topic | Why it is here |
| --- | --- |
| [text-to-cad](knowledge/cad/text-to-cad.md) | Local CAD via agent skills (`cadgen` / build123d), not a 3D generative net. Runnable in Arena. |
| [chunked file ingest](knowledge/sandbox/chunked-file-ingest.md) | HTML encoder splits any file into allow-listed chunks so sandboxes can reconstruct past upload caps. |
| [playlist «Ии»](knowledge/playlists/ii-ply8rck9gojyq.md) | 12 unlisted shorts fact-checked; most are AI ads. |
| [Soup](knowledge/tools/soup.md) | Local LoRA fine-tune of 8B on a 4 GB laptop GPU (`soup-cli`). |
| [Agent Reach](knowledge/tools/agent-reach.md) | Skill/CLI that wires unofficial readers for X/Reddit/YouTube/… |
| [Claude Code stack from the shorts](knowledge/claude-code/playlist-stack.md) | CLI-Anything, council, plugins — minus the fake “secret codes”. |
| [Railway](knowledge/hosting/railway.md) | Container PaaS: API + Postgres + workers, usage billed per second. |
| [Vercel](knowledge/hosting/vercel.md) | Next.js / CDN / Fluid functions / AI SDK. Preview on every PR. |
| [Railway vs Vercel](knowledge/hosting/railway-vs-vercel.md) | Request-shaped compute → Vercel; process-shaped → Railway. |
