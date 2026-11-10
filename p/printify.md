# printify

> printify.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/printify/ | JSON https://fshy.ajam.dev/api/v1/entity/printify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## printify

- `storage/printify` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.printify.com/hc/en-us/articles/4483617936657
- free tier: none reachable: JPEG/PNG up to 100 MB, SVG up to 20 MB. 413 Request Entity Too Large is the documented failure mode on the API. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: JPEG/PNG up to 100 MB, SVG up to 20 MB. 413 Request Entity Too Large is the documented failure mode on the API.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: JPEG/PNG up to 100 MB, SVG up to 20 MB. 413 Request Entity Too Large is the documented failure mode on the API.
  - [2] 2026-10-21: cited as the basis of the rejection: JPEG/PNG up to 100 MB, SVG up to 20 MB. 413 Request Entity Too Large is the documented failure mode on the API.
- sources:
  - [1] https://help.printify.com/hc/en-us/articles/4483617936657
  - [2] https://nearlimit.com/printify-image-checker
