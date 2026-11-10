# 面包多

> mbd.pub | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mbd/ | JSON https://fshy.ajam.dev/api/v1/entity/mbd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 面包多 (mbd.pub)

- `storage/provider-9` | fails-identity | evidence reported | binding none | category Chinese digital-content marketplace — claims unlimited hosting
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mbd.pub
- free tier: Their help centre says '面包多提供无限制的文件托管和高速下载服务(文件<1G)'. Unlimited file hosting, with a per-file note of <1 GB. So: unlimited total, 1 GB per object. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB per object | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published egress cap; download is buyer-facing. | metered: no
- identity: national-id | detail: national-id
- interface: unknown
- limits:
  - per-object-cap: 1 GB per object [1]
- limits note: per-object-cap ~1 GB; unlimited aggregate (vendor claim).
- interface detail: Web; some developer/OAuth surface for payments (afdian-style), but no public upload API found.
- tooling: Web only.
- composes with: Unlimited x 1 GB is exactly the shard shape that works. But registration is the blocker, see identity_cost.
- reliability: Creator registration has been repeatedly closed or tightened ('极大的限制甚至在某些时候关闭新创作者的注册'), and payout requires 实名认证 with ID + bank details. This is the classic Chinese-platform wall.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Their help centre says '面包多提供无限制的文件托管和高速下载服务(文件<1G)' — unlimited file hosting, with a per-file note of <1 GB. So: unlimited total, 1 GB per object.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '面包多提供无限制的文件托管和高速下载服务(文件<1G)'
  - [2] 2026-10-21: creator payout moved to a third-party provider for 资金合规 (funds compliance), i.e. real-name gated
  - [3] 2026-10-21: official post: registrations for new creators heavily restricted or closed at times
- sources:
  - [1] https://mbd.pub/help/
  - [2] https://mbd.pub/o/bread/aZeZk5c=
  - [3] https://mp.weixin.qq.com/s/CZt2-UYSQ18NYPy5zSuMUA
