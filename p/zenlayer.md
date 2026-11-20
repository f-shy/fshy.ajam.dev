# Zenlayer

> zenlayer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenlayer/ | JSON https://fshy.ajam.dev/api/v1/entity/zenlayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zenlayer

- `compute/zenlayer` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.zenlayer.com/virtual-machine/
- free tier: USD 8.72 per month is the stated floor for a cloud server with the vendor's 30 percent code, printed by the review site as a floor of USD 8.72 for a cloud server; the same offer prices bare metal from USD 134 a month across 59 data centres. The vendor page states elastic compute in 20 or more countries, hourly or monthly billing, deployment through a web interface, an API and Terraform, a free virtual firewall, and three bandwidth modes: data transfer, flat-rate capped bandwidth, and aggregated burstable at the 95th percentile. Traffic within a virtual private cloud is free. No plan table and no shape are printed on either page read. | unit: unlimited | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: three modes: data transfer, flat-rate capped bandwidth with unlimited data, and aggregated burstable at the 95th percentile; intra-VPC traffic free | metered: no | free allowance: none stated; intra-VPC transfer is free | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): Bandwidth is bought in one of three modes and the page prints no allowance for any of them, so the mode is the wall: a flat-rate row is capped at its port, a data-transfer row at its bytes, and the 95th-percentile row at an aggregate commitment. The USD 8.72 floor has no published shape. [1]
- limits note: Bandwidth is bought in one of three modes and the page prints no allowance for any of them, so the mode is the wall: a flat-rate row is capped at its port, a data-transfer row at its bytes, and the 95th-percentile row at an aggregate commitment. The USD 8.72 floor has no published shape.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: web console, API and Terraform provider documented on the vendor page; this is the only provider among documented hosts with a Terraform path stated
- composes with: A Terraform and API path with hourly billing across 20 or more countries is the shape a scripted fleet needs, and the 95th-percentile bandwidth mode is the only one among documented hosts priced on aggregate rather than per machine
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing, then the vendor page. Neither page prints a plan row, so the record is reported and the shape is empty rather than guessed. The 30 percent code is the review site's exclusive and may not be available through other channels. Unverified: the console's price for the cheapest hourly shape in Hong Kong. Rendering and provenance: currency written as USD.
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [2] 2026-10-23: offer listing quoted: 'zenlayer独家7折优惠码，云服务器低至$8.72，物理机$134起，香港/台湾/韩国/日本/美国等全球59个机房'
  - [1] 2026-10-23: vendor page quoted: 'Cost-effective compute in 20+ countries', 'Use our web interface, API, or Terraform to deploy and manage your virtual machines', 'Pay by hour', 'Data transfer', 'Flat rate - capped bandwidth: Unlimited data transfer', 'Aggregated burstable 95th', 'Data transfer within a virtual private cloud is free'; no price and no plan row on the page
- sources:
  - [1] https://www.zenlayer.com/virtual-machine/
  - [2] https://www.zhujiceping.com/youhui
