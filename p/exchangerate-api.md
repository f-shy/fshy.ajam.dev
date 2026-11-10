# ExchangeRate-API

> exchangerate-api.com | Data APIs; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exchangerate-api/ | JSON https://fshy.ajam.dev/api/v1/entity/exchangerate-api.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExchangeRate-API (exchangerate-api.com)

- `data-apis/exchangerate-api` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (daily updates on the free plan) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://www.exchangerate-api.com/
- disagrees on identity_kind: `data-apis/exchangerate-api` says email, `data-apis/exchangerate-api-open` says anonymous
- free tier: Free plan, USD 0, no card: 1.5K API requests a month with an API key, rates updated once every 24 hours. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The quota is soft-capped at 100 percent, with a little extra room. The Free plan has the standard and pair-conversion endpoints and base currency switching; historical data is for paid accounts only. The Pro plan is USD 10 a month for 30k requests, hourly updates and history from 1990. A separate keyless Open API has its own record (data-apis/exchangerate-api-open).
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 1.5K requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for an email and a password, and the key is active after email confirmation; no card for the Free plan.
- interface: rest
- limits:
  - volume-quota (binding): 1.5K API requests a month on the Free plan, soft-capped at 100 percent [1]
  - retention-clamped: no historical data on a free account; the history endpoint is for paid accounts [2]
- limits note: Rate per minute: not stated for the keyed plan on the pages read. Bulk path: none on the free plan.
- binding note: 1.5K requests a month binds first; the rates change once a day, so about 30 requests a month cover a full daily refresh.
- interface detail: GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD (standard) and a pair-conversion request; JSON
- endpoint: https://v6.exchangerate-api.com/v6/latest
- tooling: curl or any HTTP client
- composes with: Daily rates for all currencies: one call a day uses about 30 of the 1.5K requests a month. The keyless Open API in data-apis/exchangerate-api-open needs no key at all.
- reliability: The vendor states that any aspect of a free plan, the quota included, may change or end at any time without notice.
- notes: Free requests: 1.5K a month. Rate limit: no per-minute rate stated; a soft cap at 100 percent of the quota. re-distribution is not allowed. Bulk path: none on the free plan; the keyless Open API is a separate lane.
- evidence note: Quota, update rate, history gate, caching and sign-up fields are quoted from first-party home, docs, terms and sign-up pages. No key was created.
- extras:
  - bulk_path: none on the free plan; history is paid
  - free_requests: 1.5K a month
  - history_depth: none on free; from 1990 on paid plans
- evidence:
  - [1] 2026-11-02: the Free plan card lists 1.5K API requests a month | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: - 1.5K API Requests p/m
  - [3] 2026-11-02: the free API with a key allows 1.5k requests a month | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: - 1.5k Requests p/m
  - [1] 2026-11-02: free rates update once every 24 hours | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: Our free exchange rate data is updated once every 24 hours.
  - [1] 2026-11-02: the Free plan needs no card | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: No credit card details required for Free plan!
  - [1] 2026-11-02: the quota is soft-capped at 100 percent | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: We softcap at 100% so you'll have a little extra room in the event you reach your plan limit.
  - [1] 2026-11-02: the key is active after email confirmation | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: Your API key will be active & enabled after email confirmation.
  - [1] 2026-11-02: Pro is USD 10 a month | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: Pro is only $10 p/m
  - [1] 2026-11-02: Pro allows 30k requests a month | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: - 30k API Requests p/m
  - [4] 2026-11-02: the sign-up page is for the free plan | capture: sha256:692f003077c82a3f0946768caaa37a1a0239dd39549cf1aad19c6e5da0c19aa3 | quote: You're signing up to our free plan!
  - [4] 2026-11-02: the sign-up form has an email field | capture: sha256:692f003077c82a3f0946768caaa37a1a0239dd39549cf1aad19c6e5da0c19aa3 | quote: Email
  - [4] 2026-11-02: the sign-up form has a password field | capture: sha256:692f003077c82a3f0946768caaa37a1a0239dd39549cf1aad19c6e5da0c19aa3 | quote: Password
  - [5] 2026-11-02:  | capture: sha256:03ca0f3303c247f32d873fbc3d682f80ed3b93d60dcfa3a44b2aff0fcbdae0da | quote: This license does not restrict Free Plan accounts differently to paid accounts, so both Free Plan and paid ExchangeRate-API accounts are suitable for either commercial or personal use.
  - [5] 2026-11-02: the data caching policy permits storing and re-using retrieved data | capture: sha256:03ca0f3303c247f32d873fbc3d682f80ed3b93d60dcfa3a44b2aff0fcbdae0da | quote: Users are given permission to store & re-use any data retrieved from our API.
  - [5] 2026-11-02: the data may not be re-distributed | capture: sha256:03ca0f3303c247f32d873fbc3d682f80ed3b93d60dcfa3a44b2aff0fcbdae0da | quote: this license does not permit re-distribution of our data.
  - [5] 2026-11-02: free plan terms may change at any time | capture: sha256:03ca0f3303c247f32d873fbc3d682f80ed3b93d60dcfa3a44b2aff0fcbdae0da | quote: Any aspect of any of the available Free Plans is subject to change at any time - entirely at the discretion of ExchangeRate-API.
  - [2] 2026-11-02: history is for paid accounts only | capture: sha256:cfd21d2538a9d8bbc140b2fc7aa3560526a8aaa2f2e8fdc2e292e802d3426597 | quote: Historical exchange rates are only accessible by paid accounts.
  - [2] 2026-11-02: the history reaches back to 1990 on paid plans | capture: sha256:cfd21d2538a9d8bbc140b2fc7aa3560526a8aaa2f2e8fdc2e292e802d3426597 | quote: From 1 January 1990 to 31 December 2020
  - [6] 2026-11-02: the free plan has the standard and pair-conversion endpoints and base currency switching | capture: sha256:e2f660785ef0461448c7169ebc6232a8f0f670532fc6111e183babab96c3dc86 | quote: this plan includes use of our [Standard endpoint](https://www.exchangerate-api.com/docs/standard-requests) and [Pair Conversion endpoint](https://www.exchangerate-api.com/docs/pair-conversion-requests) as well as the ability to switch base currency.
  - [1] 2026-11-02: Pro updates every 60 minutes | capture: sha256:e31648679b962c50a729cd71c21cf100669f12d41dac52774c83aa0b64eb36d7 | quote: - Updates Every 60 Minutes
  - [2] 2026-11-02: the history endpoint starts on Pro | capture: sha256:cfd21d2538a9d8bbc140b2fc7aa3560526a8aaa2f2e8fdc2e292e802d3426597 | quote: It's only available to users on our Pro, Business or Volume plans.
  - [7] 2026-11-02: the standard request is a GET with the key in the path | capture: sha256:e1226b95a930ba7a0790f08e5cd15a8a493aad5e52f1a332babd6886cf59402a | quote: GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD
- sources:
  - [1] https://www.exchangerate-api.com/
  - [2] https://www.exchangerate-api.com/docs/historical-data-requests
  - [3] https://www.exchangerate-api.com/docs/free
  - [4] https://app.exchangerate-api.com/sign-up
  - [5] https://www.exchangerate-api.com/terms
  - [6] https://www.exchangerate-api.com/docs/overview
  - [7] https://www.exchangerate-api.com/docs/standard-requests

## ExchangeRate-API (open access endpoint)

- `data-apis/exchangerate-api-open` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category currency exchange rate API, keyless open access | tier Open API (no key)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:02:00.000Z (live) | stale on 2026-12-04
- url https://www.exchangerate-api.com/docs/free
- disagrees on identity_kind: `data-apis/exchangerate-api` says email, `data-apis/exchangerate-api-open` says anonymous
- free tier: Open access API with no key: GET https://open.er-api.com/v6/latest/USD, rates updated once per day, rate limited per IP address. | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: The page names no request count and no per-minute number. Requesting once every 24 hours needs no further reading, and one request an hour per server never meets the limit. A rate limited IP address receives HTTP 429 for 20 minutes.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the per-IP rate limit bounds what a caller can pull | metered: no | source: [1]
- identity: anonymous | detail: No key and no account.
- interface: rest
- limits:
  - per-ip-shaping (binding): a rate limit per IP address with no published number; a limited address receives HTTP 429 for 20 minutes [1]
- limits note: Update rate: once per day. Bulk path: none; the page asks to cache the daily table.
- binding note: The only limit is the per-IP shaping with no published threshold; one request an hour never meets it.
- interface detail: GET https://open.er-api.com/v6/latest/USD returns JSON with all supported currencies against the base
- endpoint: part of the free tier
- tooling: curl or any HTTP client
- composes with: A daily table of all currencies with no sign-up; cache it for 24 hours. Pair this with data-apis/exchangerate-api when a key is acceptable.
- reliability: A rate limited IP address receives HTTP 429 and is let through again after 20 minutes.
- notes: Free requests: no count, no key. Rate limit: per IP address, no number published. re-distribution is not allowed. Bulk path: none.
- evidence note: Limits and license are quoted from the open access docs page. One keyless GET answered HTTP 200 with a success body; the rate threshold was not measured.
- extras:
  - bulk_path: none; one daily table of all currencies per request
  - free_requests: no count; per-IP rate limit, number not published
- evidence:
  - [1] 2026-11-02: the open API needs no key | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: - No API Key
  - [1] 2026-11-02:  | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731
  - [1] 2026-11-02: the open API updates once per day | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: Updates Once Per Day
  - [1] 2026-11-02: one request an hour never meets the rate limit | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: If you can't keep a cached response for that long, you could still request once every hour and never get rate limited.
  - [1] 2026-11-02: a limited IP address gets 429 for 20 minutes | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: Rate limited IP's will receive HTTP code 429 responses. After 20 minutes the rate limit will finish and new requests will be allowed through.
  - [1] 2026-11-02: re-distribution is not | capture: sha256:69f1aae1c425c41498f1c91b334bc951cde537ebc28355020b7f502d45987731 | quote: You're welcome to cache the data we respond with and to use it for either personal or commercial currency conversion purposes. You are, however, not allowed to re-distribute it.
  - probe:https://open.er-api.com/v6/latest/USD 2026-11-03: a keyless GET of the open endpoint answered HTTP 200 | capture: sha256:245474e71237a67cd9cd971635febc81b2d3713c2b8f8cdf10cbd9519b37de6f | quote: "status": 200
  - probe:https://open.er-api.com/v6/latest/USD 2026-11-03: the keyless answer body reports success | capture: sha256:92ac914e7c91e6503439c15b805a55b293e5e257985213b177b5b299caa10a92 | quote: "result":"success"
- sources:
  - [1] https://www.exchangerate-api.com/docs/free
