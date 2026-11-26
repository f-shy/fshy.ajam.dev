# Zro

> moonmath.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/moonmath/ | JSON https://fshy.ajam.dev/api/v1/entity/moonmath.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zro

- `inference/zro` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://zro.moonmath.ai/pricing
- free tier: A free plan for the Flash models, with usage packs from USD 5 and a USD 40 monthly usage budget on the paid side. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is required; the page states no card for the free plan
- interface: rest
- limits:
  - volume-quota (binding): the free plan covers the Flash models only, with no stated request count [1]
- endpoint: https://zro.moonmath.ai/v1
- composes with: the model subset is the scarce link, because the free plan does not reach the rest of the catalogue
- reliability: a free plan tied to a named model family, so a route change by the vendor removes the allowance
- evidence:
  - [1] 2026-11-18: a free plan exists for the Flash models, and paid usage packs start at USD 5 | capture: sha256:b7c8e7b90224813398fac06097d756f29d00b7735ca275a313742d7e5d640dd9 | quote: Free plan for Flash models.
- sources:
  - [1] https://zro.moonmath.ai/pricing
