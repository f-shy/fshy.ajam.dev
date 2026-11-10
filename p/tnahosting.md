# TNAHosting

> tnahosting.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tnahosting/ | JSON https://fshy.ajam.dev/api/v1/entity/tnahosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TNAHosting

- `compute/tnahosting` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:42.901Z (live) | stale on 2026-12-08
- url https://tnahosting.net/kvm-ssd-vps/
- price parsed USD 1.33/mo
- free tier: SSD KVM 1GB at USD 1.33/month billed USD 16 annually: 2 vCPU, 1 GB RAM, 30 GB SSD, 15 TB traffic, 1 IPv4 with IPv6 available, SolusVM control panel, Chicago Illinois (the tracker's location; the site's own menu names 'Looking Glass (Chicago, IL)'). The 2 GB plan is USD 2.00/month billed USD 24 annually with 2 vCPU, 50 GB SSD and 20 TB. Monthly plans sit above it: USD 5 for 4 vCPU, 4 GB, 100 GB SSD and 30 TB, and USD 9 for 4 vCPU, 8 GB, 200 GB SSD and 45 TB. The tracker's cheapest row is the 2 GB plan, so the vendor page carries a cheaper plan than the tracker lists, and its transfer allowances are much larger than the tracker shows. No renewal price is printed on the pages read, and on 2026-11-07 the order pages of the record's plans answer out of stock. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 15 TB a month of traffic is included on the USD 16 plan and 20 TB on the USD 24 plan; no overage price is stated on the page read | metered: yes | free allowance: 15 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 15 TB a month of traffic is the plan's stated allowance at USD 16 a year; no port speed is stated on this card and no overage rule is published, so the allowance is the wall [1]
- limits note: 15 TB a month of traffic is the plan's stated allowance at USD 16 a year; no port speed is stated on this card and no overage rule is published, so the allowance is the wall
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the card names 'SolusVM Control Panel'; the site links a VPS panel at vps.tnahosting.net and there are separate panels for hybrid, Ryzen and dedicated lines. No API is documented on the page read
- composes with: 15 TB of traffic for USD 16 a year, and 30 TB for USD 5 a month on the 4 GB plan, are the largest metered transfer allowances among the USD-priced plans among documented hosts, so this suits a download or mirror node whose bottleneck is bytes rather than CPU
- reliability: the order pages of the record's SSD KVM plans answered WHMCS 'Out of Stock' with orders suspended on 2026-11-07; the marketing cards still print the prices.
- notes: This is the clearest tracker gap in this category: the vendor sells a USD 16/year plan that the tracker does not list, so the tracker's USD 24 entry is not the floor. The 15 TB figure is traffic, not storage, and the disk is 30 GB, which is why the annual plan is cheap. The USD 5 monthly 4 GB plan is the better value at 30 TB, and the tracker lists neither plan. Unverified: whether the annual price renews at 16 USD, and what the traffic counter does at 15 TB. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 30
  - price_on_page: USD 1.33/month for SSD KVM 1GB, billed USD 16 annually
- evidence:
  - [2] 2026-10-22: cheapest row: 'TNAHosting - USD 2.00 / month', 'yearly Service', '2 Intel Cores (shared)', '2,048 MB RAM', '50 GB SSD', '20,480 GB/month bandwidth', '1 Gbps port speed', 'Chicago Illinois U.S.A.'; the page opens with 'starting at USD 24.00 per year'
  - [1] 2026-10-22: plan card, quoted: 'SSD KVM 1GB', 'Only USD 1.33 / month', '(Billed USD 16 annually)', '1 GB RAM', '30 GB SSD', '2 vCPU', '15 TB Traffic', '1 IPv4 (IPv6 Available)', 'SolusVM Control Panel'
  - [1] 2026-10-22: next cards: 'SSD KVM 2GB' at 'USD 2 / month' billed 'USD 24 annually' with '50 GB SSD', '2 vCPU', '20 TB Traffic'; 'SSD KVM 4GB' at 'USD 5 / month'
  - [3] 2026-11-07: the SSD KVM order page suspends orders out of stock; the 2 GB page served the same body | capture: sha256:74fcb6826cecf64453b37e2567e91d98f668a7e45878eb24edaa1a4598dbaa5e | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available.
  - [1] 2026-11-07: the 1 GB card still prints the monthly and billed-annual prices and no renewal price | capture: sha256:580edf1fff9a0ccb529493a5ac2a7798bf3d69e29c2796752d72249b8499a38a | quote: Only **$1.33 **/ month
  - [1] 2026-11-07: the 1 GB card prices are unchanged | capture: sha256:580edf1fff9a0ccb529493a5ac2a7798bf3d69e29c2796752d72249b8499a38a | quote: Only **$1.33 **/ month
- sources:
  - [1] https://tnahosting.net/kvm-ssd-vps/
  - [2] https://vpspricetracker.com/provider/TNAHosting/vps
  - [3] https://tnahosting.net/billing/index.php/store/kvm-ssd/ssd-kvm-1gb
