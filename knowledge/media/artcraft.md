# storytold/artcraft — “IDE for artists” (desktop + web)

- **Tags:** artcraft, storytold, image-gen, video-gen, desktop, byok
- **Verified as of:** 2026-10-13
- **Sources:**
  - https://github.com/storytold/artcraft (README: MIT **or** Apache-2.0)
  - https://getartcraft.com/ and https://getartcraft.com/pricing
  - Related org apps (different repos): PhotoCraft / VectorCraft / FilmCraft / …

## Кратко

**ArtCraft** — десктоп/веб **студия для AI-картинок и видео** от storytold (сайт [getartcraft.com](https://getartcraft.com/)): 2D/3D композитинг, поза персонажа, image→mesh, потом рендер выбранной моделью. Реклама: «IDE for artists», не Adobe и не Claude-скилл.

**Приложение — бесплатное (MIT/Apache), подписка не нужна.** Платишь **только если** жжёшь **их облачные кредиты**. Свои ключи / свой compute / чужие подписки (Midjourney, fal, …) — можно без плана ArtCraft. Сноска на pricing: *“ArtCraft can be used without paying for a subscription. You can bring your own compute and third-party subscriptions.”*

## What it actually is

Not a coding agent. Not the PhotoCraft “Adobe clone” suite (those are **other** `storytold/*craft` repos). This repo is the **generation studio**: compose the shot, then call image/video/3D/audio models.

| Layer | Cost |
| --- | --- |
| Desktop/web app, source, local tools | **Free.** Dual MIT or Apache-2.0 (README on `main`, 2026-10). Downloads: getartcraft.com + GitHub Releases; Linux via build-from-source. |
| Generations **through ArtCraft’s catalog** | **Paid credits.** Plans (USD, listed 2026-10-13, promo −20% yearly): Basic ~$10/mo · 1 000 cr; Pro ~$35 · 3 750; Max ~$60 · 6 600. One-time packs **do not expire**. Failed gens refunded (their copy). |
| BYO | Midjourney (own login), fal (own API key) — recent desktop work. Pricing also says bring your own compute / third-party subs. |

Their hosted catalog (README) is large (Nano Banana, GPT Image, FLUX, Seedream, Kling, Veo, Sora, Hunyuan 3D, Marble, …). Many rows marked disabled/restricted on desktop — **do not treat the table as “all live”**.

Older search hits still quote a custom **“fair source” LICENSE.md**. On current `main` that file is **gone**; README points at `LICENSE-MIT` / `LICENSE-APACHE`. Re-read license if cloning an old commit.

Sep 2026: repo was **reset** (“fresh start”); old monorepo history lives in `storytold/artcraft-services`.

Community mirrors like getartcraft.app mix this studio with the Crafting Apps. Prefer GitHub README + getartcraft.com.

## How agents should use it

- User asks “is ArtCraft paid?” → **App no; their GPU/API yes, unless BYOK.**
- User wants Photoshop-in-Rust → send them **PhotoCraft / VectorCraft / …**, not this repo.
- **Arena:** we cannot run this GUI. Don’t clone it here expecting a compositor.
- Generated files are theirs (vendor claim); still bound by **each model’s** ToS (Midjourney, OpenAI, Kling, …).

## Pitfalls

- Name collision: ArtCraft studio vs Crafting Apps vs this Arena session.
- “Open source, yours forever” on the pricing page is **the client**. Credits are a **separate** Stripe product.
- Promo prices ($8 / $28 / $48 yearly) expire; list **list** rates when quoting.
- Not a drop-in Adobe CC. Crafting Apps are young clean-room editors; this studio is an AI compositor.
