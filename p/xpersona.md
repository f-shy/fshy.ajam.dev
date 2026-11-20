# Xpersona

> xpersona.co | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xpersona/ | JSON https://fshy.ajam.dev/api/v1/entity/xpersona.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xpersona

- `inference/xpersona` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://www.xpersona.co/inference/pricing
- free tier: Every plan includes the full model catalog. Choose monthly capacity from $20—or try the API with $2 prepaid credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: Stripe checkout for either a monthly plan or prepaid credits; no free signup credit stated
- interface: rest
- limits:
  - volume-quota (binding): builder plan USD 20 a month; prepaid credits from USD 2; credits last 12 months [1]
- endpoint: https://www.xpersona.co/v1
- composes with: No free text inference allowance is published in the fetched pricing page.
- reliability: requests pause at the plan limit instead of creating overage charges
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Xpersona sells monthly plans from USD 20 and prepaid credits from USD 2 with no free inference tier | capture: sha256:627c31e9fb10ddb83c6dca269b11e6ad0a360cadeab4777efa27b49637431fd5 | quote: Every plan includes the full model catalog. Choose monthly capacity from $20—or try the API with $2 prepaid credits.
- sources:
  - [1] https://www.xpersona.co/inference/pricing
