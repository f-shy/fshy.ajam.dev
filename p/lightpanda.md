# Lightpanda

> lightpanda.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lightpanda/ | JSON https://fshy.ajam.dev/api/v1/entity/lightpanda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lightpanda

- `compute/lightpanda` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://lightpanda.io/pricing
- price parsed USD 53.4/mo
- free tier: Explorer: USD 0 for ever, 10 browser hours a month, 5 concurrent sessions, bring your own proxy | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: a purpose-built headless engine rather than a Chromium instance
- per-object cap: not applicable
- retention: no session storage is described; the product is a stateless fetch-and-render engine | days: 0
- egress: bring your own proxy; no proxy is included on the free plan | metered: no | source: [1]
- identity: email | detail: a free signup; no card stated on the pricing page
- interface: rest, cli
- limits:
  - request-rate (binding): 5 concurrent sessions on the free plan; 30 on Builder [1]
  - per-object-cap: 10 browser hours a month on the free plan; 300 on Builder [1]
- limits note: Builder is USD 19 a month for 300 hours, then USD 0.08 an hour
- binding note: 10 browser hours a month is the allowance, and the engine's compatibility is the second wall
- interface detail: a CDP-compatible endpoint for a headless engine
- tooling: Playwright and Puppeteer over CDP; the Lightpanda binary can also be self-hosted
- composes with: 10 hours a month of a browser engine that renders without a full Chromium, so the time buys more pages
- reliability: no reliability event recorded
- notes: The only free browser allowance here that recurs monthly with no card, and the engine is lighter than Chromium. The catch is compatibility: it is not a full browser and a site that needs one will not render.
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: not stated
  - keep_rate.value: 0.0
  - keep_rate.basis: per browser hour
  - keep_rate.source: https://lightpanda.io/pricing
  - persistent_storage.durability: none
  - persistent_storage.survives_stop: no
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP
  - free_tier_kind: allowance
  - m10h_usd: 19.0
  - m24h_usd: 53.4
  - price_arithmetic: 10 hours a month free; 300 h costs USD 19, which is 0.063 an hour
  - price_note: Builder at USD 19 a month includes 300 browser hours, then USD 0.08 an hour. 730 hours is 19 + 430(0.08) = 53.40.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: Explorer is USD 0 for ever with 10 browser hours a month and 5 concurrent sessions
  - [1] 2026-10-22: Builder is USD 19 a month with 300 hours included, then USD 0.08 an hour
- sources:
  - [1] https://lightpanda.io/pricing
