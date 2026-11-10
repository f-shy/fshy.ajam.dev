# MET Norway

> met.no | Data APIs; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/met/ | JSON https://fshy.ajam.dev/api/v1/entity/met.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MET Norway Weather API

- `data-apis/met-norway` | qualifies | evidence documented | binding request-rate | category weather forecast API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://docs.api.met.no/doc/TermsOfService
- free tier: No fee, no key and no registration: Locationforecast and the other products of api.met.no answer any coordinate at up to 20 requests a second per application (total, not per client); the caller sets a User-Agent that names the application and gives a contact. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Over 20 requests a second needs a special agreement; throttled clients get HTTP 429, a missing or generic User-Agent gets HTTP 403, and coordinates are cut to 4 decimals. Locationforecast is refreshed every hour inside the Nordic area and every 6 hours elsewhere. Bulk path: the THREDDS server serves model files (NetCDF over OPeNDAP) for the Nordic and Arctic regions only, with no global files; historical observations come from the separate Frost API (see data-apis/met-norway-frost).
- per-object cap: not applicable
- retention: not applicable: the API serves current forecasts only; model archives are on THREDDS | source: [1]
- egress: not applicable: JSON answers; gzip compression is supported | metered: no | source: [1]
- identity: anonymous | detail: No sign-up and no key: the institute's capacity-building page says the service is open to anyone with no registration; only a User-Agent with an application name and a contact address, website or repository link is required. A call with no key answered HTTP 200.
- interface: rest
- limits:
  - request-rate (binding): 20 requests a second per application, total and not per client; over it requests are throttled with HTTP 429 [1]
  - request-rate (binding): coordinates to at most 4 decimals; 5 or more answer HTTP 403 on new products [1]
- binding note: The 20 requests a second ceiling is shared by all users of one application; the User-Agent requirement is met by one header.
- interface detail: REST over HTTPS GET at api.met.no/weatherapi (GeoJSON forecasts; also radar, nowcast, ocean, sunrise and others); gridded model files over OPeNDAP and NetCDF from thredds.met.no (an interface term for OPeNDAP is missing)
- endpoint: https://api.met.no/weatherapi/locationforecast/2.0/compact
- tooling: any HTTP client that sets a User-Agent; third-party client libraries are listed in the docs; THREDDS files are read with OPeNDAP clients, FIMEX or ncdump
- composes with: A keyless global point-forecast source for 9 days ahead with a high per-application ceiling; history comes from THREDDS archives and the Frost API, not from this endpoint.
- reliability: No SLA; a missing or generic User-Agent answers HTTP 403 and traffic over the limit is throttled with HTTP 429 or blocked.
- notes: Bulk path: THREDDS model files for the Nordic and Arctic regions; no global dump. The Frost API holds the historical observations.
- evidence note: Limits and identification rules are read from first-party pages; a keyless forecast call and an anonymous OPeNDAP call answered HTTP 200; the 20-requests-a-second ceiling was not driven. The docs link to thredds.met.no/thredds/metno.html, which answered HTTP 404.
- evidence:
  - [1] 2026-11-02: the limit is 20 requests a second per application, counted over all clients | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42 | quote: Anything over 20 requests/second per application (total, not per client) requires special agreement.
  - [1] 2026-11-02: a client that breaks the terms is throttled with HTTP 429 | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42 | quote: This means requests will start getting a 429 HTTP status code instead of any content.
  - [1] 2026-11-02: no delivery guarantee and no SLA | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42 | quote: There are no guarantees of delivery regarding this service, or possibilities to obtain an SLA.
  - [1] 2026-11-02: every request carries an identifying User-Agent | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42 | quote: All requests must (if possible) include an identifying User Agent-string (UA) in the request with the application/domain name, optionally version number.
  - [1] 2026-11-02: coordinates are cut to 4 decimals; 5 or more answer 403 on new products | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42
  - [1] 2026-11-02:  | capture: sha256:79f52778e38b4f53c4c56bedf17aa53d63cbad93604f562a62a381a085866a42
  - [2] 2026-11-02:  | capture: sha256:060d1c353c7e6172912db81c48147c232420f03b2d5b64ddbb4421d0418b3562
  - [2] 2026-11-02: Locationforecast gives 9 days ahead for any coordinate | capture: sha256:060d1c353c7e6172912db81c48147c232420f03b2d5b64ddbb4421d0418b3562 | quote: This service delivers weather forecasts for any given coordinate for the next nine days, in JSON and (deprecated) XML formats.
  - [2] 2026-11-02: bulk model files cover the Nordic and Arctic regions only | capture: sha256:060d1c353c7e6172912db81c48147c232420f03b2d5b64ddbb4421d0418b3562 | quote: Due to licensing issues we can only distribute model data for the Nordic and Arctic regions.
  - [3] 2026-11-02: forecast update cadence | capture: sha256:d4e9a23fb61d7591ab2e68a4e3adade520541cdbd76ade59b90913768a696702 | quote: Inside the Nordic area the forecast is updated every hour; for the rest of the world, every 6 hours.
  - [4] 2026-11-02: THREDDS serves gridded data over OPeNDAP | capture: sha256:ca083219fb7b14e88232c688d314c39377b403cc1a1bd7b6c2cfdde48c0d3205 | quote: This document is a brief introduction in how to extract and visualize data from THREDDS using the OPeNDAP protocol.
  - [5] 2026-11-02: no registration is needed | capture: sha256:da2497b4625833b2a2dc53ec4825d2f4191ba2b509536a4ee3b6bfefa23aa682 | quote: The service is open and available for anyone with no registration.
  - [6] 2026-11-02: there is no pricing model for high-volume sites | capture: sha256:232d50b802cb50f4d88fcf94e7afb988cd005e37579af164846e44890967a676 | quote: No. This is a public service funded by Norwegian taxpayers, primarily to assist in our mission to protect life and property in Norway, but also globally.
  - probe:https://api.met.no/weatherapi/locationforecast/2.0/compact 2026-11-02: a Locationforecast call with no key and no sign-up answered a GeoJSON forecast | capture: sha256:0c8c18fe4fd844d9567f0cd6dbfdd6abcfbb9e5d5719373840a8676a6e0cfd92 | quote: {"type":"Feature","geometry":{"type":"Point","coordinates":[10.75,59.91,3]}
  - probe:https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.91&lon=10.75 2026-11-02: the same call answered HTTP 200 | capture: sha256:a8c84ac6c238fa927d281383eaaafc8647498ea570b649a23098fd7e1d52dc8a | quote: "status": 200
  - probe:https://thredds.met.no/thredds/dodsC/metpplatest/met_forecast_1_0km_nordic_latest.nc.dds 2026-11-02: the THREDDS OPeNDAP dataset descriptor of the Nordic forecast answered with no credentials | capture: sha256:bf0d62a1c3f7929c9c436e7afb702528a11ee38ccc910c1fc65fc94903c32e48 | quote: Float32 air_temperature_2m[time = 59][y = 2321][x = 1796];
  - probe:https://thredds.met.no/thredds/dodsC/metpplatest/met_forecast_1_0km_nordic_latest.nc.dds 2026-11-02: the THREDDS call answered HTTP 200 | capture: sha256:84e3a0213acc63c2618d391895266f3286dc16924a4d727e6c99b50656e62b7e | quote: "status": 200
- sources:
  - [1] https://docs.api.met.no/doc/TermsOfService
  - [2] https://api.met.no/weatherapi/locationforecast/2.0/documentation
  - [3] https://docs.api.met.no/doc/locationforecast/FAQ.html
  - [4] https://docs.api.met.no/doc/thredds
  - [5] https://bistand.met.no/en/weather-api
  - [6] https://docs.api.met.no/doc/FAQ.html

## MET Norway Frost API

- `data-apis/met-norway-frost` | qualifies-with-caveat | evidence documented | binding request-rate | category weather observation archive API | tier free (client ID)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://frost.met.no/
- free tier: Free access to MET Norway's archive of historical weather and climate observations (quality controlled daily, monthly and yearly measurements of temperature, precipitation and wind, and station metadata) with a client ID issued for an email address; no numeric request quota is published. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Heavy traffic is defined as more than 1 request a second on average, which should be cached locally; users with high load or bad traffic patterns can be blocked. Large requests time out and are split by station or by time range. Bulk path: none beyond split requests; gridded model data are on THREDDS (see data-apis/met-norway).
- per-object cap: requests that are too large time out; the vendor advises splitting, for example 1000 stations into 10 requests of 100 | source: [1]
- retention: not applicable: the unit is a request | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: A client ID and secret are issued after registering with an email address; each client ID must be tied to a valid email address. The form's other fields were not readable.
- interface: rest
- limits:
  - request-rate (binding): more than 1 request a second on average is heavy traffic that should be cached; no hard number is published [1]
  - per-object-cap: requests that are too large answer a timeout and must be split [1]
- binding note: Only the 1 request a second guideline is stated, so the sustained rate binds first.
- interface detail: REST over HTTPS at frost.met.no with Basic authentication (client ID as user name, empty password) or OAuth2; JSON-LD answers
- endpoint: https://frost.met.no/observations/v0.jsonld
- tooling: any HTTP client; examples for curl, Python and Java are published
- composes with: The historical-observation companion to the keyless api.met.no forecasts: station data by source, reference time and element.
- reliability: No delivery guarantee; clients with high load or bad traffic patterns can be blocked.
- notes: Observations only; forecasts are on api.met.no.
- evidence note: Identity and traffic rules are read from first-party pages; a call with no client ID answered HTTP 401, so a keyed call was not exercised.
- evidence:
  - [2] 2026-11-02: Frost serves MET Norway's historical observation archive | capture: sha256:025df8ae4df15bc54fde881bc110704c3cb82913125f39da9d282a26ac2ea38a | quote: This data includes quality controlled daily, monthly, and yearly measurements of temperature, precipitation, and wind data.
  - [3] 2026-11-02: an email address gives a client ID | capture: sha256:9c44059398a208785e84e3710a980838bcfef5d83dd6b75e249ac850a365d6e9 | quote: To gain access to the Frost API services, register with your email address to generate a new client ID and client secret.
  - [4] 2026-11-02: every data request needs a client ID | capture: sha256:e1042982e053b697f782683052ea084e758281acd9b32f23736c6e667ddbefa2 | quote: Requests for data (typically everything else than static HTML-pages) must be authenticated with a client ID
  - [1] 2026-11-02: more than 1 request a second on average counts as heavy traffic, to be cached locally | capture: sha256:88f40f7f309f82b41ba5f248333ec8c10701593ff56f9d8005d02e1130fe2186 | quote: Heavy traffic means on average more than 1 requests to the API per second.
  - [1] 2026-11-02: a client ID needs a valid email address; several IDs per address are allowed | capture: sha256:88f40f7f309f82b41ba5f248333ec8c10701593ff56f9d8005d02e1130fe2186 | quote: Each client ID must be associated with a valid email address. It is possible to register multiple client IDs for each email address.
  - [1] 2026-11-02: large requests time out and must be split | capture: sha256:88f40f7f309f82b41ba5f248333ec8c10701593ff56f9d8005d02e1130fe2186 | quote: If your request is too large, you will get a timeout error.
  - [1] 2026-11-02: no delivery guarantee | capture: sha256:88f40f7f309f82b41ba5f248333ec8c10701593ff56f9d8005d02e1130fe2186 | quote: There are no guarantees of delivery regarding this service.
  - probe:https://frost.met.no/sources/v0.jsonld 2026-11-02: a call with no client ID answered 401 | capture: sha256:95440acbcf9f3685835289bf8fc1021d3ccd309de60bffb316460ba7e1399a9e | quote: "reason" : "Missing authentication token"
  - probe:https://frost.met.no/sources/v0.jsonld 2026-11-02: the call answered HTTP 401 | capture: sha256:bb7565dc81e61ed82bd7ac76d8ae3fd76b717c894130c52bb734f686bfb0ff95 | quote: "status": 401
- sources:
  - [1] https://frost.met.no/termsofuse2.html
  - [2] https://frost.met.no/
  - [3] https://frost.met.no/auth/requestCredentials.html
  - [4] https://frost.met.no/authentication.html
