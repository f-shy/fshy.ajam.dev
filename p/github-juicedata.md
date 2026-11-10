# juicefs community edition as an n-bucket pool

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-juicedata/ | JSON https://fshy.ajam.dev/api/v1/entity/github-juicedata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## juicefs community edition as an n-bucket pool

- `storage/juicefs-community-edition-as-an-n-bucket-pool` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/juicedata/juicefs/issues/345
- free tier: none reachable: A single JuiceFS volume binds to exactly ONE object-storage endpoint; multi-bucket/multi-provider backend has been an open feature request since 2021-04-23 and is still open with no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: A single JuiceFS volume binds to exactly ONE object-storage endpoint; multi-bucket/multi-provider backend has been an open feature request since 2021-04-23 and is still open with no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A single JuiceFS volume binds to exactly ONE object-storage endpoint; multi-bucket/multi-provider backend has been an open feature request since 2021-04-23 and is still open with no…
  - [2] 2026-10-21: cited as the basis of the rejection: A single JuiceFS volume binds to exactly ONE object-storage endpoint; multi-bucket/multi-provider backend has been an open feature request since 2021-04-23 and is still open with no implemen
- sources:
  - [1] https://github.com/juicedata/juicefs/issues/345
  - [2] https://github.com/juicedata/juicefs/discussions/5153
