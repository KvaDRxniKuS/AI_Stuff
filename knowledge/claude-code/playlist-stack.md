# Claude Code stack named in the «Ии» shorts (verified)

- **Tags:** claude-code, plugins, skills, council, cli-anything, omniroute, strix
- **Verified as of:** 2026-09-09
- **Sources:** playlist transcripts (see [ii-ply8rck9gojyq.md](../playlists/ii-ply8rck9gojyq.md)) + upstream repos
- **Related:** [agent-reach.md](../tools/agent-reach.md), [soup.md](../tools/soup.md)

## Кратко

Из 12 роликов для агента полезны **не промпт-«коды»**, а несколько реальных репо. Ниже — только то, что удалось привязать к GitHub/докам. ASR в транскриптах врёт имена.

## 1. Prompt “codes” (video 1) — skip as a product

Transcript: **Landmine, Autopsy, Devil, V10, Bem**.

These are ordinary English steering phrases (“argue against this”, “list 10 variants”, “explain simply”). They are **not** Claude Code slash commands, not undocumented model flags, not `CLAUDE.md` keys. Real control surfaces: `CLAUDE.md`, `.claude/skills/`, `/plugin`, `/mcp`, `/compact`, `/model`, effort, subagents.

If the user wants the *effect*: write the instruction in plain language or a skill, do not depend on a magic token surviving translation.

## 2. CLI-Anything (video 9) — real

[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — generate an **agent-native CLI** for desktop software (Blender, LibreOffice, OBS, …) by reading the app/repo, instead of screenshot-click RPA.

```text
/plugin marketplace add HKUDS/CLI-Anything
/plugin install cli-anything
```

Web variant (HTTP capture, not source analysis): [ItamarZand88/CLI-Anything-WEB](https://github.com/ItamarZand88/CLI-Anything-WEB).

Token pitch in the short (“fewer tokens than MCP”) is plausible for a thin CLI vs screenshot loops, not a guarantee. Still requires the **target app installed**.

Anthropic also has **Computer Use** MCP on Claude Code (macOS, Accessibility + Screen Recording) — that is a different, official path for GUIs without a CLI.

## 3. Council skill (video 7) — real pattern, many repos

Karpathy-style propose → cross-examine → synthesize, implemented as **isolated Claude Code subagents** + a chairman. Community ports include:

- write-ups / plugins titled “Council” (five thinking styles + chairman HTML)
- [aiwithremy/claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council)

Heavy (5–6 extra agent calls). Use for **irreversible decisions**, not for naming a function. The short’s `/council` is not an official Anthropic command.

## 4. Design skills (videos 3, 6, 8)

Verified pieces:

| Name in short | Likely real thing |
| --- | --- |
| “Apple design language skill” | Community **apple-design** plugin, e.g. [tekgnosis-net/apple-design-marketplace](https://github.com/tekgnosis-net/apple-design-marketplace); plus Anthropic **frontend-design** skill |
| “211 DEF” | **[21st.dev](https://21st.dev)** component gallery (ASR) |
| “Hixfield MCP” | **Higgsfield** media gen, if an MCP exists — confirm before install |
| “CDEN 2.0” | **Unverified** |
| “Fable 5” | Claude **Fable** model line (set in Claude Code `/model`), not a GitHub tool |
| “taste skill” + browser loop | frontend-design / distinctive-UI skills + Playwright or computer-use |

Official-ish frontend skill: Anthropic `frontend-design` plugin (marketplace `anthropics/claude-code` or cookbooks). It fights generic “AI slop” UI; it does **not** make sites “Apple-level” by itself.

## 5. Five GitHub tools (video 5)

| Spoken name | Verdict |
| --- | --- |
| “Agent Skills, 87k★, spec/plan/build/test/review/release” | Matches the **skills + SDLC commands** idea. Star count smells like [obra/superpowers](https://github.com/obra/superpowers) / [anthropics/skills](https://github.com/anthropics/skills) — **re-check stars**, do not install from the short alone. |
| Book-to-Skill | Real converters: e.g. [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill), [Leutenegger/book-to-skill](https://github.com/Leutenegger/book-to-skill). Point at a PDF **the user owns**. |
| Cloudflare Computer | Likely Cloudflare **Sandbox / Workers** for a durable agent VM. Exact repo not pinned in the short. |
| “TencentDB Agent Memory” | **Unverified** as a public GitHub tool. |
| Authentik, “24k★” | Real IdP: [goauthentik/authentik](https://github.com/goauthentik/authentik). Self-hosted SSO (Auth0/Clerk alternative). **Not** a Claude Code plugin. |

## 6. Five plugins (video 12)

| Spoken | Real mapping | Notes |
| --- | --- | --- |
| **Strix** | OmniSecure **Strix** / `strix-claude-code` — Kali Docker + Claude as pentester | **Authorized targets only.** Do not run from this Arena session against third parties. Prefer SAST on *local* code. |
| **Omniroute** | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) / forks — local AI gateway, free-tier fallback | “1.5B free tokens/month” is a **ceiling anecdote**, not a contract. Default configs have been called out as insecure — read the repo security notes. Does not create extra Anthropic quota. |
| **Agentic Reach** | **Agent Reach** | [agent-reach.md](../tools/agent-reach.md) |
| **Find Skills** | Skill that shells out to `npx skills find` / skills.sh | Fine as a discovery helper; 90k “skills” is a directory scrape, quality varies. |
| **Claude Code Setup** | Official-ish Anthropic plugin that **recommends** hooks/skills/MCP for a repo | Read-only recommender. Good first install. Confirm current name with `/plugin` marketplace `anthropics`. |

## How agents should use this

On a **user’s Claude Code** machine, a sane subset of the shorts is:

1. Official setup / LSP / github / playwright plugins.
2. One design skill (`frontend-design` or apple-design) if they ship UI.
3. Agent Reach **only** if they need cookie-gated social platforms.
4. CLI-Anything **only** if they need a specific desktop app with no MCP.
5. Council for big decisions.
6. Soup ([soup.md](../tools/soup.md)) if they actually want a local fine-tune.

On **Arena**: none of the above are required for normal coding. Soup needs their GPU. Agent Reach cookies are not in the sandbox. OmniRoute is a local proxy.

## Pitfalls

- Shorts are ads for a “free course in the bio”. Ignore CTAs.
- Never install a plugin from a spoken name without the GitHub URL.
- Mixing 8 unrelated repos because a short said “five tools” creates a brittle Claude Code config.
