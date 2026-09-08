# earthtojake/text-to-cad — local CAD skills for coding agents

- **Tags:** cad, skills, arena, local, step, stl, urdf, build123d, cadgen
- **Verified as of:** 2026-09-08
- **Sources:**
  - https://github.com/earthtojake/text-to-cad
  - https://www.texttocad.dev
  - https://raw.githubusercontent.com/earthtojake/text-to-cad/main/README.md
  - https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md
  - https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/requirements.txt

## Кратко

Это **не** отдельная CAD-нейросеть вроде Zoo Text-to-CAD. Это **библиотека agent skills**: LLM пишет параметрический Python (`cadgen` + `build123d` / OpenCascade), ядро считает геометрию, наружу — STEP (и STL/3MF/GLB). Всё крутится **локально**, без своего бэкенда. Агенты, включая Arena, могут клонировать репо / поставить skills и моделировать в песочнице. Локальный CAD Viewer даёт превью в браузере.

## What it actually is

`earthtojake/text-to-cad` (site: [texttocad.dev](https://www.texttocad.dev), MIT) is a **skills library for CAD / CAE / CAM**. The agent is the "text-to-CAD" model: it authors a parameterless Python model script; `cadgen` builds validated CAD from that script.

Correction of a common misconception:

| Claim | Reality |
| --- | --- |
| "Neural net generates a mesh/B-rep" | No dedicated 3D generative model. Geometry is **constructed** by OpenCascade via `cadgen`/`build123d`. |
| "Cloud CAD API" | Designed to **run locally**. No hosted inference backend is required for the skills themselves. |
| "Just clone and talk" | You still need **Python 3.11+**, the pinned `cadgen` wheel, and (for preview) Node for the viewer. |

Observed on 2026-09-08: public GitHub page showed ~14.8k stars, latest merge on `main` 2026-09-05, CAD skill pin `cadgen[snapshot]==0.5.0`.

### Skills (as published on `main` / texttocad.dev)

| Skill | Role |
| --- | --- |
| **CAD** | NL or image → parametric `cadgen` model → STEP (primary); STL / 3MF / GLB optional |
| **CAD Viewer** | Local browser preview of STEP, meshes, DXF, URDF/SRDF/SDF, G-code |
| **step.parts** | Off-the-shelf STEP (screws, bearings, motors, …) |
| **DXF** | 2D profiles / cut layouts |
| **URDF / SRDF / SDF** | Robot structure, MoveIt groups, sim worlds |
| **SendCutSend** | Preflight DXF/STEP for that vendor |
| **DfAM Check** | Printability metrics |
| **G-code / Bambu Labs** | Slice with real slicer CLIs; cautious local print |

Older write-ups mention an experimental **Implicit CAD** skill and a "CAD Explorer" name. Current docs call the UI **CAD Viewer**. Trust installed `SKILL.md` over blog posts.

### How generation works (CAD skill, cadgen 0.5)

A model is a **parameterless decorated function**. Importing the module must not build; `__main__` calls the model.

```python
from cadgen import build123d as bd
from cadgen import step

WIDTH = 10.0

@step
def bracket():
    return bd.Box(WIDTH, 10, 10)

if __name__ == "__main__":
    bracket()
```

- `python bracket.py` writes `bracket.step` next to the script (or `out=` path).
- STEP is the document the inspect/snapshot tools read.
- Assemblies: `cadgen.assembly.AssemblyHelper` + build123d joints.
- Defaults unless specified: **mm**, XY base, +Z up, closed solids.

Useful CLI shape (from SKILL.md):

```bash
python <model>.py
cadgen step inspect ...
cadgen step snapshot ...
cadgen stl build ...          # also 3mf, glb
cadgen store why <model>.py
cadgen daemon status
cadgen doctor <skill-dir>
```

Scripts are RUN; `cadgen` subcommands take **documents** (STEP/STL/…) and never execute the `.py`.

## How agents should use it

### Preferred install (desktop agents: Claude Code, Codex, Gemini, …)

```bash
npx skills add earthtojake/text-to-cad
```

`add` refreshes installed skills **and** picks up newly published ones. `npx skills update` only walks the lockfile and can miss new skills.

Provider plugins also exist:

```bash
# Codex 0.142.0+
codex plugin marketplace add earthtojake/text-to-cad
codex plugin add cad@text-to-cad

# Claude Code
claude plugin marketplace add earthtojake/text-to-cad
claude plugin install cad@text-to-cad

# Grok Build
grok plugin install earthtojake/text-to-cad --trust
grok plugin enable cad
```

### Arena / generic sandbox (no Skills CLI wired to the product)

Arena does not ship these skills preinstalled. Treat the GitHub repo as a **runbook + dependency pin**, then work in the current workspace:

```bash
python3 --version   # want 3.11+
python3 -m pip install "cadgen[snapshot]==0.5.0"
# optional, for PNG snapshots:
python3 -m playwright install chromium
```

If pip pin 0.5.0 is gone, read the current
`https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/requirements.txt`
and install **that** pin. Optionally clone the repo for SKILL.md / examples, but do **not** require Git LFS (`models/` fixtures are not needed to generate new parts).

Workflow:

1. User describes a part / assembly / fixture.
2. Agent writes `src/…py` model scripts (parameters as module-level constants).
3. Run `python model.py` → STEP (+ declared meshes).
4. Inspect with `cadgen step inspect` / snapshot; iterate by editing source, not by hand-editing STEP.
5. For visual review, start CAD Viewer **bound to `0.0.0.0`** (see pitfalls).

If the sandbox cannot install `cadgen`/OCP (wheel size, missing OpenGL, no Python 3.11), say so and fall back to generating **build123d source only**, or to mesh-only formats the environment *can* produce.

### Why this is convenient on Arena

Arena agents already have a shell, Python, background processes, and a **live browser preview** for ports bound on `0.0.0.0`. That is enough for online CAD: generate STEP in the workspace, serve the viewer, let the user inspect in the preview iframe. No extra CAD SaaS.

## Pitfalls

- **Viewer bind address.** Upstream examples use `--host 127.0.0.1`. That **breaks Arena live preview**. Bind `0.0.0.0` and use relative URLs. The preview host is `https://{port}-{sandboxId}.e2b.app`.
- **Heavy native stack.** `cadgen` pulls OpenCascade/OCP. First install can be large and slow; may fail on tiny images.
- **Python version.** Badge/docs: Python **3.11+**.
- **Source of truth is the `.py`.** STEP/STL/GLB are derived. Edit the script, rebuild.
- **Do not confuse with Zoo.dev / other "Text-to-CAD" ML products.** Same slogan, different architecture.
- **Skill docs drift.** Always prefer the installed `SKILL.md` and `cadgen <cmd> --help`.
- **Large artifacts.** Generated STEP/STL can exceed chat upload limits. To *get a user file in*, use [chunked-file-ingest](../sandbox/chunked-file-ingest.md). To *get a model out*, prefer git/release/URL, or the same chunk protocol in reverse.

## Copy-paste: Arena first CAD part

```text
Install cadgen[snapshot]==0.5.0 (or the pin in earthtojake/text-to-cad skills/cad/requirements.txt).
Write a cadgen @step model for: <spec in mm>.
Run the script, then cadgen step inspect the STEP.
If a viewer is needed, start it on 0.0.0.0, not 127.0.0.1.
```
