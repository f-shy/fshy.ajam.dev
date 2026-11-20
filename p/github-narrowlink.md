# Narrowlink

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-narrowlink/ | JSON https://fshy.ajam.dev/api/v1/entity/github-narrowlink.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Narrowlink

- `egress/narrowlink` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.342Z (live) | stale on 2026-12-20
- url https://github.com/narrowlink/narrowlink
- price USD 0
- free tier: Self-hosted zero-trust remote access platform with gateway, agent, and client components, P2P QUIC, fine-grained access control, and automatic ACME certificates when publishing local webservers. MPL-2.0/AGPL-3.0. Written in Rust. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Self-hosted zero-trust access with ACME for published web servers.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Self-hosted zero-trust access with ACME for published web servers. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub README read on 2026-11-19; it describes a self-hosted remote-access platform the user installs and runs, with no hosted endpoint or byte allowance, so the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hosted zero-trust remote access platform with gateway, agent, and client components, P2P QUIC, fine-grained access control, and automatic ACME certificates
  - [2] 2026-11-19: the first-party README describes self-hosted software the user installs and runs, with no hosted endpoint or byte allowance | capture: sha256:45ae9b467bbeff650dff4e3a90d13b27e5754716f5fcdc3013d1de4a24a0ef65 | quote: Narrowlink is a self-hosted platform that allows you to establish secure remote connections between devices within a network that may be hindered by network address translation (NAT) or firewalls.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:45ae9b467bbeff650dff4e3a90d13b27e5754716f5fcdc3013d1de4a24a0ef65 | quote: Narrowlink is a self-hosted platform that allows you to establish secure remote connections between devices within a network that may be hindered by network address translation (NAT) or firewalls.
  - [2] 2026-11-19: the first-party README describes self-hosted software with no hosted endpoint | capture: sha256:45ae9b467bbeff650dff4e3a90d13b27e5754716f5fcdc3013d1de4a24a0ef65 | quote: Narrowlink is a self-hosted platform that allows you to establish secure remote connections between devices within a network that may be hindered by network address translation (NAT) or firewalls.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/narrowlink/narrowlink
