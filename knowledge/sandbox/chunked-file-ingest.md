# Chunked HTML encoder — get large / disallowed files into an agent sandbox

- **Tags:** arena, sandbox, upload-limits, base64, html, files
- **Verified as of:** 2026-09-08
- **Sources:**
  - User-reported Arena/agent workflow (this repo)
  - Helper implementation: [`tools/chunked-file-ingest/`](../../tools/chunked-file-ingest/)
  - Arena help mentions upload errors can be caused by **file size** and **count**, without publishing a hard byte cap: https://help.arena.ai/articles/1116755327-arena-troubleshooting-file-upload-error
- **Status:** Technique verified as a sound systems workaround. Exact Arena byte/type caps are **not** publicly documented; treat chunk size as configurable.

## Кратко

Чат/песочница часто режет **размер** и **тип** вложений (бинарники, большие STEP/STL/zip). Обход: агент отдаёт одностраничный **HTML-кодировщик**. Пользователь открывает его локально, выбирает любой файл, браузер режет его на куски **допустимого формата и размера** (обычно `.json` / `.txt` с base64). Куски прикладываются в чат. Агент в песочнице склеивает и декодирует — исходный байтовый файл оказывается в workspace, минуя лимит одного вложения.

Это не взлом и не обход auth: пользователь сам дробит **свой** файл и явно загружает части.

## What it actually is

Agent products (Arena included) typically constrain **inbound** files by:

1. **Per-file size** (chat attachment or platform upload).
2. **MIME / extension allow-list** (images + text, but not `.step` / `.stl` / `.bin` / `.zip`).
3. **Count per message**.

They do **not** usually cap the total bytes the agent can `open()` after files are already in the workspace. So:

```
large arbitrary file
    → browser HTML encoder (no server)
    → N small allow-listed text chunks + 1 manifest
    → user uploads chunks to the agent
    → sandbox decoder concatenates + base64-decodes
    → original bytes on disk, SHA-256 checked
```

### What this does *not* bypass

- Workspace / snapshot caps (Arena notes ~128 MB combined patchset and excluded dirs). A 2 GB reconstruction may still not persist.
- Context-window limits. Do **not** paste megabytes of base64 into the chat body; **attach** chunk files (or have the user drop them into a folder the agent can read).
- Network egress policy. If the file is already at a URL, `curl`/`wget` is simpler than chunking.
- License / confidentiality. Chunks are still the user's data.

### Prefer these before chunking

1. File already on GitHub/HTTP → agent fetches it.
2. File fits the allow-list and size cap → attach normally.
3. Only then: chunked ingest.

## Protocol `ai-stuff-chunked-v1`

All integers are decimal. Hashes are lowercase hex SHA-256 of the **raw original bytes**.

**Manifest** (`<stem>.manifest.json`):

```json
{
  "protocol": "ai-stuff-chunked-v1",
  "original_filename": "widget.step",
  "original_size": 18432011,
  "original_sha256": "ab…",
  "encoding": "base64",
  "chunk_encoding": "utf-8",
  "chunk_ext": ".txt",
  "chunk_count": 12,
  "chunk_payload_bytes": 400000,
  "created_utc": "2026-09-08T17:00:00Z"
}
```

**Chunks** (`<stem>.part-0001.txt` … zero-padded 4 digits, 1-based): each file is **only** the base64 alphabet plus optional newlines (ignore whitespace on decode). Chunk *i* is `base64(original[start:start+payload])` where `start = (i-1) * chunk_payload_bytes` of the **raw** file (chunk, then encode — do not encode the whole file then split, which breaks padding).

Default `chunk_payload_bytes`: **400000** (~533 KB of base64 text). Tune down if uploads still fail; tune up if the UI allows 1–2 MB text.

Optional extra: encoder can also emit a single `.json` wrapping `{manifest, chunks:["b64",…]}` when the whole file is small enough for one attachment.

## How agents should use it

### A. User needs to send a large local file **in**

1. Write or `present_file` [`tools/chunked-file-ingest/encoder.html`](../../tools/chunked-file-ingest/encoder.html) (self-contained; user opens it as a `file://` page).
2. Tell the user:
   - open the HTML locally (download it first if the preview sandbox cannot read their disk);
   - pick the file, set chunk size if needed;
   - download the zip **or** the individual `.txt` + manifest;
   - attach those files in the next message (several rounds if count-capped).
3. In the sandbox, run:

```bash
python3 tools/chunked-file-ingest/decode.py --input-dir ./incoming --output-dir ./restored
```

4. Confirm printed SHA-256 matches the manifest. Then work on the restored file.

If `encoder.html` is not in the tree, regenerate an equivalent page from this protocol. The decoder is stdlib-only.

### B. Agent needs to send a large file **out**

Reverse the same protocol: split in the sandbox, give the user the HTML **decoder** (the encoder page includes a decode mode) or a zip of chunks. Do not dump base64 into the model context.

### C. Implementation constraints for Arena

- Generate the HTML in-workspace and open it with `present_file`.
- User's browser is **not** the sandbox: the encoder must run **on the user's machine** so it can read local files. A live-preview HTML on `e2b.app` cannot see the user's disk (browser security). Instruct: "Download `encoder.html`, open the download, then choose the file."
- After chunks are attached, they appear as workspace files — decode there.

## Pitfalls

- **Split-then-base64, not base64-then-split.** Splitting a single base64 string on a fixed byte length can cut in the middle of a quartet.
- **Newlines.** Some UIs reflow text files. Decoder must strip whitespace.
- **Filename collisions / sanitization.** Keep `original_filename` in the manifest; do not trust chunk names for the restored name beyond the stem convention.
- **Partial uploads.** Decode must fail if `chunk_count` files are missing or any SHA mismatches.
- **Double encoding.** Do not wrap already-base64 content again.
- **Image-only UIs.** If only images upload, this text protocol will not work; a pixel-packing variant would be a different note. Not implemented here.

## Copy-paste prompt (give this to the user)

```text
Скачай encoder.html, открой файл локально в браузере, выбери большой файл.
Скачай манифест и куски (или zip), затем прикрепи их сюда.
Я восстановлю оригинал в песочнице и сверю SHA-256.
```
