# wgcf

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-virb3/ | JSON https://fshy.ajam.dev/api/v1/entity/github-virb3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wgcf

- `egress/wgcf` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/ViRb3/wgcf
- price USD 0
- free tier: no service and no account; a CLI that registers with Cloudflare and writes a profile | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated by this tool; the profile reaches Cloudflare WARP, whose allowance is recorded at egress/cloudflare-warp as no published cap; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account and no card; "wgcf register" creates the Cloudflare device registration from the CLI | country: None
- interface: cli
- binding note: the tool adds no limit; the limit that matters is whatever WARP applies, and its record carries none published
- interface detail: wgcf register / generate / status / trace
- tooling: single static binary; outputs a wg-quick profile
- composes with: generates the .conf that cloudflare-warp's record describes, and the profile can then be fed to a router, gluetun, or a kernel interface.
- reliability: usque reports that WARP+ over WireGuard stopped working for some accounts (wgcf issue 459); the generated MTU of 1280 is conservative and can be raised
- notes: Cross-platform CLI tool generating standard WireGuard configuration files for Cloudflare WARP. Output .conf files run on standard WireGuard clients, requiring outbound UDP access to Cloudflare endpoints.
- evidence note: a probe that brings the generated profile up and moves bytes would raise it to measured
- self hosted: yes
- extras:
  - wg_path: registration-api
  - wg_detail: "wgcf register" saves wgcf-account.toml and "wgcf generate" writes wgcf-profile.conf, which is a standard WireGuard profile with MTU 1280
  - ingress: none
  - volume_stated: not stated by this tool; the profile reaches Cloudflare WARP, whose allowance is recorded at egress/cloudflare-warp as no published cap
  - bytes_transit: yes
  - transit_note: traffic exits through Cloudflare's network once the profile is up
  - hosting_requirement: none; runs on the device and emits a .conf
  - last_release: v2.3.1 2026-10-11
  - stars: 8826
- evidence:
  - [1] 2026-10-23: the register / generate / license-key feature list and the wgcf-profile.conf output
  - [1] 2026-10-23: "To ensure maximum compatibility, the generated profile will have a MTU of 1280" and --keepalive adds PersistentKeepalive
  - [1] 2026-10-23: release v2.3.1 published 2026-10-11; last push 2026-10-20; 8826 stars
  - [1] 2026-10-23: the Warp+ binding is capped: "there is a limit of 5 maximum devices linked at a time"
- sources:
  - [1] https://github.com/ViRb3/wgcf
