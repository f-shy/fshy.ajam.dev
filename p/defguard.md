# Defguard

> defguard.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/defguard/ | JSON https://fshy.ajam.dev/api/v1/entity/defguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Defguard

- `egress/defguard` | self-hosted, last resort | verdict fails-egress | evidence documented | binding request-rate | category WireGuard management (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://defguard.net/pricing/
- price USD 0
- free tier: Open Source: 'Always free', 'Unlimited users and locations - core features.' Business: 'free up to 10 users and 1 location.' | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance anywhere in the plan table; the plans meter users and locations.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: self-hosted: the Open Source plan needs no vendor account; the Business plan is a hosted or licensed deployment with its own admin | country: None
- interface: cli
- limits:
  - request-rate (binding): The published caps are users and locations, for which the vocabulary has no token; request-rate is the nearest. Nothing counts bytes, and there is no public listener to spend them through. [1]
- binding note: The published caps are users and locations, for which the vocabulary has no token; request-rate is the nearest. Nothing counts bytes, and there is no public listener to spend them through.
- interface detail: web admin plus the desktop client
- tooling: defguard server, defguard desktop client, standard WireGuard configs
- composes with: a control plane for a private WireGuard mesh; it composes with a public ingress on the same VPS
- reliability: the Open Source plan is self-run, so uptime and key rotation are local work
- notes: Open-source WireGuard VPN management platform. Provides VPN client configurations for private network access; does not provide a public reverse proxy service.
- evidence note: Reading the gateway documentation would establish whether Defguard's own gateway can bind a public port; the VPN-server model suggests not.
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: Defguard provisions a user's tunnel: 'Zero-touch Desktop Client Provisioning' and 'Client configuration update based on tokens'. The product is a WireGuard control plane, which is the one place where a standard client config is the deliverable.
  - ingress: none
  - volume_stated: No byte allowance anywhere in the plan table; the plans meter users and locations.
  - bytes_transit: overlay-only
  - transit_note: peers reach each other over the WireGuard tunnels Defguard configures; the server sees handshakes, not payload
- evidence:
  - [1] 2026-10-23: Open Source is 'Always free' with 'Unlimited users and locations'; Business is 'free up to 10 users and 1 location'
  - [1] 2026-10-23: 'Zero-touch Desktop Client Provisioning' and 'Client configuration update based on tokens', the mechanism that issues WireGuard configs
- sources:
  - [1] https://defguard.net/pricing/
