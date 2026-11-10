# usgs

> waterservices.usgs.gov | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/waterservices-usgs-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/waterservices-usgs-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## usgs / noaa ncei

- `storage/usgs-noaa-ncei` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://waterservices.usgs.gov/nwis/iv/?format=json&sites=01646500&parameterCd=00060
- free tier: none reachable: Both are read-only public data services (verified live: waterservices.usgs.gov returns real JSON). NOAA's NCEI 'data' endpoints 301-redirect to AWS Open Data buckets. No user deposit, so… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both are read-only public data services (verified live: waterservices.usgs.gov returns real JSON). NOAA's NCEI 'data' endpoints 301-redirect to AWS Open Data buckets. No user deposit, so…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both are read-only public data services (verified live: waterservices.usgs.gov returns real JSON). NOAA's NCEI 'data' endpoints 301-redirect to AWS Open Data buckets. No user deposit, so…
- sources:
  - [1] https://waterservices.usgs.gov/nwis/iv/?format=json&sites=01646500&parameterCd=00060
