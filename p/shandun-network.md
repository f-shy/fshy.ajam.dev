# ShanDun Network

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shandun-network/ | JSON https://fshy.ajam.dev/api/v1/entity/shandun-network.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ShanDun Network

- `compute/shandun-network` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.nodeseek.com/post-863994-1
- free tier: A German AS9929 cloud server with 1 core, 1 GB RAM, a 10 GB system disk, 300 Mbps and 500 GB a month, one IPv4, offered at about USD 1.01 for the first month after a permanent 20 percent code is stacked with a one-time 40 percent first-month code. The list price is not printed in the post and was not read, so only the discounted first month is stated here. The post is the vendor's own announcement account on the forum, and it also gives away 30 units of the same configuration. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB a month at 300 Mbps; no overage price stated | metered: yes | free allowance: 500 GB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 500 GB a month at 300 Mbps is the stated allowance, which the port could exhaust in under four hours of saturation, so the byte cap binds; no overage price is stated. [1]
- limits note: 500 GB a month at 300 Mbps is the stated allowance, which the port could exhaust in under four hours of saturation, so the byte cap binds; no overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order through shandun.net store pages; no API documented
- composes with: A German AS9929 route at a first-month figure near USD 1 is the cheapest way among documented hosts to test whether a Chinese-optimised German route behaves differently from a plain Frankfurt one
- reliability: no reliability event recorded
- notes: Source: nodeseek promotion thread, which is the vendor posting under its own account. The vendor's order page renders as a JavaScript template and prints no price, so only the discounted first month and the configuration are recorded. Unverified: the list price and the renewal price. The nodeseek index itself answered with an IPv6-disabled redirect, so this came from the search snippet path; the post body was read in full. Rendering and provenance: currency written as USD as the post states it.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-23: configuration table quoted from the vendor's post: '线路 | AS9929', 'CPU | 1 核', '内存 | 1GB', '系统磁盘 | 10GB', '带宽 | 300Mbps', '流量 | 500GB', 'IPv4 | 1 个'
  - [1] 2026-10-23: price quoted: '叠加后首月价格最低约 $1.01，具体以结算页面显示为准'; codes '2XrUkFhPu' at '按产品原价 8 折' recurring and '9g2fA7Laz' at '40% OFF 首月优惠，不可循环使用，每个用户仅可用一次'
  - [2] 2026-10-23: the vendor's order page is an unrendered JavaScript template: it prints '{{lang.store_product_selection}}', '{{commonData.currency_prefix}}{{item.price}}' and no price, so the list price could not be read
- sources:
  - [1] https://www.nodeseek.com/post-863994-1
  - [2] https://www.shandun.net/store/cloud-servers.html?id=10
