# dns txt records as a storage medium

> desec.readthedocs.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/desec-readthedocs-io/ | JSON https://fshy.ajam.dev/api/v1/entity/desec-readthedocs-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dns txt records as a storage medium (desec / duckdns / freedns)

- `storage/dns-txt-records-as-a-storage-medium` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://desec.readthedocs.io/en/latest/dns/rrsets.html
- free tier: none reachable: Works as a protocol but the ceiling is ~1 MB per name: one RRset allows max 4091 record values and 64,000 characters total after JSON encoding, and RRset writes are capped at 300/day/domain. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Works as a protocol but the ceiling is ~1 MB per name: one RRset allows max 4091 record values and 64,000 characters total after JSON encoding, and RRset writes are capped at 300/day/domain.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Works as a protocol but the ceiling is ~1 MB per name: one RRset allows max 4091 record values and 64,000 characters total after JSON encoding, and RRset writes are capped at 300/day/domain.
  - [2] 2026-10-21: cited as the basis of the rejection: Works as a protocol but the ceiling is ~1 MB per name: one RRset allows max 4091 record values and 64,000 characters total after JSON encoding, and RRset writes are capped at 300/day/domain.
  - [3] 2026-10-21: cited as the basis of the rejection: Works as a protocol but the ceiling is ~1 MB per name: one RRset allows max 4091 record values and 64,000 characters total after JSON encoding, and RRset writes are capped at 300/day/domain.
- sources:
  - [1] https://desec.readthedocs.io/en/latest/dns/rrsets.html
  - [2] https://desec.readthedocs.io/en/latest/rate-limits.html
  - [3] https://desec.io/
