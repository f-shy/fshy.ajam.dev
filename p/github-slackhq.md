# Nebula

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-slackhq/ | JSON https://fshy.ajam.dev/api/v1/entity/github-slackhq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nebula

- `egress/nebula` | self-hosted, last resort | verdict fails-egress | evidence inferred | binding none | category overlay network (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/slackhq/nebula
- price USD 0
- free tier: 'Nebula is a scalable overlay networking tool with a focus on performance, simplicity and security. It lets you seamlessly connect computers anywhere in the network.' Self-hosted; no quota. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance: there is no vendor and no hosted service.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: self-hosted; membership is a signed certificate from the operator's CA | country: None
- interface: cli
- binding note: Nothing meters bytes and nothing publishes a port, so no constraint fires at 1 TiB/month because the traffic cannot leave the overlay.
- interface detail: config files plus a certificate authority the operator runs
- tooling: nebula and nebula-cert binaries
- composes with: a private overlay that composes with a public ingress and adds none
- reliability: self-operated; certificate issuance and lighthouse uptime are local work
- notes: Included because the supplied list names it and because a reader will confuse it with a WireGuard tool.
- evidence note: The overlay claim is quoted; the 'no ingress' conclusion is inferred from the description, because a feature that does not exist has no page saying so. Reading the lighthouse documentation would raise this to documented.
- self hosted: yes
- extras:
  - wg_path: unknown
  - wg_detail: The repository describes 'encryption, security groups, certificates, and tunneling' without naming WireGuard; no protocol page was read, so whether the transport can carry a WireGuard datagram is open.
  - ingress: none
  - volume_stated: No allowance: there is no vendor and no hosted service.
  - bytes_transit: overlay-only
  - transit_note: peers relay through lighthouses only to find each other; payload goes peer to peer
- evidence:
  - [1] 2026-10-23: 'Nebula is a scalable overlay networking tool'; it 'lets you seamlessly connect computers anywhere in the network' and combines 'encryption, security groups, certificates, and tunneling'
- sources:
  - [1] https://github.com/slackhq/nebula
