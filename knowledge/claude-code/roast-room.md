# nateherkai/roast-room — AI advisor council (not a comedy roast)

- **Tags:** claude-code, council, subagents, business
- **Verified as of:** 2026-10-22
- **Sources:**
  - https://github.com/nateherkai/roast-room (MIT, AI Automation Society / Nate Herk)
  - Cousins: [playlist-stack council](playlist-stack.md), [arena-skill](arena-skill.md)

## Кратко

**Roast Room** — Claude Code skill `/roast-room`: совет из **симуляций** публичных фигур (Bezos, PG, Hormozi, Buffett, …) спорит о **бизнес-решении**, ставит баллы, выдаёт вердикт + PDF. Локальный UI `localhost:4730` только **проигрывает** файлы из `sessions/` — сам модель не зовёт. **Не** стендап и не Arena.ai.

Скилл бесплатный (MIT). Токены — твой Claude-план. Полный совет 7 мест = **21** субагент (3 раунда × место). `--quick` = 4 места × 2 раунда.

## What it actually is

Was `/founder-council`. Default board of 7 + 5 on-call (Naval, Codie Sanchez, Leila Hormozi, Sara Blakely, Musk as of Oct 2026 README). Chair (main Claude) picks seats; you confirm.

Each seat = `.claude/agents/council-<name>.md` + “brain” from public letters/talks. Quotes checked against sources. README: **not the real people**, no endorsement.

| Flag | Effect |
| --- | --- |
| `--quick` | 4 seats, 2 rounds |
| `--seats a,b` | named seats only |
| `ask hormozi` | one seat |
| `--all` | up to 9 |
| `/newroaster Name` | scrape public work → new brain (~8–10 extra runs). Portrait via kie.ai optional |

Need: **Claude Code** + Node 20 for the room. Optional `COUNCIL_RUNNER=api` + Anthropic key ≈ 25 API calls / full council.

Forks exist (Italian, OmniRoute-in-browser). Pin **nateherkai/roast-room**.

## How agents should use it

- User wants this **here (Arena.ai):** do **not** clone and spawn 21 sub-agents. Offer a **tiny** analogue: 3–4 named viewpoints in one reply, or they run it in Claude Code.
- User has Claude Code: clone, `npm start` optional, `/roast-room` with **options + numbers**. Garbage in → 21 rounds of garbage.
- Irreversible bets only. Not for naming a function.

## Pitfalls

- **Not advice from Bezos.** Role-play on the same model family.
- Usage bites the plan. `--quick` first.
- `/newroaster` fetches the web/YouTube; you own what it stores in `build/` (gitignored).
- Same idea as “Council of Five Claudes” / arena-skill tournament — different packaging (celebrity brains + table UI).
