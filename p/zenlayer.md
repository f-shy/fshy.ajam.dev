# Zenlayer

> zenlayer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenlayer/ | JSON https://fshy.ajam.dev/api/v1/entity/zenlayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zenlayer

- `compute/zenlayer` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:38.826Z (live) | stale on 2026-12-10
- url https://www.zenlayer.com/virtual-machine/
- free tier: The review site offers a 7折 recurring discount code: elastic cloud servers start at USD 8.72 a month and bare-metal servers at USD 134 a month, across 59 countries or regions in Asia, the Americas, Europe and Africa; the cheapest cloud-server row is 1 GB RAM, 1 core and 20 GB NVMe at USD 8.72 a month. Credit card, PayPal, Alipay and cryptocurrency payment is stated. | unit: unlimited | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
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
  - [3] 2026-11-25: the review site states the 7折 recurring code, the USD 8.72 cloud-server and USD 134 bare-metal floors, and 59 countries or regions | capture: sha256:0809cee8c8b5cb6935360e4b56f6c68da920b7497d12c2e46be63c70eedfb784 | quote: [zenlayer](https://www.zhujiceping.com/tag/zenlayer)为主机测评/zhujiceping.com独家定制了7折循环优惠码，购买云服务器低至8.72美元/月、独立服务器/物理机低至134美元/月，机房可选亚洲/美洲/欧洲/非洲：香港、韩国、日本、新加坡、泰国、越南、巴基斯坦、印度尼西亚、菲律宾、阿联酋、美国、巴西、墨西哥、德国、法国、英国、荷兰、芬兰、尼日利亚等59个国家或者地区… 支持信用卡、PayPal、支付宝、加密货币等多种付款方式。
  - [3] 2026-11-25: the cheapest paid cloud server is USD 8.72 a month with a recurring 30 percent code, bare metal starts at USD 134, across 59 regions | capture: sha256:0809cee8c8b5cb6935360e4b56f6c68da920b7497d12c2e46be63c70eedfb784 | quote: [zenlayer](https://www.zhujiceping.com/tag/zenlayer)为主机测评/zhujiceping.com独家定制了7折循环优惠码，购买云服务器低至8.72美元/月、独立服务器/物理机低至134美元/月，机房可选亚洲/美洲/欧洲/非洲：香港、韩国、日本、新加坡、泰国、越南、巴基斯坦、印度尼西亚、菲律宾、阿联酋、美国、巴西、墨西哥、德国、法国、英国、荷兰、芬兰、尼日利亚等59个国家或者地区… 支持信用卡、PayPal、支付宝、加密货币等多种付款方式。
  - [1] 2026-11-25: the vendor documents web interface, API and Terraform deployment | capture: sha256:5e7ae5311be0cfcdc934cf7a0e7588d3b2daf4a035af5270bd2caff87042bfac | quote: Use our web interface, API, or Terraform to deploy and manage your virtual machines.
- sources:
  - [1] https://www.zenlayer.com/virtual-machine/
  - [2] https://www.zhujiceping.com/youhui
  - [3] https://www.zhujiceping.com/98819.html
