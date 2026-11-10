# iFog GmbH

> ifog.ch | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ifog/ | JSON https://fshy.ajam.dev/api/v1/entity/ifog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iFog GmbH

- `compute/ifog-bgp-basic-512-ipv6` | qualifies | evidence documented | binding volume-quota | category IPv6-only VPS | tier VPS Basic 512MB - IPv6 only AMS
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://my.ifog.ch/order/main/index/BGP-Basic
- free tier: No free tier. The 512 MB IPv6-only plan is CHF 12.99 a year (or CHF 5.00 for 3 months): 1 shared Xeon core, 512 MB RAM, 10 GB SSD, 500 GB traffic, IPv6 only with no IPv4. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: billed 3-monthly or 12-monthly; the disk persists while the service is paid. No deletion grace period is printed. | source: [1]
- egress: 500 GB traffic on the 512 MB rung, per the plan card | metered: yes | free allowance: 500 GB | source: [1]
- identity: email | detail: a client account on my.ifog.ch; the checkout form and payment rails were not read on any page reached. No card hold is stated.
- interface: ssh
- limits:
  - volume-quota (binding): 500 GB on the 512 MB rung; the ladder rises to 4 TB on the 4 GB rung [1]
- binding note: 500 GB a month is the tightest traffic allowance among buyable offerings, and it is the first thing a VPN node or a monitoring fleet exhausts.
- interface detail: KVM-style virtual server with an IPv6 address only; an optional BGP session is offered on the plan. No IPv4 address is included on any IPv6-only rung.
- tooling: any SSH client over IPv6; a BGP session is available as an option
- composes with: a Swiss-hosted IPv6 node with three locations on one order page, cheap enough at CHF 12.99 a year to be a spare WireGuard endpoint
- reliability: no reliability event recorded
- notes: The smallest and cheapest Swiss option found, and the one with the least traffic: 500 GB a month on the 512 MB rung. The 1 GB rung is CHF 22.22 a year for 1 TB, which is the better buy if traffic matters. The page prints prices in CHF, not EUR, and the entity is a real GmbH with a CHE number. The add-to-cart is a POST form with a pricing_id, so there is no GET cart URL to hand a buyer; the package page plus the pricing_id is the deepest honest link. Not established: payment rails, whether a debit or prepaid card works, any card hold, and whether the traffic cap is enforced or advisory.
- evidence note: prices, cycles, shapes and the IPv6-only statement are quoted from the vendor's own order page read. The entity is quoted from the vendor's client-area footer. Payment rails, card hold and checkout fields were not read.
- evidence:
  - [1] 2026-10-24: quoted plan card: 'VPS Basic 512MB - IPv6 only AMS CPU: Intel Xeon - 1 Shared-Core RAM: 512MB Storage: 10GB SSD IPs: IPv6 Options: BGP Session Traffic: 500GB This offer does NOT include an IPv4 Address - it IPv6 ONLY' with '3 Months @ CHF 5,00 CHF' and '12 Months @ CHF 12,99 CHF'
  - [1] 2026-10-24: the same 512 MB IPv6-only shape is offered at three locations on one page: AMS, MCI and ZRH, each at '3 Months @ CHF 5,00 CHF' and '12 Months @ CHF 12,99 CHF'
  - [1] 2026-10-24: the add-to-cart control is a POST form to /order/main/index/BGP-Basic with a pricing_id select; for the 512MB AMS rung the options are pricing_id 1390 (3 Months @ CHF 5,00) and 1391 (12 Months @ CHF 12,99)
  - [2] 2026-10-24: quoted footer: 'iFog GmbH - CHE-137.614.651' - a registered Swiss company number
  - [3] 2026-10-24: quoted: 'Our special 256MB VPSs are available in all our locations, all come with IPv4 and IPv6 connectivity' - the 256 MB specials are dual-stack, so the IPv6-only line is the BGP Basic group only
- sources:
  - [1] https://my.ifog.ch/order/main/index/BGP-Basic
  - [2] https://my.ifog.ch/
  - [3] https://ifog.ch/en/vps/specials
