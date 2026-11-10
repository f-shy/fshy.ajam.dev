# GraphHopper Directions API

> graphhopper.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/graphhopper/ | JSON https://fshy.ajam.dev/api/v1/entity/graphhopper.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GraphHopper Directions API

- `data-apis/graphhopper` | qualifies-with-caveat | evidence documented | binding volume-quota | category routing, geocoding and route optimization API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://www.graphhopper.com/pricing/
- free tier: Free plan, EUR 0 a month,: 500 credits per day with 5 locations a routing request; a geocoding request costs 0.3 credit on the default provider and 0.9 credit on nominatim or opencagedata, so 500 credits cover about 1,666 default-provider geocodes a day (500 / 0.3) | unit: credits | metered on: request-count | read on: 2026-11-02 | source: [1] | note: credits are shared with the routing, matrix, isochrone and optimization APIs; the Free plan has a limited credit count per minute and carries no guarantees
- per-object cap: no batch geocoding endpoint: one query a GET request; 5 locations a routing request on the Free plan | source: [1]
- retention: source: [2]
- egress: not applicable: a query API metered in credits, not bytes | metered: no | source: [1]
- identity: email | detail: an account at graphhopper.com/dashboard/signup with a first name, last name, email, password, company and country and a terms checkbox; GraphHopper activates the access and notifies the subscriber by email; the pricing page says no credit card is required
- interface: rest
- limits:
  - volume-quota (binding): 500 credits a day on the Free plan; a geocoding request costs 0.3 credit (default) or 0.9 credit (nominatim, opencagedata) [3]
  - request-rate: a limited credit count per minute on the Free plan, size not published; HTTP 429 answers when the daily or per-minute limit is exhausted [4]
  - per-object-cap: 5 locations a request on the Free plan (routing) [1]
- binding note: the per-minute credit limit of the Free plan is not published, so the 500-credit day is the figure that binds
- interface detail: HTTPS GET to graphhopper.com/api/1/geocode (q, locale, limit, reverse, point and provider parameters) with the key as a query parameter; a keyless call answered HTTP 401 No API key specified; the provider parameter is under development and can fall back to the default at any time
- endpoint: https://graphhopper.com/api/1/geocode
- tooling: any HTTP client
- composes with: 500 credits a day, about 1,666 default-provider geocodes, on a non-commercial email account with no card, shared with routing and optimization calls
- reliability: the Free plan carries no guarantees; past the daily or per-minute limit the API answers HTTP 429; the provider parameter can fall back to the default at any time
- notes: Free requests: 500 credits a day, about 1,666 default-provider geocodes (500 / 0.3). Rate limit: a limited credit count per minute, size not published. Bulk path: none; no batch geocoding endpoint.
- evidence note: the pricing page, the credit FAQ, the OpenAPI docs, the terms, the per-minute limit article and the sign-up page were quoted on 2026-11-02; a keyless geocode answered HTTP 401. No account was opened, so the free daily credits and the per-minute limit of the Free plan were not exercised.
- extras:
  - free_requests: 500 credits a day; 0.3 credit per default geocode, 0.9 per nominatim or opencagedata geocode
  - rate_limit: unverified: a per-minute credit limit exists on the Free plan, size not published
  - bulk_path: none: no batch geocoding endpoint
- evidence:
  - [1] 2026-11-02: the Free plan costs 0 euro a month and gives 500 credits per day and 5 locations a request | capture: sha256:b686e087a5ce1bda6474a688aa24ef1ca4057e3de50c7380f56ae4dbc0fff7af | quote: Free Price per month 1 0€ 2 Credits per day 3,4 500 per day Max. locations per request 5 locations
  - [1] 2026-11-02: the free plan starts with no credit card | capture: sha256:b686e087a5ce1bda6474a688aa24ef1ca4057e3de50c7380f56ae4dbc0fff7af | quote: Launch today with our free plan. No credit card required.
  - [1] 2026-11-02:  | capture: sha256:b686e087a5ce1bda6474a688aa24ef1ca4057e3de50c7380f56ae4dbc0fff7af | quote: It has a limited credit count per minute, a limited set of vehicle profiles and cannot use the flexible mode (ch.disable=true).
  - [1] 2026-11-02: the Free plan carries no guarantees | capture: sha256:b686e087a5ce1bda6474a688aa24ef1ca4057e3de50c7380f56ae4dbc0fff7af | quote: The Free Plan does not include any guarantees.
  - [3] 2026-11-02: geocoding credit costs differ by provider | capture: sha256:a2fcd8b7c4ef354463897518a1b98a568a0937c8643de2ab39d892c1328f0d71 | quote: For the Geocoding API we have integrated different providers. Each provider has its own prices.
  - [3] 2026-11-02: a default-provider geocoding request costs 0.3 credit | capture: sha256:a2fcd8b7c4ef354463897518a1b98a568a0937c8643de2ab39d892c1328f0d71 | quote: default: 0.3 credits
  - [3] 2026-11-02: a nominatim-provider geocoding request costs 0.9 credit | capture: sha256:a2fcd8b7c4ef354463897518a1b98a568a0937c8643de2ab39d892c1328f0d71 | quote: nominatim: 0.9 credits
  - [3] 2026-11-02: an opencagedata-provider geocoding request costs 0.9 credit | capture: sha256:a2fcd8b7c4ef354463897518a1b98a568a0937c8643de2ab39d892c1328f0d71 | quote: opencagedata: 0.9 credits
  - [3] 2026-11-02: credits are one currency across the Directions API products | capture: sha256:a2fcd8b7c4ef354463897518a1b98a568a0937c8643de2ab39d892c1328f0d71 | quote: Credits are GraphHopper’s currency and can be spent on all
  - [5] 2026-11-02: a 429 means the daily or per-minute limit is exhausted | capture: sha256:a53949d44da37f952aad2d3407db89a665586ebc01948ee3904bb42a031099ab | quote: A `429` response means the daily or per-minute limit is exhausted.
  - [5] 2026-11-02: the key is passed as a query parameter | capture: sha256:a53949d44da37f952aad2d3407db89a665586ebc01948ee3904bb42a031099ab | quote: Authenticate to the API by passing your key as a query parameter in every request.
  - [4] 2026-11-02: exceeding the per-minute credit limit answers HTTP 429 | capture: sha256:5a7ccbeb3b4272c72a00c1e4ed3f697d6232542b04b3730dcd19d07dc2e32106
  - [2] 2026-11-02:  | capture: sha256:30645643587f39fe783fcb0481ca8a08349c1ef5a8d0ca7baf1e627282a78a82 | quote: The results may be temporarily cached on the client side (e.g. browser or mobile app).
  - [2] 2026-11-02: access is activated and notified by email | capture: sha256:30645643587f39fe783fcb0481ca8a08349c1ef5a8d0ca7baf1e627282a78a82 | quote: GraphHopper activates the requested access and notifies the Subscriber of this via email.
  - [2] 2026-11-02: packages without the white label option must display GraphHopper attribution | capture: sha256:30645643587f39fe783fcb0481ca8a08349c1ef5a8d0ca7baf1e627282a78a82 | quote: You understand that packages without the white label option require You to display GraphHopper attribution.
  - [6] 2026-11-02: the provider parameter is under development and can fall back to the default | capture: sha256:02fcd48719617e37f39e4241fa1cbee468af35999ec45e59c725764d09d85a5c | quote: The provider parameter is currently under development and can fall back to default at any time.
  - [6] 2026-11-02: every provider supports forward geocoding and reverse geocoding with reverse=true | capture: sha256:02fcd48719617e37f39e4241fa1cbee468af35999ec45e59c725764d09d85a5c | quote: All providers support normal "forward" geocoding and reverse geocoding via reverse=true.
  - [7] 2026-11-02: the sign-up form asks for first and last name, email, password, company and country | capture: sha256:b8d8219fd5d1297f93b1df8db3111c67730a25b388d5896f53a5f88091244458 | quote: First Name Last Name Email Password Confirm Password Company
  - [7] 2026-11-02: the sign-up form has a terms checkbox | capture: sha256:b8d8219fd5d1297f93b1df8db3111c67730a25b388d5896f53a5f88091244458
  - probe:https://graphhopper.com/api/1/geocode?q=Zurich 2026-11-02: a keyless geocode answers HTTP 401 | capture: sha256:003486d1eec8692487ea1df0694d53e0e95c1f390c42a32cf863f8eb8b5b6d97 | quote: "status": 401
  - probe:https://graphhopper.com/api/1/geocode?q=Zurich#body 2026-11-02: the keyless geocode is refused with No API key specified | capture: sha256:5eaa4336b5be536bb2171b8bb967eb457e6c95d296d53e43452d98f4cc06b45d | quote: No API key specified.
- sources:
  - [1] https://www.graphhopper.com/pricing/
  - [2] https://www.graphhopper.com/terms/
  - [3] https://www.graphhopper.com/faq/what-is-one-credit/
  - [4] https://support.graphhopper.com/support/solutions/articles/44001976065-what-is-a-credit-limit-per-minute-
  - [5] https://docs.graphhopper.com/openapi.md
  - [6] https://docs.graphhopper.com/openapi/geocoding/getgeocode.md
  - [7] https://graphhopper.com/dashboard/signup
