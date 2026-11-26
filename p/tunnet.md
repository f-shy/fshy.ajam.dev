# Tunnet

> tunnet.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnet/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnet

- `egress/tunnet` | fails-egress | evidence documented | binding write-gated | category mesh vpn with hosted control plane and public https tunnels | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:43:49.307Z (live) | stale on 2026-12-26
- url https://tunnet.io/
- price USD 0
- free tier: Private networking for every machine. SSH, internal apps, and public HTTPS - without a VPN. Open source. Start for free. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published on the landing page.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'Start for free' creates an account at app.tunnet.io. | country: None
- interface: cli
- limits:
  - write-gated (binding): public tunnels are HTTPS; no public TCP or UDP tunnel is described [1]
- binding note: No quota is published; public ingress is HTTPS only, so the protocol fails first. Private mesh paths carry TCP and UDP but require both peers to enrol.
- interface detail: CLI and Kubernetes operator.
- tooling: vendor CLI plus Rust daemon.
- composes with: Mesh between rented boxes; HTTPS ingress for services.
- reliability: Relay fallback is used when a firewall blocks direct paths.
- notes: Built on iroh. The public side is an HTTPS tunnel with a relay fallback; the private side is a mesh.
- evidence note: A published quota and a UDP ingress type would change this; neither is on the page read.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published on the landing page.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'SSH, internal apps, and public HTTPS - without a VPN. Open source. Start for free.'; 'Direct paths first, relay when a firewall gets in the way'
  - [1] 2026-11-25: the public side of the product is HTTPS; no TCP or UDP public tunnel is named | capture: sha256:5eb33e44cb66ec35fa9ef4f57b8c0d10739d343ebd32cea6b35dd466b09286b3 | quote: Private access, SSH, internal apps, and public HTTPS - one identity, not four products stitched together.
- sources:
  - [1] https://tunnet.io/
