# 62Cloud

> 61cloud.net | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/61cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/61cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 62Cloud / 61Cloud (61cloud)

- `netdisk-pan/62cloud-61cloud` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.61cloud.net
- free tier: 61 GB on registration, per a forum post: '国内商家，注册送61g' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [1]
- retention: Not published | source: [1]
- egress: Direct links need a CNY 0.10 Alipay payment for real-name verification; WebDAV is given away free around holidays, which is a promotion and not a standing entitlement | metered: no | source: [1]
- identity: country-phone | detail: a Chinese-language signup; the forum post describes a domestic vendor and a CNY 0.10 Alipay real-name payment for direct links. | country: 86
- interface: webdav
- limits:
  - per-object-cap (binding): 61 GB account total, which is the cap in practice [1]
  - write-gated: WebDAV is issued around holidays and is not a standing entitlement [1]
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
  - [1] 2026-10-21: '61Cloud 这个也挺不错，国内商家，注册送61g。不过国内直链功能需要支付宝付1毛钱用于实名，逢年过节还有免费webdav功能发放'
- sources:
  - [1] https://linux.do/t/topic/854248
