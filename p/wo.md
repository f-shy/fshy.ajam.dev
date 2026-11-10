# China Unicom

> wo.cn | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wo/ | JSON https://fshy.ajam.dev/api/v1/entity/wo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## China Unicom Cloud (联通云盘 / 沃盘, pan.wo.cn)

- `netdisk-pan/china-unicom-wopan` | trial-only | evidence reported | binding per-object-cap | category carrier cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:20:53.783Z (inherited) | stale on 2026-11-19
- url https://pan.wo.cn
- free tier: 60 GB free, raised from 10 GB by a promotion from 2025-09-01 to 15 that was made permanent: '免费用户存储空间 由10GB 提升至60GB，空间长期有效'. Non-Unicom numbers can register | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published in what was read | source: [2]
- retention: The 60 GB is stated as 长期有效, long-term valid. Promotional grants of 8 TB run one year | source: [1]
- egress: Advertised 不限速 on the homepage. One poster measured cross-carrier throughput through OpenList and WebDAV at their full 100 Mbit/s up and 500 Mbit/s down, so unlike Tianyi it is not throttled cross-carrier | metered: no | source: [3]
- identity: country-phone | detail: a PRC number, with a non-Unicom number accepted: '非联通用户也能注册'. A promo code is the alternative path | country: 86
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 60 GB is the free tier total, which is the cap in practice [1]
  - write-gated: registration wants a Unicom number or a promo code; a non-Unicom number is accepted but still a Chinese one [2]
- binding note: Free storage provides 60 GB, with larger quota grants tied to time-limited mobile contract promotions. The per-file upload cap is unpublished, making total account capacity the binding limit.
- tooling: the OpenList wopan driver, which mounts through the web client with a refresh token and an access token that a helper tool mints or that are captured from the browser. The OpenList documentation calls the interface a reverse-engineered one that the OpenList project does not actively maintain. A separate Go SDK, OpenListTeam/wopan-sdk-go, takes a refresh token
- composes with: 60 GB per account and phone-bound, so each additional carrier number is a new identity. Carrier family sharing pools within a household. Not a 500 GB play without multiplication
- reliability: The quota is promotional and has already changed once, and the operator drives historically shrink free tiers after a growth phase. Multiple posters describe the product as under-resourced with a slow interface, and the WebDAV mount and the cross-network speed are the best of the three carrier pans
- notes: A carrier pan reached through an OpenList driver and a separate Go SDK; the OpenList documentation calls the interface reverse-engineered and not actively maintained by that project. Two earlier records disagreed: one called it trial-only on a one-year promo and one called it fails-quota on the permanent free tier. Both are right about different tiers, and the verdict follows the permanent tier because the promo is time-limited. A third-party table now lists a larger free quota, which is open to a check
- extras:
  - access_mode: registration-gated
  - sdk: OpenListTeam/wopan-sdk-go, maintained
  - cross_carrier_unthrottled: yes
  - aliases: 联通云盘 (China Unicom); 联通云盘 / China Unicom Cloud (pan.wo.cn); 联通云盘 / 沃盘 WoPan; WoPan
- evidence:
  - [1] 2026-10-21: '免费用户存储空间 由10GB 提升至60GB，空间长期有效' and '非联通用户也能注册'
  - [4] 2026-10-21: homepage title '联通云盘-开启美好时光|不限速', and '非联通用户也能注册'
  - [3] 2026-10-21: '可以送8T的存储空间...本人通过Openlist挂载webdav实测，能够跑满我的100Mbps上传和500Mbps下载...会员有效期1年'
  - [5] 2026-10-21: '我是永久2T，办套餐送的', so permanent capacity rides a plan
  - [6] 2026-10-21: the web client actively blocks F12 inspection: '这个打开F12 会自动屏蔽'
  - probe:https://pan.wo.cn/ 2026-10-21: The site answered a title through another path, so the DNS result is vantage-dependent and not a death
  - [7] 2026-11-03: the OpenList wopan driver page calls the interface a reverse-engineered one that the project does not actively maintain | capture: sha256:aec32fa6844ac0f882c1c14d6742c4997052091c5c409229024715c63a4ecced | quote: 本接口是基于历史产物的逆向接口，项目组不会主动进行维护，请勿针对此驱动提出有关于任何修复或进行进一步逆向行为需求的issue。
  - probe:https://pan.wo.cn/ 2026-11-03: the host resolves and answers 200 with the 联通云盘 page, whose title advertises 不限速 | capture: sha256:4254db127d8ed4b858b9516927623e7553db9b2d3bb04e21213a4f5fd2490554 | quote: <title>联通云盘-开启美好时光|不限速</title>
  - [8] 2026-11-03: the table row lists 500G free, a 2G upload limit and a 0.5M/s download limit, unlike the 60 GB and unthrottled figures of this record | capture: sha256:87cfd4212b0eaf2bb73b16353c13f114920639a0b2df7d9e3a6465f3bf0ce870 | quote: | 联通云盘 | 500G | 2G | | | 0.5M/s | | |
  - [7] 2026-11-03: an OpenList mount of the pan uses the web client, and a later web login signs the mount out | capture: sha256:aec32fa6844ac0f882c1c14d6742c4997052091c5c409229024715c63a4ecced | quote: 如果你先使用工具获取了令牌，再去登录网页端联通云盘会将OpenList挂载的踢下线导致失效
  - [9] 2026-11-03: the Go SDK is built from a refresh token | capture: sha256:0a8b329f16a63ca53007239e588d64fc4f1e30951a2b20f7513513a9bc25dba4 | quote: w := wopan.DefaultWithRefreshToken("91d4b946-xxxx-4909-bac1-d9914e45f2de")
- sources:
  - [1] https://forum.naixi.net/thread-5251-1-1.html
  - [2] https://pan.wo.cn
  - [3] https://linux.do/t/topic/2455477
  - [4] https://pan.wo.cn/
  - [5] https://linux.do/t/topic/929354
  - [6] https://www.nodeseek.com/post-844305-2
  - [7] https://openlistteam.github.io/docs/zh/guide/drivers/wopan.html
  - [8] https://zh.wikipedia.org/zh-cn/中国大陆网盘列表
  - [9] https://github.com/OpenListTeam/wopan-sdk-go

## 联通云盘 / 沃盘 WoPan (pan.wo.cn, China Unicom)

- `storage/wopan` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pan.wo.cn
- free tier: 60 GB free. Raised from 10 GB by a 2025-09-01→15 promotion that was made permanent ('免费用户存储空间 由10GB 提升至60GB，空间长期有效'). Site tagline '不限速'. Non-Unicom numbers can register ('非联通用户也能注册'). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 60 GB free. Raised from 10 GB by a 2025-09-01→15 promotion that was made permanent ('免费用户存储空间 由10GB 提升至60GB，空间长期有效'). | source: [1] | note: not stated
- egress: Advertised '不限速' on the homepage; no per-GB egress pricing found. Paid tiers step 6 TB. | metered: no
- identity: country-phone | detail: country-phone (PRC number; non-Unicom accepted).
- interface: rest, webdav-proxy
- limits note: Account quota of 60 GB is the primary constraint. No per-file size cap is published in official documentation.
- interface detail: rest
- tooling: OpenList driver `wopan` (has its own SDK: github.com/OpenListTeam/wopan-sdk-go, refresh-token + family-id support). Maintained, not reverse-engineered, which is unusual for a Chinese carrier drive.
- composes with: 60 GB per account, phone-bound; each additional carrier number is a new identity. Carrier-family sharing ('family_id') pools within a household. Not a 500 GB play unless multiplied.
- reliability: Quota is promotional and has already changed once; operator drives historically shrink free tiers after the growth phase.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 60 GB free — raised from 10 GB by a 2025-09-01→15 promotion that was made permanent ('免费用户存储空间 由10GB 提升至60GB，空间长期有效'). Site tagline '不限速'. Non-Unicom numbers can register ('非联通用户也能注册').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '免费用户存储空间 由10GB 提升至60GB，空间长期有效'
  - [2] 2026-10-21: homepage '联通云盘-开启美好时光|不限速'
  - [3] 2026-10-21: + https://github.com/OpenListTeam/wopan-sdk-go — maintained driver + SDK
- sources:
  - [1] https://forum.naixi.net/thread-5251-1-1.html
  - [2] https://pan.wo.cn/
  - [3] https://docs.oplist.org/guide/drivers/wopan
