# Upstage

> upstage.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upstage/ | JSON https://fshy.ajam.dev/api/v1/entity/upstage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Upstage

- `compute/upstage` | paid-only | evidence documented | binding volume-quota | category inference API
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.upstage.ai/pricing/api
- free tier: no free tier and no signup credit. The price card reads Solar Pro 4 at 0.30 per million input tokens and 1.20 per million output tokens, with 0.06 for cached input. The same page carries a promotional price ladder for that model that opens with a `free` phase from 2026-08-05 to 2026-08-11, then 0.03, then 0.09, then 0.15 per million input tokens. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the Solar Pro 4 price card (0.30 input, 0.06 cached, 1.20 output per 1M tokens) and the promotional schedule whose free rung closed on 2026-08-11. Whether signup needs a card, a phone number or an ID document, and whether any hold is taken, is not stated.
- interface: unknown
- limits:
  - volume-quota (binding): every call is metered per token with no allowance: the balance is the only limit, and the one free window on the page closed on 2026-08-11. [1]
- limits note: every call is metered per token with no allowance: the balance is the only limit, and the one free window on the page closed on 2026-08-11.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the model that ran free for a week in August now costs 0.30 a million input tokens, five times DeepInfra's listed input rate for DeepSeek-V4-Flash-0731 (0.30 / 0.06 = 5); the vendor is a reason to look elsewhere, not a resource to chain.
- reliability: no reliability event recorded
- notes: Two numbers on the same page disagree: the Solar Pro 4 card says 0.30 in and 1.20 out per million tokens, while the schedule's final rung says input=0.15 and output=0.60. Both are quoted above and the card figure is recorded, because it is the one a buyer sees first. The `free` rung is a launch-week promotion that closed on 2026-08-11, so a reader who saw the free week reported in August is looking at a closed window. Currency: the Solar Pro 4 card prints bare numbers, but the same page prints `$0.01` and `$0.03` per page for the document models and sells prepaid credit packs from `$100+`, so the unit is USD and is taken from the page rather than asserted.
- extras:
  - facets.class: paid-inference
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the Solar Pro 4 card: 'Input 0.30 1M tokens', 'Input(Cached) 0.06 1M tokens', 'Output 1.20 1M tokens'; and the price schedule '2026-08-05T22:00:00Z|2026-08-11T00:00:00Z|free 2026-08-11T00:00:00Z|2026-09-11T00:00:00Z|input=0.03|cached=0.006|output=0.12', quoted
- sources:
  - [1] https://www.upstage.ai/pricing/api
