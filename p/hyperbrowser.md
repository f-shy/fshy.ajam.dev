# Hyperbrowser

> hyperbrowser.ai | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyperbrowser/ | JSON https://fshy.ajam.dev/api/v1/entity/hyperbrowser.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hyperbrowser (Compute)

- `compute/hyperbrowser` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card unknown, phone no, ID no, institution no | verified 2026-11-25T11:17:28.100Z (live) | stale on 2026-12-26
- url https://www.hyperbrowser.ai/pricing
- price parsed USD 30/mo
- free tier: 5,000 credits on a free account: 'Enough for 50 browser hours or 5,000 fetched pages at base rates.' The Free row states '$0 to start · 5,000 credits included' and 'All four products · 1 concurrent session · 7 days of data retention'. '1,000 credits = $1 in usage'. | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: 1,000 credits is USD 1 of usage
- per-object cap: not applicable
- retention: 7 days of data retention on the Free plan; 30 days on Startup and Scale; 180+ days on Enterprise | days: 7
- egress: proxy data is billed separately at 10,000 credits / GB ($10 / GB) on top of browser time, so the 5,000-credit allowance covers only 0.5 GB of proxy data | metered: yes | free allowance: within the 5,000 credits | price per TB: USD 10,000 per TB of proxy data (10,000 credits / GB at 1,000 credits = USD 1) | source: [1]
- identity: email | detail: signup offers Google or email; a card is not asked for at signup, and paid plans accept major credit cards
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
  - [1] 2026-11-25: the free account's 5,000 credits cover 50 browser hours or 5,000 fetched pages at base rates | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: Enough for 50 browser hours or 5,000 fetched pages at base rates.
  - [1] 2026-11-25: the Free plan starts at $0 with 5,000 credits, one concurrent session and seven days of data retention | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: $0 to start · 5,000 credits included All four products · 1 concurrent session · 7 days of data retention
  - [1] 2026-11-25: the credit-to-usage conversion rate is 1,000 credits per dollar | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: 1,000 credits = $1 in usage
  - [1] 2026-11-24: the free account includes 5,000 credits, enough for 50 browser hours or 5,000 fetched pages at base rates | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: Enough for 50 browser hours or 5,000 fetched pages at base rates.
  - [1] 2026-11-24: the free plan has one concurrent session and seven days of data retention | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: All four products · 1 concurrent session · 7 days of data retention
  - [1] 2026-11-24: proxy data has a separate metered rate of 10,000 credits per GB | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: | Proxy data | 10,000 credits / GB | $10 / GB |
  - [1] 2026-11-24: browser sessions bill proxy data used in addition to browser time | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: Browser time, plus any proxy data used.
  - [2] 2026-11-24: the documented rate is 10,000 credits or USD 10 per GB of proxy data | capture: sha256:458daa3f99ac150760e8bf53bd4219da817f8326b341dfbf0ddf8b5f4fa26e73 | quote: | Proxy Data Usage | 10,000 credits / GB | \$10 / GB |
  - [3] 2026-11-24: the signup page offers Google or email registration with no card field | capture: sha256:b6bbdfd536681c9a45409895fc781e20359d9d1dac8d740bb6b37b7261979375 | quote: Google or with email
  - [1] 2026-11-24: the Startup plan includes 25 concurrent sessions | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: - 25 concurrent sessions
- sources:
  - [1] https://www.hyperbrowser.ai/pricing
  - [2] https://www.hyperbrowser.ai/docs/pricing
  - [3] https://app.hyperbrowser.ai/signup

## Hyperbrowser (Crawling)

- `crawler-scraper/hyperbrowser` | trial-only | evidence documented | binding retention-clamped | category headless browser
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:22.325Z (live) | stale on 2026-12-20
- url https://www.hyperbrowser.ai/pricing
- free tier: 5,000 credits on signup, enough for 50 browser hours or 5,000 fetched pages at base rates; 1 concurrent session; 7 days of data retention | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a browser hour or a page | source: [1]
- retention: the 5,000 credits are one-time; job results are kept 7 days | source: [1]
- egress: not applicable: Markdown or JSON answers | metered: no | source: [1]
- identity: email | detail: signup is an account; no card stated for Free
- interface: rest
- limits:
  - request-rate: 1 concurrent session on Free, or 25 on Startup at USD 30 a month for 30,000 credits [1]
  - request-rate: browser usage 100 credits per hour ($0.10/hour) at 1 credit = $0.001; 50 browser hours is the vendor-stated equivalent of the 5,000-credit grant [1]
  - retention-clamped (binding): Job results are retained for 7 days on Free and 14 days for Browser Run. Subsequent requests return HTTP 410.
- interface detail: REST sessions, web crawl and scrape; 1 credit is USD 0.001
- tooling: not established
- composes with: Headless browser crawl provider with DOM rendering where per-page billing reflects browser execution time rather than simple request counts.
- reliability: no reliability event recorded
- notes: One-time, so it is a trial. It renders every page whatever is asked, which makes it the wrong leg for a cheap plain fetch and the right one for a page that cannot be read any other way.
- evidence:
  - [1] 2026-10-22: Free USD 0 to start with 5,000 credits, all four products, 1 concurrent session, 7 days of data retention; 1,000 credits is USD 1; browser usage 100 credits an hour
  - [1] 2026-11-19: Free plan gives 5,000 credits, enough for 50 browser hours or 5,000 fetched pages, with 1 concurrent session and 7 days of data retention | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: Enough for 50 browser hours or 5,000 fetched pages at base rates. $0 to start · 5,000 credits included All four products · 1 concurrent session · 7 days of data retention
  - [1] 2026-11-19: vendor states 5,000 credits equals 50 browser hours at base rates | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: Enough for 50 browser hours or 5,000 fetched pages at base rates.
  - [1] 2026-11-19: Free plan is $0 to start with a 5,000-credit grant, still a one-time trial grant | capture: sha256:1bfb973c1b1c91986e5cfc67107976a643399cec47118dc6c38b15c1a4d33b1b | quote: $0 to start · 5,000 credits included All four products · 1 concurrent session · 7 days of data retention
  - [2] 2026-11-19: signup requires a Google account or a name, email address and password; no card or phone appears on the form | capture: sha256:85c91210e571c1787ebdc1b45e1e5a918d9108fe28195870bd954306ebd61ce3 | quote: Sign Up for Hyperbrowser ... >Google< ... or with email ... placeholder="Name" ... placeholder="Email" ... placeholder="Password"
  - probe:www.hyperbrowser.ai 2026-11-19: first-party pricing endpoint answered HTTP 200 on a live keyless GET with no challenge detected | capture: sha256:37a9b9125e0597a8223d6ae2afb3722a06ccbb3bc47e79d92894b01c89c7efec | quote: "status": 200
  - [3] 2026-11-19: the scrape API is gated by an x-api-key header, so a live scrape needs an account-issued key | capture: sha256:769fe60149e1ffde3b7e9a2fcebac9a539df93ee0da4f608255a8a53e45400ad | quote: securitySchemes: ApiKeyAuth: type: apiKey in: header name: x-api-key
- sources:
  - [1] https://www.hyperbrowser.ai/pricing
  - [2] https://app.hyperbrowser.ai/signup
  - [3] https://www.hyperbrowser.ai/docs/api-reference/create-new-scrape-job
