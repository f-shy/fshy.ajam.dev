# Defined Networking

> defined.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/defined/ | JSON https://fshy.ajam.dev/api/v1/entity/defined.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Defined Networking

- `egress/defined-networking` | fails-egress | evidence documented | binding none | category managed nebula overlay (private, no public ingress) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.defined.net/
- price USD 0 (100 devices)
- free tier: Get set up in minutes and connect your first 100 devices free, no credit card required. | unit: users | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published; the free unit is devices.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: signup at admin.defined.net, 'no credit card required'. | country: None
- interface: cli
- binding note: Nothing is metered, so no quota fails at 1 TiB/month. The structure fails: a Nebula overlay has no public address, so an outside peer must be enrolled before it can send a packet.
- interface detail: Web console plus Nebula binaries.
- tooling: Nebula clients plus the vendor's certificate console.
- composes with: Private path between two rented boxes; no ingress.
- reliability: Control plane is hosted and closed; losing it blocks new certificate issuance.
- notes: Commercial control plane for open-source Nebula. The aggregator is explicit that this is private overlay access rather than public-URL ingress.
- evidence note: A public ingress feature would change the verdict; the page describes private overlay access.
- extras:
  - wg_path: none
  - wg_detail: The data plane is Nebula, which is its own protocol on UDP 4242, not WireGuard. No .conf export exists; the overlay certificate is issued by the hosted control plane.
  - ingress: tcp+udp
  - volume_stated: No byte allowance is published; the free unit is devices.
  - bytes_transit: overlay-only
  - transit_note: Peer-to-peer Nebula; the hosted plane issues certificates.
- evidence:
  - [1] 2026-10-23: 'connect your first 100 devices free, no credit card required'; 'Encrypted with the Noise Protocol Framework'
- sources:
  - [1] https://www.defined.net/
