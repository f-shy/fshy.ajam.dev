# RuAPI

> ruapi.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ruapi/ | JSON https://fshy.ajam.dev/api/v1/entity/ruapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RuAPI

- `inference/ruapi` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://www.ruapi.ai/pricing?lng=en
- free tier: Pay per token with settlement in USDT or USDC; new users save about 8% on the first top-up and VIP status keeps the discount after USD 100 of total top-ups; no standing free allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: payment is in USDT/USDC stablecoin; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): per-token billing, USDT/USDC settlement, first-top-up and VIP discounts [1]
- endpoint: https://www.ruapi.ai/v1
- composes with: the stablecoin-funded balance is the scarce link
- reliability: no standing free tier is published
- evidence:
  - [1] 2026-11-18: RuAPI is a per-token paid gateway settled in stablecoin with no free allowance | capture: sha256:ff83a52c1e8455e0ed5a421a899f2f968ab0f5b230e27e54a68fc36a2ca23417 | quote: Settlement currency USDT / USDC.
- sources:
  - [1] https://www.ruapi.ai/pricing?lng=en
