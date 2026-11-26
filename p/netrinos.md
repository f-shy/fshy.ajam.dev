# Netrinos

> netrinos.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netrinos/ | JSON https://fshy.ajam.dev/api/v1/entity/netrinos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Netrinos

- `egress/netrinos` | fails-egress | evidence documented | binding none | category mesh vpn | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:31.197Z (live) | stale on 2026-12-20
- url https://netrinos.com/pricing
- price USD 0
- free tier: Personal Free Users 5 - Devices 100 - Virtual Devices 5 - Remote Gateways 1 - Remote Routes 5. Port forwarding: not included. | unit: users | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No bandwidth metering: the pricing description says 14-day free trial, no bandwidth charges. Traffic flows peer to peer.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an email address, a first name, a last name, a username and a password | country: None
- interface: cli
- limits:
  - per-object-cap: 5 users, 100 devices, 5 virtual devices, 1 remote gateway, 5 remote routes [1]
- limits note: port forwarding is not included on the Personal Free plan
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
  - [2] 2026-10-23: Not a privacy VPN; a private network where devices connect peer to peer, encrypted with WireGuard.
  - [3] 2025-12-19: Show HN launch date.
  - [1] 2026-11-25: Personal Free lists 5 users, 100 devices, 5 virtual devices, 1 remote gateway and 5 remote routes, and no port forwarding | capture: sha256:e4f1a9f62a0664bd645a6bb7862f1f93d520e0316f2e0478978917844297c4fc
  - [1] 2026-11-25: Personal Free lists 5 users, 100 devices, 5 virtual devices, 1 remote gateway and 5 remote routes | capture: sha256:e4f1a9f62a0664bd645a6bb7862f1f93d520e0316f2e0478978917844297c4fc | quote: | Users | 5 | 10+ | Unlimited | | Devices | 100 | 100+ | Unlimited | | Virtual Devices | 5 | Unlimited | Unlimited | | Remote Gateways | 1 | Unlimited | Unlimited | | Remote Routes | 5 | Unlimited | Unlimited |
  - [1] 2026-11-25: the Port forwarding row has a dash under Personal Free: not included | capture: sha256:e4f1a9f62a0664bd645a6bb7862f1f93d520e0316f2e0478978917844297c4fc | quote: | Port forwarding | – | – | |
  - [4] 2026-11-25: the signup form asks for a first name, a last name, an email address, a username and a password | capture: sha256:6dfed95c0db3bac631e3233b122a36c9eb11a5369f6e0673af811ac0c1ebdeb7 | quote: First name ... Last name ... Email address ... Choose a Username ... Password
- sources:
  - [1] https://netrinos.com/pricing
  - [2] https://netrinos.com/
  - [3] https://news.ycombinator.com/item?id=46331364
  - [4] https://app.netrinos.com/signup
