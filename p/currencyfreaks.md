# CurrencyFreaks

> currencyfreaks.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currencyfreaks/ | JSON https://fshy.ajam.dev/api/v1/entity/currencyfreaks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CurrencyFreaks

- `data-apis/currencyfreaks` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (166 fiat currencies, 873 cryptocurrencies and 4 metals) | tier Developer (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://currencyfreaks.com/pricing
- free tier: Developer plan, free, no card: 1,000 API calls a month with a daily refresh at 00:00 UTC, USD as the only base currency; no daily or hourly rate limit. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The free key returns latest rates and the symbol endpoints only; historical rates need a paid plan, from Starter at USD 9.99 a month for 15,000 calls. The supported-currencies, currency-symbols and historical-data-limits endpoints need no key. The monthly quota may be spent in one day. At the free limit one email goes out and the API stops serving until the next month.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 1,000 calls a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: Free sign-up with Google or GitHub, or an email; no card. The terms say to sign up with a real company or personal email, that disposable addresses and shared mailboxes are deleted, and that accounts made by automated methods are removed. The sign-up runs on the vendor's APIFreaks platform.
- interface: rest
- limits:
  - volume-quota (binding): 1,000 API calls a month on the Developer plan [1]
  - retention-clamped: latest rates only on the free key; historical rates need a paid plan [2]
- limits note: Rate: no daily or hourly limit on any plan. Bulk path: none on the free key; the time series and fluctuation endpoints need Professional at USD 99.99 a month, and the vendor blog shows a Python loop that writes the series to CSV.
- binding note: The monthly count of 1,000 is the only limit, so it binds; the quota may be spent in one day.
- interface detail: GET https://api.currencyfreaks.com/v2.0/rates/latest?apikey=KEY; JSON, or XML with format=xml
- endpoint: part of interface detail
- tooling: curl or any HTTP client
- composes with: Daily rates for 1,000+ currencies at 1,000 calls a month; one call returns all currencies, so a daily pull uses about 30.
- reliability: At the free limit the API stops serving until the next month; one email notice is sent at 100 percent.
- notes: Free requests: 1,000 a month. Rate limit: none per day or hour. Bulk path: none on the free key.
- evidence note: Quota, refresh, history gate and sign-up fields are read from first-party pricing, docs, FAQ, llms.txt and terms pages. No key was created.
- extras:
  - bulk_path: none on the free key; time series needs Professional
  - free_requests: 1,000 a month
  - history_depth: none on the free key; back to 1984-11-28 on paid plans
- evidence:
  - [1] 2026-11-02: the Developer plan is 1,000 API calls a month | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: - 1,000 API calls/month
  - [1] 2026-11-02: the Developer plan refreshes every 24 hours | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: - 24 hour updates
  - [1] 2026-11-02: the Developer plan has USD as the base currency | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: - USD as base currency
  - [1] 2026-11-02: free start with no card | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: Start free with 1,000 API calls a month, no credit card required, and upgrade as your traffic grows.
  - [1] 2026-11-02: no daily or hourly throttle | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: There is no daily or hourly throttle - only your plan's monthly quota.
  - [1] 2026-11-02: Starter allows 15,000 calls a month | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: - 15K API calls/month
  - [3] 2026-11-02: no daily or hourly rate limits; the quota may be spent in a day | capture: sha256:63bb085ea92cc4f32af7e9c1d64857b603cda672df75dcf2644720d8f5505ce5 | quote: we don't have any daily or hourly rate limits on any of our plans. You can consume all of your monthly/yearly quota in a single day.
  - [3] 2026-11-02: sign-up needs no card | capture: sha256:63bb085ea92cc4f32af7e9c1d64857b603cda672df75dcf2644720d8f5505ce5 | quote: It does not require a credit card.
  - [4] 2026-11-02: the free plan stops at its limit after one notice | capture: sha256:18324c23cf996596d039c9a68f77367502bd22cc10e9d046ca8a030f0637108d | quote: For free plans, we'll notify you once when you reach 100% of your free limit and stop serving you afterwards.
  - [4] 2026-11-02: the free refresh is at 12:00 AM UTC | capture: sha256:18324c23cf996596d039c9a68f77367502bd22cc10e9d046ca8a030f0637108d | quote: Under the free plan, data is refreshed every 24 hours, with updates occurring precisely at 12:00 AM UTC.
  - [4] 2026-11-02: the source currency is fixed on the free plan | capture: sha256:18324c23cf996596d039c9a68f77367502bd22cc10e9d046ca8a030f0637108d | quote: You can change the source currency only in our paid plans.
  - [2] 2026-11-02: history needs a paid plan | capture: sha256:606b49c9f9a18f17572ae8f4b4a2b9c488acc72950aaad428d88f9eaeb164357 | quote: The free Developer key returns latest rates and the symbol endpoints only. Historical Rates needs any paid plan.
  - [2] 2026-11-02: time series and fluctuation need Professional | capture: sha256:606b49c9f9a18f17572ae8f4b4a2b9c488acc72950aaad428d88f9eaeb164357 | quote: Time Series and Fluctuation, the two endpoints that make batch downloading possible, need the Professional plan or above.
  - [5] 2026-11-02: sign-up offers Google and GitHub | capture: sha256:d5e43c803ab4b1399d89398db060c0352f02a0017998381ce105ff970fdc8992 | quote: Sign in with Google or GitHub.
  - [6] 2026-11-02: the sign-up page says free and no card | capture: sha256:f6deb2a5791ade94a33163c661830ab03f6c2d5132b43ddefe75df8c8c6a613a | quote: Free Signup! No credit card required.
  - [7] 2026-11-02: disposable and shared emails are deleted | capture: sha256:98a62255bf16219c3159b43379d95498f3faf96261b58781f86c42c5650faf11 | quote: 4. You must sign up with your real company or personal email. Signups from disposable email addresses, shared mailboxes or any other fraudulent signups will be deleted.
  - [7] 2026-11-02: accounts made by automated methods are removed | capture: sha256:98a62255bf16219c3159b43379d95498f3faf96261b58781f86c42c5650faf11 | quote: 2. You must be a human. Account created by automated methods are not permitted and will be removed.
  - [7] 2026-11-02:  | capture: sha256:98a62255bf16219c3159b43379d95498f3faf96261b58781f86c42c5650faf11
  - [5] 2026-11-02: the coverage is 166 fiat, 873 crypto and 4 metals | capture: sha256:d5e43c803ab4b1399d89398db060c0352f02a0017998381ce105ff970fdc8992 | quote: 166 fiat currencies, 873 cryptocurrencies and 4 precious metals
  - [1] 2026-11-02: Starter is USD 9.99 a month | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: $9.99/month
  - [1] 2026-11-02: Professional is USD 99.99 a month | capture: sha256:96bcc60a844d5e066a58e02f7fd0bc2d8e27037c08a21c8deb105a1d5f85c756 | quote: $99.99/month
  - [5] 2026-11-02: three metadata endpoints need no key | capture: sha256:d5e43c803ab4b1399d89398db060c0352f02a0017998381ce105ff970fdc8992 | quote: Key-free endpoints: `https://api.currencyfreaks.com/v2.0/supported-currencies`, `/currency-symbols` and `/historical-data-limits` work without an API key.
  - [2] 2026-11-02: the vendor blog shows a Python script that writes the series to CSV or Excel | capture: sha256:606b49c9f9a18f17572ae8f4b4a2b9c488acc72950aaad428d88f9eaeb164357 | quote: a short Python script writes each response straight to CSV or Excel.
  - [6] 2026-11-02: the sign-up page is the APIFreaks platform | capture: sha256:f6deb2a5791ade94a33163c661830ab03f6c2d5132b43ddefe75df8c8c6a613a | quote: First-party REST API platform unifying 80+ APIs across diverse niches under one key and one balance.
- sources:
  - [1] https://currencyfreaks.com/pricing
  - [2] https://currencyfreaks.com/blog/Historical-Forex-Data-for-Scalable-Data-Science-Workflows
  - [3] https://currencyfreaks.com/documentation
  - [4] https://currencyfreaks.com/faqs
  - [5] https://currencyfreaks.com/llms.txt
  - [6] https://currencyfreaks.com/signup.md
  - [7] https://currencyfreaks.com/tos
