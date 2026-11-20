# LocationIQ

> locationiq.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/locationiq/ | JSON https://fshy.ajam.dev/api/v1/entity/locationiq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LocationIQ

- `data-apis/locationiq` | qualifies | evidence documented | binding volume-quota | category geocoding, routing and maps API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:28:26.711Z (live) | stale on 2026-12-04
- url https://locationiq.com/pricing
- free tier: 5000 requests a day at 2 requests a second and 60 requests a minute, across the Geocoding, Routing and Street and Static Maps APIs, with 2 access tokens | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: the next plan, Developer, is USD 100 a month for 25,000 requests a day at 20 requests a second; the terms call the free account a trial that may be charged for later; a routing request is counted like the other APIs, one successful response consuming one request
- per-object cap: no batch endpoint: one address or coordinate a request; bulk work is sent as concurrent requests within the plan's per-second rate | source: [2]
- retention: source: [3]
- egress: not applicable: a query API metered in requests, not bytes | metered: no | source: [1]
- identity: email | detail: an account at my.locationiq.com with a work email, a full name and a use case, or Google sign-in; the form has no card field and carries a Google reCAPTCHA check. Whether a free-mail address passes as a work email is unverified: behind a sign-up (the email field is a required email-type input)
- interface: rest
- limits:
  - volume-quota (binding): 5000 requests a day on the Free plan [1]
  - request-rate: 2 requests a second and 60 requests a minute on the Free plan [1]
  - retention-clamped: request-response pairs cached for up to 48 hours on a free account; response data itself may be stored with no limit [3]
- binding note: 2 requests a second and 60 a minute allow more than 5000 requests in a day, so the daily quota is met first
- interface detail: HTTPS to us1.locationiq.com/v1/search with an API access token (prefix pk.), served from US and EU datacenters; a request with no valid key answers HTTP 401 {"error":"Invalid key"}; a request over a per-second, per-minute or daily limit answers HTTP 429
- endpoint: https://us1.locationiq.com/v1/search
- tooling: any HTTP client
- composes with: 5000 storable geocodes, reverse geocodes or routes a day on an email account with no card; bulk geocoding is sent as concurrent single requests at up to 2 a second, since no batch endpoint exists
- reliability: a request over the per-second, per-minute or daily limit answers HTTP 429; the free account is described as a trial that may be charged for later; an IP address that makes several sign-ups in a short time can be blocked with Error 1006 Access Denied
- notes: Bulk path: none; no batch endpoint, so addresses go as concurrent single requests at up to 2 a second.
- evidence note: the pricing page, the terms, the geocoding page, the errors and authentication docs and the sign-up page were quoted on 2026-10-31; a keyless search answered HTTP 401. No account was opened, so no keyed request was made; one would move it to measured.
- extras:
  - bulk_path: none: no batch endpoint; concurrent single requests within 2 a second
- evidence:
  - [1] 2026-10-31: the Free plan gives 5000 requests a day | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 5000 requests /day
  - [1] 2026-10-31: the Free plan rate is 2 requests a second | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 2 requests /second
  - [1] 2026-10-31: the Free plan is also capped at 60 requests a minute | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 60 requests per minute
  - [1] 2026-10-31:  | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: You can use our free plan in commercial projects if you spread the love by adding a prominent link back to us on your website or app
  - [1] 2026-10-31: the Free plan has 2 access tokens | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 2 Access Tokens
  - [1] 2026-10-31: the service runs from US and EU datacenters | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: US & EU Datacenters
  - [1] 2026-10-31: the Developer plan gives 25,000 requests a day | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 25,000 requests /day
  - [1] 2026-10-31: the Developer plan is USD 100 billed monthly | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: $100
  - [1] 2026-10-31: the Developer plan rate is 20 requests a second | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 20 requests /second
  - [2] 2026-10-31: geocoding is part of the free 5000 requests a day | capture: sha256:e637c74e1c5eaaa5191e9815132813ed60b86d2428f04150fd9d6754e0b1c7ce | quote: Yes, Geocoding is free. LocationIQ offers 5000 requests/day as a part of the free plan.
  - [2] 2026-10-31: bulk geocoding is done by concurrent single requests, not a batch endpoint | capture: sha256:e637c74e1c5eaaa5191e9815132813ed60b86d2428f04150fd9d6754e0b1c7ce | quote: you can send multiple addresses/ coordinates concurrently.
  - [2] 2026-10-31: concurrency on the free plan is bounded by 2 calls a second | capture: sha256:e637c74e1c5eaaa5191e9815132813ed60b86d2428f04150fd9d6754e0b1c7ce | quote: The free plan allows you to query upto 2 API calls per second
  - [3] 2026-10-31: a free account may cache request-response pairs for up to 48 hours | capture: sha256:ee0abea76758fab101869f3fa146b50c6a6fa74d6037f628ce5a6fcb86d6d622
  - [3] 2026-10-31:  | capture: sha256:ee0abea76758fab101869f3fa146b50c6a6fa74d6037f628ce5a6fcb86d6d622
  - [3] 2026-10-31: the free account is a trial that may be charged for later | capture: sha256:ee0abea76758fab101869f3fa146b50c6a6fa74d6037f628ce5a6fcb86d6d622 | quote: A trial account of the API is currently provided for free, but LocationIQ reserves the right to charge for the API
  - [4] 2026-10-31: the daily quota is enforced with HTTP 429 | capture: sha256:9f368f80525697409e7d37a8a42a704981b730b4cafcc9f94a78c139e4a74753 | quote: Request exceeded a daily limit: your account's quota
  - [4] 2026-10-31: the per-second limit is enforced with HTTP 429 | capture: sha256:9f368f80525697409e7d37a8a42a704981b730b4cafcc9f94a78c139e4a74753 | quote: Request exceeded a per-second limit: your account's plan limit
  - [5] 2026-10-31: product APIs are called with a pk. API token | capture: sha256:d8b1b4a10eb6910d999d9b448aa63718912330204efe4028923c90afa685b46e | quote: API token (prefix `pk.`) — Calls product APIs such as Geocoding, Routing and Maps.
  - [6] 2026-10-31: the sign-up form asks for a work email | capture: sha256:142cdc2779c3ca3263a3bbe9431a1622f8006937c362d0e8490b7a164cfa6aee | quote: Work email
  - [6] 2026-10-31: the sign-up form asks for a full name | capture: sha256:142cdc2779c3ca3263a3bbe9431a1622f8006937c362d0e8490b7a164cfa6aee | quote: Full name
  - [6] 2026-10-31: the sign-up form asks for a use case | capture: sha256:142cdc2779c3ca3263a3bbe9431a1622f8006937c362d0e8490b7a164cfa6aee | quote: Use Case Select your use case
  - [6] 2026-10-31: Google sign-in is offered | capture: sha256:142cdc2779c3ca3263a3bbe9431a1622f8006937c362d0e8490b7a164cfa6aee | quote: [Sign up with Google](https://my.locationiq.com/register?o=g)
  - probe:https://us1.locationiq.com/v1/search?q=Zurich&format=json 2026-10-31: the search endpoint answers HTTP 401 to a keyless request | capture: sha256:6ea80306e4da82c5ef497cd5482eb90c7453fc4455b7a70dab620a94b29ddeb9 | quote: "status": 401
  - probe:https://us1.locationiq.com/v1/search?q=Zurich&format=json#body 2026-10-31: the search endpoint refuses a request with no valid key | capture: sha256:b4b42b7bb0a7e0c0958f53a398246bc2199ccdaa515a8fdc38f63b7263648108 | quote: {"error":"Invalid key"}
  - [6] 2026-11-02: the sign-up form has a required email-type input and a reCAPTCHA widget | capture: sha256:5d18f485f428005ab2ffe3de3e0e82c9b6dcfbd2bb4570b612a25b9b9f3c9a90 | quote: type="email" name="SignupForm[email]" id="SignupForm_email" required ... <div class="g-recaptcha"
  - [7] 2026-11-02: a routing request counts like any other: 1 successful response is 1 request consumed | capture: sha256:1e28a2462e4066c4f1f936267a8bc8a36a5b1f425505f2b209afadcad5b6f9d0 | quote: Our routing API calculates the request like the other APIs. 1 successful response = 1 request consumed
  - [8] 2026-11-02: several sign-ups from one IP address in a short time can be blocked with Error 1006 Access Denied | capture: sha256:7f50694efc1948a3032a9ed52194e3a8ab49ae1e6d0690049ca186aa7a55a987 | quote: This might mean that your IP address got blocked due to multiple signups in a small period of time.
  - [9] 2026-11-02: registration sends a verification link to the email address given | capture: sha256:b8c16f7361d46ff153490c61412387209ff7f2607604479651c143b7fead219e | quote: Check your email inbox for a verification link sent to the provided email address during registration.
  - [1] 2026-11-02: the Free plan gives 5000 requests a day | capture: sha256:111b6310a2be4cd6d86a985d610a1b991c7ebe811c0af56943277221f49f9090 | quote: 5000 requests /day
  - [6] 2026-11-02: the sign-up form asks for an email | capture: sha256:5d18f485f428005ab2ffe3de3e0e82c9b6dcfbd2bb4570b612a25b9b9f3c9a90 | quote: <label class="ui-label" for="SignupForm_email">Work email</label>
  - [3] 2026-11-02: a free account may cache request-response pairs for up to 48 hours | capture: sha256:ee0abea76758fab101869f3fa146b50c6a6fa74d6037f628ce5a6fcb86d6d622
  - probe:https://us1.locationiq.com/v1/search?q=Zurich&format=json#body 2026-11-02: a keyless search request is refused with an invalid-key error | capture: sha256:b4b42b7bb0a7e0c0958f53a398246bc2199ccdaa515a8fdc38f63b7263648108 | quote: {"error":"Invalid key"}
- sources:
  - [1] https://locationiq.com/pricing
  - [2] https://locationiq.com/geocoding
  - [3] https://locationiq.com/tos
  - [4] https://docs.locationiq.com/docs/errors
  - [5] https://docs.locationiq.com/docs/authentication
  - [6] https://my.locationiq.com/register
  - [7] https://help.locationiq.com/support/solutions/articles/36000216101-how-are-requests-counted-under-routing-api-
  - [8] https://help.locationiq.com/support/solutions/articles/36000216091-what-is-the-meaning-of-the-error-1006-access-denied-
  - [9] https://docs.locationiq.com/docs/locationiq-access-token
