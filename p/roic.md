# ROIC.ai

> roic.ai | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roic/ | JSON https://fshy.ajam.dev/api/v1/entity/roic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ROIC.ai

- `data-apis/roic-ai` | qualifies-with-caveat | evidence documented | binding request-rate | category market and fundamentals data API (financial statements, ratios, valuation, stock prices, earnings call transcripts) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:43.773Z (live) | stale on 2026-12-03
- url https://www.roic.ai/pricing
- free tier: Free plan USD 0/month: 5 requests per minute and 2 years of history, with every endpoint and all public companies included; plans differ only by rate limit and history depth. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: A request for history beyond 2 years answers HTTP 403 naming the minimum plan that covers it, and a request over the minute limit answers HTTP 429 with Retry-After and X-RateLimit headers. The pricing comparison table lists batch stock prices and the earnings calendar as not included on Free, while the authentication page and the changelog of 4 June 2026 say every endpoint is available; most per-endpoint pages still carry the line Free tier: AAPL available on free tier, and the ticker list page says Free tier: Premium only. The next plan up is Individual at USD 24 a month billed annually, with 300 requests a minute and 5 years of history.
- per-object cap: unverified: no per-response cap is stated on the pages read; period endpoints return 10 periods by default and take a limit parameter | source: [2]
- retention: 2 years of history on the Free plan; a request for older data answers HTTP 403 | source: [3] | note: A query API with no stored objects.
- egress: not metered in bytes; the 5 requests per minute bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The sign-up page takes an email and a password, or Google sign-in; the quickstart says the free tier needs no credit card.
- interface: rest
- limits:
  - request-rate (binding): 5 requests per minute on the Free plan; over it the API answers HTTP 429 [3]
- limits note: History depth: 2 years on Free, and a request beyond it answers HTTP 403. Bulk path: none on Free; bulk downloads are listed for Professional and Enterprise.
- binding note: 5 requests a minute is the only rate cap stated for the Free plan; the 2-year history depth bounds each series.
- interface detail: GET https://api.roic.ai/v2/{endpoint} with the key in the apikey query parameter; JSON by default or tab-separated values with format=excel. An MCP server at https://mcp.roic.ai/mcp exposes the same data as tools, and two spreadsheet endpoints serve an Excel and Google Sheets add-on.
- endpoint: https://api.roic.ai/v2/company/profile/AAPL
- tooling: any HTTP client; request examples for cURL, Python, JavaScript, Ruby, Go and Google Sheets; an MCP server
- composes with: Worldwide fundamentals, ratios, prices and earnings call transcripts for the last 2 years at 5 requests a minute, with no daily or monthly count stated; deeper history, higher rates and bulk downloads are paid, so a free stack pairs it with a quote feed such as Finnhub or Alpha Vantage.
- reliability: Over the minute limit the API answers HTTP 429 with Retry-After and X-RateLimit headers; a call with no key answered HTTP 401 Invalid or missing API key.
- notes: Every endpoint and all public companies are included on Free per the authentication page; plans differ only by rate limit and history depth.
- evidence note: The Free plan limits are read from the first-party authentication page, the changelog and the pricing page, and a keyless call answered HTTP 401. The pricing table and the per-endpoint pages disagree with the authentication page on which endpoints the Free plan reaches, and a free key was not exercised, so that point is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-02: the Free plan allows 5 requests per minute against 300 on Individual | capture: sha256:38143ded010f92900fccdb7e6b48cd201a6d08de461a52e813039df8fea7255d | quote: | Requests / minute | 5 | 300 | Unlimited | Unlimited |
  - [1] 2026-11-02: the Free plan reaches 2 years of history against 5 years on Individual | capture: sha256:38143ded010f92900fccdb7e6b48cd201a6d08de461a52e813039df8fea7255d | quote: | Historical data | 2 years | 5 years | All Available Years | All Available Years |
  - [1] 2026-11-02: market coverage is worldwide on every plan | capture: sha256:38143ded010f92900fccdb7e6b48cd201a6d08de461a52e813039df8fea7255d | quote: | Market coverage | Worldwide | Worldwide | Worldwide | Worldwide |
  - [1] 2026-11-02: the pricing table lists batch stock prices as not included on Free | capture: sha256:38143ded010f92900fccdb7e6b48cd201a6d08de461a52e813039df8fea7255d | quote: | Batch stock prices[All Latest Quotes](https://www.roic.ai/api/docs/stock-prices/latest-list) | No | Yes | Yes | Yes |
  - [1] 2026-11-02: the pricing table lists the earnings calendar as not included on Free | capture: sha256:38143ded010f92900fccdb7e6b48cd201a6d08de461a52e813039df8fea7255d | quote: | Calendar[Earnings Calendar](https://www.roic.ai/api/docs/calendar/earnings) | No | No | All available | All available |
  - [1] 2026-11-02: the Free plan is USD 0 a month | capture: sha256:b44da521359082ce4c90728964958545cf13d5e4cd2648d2c43b7e66fd7d26e6 | quote: Free to grow with us using the essentials</p><p class="mt-6 flex items-baseline gap-x-1"><span class="text-4xl font-bold tracking-tight">$0</span><span class="text-muted-foreground text-sm leading-6 font-semibold">/month</span></p>
  - [1] 2026-11-02: the next plan up, Individual, is USD 24 a month billed annually | capture: sha256:b44da521359082ce4c90728964958545cf13d5e4cd2648d2c43b7e66fd7d26e6 | quote: Invest with Confidence and Ease</p><p class="mt-6 flex items-baseline gap-x-1"><span class="text-4xl font-bold tracking-tight">$24</span><span class="text-muted-foreground text-sm leading-6 font-semibold">/month</span></p><p class="text-muted-foreground text-sm leading-6">billed annually</p>
  - [3] 2026-11-02: the Free plan is 5 requests per minute and 2 years of history | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: | Free | 5 | 2 years |
  - [3] 2026-11-02: every plan, Free included, reaches every endpoint and all public companies | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: Every plan, including the free tier, has full API access to all public companies and every endpoint.
  - [3] 2026-11-02: exceeding the per-minute limit answers HTTP 429 | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: Exceeding your per-minute limit returns a `429 Too Many Requests` error.
  - [3] 2026-11-02: the 429 answer carries Retry-After and X-RateLimit headers | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: The response carries `Retry-After` (seconds until the window resets) and `X-RateLimit-Limit` / `X-RateLimit-Remaining` / `X-RateLimit-Reset` headers:
  - [3] 2026-11-02: history beyond the plan's depth answers HTTP 403 naming the minimum plan | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: Requesting data older than your plan's history depth returns a `403 Forbidden` naming the minimum plan that covers the range:
  - [3] 2026-11-02: every request carries the key in the apikey query parameter | capture: sha256:ad95296a60f0f657a17c6ba5eba8f296c3617efa94bdac1a65cbc4dbe60c72ec | quote: Every ROIC.ai API request requires an API key. Pass it as the `apikey` query parameter on any endpoint.
  - [4] 2026-11-02: the free tier needs no credit card | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: The free tier needs no credit card.
  - [4] 2026-11-02: the free account takes no credit card | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: [Sign up for ROIC.ai](https://roic.ai/login) — it's free and takes no credit card.
  - [4] 2026-11-02: endpoints are GET requests with an apikey parameter and answer JSON or tab-separated values | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: Every endpoint is a `GET` request authenticated with an `apikey` query parameter. Responses are JSON by default, or TSV with `?format=excel`.
  - [4] 2026-11-02: an MCP server exposes the same data as tools | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: The MCP server exposes the same financial data as tools your assistant calls directly.
  - [4] 2026-11-02: the MCP server URL is mcp.roic.ai | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: https://mcp.roic.ai/mcp
  - [4] 2026-11-02: request examples exist for cURL, Python, JavaScript, Ruby, Go and Google Sheets | capture: sha256:2f17a90cb486c95acc3b04c6dc8ca447dcb12d8e15a97b179edaae1efdfd3a5f | quote: cURLPythonJavaScriptRubyGoGoogle Sheets
  - [5] 2026-11-02: since 4 June 2026 every plan, Free included, has full access to every endpoint | capture: sha256:7a6a314f50e0d51998a2b5dac03458a97219a620193df430dee32dfcb3ecf9a5 | quote: Every plan — including Free — now has full access to all public companies and every endpoint.
  - [5] 2026-11-02: two endpoints power an Excel and Google Sheets add-on | capture: sha256:7a6a314f50e0d51998a2b5dac03458a97219a620193df430dee32dfcb3ecf9a5 | quote: Added two endpoints powering the spreadsheet add-on
  - [2] 2026-11-02: the per-endpoint page still states that AAPL is available on the free tier | capture: sha256:77cc1e6595bbfa35c478e8f9289f0272116ad242b3b5739b02223424ab73d4aa | quote: Free tier: AAPL available on free tier
  - [6] 2026-11-02: the historical prices page states that AAPL is available on the free tier | capture: sha256:1bd1c22df259aaf3768f19ed962f0cdbb500d4fae387cd3e59348a9caeddc364 | quote: Free tier: AAPL available on free tier
  - [7] 2026-11-02: the company profile page states that AAPL is available on the free tier | capture: sha256:9c008e570facf7740667624b03672a6485809dd368d42f354787c02792c0723d | quote: Free tier: AAPL available on free tier
  - [8] 2026-11-02: the ticker list page states that the free tier is premium only | capture: sha256:dc4790aca65d5d4b63f507fc5f257f5c946acc036b9896b402ba9a3a13acff07 | quote: Free tier: Premium only
  - [2] 2026-11-02: period endpoints return 10 periods by default and take a limit parameter | capture: sha256:77cc1e6595bbfa35c478e8f9289f0272116ad242b3b5739b02223424ab73d4aa | quote: - `limit` (number, optional, query) — default: `10` — Maximum number of periods to return.
  - [9] 2026-11-02: the sign-up page takes an email and a password | capture: sha256:f4f8889c542d55a3f37dbd2109baffe04c14df5d9fdc15f97a5f4694b2443835 | quote: Enter your email and password below to create account
  - [9] 2026-11-02: the sign-up page offers Google sign-in | capture: sha256:f4f8889c542d55a3f37dbd2109baffe04c14df5d9fdc15f97a5f4694b2443835 | quote: Or continue with
  - probe:https://api.roic.ai/v2/company/profile/AAPL 2026-11-02: a keyless call to the API answers HTTP 401 | capture: sha256:feb1e825e9fe12dcf63acae64b3cd7bc32ff838139a39be80b734e44d8aae3d4 | quote: "status": 401
  - probe:https://api.roic.ai/v2/company/profile/AAPL 2026-11-02: the keyless 401 body names a missing or invalid API key | capture: sha256:dd9a632ee7090f5de08d9b29df28debc22843a8af256de3dad59192b5ed97525 | quote: {"error":"Invalid or missing API key. Get one at https://roic.ai/account."}
- sources:
  - [1] https://www.roic.ai/pricing
  - [2] https://www.roic.ai/api/v2/docs/valuation/per-share
  - [3] https://www.roic.ai/api/v2/docs/authentication
  - [4] https://www.roic.ai/api/v2/docs/getting-started
  - [5] https://www.roic.ai/api/v2/docs/changelog
  - [6] https://www.roic.ai/api/v2/docs/stock-prices/historical
  - [7] https://www.roic.ai/api/v2/docs/company/profile
  - [8] https://www.roic.ai/api/v2/docs/tickers/list
  - [9] https://www.roic.ai/signup
