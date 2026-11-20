# Browserbase

> browserbase.com | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browserbase/ | JSON https://fshy.ajam.dev/api/v1/entity/browserbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Browserbase (Compute)

- `compute/browserbase` | trial-only | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.browserbase.com/pricing
- price parsed USD 95.6/mo
- free tier: Free: 3 concurrent browsers, 1 browser hour, 3 agent runs, 1,000 search calls, 1,000 fetch calls, 15 minutes per session | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the free hour is a one-off monthly allowance
- per-object cap: not applicable
- retention: session recordings and data retention are stated per plan; the free plan's figure was not on the page read | days: 0
- egress: proxies are priced separately; the free plan's proxy allowance was not on the page read | metered: yes | source: [1]
- identity: email | detail: a free signup; no card stated on the pricing page
- interface: rest, cli
- limits:
  - retention-clamped (binding): 15 minutes per session on Free; the Developer plan does not state a longer cap on the page read [1]
  - request-rate: 3 concurrent browsers on Free [1]
  - per-object-cap: 1 browser hour and 1,000 fetch calls a month on Free [1]
- limits note: the Developer plan is USD 20 a month for 100 browser hours, then USD 0.12 an hour
- binding note: the 15-minute session cap binds first: 1 free browser hour in 15-minute sessions is four sessions, and every reconnect pays setup
- interface detail: REST API and SDKs; a browser session over CDP
- tooling: Playwright and Puppeteer over CDP; SDKs for Python and Node
- composes with: one browser hour a month is a test allowance, not a crawl
- reliability: no reliability event recorded
- notes: One browser hour a month, in 15-minute sessions, is four sessions. The paid rate of USD 0.12 an hour is the cheapest published browser hour in this class after Lightpanda.
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 60
  - granularity.rounding_s: 60
  - session_cap.wall_clock_min: 15
  - session_cap.restart_required: no
  - session_cap.note: 15 min per session on Free
  - keep_rate.value: 0.0
  - keep_rate.basis: billing stops when the session ends
  - keep_rate.source: https://www.browserbase.com/pricing
  - persistent_storage.durability: contexts persist on paid plans
  - persistent_storage.max_retention: stated per plan
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP over the API
  - free_tier_kind: allowance
  - m10h_usd: 44.0
  - m24h_usd: 95.6
  - price_arithmetic: USD 0.12 a browser hour x 300 h = 36, but the 100 included hours cover the first 100, so 300 h = 24
  - price_note: 300 browser hours on Developer: USD 20 plan includes 100 hours, then USD 0.12 an hour, so 20 + 200(0.12) = 44.00. 730 hours: 20 + 630(0.12) = 95.60. The browser hour is not a vCPU shape, so this row is not comparable with a sandbox row.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: Free plan: 3 concurrent browsers, 1 browser hour, 3 agent runs, 1,000 search and 1,000 fetch calls, 15 minutes a session
  - [1] 2026-10-22: Developer plan USD 20 a month with 25 concurrent and 100 browser hours, then USD 0.12 a browser hour
- sources:
  - [1] https://www.browserbase.com/pricing

## Browserbase (Crawling)

- `crawler-scraper/browserbase` | trial-only | evidence documented | binding request-rate | category headless browser
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T21:12:22.105Z (live) | stale on 2026-12-20
- url https://www.browserbase.com/pricing
- free tier: Free plan USD 0/mo: 1 browser hour, 3 concurrent browsers, 15 minutes per session, 3 Agent runs, 1,000 Search calls, 1,000 Fetch calls and USD 5 in model tokens; a recurring monthly allocation | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is browser time | source: [1]
- retention: 7 days data retention on the Free plan | source: [1]
- egress: not applicable: Markdown or HTML answers | metered: no | source: [1]
- identity: any-phone | detail: an account asks for an email address, a phone number with a +1 country code and a password on the email path; Google sign-in is also offered; the vendor docs say "Start free, no credit card needed"
- interface: rest
- limits:
  - request-rate (binding): 3 concurrent browsers and 1 browser hour on Free; Developer USD 20 a month for 100 hours and 25 concurrent [1]
  - request-rate (binding): browser hours past the included ones bill at USD 0.12 an hour on Developer [1]
- interface detail: REST sessions and a Search and Fetch API
- tooling: not established
- composes with: A session model requiring stateful browser lifecycles, suitable for asynchronous batch crawl jobs rather than short-lived stateless edge functions.
- reliability: no reliability event recorded
- notes: One browser hour is one hour. The 1,000 Search and 1,000 Fetch calls are the more useful part of the plan and are easier to spend.
- evidence:
  - [1] 2026-10-22: Free plan: 3 concurrent browsers, 1 browser hour, 1,000 Search calls, 1,000 Fetch calls, USD 5 in model tokens; Developer USD 20 a month with 100 browser hours and 25 concurrent
  - [2] 2026-11-19: the email sign-up form asks for a phone number with a US +1 country code alongside email and password | capture: sha256:b4339f5043b0035f006719e394d4acb34b50141112db7dc1c7072560e4bf2231 | quote: E-mail address* Phone number* 🇺🇸+1 Password*
  - [2] 2026-11-19: the sign-up offers Google or an email-plus-phone-plus-password form; no card field is present | capture: sha256:b4339f5043b0035f006719e394d4acb34b50141112db7dc1c7072560e4bf2231 | quote: Continue with Google or E-mail address* Phone number* 🇺🇸+1 Password* Continue Already have an account?
  - [1] 2026-11-19: the vendor's own pricing page lists the Free plan at USD 0/mo with those included allowances | capture: sha256:7db04564d51fcfc0eeb0a6114b7753415b84f819b4cd93c9e62ce7f735d53ad7 | quote: ## Free Plan $0/mo [Start for free](/sign-up) Get started with Browserbase. Explore and prototype ideas. Infrastructure - 3 concurrent browsers - 1 browser hour - 3 Agent runs included - 1,000 Search calls - 1,000 Fetch calls - 15 minutes /session
  - [1] 2026-11-19: the pricing page compare table states 7 days of data retention on the Free plan | capture: sha256:7db04564d51fcfc0eeb0a6114b7753415b84f819b4cd93c9e62ce7f735d53ad7 | quote: | Data Retention | 7 days | 30 days | 30 days | 30+ days |
  - [1] 2026-11-19: the Free plan is a recurring USD 0/mo plan with 1 browser hour, 3 concurrent browsers, 1,000 Search and 1,000 Fetch calls, 15-minute sessions, 3 Agent runs and USD 5 in model tokens | capture: sha256:7db04564d51fcfc0eeb0a6114b7753415b84f819b4cd93c9e62ce7f735d53ad7 | quote: ## Free Plan $0/mo [Start for free](/sign-up) Get started with Browserbase. Explore and prototype ideas. Infrastructure - 3 concurrent browsers - 1 browser hour - 3 Agent runs included - 1,000 Search calls - 1,000 Fetch calls - 15 minutes /session Capabilities - Models $5 in tokens - Runtime included
  - [2] 2026-11-19: the sign-up asks for an email address and a phone number on the email path | capture: sha256:b4339f5043b0035f006719e394d4acb34b50141112db7dc1c7072560e4bf2231 | quote: E-mail address* Phone number*
  - [3] 2026-11-19: the Free plan's browser hours are a recurring monthly allocation, not a one-time grant | capture: sha256:3e1290b28412b8f48da5199f6fca2bae2c697cef7e6259bfd880d8560c3f2946 | quote: Each plan includes a monthly allocation of browser hours and proxy bandwidth (and more). Go beyond it and pay-as-you-go overage rates apply. No caps. No cut-offs.
  - [3] 2026-11-19: the first-party docs state the Free plan needs no credit card and includes 3 concurrent sessions | capture: sha256:3e1290b28412b8f48da5199f6fca2bae2c697cef7e6259bfd880d8560c3f2946 | quote: Start free, no credit card needed. Includes 3 concurrent sessions.
- sources:
  - [1] https://www.browserbase.com/pricing
  - [2] https://www.browserbase.com/sign-up
  - [3] https://docs.browserbase.com/account/billing/plans
