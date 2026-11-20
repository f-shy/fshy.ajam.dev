# NolimitHost

> nolimithost.cc | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nolimithost/ | JSON https://fshy.ajam.dev/api/v1/entity/nolimithost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NolimitHost

- `compute/nolimithost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.718Z (live) | stale on 2026-11-22
- url https://nolimithost.cc/cloud/vps-hosting.php
- price parsed USD 1.21/mo
- free tier: The tracker's cheapest NolimitHost row is an IPv6-only Budget VPS at EUR 12.99/year (EUR 1.08/month derived): 1 vCPU, 1 GB RAM, 10 GB NVMe, IPv6-only, Frankfurt. The vendor's own billing API confirms it as BVPS-IPV6ONLY-Offers at EUR 12.99 with annual the only base billing period enabled (biennial -3 percent, triennial -5 percent), stock 9, active, and the plan's cart page prints EUR 12.99 Annual, EUR 25.20 Biennial at -3 percent and EUR 37.02 Triennial at -5 percent, with 2 TB of bandwidth, a 500 Mbit/s uplink and no stock badge. Budget VPS 1 (2 vCPU, 4 GB RAM, 40 GB NVMe) is EUR 10.99 per quarter on the billing API and its cart page (monthly not offered; semi-annual -3, annual -5, biennial -8, triennial -10 percent; the cart prints EUR 21.32 semi-annual, EUR 41.76 annual, EUR 80.89 biennial and EUR 118.69 triennial), stock 4, EUR 3.66/month derived; the Budget table no longer appears on the vendor VPS page, which now lists only the Premium plans. Premium VPS 1 (1 vCPU, 2 GB, 20 GB NVMe) is EUR 5.99/month on the billing API; its cart page prints EUR 17.07 quarterly at -5 percent, EUR 33.06 semi-annual at -8 percent, EUR 64.69 annual at -10 percent, EUR 126.51 biennial at -12 percent and EUR 183.29 triennial at -15 percent, with stock 7 and no stock badge on the cart. Renewal: not published. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: allowance is stated per row: 2048 GB/month on the tracker's IPv6-only budget row, 5 TB on Budget VPS 1, and 5 to 8 TB across the Premium rows, all on 1 Gbit/s or 0.5 Gbps ports; no overage price was published on the page read | metered: yes | free allowance: 2048 GB/month on the recorded row; 5 TB on Budget VPS 1 | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2048 GB a month on the IPv6-only budget row recorded here. The vendor's Budget VPS 1 row carries 5 TB and the Premium rows carry 5 to 8 TB. The IPv6-only plan has no IPv4 address at all, which is a harder limit than the byte count if the workload needs a v4 endpoint. [1]
- limits note: 2048 GB a month on the IPv6-only budget row recorded here. The vendor's Budget VPS 1 row carries 5 TB and the Premium rows carry 5 to 8 TB. The IPv6-only plan has no IPv4 address at all, which is a harder limit than the byte count if the workload needs a v4 endpoint.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: full root, instant deployment, KVM; control panel at panel.nolimitcloud.eu and a documentation site; no API was stated on the page read
- composes with: EUR 3.66/month for 2 vCPU, 4 GB and 40 GB of NVMe with 5 TB at 1 Gbit/s in Frankfurt provides high cores-per-euro capacity for a crawler worker. The 5 TB allowance is the monthly cap.
- reliability: no reliability event observed; no uptime figure was stated on the page read
- notes: or docs/ (searched both trees for nolimithost, no hit). The tracker's cheapest row is filed under the offer slug BVPS_IPV6ONLY_Offers; the vendor's own billing API now lists that product (BVPS-IPV6ONLY-Offers) at EUR 12.99, active, stock 9, annual the only base period, so the EUR 12.99/year figure is vendor-confirmed. The tracker's Go link for the offer resolves to nolimit.host, a game-server brand, not to nolimithost.cc; the tracker company profile names NolimitCloud s.r.o. at nolimithost.cc, and whether nolimit.host and nolimithost.cc are the same business remains unverified.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - price_on_page: EUR 12.99/year for BVPS-IPV6ONLY-Offers
  - monthly_usd: 1.21
  - renewal_usd: not published: the cart prints the annual price and no renewal price
- evidence:
  - [2] 2026-10-22: cheapest row: 'EUR 1.08 / month', 'yearly Service', '1 Intel Cores (shared)', '1,024 MB RAM', '10 GB NVMe', '2,048 GB/month bandwidth', '0.5 Gbps port speed', 'Frankfurt Germany'; header 'starting at EUR 12.99 per year'
  - [1] 2026-10-22: Budget VPS table row quoted: 'Budget VPS 1', '2 vCPUs', '4 GB', '40 GB NVMe', '5 TB', '1 Gbit/s', '3.66 EUR /mo (prepaid quarterly)', 'Frankfurt, Germany'
  - [1] 2026-10-22: Premium VPS table row quoted: 'Premium VPS 1', '1 vCPU', '2 GB', '20 GB NVMe', '5 TB', '1 Gbit/s', '5.99 EUR /mo'; the range runs to Premium VPS 7 at EUR 79.99 with 8 vCPU, 32 GB and 320 GB
  - [3] 2026-11-07: the vendor billing API's product list carries BVPS-IPV6ONLY-Offers at price 12.99, stock 9, active, a 1 GB / 1 vCore / 10 GB NVMe IPv6-only VPS, with annual the only base period enabled (biennial -3, triennial -5 percent) | capture: sha256:6cdab34f894baa44dbba8bc54c8cd27bfae8e1b208e3b8658bb5fdc9c6f67f7c | quote: "name":"BVPS-IPV6ONLY-Offers","description":"Budget VPS - 1GB Ram \/ 1 vCore (500) \/ 10GB NVME \/ IPv6 Only\nEfficient CPU","price":12.99,"stock":9,"is_active":true
  - [3] 2026-11-07: the vendor billing API lists Budget VPS 1 at EUR 10.99 with stock 4 and quarterly as the base period | capture: sha256:a878dd6b035da4e90da67a30bd91063c7606ee7a435655231e2c49d06adfe93f | quote: "name":"Budget VPS 1","description":"Budget VPS - 4GB Ram \/ 2 vCore \/ 40GB NVME\nEfficient CPU","price":10.99,"stock":4,"is_active":true
  - [4] 2026-11-07: the vendor cart prices the IPv6-only offer at EUR 12.99 on the annual term with no stock badge | capture: sha256:27799b14a6f56fc13e013c9df64590689a58e3b05c4abdf6e353d7dcecc76f8e | quote: €12.99 Annual
  - [5] 2026-11-07: the Premium VPS 1 cart prints EUR 5.99 monthly, EUR 17.07 quarterly, EUR 33.06 semi-annual, EUR 64.69 annual, EUR 126.51 biennial and EUR 183.29 triennial, with no stock badge | capture: sha256:b7194621ef6baa74428e7f7b45d7e1f507b7c592eee24fc370418abf3294b59b | quote: -10%€64.69Annual
  - [6] 2026-11-07: the Budget VPS 1 cart prints EUR 10.99 as its base quarterly price and EUR 21.32, EUR 41.76, EUR 80.89 and EUR 118.69 for semi-annual, annual, biennial and triennial, with no monthly term and no stock badge | capture: sha256:82d7981fe02fe360e843b68399b7c0159cfd7db7509601228560e18a684143e0 | quote: €10.99Quarterly
  - [1] 2026-11-07: the vendor VPS page lists only the Premium plans and prices Premium VPS 1 at 5.99 EUR per month | capture: sha256:84a570835b024ec4fbc0ecc7de086fe7bac27e30c98abefcbc4a6c8438d5f14b | quote: Premium VPS 1 1 vCPU 2 GB 20 GB NVMe 5 TB 1 Gbit/s 5.99 € /mo
  - [4] 2026-11-07: the vendor cart prices the IPv6-only offer at EUR 12.99 on the annual term | capture: sha256:27799b14a6f56fc13e013c9df64590689a58e3b05c4abdf6e353d7dcecc76f8e | quote: €12.99 Annual
  - [4] 2026-11-07: the annual term is the only base billing period and its price is EUR 12.99 | capture: sha256:27799b14a6f56fc13e013c9df64590689a58e3b05c4abdf6e353d7dcecc76f8e | quote: €12.99 Annual
  - [4] 2026-11-07: the cart prints the annual term price; no renewal price appears | capture: sha256:27799b14a6f56fc13e013c9df64590689a58e3b05c4abdf6e353d7dcecc76f8e | quote: €12.99 Annual
  - [3] 2026-11-07: the vendor billing API lists BVPS-IPV6ONLY-Offers at EUR 12.99, active, with the 1 GB / 1 vCore / 10 GB NVMe IPv6-only shape | capture: sha256:6cdab34f894baa44dbba8bc54c8cd27bfae8e1b208e3b8658bb5fdc9c6f67f7c | quote: "name":"BVPS-IPV6ONLY-Offers","description":"Budget VPS - 1GB Ram \/ 1 vCore (500) \/ 10GB NVME \/ IPv6 Only\nEfficient CPU","price":12.99,"stock":9,"is_active":true
- sources:
  - [1] https://nolimithost.cc/cloud/vps-hosting.php
  - [2] https://vpspricetracker.com/provider/NolimitHost/vps
  - [3] https://panel.nolimitcloud.eu/billing/api/products_api.php?action=list
  - [4] https://panel.nolimitcloud.eu/billing/ordering?add=85
  - [5] https://panel.nolimitcloud.eu/billing/ordering?add=1
  - [6] https://panel.nolimitcloud.eu/billing/ordering?add=49
