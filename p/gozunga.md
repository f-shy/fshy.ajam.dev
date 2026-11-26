# gozunga

> gozunga.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gozunga/ | JSON https://fshy.ajam.dev/api/v1/entity/gozunga.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gozunga

- `storage/gozunga` | fails-egress | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:04:20.873Z (live) | stale on 2026-12-04
- url https://gozunga.com/object-storage
- free tier: none reachable: Free tier includes 100 GB per month S3-compatible storage, followed by $0.025 per GB storage and $0.005 per GB egress. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Outbound bandwidth is priced at $0.005/GB; the page lists no free outbound allowance, so 1 TiB a day is metered, not free. | metered: yes
- identity: email | detail: the first 100 GB each month needs no credit card; the other sign-up fields are not stated on the page
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the 2026-11-03 read covered https://gozunga.com/object-storage: the first 100GB of object storage free every month with no credit card, and transfer at $0.005/GB; the $0.025/GB storage price and the other sign-up fields were not quoted
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 100 GB/month free S3-compatible, then $0.025/GB and $0.005/GB egress.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 100 GB/month free S3-compatible, then $0.025/GB and $0.005/GB egress.
  - [1] 2026-11-03: outbound bandwidth is priced at $0.005 per GB | capture: sha256:87b77f1c133b9acd3891ab4df92ac83e90dc2f474d452d227e477f1c6ff8862a | quote: $0.005/GB transfer
  - [1] 2026-11-03: the free 100 GB each month needs no card | capture: sha256:87b77f1c133b9acd3891ab4df92ac83e90dc2f474d452d227e477f1c6ff8862a | quote: Get your first 100GB of cloud object storage free every month with no credit card required.
- sources:
  - [1] https://gozunga.com/object-storage
