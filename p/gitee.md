# gitee

> gitee.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitee/ | JSON https://fshy.ajam.dev/api/v1/entity/gitee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gitee (gitee.com) as a storage host

- `storage/gitee-as-a-storage-host` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:39.839Z (live) | stale on 2026-12-04
- url https://help.gitee.com/account/usage-quota
- free tier: none reachable: The most precisely documented small quota in the whole slot, which makes it a useful calibration point: 1,000 repos, 500 MB per repo, 50 MB per file, 5 GB total across all personal AND… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The most precisely documented small quota in the whole slot, which makes it a useful calibration point: 1,000 repos, 500 MB per repo, 50 MB per file, 5 GB total across all personal AND…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The most precisely documented small quota in the whole slot, which makes it a useful calibration point: 1,000 repos, 500 MB per repo, 50 MB per file, 5 GB total across all personal AND…
  - [1] 2026-11-19: the first-party community quota page still states 1000 repos, 500 MB per repo, 50 MB per file and 5 GB total | capture: sha256:d5f31adea8087bc8c84501fddb8e1790f38aae8675aadd5e1f2c6c5d0b969284 | quote: | 仓库数量 | 创建 1000 个仓库，不限制公私有。 | | 仓库容量 | 单仓库大小上限为 500M 单文件最大 50M 用户总仓库容量为 5G 注：总仓库定义为用户名下以及所创建的组织下面的所有仓库。 |
- sources:
  - [1] https://help.gitee.com/account/usage-quota
