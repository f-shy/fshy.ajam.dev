# OrangeVPS

> orangevps.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orangevps/ | JSON https://fshy.ajam.dev/api/v1/entity/orangevps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OrangeVPS

- `compute/orangevps` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:58.954Z (live) | stale on 2026-11-22
- url https://orangevps.com/nvme-vps/
- price parsed USD 1.41/mo
- free tier: SP26-1 at USD 1.96/month on the 3-month term (USD 5.88 charged per quarter), USD 1.81/month on 6 months and USD 1.41/month on 12 months: 1 vCPU, 1 GB RAM, 20 GB NVMe, 2 TB transfer, 100 Mbps; locations Kansas City (no surcharge), Singapore +USD 2.00/month, Hong Kong +USD 3.00/month; 1 available on the cart's category page; strictly no refunds. The vendor page's BASIC 1 is out of stock on the US cart at its listed price, and the Asia cart's BASIC-AP-1 is in stock (both in the evidence rows). Annual: USD 1.41/month on the 12-month term (USD 16.92 a year). Renewal: not published. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2000 GB a month on the recorded row and 2 TB on BASIC 1; the vendor page publishes no overage rate | metered: yes | free allowance: 2000 GB/month on the recorded row; 2 TB on BASIC 1 | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2000 GB a month on the tracker's quarterly row. BASIC 1 carries 2 TB and BASIC 2 4 TB on the vendor page. The tracker shows a 0.1 Gbps port on the Kansas City row against the vendor's stated 1 Gbps, so the effective throughput may be ten times lower than the plan name suggests. [1]
- limits note: 2000 GB a month on the tracker's quarterly row. BASIC 1 carries 2 TB and BASIC 2 4 TB on the vendor page. The tracker shows a 0.1 Gbps port on the Kansas City row against the vendor's stated 1 Gbps, so the effective throughput may be ten times lower than the plan name suggests.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS-style portal at portal.orangevps.com with login, registration and a knowledgebase; the vendor page says OS instal plus additional IPv4 at USD 2/month each; no API was stated on the pages read
- composes with: USD 1.96 a month for a 1 GB box with 2 TB is the cheapest US presence among documented hosts after NATVPS, and the 0.1 Gbps port on the Kansas City row makes it a control-plane box: a scheduler, a DNS primary, a monitoring probe. It is not a transfer host and not a crawler.
- reliability: the vendor FAQ states there are no service contracts and cancellation or upgrade is available at any time; no uptime figure was stated on the page read
- notes: or docs/ (searched both trees for orangevps, no hit). The vendor plan cards render as bare 'Order Now' buttons to the text extractor; the order links live in a WordPress AJAX endpoint and the plans sell through the WHMCS portal at portal.orangevps.com, whose store categories carry the prices and stock counts. SP26-1 is a current offer in the portal's 'VPS BUDGET (ALWAYS PROMO)' category with 1 available and a 100 Mbps port, so the tracker's row is neither stale nor mis-speeded.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: USD 1.96/month for SP26-1 on the 3-month term; USD 1.81/month on 6 months; USD 1.41/month on 12 months; renewal: not published
- evidence:
  - [2] 2026-10-22: cheapest row: '$1.96 / month', 'quarterly Service', '1 Intel Cores (shared)', '1,024 MB RAM', '20 GB NVMe', '2,000 GB/month bandwidth', '0.1 Gbps port speed', 'IPv4 + IPv6', Kansas City Missouri; header 'starting at $5.88 per quarter'
  - [1] 2026-10-22: plan card quoted: 'BASIC 1', '$4', '/month', '1 vCPU', '2GB Memory', '25GB Storage NVMe', '2TB Transfer Data', '1Gbps Bandwidth'; BASIC 2 at USD 6/month with 2 vCPU, 4 GB, 40 GB and 4 TB
  - [1] 2026-10-22: FAQ quoted: 'Is there any discount for pre-paying? Yes, if you buy a package for more than 1 month it will be cheaper.' and 'the price for each additional IP address is $2/month'
  - [3] 2026-11-07: the SP26-1 cart prices USD 1.96 per month on the 3-month term, USD 1.81 on 6 months, USD 1.41 on 12 months | capture: sha256:055174f9a5614109c35f775513d7d6f4158749eaf308f9381a20ce908968b4c8 | quote: 3 Month Price - $1.96 USD 6 Month Price - $1.81 USD 12 Month Price - $1.41 USD
  - [4] 2026-11-07: the cart's VPS BUDGET page lists SP26-1 with 1 available, 20 GB NVMe, 1 GB RAM, 1 vCPU, 2 TB, 100 Mbps, from USD 1.96 a month | capture: sha256:9e4ac10eec5e65c755290a4a7d831f2d3eccafda3bfc32abd22939efd2e37301 | quote: SP26-1 1 Available 20 GB NVMe SSD 1 GB RAM DDR4 1 vCPU 2 TB Transfer Data 100 Mbps Bandwidth IP Addresses Features Location US, SG, HK, TY Strictly no refunds / 不退款退Credits Starting from $1.96 USD Monthly Order Now
  - [5] 2026-11-07: BASIC-US-1's cart price is USD 4.00 a month but the plan shows 0 available | capture: sha256:96816ef27dae2de7e9b01f64049dcc95796e44083665277d40be7d8618d24759 | quote: BASIC-US-1 0 Available 25 GB NVMe SSD Storage 2 GB RAM 1 vCPU IP Addresses 2 TB Transfer Data KVM Virtualization Location Kansas City, Missouri, USA Starting from $4.00 USD
  - [6] 2026-11-07: the Asia cart's BASIC-AP-1 is USD 6.00 a month, in stock (Order Now, no stock badge) | capture: sha256:8d918a2c6dab7a9af98b630b321facf1ef240a7a6c45cd88d5e3ec88feb1ac63 | quote: BASIC-AP-1 25 GB NVMe SSD Storage 2 GB RAM 1 vCPU 2 TB Transfer Data 1 Gbps Bandwidth IP Addresses Features Starting from $6.00 USD Monthly Order Now
  - [3] 2026-11-07: the SP26-1 cart prices the 3-, 6- and 12-month terms at 1.96, 1.81 and 1.41 USD per month, and its order summary charges 5.88 USD for the 3-month term | capture: sha256:055174f9a5614109c35f775513d7d6f4158749eaf308f9381a20ce908968b4c8 | quote: 3 Month Price - $1.96 USD 6 Month Price - $1.81 USD 12 Month Price - $1.41 USD
  - [3] 2026-11-07: the SP26-1 cart order summary charges 5.88 USD for the 3-month term at 1.96 USD a month | capture: sha256:055174f9a5614109c35f775513d7d6f4158749eaf308f9381a20ce908968b4c8 | quote: Quarterly: $5.88 USD
  - [4] 2026-11-07: the cart category page lists SP26-1 with one available and a from-price of 1.96 USD a month | capture: sha256:2723906e774f440b402d1389094f8c7973d5dd3df4b4e424daa10139cf51c2a0 | quote: SP26-1 1 Available
  - [5] 2026-11-07: the US cart lists BASIC-US-1 at 4.00 USD a month with none available | capture: sha256:1f6a325b70cd9bb8d2a3e1e0c66ef780d5f3d0cbf90769fe644200243ac1ac5a | quote: BASIC-US-1 0 Available
  - [6] 2026-11-07: the Asia cart's BASIC-AP-1 card prices 6.00 USD a month with an Order button and no stock badge | capture: sha256:394010b8d084710afd68419313bc4b78772ad585f916e3a9de95f9c82120a0b7 | quote: $6.00 USD
  - [3] 2026-11-07: the SP26-1 cart prices the 3-, 6- and 12-month terms at 1.96, 1.81 and 1.41 USD per month | capture: sha256:055174f9a5614109c35f775513d7d6f4158749eaf308f9381a20ce908968b4c8 | quote: 3 Month Price - $1.96 USD 6 Month Price - $1.81 USD 12 Month Price - $1.41 USD
- sources:
  - [1] https://orangevps.com/nvme-vps/
  - [2] https://vpspricetracker.com/provider/OrangeVPS/vps
  - [3] https://portal.orangevps.com/store/vps-budget/sp26-1
  - [4] https://portal.orangevps.com/store/vps-budget
  - [5] https://portal.orangevps.com/store/vps-us-basic-cpu
  - [6] https://portal.orangevps.com/store/vps-ap-basic-cpu
