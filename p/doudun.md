# cstcloud 数据胶囊

> doudun.site | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doudun/ | JSON https://fshy.ajam.dev/api/v1/entity/doudun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cstcloud 数据胶囊 (china science and technology cloud 'data capsule')

- `storage/cstcloud` | fails-identity | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:00.041Z (live) | stale on 2026-12-04
- url https://www.doudun.site/guide/data-cstcloud/
- free tier: none reachable: Free quota is 20 GB and requires real-name verification (实名认证) to register. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: real-name verification (实名认证) is required to reach the 20 GB free quota
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: Free quota is 20 GB — 25x short — and it requires 实名认证 (real-name verification) to reach even that.…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free quota is 20 GB — 25x short — and it requires 实名认证 (real-name verification) to reach even that. Source
  - [2] 2026-10-21: Free quota is 20 GB — 25x short — and it requires 实名认证 (real-name verification) to reach even that. Source
  - [3] 2026-10-21: Free quota is 20 GB — 25x short — and it requires 实名认证 (real-name verification) to reach even that. Source
  - [1] 2026-11-19: the free quota is 20GB and is reached through real-name verification | capture: sha256:01ef3c4a5ac2806593c4d855d8f0b2db34a8951763ea3877e5b299a5eb7b748d | quote: 完成实名认证即可升级到 20GB免费容量
  - [1] 2026-11-19: real-name verification is the gate to the 20GB free quota | capture: sha256:01ef3c4a5ac2806593c4d855d8f0b2db34a8951763ea3877e5b299a5eb7b748d | quote: 完成实名认证即可升级到 20GB免费容量
- sources:
  - [1] https://www.doudun.site/guide/data-cstcloud/
  - [2] https://blog.bitefu.net/post/733.html
  - [3] https://linux.do/t/topic/1614982
