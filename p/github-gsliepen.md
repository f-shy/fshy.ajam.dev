# Tinc

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-gsliepen/ | JSON https://fshy.ajam.dev/api/v1/entity/github-gsliepen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tinc

- `egress/tinc` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.296Z (live) | stale on 2026-12-20
- url https://github.com/gsliepen/tinc
- price USD 0
- free tier: Tinc is a peer-to-peer VPN daemon that supports VPNs with an arbitrary number of nodes. Instead of configuring tunnels, you give Tinc the location and public key of a few nodes in the VPN. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Peer-to-peer VPN daemon; needs nodes.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Peer-to-peer VPN daemon; needs nodes. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README confirms a peer-to-peer VPN daemon distributed for self-hosting; no hosted endpoint is offered.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Tinc is a peer-to-peer VPN daemon that supports VPNs with an arbitrary number of nodes. Instead of configuring tunnels, you give Tinc the location and public ke
  - [2] 2026-11-19: the first-party project README describes a peer-to-peer VPN daemon the user runs as nodes, with no hosted endpoint offered | capture: sha256:a16c0e3dd0db45c4de2605a0438f27f67579fb84c0685910171eaa39fdec422d | quote: Tinc is a peer-to-peer VPN daemon that supports VPNs with an arbitrary number of nodes.
  - [2] 2026-11-19: the first-party README has the user supply the VPN nodes, so egress begins with a host the user runs | capture: sha256:a16c0e3dd0db45c4de2605a0438f27f67579fb84c0685910171eaa39fdec422d | quote: Instead of configuring tunnels, you give tinc the location and public key of a few nodes in the VPN.
  - [2] 2026-11-19: the first-party README confirms a self-hosted peer-to-peer VPN daemon | capture: sha256:a16c0e3dd0db45c4de2605a0438f27f67579fb84c0685910171eaa39fdec422d | quote: Tinc is a peer-to-peer VPN daemon that supports VPNs with an arbitrary number of nodes.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/gsliepen/tinc
