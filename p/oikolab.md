# Oikolab

> oikolab.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oikolab/ | JSON https://fshy.ajam.dev/api/v1/entity/oikolab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Oikolab

- `data-apis/oikolab` | qualifies-with-caveat | evidence documented | binding volume-quota | category weather and climate data API | tier Pay As You Go
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://oikolab.com/
- free tier: Pay As You Go plan with 1,500 data units a month free, then USD 0.01 a unit; a data unit is 1 location x 1 parameter x 1 month; up to 2,500 units per call, historical data from 1940, global forecast models and an air quality forecast; sign-up without credit card. | unit: mixed | metered on: object-count | read on: 2026-11-02 | source: [1] | note: The true unit is a data unit (one location, one parameter, one month of time series, or 1 degree x 1 degree x 1 month for NetCDF), which the unit vocabulary lacks. Ten years of two parameters for ten locations cost 2,400 units. Bulk path: multi-location calls (the Business plan allows 10 locations a call) and JSON, CSV or NetCDF answers; gridded NetCDF is listed under Enterprise. ERA5 history lags by 5 days and recent days are filled from forecasts. Next plan: Business at USD 150 a month with 50,000 units.
- per-object cap: up to 2,500 units per call on Pay As You Go; 5,000 units or 10 locations on Business | source: [1]
- retention: not applicable: the unit is a data unit | source: [1]
- egress: not applicable: answers are metered in data units | metered: no | source: [1]
- identity: email | detail: An account is needed for an API key (the key is on the profile page after login); the pricing page says sign-up needs no credit card; the sign-up is a hosted login page that no reader could render, so its fields are unverified.
- interface: rest
- limits:
  - volume-quota (binding): 1,500 data units a month free on Pay As You Go [1]
  - per-object-cap: 2,500 units per call on Pay As You Go [1]
- binding note: 1,500 free units a month is met before the 2,500 units per call cap.
- interface detail: REST over HTTPS at api.oikolab.com (/weather, /archivedforecast, /airquality, /epw, /datasets, /account) with the key in the api-key header; JSON, CSV or NetCDF answers
- endpoint: https://api.oikolab.com/weather
- tooling: any HTTP client; Python and R examples in the docs
- composes with: A history-heavy source: decades of hourly ERA5 for many locations in one call; the free units cover 125 location-years of one parameter.
- reliability: The most recent 5 days of history are filled from forecasts and overwritten when ERA5 arrives.
- notes: Derived: 1,500 units / 12 months = 125 location-years of one parameter. Bulk path: multi-location calls and NetCDF area requests.
- evidence note: Plan and metering are read from the first-party pricing and docs pages; a call with no key answered HTTP 401, so a keyed call was not exercised.
- evidence:
  - [1] 2026-11-02: 1,500 data units a month are free | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: _done_ Includes 1500 units/month for free
  - [1] 2026-11-02: the Pay As You Go price is USD 0.01 a unit | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: $0.01 / unit
  - [1] 2026-11-02: 2,500 units per call on Pay As You Go | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: _done_ Up to 2500 units per call
  - [1] 2026-11-02: sign-up needs no credit card | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: _done_ Sign-up without credit card
  - [1] 2026-11-02: historical data from 1940 | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: _done_ Historical data from 1940
  - [1] 2026-11-02: the metering definition | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: 1 data unit = 1 location x 1 parameter x 1 month
  - [1] 2026-11-02: the Business plan is USD 150 a month | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: ### $150 / month
  - [1] 2026-11-02: gridded NetCDF is listed under Enterprise | capture: sha256:9567988f69a7379dcdd7d67fcb605acd7935aa672536728b1f4606a5914d98ab | quote: _done_ Gridded Data (NetCDF)
  - [2] 2026-11-02: every request needs an API key | capture: sha256:e024083ee7a961393fbbc621bcf6a022c4668ed78542db7878dc3de10257ee58 | quote: Every request should include your API key in the `api-key` header or part of the url.
  - [2] 2026-11-02: the key is on the profile page after login | capture: sha256:e024083ee7a961393fbbc621bcf6a022c4668ed78542db7878dc3de10257ee58 | quote: You can find your API key on the profile page when you log into your
  - [3] 2026-11-02: archived GFS forecasts for 3 years | capture: sha256:dbd1a546844abe832786ba04a01ce096eee4f5917f17bcf0a39bd61a4c239041 | quote: Up to 3 years of GFS (00Z runs) are archived.
  - [4] 2026-11-02: ERA5 from 1940 with a 5-day delay | capture: sha256:ea670451bb992118b3f7fc42b286c309b6b17d4e26d4d883e9d473f4be3da91e | quote: Data is available from 1940 to present with a 5-day delay.
  - [5] 2026-11-02: JSON, CSV and NetCDF answers | capture: sha256:0963a3222c0ecfc59fb7040b62a22a6e2b7a56a99cd6fca317656e163450ebe5 | quote: downloadable in JSON, CSV or NetCDF format
  - probe:https://api.oikolab.com/weather 2026-11-02: a call with no key answered 401 | capture: sha256:c90468927fb778dd15b9da44a4dfec94fa8544d9746a59183f1bd413f87ac52a | quote: Access denied due to missing subscription key.
  - probe:https://api.oikolab.com/weather 2026-11-02: the call answered HTTP 401 | capture: sha256:5210eae0ebd076961ec936f7170e89ddee7462bde3de5388e99fedaa670c6450 | quote: "status": 401
  - [6] 2026-11-02: listed under Weather in public-apis with apiKey | capture: sha256:1ce4b056b48404fe8a332497495ca5d12ca2b9f5aa4e985e8fd5fb14f90fe164 | quote: | [Oikolab](https://docs.oikolab.com) | 70+ years of global, hourly historical and forecast weather data from NOAA and ECMWF | `apiKey` | Yes | Yes |
- sources:
  - [1] https://oikolab.com/
  - [2] https://docs.oikolab.com/authentication/
  - [3] https://docs.oikolab.com/references/
  - [4] https://docs.oikolab.com/datasets/
  - [5] https://docs.oikolab.com/
  - [6] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
