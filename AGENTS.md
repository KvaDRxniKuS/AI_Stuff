# AGENTS.md — how to use this knowledge library

This repository is a **durable knowledge base for AI agents**. Read it at the start of a session when the user is doing CAD, Arena/sandbox file transfer, or anything listed in `knowledge/INDEX.md`.

## Rules

1. Treat `knowledge/` as the source of truth for *this* project's notes. External tools change; if a note has a `Verified as of` date, re-check the upstream URL when the date is stale.
2. Prefer the English body of each note. A Russian `Кратко` block is for humans and for Russian-language retrieval.
3. When the user adds a new "interesting thing", append a note under `knowledge/` (one topic per file), add a row to `knowledge/INDEX.md`, and keep the same template:
   - title, tags, verified date, sources
   - what it actually is (correct misconceptions)
   - how an agent should use it
   - pitfalls / Arena-specific gotchas
   - copy-paste commands
4. Do not dump huge generated CAD artifacts or datasets into git. Point to generators, skills, or the chunked-ingest protocol instead.
5. Working files and helper tools live in `tools/`. Knowledge *about* those tools lives in `knowledge/`.

## Session start checklist

- [ ] Skim `knowledge/INDEX.md` for tags matching the user's request.
- [ ] Open the matching note(s); follow their agent workflow, not a guessed one.
- [ ] If you learn a correction, update the note in the same session.

## Note template

```markdown
# Title

- **Tags:** …
- **Verified as of:** YYYY-MM-DD
- **Sources:** …

## Кратко
…

## What it actually is
…

## How agents should use it
…

## Pitfalls
…
```
