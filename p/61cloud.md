# 62Cloud

> 61cloud.net | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/61cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/61cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 62Cloud / 61Cloud (61cloud)

- `netdisk-pan/62cloud-61cloud` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T14:05:48.228Z (live) | stale on 2026-12-10
- url https://www.61cloud.net
- free tier: 61 GB on registration, per a forum post: '国内商家，注册送61g' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [2]
- retention: Not published | source: [2]
- egress: Direct links need a CNY 0.10 Alipay payment for real-name verification; WebDAV is given away free around holidays, which is a promotion and not a standing entitlement | metered: no | source: [2]
- identity: country-phone | detail: a Chinese-language signup; the forum post describes a domestic vendor and a CNY 0.10 Alipay real-name payment for direct links. | country: 86
- interface: webdav
- limits:
  - per-object-cap (binding): 61 GB account total, which is the cap in practice [2]
  - write-gated: WebDAV is issued around holidays and is not a standing entitlement [2]
- binding note: 61 GB is 12% of a 500 GB threshold, and the only protocol it offers is a promotion. Either number alone closes it.
- tooling: WebDAV when granted; otherwise the web interface only
- composes with: Nothing about it scales and the protocol is the one that closes
- reliability: A small domestic host whose WebDAV availability is seasonal, so any automation built on it breaks on a holiday schedule the operator does not publish
- notes: Documentation is derived from forum reports, placing confidence at reported without a dedicated vendor pricing URL. Storage is limited to 61 GB with seasonal WebDAV access.
- extras:
  - access_mode: registration-gated
  - evidence_quality: one forum post
  - realname_cost: CNY 0.10 via Alipay, for direct links only
- evidence:
  - [2] 2026-10-21: '61Cloud 这个也挺不错，国内商家，注册送61g。不过国内直链功能需要支付宝付1毛钱用于实名，逢年过节还有免费webdav功能发放'
  - [1] 2026-11-19: a current forum post about the 六一云盘 service still states 61G of space for free users | capture: sha256:a017e067a6e6ea33a2684546f78a18532b78964430c928b7cb1626cd69240865 | quote: 61G不限速空间（免费用户通用）
  - [1] 2026-11-19: the record's cited linux.do topic now holds unrelated content, while this forum post states the 61G free allowance | capture: sha256:a017e067a6e6ea33a2684546f78a18532b78964430c928b7cb1626cd69240865 | quote: 61G不限速空间（免费用户通用）
  - [3] 2026-11-25: WebDAV is available after purchasing a membership | capture: sha256:f067cbd37d0d211c3b8b025da64f3e01dbdab62de01dd322b9f738b1921d89c9 | quote: 用户购买会员后支持使用WebDAV功能。
- sources:
  - [1] https://feedbbs.com/nodeseek/80206
  - [2] https://linux.do/t/topic/854248
  - [3] https://vip.now61.cn/post/153.html
