# VIP优盘

> u-p.vip | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/u-p/ | JSON https://fshy.ajam.dev/api/v1/entity/u-p.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VIP优盘 (u-p.vip)

- `storage/vip` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://web.u-p.vip
- free tier: VIP1 (free on registration): 500 GB+ storage. 120 GB on signup plus 380 GB for registering the partner app. With +100 GB per invited user, '扩容无上限' (unlimited expansion). Per-file 5 GB on VIP1. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file | bytes: 5000000000 | source: [1] | note: not stated
- retention: VIP2 (1.5 TB+, 10 GB/file) and VIP3 (3 TB+, 20 GB/file) are earned via points from the partner shopping app, not purchased. Storage is 'permanent' while the account stays active. | source: [1] | note: not stated
- egress: No speed limit and no traffic quota at any tier: '不限速，永久免费'. Downloads are free of charge and unmetered. | metered: no
- identity: email
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 5 GB per file [1]
  - per-object-cap (binding): 10 GB/file [1]
  - write-gated: invited user, '扩容无上限' (unlimited expansion) [1]
  - write-gated: invites and points from a third-party app, so the 'unlimited expansion' depends on a p [1]
- limits note: VIP1: 5 GB per file, 500 GB+ storage. VIP2 (1.5 TB+, 10 GB/file) and VIP3 (3 TB+, 20 GB/file) are earned via points from the partner shopping app, not purchased. Storage is 'permanent' while the account stays active.
- interface detail: webdav
- tooling: WebDAV is listed as 公测中 (public beta) on VIP1 and supported on VIP3; offline download also beta. No documented REST API.
- composes with: 500 GB base + 100 GB per invited account is a genuinely linear free multiplier, and the operator states there is no ceiling on expansion. Chain = 100 GB x N invites, capped only by the invite funnel.
- reliability: The entire free-storage economy is a shopping-rebate funnel. Capacity is denominated in invites and points from a third-party app, so the 'unlimited expansion' depends on a partner business that can disappear. WebDAV is still beta on the free tier.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'VIP1 ... 存储容量500GB，其中初始容量120GB，注册呆萌价会员后赠送380GB，每邀请1名呆萌价新人，扩容100GB容量'
  - [2] 2026-10-21: table: '单文件大小 5GB | 存储容量 500GB+' for VIP1; 10GB/1.5TB+ VIP2; 20GB/3TB+ VIP3
  - [3] 2026-10-21: '每邀请1名呆萌价新用户，赠送100GB永久容量，赠送无上限'
- sources:
  - [1] https://web.u-p.vip/about
  - [2] https://web.u-p.vip/about/vip.htm
  - [3] https://web.u-p.vip/about/free.htm
