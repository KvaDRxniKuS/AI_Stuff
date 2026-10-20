# cranebeaker/coop-anything — agent playbook to add co-op to single-player games

- **Tags:** coop, games, mods, claude-code, reverse-engineering, mcp
- **Verified as of:** 2026-10-19
- **Sources:**
  - https://github.com/cranebeaker/coop-anything (MIT, `main` active Oct 2026)
  - README FAQ + Rules; cousin: [CLI-Anything](../claude-code/playlist-stack.md) is **apps-as-CLI**, this is **SP games → co-op**

## Кратко

**Co-op Anything** — не готовый мультиплеер и не «нажал кнопку — любой тайтл в кооп». Это **скиллы + плейбук + MCP + каталог** для coding-агента (Claude Code / Codex / …): найти существующий кооп-мод и допилить, либо (если ничего нет) реверсить движок и собрать свой. Автор: cranebeaker. Реклама «any game» — **потолок амбиций**, не гарантия.

## What it actually is

| | |
| --- | --- |
| Install | Clone, tell the agent: read the GitHub URL, follow `AGENTS.md`, «I want to play \<game\> in co-op». Skills live in `.agents/skills` and `.claude/skills`. MCP: `python tools/mcp/coop_mcp.py` |
| Path 1 | Co-op mod exists but is dead/buggy → research, revive as a **separate** package, QA, Steam relay |
| Path 2 | Nothing exists → reverse engineer, second player, sync, networking, QA |
| Networking | Steam **Spacewar** relay (Valve test app) so friends join without port-forward. Everyone still **owns the game** |
| Split-screen | Points at Nucleus Co-op / PartyDeck, not a new engine |
| Binary RE | README pairs with [morluto/rea](https://github.com/morluto/rea) (`npx rea-agents setup`) |

Shipped/linked write-ups on the README (Oct 2026): Deus Ex (HX revive), Dungeon Keeper (KeeperFX), STALKER SoC fixes, FNV story co-op (preview), OoT (Ship of Harkinian fork). Plus a **DIRECTORY** of 230+ mods/gaps. Quality = whatever the agent shipped; not “official co-op”.

Rules in-repo: no game assets in this git; credit upstream mods; **co-op only**; **no cheating in other people’s multiplayer**; **don’t touch anti-cheat**. Their FAQ “is this legal?” is **community-modding rhetoric**, not a lawyer. EULAs and local law still apply.

## How agents should use it

- User wants this **on their PC** with a game they own: point at the GitHub + `AGENTS.md`. Prefer **path 1** (revive) over path 2.
- **This Arena session:** do **not** clone it and start Ghidra/Frida/Cheat Engine, dump binaries, or write hooks. No game install here. We may **read the playbook** and explain options.
- Do **not** follow path 2 for live anti-cheat titles (FromSoft online, etc.). Repo itself forbids touching anti-cheat.
- Don’t confuse with **CLI-Anything** (wrap desktop apps as CLI).

## Pitfalls

- “Any game” / “you don’t need to code” = marketing. Path 2 is weeks of RE and still may fail (Oracle of Seasons claim was closed untested).
- Steam Spacewar is a **hacky** invite channel, not a product Valve supports for this.
- Decomps/recomps (N64, etc.) have their **own** licenses and Nintendo/publisher risk.
- Don’t commit pirated ISOs or game files. Don’t bypass other players’ multiplayer.
