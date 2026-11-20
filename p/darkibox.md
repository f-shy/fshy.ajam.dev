# darkibox.com

> darkibox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/darkibox/ | JSON https://fshy.ajam.dev/api/v1/entity/darkibox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## darkibox.com

- `storage/darkibox-com` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:43.469Z (inherited) | stale on 2026-12-04
- url https://darkibox.com/
- free tier: none reachable: Returns HTTP 410 Gone on the homepage. Dataset lists a 50 GB free per-file cap; the site is retired. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Returns HTTP 410 Gone on the homepage. Dataset lists a 50 GB free per-file cap; the site is retired.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Returns HTTP 410 Gone on the homepage. Dataset lists a 50 GB free per-file cap; the site is retired.
  - probe:https://darkibox.com/ 2026-11-19: the host answers HTTP 410 Gone today, so the offer is gone | capture: sha256:f8f9b2912c698f96c83394a9b904479c4e16fc2143460f243f11e337453ed400 | quote: "status": 410
  - probe:https://darkibox.com/ 2026-11-19: the host answers HTTP 410 Gone today, so the service is gone | capture: sha256:f8f9b2912c698f96c83394a9b904479c4e16fc2143460f243f11e337453ed400 | quote: "status": 410
- sources:
  - [1] https://darkibox.com/
