# ShockHosting

> shockhosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shockhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/shockhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ShockHosting

- `compute/shockhosting` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:41.345Z (live) | stale on 2026-11-22
- url https://shockhosting.com/vps
- price parsed USD 4.99/mo
- free tier: USD 4.99/month: 1 shared Intel core, 2,048 MB RAM, 30 GB SSD, 2,048 GB/month bandwidth, 1 Gbps port, New York (the same row is priced in Los Angeles and Chicago). The vendor page states 'From just $4.99/month' and documents the 8 GB plan at USD 19.99/month with 4 cores, 120 GB SSD and 8 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2,048 GB per month on the 2 GB row; the vendor page does not state an overage price for it | metered: yes | free allowance: 2,048 GB per month | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 2,048 GB a month on a 1 Gbps port; the port can exhaust it in under a day of saturation [1]
- limits note: 2,048 GB a month on a 1 Gbps port; the port can exhaust it in under a day of saturation
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: SolusVM panel with root, console access and OS templates; Windows Server 2019 as a USD 10/month add-on, extra IPv4 at USD 2/month each
- composes with: a 2 GB US VPS at USD 4.99 with 2 TB is a front end or a small database, not a byte mover; the 8 GB row at USD 19.99 with 8 TB is the one that scales
- reliability: no reliability event observed; the vendor advertises a 7-day money-back window, which is a refund and not a trial
- notes: The configurator lists locations from New York to Singapore with term discounts of 5 to 25 percent. The cart read 2026-11-07 priced the 2 GB plan USD 4.99 monthly and the 8 GB plan USD 19.99 monthly, which confirms the tracker's USD 4.99 row first-party and answers the record's earlier open question about the 2 GB row's cart price.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - monthly_usd: 4.99
  - annual_usd: not published: the page prints a term-discount ladder (5 to 25 percent off at quarterly to 36-month pre-pay) and no annual total
  - renewal_usd: not published: the cart prices the monthly cycle at USD 4.99 and no page names a renewal rate
  - stock: in stock: the cart priced the 2 GB plan USD 4.99 monthly and the 8 GB plan USD 19.99 monthly on 2026-11-07
  - price_on_page: USD 4.99/month (the page's hero: 'From just $4.99/month')
  - term: monthly, quarterly, semiannual, 12, 24 and 36 months at 5-25% off
- evidence:
  - [1] 2026-10-22: 'From just $4.99/month' on the Virtual Servers page, and the one plan the page renders in HTML: 'SSD-KVM-8GB, 4x CPU Cores, 8 GB Memory, 120 GB SSD Storage, 8 TB Bandwidth, $19.99/mo'
  - [2] 2026-10-22: tracker row 'USD 4.99 / month, 1 Intel Cores (shared), 2,048 MB RAM, 30 GB SSD, 2,048 GB/month bandwidth, 1 Gbps port speed, IPv4 + IPv6, New York'
  - [1] 2026-11-07: the cart prices the 2 GB entry plan USD 4.99 monthly with the six term prices 4.99 to 3.74 | capture: sha256:546e026a1d7749d2b97b79fff7012f168876fcd7345c26ce97da1723bd7e87d2 | quote: "$4.99", "$4.74", "$4.49", "$4.24", "$3.99", "$3.74",
  - [1] 2026-11-07: the page's hero states the USD 4.99/month floor on 2026-11-07 | capture: sha256:202e56e4c6744e44e4e525dc8c2b38ba78625d3fde770e0d9148de15141dfcdf | quote: From just <strong>$4.99/month</strong>
- sources:
  - [1] https://shockhosting.com/vps
  - [2] https://vpspricetracker.com/provider/ShockHosting/vps
