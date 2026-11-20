# 迅雷 free account

> xunlei.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xunlei/ | JSON https://fshy.ajam.dev/api/v1/entity/xunlei.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 迅雷 free account (非会员)

- `debrid/xunlei-free-account` | fails-quota | evidence documented | binding per-ip-shaping | category download accelerator, unpaid path | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:28:59.771Z (live) | stale on 2026-12-04
- url https://vip.xunlei.com/vip_service/supervip_info/dist/
- price CNY 0
- free tier: No paid fee. The vendor's privilege page lists, for a non-member, 10GB of cloud drive space, 5GB/month of high-speed cloud-drive download traffic and 3 remote downloads per day on a NAS client; its speed graphic lists 586 KB/s for the un-membered path, so the free account has a small cloud allowance but no cloud-add product at the scale of the paid tiers. | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1] | note: The free path is not byte-metered; it is shaped. 586 KB/s is 50.6 GB/day, or about 1.5 TB/month if the machine is left running.
- per-object cap: Not published on the vendor's privilege page; the non-member cloud drive holds 10GB in total. | source: [1]
- retention: Cloud drive recycle bin: deleted files are kept 10 days for a non-member and for longer on the paid tiers. How long a non-member's files stay in the drive itself is not published. | source: [1]
- egress: Unmetered and shaped. The vendor table puts the un-membered path at 586 KB/s against 15.8 MB/s for 超级会员, a 27x difference on the same file. | metered: no | source: [1]
- identity: any-phone | detail: Same account system as 超级会员: phone plus 微信/QQ QR. Unverified beyond that.
- interface: cli
- limits:
  - per-ip-shaping (binding): 586 KB/s per the vendor speed table; no byte counter [1]
  - volume-quota: non-member: 5GB/month of high-speed cloud-drive download traffic (白金会员: 1TB/month); once used, cloud-drive downloads run at ordinary speed [1]
- limits note: NAS-client remote download: unlimited for the paid tiers, 3 per day for a non-member.
- binding note: The free client path is shaped at 586 KB/s with no byte counter, so the shaping is the measurable ceiling. The cloud-side non-member allowances (10GB of drive space, 5GB/month of high-speed download traffic, 3 NAS remote downloads per day) are too small for server-side retrieval of large volumes.
- interface detail: The same vendor client, without the membership features.
- tooling: Vendor client; the free path is the user's ordinary HTTP/BT downloader.
- composes with: The free path is the fallback when no membership is held: 1.5 TB/month is reachable in principle, but only by leaving a machine on for the whole month; the non-member cloud allowances (10GB of drive space, 5GB/month of high-speed download traffic) are too small to act as a server-side fetch at volume.
- reliability: The 27x gap is the product. The un-membered client path is shaped rather than byte-capped; the cloud-side features carry small non-member allowances (10GB of drive space, 5GB/month of high-speed download traffic).
- notes: Free-tier retrieval through 迅雷 is not a debrid-equivalent: the non-member cloud allowances are small (10GB of drive space, 5GB/month of high-speed download traffic). The value of this record is the 27x number, which prices every other accelerator in the market.
- evidence note: The 586 KB/s figure and the non-member cloud allowances are read from the vendor's privilege page. The speed graphic lists the three figures in the order of the tiers shown; a timed download on a free account would make the speed measured.
- extras:
  - free_kbs: 586
  - member_mbs: 15.8
- evidence:
  - [2] 2026-10-23: '离线下载及高速通道加速已整合为会员加速功能，超级会员是支持的哦。' - the function is now membership-only
  - [1] 2026-11-03: the vendor's privilege table gives a non-member 10GB of cloud drive space (paid tiers 12T, 6T, 3T) | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: | 12T | 6T | 3T | 10GB |
  - [1] 2026-11-03: cloud drive recycle bin keeps deleted files 10 days for a non-member (15, 30, 60 for paid tiers) | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: | 保留60天 | 保留30天 | 保留15天 | 保留10天 |
  - [1] 2026-11-03: the vendor's note on cloud-drive high-speed download traffic: 5GB/month for a non-member, 1TB/month for 白金会员 | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: 白金会员：1TB/月、非会员：5GB/月
  - [1] 2026-11-03: NAS-client remote download: unlimited for the paid tiers, 3 per day for a non-member | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: | 次数无限制 | 次数无限制 | 次数无限制 | 3次/天 |
  - [1] 2026-11-03: the vendor's speed graphic lists 586 KB/s for the lowest tier, against 15.8 MB/s for the top | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: 15.8 MB/s 7.82 MB/s 586 KB/s
- sources:
  - [1] https://vip.xunlei.com/vip_service/supervip_info/dist/
  - [2] https://www.ithome.com/1/012/491.htm
