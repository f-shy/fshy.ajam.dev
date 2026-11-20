# ipums

> ipums.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipums/ | JSON https://fshy.ajam.dev/api/v1/entity/ipums.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipums

- `storage/ipums` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.853Z (live) | stale on 2026-12-04
- url https://api.ipums.org/extracts
- free tier: none reachable: Extract API returns 403 without a key and the product is pre-registered microdata extracts, not user uploads. No deposit path exists. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Extract API returns 403 without a key and the product is pre-registered microdata extracts, not user uploads. No deposit path exists.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Extract API returns 403 without a key and the product is pre-registered microdata extracts, not user uploads. No deposit path exists.
  - [1] 2026-11-19: the extract API returns an Invalid API key error to a request without a key | capture: sha256:e0c02b0b97fe1cddc216e2d6d2d2b0c67a77599ae7980505e60a9fb473361f56 | quote: "error": "Invalid API key"
- sources:
  - [1] https://api.ipums.org/extracts
