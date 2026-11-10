# FxRatesAPI

> fxratesapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fxratesapi/ | JSON https://fshy.ajam.dev/api/v1/entity/fxratesapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FxRatesAPI

- `data-apis/fxratesapi` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (fiat and crypto, with history) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://fxratesapi.com/pricing
- free tier: Free plan, USD 0, no card: 1k requests a month and 60 requests an hour, hourly updates, all base currencies. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Standard is USD 10 a month for 10k requests, 10-minute updates, no rate limit, historical data back to 1999 and a conversion endpoint, listed as features added to the free ones. Professional is USD 30 a month for 500k requests and adds time series. The pricing page says 1999 for history and the home page says 1990.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 1k requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The docs say to sign up for an account to get an API key, and the pricing page says no credit card is needed. The form fields are unverified: no sign-up page was found.
- interface: rest
- limits:
  - volume-quota (binding): 1k requests a month on the Free plan [1]
  - request-rate: 60 requests an hour on the Free plan [1]
- limits note: History: the pricing page lists historical data as a Standard feature added to the free ones; whether the Free plan can call the historical endpoint was not readable, because the endpoint list lost its check and cross marks. Bulk path: none on the free plan; time series starts on Professional.
- binding note: 1k requests a month ends first: 60 an hour would spend it in about 17 hours.
- interface detail: GET https://api.fxratesapi.com/latest?api_key=KEY with base, currencies and resolution parameters; JSON, XML or TSV
- endpoint: part of interface detail
- tooling: curl or any HTTP client
- composes with: Hourly rates at 60 requests an hour and 1k a month: a poll every hour would spend 720 of the 1k.
- reliability: The free plan's behaviour past its limits was not read; the pricing page names no rate limit on paid plans.
- notes: Free requests: 1k a month. Rate limit: 60 requests an hour. End users may not store or distribute the data. Bulk path: none on the free plan.
- evidence note: Quota, rate and plan fields are quoted from the first-party pricing page; the sign-up step from the docs. The sign-up form fields and the free plan's history access are unverified. No key was created.
- extras:
  - bulk_path: none on the free plan; time series starts on Professional
  - free_requests: 1k a month, 60 an hour
  - history_depth: back to 1999 on Standard per the pricing page; 1990 per the home page
- evidence:
  - [1] 2026-11-02: the Free plan is 1k requests a month | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: 1k requests/month
  - [1] 2026-11-02: the Free plan is 60 requests an hour | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: 60 requests/hour
  - [1] 2026-11-02: the Free plan updates hourly | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: - Hourly Updates
  - [1] 2026-11-02: the pricing page says no card is needed | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: no credit card needed
  - [1] 2026-11-02: Standard allows 10k requests a month | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: 10k requests/month
  - [1] 2026-11-02: Standard adds historical data back to 1999 | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: Get historical data from the API all the way back to 1999.
  - [1] 2026-11-02: the Standard feature list is the free features plus its own | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: ##### Free features +
  - [1] 2026-11-02: Standard has no rate limits | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: No Rate Limits
  - [2] 2026-11-02: an account on the website gives the API key | capture: sha256:5a906ca80c6538f774135ea298334ee11cb365f850088a3c09d71ad310924118 | quote: Sign up for an account on the FXRatesAPI.com website. This will give you access to your API key
  - [3] 2026-11-02: the home page gives history back to 1990 | capture: sha256:52a2942a408a97a3ab45c739c455a01fbd367568aa327504144c0f162d25f15b | quote: We provide historical exchange rates going back to 1990.
  - [4] 2026-11-02: end users may not store or distribute the data | capture: sha256:bc0d17511188bc253685c47a3ebcd24fc2be0b869bb786925d4612638a40fcad
  - [4] 2026-11-02: the data may not be used or stored after termination | capture: sha256:bc0d17511188bc253685c47a3ebcd24fc2be0b869bb786925d4612638a40fcad | quote: use, store, or access any fxRatesAPI API Data & Services, or the fxRatesAPI API after the termination of this Agreement
  - [1] 2026-11-02: Standard is USD 10 a month | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: #### $10/month
  - [1] 2026-11-02: Professional allows 500k requests a month | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: 500k requests/month
  - [1] 2026-11-02: Professional adds time series data | capture: sha256:4d1d8426b8a891a29b3cd22841cabcb0ab72026eb3defd99531199efcf959d30 | quote: Timeseries Data
  - [5] 2026-11-02: the latest endpoint answers in JSON, XML or TSV | capture: sha256:2db5c12ea0e6de93b4a4485e55209e8072245a77e5bfd42904c4353d73ae331d | quote: You can also choose to get the response in XML or TSV format.
  - [2] 2026-11-02: the key goes in the api_key parameter | capture: sha256:5a906ca80c6538f774135ea298334ee11cb365f850088a3c09d71ad310924118 | quote: https://api.fxratesapi.com/latest?api_key=YOUR_ACCESS_TOKEN
- sources:
  - [1] https://fxratesapi.com/pricing
  - [2] https://fxratesapi.com/docs
  - [3] https://fxratesapi.com/
  - [4] https://fxratesapi.com/legal/terms-conditions
  - [5] https://fxratesapi.com/docs/endpoints/latest-exchange-rates
