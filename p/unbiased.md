# Pareto by Unbiased

> unbiased.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unbiased/ | JSON https://fshy.ajam.dev/api/v1/entity/unbiased.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pareto by Unbiased

- `inference/unbiased` | paid-only | evidence documented | binding write-gated | category inference gateway (blended model)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://unbiased.ai/pricing/
- free tier: New accounts are reviewed and approved by hand before your API access turns on; payment does not mean instant access. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a platform.unbiased.ai account is reviewed by hand before the API key is issued
- interface: rest
- limits:
  - write-gated (binding): pay-as-you-go at USD 0.80 input and USD 3.20 output per 1M tokens; Personal plan includes 50M tokens a week [1]
- endpoint: https://api.unbiased.ai/v1
- composes with: No free text inference allowance is published; the gate is a person, not a card.
- reliability: 429 over the rate limit; 401 for a missing or invalid key
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Unbiased requires manual approval of new accounts and sells pay-as-you-go credits with no free tier | capture: sha256:8b610f8700272290a36130ad14d61da4f9094fd4e3fe93c27506a390d5b9a176 | quote: New accounts are reviewed and approved by hand before your API access turns on; payment does not mean instant access.
- sources:
  - [1] https://unbiased.ai/pricing/
