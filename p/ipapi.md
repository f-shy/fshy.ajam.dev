# ipapi

> ipapi.co | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipapi/ | JSON https://fshy.ajam.dev/api/v1/entity/ipapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipapi (ipapi.co)

- `data-apis/ipapi-co` | qualifies-with-caveat | evidence documented | binding volume-quota | category IP geolocation API | tier Free Trial
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ipapi.co/pricing/
- free tier: free trial plan: up to 1,000 IP lookups a day (about 30K a month) with no sign-up for basic fields and no credit card; suitable for testing and development | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the pricing FAQ says the trial is for a limited time, while the FAQ page says it has no time limit; paid plans start at USD 15 a month for 60K lookups
- per-object cap: single lookups; bulk lookup on the free trial is limited | source: [1]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: basic fields need no sign-up and no credit card; a higher-limit trial is by contact request
- interface: rest
- limits:
  - volume-quota (binding): up to 1,000 lookups a day on the free trial [1]
- interface detail: GET https://ipapi.co/{ip}/json/ with no key (also /{ip}/{field}/, xml, csv, yaml, jsonp); HTTP 429 RateLimited when the quota is exceeded
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: up to 1,000 keyless lookups a day with city, coordinates, time zone, currency and ASN fields. Bulk path: none on the free trial
- reliability: heuristics may further restrict free calls; the trial is described as for testing and development, and the pricing page and FAQ disagree on whether it is time-limited
- notes: Free requests: up to 1,000 a day, no key. Rate limit: HTTP 429 past the quota. Bulk path: none free.
- evidence note: the pricing page, the FAQ and the API docs were quoted on 2026-10-30, and a keyless lookup answered HTTP 200 with city-level fields; the daily quota was not exhausted to observe it.
- extras:
  - bulk_path: none on the free trial
  - free_requests: up to 1,000 a day
- evidence:
  - [1] 2026-10-30: the free trial gives up to 1,000 lookups a day | capture: sha256:da8fe00888f9de83c4be43f5dd03bc46d15990ef5d670ad442cebef950f00e72 | quote: Under the free trial, you get up-to 1000 IP lookups in a day (approximately 30K/month) for a limited time.
  - [1] 2026-10-30: free calls may be further restricted | capture: sha256:da8fe00888f9de83c4be43f5dd03bc46d15990ef5d670ad442cebef950f00e72 | quote: The system may use heuristics to further restrict free trial API calls under certain conditions.
  - [1] 2026-10-30: bulk lookup is limited on the free trial | capture: sha256:da8fe00888f9de83c4be43f5dd03bc46d15990ef5d670ad442cebef950f00e72 | quote: Limited Bulk IP lookup
  - [1] 2026-10-30: the first paid plan is USD 15 a month | capture: sha256:da8fe00888f9de83c4be43f5dd03bc46d15990ef5d670ad442cebef950f00e72 | quote: $15
  - [1] 2026-10-30: the first paid plan is 60K lookups a month | capture: sha256:da8fe00888f9de83c4be43f5dd03bc46d15990ef5d670ad442cebef950f00e72 | quote: 60 K / month
  - [2] 2026-10-30: the free plan has no card, no sign-up for basic fields and no time limit | capture: sha256:ae5bd6a4c8502b6a8093969571637e7505a1723d0e35057804891c54c3d27a5f | quote: We offer a free IP location plan for trial & testing with no time limit. No credit card is required to use it. Basic fields are accessible without sign-up.
  - [3] 2026-10-30: HTTP 429 when the quota is exceeded | capture: sha256:73f9bf4446251bc0d2e21e21b2c4e768beb888a81c27840f90ee3b02e9781082 | quote: | 429 | Quota exceeded |
  - probe:https://ipapi.co/8.8.8.8/json/ 2026-10-30: a keyless lookup answered with city data | capture: sha256:d9f3fec5945420c75b83706c8b09a8289187e4f129ad4bbe18b82c3b68e4ecb9 | quote: "city": "Mountain View"
- sources:
  - [1] https://ipapi.co/pricing/
  - [2] https://ipapi.co/faq/
  - [3] https://ipapi.co/api/
