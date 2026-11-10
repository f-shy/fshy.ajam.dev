# National Weather Service API

> weather.gov | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/weather-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/weather-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## National Weather Service API

- `data-apis/nws-api` | qualifies | evidence documented | binding request-rate | category weather forecast API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2026-12-03
- url https://www.weather.gov/documentation/services-web-api
- free tier: Open data with no fee, no key and no registration: forecasts, alerts and observations for the United States from api.weather.gov; a User-Agent header is required and the request rate limit is not published. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Station observations are kept for 7 days and alerts for 7 days; a point outside the United States answers HTTP 404. Bulk path: the NOMADS server (120 hits a minute per IP address, counted across the NCEP hosts) and the NOAA Open Data Dissemination buckets on cloud platforms, open to the public; NWS alert archives are held by NCEI.
- per-object cap: not applicable
- retention: station observations are retained for 7 days and alerts for the past 7 days | days: 7 | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: No sign-up and no key: a User-Agent string, which can be anything and may carry a contact, is the only identification; the vendor plans to replace it with an API key.
- interface: rest
- limits:
  - request-rate (binding): unverified: the rate limit is not published; over it the API answers an error that can be retried after the limit clears, typically within 5 seconds [1]
- binding note: The only stated limit is the unpublished request rate.
- interface detail: REST over HTTPS at api.weather.gov (GeoJSON, JSON-LD, DWML, CAP and ATOM by the Accept header); an OpenAPI 3.1 specification is published at api.weather.gov/openapi.json
- endpoint: https://api.weather.gov/points/{latitude},{longitude}
- tooling: any HTTP client that sets a User-Agent; OpenAPI specification for generated clients
- composes with: A keyless official US forecast and alert source; pair with api.met.no for coordinates outside the United States and with NOAA's NODD buckets for model files.
- reliability: A request without a User-Agent answers HTTP 403; over the unpublished limit the API errors and recovers after about 5 seconds.
- notes: Bulk path: NOMADS and the NODD cloud buckets; no dump through the API itself.
- evidence note: Terms are read from first-party pages; keyless points and forecast calls answered HTTP 200 and a non-US point answered HTTP 404; the rate limit was not driven.
- evidence:
  - [1] 2026-11-02: the API is open data with no fee | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: All of the information presented via the API is intended to be open data, free to use for any purpose.
  - [1] 2026-11-02: the rate limit is unpublished | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: The rate limit is not public information, but allows a generous amount for typical use.
  - [1] 2026-11-02: over the limit a request errors and can be retried, typically within 5 seconds | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: If the rate limit is execeed a request will return with an error, and may be retried after the limit clears (typically within 5 seconds).
  - [1] 2026-11-02: a User-Agent is the only identification | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: A User Agent is required to identify your application.
  - [1] 2026-11-02: an API key is planned | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: This will be replaced with an API key in the future.
  - [1] 2026-11-02: station observations are kept 7 days | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: Note: since this service is designed for realtime data, only 7 days of observations are retained for weather stations.
  - [1] 2026-11-02: alerts reach back 7 days | capture: sha256:d502e3c7040d4d76e812aa65c0cc6dd36c6d7488f9daf54747525d6b1f5691d3 | quote: The /alerts endpoint contains alerts issued over the past seven days.
  - [2] 2026-11-02: the User-Agent string does not change limits | capture: sha256:3bdb5de5cd31fd30d1579868d0113ceb313f53845dbf382b335eb142009fae17 | quote: The API remains open and free to use and there are no limits imposed based on the User-Agent string.
  - [3] 2026-11-02: a request without a User-Agent answers 403 | capture: sha256:645f7b783c5a20f4db14c7a11a8d5045af464f8b55d4865716d5b25282817be2 | quote: Make sure your program is including a `User-Agent` header in your request.
  - probe:https://api.weather.gov/points/38.8894,-77.0352 2026-11-02: a points call with no key answered the forecast URL for the grid | capture: sha256:daa8b99e25fce942e1923e4bd7f819c7b009a2b2d79dcffc846ab6598216d97b | quote: "forecast": "https://api.weather.gov/gridpoints/LWX/97,71/forecast",
  - probe:https://api.weather.gov/points/38.8894,-77.0352 2026-11-02: the points call answered HTTP 200 | capture: sha256:68b7cfe24b2b965b71f84bf3a269a87e17b060fb957db60ee12142a73ab08f1a | quote: "status": 200
  - probe:https://api.weather.gov/gridpoints/LWX/96,70/forecast 2026-11-02: a forecast call with no key answered HTTP 200 | capture: sha256:6557146546234ac8fbd8917742df015d2b99377d1f34a49095e47d71426e80b2 | quote: "status": 200
  - probe:https://api.weather.gov/points/59.91,10.75 2026-11-02: a point outside the United States answers 404, so coverage is limited | capture: sha256:97f8f878e3064c7df80eb01aebd520df681a9f3066162c404d65732cffa381d5 | quote: "title": "Data Unavailable For Requested Point"
  - probe:https://api.weather.gov/points/59.91,10.75 2026-11-02: the out-of-coverage call answered HTTP 404 | capture: sha256:0cd8676e88e29788b8017ffd33aecc4768ceed99ee1cd20b29ffa1111e9b480d | quote: "status": 404
  - [4] 2026-11-02: NOMADS and the NCEP ftp hosts allow 120 hits a minute per IP address | capture: sha256:b2fe9ae872a0d03ddd983c9e2cd374c1cc8da65aca991ca9abdc9be4422b41bc
  - [5] 2026-11-02: NOAA model and radar data are published on cloud platforms | capture: sha256:654800ee6f026523ecc1fd594c31a751b6e67df42e4897fd3b7d51c4bd952206 | quote: The NOAA Open Data Dissemination (NODD) Program provides public access to NOAA's open data on commercial cloud platforms through public-private partnerships.
  - [6] 2026-11-02: NODD data are open to the public | capture: sha256:a03585b706ac7180ad650c27052738c349ddf57f286b3411904d2bcf98d44680 | quote: NOAA data disseminated through NODD are open to the public and can be used as desired.
  - [7] 2026-11-02: listed under Weather in public-apis with no auth | capture: sha256:1ce4b056b48404fe8a332497495ca5d12ca2b9f5aa4e985e8fd5fb14f90fe164 | quote: | [US Weather](https://www.weather.gov/documentation/services-web-api) | US National Weather Service | No | Yes | Yes |
- sources:
  - [1] https://www.weather.gov/documentation/services-web-api
  - [2] https://api.weather.gov/openapi.json
  - [3] https://weather-gov.github.io/api/general-faqs
  - [4] https://www.weather.gov/media/notification/pdf2/scn21-32nomad_changes.pdf
  - [5] https://www.noaa.gov/information-technology/open-data-dissemination
  - [6] https://registry.opendata.aws/noaa-gfs-bdp-pds/
  - [7] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
