# Pirate Weather

> apiable.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apiable/ | JSON https://fshy.ajam.dev/api/v1/entity/apiable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pirate Weather

- `data-apis/pirate-weather` | qualifies-with-caveat | evidence documented | binding request-rate | category weather forecast API | tier Free
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://pirate-weather.apiable.io/products/weatherdata/plans
- free tier: Free plan: 10,000 API requests a month with a Dark Sky style forecast (currently, minutely, hourly and daily data) and ERA5 historic weather; plans of USD 3 a month for 20,000 and USD 5 a month for 60,000 follow. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The monthly quota is the only published limit; at it the API answers HTTP 429, and Ratelimit-Limit, Ratelimit-Remaining and Ratelimit-Reset headers report the month's count. The plans page says historic data reach back to 1980 and the home page says 1940. Bulk path: none documented. The public-apis list marks the service as keyless, but a call with no valid key answered HTTP 401.
- per-object cap: not applicable
- retention: not applicable: the unit is a request | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: An account on the Apiable portal is created and the free plan subscribed to before a key works, and the key can take up to 20 minutes to go live; the sign-up form is rendered by script, so its fields (email, password, card, phone) are unverified, and the plans page prices the Free plan at zero.
- interface: rest
- limits:
  - request-rate (binding): 10,000 requests a month on the Free plan; at the quota the API answers HTTP 429 [1]
- binding note: The 10,000 a month quota (about 0.2 a minute) is the only published limit.
- interface detail: REST over HTTPS at api.pirateweather.net/forecast/[key]/[lat],[lon] in the Dark Sky style, with a time argument for historic requests; a hosted MCP server at mcp.pirateweather.net uses the same key
- endpoint: https://api.pirateweather.net/forecast/[apikey]/[latitude],[longitude]
- tooling: any HTTP client; Python and other libraries and a Home Assistant integration exist. Last resort: the user installs and runs the open-source server on a rented or free machine.
- composes with: A keyed Dark Sky replacement built on NOAA and ECMWF model data, with ERA5 history through the same call.
- reliability: A four hour production outage occurred on 2025-12-24; the key needs up to 20 minutes to propagate after subscribing.
- notes: Bulk path: none documented. Open-source code exists; running it is the last resort after the hosted plans.
- evidence note: Plan and quota are read from first-party pages; a call with a dummy key answered HTTP 401, so a keyed call was not exercised and the sign-up form was not readable.
- evidence:
  - [1] 2026-11-02: the Free plan allows 10,000 requests a month | capture: sha256:cca9941815f5143b13b9c4d5a5d8cb8093975788ec778f35dda536192e5846f5 | quote: Free plan, allowing up to 10,000 requests per month
  - [1] 2026-11-02: the Free plan is priced at zero | capture: sha256:cca9941815f5143b13b9c4d5a5d8cb8093975788ec778f35dda536192e5846f5 | quote: Subscriptions are free
  - [1] 2026-11-02: the USD 3 plan allows 20,000 calls a month | capture: sha256:cca9941815f5143b13b9c4d5a5d8cb8093975788ec778f35dda536192e5846f5 | quote: Subscribing to this plan helps to support this project and raises the API limit to 20,000 calls per month (~0.5 per minute)
  - [1] 2026-11-02: the USD 5 plan allows 60,000 calls a month | capture: sha256:cca9941815f5143b13b9c4d5a5d8cb8093975788ec778f35dda536192e5846f5 | quote: Subscribing to this plan helps to support this project and raises the API limit to 60,000 calls per month (~1 per minute)
  - [1] 2026-11-02: the plan table lists ERA5 historic weather back to 1980 | capture: sha256:cca9941815f5143b13b9c4d5a5d8cb8093975788ec778f35dda536192e5846f5 | quote: Historic weather data back to 1980 from the ERA5 model.
  - [2] 2026-11-02: the home page says ERA5 from 1940 | capture: sha256:8a275ff3b89b7eedcc0369b02eca3f5112cf830d648545965ab59341fb5b7404 | quote: Request ERA5 reanalysis data from 1940 onward through the same familiar API format used for current forecasts.
  - [2] 2026-11-02: the code is open source and can be run locally | capture: sha256:8a275ff3b89b7eedcc0369b02eca3f5112cf830d648545965ab59341fb5b7404 | quote: Run locally or use our cloud endpoint
  - [3] 2026-11-02: an account is created and the plan subscribed to before a key works | capture: sha256:23910e2d74271985c5b79454757dc129f71b0845f3e272d91e554ab4998a6c67 | quote: After signing up for the service, the forecast API needs to be subscribed to, by logging in and clicking subscribe.
  - [4] 2026-11-02: 429 answers at the monthly quota | capture: sha256:5e3533aa98e5d94785b7bc93ba1cd41b8c9091f35b50ac52c7fff09807a0a62e | quote: You may encounter this error if your API key has hit the quota for the month.
  - [5] 2026-11-02: a four hour production outage on 2025-12-24 | capture: sha256:12de85381454da527e88afc92f367e53a5c3a8b2798c71607905d916fc530117 | quote: The four hour production downtime had two root causes.
  - probe:https://api.pirateweather.net/forecast/0/45.42,-75.69 2026-11-02: a call with a dummy key answered 401, so a key is required | capture: sha256:119cd32f16c76dbb11892ed933df057d6c15cbadb5d130b39fd3dc6cad84cdf7 | quote: "message":"Unauthorized"
  - probe:https://api.pirateweather.net/forecast/0/45.42,-75.69 2026-11-02: the call answered HTTP 401 | capture: sha256:d6b27e0844889111e2fa42e30a0b350e96243cd5437a141483b9fa880fe7740d | quote: "status": 401
  - [6] 2026-11-02: public-apis marks Pirate Weather as needing no auth, which the 401 contradicts | capture: sha256:1ce4b056b48404fe8a332497495ca5d12ca2b9f5aa4e985e8fd5fb14f90fe164 | quote: | [Pirate Weather](https://pirateweather.readthedocs.io/en/latest/) | Free weather API with forecast data similar to Dark Sky | No | Yes | Yes |
- sources:
  - [1] https://pirate-weather.apiable.io/products/weatherdata/plans
  - [2] https://pirateweather.net/
  - [3] https://docs.pirateweather.net/en/latest/API/
  - [4] https://docs.pirateweather.net/en/latest/API/alerts-flags-errors/
  - [5] https://docs.pirateweather.net/en/latest/Blog/Infrastructure2026/
  - [6] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
