# YTunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-yetidevworks/ | JSON https://fshy.ajam.dev/api/v1/entity/github-yetidevworks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YTunnel

- `egress/ytunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel client (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.926Z (live) | stale on 2026-12-20
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
- tooling: The user installs and runs the ytunnel CLI/TUI and cloudflared, creating Cloudflare Tunnels in the user's own Cloudflare account; no hosted endpoint is offered.
- composes with: Drives Cloudflare Tunnel in the user's own Cloudflare account; see egress/cloudflare-tunnel.
- reliability: the same as interface detail
- notes: Creates Cloudflare Tunnels from a TUI. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it presents a TUI-first CLI that manages Cloudflare Tunnels on the user's own Cloudflare domain and account, with no hosted endpoint or published byte allowance. The list entry is superseded as the basis; the egress restriction still holds.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: MIT Licensed, Rust powered, uses your domains and creates Cloudflare Tunnels with easy to use TUI
  - [2] 2026-11-19: the first-party README presents user-installed software that drives Cloudflare Tunnel on the user's own domain and account, with no hosted egress of its own | capture: sha256:6f7717d2f1ee3f9bc9f1fe1ca285c34afdcea1acde77e619d426ba937c399230 | quote: A TUI-first CLI for managing Cloudflare Tunnels with custom domains. Think ngrok, but using your own Cloudflare domain with persistent URLs and a dashboard to manage them.
  - [2] 2026-11-19: the first-party README describes a management tool the user installs and runs to drive cloudflared, so there is no hosted endpoint | capture: sha256:6f7717d2f1ee3f9bc9f1fe1ca285c34afdcea1acde77e619d426ba937c399230 | quote: YTunnel is a management tool, not a daemon itself. Here's how the pieces fit together:
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:6f7717d2f1ee3f9bc9f1fe1ca285c34afdcea1acde77e619d426ba937c399230 | quote: A TUI-first CLI for managing Cloudflare Tunnels with custom domains. Think ngrok, but using your own Cloudflare domain with persistent URLs and a dashboard to manage them.
  - [2] 2026-11-19: the first-party README describes software the user installs and runs on a host the user supplies | capture: sha256:6f7717d2f1ee3f9bc9f1fe1ca285c34afdcea1acde77e619d426ba937c399230 | quote: You only need to install cloudflared. Do NOT run it as a system service. YTunnel manages cloudflared processes directly.
  - [2] 2026-11-19: the first-party README describes user-installed software driving the user's own Cloudflare domain, with no hosted endpoint | capture: sha256:6f7717d2f1ee3f9bc9f1fe1ca285c34afdcea1acde77e619d426ba937c399230 | quote: A TUI-first CLI for managing Cloudflare Tunnels with custom domains. Think ngrok, but using your own Cloudflare domain with persistent URLs and a dashboard to manage them.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/yetidevworks/ytunnel
