# opendal as a ready-made free-tier pool

> docs.rs | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs-3/ | JSON https://fshy.ajam.dev/api/v1/entity/docs-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## opendal as a ready-made free-tier pool

- `storage/opendal-as-a-ready-made-free-tier-pool` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.rs/crate/opendal-service-compfs/latest/source/src/backend.rs
- free tier: None reachable: Two separate misconceptions to kill. (1) `compfs` is not 'composed filesystem over services'. Its source is a `compio`-based local-filesystem backend. (2) RFC-7740 'Operator Composition' co. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Two separate misconceptions to kill. (1) `compfs` is not 'composed filesystem over services' — its source is a `compio`-based local-filesystem backend. (2) RFC-7740 'Operator Composition'…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Two separate misconceptions to kill. (1) `compfs` is not 'composed filesystem over services' — its source is a `compio`-based local-filesystem backend. (2) RFC-7740 'Operator Composition'…
  - [2] 2026-10-21: cited as the basis of the rejection: Two separate misconceptions to kill. (1) `compfs` is not 'composed filesystem over services' — its source is a `compio`-based local-filesystem backend. (2) RFC-7740 'Operator Composition' co
- sources:
  - [1] https://docs.rs/crate/opendal-service-compfs/latest/source/src/backend.rs
  - [2] https://opendal.apache.org/docs/rust/opendal/docs/rfcs/rfc_7740_operator_composition/index.html
