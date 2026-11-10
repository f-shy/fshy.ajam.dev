# AvaHost

> ava.hosting | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ava/ | JSON https://fshy.ajam.dev/api/v1/entity/ava.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AvaHost

- `compute/avahost` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T14:17:02.759Z (live) | stale on 2026-12-08
- url https://ava.hosting/
- price parsed USD 5.63/mo
- free tier: VPS One at EUR 5.00 per month, 1-month term: 1 vCPU, 2 GB RAM, 25 GB NVMe, 1 Gbps port, 1 IPv4, KVM, unlimited bandwidth, Chisinau, Moldova. VPS Basic is EUR 10 for 2 vCPUs / 4 GB / 50 GB, VPS Lucky EUR 15 for 2 vCPUs / 6 GB / 70 GB, VPS Power EUR 20 for 4 vCPUs / 8 GB / 90 GB, up to VPS Ultra at EUR 40 for 8 vCPUs / 16 GB / 160 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited: the vendor prints 'Infinity Bandwidth' with no monthly figure and no overage price; the tracker records 51,200 GB/month | metered: no | source: [1]
- identity: email | detail: the signup marks firstname, lastname, street address, city, state and postcode required; email and phone are collected but not marked required; no card
- interface: rest
- limits:
  - per-ip-shaping (binding): the vendor prints 'Infinity Bandwidth' and a 1 Gbps port with no monthly byte figure, so the port and any fair-use shaping are the limit rather than a counter; the tracker records 51,200 GB/month for the same plan, which is well short of the roughly 324 TB a 1 Gbps line moves in 30 days at line rate. [1]
- limits note: the vendor prints 'Infinity Bandwidth' and a 1 Gbps port with no monthly byte figure, so the port and any fair-use shaping are the limit rather than a counter; the tracker records 51,200 GB/month for the same plan, which is well short of the roughly 324 TB a 1 Gbps line moves in 30 days at line rate.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor documents a client area, KVM and a 1 Gbps port, and no API is named on the page
- composes with: 2 GB and 25 GB for EUR 5 with an unlimited-bandwidth claim and a 1 Gbps port is the best transfer-per-euro row among evaluated providers if the claim holds; Moldova sits close enough to western Europe for a crawler egress point and far enough to be a separate failure domain.
- reliability: no reliability event recorded
- notes: Two vendor domains exist and only one was read: the tracker lists ava.hosting while its contact address is on ava-host.com. The provider states it has operated from Chisinau since 2002 and publishes a 99.9 percent uptime SLA on 'core power and network layers'. verification criteria: a measured transfer at 1 Gbps, because 'Infinity Bandwidth' with no published fair-use clause is a claim about a policy that has no written limit.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 25
  - monthly_eur: 5.0
  - annual_eur: 51.0
  - renewal_eur: not published: the billing dropdown's oldprice fields are empty and no renewal price is printed on the page; read at https://ava.hosting/vps/
  - term: 1, 3, 6 and 12 months at 0, 5, 10 and 15 percent off: EUR 5.00 / 14.25 / 27.00 / 51.00 on VPS One
  - in_stock: no stock counter is printed; the page's product schema marks the plans InStock and the cart accepts the order without an account, so the plan is orderable
  - cart_url: https://my.ava.hosting/cart.php?a=add&pid=265&billingcycle=monthly
  - cart_note: the cart (WHMCS, Lagom theme) renders its totals client-side: the static configuration page shows a 0 EUR placeholder and the calctotal endpoint answers without a readable price string, so the cart's own totals were not read; the order page's own billing dropdown (server-rendered data attributes) is the price evidence
  - price_on_page: EUR 5.00/month for VPS One
- evidence:
  - [1] 2026-10-22: plan card quoted: 'VPS One', '5.00 EUR /mo', '1 vCPU', '2 GB RAM', '25 GB NVMe'; tier list 'VPS Basic 10.00 EUR /mo 2 vCPUs 4 GB RAM 50 GB NVMe' through 'VPS Ultra 40.00 EUR /mo 8 vCPUs 16 GB RAM 160 GB NVMe'
  - [1] 2026-10-22: shared plan attributes: '1 Gbps Port Speed', '1 IPv4', 'KVM Virtualization', 'Infinity Bandwidth', 'Any OS', 'DDoS Protection'; and 'VPS plans range from 5.00 EUR/mo to 40.00 EUR/mo. Dedicated servers start at 85.00 EUR/mo'
  - [2] 2026-10-22: tracker's cheapest row: 'AvaHost - 5.00 / month', 'cpu 1 Intel Cores (shared)', 'ram 2,048 MB RAM', 'disk 25 GB NVMe', 'bandwidth 51,200 GB/month bandwidth', 'rj45 1 Gbps port speed', city Moldova
  - [3] 2026-11-07: WHMCS register: six required fields, no card | capture: sha256:978487b9120787e8195dfbce867dc522f0b797d3c318909c4c255e241cc10dd9 | quote: Additional Information (required fields are marked with *)
  - [4] 2026-11-07: the VPS page prices VPS One and prints the term-discount ladder | capture: sha256:0740bec5f234963aa89c2b306216b9b532dc707bb563a24b7be3a6fe69d9a446 | quote: VPS One 5.00€ /mo 1 vCPU 2 GB RAM 25 GB NVMe
  - [4] 2026-11-07: the VPS page prices VPS One at 5.00 EUR monthly | capture: sha256:f6eac2103f0d3882ab5f27936060a3c031e6394bdbc872c8aa0bdf0f69018c88 | quote: VPS One 5.00€ /mo 1 vCPU 2 GB RAM 25 GB NVMe
  - [4] 2026-11-07: the VPS One card's billing dropdown prices the 12-month term at 51.00 | capture: sha256:949fd8850aa5969421bec7f0b475c4c9643064641d5cefc5fd52bab80466e1e0 | quote: data-price="51.00"
  - [4] 2026-11-07: the billing dropdown's oldprice fields are empty: no strike-through or renewal price is printed | capture: sha256:949fd8850aa5969421bec7f0b475c4c9643064641d5cefc5fd52bab80466e1e0 | quote: data-oldprice=""
  - [4] 2026-11-07: the VPS One card's billing dropdown lists the four terms and their discounts | capture: sha256:f6eac2103f0d3882ab5f27936060a3c031e6394bdbc872c8aa0bdf0f69018c88 | quote: 1 month 0% 3 months 5% 6 months 10% 12 months 15%
  - [4] 2026-11-07: the page's structured data marks the plans InStock | capture: sha256:949fd8850aa5969421bec7f0b475c4c9643064641d5cefc5fd52bab80466e1e0 | quote: "availability":"https://schema.org/InStock"
  - [4] 2026-11-07: the VPS One card's monthly order button links the cart with pid 265 | capture: sha256:949fd8850aa5969421bec7f0b475c4c9643064641d5cefc5fd52bab80466e1e0 | quote: href="https://my.ava.hosting/cart.php?a=add&#038;pid=265&#038;billingcycle=monthly"
  - probe:https://my.ava.hosting/cart.php?a=confproduct&i=0 2026-11-07: the cart's static configuration page renders a 0 EUR placeholder before its JS fills the totals | capture: sha256:8c7a4cd9dbe32896eb65f6a30022af270438f48570e950a4b0041cd1d93f89eb | quote: 0 EUR
  - probe:https://my.ava.hosting/cart.php?a=confproduct&i=0 2026-11-07: the warmed cart resolves pid 265 into its configuration page, so the order path works unregistered | capture: sha256:8c7a4cd9dbe32896eb65f6a30022af270438f48570e950a4b0041cd1d93f89eb | quote: "final_url": "https://my.ava.hosting/cart.php?a=confproduct&i=0"
  - [4] 2026-11-07: the VPS page still prices VPS One at EUR 5.00 monthly, 1 vCPU, 2 GB RAM, 25 GB NVMe | capture: sha256:f6eac2103f0d3882ab5f27936060a3c031e6394bdbc872c8aa0bdf0f69018c88 | quote: VPS One 5.00€ /mo 1 vCPU 2 GB RAM 25 GB NVMe
  - [4] 2026-11-07: the VPS page still prices VPS One at EUR 5.00 monthly with the shape the record states | capture: sha256:f6eac2103f0d3882ab5f27936060a3c031e6394bdbc872c8aa0bdf0f69018c88 | quote: VPS One 5.00€ /mo 1 vCPU 2 GB RAM 25 GB NVMe
- sources:
  - [1] https://ava.hosting/
  - [2] https://vpspricetracker.com/provider/AvaHost/vps
  - [3] https://my.ava.hosting/register.php
  - [4] https://ava.hosting/vps/
