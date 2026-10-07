# blueprintUE — Pastebin for Unreal Engine Blueprints

- **Tags:** unreal, blueprint, gamedev, pastebin, ue5
- **Verified as of:** 2026-10-07
- **Sources:**
  - https://blueprintue.com/ (tagline: “PasteBin For Unreal Engine”)
  - Tools: https://blueprintue.com/tools/
  - Self-host: https://github.com/blueprintue/blueprintue-self-hosted-edition
  - UE plugin: https://github.com/blueprintue/blueprintue-cpp-plugin
  - `.uasset` JS reader: https://github.com/blueprintue/uasset-reader-js

## Кратко

**blueprintUE** — не движок и не генератор игр. Это **Pastebin для графов Unreal Blueprint**: копируешь ноды в редакторе UE (`Ctrl+C`), вставляешь текстовый буфер на сайт, он рисует граф. Другой человек жмёт Copy → `Ctrl+V` обратно в Blueprint editor. Public / unlisted / private. Версии UE на форме: **4.0–4.27 и 5.0–6.0**.

## What it actually is

Unreal stores copied graph nodes as **plain text on the clipboard**. The site stores that blob, renders a web preview, and hands the same text back.

Workflow:

1. In UE Blueprint (or Material) graph: box-select nodes → copy.
2. Paste into https://blueprintue.com/ → “Create your blueprint”.
3. Share the URL. Recipient: “Code to copy” → paste in UE.

Exposure: **Public / Unlisted / Private (members)**. Expiry: never / 1h / 1d / 1w. Types on the homepage include **blueprint** and **material**.

Extra tools (official `/tools/`):

| Tool | Repo |
| --- | --- |
| Self-hosted site (company pastebin) | `blueprintue/blueprintue-self-hosted-edition` (Docker) |
| C++ plugin: send BP from editor | `blueprintue/blueprintue-cpp-plugin` (listed UE 4.26–5.4 on the tools page — re-check for 5.5+) |
| JS `.uasset` reader (dev) | `blueprintue/uasset-reader-js` |

Not CAD, not `text-to-cad`, not a substitute for Unreal itself.

## How agents should use it

- User wants to **share / archive / review** a Blueprint: tell them this clipboard loop. Do **not** invent UE graph JSON; the paste format is UE’s own clipboard dump.
- User pastes a blueprintue.com URL: fetch the page, extract the copy-buffer if present, explain nodes in words. Recreating a working graph **without Unreal** is guesswork.
- **Arena:** no Unreal Editor here. Generate/explain graphs as text or screenshots; they paste in UE on their machine.
- Private studio graphs: prefer **self-hosted**, not public pastebin.

## Pitfalls

- Public pastes are searchable. Don’t dump proprietary game logic.
- Clipboard format is **version-sensitive**. Set the matching UE version; paste into a much older/newer editor can fail.
- Plugin version list on `/tools/` may lag current UE.
- Facebook/Google OAuth on the marketing site was already being shut down (blog 2024); account = username/password or self-host.
