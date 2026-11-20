# Netrinos

> netrinos.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netrinos/ | JSON https://fshy.ajam.dev/api/v1/entity/netrinos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Netrinos

- `egress/netrinos` | fails-egress | evidence documented | binding write-gated | category mesh vpn | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://netrinos.com/pricing
- price USD 0
- free tier: Personal Free Users 3 - Devices 100 - Virtual Devices 3 - Remote Gateways 1 - Remote Routes 3. Port forwarding: not included. | unit: users | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No bandwidth metering: the pricing description says 14-day free trial, no bandwidth charges. Traffic flows peer to peer.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Install, log in, connected. The signup page is app.netrinos.com/signup. | country: None
- interface: cli
- limits:
  - write-gated (binding): port forwarding not included on Personal Free [1]
  - per-object-cap: 3 users, 100 devices, 1 remote gateway, 3 remote routes [1]
- binding note: The free plan has no port forwarding at all, so a public UDP ingress does not exist to be metered; volume never becomes the question.
- interface detail: Install, log in, connected; no configuration files described.
- tooling: Netrinos client for Windows, macOS, Linux, iOS, Android and ARM; routing through nftables, PF and WFP.
- composes with: Replaces a public endpoint with a private overlay: a free VM and a laptop can reach each other without any port, but no third party can dial in.
- reliability: There is no stated SLA; peer-to-peer means availability depends on the peers' own networks.
- notes: Launched 2025-12-19. It is a Twingate-shaped private mesh, not an ingress provider. The free tier is explicitly non-commercial, which matters for anything run as a service.
- evidence note: A measured mesh between two machines would confirm the WireGuard data plane, but it would not change the missing port-forwarding row.
- extras:
  - wg_path: native-conf
  - wg_detail: Every connection uses WireGuard: the product page says Every connection uses WireGuard and the pricing page lists WireGuard encryption and end-to-end encryption as core features. Configs are pushed by a user rather than exported as a .conf file, and no registration API is documented.
  - ingress: none
  - volume_stated: No bandwidth metering: the pricing description says 14-day free trial, no bandwidth charges. Traffic flows peer to peer.
  - bytes_transit: overlay-only
  - transit_note: Traffic flows directly between devices, with an encrypted relay as fallback.
- evidence:
  - [1] 2026-10-23: Personal Free: 3 users, 100 devices, 3 virtual devices, 1 remote gateway, 3 remote routes; the Port forwarding row is marked as not included.
  - [2] 2026-10-23: Not a privacy VPN; a private network where devices connect peer to peer, encrypted with WireGuard.
  - [3] 2025-12-19: Show HN launch date.
- sources:
  - [1] https://netrinos.com/pricing
  - [2] https://netrinos.com/
  - [3] https://news.ycombinator.com/item?id=46331364
