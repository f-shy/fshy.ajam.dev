# Weatherbit

> weatherbit.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/weatherbit/ | JSON https://fshy.ajam.dev/api/v1/entity/weatherbit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Weatherbit

- `data-apis/weatherbit` | qualifies-with-caveat | evidence documented | binding request-rate | category weather forecast API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://www.weatherbit.io/pricing
- free tier: Free plan, USD 0 a month: 50 requests a day at up to 1 request a second, current weather and 7-day daily forecasts, 1 API key; no hourly, minutely or historical data. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The daily cap resets at 00:00 UTC and answers HTTP 429; X-RateLimit-Limit, X-RateLimit-Remaining and X-RateLimit-Reset headers and a usage endpoint report the count. Bulk path: none on Free; Plus and Business add 5 and 30 years of history. Local storage of API data is stated for paid subscriptions. A free account with no login for 15 months is disabled.
- per-object cap: not applicable
- retention: not applicable: the unit is a request | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: The sign-up page offers Google or GitHub sign-in, or a form with username, password, repeated password and email, with no card or phone field; whether a card is asked after sign-up for the Free plan is unverified (the pricing page says no card for the 21 day Business trial).
- interface: rest
- limits:
  - request-rate (binding): 50 requests a day on Free, reset at 00:00 UTC [1]
  - request-rate (binding): 1 request a second on Free [1]
- binding note: 50 requests a day is met long before 1 request a second.
- interface detail: REST over HTTPS at api.weatherbit.io/v2.0 with the key in the key query parameter; JSON answers
- endpoint: https://api.weatherbit.io/v2.0/current
- tooling: any HTTP client
- composes with: A small keyed current-weather and 7-day forecast source; 50 requests a day covers a few locations polled every few hours.
- reliability: 95% uptime is listed for Free; the daily cap answers HTTP 429 until 00:00 UTC, and an account unused for 15 months is disabled.
- notes: Bulk path: none on Free.
- evidence note: Plan limits and the sign-up form are read from first-party pages; a call with no key answered HTTP 403, so a keyed call was not exercised.
- evidence:
  - [1] 2026-11-02: the Free plan is USD 0 a month | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Price | $0/mo | $/mo | $/mo | $/mo | Starting at $/mo |
  - [1] 2026-11-02: the Free plan allows 50 requests a day | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Requests per day | 50 | 25,000 | 250,000 | 2 M | > 2 M |
  - [1] 2026-11-02: the Free plan allows 1 request a second and 0 historical | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Requests per second / Requests per second (Historical) | 1 / 0 | 25 / 0 | 50 / 25 | 150 / 50 | Custom |
  - [1] 2026-11-02: the Free plan has 7-day daily forecasts | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Daily forecasts | 7 days | 16 days | 16 days | 16 days | 16 days |
  - [1] 2026-11-02: the Free plan has no historical data | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Historical data***** | | | 5 years | 30 years | 30 years |
  - [1] 2026-11-02: one API key on Free | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Account API Keys (Max) | 1 | 1 | 1 | 10 | >10 |
  - [1] 2026-11-02: 95% uptime on Free | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: | Uptime | 95% | 99.5% | 99.5% | 99.5% | >99.5% |
  - [1] 2026-11-02: the Business trial needs no card | capture: sha256:34c6a7a483623990d3cafd8ebdc158a8a6826d6deea81feb367fb4a1e55286d9 | quote: Free 21 day trial. No card required.
  - [2] 2026-11-02: an always-free plan exists | capture: sha256:ddeed29bff4f507f06340a564bb0169a3f053944533466659bde74355fe125bf | quote: along with a limited always-free plan for general users and hobbyist projects.
  - [2] 2026-11-02: local storage is stated for paid subscriptions | capture: sha256:ddeed29bff4f507f06340a564bb0169a3f053944533466659bde74355fe125bf | quote: Local storage is allowed with an active paid API subscription, including storage with cloud providers.
  - [3] 2026-11-02: daily cap answers 429 until 00:00 UTC | capture: sha256:7d586702643f9ac075e650445d1e835f98583726c9a98d1e187efb1ceea44a17 | quote: When you exceed a daily limit (requests per day) the API will return an HTTP 429 error until the rate limit resets at 00 UTC.
  - [4] 2026-11-02: quota reset time | capture: sha256:6e9eae65321e5bf57f98311745ad707e7f11140e773b2f309af34842334b67b8 | quote: Daily request limits reset at 00:00 UTC.
  - [5] 2026-11-02: an unused free account is disabled after 15 months | capture: sha256:63f98be813abb3384c6eb7bac8cd058cba22cf8ec9f754d8416b1eb400e14f17 | quote: Accounts that are not actively enrolled in a paid subscription, AND have not logged in after 15 months are disabled.
  - [6] 2026-11-02: sign-up offers Google sign-in | capture: sha256:d0764f9f0799c7a81ad888a748b18aa1a5ada0e1a5b4cc7db5527689eea8de5a | quote: [Google](https://www.weatherbit.io/login/ga)
  - [6] 2026-11-02: the form asks for a username, a password and an email | capture: sha256:b510d89bbface07b7b7adce50fa34a19f554671d12f85f6c96ee3a4e5c5e54f6 | quote: *Username: *Password: *Repeat Password: *Email:
  - probe:https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382 2026-11-02: a call with no key answered 403 | capture: sha256:3fd7940866ac890ab73b09dffc7145bbc6961aae0c4811d15621d15d9680030e | quote: {"error":"API key is required."}
  - probe:https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382 2026-11-02: the call answered HTTP 403 | capture: sha256:bb5d09b07cdb4eca134740a87f1eacb7c052988c1df4fb9f80a6da60d80a367a | quote: "status": 403
  - [7] 2026-11-02: listed under Weather in public-apis with apiKey | capture: sha256:1ce4b056b48404fe8a332497495ca5d12ca2b9f5aa4e985e8fd5fb14f90fe164 | quote: | [Weatherbit](https://www.weatherbit.io/api) | Weather | `apiKey` | Yes | Unknown |
- sources:
  - [1] https://www.weatherbit.io/pricing
  - [2] https://www.weatherbit.io/api/requests
  - [3] https://help.weatherbit.io/faq/what-happens-when-i-exceed-a-rate-limit/
  - [4] https://www.weatherbit.io/api/subscription-usage
  - [5] https://www.weatherbit.io/terms
  - [6] https://www.weatherbit.io/account/create
  - [7] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
