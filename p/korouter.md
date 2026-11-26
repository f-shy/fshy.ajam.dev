# KoRouter

> korouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/korouter/ | JSON https://fshy.ajam.dev/api/v1/entity/korouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KoRouter

- `inference/korouter` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://korouter.ai/credits
- free tier: No free allowance is stated on the pricing page read on 2026-11-18: the gateway undercuts list prices, for example USD 2.28 per 1M input tokens against an official USD 4.00. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a funded account is required before a key spends
- interface: rest
- limits:
  - volume-quota (binding): per-token billing below the official rate, with no stated allowance [1]
- endpoint: https://korouter.ai/v1
- composes with: the discount is the scarce link, and a price below official depends on the vendor's upstream access
- reliability: a price that undercuts the official rate carries resale risk, because the upstream account behind it is not named
- evidence:
  - [1] 2026-11-18: the gateway charges USD 2.28 per 1M input tokens against an official USD 4.00, with no free allowance stated | capture: sha256:d25994366d45596682ed91c02da45c97fb1fe2e67877f0a7e97eb543de45adb3 | quote: Input KoRouter price: $2.28 ~~Official price: $4.00~~ Output KoRouter price: $11.40 ~~Official price: $20.00~~
- sources:
  - [1] https://korouter.ai/credits
