# Abstract API IP Geolocation

> abstractapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abstractapi/ | JSON https://fshy.ajam.dev/api/v1/entity/abstractapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Abstract API IP Geolocation

- `data-apis/abstract-api-ip-geolocation` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.369Z (live) | stale on 2026-12-03
- url https://www.abstractapi.com/api/ip-geolocation-api
- free tier: Free plan, USD 0 a month: 1,000 requests a month at 1 request a second, no credit card; the response is the full one, including the security and company fields that paid plans gate. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Each IP in a request counts as one credit, and credits are counted per request, not per successful response. Past the monthly credits the API answers HTTP 422, and past 1 request a second HTTP 429. Starter is USD 17 a month billed annually (USD 19 paid monthly).
- per-object cap: one IP address per request; the product page says no separate batch endpoint is needed | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an email address and password with a verification link, or Google sign-in; no credit card on the free plan
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a month on the Free plan [1]
  - request-rate: 1 request a second on the Free plan; HTTP 429 above it [3]
- binding note: 1,000 requests a month is used up long before 1 request a second can matter.
- interface detail: GET https://ipgeolocation.abstractapi.com/v1/ with api_key, an optional ip_address (IPv4 or IPv6; the caller's address when omitted) and an optional fields list; JSON over HTTPS, TLS 1.2 or greater
- endpoint: part of interface detail
- tooling: any HTTP client; vendor libraries for Python, PHP and Node.js
- composes with: 1,000 keyed lookups a month, each returning location, time zone, flag, currency, ASN, company and security fields, at 1 request a second. Bulk path: none; the single-IP call is looped at the plan's rate limit, and a browser bulk tool takes a pasted list with no key
- reliability: Past the free monthly credits the API answers HTTP 422, and past 1 request a second HTTP 429; a request for an invalid IP still uses one credit.
- notes: Free requests: 1,000 a month at 1 request a second. Rate limit: 1 request a second on the free plan (HTTP 429). The product page advises caching by address block. Bulk path: none; the single-IP call is looped at the plan's rate limit, and a browser bulk lookup tool needs no key.
- evidence note: The pricing, product, documentation and sign-up pages were read on 2026-11-02, and a keyless call to the API answered HTTP 400 naming api_key as required; no keyed lookup was made, so the quota and the rate limit are as published.
- extras:
  - bulk_path: none; loop the single-IP API at the rate limit; a browser bulk tool takes a pasted list with no key
  - free_requests: 1,000 a month
- evidence:
  - [1] 2026-11-02: the free IP Geolocation plan is 1,000 requests a month at 1 request a second with no credit card | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: 1,000 requests a month at 1 request a second, no credit card.
  - [1] 2026-11-02: the free tier of the IP API is 1,000 requests, against 100 for the email and phone APIs | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: Free tier: 100 requests a month on email and phone, 1,000 on IP.
  - [1] 2026-11-02: the free plan returns the full response | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: The free plan returns the complete response, including the security and company fields that paid plans gate.
  - [1] 2026-11-02: the free plan is limited to 1 request a second | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: 10 requests a second on every paid plan, and 1 request a second on the free plan.
  - [1] 2026-11-02: the free tier is permanent and needs no card | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: Every API has a permanently free tier with no credit card
  - [1] 2026-11-02: Starter is USD 17 a month when billed annually | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: Starter is $17 a month billed annually and includes 200,000 requests a month, which works out to $0.085 per 1,000 requests.
  - [1] 2026-11-02: the same Starter plan is USD 19 a month when paid monthly | capture: sha256:92ea3542b006b90d81f693bd031c403c89219d0ee83988a93ff66eb96d148046 | quote: Abstract's price is billed annually, $19 paid monthly.
  - [3] 2026-11-02: a free plan that has used its credits is answered HTTP 422 | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: | 422 | Quota reached | The request was aborted due to insufficient API credits. (Free plans) |
  - [3] 2026-11-02: above 1 request a second a free plan is answered HTTP 429 | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: | 429 | Too many requests | The request was aborted due to the number of allowed requests per second being reached. This happens on free plans as requests are limited to 1 per second. |
  - [3] 2026-11-02: every submitted IP uses one credit, and a failed request still uses it | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: A note on metered billing: Each individual IP you submit counts as a credit used. Credits are also counted per request, not per successful response.
  - [3] 2026-11-02: the API is HTTPS only | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: The IP Geolocation API requires all communications to be secured with TLS 1.2 or greater.
  - [3] 2026-11-02: the ip_address parameter takes one IPv4 or IPv6 address | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: The IP address to geolocate. Both IPv4 and IPv6 addresses are supported.
  - [3] 2026-11-02: the base URL of the API | capture: sha256:97284f719ad5dc104ab079966d5b0c545690bd17e49a90e7c77865aa07dea355 | quote: https://ipgeolocation.abstractapi.com/v1/
  - [2] 2026-11-02: the bulk routes are a loop over the API and a free browser tool | capture: sha256:69b6c93a227230d6370e7557b523f771c724942bddba41526bd3573a56d06903 | quote: To geolocate many addresses at once, send them through the API in a loop at your plan's rate limit, or paste a list into Abstract's free bulk IP lookup tool.
  - [2] 2026-11-02: the API has no batch endpoint | capture: sha256:69b6c93a227230d6370e7557b523f771c724942bddba41526bd3573a56d06903 | quote: No separate batch endpoint is needed.
  - [2] 2026-11-02: the product page advises caching results by address block | capture: sha256:69b6c93a227230d6370e7557b523f771c724942bddba41526bd3573a56d06903 | quote: Cache by address block rather than by address, since consecutive addresses in a block almost always resolve to the same place.
  - [2] 2026-11-02: vendor libraries exist for Python, PHP and Node.js | capture: sha256:69b6c93a227230d6370e7557b523f771c724942bddba41526bd3573a56d06903 | quote: Use our dedicated Python, PHP, and Node.js libraries, or test live requests instantly in our interactive sandbox.
  - [4] 2026-11-02: the browser bulk lookup tool needs no signup | capture: sha256:2b7e62401a9ec4c7610f4552de437e28b6ff66c24592a834e3ce3807d4ee0c46 | quote: Free, no signup required.
  - [4] 2026-11-02: the browser bulk lookup tool is rate limited | capture: sha256:2b7e62401a9ec4c7610f4552de437e28b6ff66c24592a834e3ce3807d4ee0c46 | quote: The free tool is rate limited, and the counter next to the upload link shows how much of your list will run before you start.
  - [5] 2026-11-02: the sign-up page issues an API key | capture: sha256:87897d8e88152e8756afb5c755e7db6e30f6e46bc08972489f8b503c2e442a8c | quote: Get your API key in seconds
  - [5] 2026-11-02: sign-up takes an email address and a password | capture: sha256:87897d8e88152e8756afb5c755e7db6e30f6e46bc08972489f8b503c2e442a8c | quote: Email address
  - [5] 2026-11-02: Google sign-in is offered | capture: sha256:87897d8e88152e8756afb5c755e7db6e30f6e46bc08972489f8b503c2e442a8c | quote: Sign in with Google
  - [5] 2026-11-02: the account is activated through a verification link sent by email | capture: sha256:87897d8e88152e8756afb5c755e7db6e30f6e46bc08972489f8b503c2e442a8c | quote: Please click it to activate your account.
  - [6] 2026-11-02: a call with no key answers HTTP 400 and names api_key as required, so the endpoint is live and keyed | capture: sha256:6fca07c1a9f7763385d9983a7974ca59bcc5757999020fb0ffcd31f65c572655 | quote: "api_key":["This is a required argument."]
  - [6] 2026-11-02: the keyless call answers HTTP 400 | capture: sha256:6fca07c1a9f7763385d9983a7974ca59bcc5757999020fb0ffcd31f65c572655 | quote: HTTP/1.1 400 Bad Request
- sources:
  - [1] https://www.abstractapi.com/pricing
  - [2] https://www.abstractapi.com/api/ip-geolocation-api
  - [3] https://docs.abstractapi.com/api/ip-geolocation
  - [4] https://www.abstractapi.com/tools/bulk-ip-lookup
  - [5] https://app.abstractapi.com/users/signup
  - [6] https://ipgeolocation.abstractapi.com/v1/?ip_address=8.8.8.8
