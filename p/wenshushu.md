# 文叔叔 WenShuShu

> wenshushu.cn | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wenshushu/ | JSON https://fshy.ajam.dev/api/v1/entity/wenshushu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wenshushu (文叔叔)

- `storage/wenshushu-2` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.wenshushu.cn/faq
- free tier: none reachable: Free tier offers 40 GB of cloud drive capacity. Transfer bandwidth is not throttled. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: egress
  - dead_end.why: Free space is 40 GB, explicitly: '免费提供网络硬盘空间 40GB'. Its 'never throttled' promise is real but irrelevant at this quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free space is 40 GB, explicitly: '免费提供网络硬盘空间 40GB'. Its 'never throttled' promise is real but irrelevant at this quota.
- sources:
  - [1] https://www.wenshushu.cn/faq

## 文叔叔 WenShuShu (wenshushu.cn)

- `storage/wenshushu` | fails-quota | evidence reported | binding per-object-cap | category transfer-service
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.wenshushu.cn
- free tier: 40 GB free drive space. Own site: '免费提供网络硬盘空间 40GB'. Per-file: 5 GB ('单个文件最大可达5GB'). No login needed to send; login needed to keep. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file: 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered and unshaped. The entire product pitch is '永不限速', confirmed by the homepage title and by PanHunt's '永不限速' row. | metered: no
- identity: any-phone | detail: any-phone (phone binding raises the free space toward the 40 GB ceiling; anonymous sending works but does not give you storage).
- interface: rest, webdav
- limits:
  - per-object-cap (binding): Per-file: 5 GB [1]
- limits note: per-object-cap: 5 GB. storage: 40 GB total. retention: transfer links expire; drive files persist only while the account is alive. No published request-rate.
- interface detail: rest
- tooling: Qaiu/netdisk-fast-download `ws` parser (302 direct link); dtpoi/Netdisk-to-VRChat-Direct-link resolves 文叔叔 links via Edge Functions. No mount, no WebDAV. Download-only.
- composes with: 40 GB per account x N phone/email accounts. The interesting object is the 5 GB/file ceiling with zero speed shaping. Usable as a serving layer, not as bulk cold storage.
- reliability: Single-product company; historically pivoted pricing. Nothing suggests data loss within an active account.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 40 GB free drive space. Own site: '免费提供网络硬盘空间 40GB'. Per-file: 5 GB ('单个文件最大可达5GB'). No login needed to send; login needed to keep.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '文叔叔是一款永不限速的网盘（云盘）产品，免费提供网络硬盘空间 40GB'
  - [2] 2026-10-21: '免费 约 40GB，限速情况为「不限速」'
  - [3] 2026-10-21: '40GB免费存储空间...支持单文件最大5GB传输'
- sources:
  - [1] https://www.wenshushu.cn/
  - [2] https://panhunt.com/pan-platforms/wenshushu
  - [3] https://www.zmt.wiki/sites/5819.html
