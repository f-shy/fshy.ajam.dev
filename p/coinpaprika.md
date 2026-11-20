# Coinpaprika

> coinpaprika.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coinpaprika/ | JSON https://fshy.ajam.dev/api/v1/entity/coinpaprika.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coinpaprika

- `data-apis/coinpaprika` | qualifies | evidence documented | binding request-rate | category crypto market data API (tickers, coins, exchanges, OHLCV) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://coinpaprika.com/api/pricing/
- free tier: Free plan: 20,000 calls a month per IP, 2,000 assets, 1 year of daily prices, no key, no account, no card; 10 requests a second per IP | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The free host is api.coinpaprika.com/v1; paid plans use api-pro.coinpaprika.com with a key. Free updates arrive within 10 minutes; intraday history is hourly for the last 24 hours and OHLCV is the latest full day. The first paid plan is Starter at USD 99 a month for 400,000 calls.
- per-object cap: not stated | source: [1]
- retention: not applicable | note: History: 1 year of daily prices on Free; full history on Pro and above.
- egress: not metered in bytes; the 20,000 calls a month bound what one IP can pull | metered: no | source: [1]
- identity: anonymous | detail: The Free plan needs no key, no account and no card: the pricing page says so and a keyless call answered HTTP 200.
- interface: rest
- limits:
  - request-rate (binding): 20,000 calls a month per IP on the Free plan [1]
  - request-rate (binding): 10 requests a second per IP on every plan [1]
- limits note: Bulk path: none stated on the pricing page; redistribution needs the Enterprise plan. Storage terms: the API terms page captured as an empty shell, so unverified.
- binding note: 20,000 calls a month is spent in about 33 minutes at 10 requests a second, so the monthly count binds first.
- interface detail: GET https://api.coinpaprika.com/v1/... with no key; paid plans send the key as the bare Authorization header value to api-pro.coinpaprika.com
- endpoint: part of interface detail
- tooling: curl or any HTTP client; official Go, PHP, Python, TypeScript, Swift and Kotlin clients exist
- composes with: Keyless crypto prices for a year of daily history; it pairs with a macro source such as FRED when a model mixes asset classes.
- reliability: Past a limit the API answers 429 or 402 with a message naming the limit.
- notes: Keyless with a monthly count per IP. Bulk path: none stated. Storage terms: unverified.
- evidence note: A keyless ticker call answered HTTP 200; the limits are documented on the pricing page, which was reviewed by the vendor on 2026-10-27.
- extras:
  - bulk_path: none stated; redistribution is Enterprise only
  - history_depth: 1 year of daily prices on Free
- evidence:
  - [1] 2026-11-02: Free is 20,000 calls a month per IP with no key, account or card | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: Test it right now. No key, no account, no card.
  - [1] 2026-11-02: Free calls, assets and history | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: 20,000 calls a month per IP - 2,000 assets - 1 year of daily prices
  - [1] 2026-11-02: 10 requests a second per IP on every plan | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: 10 requests a second per IP address, on every plan.
  - [1] 2026-11-02: Free update interval and intraday depth | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: | Updates within | 10 min | 3 min | 3 min | 3 min | 3 min | 1 min |
  - [1] 2026-11-02: the first paid plan is USD 99 a month for 400,000 calls | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: 400,000 calls a month. $0.25 per 1,000 calls at full use.
  - [1] 2026-11-02: hitting a limit answers 429 or 402 | capture: sha256:3c302ceb119aea6bc6d398827ba9e1fc09c68051b7f5ca9d7a01e5f01681a3c8 | quote: The API answers `429` or `402` with a message that names the limit.
  - [2] 2026-11-02: most endpoints work without a key; the free base URL | capture: sha256:30f0fed18468ec55f7d4da7ffb67a5143c574c22b5b096da30e4ca939e756e6d | quote: Most of our API endpoints are available without an API key.
  - probe:https://api.coinpaprika.com/v1/tickers/btc-bitcoin 2026-11-03: a keyless ticker call answered HTTP 200 | capture: sha256:c03d2a9e5bcf3c03d84655245c31349a3c09ed90ce770c287f75f2eeb4ede866 | quote: "status": 200
- sources:
  - [1] https://coinpaprika.com/api/pricing/
  - [2] https://docs.coinpaprika.com/api-reference/rest-api/introduction
