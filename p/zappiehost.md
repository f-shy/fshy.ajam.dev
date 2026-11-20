# Zappie

> zappiehost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zappiehost/ | JSON https://fshy.ajam.dev/api/v1/entity/zappiehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zappie

- `compute/zappie` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-12-08
- url https://zappiehost.com/new-zealand-linux-ssd-vps-servers
- price parsed USD 6.5/mo
- free tier: Starter 512 MB VPS [NZ]: USD 6.50 per month on monthly billing and USD 27.00 per six months on the semi-annual term the marketing page advertises, both as the cart renders ('Monthly:$6.50 USD' and 'Semi-Annually:$27.00 USD', each also printed as the total due today, setup USD 0.00); derived USD 27.00 / 6 months = USD 4.50 per month, matching the page's printed $4.50/mo. The store listing prints monthly starting prices for every tier: 512 MB USD 6.50, 1 GB USD 10.00, 2 GB USD 18.50, 4 GB USD 27.50; the carts of the 1 GB, 2 GB and 4 GB plans price the semi-annual term at USD 42.00, USD 78.00 and USD 114.00 (derived USD 7.00, USD 13.00 and USD 19.00 per month). Annual billing appears only inside the cart's cycle options: the cart render for the 512 MB plan lists USD 54.00 (derived USD 54.00 / 12 = USD 4.50 per month) and USD 108.00. Renewal price: not published on any page read. No sold-out marker in any cart read; every cart read renders the plan with prices and a USD 0.00 setup fee. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 200 GB a month of traffic on a 1 Gbps port on the entry plan; no overage price published on the page read | metered: yes | free allowance: 200 GB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 200 GB a month on the entry plan, the tightest allowance among documented hosts. The plan is LXC on the budget page rather than KVM, which the vendor separates into its own KVM pages. [1]
- limits note: 200 GB a month on the entry plan, the tightest allowance among documented hosts. The plan is LXC on the budget page rather than KVM, which the vendor separates into its own KVM pages.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a billing panel is linked and BGP peering is offered; no API or client is documented on the page read
- composes with: this is the only New Zealand, South Africa and Chile option among documented hosts: $4.50 buys Oceania latency that no other provider here sells, and the 200 GB allowance caps it at a resolver or a small API rather than a crawler
- reliability: no reliability event recorded
- notes: Two things are stated carefully. The currency is printed as '$' with no code anywhere on the pages read, so no USD or NZD conversion is asserted. And the price is a semi-annual prepay figure, which the page qualifies in its own footnote; the monthly rate was not read. The tracker says $6.50 for the same 512 MB plan while the vendor currently prints $4.50, and the vendor is first-party, so the lower figure is recorded with the tracker row kept as evidence.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 30
  - price_on_page: USD 6.50/month for Starter 512 MB VPS [NZ] on monthly billing
  - renewal_usd: not published: the store listing prices the plan from USD 6.50 monthly and prints no renewal figure
- evidence:
  - [1] 2026-10-22: plan card: '512MB VPS / $ / 4.50 / /mo / Starter New Zealand VPS / 512MB RAM / 1 CPU CORE / 30GB SSD Storage / 200GB Traffic (1Gbps Port) / Dedicated IPv4 & IPv6 Address' with the footnote 'Advertised prices are on semi-annual plans'
  - [1] 2026-10-22: higher tiers: '1GB VPS $ 7.00 /mo / Medium ... 1GB RAM / 2 CPU CORE / 50GB SSD / 400GB Traffic' and '4GB VPS $ 19.00 /mo / Super ... 4GB RAM / 6 CPU CORE / 150GB SSD / 1.2TB Traffic'
  - [2] 2026-10-22: tracker's same plan carries a different price: '$6.50 / month 1 Intel Cores (shared) 512 MB RAM 30 GB SSD 200 GB/month bandwidth 1 Gbps port speed IPv4 + IPv6 New Zealand'
  - [3] 2026-11-07: the cart prices the 512 MB plan at USD 27.00 for the semi-annual term | capture: sha256:b36b4d148bc88fb7fa834b7f5474025609334b6791a56410c2f2680c6fb24ca1 | quote: Semi-Annually:$27.00 USD
  - [4] 2026-11-07: the cart prices the 512 MB plan at USD 6.50 on monthly billing | capture: sha256:27d65c61240e7910da6a03167dd8b109889babedc39f5291a2a0b5511ace8212 | quote: Monthly:$6.50 USD
  - [5] 2026-11-07: the store listing prints USD 6.50 as the monthly starting price of the 512 MB plan | capture: sha256:b27afb485220d3a0be260425343301151796d98ed96b4e0d8d2db6215f48052b | quote: Starting from $6.50 USD Monthly
  - probe:https://billing.zappiehost.com/cart.php?a=add&billingcycle=semiannually&pid=54 2026-11-07: the cart render's price list contains USD 54.00; with the semi-annual cart at USD 27.00 per six months this is the twelve-month total at the same USD 4.50 a month | capture: sha256:d6ecf1126e21836f2d89631d3432796903d5d55e8d657b80ee70532e5d7a3ca0 | quote: "$54.00"
  - [1] 2026-11-07: the marketing page's per-month rates are semi-annual-plan rates, and the plan cards print 200 GB Traffic (1Gbps Port) on the entry plan | capture: sha256:abfff01f1467fb3ce4a97b035321564fb23aaccca1d762c430f25ae3e7306158 | quote: Advertised prices are on semi-annual plans
  - [5] 2026-11-07: the vendor's own store listing prices the 512 MB plan from USD 6.50 monthly | capture: sha256:b27afb485220d3a0be260425343301151796d98ed96b4e0d8d2db6215f48052b | quote: Starting from $6.50 USD Monthly
- sources:
  - [1] https://zappiehost.com/new-zealand-linux-ssd-vps-servers
  - [2] https://vpspricetracker.com/provider/Zappie/vps
  - [3] https://billing.zappiehost.com/cart.php?a=add&billingcycle=semiannually&pid=54
  - [4] https://billing.zappiehost.com/index.php?rp=/store/new-zealand-vps/512mb-vps-nz
  - [5] https://billing.zappiehost.com/index.php?rp=/store/new-zealand-vps
