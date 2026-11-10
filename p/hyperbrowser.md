# Hyperbrowser

> hyperbrowser.ai | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyperbrowser/ | JSON https://fshy.ajam.dev/api/v1/entity/hyperbrowser.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hyperbrowser (Compute)

- `compute/hyperbrowser` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hyperbrowser.ai/pricing
- price parsed USD 30/mo
- free tier: 5,000 credits on a free account, enough for 50 browser hours or 5,000 fetched pages at base rates | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: 1,000 credits is USD 1 of usage
- per-object cap: not applicable
- retention: not stated on the page read
- egress: proxies are bundled into the credit; the page states no separate per-GB line | metered: no | free allowance: within the 5,000 credits | source: [1]
- identity: email | detail: a free account; no card stated
- interface: rest, cli
- limits:
  - per-object-cap: 5,000 credits a month on the free account [1]
  - request-rate (binding): 25 concurrent sessions on Startup at USD 30 a month [1]
- limits note: one credit is USD 0.001, so 5,000 credits is USD 5 of usage
- binding note: the 5,000-credit monthly pool is shared across browsers, sandboxes, web data and agents, so an agent run spends the browser budget
- interface detail: REST API and SDKs; browser sessions, scraping and agents
- tooling: SDK and REST; Playwright over CDP
- composes with: an allowance that covers browsers, sandboxes, scraping and agents from one credit pool
- reliability: no reliability event recorded
- notes: 50 browser hours a month at base rates is the largest free browser allowance in this class, and it is a credit pool rather than a browser-hour cap.
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: not stated
  - keep_rate.value: 0.0
  - keep_rate.basis: credits are spent per use
  - keep_rate.source: https://www.hyperbrowser.ai/pricing
  - persistent_storage.durability: not stated
  - persistent_storage.max_retention: not stated
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP
  - free_tier_kind: allowance
  - m10h_usd: 30.0
  - m24h_usd: 30.0
  - price_arithmetic: 5,000 credits = USD 5; 50 browser hours at base rate is 100 credits an hour
  - price_note: Startup at USD 30 a month includes USD 30 of usage and 25 concurrent sessions; 300 browser hours at base rate is inside the credit.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: free account: 5,000 credits, enough for 50 browser hours or 5,000 fetched pages; 1 credit is USD 0.001
  - [1] 2026-10-22: Startup is USD 30 a month with USD 30 of usage and 25 concurrent sessions
- sources:
  - [1] https://www.hyperbrowser.ai/pricing

## Hyperbrowser (Crawling)

- `crawler-scraper/hyperbrowser` | trial-only | evidence documented | binding retention-clamped | category headless browser
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hyperbrowser.ai/pricing
- free tier: 5,000 credits on signup, 1 concurrent session, 7 days of data retention | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a browser hour or a page | source: [1]
- retention: the 5,000 credits are one-time; job results are kept 7 days | source: [1]
- egress: not applicable: Markdown or JSON answers | metered: no | source: [1]
- identity: email | detail: signup is an account; no card stated for Free
- interface: rest
- limits:
  - request-rate: 1 concurrent session on Free, or 25 on Startup at USD 30 a month for 30,000 credits [1]
  - request-rate: browser usage 100 credits an hour, so 5,000 credits is 50 browser hours [1]
  - retention-clamped (binding): Job results are retained for 7 days on Free and 14 days for Browser Run. Subsequent requests return HTTP 410.
- interface detail: REST sessions, web crawl and scrape; 1 credit is USD 0.001
- tooling: not established
- composes with: Headless browser crawl provider with DOM rendering where per-page billing reflects browser execution time rather than simple request counts.
- reliability: no reliability event recorded
- notes: One-time, so it is a trial. It renders every page whatever is asked, which makes it the wrong leg for a cheap plain fetch and the right one for a page that cannot be read any other way.
- evidence:
  - [1] 2026-10-22: Free USD 0 to start with 5,000 credits, all four products, 1 concurrent session, 7 days of data retention; 1,000 credits is USD 1; browser usage 100 credits an hour
- sources:
  - [1] https://www.hyperbrowser.ai/pricing
