# LeapSwitch

> leapswitch.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leapswitch/ | JSON https://fshy.ajam.dev/api/v1/entity/leapswitch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LeapSwitch

- `compute/leapswitch` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:38.153Z (live) | stale on 2026-12-08
- url https://leapswitch.com/mumbai-india/unmanaged-vps-hosting/linux.php
- free tier: USD 9.00/month (G2-LU-4G): 2 Epyc vCPUs, 4,096 MB RAM, 60 GB NVMe, 1,024 GB/month bandwidth, 1 Gbps port, IPv4 and IPv6, Mumbai India. The vendor page quotes: 'G2-LU-4G', '$9', '4 GB RAM', '2 vCPUs', '60 GB NVMe Space', '1 TB Bandwidth'. The same USD 9.00 plan is offered in Lisbon and Barcelona, and the range climbs to G2-LU-64G at USD 149 for 16 vCPU, 64 GB and 10 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the cart (manage.leapswitch.com, USD store) prices G2-LU-4G at USD 9.00 monthly, USD 25.00 quarterly, USD 48.00 semi-annually, USD 93.00 annually, USD 168.00 biennially and USD 235.00 triennially, with USD 0.00 setup and USD 9.00 total due today on the monthly term; no renewal price is printed and the cart shows no stock marker
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month included per the vendor plan list (free_allowance is in GB a month); the overage price is not stated on the page read | metered: yes | free allowance: 1024 | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 1 TB a month on a 1 Gbps port; the vendor's next size, G2-LU-8G, doubles RAM, disk and bandwidth for USD 19, so the 1 TB cap is the first wall for anything serving pages [1]
- limits note: 1 TB a month on a 1 Gbps port; the vendor's next size, G2-LU-8G, doubles RAM, disk and bandwidth for USD 19, so the 1 TB cap is the first wall for anything serving pages
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: per-location product pages with cart links into manage.leapswitch.com; managed and unmanaged variants, Linux and Windows, with separate per-location pages for each of about 12 sites
- composes with: USD 9 for 2 vCPU and 60 GB NVMe at one price in Mumbai, Lisbon and Barcelona is the only three-continent offer among evaluated providers, which makes it a plausible crawler control plane close to EU and Indian targets; 1 TB a month keeps it out of the serving path.
- reliability: no reliability event observed; the vendor claims 99.9% uptime and 19 locations, which were not checked.
- notes: Leapswitch provides VPS and dedicated hosting across multiple international locations.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 60
- evidence:
  - [1] 2026-10-22: plan quoted: 'G2-LU-4G', '$9', 'CONFIGURE NOW', '4 GB RAM', '2 vCPUs', '60 GB NVMe Space', '1 TB Bandwidth'; the page is titled 'Self-Managed Cloud Linux Cloud Server | Mumbai, India'
  - [1] 2026-10-22: the ladder above that plan, priced 19, 37, 75 and 149 in the same currency: G2-LU-8G (8 GB, 3 vCPU, 100 GB, 2 TB), G2-LU-16G, G2-LU-32G, G2-LU-64G (16 vCPU, 64 GB, 800 GB, 10 TB); each links to a cart id at manage.leapswitch.com
  - [2] 2026-10-22: three cards quoted at '$9.00 / month' for Mumbai, Lisbon and Barcelona, each '2 Epyc Cores (shared)', '4,096 MB RAM', '60 GB NVMe', '1,024 GB/month bandwidth', '1 Gbps port speed', matching the vendor page
  - [3] 2026-11-07: the cart prices G2-LU-4G across six billing cycles | capture: sha256:c866ddf117b4cb3474b247e781ebd97a825325ac783edfab51dece3dda4bcbc2 | quote: $9.00 </span><span class="product-price cycle-q">$25.00 </span><span class="product-price cycle-s">$48.00 </span><span class="product-price cycle-a">$93.00 </span><span class="product-price cycle-b">$168.00 </span><span class="product-price cycle-t">$235.00
  - [3] 2026-11-07: the cart lists G2-LU-4G at USD 9.00 with 2 allocated CPUs, 4 GB RAM, 60 GB NVMe and 1 TB bandwidth | capture: sha256:c866ddf117b4cb3474b247e781ebd97a825325ac783edfab51dece3dda4bcbc2 | quote: G2-LU-4G ... Allocated CPUs ... 4 GB ... 60 GB ... 1 TB
  - [3] 2026-11-07: the cart prices G2-LU-4G at USD 9.00 monthly, 25.00 quarterly, 48.00 semi-annually, 93.00 annually, 168.00 biennially and 235.00 triennially, with no renewal price printed and no out-of-stock marker | capture: sha256:3690212579ef7864ab4e6b98731aa7dc3cf8d30a1700e48d0dc7ae29f16796e8 | quote: <span class="product-price cycle-m">$9.00 </span><span class="product-price cycle-q">$25.00 </span><span class="product-price cycle-s">$48.00 </span><span class="product-price cycle-a">$93.00 </span><span class="product-price cycle-b">$168.00 </span><span class="product-price cycle-t">$235.00 </span>
- sources:
  - [1] https://leapswitch.com/mumbai-india/unmanaged-vps-hosting/linux.php
  - [2] https://vpspricetracker.com/provider/LeapSwitch/vps
  - [3] https://manage.leapswitch.com/cart/self-managed-nvme-cloud-vm-usd?id=6078
