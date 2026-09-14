# Claude “leaked” system prompts — what the shorts actually point at

- **Tags:** claude, fable, system-prompt, leaks, anthropic
- **Verified as of:** 2026-09-14
- **Sources:**
  - Short (AITron, Made with AI): https://www.youtube.com/watch?v=qgl4LKzfsf0
  - https://github.com/asgeirtj/system_prompts_leaks (~66k★) — `Anthropic/claude-fable-5.1.md`
  - Earlier Fable 5 capture: https://github.com/elder-plinius/CL4R1T4S (`ANTHROPIC/CLAUDE-FABLE-5.md`)
  - Anthropic also publishes *official* `claude_behavior` snapshots: https://platform.claude.com/docs/en/release-notes/system-prompts

## Кратко

Ролик: «слили секретный системпромт Claude Fable 5.1, 275 000 символов, ~8000 строк, публичный GitHub».  
Факт: **архив извлечённых промптов существует** и давно публичный. Это не взлом Anthropic. Файл Fable 5.1: **7810 строк, 405 KB** (на 2026-09-01). «275k символов» не совпадает с размером файла. Копировать целиком в своего агента бессмысленно: это операторские инструкции **claude.ai** (тулы, классификаторы, safety), не универсальный гайд по промптингу.

## What it actually is

| Short claim | Check |
| --- | --- |
| Just leaked | Fable **5** dump: June 2026 (Pliny / CL4R1T4S, ~1.6k lines). Fable **5.1** file in `system_prompts_leaks`: **2026-09-01**. Short: **2026-09-13**. Not news. |
| Secret | Community extracts + Anthropic’s own published system-prompt notes. “Secret” is the thumbnail. |
| 275 000 characters, ~8000 lines | GitHub metadata: **7810 lines (6918 loc) · 405 KB**. 8k lines ≈ ok. 275k chars ≠ 405 KB. |
| Use it to “upgrade your prompting” | Read for **structure** (tools, refusals, memory phrasing). Do **not** paste the XML stack into another model. |

Two different surfaces:

- **claude.ai / apps** — `claude-fable-5.1.md` (chat, artifacts, memory, wellbeing).
- **Claude Code** — separate files in the same repo (`Anthropic/Claude Code/…`). Not the same prompt.

## How agents should use it

1. If the user wants to *study* product prompts: open the GitHub file, don’t vendor 400 KB into this repo.
2. Prefer Anthropic’s **official** system-prompt release notes when they exist.
3. For our own agents: keep short `AGENTS.md` / skills. Copying Fable’s prompt will fight Arena/Claude Code’s real system prompt and waste context.

## Pitfalls

- Same AITron CTA as the «Ии» playlist.
- “Leak” repos can mix verbatim captures, reconstructions, and stale diffs. Treat as **unofficial**.
- Pasting leaked prompts into third-party products can violate Anthropic ToS; we don’t mirror the text here.
