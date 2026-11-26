# PremierVPN

> premiervpn.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiervpn/ | JSON https://fshy.ajam.dev/api/v1/entity/premiervpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PremierVPN

- `egress/premiervpn` | paid-only | evidence documented | binding per-ip-shaping | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://premiervpn.net/port-forwarding-wireguard-dedicated-vpn
- price USD 11.99 per month or USD 119.99 per year | parsed USD 11.99/mo
- free tier: No free tier. $11.99 per month or $119.99 per year, and the page states no setup fee: No setup fee, no bandwidth charges. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The server, its bandwidth and its IP are yours alone, so nobody else's traffic competes with yours. The page also states No setup fee, no bandwidth charges, with no byte figure.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: A checkout with a 24-hour provisioning step: Set up within 24 hours; no free tier and no trial stated on the page. | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): bandwidth is shared with nobody but the tenant, and the page states no byte cap: The server, its bandwidth and its IP are yours alone [1]
  - write-gated: provisioning is manual and takes up to a day: Set up within 24 hours [1]
- binding note: No byte cap is stated and the address is dedicated, so at 1 TiB/month the risk is the tenant's own bandwidth share on one machine rather than a quota. Provisioning delay is the only gate.
- interface detail: Dashboard for forwards per the page: Add and remove forwards from your dashboard.
- tooling: WireGuard, with forwards managed in a dashboard.
- composes with: Replaces the need for a separate free VM: the tunnel endpoint is also the machine, and every port can be published.
- reliability: unverified: single small provider, no uptime figure or audit read; the dedicated server has no failover in the offer as written.
- notes: VPN provider offering dedicated static IP addresses with unlimited port forwarding as standard subscription features.
- evidence note: All facts are from the vendor's own product page read. A measured claim would need a provisioned server, a forwarded port and a byte count; the absence of any published cap is itself the documented fact.
- extras:
  - wg_path: native-conf
  - wg_detail: A dedicated WireGuard server with a static address: Unlimited port forwarding, a static dedicated IP and the modern WireGuard protocol, on a server that only you use.
  - ingress: tcp+udp
  - volume_stated: The server, its bandwidth and its IP are yours alone, so nobody else's traffic competes with yours. The page also states No setup fee, no bandwidth charges, with no byte figure.
  - bytes_transit: yes
  - transit_note: Traffic crosses the tenant's own dedicated server.
- evidence:
  - [1] 2026-10-23: Unlimited port forwarding on any external port mapped to any internal port, TCP, UDP or both, a static dedicated IP, WireGuard, $11.99 per month or $119.99 per year, no bandwidth charges, provisioning within 24 hours.
- sources:
  - [1] https://premiervpn.net/port-forwarding-wireguard-dedicated-vpn
