# VIP Cloud

> vipserver.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vipserver/ | JSON https://fshy.ajam.dev/api/v1/entity/vipserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VIP Cloud

- `compute/vip-cloud` | qualifies-with-caveat | evidence reported | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vipserver.cloud/
- free tier: Free 2 vCPU / 2 GiB / 20 GB cloud server in Los Angeles on CN2 GIA, China Unicom 9929 and China Mobile CMIN2 return routes, quoted as 美国2H2G 云服务器 免费领取 最高可领10年 (a US 2H2G cloud server, free, claimable for up to ten years). The first grant is three days; renewal is earned through the referral programme. The paid ladder starts at CNY 199 a year for 8 vCPU / 8 GiB / 50 GB SSD / 20 Mbps. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-renewable
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: A community report describes the first grant as free with no stated verification, and one thread reports an account being asked for further verification when a payment failed. No vendor page read states the registration fields.
- interface: unknown
- limits:
  - write-gated (binding): The machine runs three days and renewal is earned by recruiting, so the free tier is a promotion loop rather than a standing allowance; a user who does not bring in referrals loses the box every three days. [1]
- limits note: The machine runs three days and renewal is earned by recruiting, so the free tier is a promotion loop rather than a standing allowance; a user who does not bring in referrals loses the box every three days.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A free 2 GiB box on premium China-return routes is a cheap origin for a proxy front, and it composes with any free IPv4 tunnel for inbound; the renewal loop is what breaks it.
- reliability: no reliability event recorded
- notes: New to documented records. The vendor homepage returned a 403 upstream status while still yielding the body, so the extraction is real text but the read is not a clean 200; that is recorded rather than smoothed over. The CNY 199/year 8 vCPU 8 GiB plan is the largest machine found for that money among documented hosts and belongs in the floor comparison.
- extras:
  - facets.class: perpetual-vps
  - facets.free_tier_kind: perpetual-renewable
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: page states 学生初创者免费计划, 美国2H2G 云服务器 免费领取 最高可领10年, and lists LAX-Pro.VPS.Project-199 at ¥199/年 with 8核 8G 50G SSD 20M, quoted
  - [2] 2026-10-22: a community thread states 首次免费体验3天，续期 through the referral programme, quoted from the snippet
  - [3] 2026-10-22: a user test of the ten-year free machine lists 2 cores, 2 GiB RAM, 20 GB disk and unlimited monthly traffic on CN2GIA plus 9929 plus CMIN2
  - [4] 2026-10-22: a dissenting report claims the site only pays rewards when the recruit tops up, which is the reliability side of the same renewal mechanic
- sources:
  - [1] https://www.vipserver.cloud/
  - [2] https://www.nodeseek.com/post-947314-1
  - [3] https://www.nodeseek.com/post-990236-1
  - [4] https://www.nodeloc.com/t/topic/107011
