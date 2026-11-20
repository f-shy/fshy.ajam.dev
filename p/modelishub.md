# Modelis

> modelishub.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modelishub/ | JSON https://fshy.ajam.dev/api/v1/entity/modelishub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modelis

- `inference/modelis` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://modelishub.com/pricing
- free tier: A RapidAPI free tier that needs no card, plus USD 1 of signup credit; the paid starter is listed at USD 9.99 with 100 free requests a month on the free listing. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a RapidAPI account and a subscription to the listing; the page states no card for the free tier
- interface: rest
- limits:
  - volume-quota (binding): 100 free requests a month on the free listing [1]
- endpoint: https://modelishub.com/v1
- tooling: the RapidAPI key in an X-RapidAPI-Key header or the vendor console
- composes with: the monthly request count is the scarce link, and it is small enough that a single agent sweep consumes it
- reliability: the free allowance is mediated by RapidAPI, so both the quota and the routing depend on that account
- evidence:
  - [1] 2026-11-18: the free tier is on RapidAPI with no card to start, 100 free requests a month, plus USD 1 signup credit | capture: sha256:bd0139e336243069d5cc0007743628229b7cc678e2699e05be316057e75a6d5c | quote: Subscribe on RapidAPI (free tier, no card to start), copy your key, and make your first call — one `base_url`, OpenAI-compatible, zero migration.
- sources:
  - [1] https://modelishub.com/pricing
