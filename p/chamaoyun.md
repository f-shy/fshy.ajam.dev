# Chamaoyun

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chamaoyun/ | JSON https://fshy.ajam.dev/api/v1/entity/chamaoyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chamaoyun

- `compute/chamaoyun` | fails-identity | evidence reported | binding volume-quota | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.hostloc.com/thread-1411786-1-1.html
- free tier: The cheapest large machine found among evaluated providers: 4 vCPU, 4 GiB RAM, 50 GB system disk, 50 Mbps with a 1 TB monthly cap that falls to 10 Mbps once reached, at CNY 99 a year, quoted as 4C4G 50G 50Mps 99元/年. The vendor sells it as a student offer restricted to ages 18 to 25. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: Three gates stated in the offer post: 18-25 (age 18 to 25), (overseas access blocked), and (a domain with a mainland ICP filing is required, and IP plus port access is not supported). The operator is , trading since 2020, per two reseller profiles.
- interface: unknown
- limits:
  - volume-quota (binding): The 1 TB monthly transfer is the first thing to bind: past it the port drops to 10 Mbps rather than stopping, so a 500 GB day of transfer takes about 111 hours at the throttled rate. The student offer also carries no 24-hour refund. [1]
- limits note: The 1 TB monthly transfer is the first thing to bind: past it the port drops to 10 Mbps rather than stopping, so a 500 GB day of transfer takes about 111 hours at the throttled rate. The student offer also carries no 24-hour refund.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: With a mainland identity and a filed domain, this is 4 cores and 4 GiB for the price of two coffees a year; without them it is unreachable, which is the whole finding.
- reliability: no reliability event recorded
- notes: The floor of the Chinese annual market, with its spec intact: the number is what makes it interesting and the gates are what make it unusable. CNY 99 a year is quoted as written and not converted. The 1 TB cap and the 10 Mbps throttle are the vendor's own words in the offer post, not a measurement.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 50
- evidence:
  - [1] 2026-10-22: the offer post states 处理器：4核心 内存：4gb 硬盘 50g系统盘 带宽50Mbps 限制流量1t/月 达量限速10Mbps 学生特惠：99/年 限制年龄18-25区间, quoted from the snippet
  - [1] 2026-10-22: the same post states 屏蔽海外 不支持ip+端口直接访问 需使用北岸域名 学生特惠机不支持24h无理由退款, quoted
  - [2] 2026-10-22: a reseller profile states 茶猫云(chamaoyun.com)成立于2020年，隶属于成都艾特世纪网络科技有限公司, quoted
- sources:
  - [1] https://www.hostloc.com/thread-1411786-1-1.html
  - [2] https://www.lantizi.com/article/2880.html
