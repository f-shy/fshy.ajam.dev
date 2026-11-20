# Mixpanel

> mixpanel.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixpanel/ | JSON https://fshy.ajam.dev/api/v1/entity/mixpanel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mixpanel

- `dev-services/mixpanel` | qualifies-with-caveat | evidence documented | binding volume-quota | category product analytics with session replay, experiments and feature flags (hosted) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://mixpanel.com/pricing/
- free tier: Free plan, free forever with no credit card required: up to 1M events per month, unlimited seats, 10K session replays per month, up to 1k monthly experiment users, up to 10 active feature flags, 5 saved reports per seat; the Query API is not part of Free | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: Events, session replays and experiment users each have their own monthly count, so no single unit of the vocabulary fits. The Growth plan starts at USD 0 for the first 1M events a month and bills further events by volume tier; what the Free plan does with events past 1M is unverified: not stated on the pages read.
- per-object cap: the import endpoint accepts up to 2000 events and 10MB uncompressed per request | source: [2]
- retention: event data is deleted 2 years after ingestion by default on Free, Growth and Enterprise, and a custom policy is an Enterprise feature; session replays are kept 30 days | days: 730 | source: [1]
- egress: the Query API, which downloads reports as CSV, PNG or PDF or exports results to JSON or CSV, is not available on Free; whether the Raw Data Export API is open to a Free project is unverified: the pricing page lists only Ingestion & export API access (Import historical data) as available | metered: no | source: [1]
- identity: email | detail: The sign-up page offers a free account from an email address, with an agreement to the terms; the pricing page states no credit card is required. Any later step is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): up to 1M events per month on Free [1]
  - volume-quota (binding): 10K session replays and 1k monthly experiment users per month; up to 10 active feature flags [1]
  - request-rate: Ingestion API: 2GB of uncompressed JSON per minute or about 30k events per second, per project [3]
  - per-object-cap: 2000 events and 10MB uncompressed per import request [2]
  - retention-clamped: events deleted after 2 years by default; session replays kept 30 days [1]
- limits note: Free has no Query API.
- binding note: The 1M events a month is the first ceiling for an app with traffic, and the missing Query API means reports are read in the web app only.
- interface detail: The Ingestion API (import and track endpoints) authenticates with a project token as the basic auth username or with an Owner or Admin service account, at api.mixpanel.com or api-eu.mixpanel.com for EU data residency; an MCP server and Mixpanel Headless (work with Mixpanel as code) are listed as available on Free. The Query API is not part of Free.
- endpoint: https://api.mixpanel.com/import
- tooling: the Ingestion API, an MCP server, Mixpanel Headless and the web app
- composes with: Event analytics, funnels and retention for the front end of a free-hosted app, up to 1M events a month, with 10K session replays and 10 feature flags in the same project.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 2-year event retention and the 30-day session replay retention; a 429 answer means a per-project rate limit was reached
- notes: Companies founded less than 5 years ago with up to USD 8M in funding receive a first free year of the Startup Plan, a separate offer.
- evidence note: Plan limits are quoted from the first-party pricing page and the rate limits from its API documentation. No account was opened, so the behaviour past 1M events and any later sign-up step are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free plan is free forever and needs no credit card | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: Free plan ($0/month, free forever): Explore product intelligence for free, no credit card required.
  - [1] 2026-11-01: the Free plan includes up to 1M events, 10K session replays, 1k experiment users and 10 active feature flags, with unlimited seats | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: Includes unlimited seats, up to 1M events/month, 10K session replays/month, up to 1k MEU/month for experiments, up to 10 active feature flags, and funnels & retention analysis.
  - [1] 2026-11-01: the Growth plan starts at $0 a month with volume discounts | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: Growth plan (starts at $0/month, volume discounts available): Get advanced intelligence with higher limits.
  - [1] 2026-11-01: early-stage companies with up to USD 8M in funding receive a first free year of the Startup Plan | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: Early-stage companies that were founded less than 5 years ago, with up to $8M in total funding, and haven't redeemed any other offers receive their first year free on the Startup Plan.
  - [1] 2026-11-01: Free allows up to 1M monthly events | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - Monthly events: Free – Up to 1M; Growth – First 1M free, up to 20M; Enterprise – Up to 1T.
  - [1] 2026-11-01: Free has 5 saved reports per seat | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - Saved reports: Free – 5 per seat; Growth – Unlimited; Enterprise – Unlimited.
  - [1] 2026-11-01: Free session replays are kept 30 days | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - Replay retention: Free – 30 days; Growth – 30 days; Enterprise – 7-360 days.
  - [1] 2026-11-01: event data is deleted after 2 years by default and a custom policy is Enterprise only | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: Automatic delayed deletion of data after ingestion. Default 2 years for Free, Growth, and Enterprise plans.): Free – Not available; Growth – Not available; Enterprise – Available.
  - [1] 2026-11-01: the Query API is not available on Free | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: export report results to JSON or CSV.): Free – Not available; Growth – Available; Enterprise – Available.
  - [1] 2026-11-01: ingestion and export API access for importing historical data is available on Free | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - Ingestion & export API access (Import historical data.): Free – Available; Growth – Available; Enterprise – Available.
  - [1] 2026-11-01: Mixpanel Headless, working with Mixpanel as code, is available on Free | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - Mixpanel Headless (Work with Mixpanel as code. Learn more here.): Free – Available; Growth – Available; Enterprise – Available.
  - [1] 2026-11-01: an MCP server is available on Free | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - MCP server: Free – Available; Growth – Available; Enterprise – Available.
  - [1] 2026-11-01: US or EU data residency is available on Free and chosen at project creation | capture: sha256:402d0c346d667d3df0634407cdeb7a92a5331e3741e7e35ad730c147ec46cee9 | quote: - US or EU data residency (Can be enabled during project creation; not enabled by default.): Free – Available; Growth – Available; Enterprise – Available.
  - [3] 2026-11-01: the Ingestion API allows 2GB of uncompressed JSON a minute or about 30k events a second per project | capture: sha256:74b200ff92a58963f6f65a72f8d31b8067189ba667c912f7b74f992be53ec217 | quote: 2GB of uncompressed JSON/minute or \~30k events per second, measured on a rolling 1 minute basis.
  - [3] 2026-11-01: rate limits are scoped per project and a 429 answer means a limit was reached | capture: sha256:74b200ff92a58963f6f65a72f8d31b8067189ba667c912f7b74f992be53ec217 | quote: These rate limits are scope per project.
  - [2] 2026-11-01: the data collection server is a regional host, api for the US and api-eu for EU data residency | capture: sha256:eebaa5c52978509eb399a6ae40ee6d6369f63ec0270d722aa881c9bb4cafd287 | quote: `api` - The default (US) servers used for most projects * `api-eu` - EU servers if you are enrolled in EU Data Residency
  - [2] 2026-11-01: an import request accepts up to 2000 events and 10MB uncompressed | capture: sha256:eebaa5c52978509eb399a6ae40ee6d6369f63ec0270d722aa881c9bb4cafd287 | quote: We accept up to 2000 events and 10MB uncompressed per request.
  - [2] 2026-11-01: the import endpoint accepts a project token as the basic auth username | capture: sha256:eebaa5c52978509eb399a6ae40ee6d6369f63ec0270d722aa881c9bb4cafd287 | quote: `/import` also supports [Project Token](https://docs.mixpanel.com/reference/project-token.md) as an authentication method. You can provide your token as the basic auth username value with an empty password.
  - [4] 2026-11-01: the sign-up page offers a free account from an email address | capture: sha256:3f617d120addda53393c6b07c2e4b437532474304c2d632cca767d71165ba1d3 | quote: Sign up for a free account. or Email
- sources:
  - [1] https://mixpanel.com/pricing/
  - [2] https://docs.mixpanel.com/reference/import-events
  - [3] https://docs.mixpanel.com/reference/rate-limits
  - [4] https://mixpanel.com/register/
