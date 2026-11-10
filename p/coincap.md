# CoinCap

> coincap.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coincap/ | JSON https://fshy.ajam.dev/api/v1/entity/coincap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoinCap

- `data-apis/coincap` | qualifies-with-caveat | evidence documented | binding request-rate | category crypto market data API (assets, exchanges, markets, rates, indicators) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://pro.coincap.io/api-docs
- free tier: Free tier: 500 credits per month at 5 API calls per minute, with no WebSocket access; each call costs 1 credit plus 1 more per 2,500 bytes of response | unit: credits | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Every call needs an API key, also on the Free tier; the old keyless v2 host is not the current API. Responses to identical requests may come from a 60-second cache and are billed like fresh ones. Ten agent-friendly endpoints can instead be paid per call in USDC with no account. Paid tiers start at Builder, 50,000 credits per month at 30 calls per minute.
- per-object cap: 100 results per page by default, up to 2,000 per page on request | source: [1]
- retention: not applicable | note: History reaches back to July 2010 for Bitcoin; depth varies by asset.
- egress: not metered in bytes, but each 2,500 bytes of a response costs 1 extra credit against the 500-credit monthly allowance | metered: yes | free allowance: 500 credits per month | source: [1]
- identity: email | detail: A key needs an account made at coincap.io; the vendor says no credit card is required. The fields of the sign-up form were not read, so email as the only identifier is unverified: behind a sign-up.
- interface: rest
- limits:
  - request-rate (binding): 5 API calls per minute on the Free tier [1]
  - request-rate (binding): 500 credits per month on the Free tier, 1 credit per call plus 1 per 2,500 bytes [1]
- limits note: Bulk path: none; pages of up to 2,000 rows. Storage terms: not read (unverified: the terms page captured answered HTTP 404).
- binding note: 500 credits a month, spent at 1 credit or more per call, run out long before the 5 calls per minute matter.
- interface detail: GET https://rest.coincap.io/v3/... with Authorization: Bearer KEY or the apiKey query parameter; an MCP endpoint and WebSocket (paid tiers) also exist
- endpoint: part of interface detail
- tooling: curl or any HTTP client; an OpenAPI 3.0 spec is published
- composes with: Spot prices and history for a few hundred calls a month; CoinPaprika and CoinLore cover the same ground with no key.
- reliability: A call with no key answers HTTP 401; the Free tier is capped at 5 calls per minute.
- notes: 500 credits a month is the binding quota; the keyless route exists only as paid per-call USDC. Bulk path: none. Storage terms: unverified.
- evidence note: Tier numbers are read from the vendor docs and pricing page; a keyless call answered 401. The key was not exercised.
- extras:
  - bulk_path: none; pages of up to 2,000 rows
  - history_depth: back to July 2010 for Bitcoin; varies by asset
- evidence:
  - [1] 2026-11-02: the Free tier is 500 credits a month at 5 calls a minute, REST only | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: Rate limits vary by tier, from 5 API calls per minute on the Free tier up to 900 on Enterprise.
  - [1] 2026-11-02: Free tier credits per month and no WebSocket | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: Free Tier ... 500 credits per month ... 5 API calls per minute ... NO web-socket access
  - [1] 2026-11-02: credit cost per call | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: Each API call charges a base cost of 1 credit, and then 1 additional credit per 2,500 bytes of additional data.
  - [1] 2026-11-02: every call needs a bearer token | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: All API calls require a bearer token in the header or URL.
  - [1] 2026-11-02: a response may be served from a 60-second cache and is billed the same | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: Responses to identical requests may be served from an in-memory cache for up to 60 seconds to improve performance. Cached responses are billed the same as fresh responses.
  - [1] 2026-11-02: page size is 100 by default and up to 2,000 | capture: sha256:a6cb2946aea9868670a2720110c472d211755caee526bfdb137a711f4799c22a | quote: a single page offers 100 responses by default and supports up to 2,000 responses per page upon requests
  - [2] 2026-11-02: the Free plan needs no card and does not expire | capture: sha256:b8661d3f0f87cb40e3c386e6e9317ce5d246ee0b4ae315cccd9887d5ebca31a0 | quote: The Free plan includes 500 credits per month and 5 requests per minute with no credit card and no expiration
  - [3] 2026-11-02: history reaches back to July 2010 | capture: sha256:8c78c194d1b1e1fa24b7bcc184b5c51caedfb6a5e1bfee2a4888583d2697f977 | quote: Back to July 2010, starting from Bitcoin's first recorded price of $0.086.
  - [3] 2026-11-02: ten endpoints accept pay-per-call USDC with no account | capture: sha256:8c78c194d1b1e1fa24b7bcc184b5c51caedfb6a5e1bfee2a4888583d2697f977 | quote: Ten agent-friendly routes accept x402 pay-per-call payment in USDC on Base instead of an account
  - probe:https://rest.coincap.io/v3/price/bysymbol/BTC 2026-11-03: a call with no key answers HTTP 401 | capture: sha256:cd14ebce354acf278226c18235690dc657bb88198e317e08f93408a0a097dad4 | quote: "status": 401
- sources:
  - [1] https://pro.coincap.io/api-docs
  - [2] https://splash.coincap.io/pricing
  - [3] https://splash.coincap.io/
