# cnab

> cnab.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cnab/ | JSON https://fshy.ajam.dev/api/v1/entity/cnab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cnab (cloud native application bundles)

- `storage/cnab` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.378Z (live) | stale on 2026-12-04
- url https://cnab.io/
- free tier: none reachable: A packaging spec for distributed apps, not a storage provider; it defines a bundle format you push to a registry you already have. Adds nothing beyond ORAS itself. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: A packaging spec for distributed apps, not a storage provider; it defines a bundle format you push to a registry you already have. Adds nothing beyond ORAS itself.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A packaging spec for distributed apps, not a storage provider; it defines a bundle format you push to a registry you already have. Adds nothing beyond ORAS itself.
  - [1] 2026-11-19: CNAB is an app packaging and bundling specification, not a storage provider | capture: sha256:ed69a7fc747b54a8d64e9e0069db7f5ceb6d5c39cda1dac9dffa2b00bfcb4a36 | quote: CNABs facilitate the bundling, installing and managing of container-native apps — and their coupled services.
- sources:
  - [1] https://cnab.io/
