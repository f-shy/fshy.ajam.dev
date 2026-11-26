# TeamoRouter

> teamorouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/teamorouter/ | JSON https://fshy.ajam.dev/api/v1/entity/teamorouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TeamoRouter

- `inference/teamorouter` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://teamorouter.com/docs/api-integration
- free tier: All listed models are billed; the -free variants are described as a lower-priced tier that is still billed, not a zero-price allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: top-up by card or crypto from the console; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): all models including -free variants are billed from a prepaid balance [1]
- endpoint: https://api.teamorouter.com/v1
- composes with: the prepaid balance is the scarce link
- reliability: paid models are rate limited by requests per minute per account
- evidence:
  - [1] 2026-11-18: the -free model variants are lower-priced but still billed, so there is no free allowance | capture: sha256:67349b39d3cafd0eb1e0588540546e0f0fdb49c7bdfdef7ee1c6897d015e79cb | quote: lower-priced tier, still billed
- sources:
  - [1] https://teamorouter.com/docs/api-integration
