# dns txt records as a storage medium

> desec.readthedocs.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/desec-readthedocs-io/ | JSON https://fshy.ajam.dev/api/v1/entity/desec-readthedocs-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dns txt records as a storage medium (desec / duckdns / freedns)

- `storage/dns-txt-records-as-a-storage-medium` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.671Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: one RRset holds at most 4091 values and 64,000 characters after JSON encoding | capture: sha256:e73f70045eec55acd7d1d6d0caae67760420db0c08e4a4ac150c39e785d2d239 | quote: The maximum number of array elements is 4091, and the maximum length of the array is 64,000 (after JSON encoding).
  - [2] 2026-11-19: RRset writes are limited to 300 per day per domain | capture: sha256:72d1a1d847779ebf7deeb02594ff94395285c7257c2c82ec6012d041cd066923 | quote: | `dns_api_per_domain_expensive` | 2/s 15/min 100/h 300/day | RRset creation/deletion/modification (per domain). If you require more requests, consider using bulk requests. |
- sources:
  - [1] https://desec.readthedocs.io/en/latest/dns/rrsets.html
  - [2] https://desec.readthedocs.io/en/latest/rate-limits.html
  - [3] https://desec.io/
