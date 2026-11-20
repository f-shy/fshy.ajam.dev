# WireGress

> wiregress.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wiregress/ | JSON https://fshy.ajam.dev/api/v1/entity/wiregress.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WireGress

- `egress/wiregress` | fails-quota | evidence documented | binding volume-quota | category managed WireGuard gateway with a static public IP | tier core-plus
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://wiregress.com/pricing.html
- price USD 15 per month for Core (450 GB, outbound); USD 29 per month for Core Plus (900 GB, inbound) | parsed USD 15/mo
- free tier: No free tier and no trial. "Core $15 / month" and "Core Plus $29 / month"; "Plans from $15/month". | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "450 GB monthly data transfer" on Core and "900 GB monthly data transfer" on Core Plus. No overage price is published; the next step offered is Custom.; ingress: tcp+udp | metered: yes | free allowance: "450 GB monthly data transfer" on Core and "900 GB monthly data transfer" on Core Plus. No overage price is published; the next step offered is Custom. | source: [1]
- identity: card | detail: A business-oriented paid signup; the Custom tier routes through sales. The signup form was not read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 450 GB per month on Core, 900 GB on Core Plus [1]
  - request-rate: 10 peers included per gateway [1]
- binding note: 900 GB is 0.818 TiB, so 1 TiB/month needs the Custom tier, and the price of that is a quote. At USD 29 for 0.9 TB the row is about USD 32 per TiB, the most expensive volume.
- interface detail: Dashboard for peers and usage; no API named.
- tooling: dashboard-generated peer configurations for WireGuard
- composes with: Volume cap restricts composition; the inbound plan includes dedicated public address assignment.
- reliability: Dedicated gateway per customer with no shared contention; 24/7 operations is claimed, no SLA figure published for the listed tiers.
- notes: The Core tier cannot answer test I at all: its product is outbound egress, and inbound is the thing Core Plus sells. The vendor is operated by APYL and markets to business and remote-site connectivity, which sets the price floor.
- evidence note: Both tiers, their transfer caps and the inbound/outbound split are first-party. A quote for Custom would show what 1 TiB actually costs.
- extras:
  - wg_path: native-conf
  - wg_detail: Peers are issued from the dashboard: "Create and revoke peers, generate configurations, and monitor usage from one dashboard." Inbound requires the higher tier: Core Plus adds "Configurable inbound TCP/UDP port forwarding" while Core is "Outbound connectivity" only.
  - ingress: tcp+udp
  - volume_tib_month: 0.818
  - volume_stated: "450 GB monthly data transfer" on Core and "900 GB monthly data transfer" on Core Plus. No overage price is published; the next step offered is Custom.
  - bytes_transit: yes
  - transit_note: APYL operates the gateways and the addresses.
- evidence:
  - [1] 2026-10-23: Core USD 15/month, 450 GB, outbound only; Core Plus USD 29/month, 900 GB, inbound TCP/UDP port forwarding; 10 peers; Custom by quote
  - [2] 2026-10-23: "One dedicated gateway. One stable public IP. Up to 10 peers included. No per-user licensing."
- sources:
  - [1] https://wiregress.com/pricing.html
  - [2] https://wiregress.com/
