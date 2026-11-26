# TheRouter

> therouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/therouter/ | JSON https://fshy.ajam.dev/api/v1/entity/therouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TheRouter

- `inference/therouter` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://therouter.ai/docs/quickstart/
- free tier: An account and API key are required, and the model catalog lists a current price for each model; no standing free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account and an API key in the dashboard; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): per-model prices from the model catalog; no free tier stated [1]
- endpoint: https://api.therouter.ai/v1
- composes with: the funded balance is the scarce link
- reliability: the legacy China accelerated endpoint is retired
- evidence:
  - [1] 2026-11-18: TheRouter requires an account and charges per the catalog with no published free tier | capture: sha256:b444c7f6c4801763a35ddf56a4c5cc6e1d66cf20429dea7187f6c2e7cf5003ea | quote: Check the [model catalog](https://therouter.ai/models/) for an available model and its current price before sending a request.
- sources:
  - [1] https://therouter.ai/docs/quickstart/
