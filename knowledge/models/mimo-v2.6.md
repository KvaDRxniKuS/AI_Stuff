# Xiaomi MiMo-V2.6 — open-weight omnimodal MoE (Sep 2026)

- **Tags:** llm, xiaomi, mimo, moe, open-weight, multimodal, agents
- **Verified as of:** 2026-09-30
- **Sources:**
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL (official card)
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL
  - https://huggingface.co/collections/XiaomiMiMo/mimo-v26
  - https://mimo.xiaomi.com/mimo-v2-6
  - https://platform.xiaomimimo.com/
  - Org: https://huggingface.co/XiaomiMiMo · https://github.com/XiaomiMiMo

## Кратко

**MiMo-V2.6** — семейство моделей **Xiaomi MiMo**, не отдельный «чатбот-сайт». Open-weight, **MIT**, нативно **текст + картинка + видео + аудио**, контекст **1M токенов**. Флагман **Pro-RL**: sparse MoE **1.02T total / 42B active**. Дешевле/быстрее: **Flash-RL** (~309–311B / 15B active). Есть **9B distill** на Qwen3.5 (для RL-исследований, не как замена Pro). API: `mimo-v2.6-pro` / `flash` / `pro-ultraspeed`. Это **не** MIMO из радиосвязи и не MiMo-7B 2025 года.

## What it actually is

Xiaomi’s MiMo line: 7B (2025) → V2-Flash → V2.5 → **V2.6** (weights ~**2026-09-21/22**). Pitch: scale **one mixed RL run** (“You Only RL Once”) across coding, general agents, vision, cybersecurity instead of separate RL jobs per domain. GRPO, large batches, groupwise graders.

| Checkpoint | Shape (from Xiaomi card / HF) | Role |
| --- | --- | --- |
| **MiMo-V2.6-Pro-RL** | 1.02T MoE, **42B** active, 384 experts / 8 on, 70 layers (60 SWA + 10 global), hidden 6144 | Flagship |
| **MiMo-V2.6-Flash-RL** | ~309–311B / **15B** active | Throughput / cost |
| **Pro UltraSpeed** | Same Pro, speed-tuned **API** SKU | Latency; weights not a separate HF card |
| **Distill-Qwen-9B** | Dense SFT of **Qwen3.5-9B** on MiMo data | Research / small GPU, not a 1T substitute |

Also on the Pro card: 681M ViT, audio tokenizer (~308M) + patch encoder (~127M), 5-layer MTP speculative decoder (drafts 7 tokens). Max context **1M**. HF license on Pro-RL: **mit**.

Vendor eval table (same card) compares to Claude Opus 5 / GPT-5.6 Sol / Claude Fable 5 on *their* agent benches. Treat as **Xiaomi numbers**, not an independent league table. Third-party writeups cite Artificial Analysis Intelligence Index ~46 for Pro — re-check AA if ranking matters.

## How agents should use it

- **API (typical):** Xiaomi OpenAI-compatible `https://api.xiaomimimo.com/v1` (confirm current base URL on the platform). Model ids reported: `mimo-v2.6-flash`, `mimo-v2.6-pro`, `mimo-v2.6-pro-ultraspeed`. Also listed on OpenRouter / some gateways.
- **Self-host:** SGLang or vLLM with `--trust-remote-code`. Pro serving examples use **multi-node / high TP** (card shows `--tp 16` / 2 nodes). Not a laptop model. Flash is still a large MoE.
- **9B distill:** only if the user wants a small agentic-RL starting point.
- **Arena:** no 1T GPU here. Use the user’s API key if they ask; do not pretend local weights are installed.

Pricing (catalogs ~2026-09, **re-check** `platform.xiaomimimo.com`): Flash ~$0.14 / $0.28 per 1M in/out (cache-miss); Pro ~$0.435 / $0.87; UltraSpeed ~10× Pro. Cache-hit input is much cheaper. V2.5 API was announced for deprecation (migration window toward late Oct 2026 in third-party notes).

Same-week Xiaomi **MiMo Code** CLI (0.1.15) got multimodal Read + tool-call gating — a *product*, not the weights.

## Pitfalls

- **Do not confuse** with older **MiMo-7B** or the generic GitHub org README (still 7B-era).
- Flash param count **309B vs 311B** depending on HF vs blogs — same model family, don’t bikeshed.
- 1M context is a **max**; serving config, KV cache, and bill dominate.
- Benchmarks vs Claude/GPT on the card are **in-house**. Cyber/agent scores can look wild; read the bench.
- `trust_remote_code=True` on HF pipelines — review custom code before running untrusted.
- Arena/Claude Code default stack is not MiMo; switching models is a user/API choice.
