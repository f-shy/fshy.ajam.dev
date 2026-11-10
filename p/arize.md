# arize ax

> arize.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arize/ | JSON https://fshy.ajam.dev/api/v1/entity/arize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## arize ax / phoenix cloud free tier

- `storage/arize-ax-phoenix-cloud-free-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://arize.com/docs/ax/security-and-settings/pricing-and-usage
- free tier: none reachable: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
  - [2] 2026-10-21: cited as the basis of the rejection: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
- sources:
  - [1] https://arize.com/docs/ax/security-and-settings/pricing-and-usage
  - [2] https://markaicode.com/pricing/arize-phoenix-pricing/
