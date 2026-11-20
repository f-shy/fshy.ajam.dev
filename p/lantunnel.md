# Lantunnel

> lantunnel.app | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lantunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/lantunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lantunnel

- `egress/lantunnel` | fails-egress | evidence documented | binding none | category p2p mesh with an optional hosted control plane | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://lantunnel.app/
- price USD 0
- free tier: Lantunnel Client on each device. Encrypted P2P paths, Relay fallback, and no router port forwarding. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published; Relay capacity is described as a shared resource rather than a quota.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: clients are free; the hosted control plane at lantunnel.app is closed source and optional. | country: None
- interface: cli
- binding note: No public URL and no metered quota: the mesh gives reachability between enrolled devices only, and 'Direct connectivity is not guaranteed'.
- interface detail: GUI clients plus a CLI.
- tooling: desktop and mobile clients.
- composes with: Private access between boxes already held.
- reliability: Relay capacity is shared; direct paths depend on NAT.
- notes: The hosted control plane does not carry public ingress; that would need a Gateway run locally.
- evidence note: A hosted gateway with a public port would change it; the page says a self-hosted Gateway is what needs a public IP.
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance is published; Relay capacity is described as a shared resource rather than a quota.
  - bytes_transit: overlay-only
  - transit_note: Direct QUIC when NAT allows, else encrypted relay.
- evidence:
  - [1] 2026-10-23: 'Normal Client access does not require router port forwarding on your LAN or a public URL for each service. If you host a Gateway yourself, that Gateway needs a reachable public IP'
- sources:
  - [1] https://lantunnel.app/
