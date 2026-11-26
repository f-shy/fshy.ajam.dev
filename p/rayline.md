# Rayline

> rayline.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rayline/ | JSON https://fshy.ajam.dev/api/v1/entity/rayline.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rayline

- `inference/rayline` | paid-only | evidence documented | binding volume-quota | category inference gateway (model router)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://rayline.ai/pricing
- free tier: Pay the published rates whichever model ARC selects. Routing and generation are included. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup at rayline.ai; no free inference allowance stated
- interface: rest
- limits:
  - volume-quota (binding): ARC Swift starts at USD 0.10 input and USD 0.50 output per 1M tokens; Contributor models are cheaper in exchange for training data use [1]
- endpoint: https://api.rayline.ai/v1
- composes with: No free text inference allowance is published in the fetched pricing page.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Rayline publishes fixed and passthrough token rates with a Contributor discount for data use, and no free tier | capture: sha256:587f61ae2c9eb495bf1cd78a87ad9fc801a2ba83f41e2713716d83b7d356733e | quote: Pay the published rates whichever model ARC selects. Routing and generation are included.
- sources:
  - [1] https://rayline.ai/pricing
