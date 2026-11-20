# Browser Use

> browser-use.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browser-use/ | JSON https://fshy.ajam.dev/api/v1/entity/browser-use.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Browser Use

- `compute/browser-use` | trial-only | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://browser-use.com/pricing
- price parsed USD 14.4/mo
- free tier: USD 15 of one-time credit; browsers cost USD 0.02 an hour; a USD 100 one-time top-up runs 50 in parallel | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: credits never expire, stated in the page description
- per-object cap: not applicable
- retention: credits never expire; session state retention is not stated on the page read
- egress: consumer-connection proxy is USD 5 per GB, priced separately from the browser hour | metered: yes | price per TB: USD 5,120 per TB | source: [1]
- identity: email | detail: a signup; the pricing page states no card for the first credit
- interface: rest, cli
- limits:
  - per-ip-shaping: consumer-connection proxy USD 5 per GB, billed separately from browser time [1]
  - request-rate: a USD 100 top-up runs 50 browsers in parallel [1]
- limits note: a model-driven agent adds 20% on the model rate plus browser time and traffic
- binding note: the one-time credit is the clock; the 15-minute session cap is the second constraint
- interface detail: cloud browser over CDP plus a web-agent API
- tooling: Playwright and Puppeteer over CDP; cloud browser API
- composes with: USD 0.02 a browser hour is the cheapest published rate in this class, and the proxy is 100 times the browser cost per hour of video
- reliability: no reliability event recorded
- notes: The browser hour is almost free and the traffic is not. A crawl that pulls 1 GB through the consumer-connection proxy costs 250 browser hours at this rate, so the proxy is the bill.
- evidence note: a one-time credit is a trial: it does not renew, and the browser stops when it is spent
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: not stated on the pricing page
  - keep_rate.value: 0.0
  - keep_rate.basis: billing is per browser hour
  - keep_rate.source: https://browser-use.com/pricing
  - persistent_storage.durability: not stated
  - persistent_storage.max_retention: not stated
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP
  - free_tier_kind: one-time-credit
  - m10h_usd: 6.0
  - m24h_usd: 14.4
  - price_arithmetic: USD 0.02 x 300 h = 6.00 before proxy traffic
  - price_note: 300 browser hours at USD 0.02 an hour is 6.00; 730 hours is 14.60. Proxy traffic is separate at USD 5 per GB and dominates any real crawl.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: browsers cost USD 0.02 an hour; a USD 100 one-time top-up runs 50 in parallel; credits never expire
  - [1] 2026-10-22: consumer-connection proxy is USD 5 per GB, separate from browser time
- sources:
  - [1] https://browser-use.com/pricing
