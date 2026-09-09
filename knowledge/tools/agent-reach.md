# Agent Reach — give a coding agent unofficial “eyes” on social platforms

- **Tags:** claude-code, skills, scraping, mcp, twitter, reddit, youtube
- **Verified as of:** 2026-09-09
- **Sources:**
  - https://github.com/Panniantong/Agent-Reach (~79k★, MIT, Python 3.10+)
  - English README: https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md
  - Playlist short (misnames it “Agentic”): https://www.youtube.com/watch?v=l_K0QG6TdiA

## Кратко

**Agent Reach** — скилл + CLI `agent-reach`: ставит и роутит **бесплатные** ридеры/скрейперы (Twitter/X, Reddit, YouTube, GitHub, Bilibili, 小红书, …) без официальных платных API. Это **не** «Anthropic выдал Claude глаза». Часть каналов — cookies / сессия Chrome. Обход ToS и баны — на пользователе. На Arena обычно **не нужно**: уже есть `web_search` / `fetch_page`.

## What it actually is

Installer + router for existing open CLIs (Jina Reader, twitter-cli, yt-dlp-class tools, OpenCLI Chrome session, …). Primary + fallback backend per platform; `agent-reach doctor` health-checks.

Install (desktop Claude Code / Cursor / Codex):

```bash
npx skills add Panniantong/Agent-Reach
# or
pip install agent-reach
agent-reach install
```

Natural-language bootstrap from their docs:

```text
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Zero-config-ish: generic web (Jina), V2EX, some GitHub/YouTube paths. Cookie/session: X, Reddit (datacenter IPs often 403), Xiaohongshu, Instagram/Facebook via OpenCLI.

**Not affiliated with any crypto token** — README warns of impersonation.

English fork exists ([Stephen-Garner/steves-agent-reach](https://github.com/Stephen-Garner/steves-agent-reach)) if the original Chinese-first docs are painful.

## How agents should use it

- **Claude Code on the user’s machine**, when they need YouTube transcripts, X/Reddit threads, or CN platforms that vanilla fetch blocks.
- After install: `agent-reach doctor`, then platform commands from SKILL.md — do not invent API keys.
- **Arena / this sandbox:** skip. Use built-in web tools. Do not install scrapers that need the user’s Chrome cookies (they are not here).

## Pitfalls

- **Terms of service.** “No API fees” often means unofficial access. Logged-in cookie reuse can throttle or ban **the user’s** account. Prefer a throwaway login if they insist.
- Rate limits and layout breakage. Doctor + fallbacks help; they do not grant a stable SLA.
- Cookies stay local **if** you use the official CLI; still treat them as credentials.
- Shorts quote stale star counts (62k vs ~79k). Always open GitHub.
