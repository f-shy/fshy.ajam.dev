# Tunnel-IP.com

> tunnel-ip.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnel-ip/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnel-ip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnel-IP.com (Netaris)

- `egress/tunnel-ip` | paid-only | evidence documented | binding none | category routed public IP over WireGuard | tier basic
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnel-ip.com/
- price EUR 8 per month for Basic (1 IPv4, 1 /56 IPv6, 1 tunnel, 10 Gbps) | parsed USD 8.95/mo
- free tier: No free tier. The offer list is "Basic 8 [EUR] / mois", "Custom X [EUR] / mois" and "BYOIP 11 [EUR] / mois"; the page prints the euro sign, rendered here as EUR. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No transfer allowance is stated anywhere on the page. The plan lists a port rate instead: "10 Gbps" on every tier.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: Orders are placed in the Netaris panel (panel.netaris.fr), which implies a paid account; the registration form was not read. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 10 Gbps port per tunnel, no byte allowance published [1]
- binding note: At 1 TiB/month, 3.24 Mbit/s sustained, a 10 Gbps port is not the constraint and no byte quota is published. What would bind at larger scale is the one-tunnel, one-IPv4 shape of the Basic plan, which is an allocation limit rather than a volume one.
- interface detail: Tunnels are created and deleted in the panel; no API named on the pages read.
- tooling: wg-quick; panel provisioning for GRE, VXLAN, EOIP, WireGuard, IPIP
- composes with: One IPv4 plus a /56 on a single tunnel covers a small fleet; the /56 removes the port-remap question for IPv6 clients.
- reliability: Anti-DDoS is an option on the Custom tier only; nothing is stated about attacks on the Basic tier.
- notes: Tunnel provider offering public IP transit with optional BGP sessions included in base subscription tiers. Bridge configurations carry an extra EUR 1 fee.
- evidence note: Price, allocation and tunnel types are first-party. The volume policy is absent, so a support answer would raise the volume field from unstated to documented.
- extras:
  - wg_path: extractable
  - wg_detail: WireGuard is one of six tunnel types that can be created in the panel: "GRE, VXLAN, EOIP, WireGuard, IPIP, BGP", and "vous pouvez le creer avec n'importe quel type et le supprimer comme vous le souhaitez sur votre panel". The Basic plan carries "1 IPv4" and "1 /56 IPv6" routed to the tunnel.
  - ingress: tcp+udp
  - volume_stated: No transfer allowance is stated anywhere on the page. The plan lists a port rate instead: "10 Gbps" on every tier.
  - bytes_transit: yes
  - transit_note: The vendor runs the tunnels on its own network, "interconnecte avec les plus gros operateurs Francais".
- evidence:
  - [1] 2026-10-23: Basic 8 EUR/mo with 1 IPv4, 1 /56 IPv6, 1 tunnel, 1 subnet, 10 Gbps and a BGP session; WireGuard among the six tunnel technologies; no traffic figure
  - [2] 2026-10-23: the documentation site is a stub: "Documentation en cours d'ecriture", so the panel workflow could not be checked
- sources:
  - [1] https://tunnel-ip.com/
  - [2] https://docs.tunnel-ip.com/
