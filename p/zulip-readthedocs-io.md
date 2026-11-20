# zulip self-hosted free

> zulip.readthedocs.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zulip-readthedocs-io/ | JSON https://fshy.ajam.dev/api/v1/entity/zulip-readthedocs-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zulip self-hosted free / community

- `storage/zulip-self-hosted-free-community` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zulip.readthedocs.io/en/stable/production/upload-backends.html
- free tier: none reachable: Self-hosted means the disk is yours to pay for. The only interesting artifact is the S3 upload backend, which points at a bucket you already pay for. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Self-hosted means the disk is yours to pay for. The only interesting artifact is the S3 upload backend, which points at a bucket you already pay for.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Self-hosted means the disk is yours to pay for. The only interesting artifact is the S3 upload backend, which points at a bucket you already pay for.
- sources:
  - [1] https://zulip.readthedocs.io/en/stable/production/upload-backends.html
