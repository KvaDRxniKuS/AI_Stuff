# Cheap-model routing — “Claude as a loader on your dime”

- **Tags:** claude-code, routing, tokens, omniroute, subagents
- **Verified as of:** 2026-10-19
- **Sources:**
  - Short: https://www.youtube.com/shorts/_W1Gr5XH42M — Бади Ворлд Шортс, 2026-10-17. Title: «Почему твой Claude работает грузчиком за твои же деньги?» / EN oEmbed: “delivery boy on your dime”. Description is **channel boilerplate**, no GitHub. Comments describe the pitch.
  - Native: Claude Code subagents + `/model` (Haiku/Sonnet/Opus/Fable)
  - Class of third-party tools (none named in the short): OmniRoute, [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router), [AqueGen/model-routing](https://github.com/AqueGen/model-routing)

## Кратко

Шортс **не называет репо**. Смысл из тайтла + комментов: не гоняй дорогой Claude (Opus/Fable) на «грузчицкую» работу (поиск файлов, рутина) — отдай дешёвым моделям, мозг оставь дорогим.

**Паттерн настоящий. Волшебного −95% нет.** В Claude Code это уже есть: субагент с более дешёвой моделью. Сторонние роутеры (CCR, OmniRoute) подменяют endpoint. Дешёвая модель часто пишет мусор → Claude переписывает → **токенов больше**.

## What it actually is

| Claim | Reality |
| --- | --- |
| Claude «работает грузчиком за твои деньги» | Premium model **does** cost more per token. Grunt work on Opus is wasteful **if** a weaker model would have done it **and** you don’t redo it |
| One GitHub/skill fixes the bill | **Not named.** Dozens of routers/skills. Don’t install from a 60s title |
| Free/cheap nets = same code | Comments on this short: cheap nets write code Claude rejects; loop eats **more** quota |
| Native Claude can’t do this | False. Spawn a subagent with Haiku/Sonnet; or `/model`. Commenter: “Opus, выноси в подзадачи, сам выберет Sonnet/Fable” |

Honest third-party note ([AqueGen/model-routing](https://github.com/AqueGen/model-routing)): a subagent starts **empty**. Delegation turns cheap **cache reads** in the main session into expensive **first reads**. Routing saves money if you **already** delegate a lot; it can **cost more** if you mostly work in one session.

OmniRoute / CCR: local gateway, mix providers. Same class as playlist #12/#31. Not extra Anthropic quota. Default configs have been called insecure — read the repo.

## How agents should use it

- User sends this short: **don’t clone a random router.** Explain native `/model` + subagents first.
- They already run Claude Code and want routing: name **one** repo after they pick (CCR vs native vs OmniRoute). Don’t stack three.
- **Arena:** we are not Claude Code. No CCR here. We already pick a model per session.

## Pitfalls

- **Redo tax.** Cheap implementer + expensive reviewer can beat “all Opus” **or lose**.
- **ToS / keys.** Pointing Claude Code at a third-party proxy = your prompts go there.
- Channel CTA is generic “subscribe to AI tips”, not a runbook.
