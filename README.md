# AI_Stuff

Durable **knowledge library for AI agents**. Humans dump interesting tools and workarounds here; agents expand them into checkable notes so later sessions do not rediscover the same facts.

- Notes: [`knowledge/INDEX.md`](knowledge/INDEX.md)
- How agents should read/write this repo: [`AGENTS.md`](AGENTS.md)
- Helper tools: [`tools/`](tools/)

Пиши новые темы агенту обычным языком — он проверяет факты и кладёт карточку в `knowledge/`.

## Contents

| Topic | Why it is here |
| --- | --- |
| [text-to-cad](knowledge/cad/text-to-cad.md) | Local CAD via agent skills (`cadgen` / build123d), not a 3D generative net. Runnable in Arena. |
| [chunked file ingest](knowledge/sandbox/chunked-file-ingest.md) | HTML encoder splits any file into allow-listed chunks so sandboxes can reconstruct past upload caps. |
