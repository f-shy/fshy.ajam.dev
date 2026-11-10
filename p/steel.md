# Steel

> steel.dev | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/steel/ | JSON https://fshy.ajam.dev/api/v1/entity/steel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Steel

- `compute/steel` | trial-only | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://steel.dev/pricing
- price parsed USD 43/mo
- free tier: Launch: USD 0 a month plus usage, USD 30 of credits one time, 10 concurrent sessions, sessions up to 15 minutes, no credit card needed | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the USD 30 is one time; Scale is USD 250 a month with USD 100 of credits each month
- per-object cap: not applicable
- retention: data retention is 7 days on Launch and 14 days on Scale | days: 7
- egress: proxy bandwidth USD 10 per GB on Launch and USD 6 per GB on Scale | metered: yes | price per TB: USD 10,240 per TB | source: [1]
- identity: email | detail: 'No credit card needed' on the Launch plan, quoted
- interface: rest, cli
- limits:
  - retention-clamped (binding): sessions up to 15 minutes on Launch; 1 hour on Scale [1]
  - request-rate: 60 requests a minute on Launch; 10 concurrent sessions [1]
  - per-ip-shaping: proxy bandwidth USD 10 per GB on Launch [1]
- limits note: data retention is 7 days on Launch, 14 on Scale
- binding note: the 15-minute session cap on Launch binds first, and it doubles with the plan step to Scale
- interface detail: REST API and SDKs; a hosted browser over CDP
- tooling: Steel SDK, Playwright and Puppeteer over CDP, a scraping endpoint
- composes with: a 15-minute session and a 60-request-a-minute cap make this a scrape worker, not a crawl platform
- reliability: no reliability event recorded
- notes: USD 30 of credit at USD 0.10 a browser hour is 300 hours, but the 15-minute session cap turns that into 1,200 sessions with setup between each.
- extras:
  - billing_model: wall-clock
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.wall_clock_min: 15
  - session_cap.restart_required: yes
  - session_cap.note: 15 min on Launch, 60 on Scale, up to 24 h on Enterprise
  - keep_rate.value: 0.0
  - keep_rate.basis: per browser hour
  - keep_rate.source: https://steel.dev/pricing
  - persistent_storage.durability: sessions and data retained 7 days on Launch
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 7 days
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: CDP
  - free_tier_kind: one-time-credit
  - m10h_usd: 30.0
  - m24h_usd: 43.0
  - price_arithmetic: USD 30 of credit at USD 0.10/h is 300 browser hours, in 15-minute sessions
  - price_note: 300 browser hours at USD 0.10 an hour is USD 30, which the one-time credit covers exactly. 730 hours is USD 73 of usage, minus the USD 30 credit, so USD 43.00. The 15-minute session cap makes 300 hours 1,200 sessions.
  - price_basis: 300 and 730 BROWSER HOURS, not a 2 vCPU shape. A browser host sells minutes of a remote browser, so these rows are not comparable with a sandbox row.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: Launch: USD 0 a month plus usage, USD 30 of credits one time, 10 concurrent sessions, 15-minute sessions, no credit card
  - [1] 2026-10-22: browser hours USD 0.10 on Launch and USD 0.08 on Scale; proxy bandwidth USD 10 and USD 6 per GB
- sources:
  - [1] https://steel.dev/pricing

## Steel.dev

- `crawler-scraper/steel` | trial-only | evidence documented | binding retention-clamped | category headless browser
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:02:34.147Z (live) | stale on 2026-12-03
- url https://steel.dev/
- free tier: USD 30 of credits, one time, valid 90 days (about 300 browser hours at USD 0.10 an hour); 10 concurrent sessions of up to 15 minutes | unit: mixed | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: one-time credit valid for 90 days; no credit card required; CAPTCHA solving and Steel-provided proxies on Launch need a USD 10 paid deposit, which free credits do not cover
- per-object cap: not applicable: the unit is a browser session | source: [2]
- retention: session data is kept 7 days on Launch; the USD 30 credit expires after 90 days | days: 7 | source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: email | detail: an account opened with an email address, which the sign-up verifies by a code or a link, or with GitHub or Google; the sign-up configuration has no phone field and no CAPTCHA, makes first and last names optional, and blocks disposable email domains and email sub-addresses; what the dashboard asks after sign-up is unverified: behind a sign-up
- interface: rest
- limits:
  - request-rate: 10 concurrent browser sessions and 60 requests a minute on the Launch plan [1]
  - retention-clamped (binding): the USD 30 credit expires after 90 days [1]
- limits note: Browser Tools calls (/scrape, /screenshot, /pdf) are limited to 20 requests a minute per organization, under the plan's request rate
- binding note: the USD 30 credit is one-time and lapses after 90 days; a Launch session ends at 15 minutes
- interface detail: REST sessions and a scrape route; 10 concurrent and 20 requests a minute on Browser Tools
- tooling: a session model with a browser control protocol
- composes with: A session model, so it is the wrong shape for a Worker and the right shape for a long agent run
- reliability: no reliability event recorded
- notes: A 421 naming the missing route is the useful shape: it distinguishes a wrong path from a dead host. Every other browser provider in this class answered 401, which proves less.
- evidence note: free tier, limits, retention and the deposit rule read on the vendor's pricing and docs pages
- evidence:
  - [3] 2026-10-22: 421 with a 35-byte body reading `No route defined for GET /v1/scrape`: the host is live and the path is wrong, which proves the API exists and not that the route does
  - [1] 2026-10-30: the Launch plan's USD 30 of credits is one-time and valid 90 days | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: Launch includes $30 in one-time free usage credits, valid for 90 days.
  - [1] 2026-10-30: the Launch plan allows 60 requests a minute; the same table gives it 10 concurrent sessions | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: | Limits | Requests per minute | 60 | 600 | Custom |
  - [1] 2026-10-30: the Launch plan runs 10 sessions at once | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: | Features | Concurrent browser sessions | 10 | 100 | 1,000+ |
  - [4] 2026-10-30: Browser Tools calls have their own 20-a-minute limit per organization | capture: sha256:74050b053fe26b60795385b435c1a2f9f4743c1d8b0ce687e3be28c3c4502071 | quote: Calls are rate limited to 20 requests per minute per organization.
  - [1] 2026-10-30: the Launch plan keeps data 7 days | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: | Limits | Data retention | 7 days | 14 days | Custom |
  - [1] 2026-10-30: proxies and CAPTCHA solving on the free plan need a USD 10 paid deposit | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: To use CAPTCHA solving or Steel-provided proxies on Launch, verify your account by adding $10 in paid balance.
  - [5] 2026-10-30: the quickstart opens an account with no credit card | capture: sha256:b4293dac4575356771e569195403817dca6a5a08158f31c30ad51eb33adb3226 | quote: No credit card required
  - [6] 2026-10-30: the pricing page's Launch card needs no credit card | capture: sha256:db0a3543db430c6f30b30cf91c2f046b01a9531305ae0c895c9ff5b4767a94e4 | quote: No credit card needed
  - [7] 2026-11-01: the sign-up configuration served by the vendor's authentication service requires an email address verified at sign-up, turns the phone number and CAPTCHA off, makes first and last names optional, and blocks disposable email domains and email sub-addresses | capture: sha256:3fa35f37334836816a238e73acd962fab20738d62909ebbf263e6b175e69abe1 | quote: "email_address":{"enabled":true,"required":true ... "phone_number":{"enabled":false,"required":false ... "first_name":{"enabled":true,"required":false ... "captcha_enabled":false ... "block_email_subaddresses":{"enabled":true},"block_disposable_email_domains":{"enabled":true}
  - [1] 2026-11-01: the pricing and limits page lists the Launch credit, the request rate, the data retention and the USD 10 deposit rule | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: $30 in one-time free usage credits, valid for 90 days ... Requests per minute | 60 | 600 ... Data retention | 7 days | 14 days ... verify your account by adding $10 in paid balance
  - [8] 2026-11-02: the vendor's docs state a one-time Launch credit valid for 90 days, no credit card required, and a USD 10 paid deposit for CAPTCHA solving or Steel-provided proxies that free credits do not cover | capture: sha256:46ac8a61f1928c99315cbad15ed7b348b488002b4adb3f3ad0ae873ee378791b | quote: Launch includes $30 in one-time free usage credits, valid for 90 days. ... No credit card required ... To use CAPTCHA solving or Steel-provided proxies on Launch, verify your account by adding $10 in paid balance. Free credits do not count.
  - [9] 2026-11-01: the sign-in page offers GitHub, Google and email as the ways in | capture: sha256:efb4433b896ad858f0fe887bde446360615d931a52d418e3b5efd6582c6b5885 | quote: Continue with GitHubContinue with Google ... Continue with email
  - [5] 2026-11-01: the quickstart opens an account for the Launch credits with no credit card | capture: sha256:b4293dac4575356771e569195403817dca6a5a08158f31c30ad51eb33adb3226 | quote: No credit card required
  - [6] 2026-11-01: the pricing page's Launch card needs no credit card | capture: sha256:db0a3543db430c6f30b30cf91c2f046b01a9531305ae0c895c9ff5b4767a94e4 | quote: No credit card needed
  - [1] 2026-11-01: the pricing and limits page lists the Launch plan at USD 30 of one-time credits valid for 90 days, 10 concurrent sessions, 15-minute sessions, 60 requests a minute and 7 days of data retention | capture: sha256:55115f2554c7ea9c57b12b64d1fde291f49bdf4ed5ef08894f95e58d349c41e0 | quote: $30 in one-time free usage credits, valid for 90 days ... Concurrent browser sessions | 10 | 100 ... Max session time | 15 minutes | 1 hour ... Requests per minute | 60 | 600 ... Data retention | 7 days | 14 days
- sources:
  - [1] https://docs.steel.dev/overview/pricinglimits
  - [2] https://steel.dev/
  - [3] https://api.steel.dev/v1/scrape?url=https://example.com
  - [4] https://docs.steel.dev/overview/browser-tools/overview
  - [5] https://docs.steel.dev/overview/sessions-api/quickstart
  - [6] https://steel.dev/pricing
  - [7] https://clerk.steel.dev/v1/environment
  - [8] https://docs.steel.dev/llms-full.txt
  - [9] https://app.steel.dev/sign-in
