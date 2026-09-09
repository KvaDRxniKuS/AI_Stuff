# Playlist «Ии» — 12 shorts, fact-checked

- **Tags:** youtube, shorts, claude-code, skills, soup, agent-reach
- **Verified as of:** 2026-09-09
- **Sources:**
  - Playlist (unlisted): https://www.youtube.com/playlist?list=PLY8rck9goJYQ
  - Channel that owns the list: [Гриша Петрозаводский](https://www.youtube.com/@ГришаПетрозаводский)
  - Per-video pages + auto-transcripts (YouTube), then upstream GitHub/docs for each named tool

## Кратко

Плейлист **не курс**, а **unlisted подборка из 12 шортсов** (≈50–85 с). 10 из 12 — канал [Ринат Сулейманов | AITron](https://www.youtube.com/@RinatSuleyman), почти все помечены *Made with AI*. Это рекламные нарезки про Claude Code / skills. Полезное — **имена инструментов**; цифры, «секретные коды» и обещания «убил индустрию» — нет. Ниже: каталог → что реально существует → куда смотреть дальше.

## What the playlist actually is

| # | Length | Video | Channel | Claim in the short | What checks out |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:58 | [5 Secret Codes…](https://www.youtube.com/watch?v=IXkfkIo_Diw) | AITron | Words `Landmine`, `Autopsy`, `Devil`, `V10`, `Bem` are “secret Claude codes” | **Not product features.** Extra English instructions. See [playlist-stack](../claude-code/playlist-stack.md). |
| 2 | 1:16 | [Agent Reach…](https://www.youtube.com/watch?v=l_K0QG6TdiA) | Вечный двигатель контента | “Agentic”, 62k stars, 17 platforms, no API fees | Real repo **[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)** (~79k★ on 2026-09-09). Transcript misnames it. [agent-reach.md](../tools/agent-reach.md) |
| 3 | 0:59 | [Apple-Level Designer](https://www.youtube.com/watch?v=EeL8CfGg-mQ) | AITron | “Apple’s entire design language as a skill” | Pattern is real (design-system **skill**, not a new model). Repo **not named** in the short. Likely Anthropic `frontend-design` and/or `apple-design` plugins. |
| 4 | 0:51 | [4GB graphics card / Soup](https://www.youtube.com/watch?v=_cxDr_t8PN4) | Кирилл Жильников | Alpamys Makazhan, Soup, 8B on 4 GB, “85k users” | **Soup is real.** User count **unverified**. [soup.md](../tools/soup.md) |
| 5 | 1:12 | [5 Free GitHub Tools](https://www.youtube.com/watch?v=5ngX8UO-nrk) | AITron | Agent Skills, Book-to-Skill, Cloudflare Computer, TencentDB memory, Authentik | Mix of real projects + ASR mush. Authentik is an IdP, not a Claude plugin. Details in playlist-stack. |
| 6 | 1:04 | [Apple-Level Websites](https://www.youtube.com/watch?v=Mu4ta3wFYLY) | AITron | Fable 5 + “211 DEF” + “Hixfield MCP” + “CDEN 2.0” | **Fable** = Claude model family. **21st.dev** is the likely “211 DEF”. Higgsfield plausible for media MCP. **CDEN 2.0 unverified** (ASR). |
| 7 | 0:53 | [Council of Five Claudes](https://www.youtube.com/watch?v=fNtyFAzdxvI) | AITron | `/council` skill, 5 personas + chairman HTML | Real pattern (Karpathy “LLM Council” → Claude **subagents**). Several community skills; short does not pin one repo. |
| 8 | 0:57 | [Agency-Level Websites](https://www.youtube.com/watch?v=J_4jZfHcGk8) | AITron | 2 design skills + taste skill + browser test loop | Same as #3/#6: `frontend-design` + visual QA (Playwright / computer-use). No unique repo named. |
| 9 | 0:58 | [Control Any Software](https://www.youtube.com/watch?v=TV1hnyX4J7s) | AITron | **CLI Anything** wraps any app as CLI | Real: **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)** (desktop). Web cousin: CLI-Anything-WEB. |
| 10 | 0:49 | [CapCut](https://www.youtube.com/watch?v=II0yNAQU-x0) | AITron | Claude edits CapCut in <20 min | **No installable skill named.** Treat as demo/ad. CapCut APIs/skills exist in the wild; this short is not a runbook. |
| 11 | 1:10 | [Zero Employees](https://www.youtube.com/watch?v=aH1IFjNLowI) | AITron | “Uber founder’s employee built a millions/year zero-staff company” | Product name garbled (“This is AI breaking ahead”). **Unverified marketing.** Skip. |
| 12 | 1:25 | [5 Plugins…](https://www.youtube.com/watch?v=QH4p9APni-w) | AITron | Strix, Omniroute, Agentic Reach, Find Skills, Claude Code Setup | Four of five map to real tools. “1.5 billion free tokens” is **marketing**. playlist-stack. |

How this was made: most AITron shorts are auto-dubbed / AI-generated. Transcripts garble names (`Agentic` = Agent Reach, `211 DEF` = 21st.dev). Always resolve to a GitHub/docs URL before installing.

## How agents should use this playlist

1. Do **not** treat a 60-second short as a procedure.
2. For each named tool, open the dedicated note (Soup, Agent Reach, playlist-stack).
3. Prefer `npx skills add <owner/repo>` / official `claude plugin …` over “paste this magic word in the prompt”.
4. On **Arena**, Agent Reach / CLI-Anything / OmniRoute are usually unnecessary: this environment already has web search, fetch, shell, and a sandbox. Soup needs a **local CUDA/MPS GPU**, not the Arena VM.

## Pitfalls

- **ToS / scraping.** Agent Reach and “scrape LinkedIn/X without API keys” reuse cookies or unofficial CLIs. That can ban accounts. Not for third-party systems you do not own.
- **Strix** is an *offensive* security agent (Kali sandbox). Only against systems you are authorized to test. This repo’s agents must not run it against random hosts.
- **OmniRoute “unlimited Claude”** is a local gateway over *other* providers’ free tiers. It does not mint Anthropic tokens.
- Playlist is **unlisted** and may grow/reorder; IDs above are the 2026-09-09 snapshot.
