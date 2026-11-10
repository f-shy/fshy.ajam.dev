# LatLng

> latlng.work | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/latlng/ | JSON https://fshy.ajam.dev/api/v1/entity/latlng.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LatLng

- `data-apis/latlng` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding, places and map tiles API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://www.latlng.work/docs
- free tier: Free plan, USD 0 a month, no credit card: 3,000 forward geocodes a day, 300 reverse geocodes a day and 100 places searches a day by the terms table; the API docs describe one unified pool of 3,000 total API calls a day shared by geocoding, reverse, places and tile requests | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: the terms table and the docs page describe the daily quota differently, and which one applies is unverified; calls without any key are also answered in small numbers (the Python SDK page says 30 geocodes a day, and a keyless call returned an x-ratelimit-limit header of 60); the Pro plan is USD 29 a month for 1,000,000 geocoding requests a month
- per-object cap: no batch endpoint: one address a request, and the batch geocoding page sends 10 to 50 parallel single requests; Free dataset uploads are 3 datasets of at most 50 MB each | source: [2]
- retention: no rule for storing results is stated | source: [1]
- egress: not applicable: a query API metered in requests, not bytes | metered: no | source: [3]
- identity: email | detail: an account at dash.latlng.work, a JavaScript sign-in page whose fields are not in the page text; the vendor's page says to sign up with an email or GitHub and get instant API keys with no credit card; one account and one API key per entity on the free tier; the form fields themselves are unverified: behind a sign-up
- interface: rest
- limits:
  - volume-quota (binding): 3,000 forward geocodes, 300 reverse geocodes and 100 places searches a day on the Free plan (terms table); the docs list one pool of 3,000 total API calls a day [1]
  - request-rate: no per-second limit is published; the API answers HTTP 429 when the quota is exceeded and sends X-RateLimit-Limit and X-RateLimit-Remaining headers [3]
  - per-object-cap: 3 datasets of at most 50 MB each on the Free plan [3]
- binding note: no per-second figure is published, so the daily quota is the ceiling that is stated and met first
- interface detail: HTTPS GET to api.latlng.work/api (forward) and /reverse with the key in an X-Api-Key header or an api_key parameter, GeoJSON answers; places, static map and autosuggest endpoints and vector tiles at tiles.latlng.work use the same account; a call without any key answered HTTP 200 with GeoJSON and an x-ratelimit-limit header of 60
- endpoint: https://api.latlng.work/api
- tooling: any HTTP client; an official Rust crate and a Python SDK
- composes with: 3,000 forward geocodes a day on an email or GitHub account with no card, built on OpenStreetMap data, plus 300 reverse geocodes a day and vector tiles on the same key; public applications must show the OpenStreetMap attribution; bulk work is parallel single requests since no batch endpoint exists
- reliability: exceeding the plan limits may suspend access to the affected service, and extra free accounts opened to get more quota can end every account; the allowance without a key is small
- notes: Free requests: 3,000 forward geocodes a day (the docs describe a shared 3,000-call pool). Rate limit: no per-second figure published. Caching is advised and scraping to build a competing dataset is barred. Bulk path: none; parallel single requests.
- evidence note: the home page, the docs, the terms, the batch geocoding page, the Python SDK page and the key-free sign-up page were quoted on 2026-11-02; a call without a key answered HTTP 200 with GeoJSON. No account was opened, so the free daily quota and the sign-up fields were not exercised.
- extras:
  - free_requests: 3,000 forward geocodes, 300 reverse geocodes and 100 places searches a day (terms); 3,000 total calls a day (docs)
  - rate_limit: unverified: no per-second limit is published; a key-free call returned x-ratelimit-limit 60
  - bulk_path: none: no batch endpoint; parallel single requests, 10 to 50 at a time
- evidence:
  - [1] 2026-11-02: the Free plan allows 3,000 forward geocodes a day | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767 | quote: | Geocoding (forward) | 3,000 / day | 1,000,000 / month |
  - [1] 2026-11-02: the Free plan allows 300 reverse geocodes a day | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767 | quote: | Reverse Geocoding | 300 / day | 100,000 / month |
  - [1] 2026-11-02: the Free plan allows 100 places searches a day | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767 | quote: | Places Search | 100 / day | 50,000 / month |
  - [3] 2026-11-02: the docs list the Free plan as 3,000 total API calls a day | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: | Free | 3,000 total API calls | Per day |
  - [3] 2026-11-02: the docs describe one unified quota shared by geocoding, reverse, places and tile calls | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: Usage is tracked per-user across all API keys with a unified quota — all API calls (geocoding, reverse, places, tiles) count toward one shared pool.
  - [4] 2026-11-02: the home page prices the Free plan at USD 0 a month | capture: sha256:b4e1a3dadca9bf1edf7c5f6ac4b4be83f407497f67cced781b6ee1e1bf27dfdc | quote: $0/month
  - [4] 2026-11-02: the home page lists 3,000 geocoding requests a day on the Free plan | capture: sha256:b4e1a3dadca9bf1edf7c5f6ac4b4be83f407497f67cced781b6ee1e1bf27dfdc | quote: 3,000 geocoding requests/day
  - [3] 2026-11-02: exceeding the rate limit answers HTTP 429 | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: | `429` | Too Many Requests — Rate limit exceeded |
  - [1] 2026-11-02: exceeding the limits may suspend access to the affected service | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767 | quote: Exceeding these limits may result in temporary suspension of API access for the affected service.
  - [1] 2026-11-02: the free tier allows one account and one API key per entity | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767 | quote: Each entity is permitted only one account and one API key on the free tier.
  - [1] 2026-11-02: public applications must carry the OpenStreetMap attribution | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767
  - [1] 2026-11-02: automated scraping of results to build a competing dataset is barred | capture: sha256:4aa5539f207650a3b40e6cb4548d57caca3ed3089aa9b4a69481e3ce3b78e767
  - [2] 2026-11-02: the batch geocoding page advises caching results to avoid re-geocoding duplicates | capture: sha256:3068db32661180e62a7384f4d27ab89c266f288e90d0d28949b09b3c0399cdfd | quote: Cache results to avoid re-geocoding duplicates
  - [2] 2026-11-02: bulk geocoding is parallel single requests, 10 to 50 at a time | capture: sha256:3068db32661180e62a7384f4d27ab89c266f288e90d0d28949b09b3c0399cdfd | quote: Use parallel requests (10-50 concurrent) for best performance
  - [3] 2026-11-02: Free dataset uploads are 3 datasets of at most 50 MB each | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: | Free | 3 | 50 MB |
  - [3] 2026-11-02: forward geocoding is a GET to api.latlng.work/api | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: GET https://api.latlng.work/api
  - [3] 2026-11-02: the key goes in an X-Api-Key header or an api_key parameter | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: The `X-Api-Key` header is the recommended format. You can also pass the key as a query parameter (`?api_key=YOUR_KEY`) for backward compatibility.
  - [4] 2026-11-02: the Pro plan is $29/month for 1,000,000 geocoding requests a month | capture: sha256:b4e1a3dadca9bf1edf7c5f6ac4b4be83f407497f67cced781b6ee1e1bf27dfdc | quote: ### Pro $29/month - 1,000,000 geocoding requests/month
  - [3] 2026-11-02: reverse geocoding is a GET to api.latlng.work/reverse | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: GET https://api.latlng.work/reverse
  - [3] 2026-11-02: a places search endpoint exists on the same API host | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: https://api.latlng.work/v1/places/search
  - [3] 2026-11-02: an autosuggest endpoint exists at suggest.latlng.work | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: https://suggest.latlng.work/autosuggest
  - [3] 2026-11-02: vector tiles are served at tiles.latlng.work with a maps key | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: https://tiles.latlng.work/v1/tiles/{z}/{x}/{y}.pbf?key=pk_latlng_...
  - [3] 2026-11-02: a static maps endpoint exists on the same API host | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: https://api.latlng.work/v1/static
  - [3] 2026-11-02: an official Rust crate is offered | capture: sha256:9b2e3b2a4dfa27cdd98175f3910b4fa18bd7f770055712901c1497a3053ba3a1 | quote: Use the official Rust crate for geocoding
  - [5] 2026-11-02: sign-up takes an email or GitHub login, with no credit card gate | capture: sha256:ff21fda109e9cc8f052671f0ada80a052ca6989b77a31640c8a5c531bec34adf | quote: Zero Credit Card Gatekeeping:** Sign up with your email or GitHub and get instant API keys.
  - [6] 2026-11-02: the SDK page sends users to dash.latlng.work for a free key | capture: sha256:7c60afe1df7c7755041ddd7d67905f046a438c20f86bca67db3bc8b84d9ba4c4 | quote: Get your free key at dash.latlng.work
  - [6] 2026-11-02: a client without a key is allowed 30 geocodes a day | capture: sha256:7c60afe1df7c7755041ddd7d67905f046a438c20f86bca67db3bc8b84d9ba4c4 | quote: client = LatlngClient() # anonymous — 30 geocodes/day
  - probe:https://api.latlng.work/api?q=Zurich 2026-11-02: a geocode call without any key answers HTTP 200 | capture: sha256:d6f9987b258a33627591d51c93310d36441fd2a38c759efb77198eadaf1ce9e1 | quote: "status": 200
  - probe:https://api.latlng.work/api?q=Zurich 2026-11-02: the key-free call carries an x-ratelimit-limit header of 60, whose period is not stated | capture: sha256:d6f9987b258a33627591d51c93310d36441fd2a38c759efb77198eadaf1ce9e1 | quote: "x-ratelimit-limit": "60"
- sources:
  - [1] https://www.latlng.work/terms
  - [2] https://www.latlng.work/batch-geocoding
  - [3] https://www.latlng.work/docs
  - [4] https://www.latlng.work/
  - [5] https://www.latlng.work/free-geocoding-api
  - [6] https://www.latlng.work/python-sdk
