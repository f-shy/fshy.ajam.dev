# Headscale

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-juanfont/ | JSON https://fshy.ajam.dev/api/v1/entity/github-juanfont.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Headscale

- `egress/headscale` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category mesh control plane (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/juanfont/headscale
- free tier: BSD-3 control server for Tailscale clients, with no node cap | unit: unlimited | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: signalling only once peers connect directly; DERP relay only when they do not | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: cli
- binding note: the software imposes no byte meter; what runs out is the monthly egress allowance of the host it runs on, and that host is a separate provider
- interface detail: tailscale up --login-server against your own headscale
- tooling: tailscale clients against headscale
- composes with: signalling for a private mesh: it composes with a private set of machines and carries no bytes once they hole-punch.
- reliability: the control server's uptime is the constraint
- notes: 2026-10-23: public instances exist and carry no ingress. One public control server, headscale.kf8edq.dev, publishes join keys and shows 'Active Nodes 4 / 5 total', so the free public instance is a 5-node control plane with no public listener of any kind. A control plane distributes keys and endpoints; the payload never touches it, which is why headscale cannot satisfy ingress test at any size. Re-graded 2026-10-23: the software is free and the path is not, because it needs a host. The finding is the host.
- evidence note: Control server architecture and mesh coordination specifications are documented in official project documentation.
- self hosted: yes
- extras:
  - stale_after_days: 180
  - bytes_transit: no
  - transit_note: a control server for Tailscale clients: it distributes keys and endpoints and sees no payload
  - hosting_requirement: a rented or free compute service; no local machine is assumed
- evidence:
  - [1] 2026-10-22: BSD-3 control server with no node limit stated
  - [2] 2026-10-23: a public headscale instance advertising 'Active Nodes 4 / 5 total' and an authkey join flow, with no service-publishing feature, read through the search index
- sources:
  - [1] https://github.com/juanfont/headscale
  - [2] https://kf8edq.dev/
