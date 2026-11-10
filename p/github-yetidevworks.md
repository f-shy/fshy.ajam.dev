# YTunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-yetidevworks/ | JSON https://fshy.ajam.dev/api/v1/entity/github-yetidevworks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YTunnel

- `egress/ytunnel` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel client (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/yetidevworks/ytunnel
- price USD 0
- free tier: MIT Licensed, Rust powered, uses your domains and creates Cloudflare Tunnels with easy to use TUI | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: a client of egress/cloudflare-tunnel: the hosted capacity and its limits are those of Cloudflare Tunnel in the user's own Cloudflare account. Creates Cloudflare Tunnels from a TUI.
- interface detail: not established
- tooling: self-hosted binaries
- composes with: Drives Cloudflare Tunnel in the user's own Cloudflare account; see egress/cloudflare-tunnel.
- reliability: the same as interface detail
- notes: Creates Cloudflare Tunnels from a TUI. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: MIT Licensed, Rust powered, uses your domains and creates Cloudflare Tunnels with easy to use TUI
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/yetidevworks/ytunnel
