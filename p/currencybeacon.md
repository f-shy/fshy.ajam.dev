# CurrencyBeacon

> currencybeacon.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currencybeacon/ | JSON https://fshy.ajam.dev/api/v1/entity/currencybeacon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CurrencyBeacon (formerly CurrencyScoop)

- `data-apis/currencybeacon` | qualifies-with-caveat | evidence documented | binding request-rate | category currency exchange-rate API (fiat and crypto: latest, historical, conversion, time series) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:43.773Z (live) | stale on 2026-12-03
- url https://currencybeacon.com/pricing
- free tier: Free plan USD 0 per month: 5,000 API requests per month shared by REST and MCP calls, hourly rate updates, latest, historical and conversion endpoints, community support. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: No credit card is needed to start. The Timeseries API and base currency switching are not on Free or Basic, and a request to an endpoint outside the plan answers HTTP 403. Historical rates go back to January 1, 1996. The next plan up is Basic at USD 10 a month with 50,000 requests a month and 15 minute updates. The former name CurrencyScoop: currencyscoop.com and api.currencyscoop.com answer a 301 redirect to the currencybeacon.com hosts.
- per-object cap: unverified: no per-response cap is stated on the pages read | source: [2]
- retention: not applicable: a query API with no stored objects; historical rates go back to January 1, 1996 | source: [2]
- egress: not metered in bytes; the 5,000 requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The register page asks for a first name, a last name, an email, a password of at least 12 characters with uppercase and lowercase letters, a number and a symbol, a confirmation and a terms checkbox, or Log in with Google or GitHub; it states that no credit card is required.
- interface: rest
- limits:
  - request-rate (binding): 5,000 API requests per month on the Free plan, shared by REST and MCP calls [1]
- limits note: Plan gating: Free is hourly updates and the latest, historical and conversion endpoints; the Timeseries API and base currency switching are not on Free or Basic. Bulk path: none; each call is one request.
- binding note: The 5,000 requests a month cap is the only limit stated for the Free plan.
- interface detail: GET https://api.currencybeacon.com/v1/{endpoint} (latest, convert, historical, timeseries, currencies) with the key as an api_key query parameter or as a Bearer token in the Authorization header; JSON answers. An MCP server on the same account shares the request quota.
- endpoint: https://api.currencybeacon.com/v1/latest
- tooling: any HTTP client; code samples for cURL, JavaScript, Python and PHP; an MCP server
- composes with: 5,000 requests a month of hourly fiat and crypto rates with history back to 1996, so a free stack caches the latest rates once an hour and converts locally; UniRateAPI gives a daily quota instead of a monthly one.
- reliability: Past the request volume the API answers HTTP 429; an endpoint outside the plan answers HTTP 403; a call with no key answered HTTP 401 auth failed.
- notes: Formerly CurrencyScoop: the old site and API hosts redirect to currencybeacon.com; Free is 5,000 requests a month at hourly updates.
- evidence note: The plan, quota, update rate and endpoint gating are read from the first-party pricing and documentation pages; a keyless call answered HTTP 401 and the old CurrencyScoop hosts answered a 301 redirect. A free key was not exercised, so the answer past 5,000 requests is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-02: the Free plan is USD 0 a month with 5,000 API requests a month and no credit card to start | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: ### Free Start here Prototype with live and historical endpoints before committing. $0 / month No credit card needed to start API requests / month 5,000
  - [1] 2026-11-02: Free updates rates hourly and REST and MCP calls share the quota | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: Hourly updates REST and MCP calls share this quota.
  - [1] 2026-11-02: Free includes latest, historical and conversion rates | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: - Latest, historical, and conversion rates
  - [1] 2026-11-02: Free comes with community support | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: - Community support
  - [1] 2026-11-02: the next plan up, Basic, is USD 10 a month | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: $10 / month
  - [1] 2026-11-02: Basic includes 50,000 API requests a month | capture: sha256:981383e4445e8bc8ca77b429fbb63e2ab742c08f86cd6244de2209f8ab69739c | quote: API requests / month 50,000
  - [3] 2026-11-02: monthly requests are 5,000 on Free and 50,000 on Basic | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: | Monthly API requests | 5,000 | 50,000 | 500,000 | 2,000,000 |
  - [3] 2026-11-02: Free refreshes hourly and Basic every 15 minutes | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: | Rate refresh | Hourly updates | 15 min updates | 1 min updates | Real-time updates |
  - [3] 2026-11-02: the comparison table lists the Timeseries API as not included on Free and Basic | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: | Timeseries API | — | — | | |
  - [3] 2026-11-02: the comparison table lists base currency switching as not included on Free and Basic | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: | Base currency switching | — | — | | |
  - [3] 2026-11-02: every plan includes REST access and MCP tool calls count as API requests | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: Every plan includes REST API access. MCP is available on the same account, and successful MCP tool calls count as normal API requests.
  - [3] 2026-11-02: the REST endpoints are latest, convert, historical, timeseries and currencies | capture: sha256:2de66420de374cf33d813ceeaff1986e6817c184e5fe8502100194941fb09847 | quote: Call `/latest`, `/convert`, `/historical`, `/timeseries`, and `/currencies` from any backend or app.
  - [2] 2026-11-02: the API covers over 160 currencies and more than 2,000 cryptocurrencies | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: We provide a simple yet powerful RESTful interface for accessing real-time and historical exchange rates for over 160 world currencies and more than 2,000 cryptocurrencies.
  - [2] 2026-11-02: historical rates go back to January 1, 1996 | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: Our database goes back to January 1, 1996.
  - [2] 2026-11-02: authentication is required for all API requests | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: Authentication is required for all API requests.
  - [2] 2026-11-02: the key goes in an api_key query parameter | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: Simply append the `api_key` parameter to any request URL.
  - [2] 2026-11-02: the key may instead go in a Bearer Authorization header | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: Pass the key as a Bearer token in the request header.
  - [2] 2026-11-02: the base URL of the API | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: https://api.currencybeacon.com/v1
  - [2] 2026-11-02: the timeseries endpoint is limited to Startup and Professional plans | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: \*Available on Startup and Professional plans only.
  - [2] 2026-11-02: exceeding the request volume limit answers HTTP 429 | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: | 429 | Too Many Requests | You have exceeded your request volume limit. Please upgrade your plan or slow down your request rate. |
  - [2] 2026-11-02: an endpoint outside the plan answers HTTP 403 | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03
  - [2] 2026-11-02: code samples exist for cURL, JavaScript, Python and PHP | capture: sha256:31aa0e5b8d0556a9fa84aeb264cc792915f2161dba38220ce9afb03688470b03 | quote: cURL JavaScript Python PHP Copy
  - [4] 2026-11-02: the register page offers 5,000 free API requests a month with no credit card | capture: sha256:0322862c8fb34e09bf8aaec2f0f26d989f340fb2c260250d97985163fcd8d0b1 | quote: Start with 5,000 free API requests a month. No credit card required.
  - [4] 2026-11-02: the register form asks for a first name, a last name and an email | capture: sha256:0322862c8fb34e09bf8aaec2f0f26d989f340fb2c260250d97985163fcd8d0b1 | quote: First name Last name Email
  - [4] 2026-11-02: the password needs at least 12 characters with mixed case, a number and a symbol | capture: sha256:0322862c8fb34e09bf8aaec2f0f26d989f340fb2c260250d97985163fcd8d0b1 | quote: Use at least 12 characters with uppercase and lowercase letters, a number, and a symbol.
  - [4] 2026-11-02: the register page offers Google and GitHub sign-in | capture: sha256:0322862c8fb34e09bf8aaec2f0f26d989f340fb2c260250d97985163fcd8d0b1 | quote: [Log in with Google](https://currencybeacon.com/auth/google/redirect) [Log in with GitHub](https://currencybeacon.com/auth/github/redirect)
  - probe:https://currencyscoop.com/ 2026-11-02: currencyscoop.com answers a 301 redirect to currencybeacon.com | capture: sha256:2d360c6a06b3e20815bc60dc27e11981671364473fa4f049bd11e9827593edd1 | quote: "location": "https://currencybeacon.com/"
  - probe:https://api.currencyscoop.com/v1/latest 2026-11-02: api.currencyscoop.com answers a 301 redirect to api.currencybeacon.com | capture: sha256:2f3c4ab2dd1b4ca97e755c6a4039855ee0b816fb20c6a5c8460ad8b9ca47f2ba | quote: "location": "https://api.currencybeacon.com/v1/latest"
  - probe:https://api.currencybeacon.com/v1/latest 2026-11-02: a keyless call to the API answers HTTP 401 | capture: sha256:0d9fe9d566312e227df5040b3fe67fe869f0076825bb48adb8df02bee4716471 | quote: "status": 401
  - probe:https://api.currencybeacon.com/v1/latest 2026-11-02: the keyless 401 body reports an auth failure | capture: sha256:5d1e3f31208a8eb89d592b75ca6644b60b3627da47aa27acba9aa544d5a00fe4 | quote: "error_type":"auth failed"
- sources:
  - [1] https://currencybeacon.com/pricing
  - [2] https://currencybeacon.com/api-documentation
  - [3] https://currencybeacon.com/
  - [4] https://currencybeacon.com/register
