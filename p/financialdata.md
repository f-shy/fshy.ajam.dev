# Financial Data

> financialdata.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/financialdata/ | JSON https://fshy.ajam.dev/api/v1/entity/financialdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Financial Data

- `data-apis/financial-data` | qualifies-with-caveat | evidence documented | binding request-rate | category market data API (stock, OTC and commodity prices, symbol lists, fundamentals, insider and institutional trading) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:43.773Z (live) | stale on 2026-12-03
- url https://financialdata.net/pricing
- free tier: Free plan USD 0/month: up to 300 requests a day, REST API and Python SDK, symbol lists and daily prices for stocks, commodities and OTC securities. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The documentation labels nine endpoints as Free: the stock, international stock, ETF, commodity and OTC symbol lists, stock prices, commodity prices, OTC prices and OTC volume. Quotes, intraday prices, fundamentals, news, calendars, insider and institutional data are labelled Standard or Premium. Prices return at most 300 records a call and symbol lists 500, paged with the offset parameter; stock prices cover more than 10 years of daily history. The next plan up is Standard at USD 29 a month with 10 requests per second.
- per-object cap: 300 records per call for stock, commodity and OTC prices; 500 records per call for symbol lists | source: [2] | note: Further records are fetched with the offset parameter.
- retention: not applicable: a query API with no stored objects; the stock prices endpoint serves more than 10 years of daily history | source: [2]
- egress: not metered in bytes; the 300 requests a day bound what a free key can pull | metered: no | source: [2]
- identity: email | detail: The sign-up form takes a first name, a last name, an email, a password and a terms checkbox, with a Cloudflare Turnstile check; it has no card or phone field. Payment methods named for paid plans are cards, PayPal, Google Pay, Apple Pay and Link.
- interface: rest
- limits:
  - request-rate (binding): up to 300 requests a day on the Free plan [2]
  - per-object-cap: 300 records per call for prices; 500 records per call for symbol lists [2]
- limits note: Plan gating: only the nine endpoints labelled Free answer a free key; the rest need Standard or Premium. Bulk path: none on Free; the offset parameter pages 300 price records per call.
- binding note: 300 requests a day is the only rate cap stated for the Free plan, and each price call returns at most 300 records.
- interface detail: GET https://financialdata.net/api/v1/{endpoint} with the key in the key query parameter; format=json (the default) or format=csv. An MCP server exists but is limited to the Professional and Enterprise plans.
- endpoint: https://financialdata.net/api/v1/stock-prices
- tooling: any HTTP client; an official Python SDK (fdnpy) is published on GitHub
- composes with: Daily price history and symbol lists in 300-record pages; fundamentals, quotes and filings are not on the Free plan, so a free stack pairs it with a filings or fundamentals source such as Finnhub or Financial Modeling Prep.
- reliability: A call with no key answered HTTP 401 with the message Invalid API key.
- notes: The Free plan reaches symbol lists, daily prices and OTC volume only; everything else the documentation lists needs Standard or Premium.
- evidence note: The plan, quota, record caps and endpoint labels are read from the first-party pricing and documentation pages, and a keyless call answered HTTP 401. A free key was not exercised, so the answer past 300 requests a day is unverified: behind a sign-up.
- evidence:
  - [2] 2026-11-02: the Free subscription includes up to 300 requests per day | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: Free subscriptions include up to 300 requests per day.
  - [2] 2026-11-02: Standard is limited to 10 requests per second and Premium and Professional to 30 | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: Standard subscriptions are limited to 10 requests per second, while Premium and Professional subscriptions to 30 requests per second.
  - [1] 2026-11-02: the Free plan costs USD 0 a month | capture: sha256:ed003d118bd17008f83fcf685f61e98fa36384d008594c87e66011b383bfd6e8 | quote: <h6 class="title name fw-bold text-uppercase mb-4">Free</h6><div class="d-flex mb-4"><span class="h4 mb-0 mt-1 mt-lg-2">$</span><span class="price h1 mb-0">0</span><span class="h4 align-self-end mb-1">/month</span></div>
  - [1] 2026-11-02: the Free plan lists 300 requests a day with the REST API and Python SDK | capture: sha256:ed003d118bd17008f83fcf685f61e98fa36384d008594c87e66011b383bfd6e8 | quote: 300 Requests / Day</li><li class="h6 text-muted mb-0"><span class="icon h5 me-2"><i class="uil uil-check-circle align-middle"></i></span>REST API & Python SDK</li>
  - [1] 2026-11-02: the next plan up, Standard, costs USD 29 a month | capture: sha256:ed003d118bd17008f83fcf685f61e98fa36384d008594c87e66011b383bfd6e8 | quote: <h6 class="title name fw-bold text-uppercase mb-4">Standard</h6><div class="d-flex mb-4"><span class="h4 mb-0 mt-1 mt-lg-2">$</span><span class="price h1 mb-0">29</span><span class="h4 align-self-end mb-1">/month</span></div>
  - [2] 2026-11-02: stock prices are a Free endpoint with more than 10 years of daily history and 300 records per call | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: The API endpoint provides more than 10 years of daily historical stock prices and volumes. The data covers several thousand US and international companies. There is a limit of 300 records per API call.
  - [2] 2026-11-02: the Stock Prices endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Stock PricesFree subscription
  - [2] 2026-11-02: the Commodity Prices endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Commodity PricesFree subscription
  - [2] 2026-11-02: the Otc Prices endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Otc PricesFree subscription
  - [2] 2026-11-02: the Stock Symbols endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Stock SymbolsFree subscription
  - [2] 2026-11-02: symbol lists return at most 500 records per call | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: There is a limit of 500 records per API call.
  - [2] 2026-11-02: every request carries the key in the key query parameter | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: When making requests, ensure that each URL ends with ?key=API_KEY.
  - [2] 2026-11-02: responses are JSON or CSV, JSON by default | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: (Optional) The format of the returned data, either JSON or CSV. Defaults to JSON.
  - [2] 2026-11-02: an official Python SDK is published on GitHub | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: a [Python SDK](https://github.com/financialdatanet/fdnpy) (available on GitHub)
  - [3] 2026-11-02: the MCP server is limited to the Professional and Enterprise plans | capture: sha256:e7e1df4bc6c65c5625ba3d5f7b6273e8bfd62f7f8fefe81bc8800ae931779a53 | quote: *Available exclusively to Professional & Enterprise subscribers
  - [4] 2026-11-02: records past the per-call limit are fetched with the offset parameter | capture: sha256:dd08aae4eb0ffecf4e8f926674bada5fd61ef3aa0c41cb4d23bb331ee36c2f7b | quote: If the API endpoint specifies a limit on records to be retrieved, then you need to use the offset parameter.
  - [4] 2026-11-02: payment methods for paid plans are cards, PayPal, Google Pay, Apple Pay and Link | capture: sha256:dd08aae4eb0ffecf4e8f926674bada5fd61ef3aa0c41cb4d23bb331ee36c2f7b | quote: Credit and debit cards, PayPal, Google Pay, Apple Pay, Link.
  - [5] 2026-11-02: the sign-up form requires an email address | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: <input type="email" class="form-control ps-5" placeholder="Email" name="email" required="" value="">
  - [5] 2026-11-02: the sign-up form requires a first name | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: <label class="form-label">First Name <span class="text-danger">*</span></label>
  - [5] 2026-11-02: the sign-up form requires a last name | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: <label class="form-label">Last Name <span class="text-danger">*</span></label>
  - [5] 2026-11-02: the sign-up form requires a password | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: <label class="form-label">Password <span class="text-danger">*</span></label>
  - [5] 2026-11-02: the sign-up form carries a required terms checkbox | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: I Accept <a href="/terms-of-service" class="text-primary">Terms And Condition</a>
  - [5] 2026-11-02: the sign-up form carries a Cloudflare Turnstile widget | capture: sha256:25f1aa23e7ab461a20b6d97af1f4e853cbbd8971827a7b191f85b7ab5ea388a4 | quote: <div class="cf-turnstile" data-sitekey="0x4AAAAAAAusX2WGFLXRUhKT"></div>
  - [2] 2026-11-02: the International Stock Symbols endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### International Stock SymbolsFree subscription
  - [2] 2026-11-02: the Etf Symbols endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Etf SymbolsFree subscription
  - [2] 2026-11-02: the Commodity Symbols endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Commodity SymbolsFree subscription
  - [2] 2026-11-02: the Otc Symbols endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Otc SymbolsFree subscription
  - [2] 2026-11-02: the Otc Volume endpoint is labelled Free | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Otc VolumeFree subscription
  - [2] 2026-11-02: the Stock Quotes endpoint is labelled Premium | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Stock QuotesPremium subscription
  - [2] 2026-11-02: the Minute Prices endpoint is labelled Standard | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Minute PricesStandard subscription
  - [2] 2026-11-02: the Income Statements endpoint is labelled Standard | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Income StatementsStandard subscription
  - [2] 2026-11-02: the Latest News endpoint is labelled Premium | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Latest NewsPremium subscription
  - [2] 2026-11-02: the Earnings Calendar endpoint is labelled Premium | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Earnings CalendarPremium subscription
  - [2] 2026-11-02: the Insider Transactions endpoint is labelled Premium | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Insider TransactionsPremium subscription
  - [2] 2026-11-02: the Institutional Holdings endpoint is labelled Premium | capture: sha256:0a98a92466048038cc4c19f8151c907ebe6906fff9b82e402c6933d81e81928b | quote: #### Institutional HoldingsPremium subscription
  - probe:https://financialdata.net/api/v1/stock-symbols 2026-11-02: a keyless call to the API answers HTTP 401 | capture: sha256:12e4ecac38d8efcd03b79302587b7b0cd6800200e3aadbc0df3762022df23dad | quote: "status": 401
  - probe:https://financialdata.net/api/v1/stock-symbols 2026-11-02: the keyless 401 body names an invalid API key | capture: sha256:48e80351efa5107d5db16d4c39d85d5a3abb86fedf66c017be3a92935f3c72e0 | quote: "message": "Invalid API key"
- sources:
  - [1] https://financialdata.net/pricing
  - [2] https://financialdata.net/documentation
  - [3] https://financialdata.net/mcp-server
  - [4] https://financialdata.net/faq
  - [5] https://financialdata.net/sign-up
