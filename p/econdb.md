# Econdb

> econdb.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/econdb/ | JSON https://fshy.ajam.dev/api/v1/entity/econdb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Econdb

- `data-apis/econdb` | paid-only | evidence documented | binding write-gated | category economic and shipping data API (macro time series, ports, vessels) | tier Subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://www.econdb.com/pricing/
- free tier: No free API: the website allows 15 free views a day; the USD 400 a year subscription includes CSV downloads and API access | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: The API docs (released 29 July 2025) require a token in the Authorization header. Keyless calls to both the legacy series endpoint and the v1 ports endpoint answered HTTP 401. Whether a free account can mint a token is unverified: behind a sign-up.
- per-object cap: not stated | source: [1]
- retention: not applicable | note: Port calls, congestion, dwell and throughput are available from 2022 onwards.
- egress: not metered in bytes; no request quota is stated | metered: no | source: [1]
- identity: email | detail: The account form takes an optional email, a username and a password, or Google sign-in; no card on the form. The paid API needs a payment.
- interface: rest
- limits:
  - write-gated (binding): API access is part of the USD 400 a year subscription; keyless calls answer 401 [1]
- limits note: Bulk path: CSV downloads are part of the subscription; Enterprise offers bulk files and feeds. Storage terms: unverified, the terms page answered HTTP 404.
- binding note: A paid subscription, not a request count, stands between a caller and the API.
- interface detail: GET https://api.econdb.com/v1/... with Authorization: Token KEY
- endpoint: part of interface detail
- tooling: curl or any HTTP client; Python and R clients are published
- composes with: Macro series and port data need a paid token here; FRED and Fiscal Data give macro series with a free key or none.
- reliability: Keyless calls answer HTTP 401 Authentication credentials were not provided.
- notes: API needs a paid token; the free tier is website views only. Bulk path: Enterprise. Storage terms: unverified.
- evidence note: Plan and API terms are read from the vendor pages; two keyless probes answered 401; the free account's token rights were not read.
- extras:
  - bulk_path: CSV exports on the subscription; bulk files on Enterprise
- evidence:
  - [1] 2026-11-02: 15 free views a day on the website | capture: sha256:0269846ad3a3bef8737e787ca023a3bac61185fe9b8e8bd665c54649c064a824 | quote: You've used 0 of 15 free views today.
  - [1] 2026-11-02: the subscription is USD 400 a year | capture: sha256:0269846ad3a3bef8737e787ca023a3bac61185fe9b8e8bd665c54649c064a824 | quote: $400per year
  - [1] 2026-11-02: API access comes with the subscription | capture: sha256:0269846ad3a3bef8737e787ca023a3bac61185fe9b8e8bd665c54649c064a824 | quote: The subscription includes chart CSV exports and API access.
  - [1] 2026-11-02: Enterprise offers bulk files or feeds | capture: sha256:0269846ad3a3bef8737e787ca023a3bac61185fe9b8e8bd665c54649c064a824 | quote: Bulk files or recurring feeds delivered to your systems.
  - [2] 2026-11-02: the API was released on 29 July 2025 and uses a token | capture: sha256:a0c9344ccedf1a40ba5adc4d9ecab6f4ffc73d4dc889348ef3cb0bd601471e9b | quote: Released on July 29, 2025, the
  - [3] 2026-11-02: the account form takes an optional email, a username and a password | capture: sha256:aa0bcd605fe9a25b26b211cddb10412599cf390b9e0bc8396538929a36a83ec1 | quote: Email (optional):
  - probe:https://api.econdb.com/v1/ports/ 2026-11-02: a keyless v1 call answered HTTP 401 | capture: sha256:f95e70533f8c5d1fb44e54fe939fba26064f6395598b3c61df081580e0e641bb | quote: "status": 401
  - probe:https://www.econdb.com/api/series/RGDPUS/?format=json 2026-11-02: a keyless legacy series call answered HTTP 401 | capture: sha256:bbd9ca0c7216c8fec3f9a72e79f21cfe940dbf20d05e483a72c82668b55154bd | quote: "status": 401
- sources:
  - [1] https://www.econdb.com/pricing/
  - [2] https://developers.econdb.com/docs/
  - [3] https://www.econdb.com/accounts/signup/
