# mivoCloud

> mivocloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mivocloud/ | JSON https://fshy.ajam.dev/api/v1/entity/mivocloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mivoCloud

- `compute/mivocloud` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.717Z (live) | stale on 2026-12-08
- url https://mivocloud.com/ssd-kvm-vps
- price parsed USD 5.63/mo
- free tier: S1 at EUR 5.00/month billed monthly, EUR 14.25 quarterly, EUR 27.00 semi-annually and EUR 51.00 annually on the cart: 1 vCPU, 2 GB RAM, 30 GB SSD, 2 TB transfer at 1 Gbps shared, 1 IPv4 plus IPv6, DDoS protection included. S2 is EUR 10.00/month on the cart with 2 vCPU, 4 GB RAM and 3 TB of traffic (its full cart prices are in the evidence rows). Renewal: not published (no page prints a renewal price). Term: monthly, quarterly, semi-annual or annual. In stock: orderable (the vendor page's S1 row links Order Now to the S1 cart, and the cart's configure page renders with no out-of-stock marker; read 2026-11-07). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month included on S1 (the cart's included line reads 'Bandwidth: 1 Gbps - 2 TB' at EUR 0.00); traffic add-on steps on the cart cost EUR 5 per additional TB a month (3 TB +5, 4 TB +10, 5 TB +15, 6 TB +20, 8 TB +25, 10 TB +35) | metered: yes | free allowance: 2 TB a month | price per TB: EUR 5 per additional TB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month on a 1 Gbps shared port. The port is shared rather than guaranteed, so a sustained daytime pull competes with neighbours before the 2 TB counter matters, and the 30 GB disk caps any local working set long before either. [1]
- limits note: 2 TB a month on a 1 Gbps shared port. The port is shared rather than guaranteed, so a sustained daytime pull competes with neighbours before the 2 TB counter matters, and the 30 GB disk caps any local working set long before either.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with autoinstall for Hestia CP, VestaCP and Plesk; the page advertises instant setup by email. No API was read.
- composes with: 2 GB of RAM, 30 GB of SSD and 2 TB of transfer for EUR 5, with a US east coast, a US west coast and a Moldovan location at one price (the S1 cart offers USA (New York), Moldova and USA (Oregon); no Romania). It is the node to put a crawler queue, a small database or a scheduler on; the 30 GB disk rules out any archive role.
- reliability: no reliability event recorded
- notes: The page prints the euro sign; every figure here is spelled EUR to keep the strings ASCII. No free tier was read, so the verdict stays paid-only. Two billing facts on the page are not a free tier and stay here rather than promoted: 'Make an annually order and pay only 10 months', which is two months of service free on an annual term, and a 'FREE TRIAL WINDOWS' note that refers to a 180-day Windows licence trial, not to the server. The vendor's homepage advertises the NVMe line separately, so the EUR 5 plan is the SSD line, not the NVMe line. The traffic add-on's price, formerly unsettled, is now in egress.price_per_tb from the cart.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - price_on_page: EUR 5.00/month for S1
  - renewal_usd: not published: the cart prints the four billing-cycle prices and no renewal price
- evidence:
  - [1] 2026-10-22: S1 row of the vendor's configuration table, quoted cell by cell: 'S1', vCPU '1', RAM '2GB', disk '30GB SSD', transfer '2TB', price 'EUR 5' monthly and 'EUR 4.25 / month' annually; the table header reads 'Package vCPU RAM Disk 1 Gbps Price' and the page states 'All Virtual Servers have DDoS Protection, 1 IPv4 and 1 Gbps Shared Bandwidth'. The page prints the euro sign; it is spelled EUR here for ASCII
  - [1] 2026-10-22: the next row, quoted cell by cell: 'S2', vCPU '2', RAM '4GB', disk '60GB SSD', transfer '3TB', price 'EUR 10' monthly, 'EUR 8.50 / month' annually
  - [1] 2026-10-22: locations, quoted: 'We offer SSD Virtual Servers in USA (New York), MD (Chisinau) and RO (Iasi)'
  - [2] 2026-10-22: tracker row, cells in page order: '1 Intel Cores (shared)', '2,048 MB RAM', '30 GB SSD', '2,048 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'New York U.S.A.', with the price cell reading the euro sign then '5.00 / month'; the identical row repeats at the same price for Moldova and for Oregon
  - [3] 2026-11-07: the S1 cart prices EUR 5.00 monthly, EUR 14.25 quarterly, EUR 27.00 semi-annually, EUR 51.00 annually | capture: sha256:041f1ff00093cff5008ee0cab12b22ec197e96ce24f5e14af2fcffce7027c241 | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually
  - [1] 2026-11-07: the vendor page states the annual term is billed as 10 months | capture: sha256:6abe2f5b967b2476ce3f2f589902d1e64d07e0105987031f5725be6937732bfd | quote: Make an annually order and pay only 10 months. That means you get 2 months of service for free
  - [3] 2026-11-07: traffic add-on steps on the S1 cart cost EUR 5 per additional TB a month | capture: sha256:041f1ff00093cff5008ee0cab12b22ec197e96ce24f5e14af2fcffce7027c241 | quote: Bandwidth 1 Gbps - 2 TB 1 Gbps - 3 TB €5.00EUR 1 Gbps - 4 TB €10.00EUR 1 Gbps - 5 TB €15.00EUR 1 Gbps - 6 TB €20.00EUR 1 Gbps - 8 TB €25.00EUR 1 Gbps - 10 TB €35.00EUR
  - [3] 2026-11-07: the S1 cart offers the locations USA (New York), Moldova and USA (Oregon); no Romania | capture: sha256:041f1ff00093cff5008ee0cab12b22ec197e96ce24f5e14af2fcffce7027c241 | quote: Location USA (New York) Moldova USA (Oregon)
  - [4] 2026-11-07: the S2 cart prices EUR 10.00 monthly, EUR 28.50 quarterly, EUR 54.00 semi-annually, EUR 102.00 annually (EUR 8.50 per month derived) | capture: sha256:5f0a823a4359e06a96e5654f58afb11fe892ab30a80c120d037752c357575be2 | quote: Choose Billing Cycle €10.00EUR Monthly €28.50EUR Quarterly €54.00EUR Semi-Annually
  - [3] 2026-11-07: the S1 cart renders its configure page with all four cycle prices and no out-of-stock marker, so the plan is orderable | capture: sha256:078754d98a09bf8f9a17c0779802d8aefb86c6f641786e85a5f493f640afe9fb | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually €51.00EUR Annually
  - [3] 2026-11-07: the S1 cart prices the four billing cycles at EUR 5.00, 14.25, 27.00 and 51.00 with no out-of-stock marker | capture: sha256:078754d98a09bf8f9a17c0779802d8aefb86c6f641786e85a5f493f640afe9fb | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually €51.00EUR Annually
  - [3] 2026-11-07: the S1 cart prices EUR 5.00 on the monthly term | capture: sha256:078754d98a09bf8f9a17c0779802d8aefb86c6f641786e85a5f493f640afe9fb | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually €51.00EUR Annually
  - [3] 2026-11-07: the cart's printed prices are the four billing-cycle prices; no renewal price appears among them | capture: sha256:078754d98a09bf8f9a17c0779802d8aefb86c6f641786e85a5f493f640afe9fb | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually €51.00EUR Annually
  - [3] 2026-11-07: the S1 cart prices EUR 5.00 monthly across the four cycles with no out-of-stock marker | capture: sha256:078754d98a09bf8f9a17c0779802d8aefb86c6f641786e85a5f493f640afe9fb | quote: Choose Billing Cycle €5.00EUR Monthly €14.25EUR Quarterly €27.00EUR Semi-Annually €51.00EUR Annually
- sources:
  - [1] https://mivocloud.com/ssd-kvm-vps
  - [2] https://vpspricetracker.com/provider/mivoCloud/vps
  - [3] https://clients.mivocloud.com/cart.php?a=add&pid=466
  - [4] https://clients.mivocloud.com/cart.php?a=add&pid=467
