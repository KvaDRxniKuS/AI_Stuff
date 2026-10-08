# Jakeschincariol/arena-skill — `/arena` tournament (not Arena.ai)

- **Tags:** claude-code, skills, subagents, tournament, council
- **Verified as of:** 2026-10-07
- **Sources:**
  - https://github.com/Jakeschincariol/arena-skill (README + MIT LICENSE; first commit 2026-09-26)
  - Short: https://www.youtube.com/shorts/vuYZV9ZxHSM — Кирилл Жильников, title matches the README slogan

## Кратко

Реальный **Claude Code skill** (MIT, Jake Schincariol): `/arena` поднимает **N субагентов одной и той же модели** (дефолт **100**, `--quick` = 16), каждому одна и та же задача + разная «карточка» стратегии, дальше **олимпийка**: атака → защита/ревизия → судья по рубрике. Победитель — тот, кто выжил, не «доказанно лучший ответ в мире».

**Не** Arena.ai Agent Mode. Имя совпало. Этот чат — Arena.ai; скилл крутится только в **Claude Code**.

## What it actually is

| Claim in the short | Reality |
| --- | --- |
| «100 версий Claude сражаются» | 100 **sub-agents of the model you already run**, not 100 different models |
| «бесплатный скилл» | Repo **MIT**, no signup. **Tokens are yours.** Default 100-agent run ≈ **595** Agent-tool calls (README table) |
| «выдаёт лучший ответ» | Survivor of a **Claude-judged** bracket + written rubric. Same model family judging itself |
| Needs Arena.ai | **No.** Needs **Claude Code** Agent tool + **Python 3.8+**. Nothing to pip install |

Deck: 15 reasoning modes × 12 workflows × 12 strategies = **2,160** cards, no repeats. Isolation: work in **`.arena/`**, README says it **never touches your files**; you apply the winner yourself.

Install (Claude Code only):

```text
/plugin marketplace add Jakeschincariol/arena-skill
/plugin install arena-skill@arena-skill
```

Plugin command is namespaced: `/arena-skill:arena`. Plain `/arena` = copy `skills/arena` into `~/.claude/skills/` or `.claude/skills/`.

Everyday: **`--quick` (16 agents, ~91 calls)**. Full 100 is a bill, not a vibe.

Related, smaller: “Council of Five Claudes” in [playlist-stack](playlist-stack.md) — same *multi-persona* idea, not this bracket.

## How agents should use it

- User wants this **here (Arena.ai):** do **not** clone it and spawn 100 sub-agents. We are not Claude Code; we have no `/arena`. Offer a **tiny** analogue: 2–4 distinct approaches in one reply, or they run the skill in Claude Code.
- User runs **Claude Code:** point at the GitHub README. Prefer `--quick` unless they accept hundreds of calls.
- Name collision: “Arena skill” ≠ this product (Arena.ai). Ask which they mean.

## Pitfalls

- **Cost.** Skill free ≠ run free. 100 default is ~70 waves of 10.
- **Self-play.** Judges are the same model; tournament can converge on fluent consensus, not truth.
- **Does not edit the repo** by design — winner is text in `.arena/`.
- Other GitHub “arena” skills exist (e.g. worktree bake-offs). Pin **Jakeschincariol/arena-skill** if this short is the source.
