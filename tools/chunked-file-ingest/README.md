# chunked-file-ingest

Browser encoder + stdlib decoder for protocol `ai-stuff-chunked-v1`.

Full rationale: [`knowledge/sandbox/chunked-file-ingest.md`](../../knowledge/sandbox/chunked-file-ingest.md).

## Encoder (user machine)

1. Download [`encoder.html`](encoder.html).
2. Open the download in a browser (`file://`). Do not rely on an Arena live preview — that page cannot read the user's disk.
3. Pick a file, choose chunk payload size, download zip or individual parts.
4. Attach `*.manifest.json` and `*.part-NNNN.txt` in chat.

## Decoder (agent sandbox)

```bash
python3 tools/chunked-file-ingest/decode.py --input-dir ./incoming --output-dir ./restored
```
