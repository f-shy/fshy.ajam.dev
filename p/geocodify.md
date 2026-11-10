# Geocodify

> geocodify.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geocodify/ | JSON https://fshy.ajam.dev/api/v1/entity/geocodify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Geocodify

- `data-apis/geocodify` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding, geoparsing and elevation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://geocodify.com/pricing
- free tier: Free plan: 30,000 calls a month at 1 request per second, community support; the sign-up page says no card is required | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: the API docs call the 1-request-per-second allowance a Free Trial, while the pricing page and the sign-up page list it as the Free plan at 30,000 calls a month
- per-object cap: the API docs list one address or coordinate a request (q for /geocode, lat and lng for /reverse); the home page also offers batch geocoding and a dashboard upload of CSV or Excel spreadsheets, and whether the Free plan includes them is unverified | source: [2]
- retention: data returned from the API may be reproduced in applications with credit, and must not be cached, stored or persisted for more than 30 days | days: 30 | source: [3]
- egress: not applicable: a query API metered in calls, not bytes | metered: no | source: [1]
- identity: email | detail: an account at geocodify.com/signup with a first name, last name, email and password, or Google or GitHub sign-in; the page says no card is required
- interface: rest
- limits:
  - volume-quota (binding): 30,000 calls a month on the Free plan [1]
  - request-rate: 1 request per second on the Free plan, answered with HTTP 429 beyond it [2]
  - retention-clamped: data returned from the API may be cached or stored for at most 30 days [3]
- binding note: 1 request per second allows far more than 30,000 calls in a month, so the monthly allowance is met first
- interface detail: HTTPS GET to api.geocodify.com/v2 (/geocode, /reverse, /geoparse, /autocomplete, /parse, /elevation) with the key in an api_key parameter, JSON answers, CORS enabled; a keyless geocode answered HTTP 401 with Missing or invalid api credentials
- endpoint: https://api.geocodify.com/v2/geocode
- tooling: any HTTP client; a CSV and Excel upload tool in the dashboard
- composes with: bulk work is single requests at 1 a second or the dashboard's spreadsheet upload
- reliability: the docs warn that a 200 OK can be returned even when usage limits are reached or parameters are missing, with the details in the JSON meta field; past 1 request per second the API answers HTTP 429
- notes: Free requests: 30,000 calls a month. Rate limit: 1 request per second. Bulk path: spreadsheet upload in the dashboard (Free plan availability unverified); the API is one query a request.
- evidence note: the pricing page, the API docs, the terms, the sign-up page and the home page were quoted on 2026-11-02; a keyless geocode answered HTTP 401. No account was opened, so the free monthly allowance was not exercised.
- extras:
  - free_requests: 30,000 calls a month at 1 request per second
  - rate_limit: 1 request per second on the Free plan
  - bulk_path: dashboard upload of CSV or Excel spreadsheets; single API requests at 1 a second
- evidence:
  - [1] 2026-11-02:  | capture: sha256:850a0ec3256e6abdee4a01a5b7265d35116bddca61858bdcc79ee3478bed8fa2
  - [1] 2026-11-02:  | capture: sha256:850a0ec3256e6abdee4a01a5b7265d35116bddca61858bdcc79ee3478bed8fa2
  - [4] 2026-11-02: the free account gives 30,000 requests a month with no card | capture: sha256:d5c7b95cda4d29f6d710cd4aa048a456008780979468f626c723be0db87ec352 | quote: 30,000 requests a month, no card required.
  - [4] 2026-11-02: the sign-up form asks for first name, last name, email and password | capture: sha256:d5c7b95cda4d29f6d710cd4aa048a456008780979468f626c723be0db87ec352 | quote: First name Last name Email Password
  - [4] 2026-11-02: sign-up also offers Google and GitHub | capture: sha256:d5c7b95cda4d29f6d710cd4aa048a456008780979468f626c723be0db87ec352 | quote: [Google](https://geocodify.com/auth/google/redirect) [GitHub](https://geocodify.com/auth/github/redirect)
  - [2] 2026-11-02: the docs call the free allowance a Free Trial limited to 1 request per second | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: Free Trial:** Limited to 1 request per second.
  - [2] 2026-11-02: exceeding the rate limit answers HTTP 429 | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: If you exceed these limits, you will receive a `429 Too Many Requests` response.
  - [2] 2026-11-02: a 200 OK can come back even when usage limits are reached or parameters are missing | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: Note that in some cases, a `200 OK` may be returned even if usage limits are reached or parameters are missing, with details in the JSON `meta` field.
  - [2] 2026-11-02: the key goes in an api_key URL parameter | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: An API key is required for every request. This key authenticates you with our API and must be provided as an `api_key` URL parameter.
  - [2] 2026-11-02: the API base URL is api.geocodify.com/v2 | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: https://api.geocodify.com/v2
  - [2] 2026-11-02: the /geocode endpoint returns coordinates and place details for one search query | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: | `/geocode` | Returns longitude, latitude, and place details based on a search query (address, place name, or location). |
  - [2] 2026-11-02: CORS is supported by default | capture: sha256:de25bbdbbf98dc979ab17e7f558e2256c21b4bd57e62246c87db653b769cbda9 | quote: The Geocodify API supports Cross-Origin Resource Sharing (CORS) by default, allowing you to call the API directly from client-side JavaScript.
  - [3] 2026-11-02:  | capture: sha256:95f6699bb91381d4f66135d73bfb66efd3438038ba674617fe81c6ef18f9459a | quote: You can not cache / store / persist the data returned from our API for more than 30 days.
  - [3] 2026-11-02: API data may be reproduced in applications with credit | capture: sha256:95f6699bb91381d4f66135d73bfb66efd3438038ba674617fe81c6ef18f9459a | quote: You can reproduce the data returned from the API in your applications, but you need to credit us in your terms or about page.
  - [5] 2026-11-02: the dashboard geocodes uploaded CSV or Excel spreadsheets | capture: sha256:1bafb6fc99227d603652ba58c63553f012df23979d185c6a4dd676b868b1af26 | quote: Upload your CSV or Excel spreadsheet into our easy-to-use dashboard and perform all your geocoding needs.
  - [5] 2026-11-02: the home page offers forward, reverse and batch geocoding | capture: sha256:1bafb6fc99227d603652ba58c63553f012df23979d185c6a4dd676b868b1af26 | quote: We offer forward, reverse and batch geocoding for over 200 countries and millions of addresses around the world.
  - probe:https://api.geocodify.com/v2/geocode?q=Zurich 2026-11-02: a keyless geocode answers HTTP 401 | capture: sha256:c41aacd65fe4f549b7f7e97c170ab54bc6ee1fbf54440a82d99169723eaf1d75 | quote: "status": 401
  - probe:https://api.geocodify.com/v2/geocode?q=Zurich#body 2026-11-02: the keyless geocode is refused with Missing or invalid api credentials | capture: sha256:7e1b4c0c39afca6b09359ed585a23a85799ca9a298385023128dfc4c2a575b65 | quote: Missing or invalid api credentials.
- sources:
  - [1] https://geocodify.com/pricing
  - [2] https://geocodify.com/api-documentation
  - [3] https://geocodify.com/terms
  - [4] https://geocodify.com/signup
  - [5] https://geocodify.com/
