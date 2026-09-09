# Soup — fine-tune an 8B LLM on a 4 GB laptop GPU

- **Tags:** llm, finetune, lora, qlora, local-gpu, yaml, kazakhstan
- **Verified as of:** 2026-09-09
- **Sources:**
  - https://github.com/MakazhanAlpamys/Soup (~5.9k★, Apache-2.0)
  - https://trysoup.dev
  - https://pypi.org/project/soup-cli/
  - Paper: Makazhan, A. (2026). *Exact Layer Streaming…* https://doi.org/10.5281/zenodo.21771064 (v3 also on 10.5281/zenodo.21918325)
  - Playlist short: https://www.youtube.com/watch?v=_cxDr_t8PN4 (hype; do not trust its user-count)

## Кратко

**Soup** (`soup-cli`) — CLI: один YAML, `soup train`, LoRA/QLoRA дообучение. Фишка **layer streaming** (BETA, `stream_layers: true`): замороженный base сидит в RAM и гоняется на GPU **по одному decoder-слою**. Замер автора: Llama-3.1-8B-Instruct + NF4 + LoRA, batch 1, seq 512, RTX 3050 Laptop **4 GB** → пик **3.32 GB**, **119.6 tok/s**, bit-exact vs resident run. Это **не** полноценный pretrain и **не** «нейросеть рисует CAD». Python **3.10–3.12**.

## What it actually is

Author: **Alpamys Makazhan** ([MakazhanAlpamys](https://github.com/MakazhanAlpamys)), Kazakhstan. Package: `soup-cli`.

```bash
pip install "soup-cli[train]"   # bare soup-cli is CLI-only, no PyTorch
soup init --template chat
soup train
```

| Short / blog claim | Reality |
| --- | --- |
| “Retrain an LLM on 4 GB” | **LoRA on a quantized frozen base**, not full-weight training. |
| “85,000 users” (YouTube) | **Unverified.** GitHub ~5.9k stars / ~891 forks on 2026-09-09. |
| Always 4 GB | Default docs still say **8 GB+ VRAM for 7B QLoRA**. 4 GB path is **opt-in streaming + NF4**, small batch/seq. |
| Layer streaming is production | README: **BETA**. tok/s number is from **v0.72.2**; v0.73.0 correctness repair cost ~−4.8% at 32B and was **not re-run on 4 GB**. |
| Any GPU | CUDA recommended; MPS yes; CPU “experimental / very slow”. Free Colab T4 needed extra dtype fixes (v0.74). |

**Layer streaming:** frozen decoder layers live in host RAM (or NVMe if they do not fit); GPU holds two small VRAM buffers and the trainable adapter. Proof notebook: `notebooks/proof-4gb.ipynb` (caps process at 4 GB, asserts bit-identity vs resident).

Also in the CLI (beyond train): init templates, serve, merge, x-ray, recipes catalog. v0.74.0: frozen base was accidentally loaded fp32 on SFT paths (big VRAM win when fixed); `soup serve` now **exits 2** if bound off-loopback without `--tool-auth-token`.

## How agents should use it

Useful when the user wants a **domain-tuned local 7B/8B** (style, jargon, private docs) and has a NVIDIA laptop GPU.

1. Confirm Python 3.10–3.12 and `nvidia-smi`.
2. `pip install "soup-cli[train]"` in a venv.
3. `soup init --template chat`, point YAML at their JSONL/chat data.
4. For ≤4 GB cards: `training.stream_layers: true`, `quantization: 4bit`, batch 1, seq 512 as a starting point.
5. Do not run this inside **Arena** expecting a 4 GB NVIDIA GPU — the sandbox is CPU/cloud, not the user’s laptop.

Eval: compare against vanilla base on a held-out set. Streaming should match resident numerics; if it does not, turn streaming off and file upstream.

## Pitfalls

- **Data, not CLI, is the hard part.** Garbage JSONL → garbage adapter.
- **License of the base** (Llama, Qwen, …) still applies.
- Torch floor vs `trl>=0.29` can fail on pinned torch 2.5.x (upstream #651).
- `soup serve` + `/v1/tools/bash` is a shell. Bind loopback; require `--tool-auth-token` off-localhost.
- Do not confuse with HTML “soup” parsers or unrelated `soup` PyPI names — install **`soup-cli`**.
