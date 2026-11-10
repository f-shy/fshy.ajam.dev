# Twelve Data

> twelvedata.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/twelvedata/ | JSON https://fshy.ajam.dev/api/v1/entity/twelvedata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Twelve Data

- `data-apis/twelve-data` | qualifies-with-caveat | evidence documented | binding request-rate | category market data API (stocks, forex, crypto, ETFs, technical indicators) | tier Basic
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:51.446Z (live) | stale on 2026-12-04
- url https://twelvedata.com/pricing
- free tier: Basic plan USD 0/month: 8 API credits per minute with an 800 per day cap, 8 trial WebSocket credits; real-time US equities, forex and crypto | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: A standard request costs 1 credit per symbol; heavier endpoints weigh more (income_statement is 100 credits per symbol). The daily quota resets to 800 at midnight UTC. Batch requests, technical indicators and a global trial symbol set are on Basic. time_series returns at most 5000 rows per call, and daily intervals hold the complete history since the first trading date for most symbols. The cheapest paid individual plan is Grow at USD 29/month with 55 credits per minute and no daily cap.
- per-object cap: 5000 rows per time_series call (the outputsize maximum) | source: [2]
- retention: not applicable
- egress: not metered in bytes; the 800 credits a day bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The signup form asks for a full name, an email and a password of at least 8 characters, or a Google or Apple sign-in; it has no card field. Card and PayPal payment are named for the paid plans. apikey=demo answered a daily time_series call for AAPL with no signup.
- interface: rest
- limits:
  - request-rate (binding): 8 API credits per minute [1]
  - request-rate (binding): 800 API credits per day, reset at midnight UTC [3]
  - per-object-cap: 5000 rows per time_series call [2]
- limits note: Bulk path: no bulk path; batch requests and outputsize=5000 are the widest pulls a free key has.
- binding note: Over a full day the 800 per day cap binds before the 8 per minute rate does.
- interface detail: GET https://api.twelvedata.com/time_series with symbol, interval and apikey; a WebSocket on trial credits on Basic. Each response carries api-credits-used and api-credits-left headers, and apikey=demo answers for trial symbols.
- endpoint: part of interface detail
- tooling: curl or any HTTP client; official SDKs and spreadsheet integration are on every plan
- composes with: Full daily history in 5000-row pages at 800 credits a day; it pairs with a real-time feed such as the Finnhub free quotes, or with Massive flat files on its paid tiers for a wide universe.
- reliability: A call past the minute's credits answers HTTP 429; Basic covers US markets, with other markets only through trial symbols.
- notes: Credits are a weight, not a request count: a 1-credit time_series call per symbol is the cheap path, and fundamentals at 100 credits per symbol exhaust a day's 800 in 8 symbols.
- evidence note: The plan, the credit weights and the daily reset are documented on the pricing page and the support articles. A demo-key probe returned a daily series; the 800-per-day cut-off needs a free key to measure.
- extras:
  - bulk_path: no bulk path
  - cutoff.http_status: 429
  - cutoff.body: a JSON object with code, message and status keys; the documented 429 message reads: You have run out of API credits for the current minute. 1000 API credits were used, with the current limit being 987. Wait for the next minute or consider upgrading your plan at https://twelvedata.com/pricing; the message for the 800-per-day cap is unverified: behind a sign-up
  - cutoff.reset: per-minute credits are restored at the start of each new minute; the Basic daily quota of 800 resets at midnight UTC (00:00:00)
- evidence:
  - [1] 2026-10-30: the Basic plan allows 8 API credits per minute and 800 a day | capture: sha256:205d3546d38f2d0c72baa01d7e2f5aa13be32d08433968ac117c5d48a5e24dd4 | quote: API requests: 8 (800 a day)
  - [4] 2026-10-30: Basic is USD 0 with 8 credits per minute, an 800 per day cap, 8 trial WebSocket credits and US markets | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: | Basic | $0/mo | 8 (800/day cap) | 8 (trial) | US | Real-time US equities, forex, crypto |
  - [4] 2026-10-30:  | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: - Basic (Free): 800 API requests/day, 8 trial WS credits, real-time US equities/forex/crypto, technical indicators, spreadsheets, batch requests, global trial symbols.
  - [4] 2026-10-30: the cheapest paid individual plan is USD 29 a month with 55 credits per minute and no daily cap | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: | Grow | $29/mo | 55 | 8 (trial) | 20+ | Real-time US stocks, fundamentals, no daily cap |
  - [4] 2026-10-30:  | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: For individuals only — personal, internal,.
  - [4] 2026-10-30: every plan includes REST, WebSocket, SDKs and spreadsheet integration | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: All plans include: REST and WebSocket APIs, official SDKs, technical indicators, batch requests, spreadsheets integration, reference data, and access to a global trial symbol set.
  - [1] 2026-10-30: income_statement weighs 100 credits per symbol | capture: sha256:205d3546d38f2d0c72baa01d7e2f5aa13be32d08433968ac117c5d48a5e24dd4 | quote: 2. `/income_statement` for the same three symbols: 100 credits × 3 symbols = 300 credits.
  - [1] 2026-10-30: card and PayPal are the payment methods for paid plans | capture: sha256:205d3546d38f2d0c72baa01d7e2f5aa13be32d08433968ac117c5d48a5e24dd4 | quote: We accept PayPal and all major credit cards (including Visa, Mastercard, Discover, American Express and UnionPay.)
  - [3] 2026-10-30: the Basic daily quota resets to 800 at midnight UTC | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: The same principle applies to daily limits on the Basic plan, where the quota resets to 800 at midnight UTC (00:00:00).
  - [3] 2026-10-30: a call past the credit limit answers HTTP 429 | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: If you run out of API credits, a 429 error code will notify you that the API credits limit has been reached.
  - [3] 2026-10-30: each response carries the credits used and left | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: Each API request returns `api-credits-used` and `api-credits-left` in response headers.
  - [2] 2026-10-30: a time_series call returns at most 5000 rows | capture: sha256:4855d8a0670fcaabd16e8142563338338124bf48023c3a3c6f0042fe2d4755d1 | quote: Specify the number of records to be returned with the `outputsize` parameter. This is the simplest and the most efficient approach; however, the maximum value to be set is 5000.
  - [2] 2026-10-30: daily intervals hold the complete history since the first trading date for most symbols | capture: sha256:4855d8a0670fcaabd16e8142563338338124bf48023c3a3c6f0042fe2d4755d1 | quote: Daily intervals include `1day`, `1week`, and `1month` and contain data for the complete history since the first trading date for most symbols.
  - [5] 2026-10-30: the demo key answers for trial symbols | capture: sha256:186d1bb8ad4aef8d424d9f258999dc4792f5f6e3274e55a0e0dcd5bf68750404 | quote: In most cases `apikey=demo` parameter will be sufficient for trial symbols.
  - [6] 2026-10-30: the signup form asks for a full name; the same form asks for an email and a password and has no card field | capture: sha256:54ec0f70e37f5fbd4cfc7cc4c38147964f0f684ac69031cacf4bb0f7bf79644c | quote: Full name<sup>\*</sup>
  - [6] 2026-10-30: the signup password has at least 8 characters | capture: sha256:54ec0f70e37f5fbd4cfc7cc4c38147964f0f684ac69031cacf4bb0f7bf79644c | quote: Password<sup>\*</sup> Mimimum 8 characters
  - [6] 2026-10-30: Google sign-in is offered at signup; the same page offers Apple sign-in | capture: sha256:54ec0f70e37f5fbd4cfc7cc4c38147964f0f684ac69031cacf4bb0f7bf79644c | quote: [Sign up with Google](https://twelvedata.com/auth/google?action=register)
  - [7] 2026-10-30:  | capture: sha256:f5657237950473f8af5327943ab39c4fbda2266eb894f7b3af5931133876cefb
  - [7] 2026-10-30: stored data is deleted within 30 days of termination | capture: sha256:f5657237950473f8af5327943ab39c4fbda2266eb894f7b3af5931133876cefb | quote: - (a) All Data must be deleted within 30 days
  - probe:https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&outputsize=5&apikey=demo 2026-10-30: the time_series endpoint answered HTTP 200 to the demo key | capture: sha256:bd463b24163ed9440fdaf72364dfa612d7e1667f7598ea4fb6fd8f6ccafe6fc2 | quote: "status": 200
  - probe:https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&outputsize=5&apikey=demo 2026-10-30: the demo key returned a daily series for AAPL | capture: sha256:cfec03ded427f6e8dfda6a2501da2496985fcfdbd0eae77a47396cbb9d091386 | quote: "symbol":"AAPL","interval":"1day"
  - [3] 2026-11-02: running out of API credits answers HTTP 429 | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: If you run out of API credits, a 429 error code will notify you that the API credits limit has been reached.
  - [8] 2026-11-02: the error table lists 429 Too Many Requests for a key that reached its request limit | capture: sha256:3c41649934105bfda1bbb933bc08fe8c6e296beae725ac322a29547e04fab11a | quote: | 429 | Too Many Requests | API request limit reached for your key. | Wait briefly or upgrade your plan [here](https://twelvedata.com/pricing). |
  - [9] 2026-11-02: the OpenAPI spec gives this as the example message of the 429 error body, whose code example is 429 | capture: sha256:fb7330d8aac07b38750040240280ccd034f3e59b7bcf5ccf7df6e727474a1c72 | quote: You have run out of API credits for the current minute. 1000 API credits were used, with the current limit being 987. Wait for the next minute or consider upgrading your plan at https://twelvedata.com/pricing
  - [8] 2026-11-02: every error, the 429 included, is a JSON object with code, message and status keys | capture: sha256:3c41649934105bfda1bbb933bc08fe8c6e296beae725ac322a29547e04fab11a | quote: Twelve Data API employs a standardized error response format, delivering a JSON object with `code`, `message`, and `status` keys for clear and consistent error communication.
  - [10] 2026-11-02: a client log shows code 429 with this message for a key whose per-minute limit was 8 credits, the Basic plan's rate | capture: sha256:740e33ffc2eee85417ad15fa48193a9a921d340fe91e78a04eb55eb822808522 | quote: API error (code: 429): You have run out of API credits for the current minute. 38 API credits were used, with the current limit being 8. Wait for the next minute or consider switching to a higher tier plan at https://twelvedata.com/pricing
  - [3] 2026-11-02: the Basic daily quota resets to 800 at midnight UTC | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: The same principle applies to daily limits on the Basic plan, where the quota resets to 800 at midnight UTC (00:00:00).
  - [3] 2026-11-02: the per-minute credit quota is restored at the start of each new minute | capture: sha256:82bf4dbb5db5d1f8e76d33848304a2c146a7681f898540c6b87764c7f7540c20 | quote: Your full API credit quota is restored at the start of each new minute.
  - [4] 2026-11-02: Basic is USD 0 with 8 credits per minute, an 800 per day cap and US markets | capture: sha256:7bb05e09eb5575f76cf5ed4a81a5a32780614c00d0fcd6ba53a39612ca8eca6f | quote: | Basic | $0/mo | 8 (800/day cap) | 8 (trial) | US | Real-time US equities, forex, crypto |
- sources:
  - [1] https://twelvedata.com/pricing
  - [2] https://support.twelvedata.com/en/articles/5656039-how-to-get-historical-prices
  - [3] https://support.twelvedata.com/en/articles/5615854-credits
  - [4] https://twelvedata.com/pricing.md
  - [5] https://support.twelvedata.com/en/articles/5335783-trial
  - [6] https://twelvedata.com/register
  - [7] https://twelvedata.com/terms
  - [8] https://twelvedata.com/docs/introduction/errors
  - [9] https://api.twelvedata.com/doc/swagger/openapi.json
  - [10] https://github.com/we-promise/sure/issues/194
