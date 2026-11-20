# Ignyte Solutions

> ignyte.solutions | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ignyte/ | JSON https://fshy.ajam.dev/api/v1/entity/ignyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ignyte Solutions

- `egress/ignyte-solutions` | paid-only | evidence documented | binding volume-quota | category dedicated IPv4 over WireGuard | tier standard
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://ignyte.solutions/
- price USD 7 per month for one IPv4; USD 3 per month for each additional address up to ten | parsed USD 3/mo
- free tier: No free tier and no trial named: "Standard ... $7/ month" and "Enterprise ... Custom". | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No transfer allowance and no rate is published on the homepage. The comparison table lists architecture only, and "Zero traffic logs" is a logging claim rather than a quota.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: A paid dashboard signup ("Reserve an IP"); the signup form was not read. The operator describes itself as a Public Benefit Corporation. | country: None
- interface: cli
- limits:
  - volume-quota (binding): unpublished [1]
  - request-rate: 10 IPv4 addresses maximum on Standard, at USD 3 each [1]
- binding note: No allowance is published, so 1 TiB/month meets an unknown policy rather than a number. The address count is the documented limit: one address at USD 7 and up to nine more at USD 3.
- interface detail: Dashboard provisioning; no API named on the page read.
- tooling: dashboard-issued tunnel; client-side WireGuard
- composes with: One address with every port open replaces a port-mapped tunnel and a reverse proxy at once.
- reliability: Edge scrubbing is included; no uptime figure is published for the Standard tier.
- notes: Offers up to 65,535 port forward mappings via dedicated IPv4 tunneling. Tunnel traffic migrates across an anycast router fabric rather than relying on a single tunnel endpoint.
- evidence note: Price, port range, protocol and the 1:1 mapping are first-party. Volume is the open field, and a support email is what would close it.
- extras:
  - wg_path: extractable
  - wg_detail: The address is mapped one to one over a tunnel: "A public IPv4 delivered through an encrypted WireGuard tunnel and mapped 1:1 to your device." Provisioning is a dashboard action: "Provisioned in under a minute from the dashboard", and the port range is the selling point: "Bind up to 65,535 TCP and UDP ports".
  - ingress: tcp+udp
  - volume_stated: No transfer allowance and no rate is published on the homepage. The comparison table lists architecture only, and "Zero traffic logs" is a logging claim rather than a quota.
  - bytes_transit: yes
  - transit_note: BGP-managed ingress from the vendor's own edge fabric, six regions.
- evidence:
  - [1] 2026-10-23: USD 7/month for one dedicated IPv4 with up to 65,535 TCP and UDP ports; additional IPs at USD 3 up to ten; WireGuard tunnel; DDoS scrubbing included; no bandwidth figure
- sources:
  - [1] https://ignyte.solutions/
