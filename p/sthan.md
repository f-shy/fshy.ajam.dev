# sthan.io IP Geolocation

> sthan.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sthan/ | JSON https://fshy.ajam.dev/api/v1/entity/sthan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sthan.io IP Geolocation

- `data-apis/sthan-io-ip-geolocation` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://sthan.io/pricing/global
- free tier: Free plan, USD 0 a month: 50,000 requests a month, up to 5,000 a day and at most 2,000 a minute, one IP lookup per request, no credit card | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Basic is USD 4.50 a month for 100,000 lookups, Starter USD 32 for 1,000,000 and Business USD 120 for 5,000,000; usage notices at 80% and 100%.
- per-object cap: single IP lookup per request | source: [1]
- retention: not applicable: a lookup API | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: email | detail: an email address, verified before the key works, or GitHub or Google sign-in; no credit card
- interface: rest
- limits:
  - volume-quota (binding): 50,000 requests a month and 5,000 a day on the Free plan [1]
  - request-rate: 2,000 requests a minute on the Free plan; HTTP 429 with Retry-After past a limit [2]
  - per-object-cap: one IP lookup per request [1]
- binding note: the daily count of 5,000 requests is met before the monthly 50,000 or the 2,000 a minute rate.
- interface detail: GET https://api.sthan.io/IpGeolocation/{ip} with an Authorization: Bearer key answers JSON; an omitted IP geolocates the caller; every answer carries X-RateLimit-ByEndpoint-Per{Minute|Hour|Day|Month} headers and the remaining counts
- endpoint: part of interface detail
- tooling: any HTTP client; a 429 answer carries Retry-After and an Errors list naming the limit reached
- composes with: 50,000 lookups a month with city, postal code, timezone, ASN, ISP and proxy and hosting flags from one email sign-up. Bulk path: none; single IP lookup per request.
- reliability: at a limit the API answers HTTP 429 Too Many Requests with Retry-After and an Errors list; a keyless call answered HTTP 401
- notes: Free requests: 50,000 a month, 5,000 a day. Rate limit: 2,000 a minute; HTTP 429 with Retry-After. Bulk path: none; single IP lookup per request.
- evidence note: The pricing, product, documentation and sign-up pages were quoted on 2026-11-02 and a keyless call answered HTTP 401; no keyed lookup was made, so the limits are the vendor's.
- extras:
  - bulk_path: none
  - free_requests: 50,000 a month, 5,000 a day
- evidence:
  - [1] 2026-11-02: the Free plan is 50,000 requests a month | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: 50,000 requests / month
  - [1] 2026-11-02: the Free plan costs USD 0 a month | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: $ 0 / month
  - [1] 2026-11-02: no credit card and up to 5,000 requests a day | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: - No credit card required. Up to 5,000 requests a day.
  - [1] 2026-11-02: the Free plan is capped at 2,000 requests a minute | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: - Max. 2000 requests / minute.
  - [1] 2026-11-02: one IP per request | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: - Single IP lookup per request.
  - [1] 2026-11-02: usage notices at 80% and 100% | capture: sha256:cd38d0d9641ddc24a9597666bddf4ab4a3e1173b28d9171d4c60ceab3ad414bf | quote: We notify you at 80% and 100% usage.
  - [3] 2026-11-02: the Basic plan costs USD 4.50 a month | capture: sha256:75ebfebe51eb55ac64cc4dd3ea87c63e8531665b27dad99cdf66e52c0838658c | quote: $4.50 /mo
  - [3] 2026-11-02: an email address is all the sign-up needs and no card is on file | capture: sha256:75ebfebe51eb55ac64cc4dd3ea87c63e8531665b27dad99cdf66e52c0838658c | quote: An email address. Sign up, grab your API key, and send your first request. The free tier gives you 50,000 lookups a month with no card on file.
  - [3] 2026-11-02: an omitted IP geolocates the caller | capture: sha256:75ebfebe51eb55ac64cc4dd3ea87c63e8531665b27dad99cdf66e52c0838658c | quote: send no IP and it geolocates the request's own address.
  - [2] 2026-11-02: the IP Geolocation limits per plan: Free is 50,000 a month, 5,000 a day, 2,000 a minute | capture: sha256:325e910a4c3b4f31c03a1013a4013287c40cc0e99164a769fb17b9b3b92726d6 | quote: | IP Geolocation | 50,000 / mo 5,000 / day 2,000 / min | 100,000 / mo 4,000 / min | 1,000,000 / mo 40,000 / min | 5,000,000 / mo 200,000 / min |
  - [2] 2026-11-02: past a limit the API answers HTTP 429 with Retry-After | capture: sha256:325e910a4c3b4f31c03a1013a4013287c40cc0e99164a769fb17b9b3b92726d6 | quote: When you exceed your limit, the API returns `429 Too Many Requests`. The `Retry-After` header gives the number of seconds until you can retry
  - [4] 2026-11-02: the key is ready after the email is verified; no credit card | capture: sha256:9258ca3700da75a24f2efdb2f932a4eddaf60a81a4b9bef67dccc341ab1a2249 | quote: Free tier, no credit card. Your API key is ready as soon as you verify your email.
  - [4] 2026-11-02: GitHub, Google or email sign-in is offered | capture: sha256:9258ca3700da75a24f2efdb2f932a4eddaf60a81a4b9bef67dccc341ab1a2249 | quote: By continuing with GitHub, Google, or email, you agree to our
  - probe:https://api.sthan.io/IpGeolocation/8.8.8.8 2026-11-02: a keyless GET of /IpGeolocation/8.8.8.8 answered HTTP 401 | capture: sha256:29077c6a3c33502898605ed308f0e6f05d0f3df22d42258c932abfa1e9f90d0c | quote: "status": 401
- sources:
  - [1] https://sthan.io/pricing/global
  - [2] https://sthan.io/docs
  - [3] https://sthan.io/products/ip-geolocation
  - [4] https://sthan.io/signup
