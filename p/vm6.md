# VM6_Networks

> vm6.co.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vm6/ | JSON https://fshy.ajam.dev/api/v1/entity/vm6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VM6_Networks

- `compute/vm6-networks` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T17:40:47.142Z (live) | stale on 2026-12-08
- url https://www.vm6.co.uk/cheap-vps-uk
- price parsed USD 2.34/mo
- free tier: UK Xeon S (order product Budget VPS UK 1) at GBP 1.75 a month on the order page: 1 vCPU, 1 GB ECC DDR4, 20 GB NVMe, 1 dedicated UK IPv4, KVM under the VirtFusion panel, in Norwich. Order page read 2026-11-07: monthly GBP 1.75, quarterly GBP 5.25, 6 months GBP 10.50, 1 year GBP 17.50; the cart totals GBP 1.75 due today and accepts the plan (in stock); renewal price not published on the page. The order form's traffic figure differs from the marketing page's (see egress). Three higher Xeon tiers sit above it; their prices are quoted in the record's evidence rows. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Order form for Budget VPS UK 1: 'Monthly Traffic: 3TB @ 1Gbps' (read 2026-11-07); the marketing page's plan-table figure (2026-10-22) was lower and stays in the record's evidence rows. No overage price is published on either page. | metered: yes | free allowance: 3TB a month per the order form read 2026-11-07; the marketing page's plan-table figure (2026-10-22) was lower and stays in the record's evidence rows | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): The order form read 2026-11-07 states 'Monthly Traffic: 3TB @ 1Gbps' for Budget VPS UK 1; the marketing page's plan-table figure (2026-10-22) was lower and stays in the record's evidence rows. The byte allowance, not the port, is the wall a crawler meets. [1]
- limits note: The order form read 2026-11-07 states 'Monthly Traffic: 3TB @ 1Gbps' for Budget VPS UK 1; the marketing page's plan-table figure (2026-10-22) was lower and stays in the record's evidence rows. The byte allowance, not the port, is the wall a crawler meets.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: VirtFusion panel named on the page; no API or client is documented, and a panel is not a storage or compute interface that can be scripted against from the page read
- composes with: GBP 1.75 for a real KVM slice with a dedicated UK IPv4 is the cheapest always-on presence machine among documented hosts; it is a DNS resolver, an uptime monitor or a WireGuard endpoint, and it carries no workload that needs disk
- reliability: no reliability event recorded
- notes: The tracker and the vendor disagree on two fields and the vendor is first-party: the vendor says 20 GB NVMe and 2 TB a month, the tracker says 20 GB SSD and 3,072 GB a month. Both figures are recorded here rather than averaged. Unverified: whether the 2 TB is enforced by throttling or by suspension, which the page does not say.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: GBP 1.75/month for UK Xeon S (order product Budget VPS UK 1)
  - renewal_gbp: not published: the order page prices monthly, quarterly, semi-annual and annual terms and prints no renewal price
- evidence:
  - [1] 2026-10-22: plan card: 'UK Xeon S / GBP 1.75 per month / CPU 1 vCPU / RAM 1 GB / NVMe Storage 20 GB / Traffic 2 TB / IPs Included 1 IPv4'
  - [1] 2026-10-22: FAQ: 'Our cheap UK VPS plans start at GBP 1.75/month for UK Xeon S (1 vCPU, 1 GB RAM, 20 GB NVMe) ... All include dedicated UK IPv4, DDoS protection, full root access via VirtFusion and KVM virtualisation.'
  - [2] 2026-10-22: tracker disagrees on two numbers: 'GBP 1.75 / month 1 Intel Cores (shared) 1,024 MB RAM 20 GB SSD 3,072 GB/month bandwidth 1 Gbps port speed IPv4 United Kingdom'
  - [3] 2026-11-07: the order page prints the four billing cycles and their prices for Budget VPS UK 1 | capture: sha256:982f96a9345a6e900c1d94895ecf8576c983c808baf4212015d9bcc8238715f9 | quote: Monthly £1.75 GBP Monthly Quarterly £5.25 GBP Quarterly 6 Months £10.50 GBP Semi-Annually 1 Year £17.50 GBP Annually
  - [3] 2026-11-07: the order form states Monthly Traffic 3TB @ 1Gbps for Budget VPS UK 1 | capture: sha256:982f96a9345a6e900c1d94895ecf8576c983c808baf4212015d9bcc8238715f9 | quote: 3TB @ 1Gbps
  - [3] 2026-11-07: the cart totals GBP 1.75 due today for Budget VPS UK 1 | capture: sha256:982f96a9345a6e900c1d94895ecf8576c983c808baf4212015d9bcc8238715f9 | quote: £1.75 GBP Total Due Today
  - [3] 2026-11-07: no setup fee on the order form | capture: sha256:982f96a9345a6e900c1d94895ecf8576c983c808baf4212015d9bcc8238715f9 | quote: Setup Fees: £0.00 GBP
  - [1] 2026-11-07: the marketing page read 2026-11-07 still prints the four plan prices and specs | capture: sha256:64f7a327795b43fcfc43303031d2a7fb537bf860d5685d24af79dde3c93de762 | quote: Our Budget VPS plans start at £1.75 a month for UK Xeon S (1 vCPU, 1 GB RAM, 20 GB NVMe). UK Xeon M is £3.50 (2 GB), UK Xeon L is £7 (4 GB) and UK Xeon XL is £12 (2 vCPU, 8 GB). Every plan includes a dedicated UK IPv4 address, DDoS protection, full root access and KVM virtualisation.
  - [1] 2026-11-07: the marketing page's plan table still prints 2 TB of traffic for UK Xeon S, against the order form's 3TB | capture: sha256:64f7a327795b43fcfc43303031d2a7fb537bf860d5685d24af79dde3c93de762 | quote: Traffic2 TB
  - [3] 2026-11-07: the entry plan and its cycle prices are unchanged on the order page | capture: sha256:982f96a9345a6e900c1d94895ecf8576c983c808baf4212015d9bcc8238715f9 | quote: Monthly £1.75 GBP Monthly Quarterly £5.25 GBP Quarterly 6 Months £10.50 GBP Semi-Annually 1 Year £17.50 GBP Annually
- sources:
  - [1] https://www.vm6.co.uk/cheap-vps-uk
  - [2] https://vpspricetracker.com/provider/VM6_Networks/vps
  - [3] https://www.vm6.co.uk/manager/store/budget-uk-vps-hosting/budget-vps-uk-1
