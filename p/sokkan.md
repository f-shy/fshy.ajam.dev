# SOKKAN Router

> sokkan.ch | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sokkan/ | JSON https://fshy.ajam.dev/api/v1/entity/sokkan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SOKKAN Router

- `inference/sokkan` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://router.sokkan.ch/models
- free tier: Prices in USD per million tokens paid from a prepaid balance; some models are sold only as a weekly prepaid throughput commitment, and no free allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account and a prepaid balance are required; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): prepaid balance, or a weekly committed-throughput plan for some models [1]
- endpoint: https://router.sokkan.ch/v1
- composes with: the prepaid balance is the scarce link
- reliability: best-effort models are served only while their capacity is running, with no guarantee; models listed as coming soon return HTTP 503 until live
- evidence:
  - [1] 2026-11-18: Sokkan charges from a prepaid USD balance with no free inference allowance | capture: sha256:f52bc6f57dfae17b6b67e4ec24993557394874385661933ee58de708a9804c95 | quote: Prices in USD per million tokens. You pay for the tokens you use, from a prepaid balance.
- sources:
  - [1] https://router.sokkan.ch/models
