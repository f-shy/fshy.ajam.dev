# 联想乐云 LeCloud

> lenovo.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lenovo/ | JSON https://fshy.ajam.dev/api/v1/entity/lenovo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 联想乐云 LeCloud (lecloud.lenovo.com)

- `storage/lecloud` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lecloud.lenovo.com
- free tier: 5 GB base. '新注册账号有5GB云空间，如您在注册后7日内完成新人任务可以免费获赠1个月黄金会员扩容空间200GB'. Membership adds 20 GB per tier via sign-in activities. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: '全程不限速' on the homepage. The one genuinely good property. | metered: no
- identity: email | detail: email or Lenovo account
- interface: rest, webdav-proxy
- limits note: quota: 5 GB. retention-clamped: the 200 GB grant is '1个月'.
- interface detail: rest
- tooling: OpenList driver `lenovonas_share` (Lenovo NAS share-link parsing) and qaiu/netdisk-fast-download `le`. Both narrow: share-link resolution, not account mounting.
- composes with: 5 GB per Lenovo ID; Lenovo device serials are the natural multiplier but each still yields 5 GB. The 200 GB is a 1-month teaser, not a tier.
- reliability: Lenovo has kept the service running for years; the free tier has never been large.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB base. '新注册账号有5GB云空间，如您在注册后7日内完成新人任务可以免费获赠1个月黄金会员扩容空间200GB'. Membership adds 20 GB per tier via sign-in activities.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '目前新注册账号有5GB云空间，如您在注册后7日内完成新人任务可以免费获赠1个月黄金会员扩容空间200GB'
  - [2] 2026-10-21: https://lecloud.lenovo.com/ — '全程不限速'
  - [3] 2026-10-21: `le` parser present
- sources:
  - [1] https://iknow.lenovo.com.cn/detail/195851
  - [2] https://lecloud.lenovo.com/
  - [3] https://github.com/qaiu/netdisk-fast-download
