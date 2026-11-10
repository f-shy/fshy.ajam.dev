# vmiss

> vmiss.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vmiss/ | JSON https://fshy.ajam.dev/api/v1/entity/vmiss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vmiss

- `compute/vmiss` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.vmiss.com/
- free tier: CAD 24 per year for the Hong Kong international-line VPS: 1 GB RAM, 1 core, 10 GB SSD, 1 TB a month, 500 Mbps, on NTT plus CMI. The Hong Kong optimised-BGP line starts at CAD 5 per month for 1 GB, 1 core, 10 GB and 300 GB a month, and the three-network premium line at CAD 12 per month for the same shape. The article states the currency is Canadian dollars and that annual billing is discounted to 83 percent of the list price before any coupon. Other locations in the same catalogue are Seoul, Osaka, Tokyo and Los Angeles. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on the CAD 24 annual row, 300 GB a month on the CAD 5 and CAD 12 monthly rows; no overage price stated | metered: yes | free allowance: 1 TB per month on the annual row | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on the CAD 24 annual row and 300 GB a month on the CAD 5 monthly row, so the allowance moves by a factor of three with the line; no overage price is stated. [1]
- limits note: 1 TB a month on the CAD 24 annual row and 300 GB a month on the CAD 5 monthly row, so the allowance moves by a factor of three with the line; no overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS cart at app.vmiss.com; no API documented
- composes with: CAD 24 a year for 1 TB a month in Hong Kong is the lowest annual commitment among documented hosts, which suits a box that must exist for a year but is idle most of it
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing and article, then the vendor page, which answered 403 and carries no plan table. The record is reported for that reason. The article's own title advertises a 9 yuan a month floor, which is a conversion of the CAD 24 annual row and is not repeated here. Rendering and provenance: currency written as CAD exactly as the article states it.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [2] 2026-10-23: cheapest row quoted: '1G | 1核 | 10G | 1T/月 | 500M | 24加元/年' on the '香港VPS - 国际线路（NTT+CMI）' line; '1G | 1核 | 10G | 300G/月 | 5加元/月' on the '优化BGP' line; '1G | 1核 | 10G | 300G/月 | 12加元/月' on '三网优选'
  - [2] 2026-10-23: currency quoted: '1.货币为加拿大元，当前汇率大致4.68'; '官方年付默认8.3折'; coupon 'INTL20%OFF' for the Hong Kong international line
  - [1] 2026-10-23: the vendor page returned upstream_status 403 and a marketing shell only ('fly in the clouds', 'Best Hosting Platform') with no plan table and no price
- sources:
  - [1] https://www.vmiss.com/
  - [2] https://www.zhujiceping.com/90285.html
