# BulkVM

> bulkvm.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bulkvm/ | JSON https://fshy.ajam.dev/api/v1/entity/bulkvm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BulkVM

- `compute/bulkvm` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T08:51:29.950Z (live) | stale on 2026-12-08
- url https://bulkvm.com/
- price parsed USD 5/mo
- free tier: Starter at USD 5/month: 1 vCore Intel, 1 GB ECC memory, 10 GB SSD boot plus 2 TB of ZFS RAIDZ2 HDD storage, 10 TB transfer with unmetered inbound, 1 Gbit port with paid upgrades to 2.5 / 5 / 10 Gbit at USD 5 / 10 / 15 per month, KVM with root access, 1 IPv4 plus a /64 IPv6, Phoenix AZ. The page states 'Transfer is included in every plan' and the FAQ states 'No egress fees'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: flat transfer allowance included in the plan price billed monthly, inbound unmetered, no egress fee and no overage price published on the page read | metered: yes | free allowance: 10 TB/month on Starter (15 TB on Standard, 25 TB on Pro) | source: [1]
- identity: email | detail: not stated
- interface: rest, s3-compatible
- limits:
  - volume-quota (binding): 10 TB of transfer on Starter with inbound unmetered at 1 Gbit; the vendor prints the allowance without a period and the tracker states it per month, so the wall is the byte count rather than the port [1]
- limits note: 10 TB of transfer on Starter with inbound unmetered at 1 Gbit; the vendor prints the allowance without a period and the tracker states it per month, so the wall is the byte count rather than the port
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: KVM with root access and full provisioning at checkout; the page names no API, S3 endpoint or client, so the 2 TB is block storage inside the VM rather than object storage
- composes with: 2 TB of ZFS HDD for USD 5/month with 10 TB of transfer is the cheapest cold tier in this slice: it can hold a large share of the 20 TB dataset in one VM, but the 1 GB of RAM means a rebuild or scrub of that pool is slow and the 10 TB allowance caps a hot-served mirror.
- reliability: the page states there is no formal SLA: 'No formal SLA. We keep things running and respond to issues quickly, but this is unmanaged hosting at a low price point'
- notes: The vendor page and the tracker agree on price, RAM and transfer; the tracker files the 2 TB of HDD as '2,000 GB HDD' disk, which is the same pool the vendor calls ZFS RAIDZ2 storage, so the shape records the bulk pool and the 10 GB SSD boot drive is named only in the offer text.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 2000
  - monthly_usd: 5.0
  - annual_usd: not published: the store page prints one monthly rate and no annual total
  - renewal_usd: not published: the store page prints one monthly rate with no renewal sentence
  - billing_term: monthly
  - in_stock: yes
- evidence:
  - [1] 2026-10-22: plan card quoted: 'Starter', '$5 /mo', '1 GB ECC Memory', '1 vCore Intel CPU', '10 GB SSD Boot', '2 TB ZFS HDD Storage', '10 TB Transfer + Unmetered Inbound', '1 Gbit port included', 'KVM + Root Access', '1 IPv4 + /64 IPv6'
  - [1] 2026-10-22: FAQ quoted: 'Are there egress fees? No. Each plan includes a flat transfer allowance - 10TB on Starter, 15TB on Standard, 25TB on Pro. Inbound is always unmetered.' and 'Port upgrades are $5/mo for 2.5 Gbit, $10/mo for 5 Gbit, and $15/mo for 10 Gbit'
  - [2] 2026-10-22: tracker row quoted: 'BulkVM - $5.00 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '2,000 GB HDD', '10,000 GB/month bandwidth', '1 Gbps port speed', 'U.S.A.'; info page marks the offer 'In stock now'
  - [3] 2026-11-07: the WHMCS store prices Starter at USD 5.00 monthly | capture: sha256:3d8d337af03bb07500e72f460c99750f280bab9d81c76dca3f6d240f6121032c | quote: <span class="price">$5.00 USD</span>
  - [3] 2026-11-07: the vendor's own store prices Starter at USD 5.00 monthly with the same 2 TB HDD, 10 TB transfer shape | capture: sha256:3d8d337af03bb07500e72f460c99750f280bab9d81c76dca3f6d240f6121032c | quote: <span class="price">$5.00 USD</span>
  - [1] 2026-11-07: the Starter card on the vendor landing page states 1 GB ECC memory, 1 vCore Intel CPU, 10 GB SSD boot, 2 TB ZFS HDD storage, 10 TB transfer at USD 5/mo, KVM + root, 1 IPv4 + /64 IPv6 | capture: sha256:4d84b2b48f3f5a55408a12814b2a6138f12d37b055ca65940c1e484a10ade37a | quote: <div class="pricing-feature"><strong>1 GB</strong> ECC Memory</div> <div class="pricing-feature"><strong>1 vCore</strong> Intel® CPU</div> <div class="pricing-feature"><strong>10 GB</strong> SSD Boot</div>
  - [1] 2026-11-07: each plan includes a flat transfer allowance with unmetered inbound and no egress fee | capture: sha256:4d84b2b48f3f5a55408a12814b2a6138f12d37b055ca65940c1e484a10ade37a | quote: No. Each plan includes a flat transfer allowance — 10TB on Starter, 15TB on Standard, 25TB on Pro. Inbound is always unmetered. No surprise bills at the end of the month.
- sources:
  - [1] https://bulkvm.com/
  - [2] https://vpspricetracker.com/provider/BulkVM/vps
  - [3] https://my.bulkvm.com/store/vps/starter
