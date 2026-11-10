# Ultahost

> ultahost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ultahost/ | JSON https://fshy.ajam.dev/api/v1/entity/ultahost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ultahost

- `compute/ultahost` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ultahost.com/vps-hosting
- free tier: VPS Basic at USD 5.52/month on a 24-month term, list USD 9.19 with 'Save 40%': 1 CPU core, 1 GB DDR5, 30 GB NVMe, 1 dedicated IPv4 plus 4 IPv6, managed server; the tracker lists the same plan in Frankfurt, London and Stockholm, while the vendor card names no location. The page header states 'Starting at USD 5.51/mo*'. The tracker's row is USD 6.89/month for the same 1 GB and 30 GB shape. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: sold as unmetered: the comparison table lists 'Unmetered' monthly bandwidth for this price row and the page title says 'Unlimited Bandwidth VPS Server'; no overage price exists because no allowance is sold | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: the vendor sells the plan as unmetered: the page title reads 'Unlimited Bandwidth VPS Server' and its own comparison table lists the USD 5.50 row's monthly bandwidth as 'Unmetered'. No byte allowance is published, so the first limit is the 30 GB disk. The tracker's 51,200 GB a month is third-party and not on the page read
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the plan is sold as managed with Hestia, CyberPanel, Plesk or cPanel offered as panel choices; no API is documented on the page read
- composes with: unmetered transfer and a managed panel at USD 5.52 on a two-year prepay is the only plan among documented hosts sold explicitly as managed, so it fits a service that is handed off rather than administered, at the cost of two years of prepayment
- reliability: no reliability event recorded
- notes: Three price figures for one plan on one page (USD 9.19 list, USD 5.52 on a 24-month term, USD 5.51 in the hero) and a tracker figure of USD 6.89 that matches none of them, so the tracker is likely quoting a 12-month rate the page does not currently show; the record takes the 24-month card and states the term because the price is only available on it. The 30-day money-back guarantee is a refund term, not a trial. Unverified: the month-to-month price, which the page's billing tabs hide from a text read. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 30
- evidence:
  - [2] 2026-10-22: cheapest row repeated for three locations: 'Ultahost - USD 6.89 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '30 GB NVMe', '51,200 GB/month bandwidth', '1 Gbps port speed', 'Frankfurt Germany', 'London United Kingdom', 'Stockholm Sweden'
  - [1] 2026-10-22: plan card, quoted: 'VPS Basic', 'USD 9.19', 'Save 40%', 'USD 5.52 /mo', 'Billed for 24 month term', 'Renews at USD 5.52/mo for 2 years', '1 CPU Core', '1 GB RAM DDR5', '30 GB NVMe SSD', 'Managed Server', '1 IPv4 Dedicated IP', '4 IPv6 Dedicated IP'
  - [1] 2026-10-22: 'HOSTING SALE: GET 40% OFF VPS HOSTING' and 'Starting at USD 5.51 /mo*' in the hero, a one-cent disagreement with the card's USD 5.52
  - [1] 2026-10-22: comparison table row at 'USD 5.50/mo' with '30GB NVMe', '1 GB', 'Monthly Bandwidth: Unmetered'; the VPS Business card at 'USD 9.78/mo' states 'Unlimited Bandwidth' explicitly
- sources:
  - [1] https://ultahost.com/vps-hosting
  - [2] https://vpspricetracker.com/provider/Ultahost/vps
