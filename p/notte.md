# Notte

> notte.cc | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/notte/ | JSON https://fshy.ajam.dev/api/v1/entity/notte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Notte (Compute)

- `compute/notte` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:20.762Z (live) | stale on 2026-12-05
- url https://www.notte.cc/pricing
- free tier: a free start without a card: USD 10 of credits granted once with no expiry, spendable on sessions, proxies, LLMs and functions; 5 concurrent browsers and a 15-minute maximum session | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no included data-transfer allowance published; proxy traffic is billed from credits at USD 10 per GB (residential) or USD 0.20 per GB with a bring-your-own proxy on Startup | metered: yes | source: [1]
- identity: email | detail: 'Try the full platform without a card', quoted from notte.cc/pricing read 2026-10-22
- interface: rest, cli
- limits:
  - request-rate (binding): 5 concurrent browser sessions on the free tier, 25 on the $20 tier [1]
  - retention-clamped: Free: USD 10 of credits granted once with no expiry; paid-plan monthly credits expire each cycle [1]
  - per-ip-shaping: a bring-your-own proxy is $0.20 a GB [1]
- interface detail: a REST API, Python and TypeScript SDKs (NotteClient) and a CLI
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the no-card start, the 5-browser concurrency and that paid credits expire each cycle. The free credit's size is not published, so the record does not put a number on it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: bounded by 5 concurrent browsers; the page states no session clock
  - free_tier_kind: allowance
  - burst_x: 1.0
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: proxies are billed from the credit at $0.20 a GB
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Try the full platform without a card.' with 'Credits cover: sessions, proxies, LLMs, functions', 'Browser concurrency: 5', and on the paid tier '$20 credits / mo' with 'Monthly credits expire each cycle', quoted
  - [1] 2026-11-03: proxy traffic is billed per GB from credits | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Billed when enabled. BYO proxy: $0.20 / GB
  - [1] 2026-11-03: the Free plan grants a one-time credit with no expiry | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Granted once. No expiry.
  - [2] 2026-11-03: an API reference exists | capture: sha256:092acce7091d09ae44a150ac3b17d54ad9b8f8762204210078e121e222ea1411 | quote: Explore authentication, endpoints, parameters, and API responses.
  - [3] 2026-11-03: a CLI setup exists | capture: sha256:7a837097221f913774d64c876bcac5a5e539b73deb4e9e3a6c566e16a35f0e46 | quote: This is the shared source for CLI setup, authentication, and the browser-to-code workflow.
- sources:
  - [1] https://www.notte.cc/pricing
  - [2] https://docs.notte.cc/
  - [3] https://docs.notte.cc/sdk-reference/manual/index.md

## Notte (Crawling)

- `crawler-scraper/notte` | trial-only | evidence documented | binding retention-clamped | category headless browser
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:02:34.146Z (live) | stale on 2026-12-03
- url https://www.notte.cc/
- free tier: USD 10 of credits, granted once with no expiry, spent on sessions, proxies, LLM tokens and functions; 5 concurrent browsers and 15-minute sessions | unit: mixed | metered on: wall-clock | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable: the unit is a session | source: [2]
- retention: the credits do not expire; a session is capped at 15 minutes | source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: email | detail: an account opened with an email magic link, Google, GitHub, AgentID or SSO; the free plan needs no card
- interface: rest
- limits:
  - request-rate: 5 concurrent sessions [1]
  - retention-clamped (binding): a session is capped at 15 minutes [1]
- limits note: POST /sessions/start, POST /agents/start and the prompt helpers each have per-minute, per-hour and per-day windows counted per API key; the free plan's numbers are on neither the pricing page nor the rate-limit reference
- binding note: a free-plan session ends at 15 minutes, with 5 browsers at once
- interface detail: REST sessions; 5 concurrent and 15 minute sessions
- tooling: an agent-oriented session API
- composes with: A session model with a 15-minute cap, so a long crawl needs resubmission
- reliability: no reliability event recorded
- notes: At the listed USD 0.01 a browser-hour, the one-time USD 10 credit is 1,000 hours of browser sessions, before the proxy, function and LLM-token charges that draw on the same credit; a Free-plan session ends at 15 minutes.
- evidence note: free tier, concurrency, session cap and sign-in options read on the vendor's pricing and console pages; the per-minute rate is not published for the free plan
- evidence:
  - [3] 2026-10-22: 401 with a 30-byte JSON body `Not authenticated`: the route exists and needs a key
  - [1] 2026-10-30: the Free plan's USD 10 of credits is granted once and does not expire | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Granted once. No expiry.
  - [1] 2026-10-30: the Free plan runs 5 browsers at once | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Browser concurrency- 5
  - [1] 2026-10-30: a Free plan session lasts at most 15 minutes | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Session duration- 15 min
  - [4] 2026-10-30: the API rate-limits session and agent starts per key in minute, hour and day windows whose sizes depend on the plan | capture: sha256:01ebd8b53f8893281b9510726612667ce11ddfc0571f7e9854f48616015544af | quote: Each endpoint has a per-minute, per-hour, and per-day window.
  - [5] 2026-10-30: the console sign-in takes an email magic link or an OAuth provider | capture: sha256:427ae61689922767add9c610afecda5ecaaa8f0586a1e7a7a89014108997889a | quote: Use an email magic link or continue with oauth
  - [1] 2026-10-30: the Free plan needs no card | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Try the full platform without a card.
  - [5] 2026-10-30: the OAuth options are Google, GitHub, AgentID and SSO | capture: sha256:427ae61689922767add9c610afecda5ecaaa8f0586a1e7a7a89014108997889a | quote: Use GoogleUse GitHubUse AgentIDContinue with SSO
  - [1] 2026-11-02: the pricing page lists browser sessions at USD 0.01 an hour and a one-time USD 10 Free credit that covers sessions, proxies, LLMs and functions, with 15-minute sessions | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Browser Sessions $0.01 / hour ... $10 credits Granted once. No expiry. Credits cover- Sessions, proxies, LLMs, functions ... Session duration- 15 min
  - [1] 2026-11-02: the Free card lists a start with no card, USD 10 of credits granted once with no expiry for sessions, proxies, LLMs and functions, 5 concurrent browsers and 15-minute sessions | capture: sha256:e132955d9bc8a4bd981e388ecb2262080989d181d524257d081b492938441712 | quote: Try the full platform without a card. ... $10 credits Granted once. No expiry. ... Credits cover- Sessions, proxies, LLMs, functions ... Browser concurrency- 5 ... Session duration- 15 min
  - [5] 2026-11-02: the console sign-in takes an email magic link, or Google, GitHub, AgentID or SSO | capture: sha256:427ae61689922767add9c610afecda5ecaaa8f0586a1e7a7a89014108997889a | quote: Use an email magic link or continue with oauth ... Use GoogleUse GitHubUse AgentIDContinue with SSO
- sources:
  - [1] https://www.notte.cc/pricing
  - [2] https://www.notte.cc/
  - [3] https://api.notte.cc/sessions
  - [4] https://docs.notte.cc/api-reference/rate-limits
  - [5] https://console.notte.cc/signin
