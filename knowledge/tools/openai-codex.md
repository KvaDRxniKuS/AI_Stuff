# OpenAI Codex — coding agent (not the 2021 model)

- **Tags:** openai, codex, cli, agents, claude-code-competitor
- **Verified as of:** 2026-10-07
- **Sources:**
  - https://github.com/openai/codex — “Lightweight coding agent that runs in your terminal”
  - https://developers.openai.com/codex/guides/agents-md
  - https://developers.openai.com/codex/cli/reference

## Кратко

Сегодня **Codex** — это **агент OpenAI для кода**, прямой аналог **Claude Code**: читает репо, правит файлы, гоняет шелл, MCP, skills, `AGENTS.md`. CLI на GitHub **open source (Rust)**. Не путать с **Codex 2021** (модель дополнения кода на базе GPT-3, Copilot; API снят ~2023).

## What it actually is

Two eras, same brand:

| | **Codex (2021)** | **Codex (2025–2026)** |
| --- | --- | --- |
| What | Completion **model** | **Agent product** + CLI/IDE/cloud |
| Loop | prompt → snippet | task → edit files → run commands → (often) PR |
| Where | API / Copilot | `codex` CLI, IDE extension, ChatGPT/cloud sandbox |
| Status | Deprecated | Current OpenAI coding agent |

Official CLI repo: [openai/codex](https://github.com/openai/codex). Install is typically `npm i -g @openai/codex` (or native installers — check the README). Auth: ChatGPT plan and/or API key.

Project memory: **`AGENTS.md`** (global `~/.codex/AGENTS.md`, then repo, then nested `AGENTS.override.md`). `/init` scaffolds it. Same idea as our repo’s `AGENTS.md` and Claude’s `CLAUDE.md`.

Also in this knowledge base: earthtojake/text-to-cad installs as a **Codex plugin** (`codex plugin marketplace add …`). Skills CLI / MCP work across Codex and Claude Code.

Models behind the agent change (GPT-5.x, then GPT-6 Astra/Sol/Luna in 2026 writeups). Do not pin a model name without checking `/model` or current docs.

## How agents should use it

- If the **user** runs Codex on their machine: it’s their Claude Code equivalent. Point them at `AGENTS.md`, plugins, sandbox approvals.
- **This Arena session is not Codex.** We are a different agent runtime. Don’t tell them to type `codex` here expecting OpenAI’s CLI.
- Don’t confuse “Codex” in a YouTube short with GitHub Copilot or the 2021 API.

## Pitfalls

- Name collision: Codex Alimentarius, other “codex” tools.
- CLI is local; cloud Codex clones a repo into **OpenAI’s sandbox** — different trust model than “files stay on my disk”.
- Comparisons to Claude Code are close and move monthly; pick by account (ChatGPT vs Claude), not by last week’s bench tweet.
