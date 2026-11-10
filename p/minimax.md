# MiniMax Agent

> minimax.io | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/minimax/ | JSON https://fshy.ajam.dev/api/v1/entity/minimax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

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
