# boykopovar/AnyPS5 — PS5 executable relinker (not an emulator)

- **Tags:** ps5, relinker, linux, windows, gpl2
- **Verified as of:** 2026-11-10
- **Sources:**
  - https://github.com/boykopovar/AnyPS5 (GPL-2.0-only; GitHub tagline: “automatic PS5 executables porting to Linux and Windows”)
  - README: relinker + replacement `prx` libs; “No emulation or separate runtime process”
  - Independent tracker (not upstream): https://anyps5.org/progress/ — listed **v0.1.4** (2026-10-30)

## Кратко

**AnyPS5** — open-source **релинкер**: берёт PS5-исполняемый файл, перекладывает в нативный формат Linux/Windows и линкует к **своим** реализациям системных `.prx`. Это **не** классический эмулятор (нет гостевой ОС/отдельного runtime) и **не** «любая игра с диска заводится». Ранняя серия **0.1.x**. К Sony не относится.

Репо **не** кладёт прошивку, ключи и копирайтные либы. Дисклеймер: бинарники — на совести пользователя и закона.

## What it actually is

| Claim in the wild | Reality |
| --- | --- |
| PS5 emulator | Relink + host implementations of known `libSce*` / libkernel exports. Shader path → SPIR-V (README) |
| Play any title | Compatibility is **per game**, in GitHub Discussions “Game bring-up”. Library % on badges = functions **declared in this repo**, not the whole OS |
| Web converter | README: [boykopovar.github.io/AnyPS5](https://boykopovar.github.io/AnyPS5/) — files stay in the browser |
| macOS | Relinker-only build, including Apple silicon — not a full Windows/Linux port stack |

Input: SDL pads; optional `anyps5-input.ini`.

Not Craft Anything, not Co-op Anything, not RPCS3/Kyty.

## How agents should use it

- Explain the **mechanism** (relink, not emulate). Do **not** give dump/decrypt/firmware/key steps, do **not** convert games, do **not** install it here.
- **Arena:** no. No game files, no relinker, no “web converter” of titles.
- User asks “will X run”: send them to **that title’s** discussion thread, not a yes.

## Pitfalls

- Running commercial PS5 software you don’t have rights to is still illegal, whatever the README says about “preservation”.
- Early alpha. “Converted” ≠ playable.
- Community mirrors (anyps5.org, anyps5.tools) are **not** the GitHub project.
