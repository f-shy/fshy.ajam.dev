# Geolocated.io

> geolocated.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geolocated/ | JSON https://fshy.ajam.dev/api/v1/entity/geolocated.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Geolocated.io

- `data-apis/geolocated-io` | dead | evidence documented | binding volume-quota | category IP geolocation API | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.369Z (live) | stale on 2026-12-03
- url https://geolocated.io/pricing.html
- free tier: Hobby plan, USD 0 a month, as listed on the pricing page: 2,000 requests a day at 100 requests a minute, Essentials data, standard IP lookup only (no self lookup, no batch), no credit card. The home page now links to Contact Us in place of a sign-up page, and the sign-up host answers HTTP 522. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The daily quota counts every endpoint together; past it the API answers HTTP 429 DailyLimitExceeded until the reset time, and past the per-minute rate HTTP 429 RateLimitExceeded. The API servers are in the US and Asia. Starter is USD 25 a month for 50,000 requests a day at 800 a minute.
- per-object cap: one IP address per lookup on Hobby; the batch lookup takes up to 25 addresses a request and starts at the Growth plan | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: when sign-up was open: a name, email address, business name and country, and an email code to sign in; no credit card for Hobby. The sign-up page is no longer linked.
- interface: rest
- limits:
  - volume-quota (binding): 2,000 requests a day on the Hobby plan, counted across all endpoints [1]
  - request-rate: 100 requests a minute on the Hobby plan [1]
- binding note: No quota can be reached while registration is closed; if it reopened, 2,000 requests a day would bind long before 100 a minute.
- interface detail: GET /ip/{ip-address}?api-key=KEY, GET /ip/me (self lookup) and POST /ip/batch (a JSON array) on an API-server host named {api-server}.geolocated.io, JSON over HTTPS; the key is tied to the chosen API server
- tooling: any HTTP client
- composes with: Not reachable for a new account: the sign-up page is no longer linked and its host answers HTTP 522, so the 2,000 daily lookups of Hobby cannot be obtained. Bulk path: none on Hobby; the batch lookup (25 addresses a request) is on Growth and Scale
- reliability: The home and pricing pages carry Sunset: Mon, 31 Aug 2026 23:59:59 GMT, the archived home page of 2026-08-28 already shows Contact Us in place of the sign-up button, and the sign-up host app.geolocated.io answers HTTP 522 on 2026-11-02.
- notes: Free requests: 2,000 a day at 100 a minute on the Hobby plan, which no new account can reach because sign-up is not offered. Rate limit: 100 requests a minute (HTTP 429 RateLimitExceeded). Bulk path: batch lookup, 25 addresses a request, on Growth and Scale only; none on Hobby.
- evidence note: The pricing, documentation, privacy and archived pages were read on 2026-11-02, and the Sunset header and the HTTP 522 answers were measured. No API request was made: the API server host names are not published on the pages that could be read. A sign-up host that answers again would reopen the verdict.
- extras:
  - death.on: 2026-11-02
  - death.cause: registration-closed
  - bulk_path: batch lookup, 25 addresses a request, Growth and Scale only
  - free_requests: 2,000 a day
- evidence:
  - [1] 2026-11-02: the Hobby plan is listed at USD 0 a month | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: ### Hobby ## $0 /Month
  - [1] 2026-11-02: the free tier needs no credit card | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: Start on our FREE tier & upgrade as you scale. No credit card required.
  - [1] 2026-11-02: Hobby allows 2,000 requests a day, Starter 50,000 | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: | Requests / day | | | | | 2000 | 50K | 150K | 350K |
  - [1] 2026-11-02: Hobby is limited to 100 requests a minute, Starter to 800 | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: | Rate Limit | | | | | 100 / minute | 800 / minute | None | None |
  - [1] 2026-11-02: the API servers are in the US and Asia on every plan | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: | API Server Location | | | | | US, Asia | US, Asia | US, Asia | US, Asia |
  - [1] 2026-11-02: Hobby and Starter return the Essentials data, Growth and Scale the Advanced data | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: | Geolocation Data | | | | | Essentials | Essentials | Advanced | Advanced |
  - [1] 2026-11-02: Starter is listed at USD 25 a month | capture: sha256:12eb92455af0c868c58846dcad29b8803e358996f525bea7bc5f2c5011e488de | quote: ### Starter ## $25 /Month
  - [1] 2026-11-02: the Self IP Lookup row of the plan table is crossed out for Hobby and ticked for Starter | capture: sha256:fbdb035216e45fd9e4f03ac3010b38ea1381c2fe1d9137d3caf271357ccea986 | quote: <td class="ps-0" colspan="5">Self IP Lookup</td><td class="ps-0"><i class="fe fe-x fs-3 text-muted"></i></td><td class="ps-0"><i class="fe fe-check fs-3 text-success"></i></td>
  - [1] 2026-11-02: the Batch IP Lookup row is crossed out for Hobby and Starter and ticked from Growth | capture: sha256:fbdb035216e45fd9e4f03ac3010b38ea1381c2fe1d9137d3caf271357ccea986 | quote: <td class="ps-0" colspan="5">Batch IP Lookup</td><td class="ps-0"><i class="fe fe-x fs-3 text-muted"></i></td><td class="ps-0"><i class="fe fe-x fs-3 text-muted"></i></td><td class="ps-0"><i class="fe fe-check fs-3 text-success"></i></td>
  - [2] 2026-11-02: the batch lookup takes at most 25 addresses a request | capture: sha256:a9d2caf09e1bc86c171b333d63e6583ca4ed1dd6dc6a9fa691ed9d5d5ccd17fc | quote: The request must contain a JSON array of IP addresses. A maximum of 25 addresses per request is allowed.
  - [3] 2026-11-02: past the daily quota requests are blocked until the reset time | capture: sha256:35ac156b98561c41dbe14cec658d6cc0872b72c9b8825aa8be24604749e75f62 | quote: Upon reaching this daily limit, further requests will be blocked until the reset time.
  - [4] 2026-11-02: the per-minute limit is answered HTTP 429 RateLimitExceeded | capture: sha256:0cb7a93e1bb6ffb34049879e22a778cfdde8a278a423359d562ebb63607d8951 | quote: | 429 | RateLimitExceeded | The request rate limit for your current subscription level has been exceeded. Please wait before making additional requests or consider upgrading to a plan with a higher or unlimited request quota. |
  - [4] 2026-11-02: the daily quota is answered HTTP 429 DailyLimitExceeded | capture: sha256:0cb7a93e1bb6ffb34049879e22a778cfdde8a278a423359d562ebb63607d8951 | quote: | 429 | DailyLimitExceeded | The daily request quota for your current subscription level has been reached. Please wait until the limit resets or consider upgrading to a plan with a higher or unlimited daily quota. |
  - [5] 2026-11-02: every request needs an API key | capture: sha256:5764098ae564da9f563572678c657cd9d017c72c59b68b6b0f071c291f0b8619 | quote: Geolocated.io APIs require an API key for all requests.
  - [6] 2026-11-02: sign-up collected a name, an email address, a business name and a country | capture: sha256:4fd154c2609e38dc3a6a3cd3357476e76bee18a2e9af9433072949a81961b757 | quote: When you sign up on the Site, we collect certain information, including your name, email address, business name and the country of origin.
  - [7] 2026-11-02: the app answered on 2026-08-28 with an email-code sign-in | capture: sha256:f895ca490a7bae494a04ce48190a17965b0cd9078c4c6c0d69a7caf8f905aa99 | quote: Send new code
  - [8] 2026-11-02: the archived home page of 2026-07-09 linked a Get Started For Free button to app.geolocated.io/signup | capture: sha256:c37203c3287629412132fef4c58d3222462a1cdfbf8e777e4b1581a6a1d88453 | quote: [Get Started For Free](https://web.archive.org/web/20260709185334/https://app.geolocated.io/signup)
  - [9] 2026-11-02: the archived home page of 2026-08-28 ends with a Contact Us Now button where the 2026-07-09 copy had a sign-up button | capture: sha256:c71fa9b6d0d8d637f6506b4d484690f8ef31e1a31a61832f5567dcdf834951fc | quote: Contact Us Now
  - [10] 2026-11-02: the home page served on 2026-11-02 ends with a Contact Us Now button | capture: sha256:5791b2de8cd3774013b9f290af9ba1f145361e861f5cc2746623d3320b0ef3fc | quote: Contact Us Now
  - probe:https://geolocated.io/pricing.html 2026-11-02: the pricing page is served with a Sunset header dated 2026-08-31 | capture: sha256:62b1ff7c24d3c4bd1d51a945d12ed6b0b015b3264c511465f03bce46708eada8 | quote: "sunset": "Mon, 31 Aug 2026 23:59:59 GMT"
  - [10] 2026-11-02: the home page is served with the same Sunset header | capture: sha256:5791b2de8cd3774013b9f290af9ba1f145361e861f5cc2746623d3320b0ef3fc | quote: sunset: Mon, 31 Aug 2026 23:59:59 GMT
  - [1] 2026-11-02: the pricing page response read through a fetch carries the same Sunset header | capture: sha256:fbdb035216e45fd9e4f03ac3010b38ea1381c2fe1d9137d3caf271357ccea986 | quote: sunset: Mon, 31 Aug 2026 23:59:59 GMT
  - probe:https://app.geolocated.io/ 2026-11-02: the app host answered HTTP 522, an origin that does not respond, on 2026-11-02 | capture: sha256:ee61d89904157d7f401c1ffda6aa5404ed4b3f326e150bb707d38ef39c3c26d4 | quote: "status": 522
  - probe:https://app.geolocated.io/signup 2026-11-02: the sign-up page answered HTTP 522 on 2026-11-02 | capture: sha256:121615ebf9e744044995f7db666e705d6c3af1fa2588d4215d3ed44f671f27f0 | quote: "status": 522
- sources:
  - [1] https://geolocated.io/pricing.html
  - [2] https://geolocated.io/docs/lookup-batch.html
  - [3] https://geolocated.io/docs/limits.html
  - [4] https://geolocated.io/docs/errors.html
  - [5] https://geolocated.io/docs/authentication.html
  - [6] https://geolocated.io/privacy-policy.html
  - [7] https://web.archive.org/web/20260828130617/https://app.geolocated.io/login
  - [8] https://web.archive.org/web/20260709185334/https://geolocated.io/
  - [9] https://web.archive.org/web/20260828130604/https://geolocated.io/
  - [10] https://geolocated.io/
