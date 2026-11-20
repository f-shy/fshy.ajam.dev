# Aluy

> aluy.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aluy/ | JSON https://fshy.ajam.dev/api/v1/entity/aluy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aluy

- `compute/aluy` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T14:17:02.759Z (live) | stale on 2026-12-08
- url https://aluy.net/pricing
- price parsed USD 3.94/mo
- free tier: Custom VPS at the configurator's minimum: EUR 3.50 per month for 1 core (1.00), 1 GB RAM (1.50) and 10 GB SSD (1.00), in Hong Kong, on a 10 Gbps shared port, with 1 IPv4 and a /64 IPv6, full root, KVM. The page prices components rather than plans: 1.00 per core, 1.50 per GB of RAM, 1.00 per 10 GB of SSD, and each extra IPv4 adds 1.00 per month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: fair use: no monthly byte figure printed by the vendor, and a shared 10 Gbps port; the tracker states 20,000 GB/month | metered: yes | free allowance: 20,000 GB/month per the tracker; unquantified fair use per the vendor | source: [1]
- identity: email | detail: the signup page offers a Personal and a Business account ('Personal: No company details needed. Business: VAT ID and reverse charge supported'); the form fields are client-rendered
- interface: rest
- limits:
  - volume-quota (binding): the tracker records 20,000 GB a month for this configuration; the vendor prints no figure and instead applies a Fair Use Policy under which 'sustained, disproportionate traffic may have its network speed temporarily reduced'. The port is 10 Gbps shared, so shaping, not a byte count, is what a heavy month meets. [1]
- limits note: the tracker records 20,000 GB a month for this configuration; the vendor prints no figure and instead applies a Fair Use Policy under which 'sustained, disproportionate traffic may have its network speed temporarily reduced'. The port is 10 Gbps shared, so shaping, not a byte count, is what a heavy month meets.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor documents a reseller REST API v1 (Bearer key; scopes for orders, services, billing, tickets, ssh-keys, webhooks) at aluy.net/api-docs; the panel and configurator are web; no client tool is documented
- composes with: the only host among evaluated providers whose shape is priced per component, so a 1 core / 1 GB box can be raised to 4 GB or 40 GB without changing plan; 20 TB of allowance on a shared 10 Gbps port makes it a candidate for the crawler's fetch tier rather than its storage.
- reliability: no reliability event recorded
- notes: Two disagreements worth keeping: the vendor computes EUR 3.50 for 1 core / 1 GB / 10 GB in Hong Kong while the tracker lists EUR 4.27 for the same configuration, and three of four locations are marked out of stock, so the price is orderable from Hong Kong only. The vendor also states that outgoing mail ports 25, 465 and 587 are blocked by default, which matters for any mail work. The page returned upstream 403 and was extracted by automated retrieval's provider fallback, not by a direct fetch. verification criteria: whether 4.27 reflects an extra IPv4 or an older price, which the configurator arithmetic does not explain.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - monthly_eur: 3.5
  - annual_eur: not published: the configurator prices a monthly total only and the page prints no annual term; read at https://aluy.net/pricing
  - renewal_eur: not published: no renewal price is printed on the pricing page and the order page is a sign-in gate; read at https://aluy.net/pricing
  - term: monthly; the configurator prints a monthly total only
  - stock: Hong Kong in stock; the location selector marks Bulgaria and Finland 'out of stock'; Netherlands carries no stock mark
  - cart_url: https://aluy.net/pricing/order?type=vm-custom&ram=1&cpu=1&ssd=10&location=hk
  - cart_note: the order page is a sign-in gate ('You need an account to place orders and manage services', Wayback capture of 2026-07-26 replayed today), so the cart's own price and stock are unverified: behind a sign-up
  - price_on_page: EUR 3.50/month for the custom VM floor (1 core, 1 GB RAM, 10 GB SSD, Hong Kong)
- evidence:
  - [1] 2026-10-22: configurator quoted: 'RAM (1 GB x 1.50 EUR) 1.50 EUR', 'CPU (1 core x 1.00) 1.00 EUR', 'SSD (10 GB x 1.00/10 GB) 1.00 EUR', 'Monthly total 3.50 EUR', 'Order - 3.50/mo'
  - [1] 2026-10-22: location selector: 'Hong Kong', 'Bulgaria - out of stock', 'Finland - out of stock', 'Netherlands - out of stock'; and 'All VMs include: 10 Gbps shared port, 1x IPv4, /64 IPv6, full root access, KVM virtualisation'
  - [1] 2026-10-22: limits quoted: 'The 10 Gbps port is shared with other customers, so full 10 Gbps throughput cannot be guaranteed at all times' and 'Fair-use traffic under our Fair Use Policy - normal hosting use is never affected, but sustained, disproportionate traffic may have its network speed temporarily reduced'
  - [2] 2026-10-22: tracker's cheapest row: 'Aluy - 4.27 / month', 'cpu 1 Ryzen Cores (shared)', 'ram 1,024 MB RAM', 'disk 10 GB SSD', 'bandwidth 20,000 GB/month bandwidth', 'rj45 10 Gbps port speed', city Hong Kong
  - [3] 2026-11-07: Aluy documents a reseller REST API v1 | capture: sha256:8b730559fc27cfa04e9bece12e6af2f3f241034a32eca46bca9a7b9f6f128b14 | quote: Use a reseller API key with the minimum scopes your integration needs; every example below sends one as `$KEY`.
  - [4] 2026-11-07: the signup page asks for an account; Personal needs no company details, Business a VAT ID | capture: sha256:684135808c9f3be6589db4627d69e5b8cb15b38a350eae3b58d326760d502d9a | quote: Personal No company details needed. Business VAT ID and reverse charge supported.
  - [1] 2026-11-07: the configurator's minimum (1 core, 1 GB RAM, 10 GB SSD, Hong Kong) is EUR 3.50 monthly; Hong Kong in stock, Bulgaria and Finland out of stock | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
  - [1] 2026-11-07: the configurator's minimum (1 core, 1 GB RAM, 10 GB SSD, Hong Kong) totals EUR 3.50 a month | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
  - [1] 2026-11-07: the only total the configurator prints is the monthly one | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
  - [1] 2026-11-07: the order link prices the service at EUR 3.50 per month and names no renewal figure | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Order — €3.50/mo
  - [1] 2026-11-07: the configurator's only total is the monthly one | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
  - [1] 2026-11-07: the location selector's stock marks: Bulgaria and Finland out of stock | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Hong KongNetherlandsBulgaria — out of stockFinland — out of stock
  - [1] 2026-11-07: the pricing page's order button links the custom-VM order page with the configurator's parameters | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Order — €3.50/mo
  - [5] 2026-11-07: the order page for the custom VM is a sign-in gate (capture of the 2026-07-26 Wayback copy) | capture: sha256:6e4b43240315a38888a31da6f09b760e983ac409744e9bf8f575b1e74f30af20 | quote: You need an account to place orders and manage services.
  - probe:https://aluy.net/pricing/order?type=vm-custom&ram=1&cpu=1&ssd=10&location=hk 2026-11-07: the order URL answers HTTP 403 today | capture: sha256:e5de7e325b03770cad9a897c1b6cd545dd034d3d400161a3aaf5eada7c5b2dbd | quote: "status": 403
  - [1] 2026-11-07: the configurator's minimum is unchanged: EUR 3.50 a month for 1 core, 1 GB RAM and 10 GB SSD in Hong Kong | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
  - [1] 2026-11-07: the configurator's floor (1 core, 1 GB RAM, 10 GB SSD, Hong Kong) totals EUR 3.50 a month | capture: sha256:4381fb8a9d0958dfb9b793718f96cc1efc3add093ff40cbbdc76a0312d0e1fed | quote: Monthly total€3.50
- sources:
  - [1] https://aluy.net/pricing
  - [2] https://vpspricetracker.com/provider/Aluy/vps
  - [3] https://aluy.net/api-docs
  - [4] https://aluy.net/register
  - [5] https://web.archive.org/web/20260726003556/https://aluy.net/pricing/order%3Ftype=vm-custom&ram=1&cpu=1&ssd=10&location=hk?provider=wayback
