# TinyFish

> tinyfish.ai | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tinyfish/ | JSON https://fshy.ajam.dev/api/v1/entity/tinyfish.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TinyFish (Compute)

- `compute/tinyfish` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.985Z (live) | stale on 2026-12-07
- url https://www.tinyfish.ai/pricing
- free tier: Search and Fetch are free at any wallet balance, within 30 requests a minute and 500 an hour for Search and 150 URLs a minute and 1,000 a day for Fetch; an $8 wallet grant covers Agent and Browser | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: an email address at sign-up: the sign-up page asks for 'Email address'. No credit card is required: '$8 free in your wallet — no credit card required'. The phone requirement is not published on https://agent.tinyfish.ai/sign-up. Country: not published on https://agent.tinyfish.ai/sign-up.
- interface: rest, cli
- limits:
  - request-rate (binding): Search is capped at 30 requests a minute and 500 an hour on the free path [1]
  - request-rate (binding): Fetch is capped at 150 URLs a minute and 1,000 a day on the free path [1]
  - retention-clamped: an $8 wallet grant is one-time; Agent and Browser need funds to start, and a run under way finishes at a zero balance [1]
- interface detail: HTTP API endpoints for Agent, Research, Search, Fetch and Browser, plus SDKs, a CLI and MCP per the pricing page
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states which meters are free at a zero balance and which draw from the wallet. The distinction is the whole finding: two of four products are free indefinitely
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: Search and Fetch answer a request; Agent runs are capped at 2 concurrent and Browser sessions at 5
  - free_tier_kind: one-time-credit
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: no subscription and no monthly minimum
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Search and Fetch free at any Wallet balance' with 'Search at 30 requests / min and 500 requests / hour, Fetch at 150 urls / min and 1,000 urls / day. No charge, no Wallet draw, and they keep working at a $0 balance.' and 'New accounts start with $8 in Wallet funds', quoted
  - [2] 2026-11-04: the docs list HTTP API endpoints | capture: sha256:2bdba7acbddd2fe9431cd4f0130a2e68b4fa04d05187c46b2c39ec6f01a7a8bc | quote: | Search | `GET https://api.search.tinyfish.ai` |
  - [1] 2026-11-04: the pricing page lists SDKs, a CLI and MCP | capture: sha256:ab9fc67de4212d5cf874737ec0e26197ebc2177851e36f8346ce43f34f857fe4 | quote: –SDKs, CLI, and MCP
  - [3] 2026-11-04: the sign-up form asks for an email address | capture: sha256:cbc00e28a0a5cf0a63137d0884bc77ef45b4a327cb3c6f78da14c59d969785dc | quote: Email address
  - [3] 2026-11-06: the free wallet grant needs no credit card | capture: sha256:cbc00e28a0a5cf0a63137d0884bc77ef45b4a327cb3c6f78da14c59d969785dc | quote: $8 free in your wallet — no credit card required
  - [3] 2026-11-06: the sign-up form asks for an email address | capture: sha256:cbc00e28a0a5cf0a63137d0884bc77ef45b4a327cb3c6f78da14c59d969785dc | quote: Email address
- sources:
  - [1] https://www.tinyfish.ai/pricing
  - [2] https://docs.tinyfish.ai
  - [3] https://agent.tinyfish.ai/sign-up

## TinyFish (Crawling)

- `crawler-scraper/tinyfish` | qualifies-with-caveat | evidence documented | binding request-rate | category search and fetch API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.tinyfish.ai/pricing
- free tier: Search free at 30 requests a minute and 500 an hour; Fetch free at 150 URLs a minute and 1,000 URLs a day | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a request or a URL | source: [1]
- retention: the fetch allowance resets daily | source: [1]
- egress: not applicable: JSON and Markdown answers | metered: no | source: [1]
- identity: email | detail: no card stated; signup is an account
- interface: rest
- limits:
  - request-rate (binding): search 30 requests a minute and 500 an hour [1]
  - request-rate (binding): fetch 150 URLs a minute and 1,000 URLs a day [1]
- interface detail: REST search and fetch; free per request, no plan and no monthly minimum
- tooling: not established
- composes with: The read path's step-3 renderer behind Jina
- reliability: no reliability event recorded
- notes: The pricing page states 500 an hour, which is 12,000 a day only if the hour cap is sustained for all 24 hours; 30 a minute is 1,800 an hour. Treat 500 an hour as the cap and 42,000 a day as impossible.
- evidence:
  - [1] 2026-10-22: Search free, limits 30 requests a minute and 500 an hour; Fetch free, limits 150 URLs a minute and 1,000 URLs a day; Agent USD 0.016 a step; Browser USD 0.002 a minute
  - [2] 2026-10-22: pinned read answered 200 with a rewrite, so the fetch leg is live
- sources:
  - [1] https://www.tinyfish.ai/pricing
  - [2] https://example.com/?__provider=tinyfish
