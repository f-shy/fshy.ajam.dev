# The IP API

> theipapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/theipapi/ | JSON https://fshy.ajam.dev/api/v1/entity/theipapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## The IP API (theipapi.com)

- `data-apis/theipapi` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.118Z (live) | stale on 2026-12-04
- url https://theipapi.com/pricing
- free tier: Free plan: 1,000 requests a day, geolocation and ASN with company data, daily data updates | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: Beginner is USD 19 a month for 600,000 requests a month
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: email and password, or Google sign-in
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a day [1]
- limits note: unverified: behind a sign-up: the response headers of a keyed lookup, which the documentation does not list
- tooling: any HTTP client
- composes with: 1,000 keyed lookups a day with ASN and company data. Bulk path: POST /v1/ip/batch with up to 100 IPs per request, each unique IP counting as one request against the quota; the documentation names no plan restriction for it
- reliability: no email support on the free plan
- notes: Free requests: 1,000 a day. Rate limit: 1,000 requests a day on the free plan, reset daily; a request past the limit answers HTTP 429. The documentation advises caching results. Bulk path: POST /v1/ip/batch with up to 100 IPs per request.
- evidence note: the pricing and signup pages were quoted on 2026-10-30 and 2026-10-31; no keyed lookup was made.
- extras:
  - bulk_path: POST /v1/ip/batch, up to 100 IPs per request
  - free_requests: 1,000 a day
- evidence:
  - [1] 2026-10-30: the free plan is 1,000 requests a day | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1 | quote: 1,000 req / day
  - [1] 2026-10-30: the free plan has no end date | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1 | quote: $0/ forever
  - [1] 2026-10-30: data updates daily | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1
  - [1] 2026-10-30: Beginner is USD 19 a month | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1 | quote: $19/ month
  - [1] 2026-10-30: Beginner is 600,000 requests a month | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1 | quote: 600,000 req / month
  - [2] 2026-10-31: the signup form asks an email | capture: sha256:60688ed006262e0396bbfd8919709626bd98e4a3e264886508f2aa19581249ae | quote: Your Email
  - [2] 2026-10-31: Google sign-in is offered | capture: sha256:60688ed006262e0396bbfd8919709626bd98e4a3e264886508f2aa19581249ae | quote: [Sign up with Google](https://theipapi.com/auth/google)
  - [3] 2026-11-02: the documentation lists POST /v1/ip/batch with up to 100 IPs per request, each unique IP counting as one request against the quota, and names no plan restriction for it | capture: sha256:43a94509f9a1542dda46b01029af3fcb593067e852854318a41f0fda464bbb1b | quote: Up to 100 IPs per request. Each unique IP counts as one request against your API quota.
  - [3] 2026-11-02: the documentation lists POST /v1/ip/batch with up to 100 IPs per request | capture: sha256:43a94509f9a1542dda46b01029af3fcb593067e852854318a41f0fda464bbb1b | quote: Up to 100 IPs per request. Each unique IP counts as one request against your API quota.
  - [3] 2026-11-02: the documentation states that rate limits reset daily for the free plan, lists HTTP 429 for a request past the limit, and lists the batch endpoint with up to 100 IPs per request | capture: sha256:43a94509f9a1542dda46b01029af3fcb593067e852854318a41f0fda464bbb1b | quote: Rate limits reset daily for the Free plan and monthly for paid plans.
  - probe:https://api.theipapi.com/v1/ip/8.8.8.8 2026-11-02: a lookup with no API key answered HTTP 401 with the error No API Key Provided, so a keyed answer and its headers show only after sign-up | capture: sha256:e1397cc09b6d3c3e39ddfb778467e4b4da75dda946c8ac965e8fadf58a3a92c2 | quote: "status": 401
  - [4] 2026-11-02: after sign-up the account email is confirmed to receive the API key | capture: sha256:d50e0d83c8e9d62879574cb8e3413b226f3161d378373366b8ec8b3c28f0d7c9 | quote: 2. Confirm your email to receive your API key
  - [1] 2026-11-02:  | capture: sha256:d20554da3343c96c9ab10f7210a12da6cac71fd3ce4ab5fd025ffcd982143dd1 | quote: 1,000 req / day
- sources:
  - [1] https://theipapi.com/pricing
  - [2] https://theipapi.com/signup
  - [3] https://theipapi.com/documentation
  - [4] https://theipapi.com/llms.txt
