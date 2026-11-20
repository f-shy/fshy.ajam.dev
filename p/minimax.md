# MiniMax

> minimax.io | Inference, Compute, Coding subscriptions; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/minimax/ | JSON https://fshy.ajam.dev/api/v1/entity/minimax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MiniMax (minimax.io)

- `inference/minimax` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.minimax.io/docs/guides/quickstart
- free tier: No free text allowance stated; the quickstart requires account registration and an API Key, and offers pay-as-you-go or an M Plan subscription. The docs show Anthropic- and OpenAI-compatible base URLs. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: register or log in and create an API Key; no card or phone gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): per-usage billing; no free text tier stated [1]
- endpoint: https://api.minimax.io/anthropic/v1
- tooling: Anthropic SDK or OpenAI SDK by overriding the base URL
- composes with: no free tier published; usage requires a pay-as-you-go key or an M Plan seat or credits
- reliability: a Subscription Key can exist before paid resources are available but only becomes usable with an M Plan seat or credits
- notes: No self-serve free text allowance documented on the quickstart page.
- evidence:
  - [1] 2026-11-18: the API requires registration and a key, with pay-as-you-go or M Plan billing | capture: sha256:283b75b9b573c0e0cafb17ace907de3a157812ca396adbdda2c9793c19a8355a | quote: Before using the MiniMax API, you need to complete account registration and obtain an API Key.
- sources:
  - [1] https://platform.minimax.io/docs/guides/quickstart

## MiniMax Agent hosting / developer API scope

- `compute/minimax` | paid-only | evidence reported | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:27.000Z (live) | stale on 2026-11-06
- url https://platform.minimax.io/docs/llms.txt
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: rate limits are documented per user and client; the page links them but does not state a free tier [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the llms.txt index was read on 2026-10-22. It lists documentation rather than prices, and the record's own URL is an index file, so the paid-only verdict rests on the absence of a compute product rather than on a price page
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the product answers model and speech requests; there is no machine
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the documentation index was read on 2026-10-22 and lists the platform's model, speech, video and rate-limit pages; it publishes no free tier and no machine product
- sources:
  - [1] https://platform.minimax.io/docs/llms.txt

## MiniMax API Platform (platform.minimax.io)

- `inference/minimax-api-platform` | paid-only | evidence documented | binding none | category inference API, paid
- identity a placeholder: card and phone unknown | verified 2026-10-28T04:36:18.792Z (live) | stale on 2026-11-28
- url https://platform.minimax.io/docs/guides/pricing-paygo
- free tier: no free LLM allowance on the pay-as-you-go page: MiniMax-M3.1-Flash is USD 0.15 per 1M input and USD 0.60 per 1M output, and MiniMax-M3 carries a permanent 50% discount, not a free tier. The free items listed are input-side allowances on video tasks, such as the first 5 images per task, and free music generation APIs that are being discontinued | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: none
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: the sign-up requirements were not read; the pricing page links a Recharge Now balance page
- interface: rest
- limits note: no rate or quota is stated on the pricing page
- tooling: not stated
- composes with: pairs with an agent as a per-token paid model; the free music APIs are being discontinued
- reliability: from August 20, 2026 the paid music and lyrics APIs close to new users and the free music generation APIs are discontinued
- evidence:
  - [1] 2026-10-28: MiniMax-M3.1-Flash list price in USD per 1M input, output and cached read tokens | capture: sha256:ccf045dbf941dc6a2064d84cc2654c24e0106a501f6d3cf9ff75a4e3d51a9e47 | quote: | MiniMax-M3.1-Flash | $0.15 | $0.60 | $0.015 |
  - [1] 2026-10-28: the only free generation APIs listed are being discontinued | capture: sha256:ccf045dbf941dc6a2064d84cc2654c24e0106a501f6d3cf9ff75a4e3d51a9e47 | quote: The free music generation APIs (Music-3.0-free, Music-2.6-free, music-cover-free) will be discontinued.
  - [1] 2026-10-28: the first 5 input images per video task are free | capture: sha256:ccf045dbf941dc6a2064d84cc2654c24e0106a501f6d3cf9ff75a4e3d51a9e47 | quote: - Image input: The first 5 images per task are free; additional images are billed per image.
- sources:
  - [1] https://platform.minimax.io/docs/guides/pricing-paygo

## MiniMax Token Plan (minimax.io)

- `coding-subs/minimax-coding-plan` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://platform.minimax.io/docs/token-plan/intro
- free tier: No free tier. M Plan is a paid subscription for individuals with three tiers—Go, Explore, and Build—and the page states no prices and no free allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an M Plan or API account; the page names no card for signup and no free tier either way
- interface: rest
- limits:
  - volume-quota (binding): per-token billing with no free text allowance [1]
- endpoint: https://api.minimax.io/anthropic/v1
- tooling: the vendor console, its own agents, and an OpenAI-compatible key
- composes with: there is no free allowance to chain, so every call spends money
- reliability: the page says image and video models are subject only to the weekly usage limit, not the 5-hour limit; it states no prices
- evidence:
  - [1] 2026-11-18: the retired MiniMax-M3.1-Flash-Preview name is now served by MiniMax-M3.1-Flash | capture: sha256:5066155c189b75927fd7cf910a7c7044398cb5441468797f0cdd71fb6c602484 | quote: > MiniMax-M3.1-Flash-Preview has been retired. Requests using the old name are now served by MiniMax-M3.1-Flash.
  - [1] 2026-11-18: M Plan has three paid tiers and no free text allowance | capture: sha256:5066155c189b75927fd7cf910a7c7044398cb5441468797f0cdd71fb6c602484 | quote: it offers three flexible tiers—Go, Explore, and Build
  - [1] 2026-11-18: the retired preview model is redirected | capture: sha256:5066155c189b75927fd7cf910a7c7044398cb5441468797f0cdd71fb6c602484 | quote: > MiniMax-M3.1-Flash-Preview has been retired.
- sources:
  - [1] https://platform.minimax.io/docs/token-plan/intro
