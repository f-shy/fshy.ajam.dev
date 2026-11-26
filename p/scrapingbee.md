# Scraping Bee

> scrapingbee.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapingbee/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapingbee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scraping Bee

- `compute/scrapingbee` | trial-only | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:22.988Z (live) | stale on 2026-12-05
- url https://www.scrapingbee.com/pricing/
- free tier: 1,000 free API credits at signup with no card; paid tiers run from $19 to $5,799 a month | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.scrapingbee.com/pricing/ states API credits per plan and no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: 'No credit card required', quoted from scrapingbee.com/pricing read 2026-10-22
- interface: rest, cli
- limits:
  - request-rate (binding): 1,000 free API credits at signup, one time; paid tiers from $19 a month [1]
  - request-rate (binding): concurrent requests are a plan row and scale with the tier [1]
- interface detail: HTTP API authenticated with an API key (bearer header); a scrapingbee CLI installed with pip; client libraries for several languages shown in the documentation
- tooling: scrapingbee-cli (pip install scrapingbee-cli) and ScrapingBeeClient libraries
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the 1,000-credit free trial and the paid ladder. The record's paid-only verdict is contradicted by a free credit grant, so it moves to trial-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a request against a credit balance; there is no machine to reap
  - free_tier_kind: one-time-credit
  - reclassified_from: dead
  - net.out: yes
  - net.in: no
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Try ScrapingBee with 1,000 free API credits.' and 'No credit card required.' with paid tiers from 'Hobby $19/mo' to 'Enterprise 120 $5,799/mo', quoted
  - [2] 2026-11-03: the documentation shows a CLI install; the same page authenticates the HTTP API with a bearer API key | capture: sha256:27d152963eafdeb5bbc0e7ee4449546ced5ff93db3350a3bc8ab2ffd65493dcb | quote: # Install the ScrapingBee CLI:
  - [1] 2026-11-03: pricing is in API credits; no egress allowance or overage price is stated | capture: sha256:51e24498a8c650c8e698008b4cb0d7eb321e418260cb3b8d6135d024d8dfd6f3 | quote: Try ScrapingBee with 1,000 free API credits.
- sources:
  - [1] https://www.scrapingbee.com/pricing/
  - [2] https://www.scrapingbee.com/documentation/
