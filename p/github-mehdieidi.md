# tunelo

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mehdieidi/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mehdieidi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunelo

- `egress/tunelo` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/mehdieidi/tunelo
- price USD 0
- free tier: no service and no account; two Go programs built from source | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account required. Requires a Linux server with NAT rules and local deployment alongside a VPN endpoint. | country: None
- interface: cli
- binding note: the constraint is a Linux server with IP forwarding and MASQUERADE, outside the vocabulary
- interface detail: tunelo-server and tunelo-client
- tooling: go build; server needs iptables and ip_forward
- composes with: websocket mode rides the same class of forwarder as wstunnel; the server must sit on a host with a public address.
- reliability: client skips certificate verification in utls mode, stated in the README; last tagged build is from 2023
- notes: Open-source transport proxy using uTLS client hello shaping to bypass network inspection. Client and relay run as self-hosted components.
- evidence note: a measured run would raise it; the repository publishes no benchmark
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "tunelo encrypts and tunnels UDP traffic (e.g. WireGuard) over a transport protocol like websocket or TCP"; server/ and client/ are separate binaries, both defaulting to websocket
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - hosting_requirement: a Linux server with a public address, IP forwarding and a NAT rule, plus the client binary on the device
  - last_release: v0.4.0 2023-09-10
  - stars: 16
- evidence:
  - [1] 2026-10-23: the description sentence, the two-binary layout, and the server requirements (WireGuard, Go, NAT rules, IP forwarding)
  - [1] 2026-10-23: "The current client skips certificate verification" in utls mode
  - [1] 2026-10-23: release v0.4.0 published 2023-09-10; last push 2026-09-27; 16 stars
- sources:
  - [1] https://github.com/mehdieidi/tunelo
