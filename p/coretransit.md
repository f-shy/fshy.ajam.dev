# Core Transit

> coretransit.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coretransit/ | JSON https://fshy.ajam.dev/api/v1/entity/coretransit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Core Transit

- `egress/core-transit` | paid-only | evidence documented | binding none | category routed public IP over WireGuard | tier wireguard
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.coretransit.net/core-transit-pricing/
- price USD 38 per month for a WireGuard tunnel; USD 10 per month for a BGP session | parsed USD 10/mo
- free tier: No free tier. "WireGuard 38$ /Month" is the cheapest WireGuard entry; the only lower entry is L2TP at "32$". | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No transfer allowance is published. The plan lists a rate: "100Mbps & Upgrade to 1Gbps", and "IPv4 Addresses: Available on Request".; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: Self-serve portal checkout, with purchase orders accepted: "Can I pay via a purchase order or for a full year in advance? Yes!". The signup form was not read. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 100 Mbps, upgradeable to 1 Gbps [1]
- binding note: 100 Mbps port speed supports up to 32 TB monthly transfer. The primary constraint is pricing at USD 38 per tunnel.
- interface detail: Client-configured tunnel; billing portal is a standard hosting cart.
- tooling: wg-quick on the router at the customer end; L2TP, GRE and WireGuard are all offered
- composes with: Only worth it if a custom block and BGP are needed, which a free-tier VM cannot provide on its own.
- reliability: Standard service is described as best-effort and month-to-month; no uptime figure is published for it.
- notes: Enterprise tier is USD 99/month plus USD 279 setup with a 12-month minimum and a managed device; that tier is out of reach here but confirms the vendor ships real L2 handoff. Competitor GetAStatic's table lists Core Transit at "$38/mo (WireGuard)" and "Any port", which agrees with the vendor's own page. Not a free or nearly-free answer at any tier.
- evidence note: Price, rate and options are first-party. Address count at the base price is not stated ("Available on Request"), which is the gap a sales email would close.
- extras:
  - wg_path: extractable
  - wg_detail: The product is an encrypted tunnel with custom addressing, configured on the router at the customer end: "Encrypted Tunnels", "Bring Your Own Router", "Custom IP Allocations", "IPv4 & IPv6". A BGP session is a paid add-on at "$10 /Month".
  - ingress: tcp+udp
  - volume_stated: No transfer allowance is published. The plan lists a rate: "100Mbps & Upgrade to 1Gbps", and "IPv4 Addresses: Available on Request".
  - bytes_transit: yes
  - transit_note: Core Transit routes the customer's allocation from its own N+1 redundant network.
- evidence:
  - [1] 2026-10-23: WireGuard USD 38/month with custom IP allocations, 100 Mbps upgradeable to 1 Gbps, IPv4 and IPv6, BGP addon USD 10/month; month-to-month
  - [2] 2026-10-23: "Static IP Anywhere" is aimed at hobbyists, small business, MSPs and enterprises; a 30 minute call is offered for enterprise sizing
- sources:
  - [1] https://www.coretransit.net/core-transit-pricing/
  - [2] https://www.coretransit.net/
