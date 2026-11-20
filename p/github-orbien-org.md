# Orbien

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-orbien-org/ | JSON https://fshy.ajam.dev/api/v1/entity/github-orbien-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Orbien

- `egress/orbien` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.144Z (live) | stale on 2026-12-20
- url https://github.com/orbien-org/orbien
- price USD 0
- free tier: Lightweight alternative to frp. Supports hot reload. Low resource consumption. Supports TCP (with multiplexing), WebSocket, QUIC and KCP transports, built-in server Web admin UI and native desktop client. Written in Rust. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: the first-party README describes a reverse proxy with TCP, UDP, HTTP, HTTPS, SOCKS5, KCP, WebSocket and QUIC transports that the user runs on a host the user supplies; no hosted endpoint or allowance is offered.
- interface detail: not established
- tooling: The user installs and runs the orbien server and client binaries on a host the user supplies.
- reliability: the same as interface detail
- notes: TCP with muxing, WebSocket, QUIC and KCP transports. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes a user-installed reverse proxy with no hosted endpoint and no byte allowance. The first-party source supersedes the aggregator list sentence as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Lightweight alternative to frp. Supports hot reload. Low resource consumption. Supports TCP (with multiplexing), WebSocket, QUIC and KCP transports, built-in se
  - [2] 2026-11-19: the first-party README presents a reverse proxy the user runs, with no hosted endpoint or published byte allowance | capture: sha256:e0b970f5bf9d7ff877e3b265a2fc2f8a4c1a7d7222e2dd30eb34d054e8006c79 | quote: Securely expose local services behind a firewall to the public internet.
  - [2] 2026-11-19: the first-party README gives download and run steps for user-installed binaries | capture: sha256:e0b970f5bf9d7ff877e3b265a2fc2f8a4c1a7d7222e2dd30eb34d054e8006c79 | quote: Download the binary archive for your platform and extract it.
  - [2] 2026-11-19: the first-party README lists tunnel protocols and presents user-run software | capture: sha256:e0b970f5bf9d7ff877e3b265a2fc2f8a4c1a7d7222e2dd30eb34d054e8006c79 | quote: Tunnel protocols: TCP, UDP, HTTP, HTTPS,SOCKS5 and more
  - [2] 2026-11-19: the first-party README is the basis for the egress finding | capture: sha256:e0b970f5bf9d7ff877e3b265a2fc2f8a4c1a7d7222e2dd30eb34d054e8006c79 | quote: Securely expose local services behind a firewall to the public internet.
  - [2] 2026-11-19: the first-party README describes user-run reverse-proxy software with no hosted endpoint | capture: sha256:e0b970f5bf9d7ff877e3b265a2fc2f8a4c1a7d7222e2dd30eb34d054e8006c79 | quote: Securely expose local services behind a firewall to the public internet.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/orbien-org/orbien
