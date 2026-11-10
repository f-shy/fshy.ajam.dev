# Geokeo

> geokeo.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geokeo/ | JSON https://fshy.ajam.dev/api/v1/entity/geokeo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Geokeo

- `data-apis/geokeo` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://geokeo.com/pricing.php
- free tier: Free plan, USD 0 a month: 2,500 api requests daily for forward and reverse geocoding; the daily limit refreshes at midnight UTC, and sign-up needs no credit card | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: no hard limit is set: responses are throttled if requests are more than 30% of the allowed quota daily
- per-object cap: one query a request: the q parameter takes up to 50 characters; no batch endpoint is documented | source: [2]
- retention: the service does not store query requests | source: [2]
- egress: not applicable: a query API metered in requests, not bytes | metered: no | source: [1]
- identity: email | detail: an account at geokeo.com/signup.php with a name, an email address, a password and a CAPTCHA; the home page says to sign up without any credit card; the service stores the email address, billing address and name
- interface: rest
- limits:
  - volume-quota (binding): 2,500 api requests a day on the Free plan, refreshed at midnight UTC [2]
  - request-rate: no hard limit is set; responses are throttled if requests are more than 30% of allowed quota daily [2]
  - per-object-cap: the q parameter is limited to 50 characters, one query a request [2]
- binding note: no per-second limit is published, so the stated 2,500-request day is the ceiling that is met first
- interface detail: HTTPS GET to geokeo.com/geocode/v1/search.php (q and api parameters) for forward and /geocode/v1/reverse.php (lat, lng and api) for reverse geocoding, JSON or XML; a keyless call answered HTTP 200 with the JSON status INVALID_REQUEST, so the status field carries the error, not the HTTP code
- endpoint: https://geokeo.com/geocode/v1/search.php
- tooling: any HTTP client
- composes with: 2,500 storable forward or reverse geocodes a day on a name, email and password account with no card, built from OpenStreetMap, GeoNames and Natural Earth data; one query per request, so bulk work is sent as many single requests
- reliability: a request over the allowance is throttled rather than refused; an application error such as INVALID_REQUEST comes back with HTTP 200, so the JSON status field must be read
- notes: Free requests: 2,500 a day. Rate limit: no hard limit, throttled above the quota. Bulk path: none; single forward and reverse queries only.
- evidence note: the pricing page, the documentation, the sign-up page and the home page were quoted on 2026-11-02; a keyless call answered HTTP 200 with the JSON status INVALID_REQUEST. No account was opened, so the free daily allowance was not exercised.
- extras:
  - free_requests: 2,500 api requests a day, refreshed at midnight UTC
  - rate_limit: no hard limit; throttled if requests are more than 30% of allowed quota daily
  - bulk_path: none documented; one forward or reverse query a request
- evidence:
  - [1] 2026-11-02: the Free plan costs USD 0 a month and lists 2,500 api requests daily | capture: sha256:1363577a3774ce16dbc8a2332106a43188addb749fdeddb2391551de85f7b745 | quote: #### Free # $0/mo - 2,500 api requests daily
  - [3] 2026-11-02: sign-up needs no credit card and gives 2500 free api requests daily | capture: sha256:b0bedffbde344a70380d07ede1e96af69406c02c6affc352cff3847385da4f2b | quote: Sign up without any credit card and get 2500 free api requests daily.
  - [2] 2026-11-02: the free daily limit of 2500 refreshes at midnight UTC | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: The free plan has daily 2500 api limit which refresh at midnight(24:00) UTC.
  - [2] 2026-11-02: no hard limit is set; responses are throttled above the quota | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: Hard limits are not set but responses are throttled if requests are more than 30% of allowed quota daily.
  - [2] 2026-11-02:  | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab
  - [2] 2026-11-02: the service does not store query requests | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: The query requests are not stored.
  - [2] 2026-11-02: the q parameter takes up to 50 characters | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: Your query can be a 50 character limit word for example- Empire state building
  - [2] 2026-11-02: the forward geocoding endpoint takes q and api parameters | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: https://geokeo.com/geocode/v1/search.php?q=empire+state+building&api=YOUR_API_KEY
  - [2] 2026-11-02: the reverse geocoding endpoint takes lat, lng and api parameters | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: https://geokeo.com/geocode/v1/reverse.php?lat=40.74842&lng=-73.9856&api=YOUR_API_KEY
  - [2] 2026-11-02: answers are JSON or XML | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: Format can be either json or xml.default is json
  - [2] 2026-11-02: the service stores the email address, billing address and name of customers | capture: sha256:0057edfb6cf3f833c2cd2d7f38675df5760a96549004c9efb54958123b5775ab | quote: Email address, billing address, name of the customers are stored
  - [4] 2026-11-02: the sign-up form asks for a name, an email address and a password | capture: sha256:24e1065b32f35392b99f9e7ec70879e66fd224426acc06afb8b664f70d0187b5 | quote: Name Email Password
  - [4] 2026-11-02: the sign-up form includes a CAPTCHA | capture: sha256:24e1065b32f35392b99f9e7ec70879e66fd224426acc06afb8b664f70d0187b5 | quote: CAPTCHA Refresh
  - [3] 2026-11-02: results are built from OpenStreetMap, GeoNames and Natural Earth data | capture: sha256:b0bedffbde344a70380d07ede1e96af69406c02c6affc352cff3847385da4f2b | quote: Geokeo is developed from open source data available from various sources like- openstreetmap, geonames, natural earth etc
  - probe:https://geokeo.com/geocode/v1/search.php?q=empire+state+building 2026-11-02: a keyless call answers HTTP 200 | capture: sha256:e3ab557059f4988f132e114ae678972d4467a42356540c414496661b0173e33a | quote: "status": 200
  - probe:https://geokeo.com/geocode/v1/search.php?q=empire+state+building#body 2026-11-02: the HTTP 200 body carries the application status INVALID_REQUEST | capture: sha256:ead05d969af8b30a873e3a673a1d582a30661130d4335b00f0cf98bb8aa077f2 | quote: "status": "INVALID_REQUEST"
- sources:
  - [1] https://geokeo.com/pricing.php
  - [2] https://geokeo.com/documentation.php
  - [3] https://geokeo.com/
  - [4] https://geokeo.com/signup.php
