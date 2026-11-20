# The Grid AI

> thegrid.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thegrid/ | JSON https://fshy.ajam.dev/api/v1/entity/thegrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## The Grid AI

- `inference/the-grid-ai` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://thegrid.ai/pricing
- free tier: A central limit order book with no rate card: requests fill at the market clearing price per million tokens, with no subscription, seat fee or minimum commitment, and no free allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a Trading USD balance funds buys on the order book; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): market-clearing per-token price, no subscription or minimum [1]
- endpoint: https://api.thegrid.ai/v1
- composes with: the market price and the funded balance are the scarce link
- reliability: prices move with the market, so the clearing price is not fixed
- evidence:
  - [1] 2026-11-18: The Grid has no subscription and charges at the market clearing price with no free tier | capture: sha256:e84e14d41eca2a675c1b9d93596fde9484d23226688d9b221bd234c502b29c71 | quote: There is no subscription, no seat fee, and no minimum commitment.
- sources:
  - [1] https://thegrid.ai/pricing
