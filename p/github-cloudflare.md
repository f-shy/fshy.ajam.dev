# boringtun

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-cloudflare/ | JSON https://fshy.ajam.dev/api/v1/entity/github-cloudflare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boringtun

- `egress/boringtun` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/cloudflare/boringtun
- price USD 0
- free tier: no service and no account; a Rust library and the boringtun-cli binary | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: boringtun adds no path of its own: it encrypts and decapsulates over UDP exactly as the protocol specifies, so a UDP block stops it
- interface detail: boringtun-cli, cargo, crates.io
- tooling: cargo install boringtun-cli; Rust library for embedding
- composes with: sits under a WARP client or under a wrapper; it composes with cloudflare-warp and adds nothing to a hosted tunnel by itself.
- reliability: README warns the master branch is mid-restructure; use the crates.io releases
- notes: Userspace WireGuard implementation in Rust. Operates as a protocol implementation and network interface, not as a transport encapsulation proxy or hosted service. Used in Cloudflare WARP client software.
- evidence note: the verdict is about egress, not quality: boringtun is load-bearing inside the official Cloudflare WARP apps, and is the substrate a wrapper needs
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: boringtun-cli is a userspace WireGuard executable that takes the standard interface configuration, so a normal .conf drives it
  - ingress: none
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: carries a user's own traffic to whatever peer it is configured against
  - hosting_requirement: none beyond the device, but no far end either: it needs a WireGuard peer and speaks only UDP to it
  - last_release: boringtun-cli-0.5.2 2022-07-20
  - stars: 7230
- evidence:
  - [1] 2026-10-23: "an implementation of the WireGuard protocol designed for portability and speed", deployed on millions of iOS and Android consumer devices
  - [1] 2026-10-23: "It implements the underlying WireGuard protocol, without the network or tunnel stacks" - the library half does no I/O at all
  - [1] 2026-10-23: release boringtun-cli-0.5.2 published 2022-07-20; last push 2026-06-29; 7230 stars
  - [1] 2026-10-23: "Boringtun is currently undergoing a restructuring. You should probably not rely on or link to the master branch right now"
- sources:
  - [1] https://github.com/cloudflare/boringtun
