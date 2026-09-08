#!/usr/bin/env python3
"""Restore a file from ai-stuff-chunked-v1 chunks.

Usage:
  python3 decode.py --input-dir ./incoming --output-dir ./restored
  python3 decode.py --manifest path/to/stem.manifest.json --output-dir ./restored
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
from pathlib import Path

PROTOCOL = "ai-stuff-chunked-v1"
PART_RE = re.compile(r"^(?P<stem>.+)\.part-(?P<n>\d{4})\.txt$", re.IGNORECASE)


def _die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def _load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("protocol") != PROTOCOL:
        _die(f"{path}: protocol {data.get('protocol')!r} != {PROTOCOL!r}")
    for key in ("original_filename", "original_size", "original_sha256", "chunk_count"):
        if key not in data:
            _die(f"{path}: missing {key}")
    if data.get("encoding") not in (None, "base64"):
        _die(f"{path}: unsupported encoding {data.get('encoding')!r}")
    return data


def _find_manifests(input_dir: Path) -> list[Path]:
    found = sorted(input_dir.rglob("*.manifest.json"))
    if not found:
        _die(f"no *.manifest.json under {input_dir}")
    return found


def _chunk_path(manifest_path: Path, stem: str, index_1: int) -> Path:
    return manifest_path.parent / f"{stem}.part-{index_1:04d}.txt"


def _stem_from_manifest_name(manifest_path: Path) -> str:
    name = manifest_path.name
    suffix = ".manifest.json"
    if not name.endswith(suffix):
        _die(f"unexpected manifest name {name}")
    return name[: -len(suffix)]


def _decode_chunk(path: Path) -> bytes:
    if not path.is_file():
        _die(f"missing chunk {path}")
    text = path.read_text(encoding="utf-8")
    compact = re.sub(r"\s+", "", text)
    try:
        return base64.b64decode(compact, validate=False)
    except Exception as exc:  # noqa: BLE001 — surface any decode failure
        _die(f"{path}: base64 decode failed: {exc}")


def restore_one(manifest_path: Path, output_dir: Path) -> Path:
    manifest = _load_manifest(manifest_path)
    stem = _stem_from_manifest_name(manifest_path)
    count = int(manifest["chunk_count"])
    expected_size = int(manifest["original_size"])
    expected_sha = str(manifest["original_sha256"]).lower()
    original_name = Path(str(manifest["original_filename"])).name
    if not original_name or original_name in {".", ".."}:
        _die(f"{manifest_path}: bad original_filename")

    parts: list[bytes] = []
    for i in range(1, count + 1):
        parts.append(_decode_chunk(_chunk_path(manifest_path, stem, i)))

    blob = b"".join(parts)
    if len(blob) != expected_size:
        _die(
            f"{manifest_path}: size mismatch restored={len(blob)} "
            f"manifest={expected_size}"
        )
    digest = hashlib.sha256(blob).hexdigest()
    if digest != expected_sha:
        _die(f"{manifest_path}: sha256 mismatch restored={digest} manifest={expected_sha}")

    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / original_name
    out.write_bytes(blob)
    print(f"ok  {out}  {len(blob)} bytes  sha256={digest}")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, help="directory containing manifests + chunks")
    parser.add_argument("--manifest", type=Path, help="single manifest path")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    if bool(args.input_dir) == bool(args.manifest):
        _die("pass exactly one of --input-dir or --manifest")

    if args.manifest:
        restore_one(args.manifest, args.output_dir)
        return

    manifests = _find_manifests(args.input_dir)
    for path in manifests:
        restore_one(path, args.output_dir)


if __name__ == "__main__":
    main()
