# Hysteria

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-apernet/ | JSON https://fshy.ajam.dev/api/v1/entity/github-apernet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hysteria

- `egress/hysteria` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.939Z (live) | stale on 2026-12-20
- url https://github.com/apernet/hysteria
- price USD 0
- free tier: QUIC-based censorship-resistant proxy and relay (SOCKS5/HTTP, TCP/UDP forwarding, TUN/TProxy) with NAT traversal for hosting the server behind NAT (Realms). MIT License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. QUIC proxy with TCP/UDP forwarding and TUN; egress proxy, not ingress.
- interface detail: not established
- tooling: The user builds and runs the Hysteria server and client on a host the user supplies; no hosted endpoint is published.
- reliability: the same as interface detail
- notes: QUIC proxy with TCP/UDP forwarding and TUN; egress proxy, not ingress. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read on 2026-11-19; it describes a QUIC proxy with SOCKS5, HTTP, TCP/UDP forwarding and TUN that the user deploys, with no hosted endpoint or published byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: QUIC-based censorship-resistant proxy and relay (SOCKS5/HTTP, TCP/UDP forwarding, TUN/TProxy) with NAT traversal for hosting the server behind NAT (Realms). MIT
  - [2] 2026-11-19: the first-party README describes user-deployed software with no hosted endpoint or byte allowance | capture: sha256:2b6521b41c6067bd338c47fd490387ad6d68c8ed6d650429d804df5b42c703bc | quote: We have builds for every major platform and architecture. Deploy anywhere & use everywhere.
  - [2] 2026-11-19: the first-party README says the user deploys the software | capture: sha256:2b6521b41c6067bd338c47fd490387ad6d68c8ed6d650429d804df5b42c703bc | quote: We have builds for every major platform and architecture. Deploy anywhere & use everywhere.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis | capture: sha256:2b6521b41c6067bd338c47fd490387ad6d68c8ed6d650429d804df5b42c703bc | quote: Hysteria is a powerful, lightning-fast, and censorship-resistant proxy.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/apernet/hysteria
