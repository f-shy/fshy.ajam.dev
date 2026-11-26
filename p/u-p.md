# VIP优盘

> u-p.vip | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/u-p/ | JSON https://fshy.ajam.dev/api/v1/entity/u-p.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VIP优盘 (u-p.vip)

- `storage/vip` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:18.735Z (live) | stale on 2026-12-10
- url https://web.u-p.vip
- free tier: VIP1 (free on registration): 500 GB+ storage. 120 GB on signup plus 380 GB for registering the partner app. With +100 GB per invited user, '扩容无上限' (unlimited expansion). Per-file 5 GB on VIP1. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file | bytes: 5000000000 | source: [1] | note: VIP1 单文件大小 5GB; VIP2 10GB; VIP3 20GB
- retention: 只要你经常使用VIP优盘，就可以永久保留。 | source: [1] | note: 只要你经常使用VIP优盘，就可以永久保留。
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
- composes with: 每邀请1名呆萌价新用户，赠送100GB永久容量，赠送无上限。
- reliability: The entire free-storage economy is a shopping-rebate funnel. Capacity is denominated in invites and points from a third-party app, so the 'unlimited expansion' depends on a partner business that can disappear. WebDAV is still beta on the free tier.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'VIP1 ... 存储容量500GB，其中初始容量120GB，注册呆萌价会员后赠送380GB，每邀请1名呆萌价新人，扩容100GB容量'
  - [2] 2026-10-21: table: '单文件大小 5GB | 存储容量 500GB+' for VIP1; 10GB/1.5TB+ VIP2; 20GB/3TB+ VIP3
  - [3] 2026-10-21: '每邀请1名呆萌价新用户，赠送100GB永久容量，赠送无上限'
  - [1] 2026-11-19: VIP1 free: 500 GB total (120 GB signup + 380 GB partner app), +100 GB per invite | capture: sha256:f46b489bc9d4e8bace516ff2f61e7295e72872bea5137ab9b0d4bd898d90679d | quote: 存储容量500GB，其中初始容量120GB，注册呆萌价会员后赠送380GB，每邀请1名呆萌价新人，扩容100GB容量
  - [2] 2026-11-19: per-file caps: VIP1 5 GB, VIP2 10 GB, VIP3 20 GB | capture: sha256:d7a911b66a25a74fda5361ade9712660af926b929a0b58fe025b042dbfa5ea9e | quote: 单文件大小 | 5GB | 10GB | 20GB | 20GB
  - [3] 2026-11-19: each invited partner-app user grants 100 GB permanent capacity with no stated ceiling | capture: sha256:31738449caa932618acd44b1ee8e21d828cf6084fb8b2b1714014f995d4b5112 | quote: 每邀请1名呆萌价新用户，赠送100GB永久容量，赠送无上限
  - [2] 2026-11-25: the tier table maps VIP1 to 5GB, VIP2 to 10GB and VIP3 to 20GB single-file sizes | capture: sha256:d7a911b66a25a74fda5361ade9712660af926b929a0b58fe025b042dbfa5ea9e | quote: | | [VIP1](https://web.u-p.vip/duty) | [VIP2](https://www.u-p.vip/buy?tab=1) | [VIP3](https://www.u-p.vip/buy?tab=1) | [定制版](https://www.u-p.vip/buy?tab=1) | | --- | --- | --- | --- | --- | | 单文件大小 | 5GB | 10GB | 20GB | 20GB |
  - [1] 2026-11-25: the first-party page says files are kept permanently with regular use | capture: sha256:f46b489bc9d4e8bace516ff2f61e7295e72872bea5137ab9b0d4bd898d90679d | quote: 只要你经常使用VIP优盘，就可以永久保留。
  - [1] 2026-11-25: the first-party page answers the longest-file-retention question with permanent retention under regular use | capture: sha256:f46b489bc9d4e8bace516ff2f61e7295e72872bea5137ab9b0d4bd898d90679d | quote: 只要你经常使用VIP优盘，就可以永久保留。
  - [3] 2026-11-25: each invited partner-app user grants 100GB permanent capacity with no stated ceiling | capture: sha256:31738449caa932618acd44b1ee8e21d828cf6084fb8b2b1714014f995d4b5112 | quote: 每邀请1名呆萌价新用户，赠送100GB永久容量，赠送无上限。
  - [1] 2026-11-25: the about page states permanent retention with regular use and the operator's deletion right | capture: sha256:f46b489bc9d4e8bace516ff2f61e7295e72872bea5137ab9b0d4bd898d90679d | quote: 请注意，由于VIP优盘用户数目庞大、服务器成本巨高，为保证服务质量，VIP优盘有权利在不通知其本人的情况下删除一些违规文件，您也可以通过[《免费》](https://web.u-p.vip/about/free.htm)获得[《超值》](https://web.u-p.vip/about/vip.htm)会员服务。 常见问题回答： ①文件最长存储多久？ 只要你经常使用VIP优盘，就可以永久保留。
  - [2] 2026-11-25: the tier table lists WebDAV support | capture: sha256:d7a911b66a25a74fda5361ade9712660af926b929a0b58fe025b042dbfa5ea9e | quote: | WebDAV | 公测中 | 公测中 | 支持 | 支持 |
- sources:
  - [1] https://web.u-p.vip/about
  - [2] https://web.u-p.vip/about/vip.htm
  - [3] https://web.u-p.vip/about/free.htm
