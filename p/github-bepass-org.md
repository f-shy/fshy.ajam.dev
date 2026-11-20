# warp-plus

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-bepass-org/ | JSON https://fshy.ajam.dev/api/v1/entity/github-bepass-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## warp-plus

- `egress/warp-plus` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/bepass-org/warp-plus
- price USD 0
- free tier: no service and no account; "an open-source implementation of Cloudflare's Warp, enhanced with Psiphon integration" | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated by this tool; the traffic reaches Cloudflare WARP and Psiphon, neither of which it prices; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; WARP registration is created by the tool | country: None
- interface: cli
- binding note: the tool adds no quota of its own; the WARP record carries the allowance
- interface detail: warp-plus -b 127.0.0.1:8086
- tooling: single binary; SOCKS5 listener
- composes with: feeds a SOCKS5 consumer, so it composes with a proxy-aware client rather than with a router.
- reliability: SOCKS5 in, not a tunnel interface; behaviour depends on Cloudflare and Psiphon endpoints the tool does not control
- notes: Its unique feature is chaining WARP through Psiphon, which reaches a different exit than WARP alone. Maintenance is slower than wgcf: one release in the last 18 months.
- evidence note: a probe through the SOCKS5 listener would raise it
- self hosted: yes
- extras:
  - wg_path: registration-api
  - wg_detail: it registers its own WARP identity and exposes a local SOCKS5 listener (default 127.0.0.1:8086) rather than emitting a .conf
  - ingress: none
  - volume_stated: not stated by this tool; the traffic reaches Cloudflare WARP and Psiphon, neither of which it prices
  - bytes_transit: yes
  - transit_note: through Cloudflare WARP, optionally then Psiphon
  - hosting_requirement: none; runs on the device, exposes SOCKS5 only
  - last_release: v1.2.6 2025-06-04
  - stars: 1975
- evidence:
  - [1] 2026-10-23: the feature list: Warp integration, Psiphon chaining, warp-in-warp, SOCKS5 proxy
  - [1] 2026-10-23: the -b flag: "socks bind address (default: 127.0.0.1:8086)"; no .conf output
  - [1] 2026-10-23: release v1.2.6 published 2025-06-04; last push 2025-12-15; 1975 stars
- sources:
  - [1] https://github.com/bepass-org/warp-plus
