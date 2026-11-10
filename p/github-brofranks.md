# Headwire

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-brofranks/ | JSON https://fshy.ajam.dev/api/v1/entity/github-brofranks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Headwire

- `egress/headwire` | self-hosted, last resort | verdict fails-egress | evidence documented | binding per-ip-shaping | category wireguard mesh | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/brofranks/headwire
- price USD 0
- free tier: Headwire statically configures WireGuard peers with support for NAT traversal using DERP relays. It is experimental. No hosted service and no price are offered. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance: relays rely on self-hosted DERP servers or Tailscale free rate-limited relays.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account required. Self-hosted DERP servers or rate-limited Tailscale DERP relays provide relay infrastructure. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): Tailscale's DERP relays are described as free rate-limited relays [1]
- binding note: There is no ingress to meter. If Tailscale's DERP relays are borrowed, the rate limit on those relays is the first thing to bite, and it applies to the relay path only.
- interface detail: headwire ping 100.64.0.2; config file with [DERPRegion] and [Interface].
- tooling: headwire CLI plus a macOS app; config file with DERPRegion and Interface sections.
- composes with: Gives a free VM a private WireGuard path to a laptop; to expose it publicly you still need a tunnel or a public relay.
- reliability: Experimental and dependency-heavy: it reuses Tailscale data-plane libraries and needs a DERP server or Tailscale's rate-limited relays.
- notes: Launched 2026-09-24. A one-person experimental project that composes WireGuard with Tailscale's open-source data plane. It is a way to reach your own machines, not to publish a port.
- evidence note: Mesh networking topology is documented. Operates as a private WireGuard overlay without public ingress endpoints.
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: Configuration is a standard WireGuard-plus-DERP file: a [DERPRegion] block with ID and Nodes, then an [Interface] block. The tool writes peers directly rather than calling an API.
  - ingress: none
  - volume_stated: No allowance: the relays are a user's own DERP servers or Tailscale's free rate-limited relays.
  - bytes_transit: overlay-only
  - transit_note: Direct WireGuard where NAT allows, DERP relay otherwise.
- evidence:
  - [1] 2026-10-23: Statically configures WireGuard peers with DERP relay fallback, upgrades to a direct path; config uses a [DERPRegion] block and an [Interface] block; experimental.
  - [2] 2026-09-24: Show HN launch date and description: WireGuard with NAT traversal via Tailscale's magicsock.
- sources:
  - [1] https://github.com/brofranks/headwire
  - [2] https://news.ycombinator.com/item?id=49834349
