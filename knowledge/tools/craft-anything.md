# storytold/craft-anything — inspect software, then rebuild (early alpha)

- **Tags:** storytold, artcraft, reverse-engineering, clean-room, claude-code, rust
- **Verified as of:** 2026-11-03
- **Sources:**
  - https://github.com/storytold/craft-anything (README on `main`; MIT **or** Apache-2.0)
  - Not [artcraft](../media/artcraft.md) (AI image/video studio). Not [coop-anything](../gamedev/coop-anything.md) (SP games → co-op).

## Кратко

**Craft Anything** — десктоп/CLI/MCP на **Rust** от той же конторы, что ArtCraft: тыкаешь в сайт/апп/игру → **Study → Build → Check → Ready**. Сборку делает **твой** coding agent (сейчас в первую очередь **Claude Code** на твоём логине). Статус README: **early alpha**. «Any software» — маркетинг.

Два режима: **Clean room** (дефолт) — только то, что видно снаружи (скриншоты, вёрстка, текст). **Deep** — код, файлы, JS, Ghidra. Их же правило: только софт, **который тебе можно смотреть**; DRM / логины / античит **не обходят**.

## What it actually is

| Piece | Notes |
| --- | --- |
| Engine | Pure-Rust RE/inspect: README claims **314** tools (native, .NET, Java, Android, Electron, web, firmware, games…). Own disasm/decomp; Ghidra optional in Deep |
| Surfaces | Desktop (egui; Simple + Advanced), `craft-anything-cli`, MCP (`craft-anything-cli mcp`) |
| Builder | Unmodified local `claude`. Codex adapter **unverified**. Other ACP agents listed; only **Maki** said to have been run live |
| Checks | Web: three viewport widths. Games: Unity/Unreal/Godot rebuilds “work today” (alpha). Behaviour checks for apps/games **partial** |
| Cost | App OSS. **Claude/API tokens yours.** fal.ai images/3D opt-in with **your** key. README “next: managed tier” |
| Build from source | Rust **1.97+**. Releases: Win/macOS/Linux/FreeBSD installers, still alpha |

Not PhotoCraft. Not “clone Adobe in one click”. Rebuilds are **new projects** from evidence; agent is told not to copy logos/photos/text without permission.

## How agents should use it

- User wants to **understand / recreate** a site they own or may inspect: point at GitHub + Clean room first. They run it **on their machine** with Claude Code.
- **This Arena session:** do **not** clone it and dump binaries, attach Ghidra, scrape logins, or rebuild a third-party product. We can explain the workflow.
- Deep mode + REA/Ghidra = same class as [coop-anything](../gamedev/coop-anything.md) path 2. No anti-cheat titles. No exploits.

## Pitfalls

- Alpha. Codex “adapter exists” ≠ works.
- Clean room ≠ legal clone. Look-and-feel / copyright still on the user.
- 314 tools ≠ all production-ready (`docs/tool-status.md`).
- Name collision: Craft Anything vs ArtCraft vs Crafting Apps (`photocraft`, …).
