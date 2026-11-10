# Coinlore

> coinlore.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coinlore/ | JSON https://fshy.ajam.dev/api/v1/entity/coinlore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coinlore

- `data-apis/coinlore` | qualifies | evidence documented | binding request-rate | category crypto market data API (tickers, coin info, exchanges, 365-day OHLCV) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://www.coinlore.com/cryptocurrency-data-api
- free tier: Open API with no registration and no key; no strict rate limit, about one request per second recommended; more than 14992 coins and 300+ exchanges | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: The base is api.coinlore.net/api. Tickers return up to 100 coins a request with a start offset; daily OHLCV covers 365 days per coin. A keyless global-stats call answered HTTP 200.
- per-object cap: 100 coins per tickers request, paged with start | source: [1]
- retention: not applicable | note: OHLCV history is 365 days per coin.
- egress: not metered; no quota is stated | metered: no | source: [1]
- identity: anonymous | detail: No registration and no key: the vendor page says the API requires no registration and a keyless call answered HTTP 200.
- interface: rest
- limits:
  - request-rate (binding): no strict limit; about 1 request per second recommended [1]
  - per-object-cap: 100 coins per tickers request [1]
- limits note: Bulk path: page /api/tickers/ in steps of 100 using info.coins_num. Storage terms: unverified, the terms page answered HTTP 404. History is 365 days of daily OHLCV.
- binding note: Only a soft request rate of about 1 a second is stated, so it is the one ceiling that applies.
- interface detail: GET https://api.coinlore.net/api/global/, /api/tickers/?start=N&limit=100, /api/ticker/?id=ID, /api/coin/ohlcv/?coin=ID and others, JSON, no key
- endpoint: part of interface detail
- tooling: curl or any HTTP client
- composes with: Keyless crypto tickers and a year of daily candles; it pairs with CoinPaprika for a second source and with FRED for macro series.
- reliability: No strict limit is published; the vendor asks for about one request per second.
- notes: Keyless with a soft rate. Bulk path: paged tickers in steps of 100. Storage terms: unverified.
- evidence note: The terms of access are read from the vendor page and a keyless call answered HTTP 200; the soft rate was not stress-tested.
- extras:
  - bulk_path: tickers paged 100 at a time
  - history_depth: 365 days of daily OHLCV per coin
- evidence:
  - [1] 2026-11-02: the API is open and needs no registration | capture: sha256:af2a1a28c67112b1123ef16f57cbc77d4768af1457c70524df72e4b4d991b8d7 | quote: The API is open, requires no registration, and provides real-time crypto market data for more than 14992 coins and 300+ exchanges.
  - [1] 2026-11-02: no key and no strict rate limit, about one request per second | capture: sha256:af2a1a28c67112b1123ef16f57cbc77d4768af1457c70524df72e4b4d991b8d7 | quote: While there is no strict rate limit, we recommend around one request per second for stable and fair usage.
  - [1] 2026-11-02: 365 days of daily OHLCV per coin | capture: sha256:af2a1a28c67112b1123ef16f57cbc77d4768af1457c70524df72e4b4d991b8d7 | quote: Get 365 days of daily OHLCV history for a specific coin
  - [1] 2026-11-02: tickers return at most 100 coins a request and page with start | capture: sha256:af2a1a28c67112b1123ef16f57cbc77d4768af1457c70524df72e4b4d991b8d7 | quote: Number of coins to return. Maximum is
  - probe:https://api.coinlore.net/api/global/ 2026-11-03: a keyless global-stats call answered HTTP 200 | capture: sha256:0821f2c665c2776c46c9af5626c539f3b5dc93d50aa86570c22416c0864e5227 | quote: "status": 200
- sources:
  - [1] https://www.coinlore.com/cryptocurrency-data-api
