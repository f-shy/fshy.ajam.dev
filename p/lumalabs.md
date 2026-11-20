# Luma AI

> lumalabs.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lumalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/lumalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Luma AI

- `compute/luma-ai` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://lumalabs.ai/pricing
- free tier: The published individual plans begin at Plus, 'USD 30/month ... 10,000 credits', with Pro at USD 90 for 40,000 and the top individual plan at USD 300 for 150,000. No free plan is listed. The rate card prices Ray3.2 at '50 credits/5 sec' for 540p, '100 credits/5 sec' for 720p and '400 credits/5 sec' for 1080p, and the Draft tier at '20 credits/5 sec'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-published
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): there is no free lane on the pricing page: the first credit costs USD 30 for 10,000, and 10,000 credits at 100 a five-second 720p clip is 500 seconds of video, so the minimum purchase is also the only way to generate one clip. [1]
- limits note: there is no free lane on the pricing page: the first credit costs USD 30 for 10,000, and 10,000 credits at 100 a five-second 720p clip is 500 seconds of video, so the minimum purchase is also the only way to generate one clip.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing to chain: a paid minimum of USD 30 is the entry price, and the Draft tier at 20 credits a five-second clip is the only rate that makes 10,000 credits go far. What breaks: the absence of a free lane, which is the finding.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. Classified as paid-only and not dead: the product sells and the plans are published. The page was read through its markdown source (lumalabs.ai/pricing.md), which is the vendor's own rendering. Luma has historically offered a free monthly generation allowance in-app; nothing on this page states one on 2026-10-22, and an in-app free tier that is unpublished would not be a documented finding. A reader who has an old account may still hold the older allowance.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: none-published
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page lists 'Individual plans' beginning with 'Plus $30/month ... 10,000 credits'; no free plan appears in the document, quoted from the page's markdown source
  - [1] 2026-10-22: the cost table prices 'Ray3.2 ... 540p ... 50 credits/5 sec', '720p ... 100 credits/5 sec', '1080p ... 400 credits/5 sec', 'Draft ... 20 credits/5 sec', quoted
- sources:
  - [1] https://lumalabs.ai/pricing
