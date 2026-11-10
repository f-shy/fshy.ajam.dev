# Innernet

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-tonarino/ | JSON https://fshy.ajam.dev/api/v1/entity/github-tonarino.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Innernet

- `egress/innernet` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category WireGuard overlay (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/tonarino/innernet
- price USD 0
- free tier: 'A private network system that uses WireGuard under the hood.' MIT licensed and self-hosted; no quota of any kind. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance exists: the coordination server is the operator's.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: self-hosted; peers are invited by an admin running 'innernet-server add-peer', so identity is a key handed out locally | country: None
- interface: cli
- binding note: Nothing counts bytes. At 1 TiB/month only the host's own link binds, and there is no public listener through which a reader could spend it.
- interface detail: innernet-server and the innernet client
- tooling: innernet and innernet-server
- composes with: a private mesh control plane; composes with a public ingress but adds none
- reliability: 'should be considered experimental software'; the coordination server's uptime is the constraint
- notes: Self-described as similar in goal to nebula and Tailscale. The README's own warning - 'This has not received an independent security audit' - is a technical reliability fact, not a reason to exclude it.
- evidence note: Point-to-point WireGuard mesh network. Overlay coordination and peer configuration are documented in repository manuals.
- self hosted: yes
- extras:
  - wg_path: unknown
  - wg_detail: The README states WireGuard under the hood and a coordination server that 'manages peers and provide endpoint information so peers can directly connect', but no page read documents a .conf export.
  - ingress: none
  - volume_stated: No allowance exists: the coordination server is the operator's.
  - bytes_transit: overlay-only
  - transit_note: peers connect directly; the coordination server hands out endpoints and sees no payload
- evidence:
  - [1] 2026-10-23: 'A private network system that uses WireGuard under the hood'; 'Every innernet network needs a coordination server to manage peers and provide endpoint information so peers can directly connect to each other'
- sources:
  - [1] https://github.com/tonarino/innernet
