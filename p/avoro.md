# Avoro

> avoro.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/avoro/ | JSON https://fshy.ajam.dev/api/v1/entity/avoro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Avoro

- `compute/avoro` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:02.760Z (live) | stale on 2026-12-08
- url https://avoro.eu/en/vps
- price parsed USD 4.59/mo
- free tier: Basic S at EUR 4.07 per month excluding VAT when paid quarterly: 1 shared vCPU on a Xeon Gold-class host, 2 GB DDR4 ECC RAM, 20 GB NVMe, 10 TB traffic included, up to 1 Gbit/s, IPv4 + IPv6, Frankfurt. The Basic ladder is S 4.07, M 7.13 (2 vCPU / 4 GB / 40 GB), L 12.26 (4 / 8 / 80), XL 21.09 (8 / 16 / 160), all with 10 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 TB included on every Basic plan; after the allowance the speed is reduced to 10 Mbit/s at no extra cost, and traffic can be added at any time at EUR 1.00 per TB excl. VAT in steps of 5… | metered: yes | free allowance: 10 TB/month | price per TB: EUR 1.00 | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 10 TB included on the Basic class at up to 1 Gbit/s; the Standard class doubles the allowance to 20 TB but starts at EUR 8.50, so on Basic the monthly counter is the first limit a crawler meets. [1]
- limits note: 10 TB included on the Basic class at up to 1 Gbit/s; the Standard class doubles the allowance to 20 TB but starts at EUR 8.50, so on Basic the monthly counter is the first limit a crawler meets.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor runs its own AS58212 network and documents DDoS protection and a prepaid model, with no API named on the page
- composes with: 2 GB and 20 GB of NVMe in Frankfurt for EUR 4.07 excluding VAT, with data stored three times on separate servers, is the strongest redundancy claim among evaluated providers at the price; 10 TB is enough for a crawler at moderate rate.
- reliability: no reliability event recorded
- notes: The two prices are consistent once VAT is added: 4.07 x 1.19 = 4.84, which is exactly the tracker's quarterly-derived monthly figure, and the vendor states prices exclude VAT. That arithmetic is an observation, not a statement the tracker makes. The cart page itself prints 4.84 EUR as the monthly equivalent of the quarterly cycle, whose summary reads 12.20 EUR plus 2.32 EUR VAT, 14.52 EUR due for the quarter. The cart page offers Quarterly (default), Semi-Annually and Annually and no monthly billing cycle; the shortest term is quarterly, and no renewal figure is printed on it. Avoro is a part of dataforest; the site's owner meta tag names dataforest GmbH.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - monthly_eur: 4.07
  - annual_eur: 58.08
  - renewal_eur: not published: the cart prints cycle prices and no renewal figure; read at https://avoro.eu/cp/index.php?rp=/store/vps/basic-s&language=english
  - term: quarterly (the selector's default), semi-annually and annually; no monthly billing cycle exists
  - in_stock: no stock counter is printed on the plan page or the cart; the cart resolves the Basic S product with its price summary, so the plan is orderable
  - cart_url: https://avoro.eu/cp/index.php?rp=/store/vps/basic-s&language=english
  - price_on_page: EUR 4.07/month for Basic S (excluding VAT, when paid quarterly)
- evidence:
  - [1] 2026-10-22: table row quoted: '| S | 1 | 2 GB | 20 GB | 10 TB | 4.07 EUR when paid quarterly |', under heading 'Basic' with 'Xeon Gold-class', 'shared vCPUs', 'DDR4 ECC', 'up to 1 Gbit/s'
  - [1] 2026-10-22: page header: 'from 4.07 EUR per month excl. VAT, when paid quarterly'; footer: 'All prices excl. VAT - IPv4 and IPv6 included with every model'; Standard class XS at 8.50 EUR with 20 TB
  - [2] 2026-10-22: tracker's cheapest row: 'Avoro - 4.84 / month', 'quarterly Service', 'cpu 1 Intel Cores (shared)', 'ram 2,048 MB RAM', 'disk 20 GB NVMe', 'bandwidth 10,240 GB/month bandwidth', 'rj45 1 Gbps port speed', city Frankfurt Germany; header 'starting at 14.52 per quarter'
  - [3] 2026-11-07: the cart's order summary prices Basic S quarterly at 12.20 EUR plus 2.32 EUR VAT (19.00%), 14.52 EUR total due today | capture: sha256:f82ca86d053148e288b2685d5a73309dedd9fb023bbfd1f23ab0ca3d53767c98 | quote: Quarterly:12,20 EUR MwSt @ 19.00%:2,32 EUR Total Due Today14,52 EUR
  - [1] 2026-11-07: the traffic FAQ states the 10 Mbit/s throttle after the allowance and prices added traffic at EUR 1.00 per TB excl. VAT in steps of 5 TB | capture: sha256:6d9fa2179a0079673ccb7792eb11338b06845dd861e84439c97b390b0ad480c2 | quote: Yes, then we limit the bandwidth to 10 Mbit/s at no extra cost, so you never get a surprise bill. If you need more, you can add traffic at any time: €1.00 per TB excl. VAT, in steps of 5 TB.
  - [1] 2026-11-07: the traffic FAQ prices added traffic at EUR 1.00 per TB excl. VAT, in steps of 5 TB | capture: sha256:6d9fa2179a0079673ccb7792eb11338b06845dd861e84439c97b390b0ad480c2 | quote: Yes, then we limit the bandwidth to 10 Mbit/s at no extra cost, so you never get a surprise bill. If you need more, you can add traffic at any time: €1.00 per TB excl. VAT, in steps of 5 TB.
  - [3] 2026-11-07: the cart page's footer names Avoro a part of dataforest | capture: sha256:f82ca86d053148e288b2685d5a73309dedd9fb023bbfd1f23ab0ca3d53767c98 | quote: All Rights Reserved.
  - [1] 2026-11-07: the plan page's Basic table prices S at 4.07 EUR net monthly when paid quarterly: 1 shared vCPU, 2 GB RAM, 20 GB NVMe, 10 TB traffic | capture: sha256:6d9fa2179a0079673ccb7792eb11338b06845dd861e84439c97b390b0ad480c2 | quote: | S | 1 | 2 GB | 20 GB | 10 TB | 4.07 € when paid quarterly |
  - [3] 2026-11-07: the cart prints the quarterly cycle's monthly equivalent, 4.84 EUR incl. VAT | capture: sha256:dfe6bec08d81205b0f58cde59f5e2c0ebe8a87d1459a8257ee8bcb78bb6745b2 | quote: 4.84 EUR Monthly
  - [3] 2026-11-07: the cart's Annually block prices the annual cycle at 58.08 EUR gross | capture: sha256:dfe6bec08d81205b0f58cde59f5e2c0ebe8a87d1459a8257ee8bcb78bb6745b2 | quote: 58.08 EUR
  - [3] 2026-11-07: the cart's cycle blocks print the term totals and no renewal figure | capture: sha256:dfe6bec08d81205b0f58cde59f5e2c0ebe8a87d1459a8257ee8bcb78bb6745b2 | quote: 58.08 EUR
  - [3] 2026-11-07: the cart's cycle selector defaults to quarterly; the selector's radios are quarterly, semiannually and annually and no monthly radio exists in the page | capture: sha256:aea2bc68c5e2782e7142dba68fff188d624fa0910333296a495d62fbce96ed9c | quote: type="radio" value="quarterly" name="billingcycle" checked=""
  - [3] 2026-11-07: the cart resolves the Basic S product with its order summary | capture: sha256:dfe6bec08d81205b0f58cde59f5e2c0ebe8a87d1459a8257ee8bcb78bb6745b2 | quote: VPS - Basic S
  - [3] 2026-11-07: the captured page is the Avoro cart | capture: sha256:aea2bc68c5e2782e7142dba68fff188d624fa0910333296a495d62fbce96ed9c | quote: <title>Shopping Cart - Avoro - a part of dataforest</title>
  - [1] 2026-11-07: the plan page still prices Basic S at 4.07 EUR net monthly when paid quarterly, 1 vCPU, 2 GB RAM, 20 GB NVMe, 10 TB | capture: sha256:6d9fa2179a0079673ccb7792eb11338b06845dd861e84439c97b390b0ad480c2 | quote: | S | 1 | 2 GB | 20 GB | 10 TB | 4.07 € when paid quarterly |
- sources:
  - [1] https://avoro.eu/en/vps
  - [2] https://vpspricetracker.com/provider/Avoro/vps
  - [3] https://avoro.eu/cp/index.php?rp=/store/vps/basic-s&language=english
