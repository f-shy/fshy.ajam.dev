# bifrost

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-aperturerobotics/ | JSON https://fshy.ajam.dev/api/v1/entity/github-aperturerobotics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bifrost

- `egress/bifrost` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.398Z (live) | stale on 2026-12-20
- url https://github.com/aperturerobotics/bifrost
- price USD 0
- free tier: Bifrost is a peer-to-peer communications engine with pluggable transports. It supports dynamic configuration of transports, listeners, forwarding rules, and can tunnel other protocols over WebRTC and Quic. Apache 2.0 License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. P2P engine tunnelling over WebRTC and QUIC.
- interface detail: not established
- tooling: The user installs and runs the Spacewave application; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: P2P engine tunnelling over WebRTC and QUIC. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party repository read; the project now presents as Spacewave, self-hosted software with no servers; no hosted endpoint or allowance is published. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Bifrost is a peer-to-peer communications engine with pluggable transports. It supports dynamic configuration of transports, listeners, forwarding rules, and can
  - [2] 2026-11-19: the first-party repository now presents self-hosted software with no servers and no hosted endpoint | capture: sha256:44358314e77ba49a2d9607954df7c7e5663e8e875473a78b549c74a789c8d9ee | quote: Spacewave runs in your browser with no servers: a private, encrypted workspace running entirely on your own machine: no account, no setup, no server to run.
  - [2] 2026-11-19: the software runs on the user's own machine | capture: sha256:44358314e77ba49a2d9607954df7c7e5663e8e875473a78b549c74a789c8d9ee | quote: Spacewave runs in your browser with no servers: a private, encrypted workspace running entirely on your own machine: no account, no setup, no server to run.
  - [2] 2026-11-19: the first-party repository replaces the list sentence as the basis for the egress finding | capture: sha256:44358314e77ba49a2d9607954df7c7e5663e8e875473a78b549c74a789c8d9ee | quote: Spacewave runs in your browser with no servers: a private, encrypted workspace running entirely on your own machine: no account, no setup, no server to run.
  - [2] 2026-11-19: the software runs on the user's own machine and offers no hosted endpoint | capture: sha256:44358314e77ba49a2d9607954df7c7e5663e8e875473a78b549c74a789c8d9ee | quote: Spacewave runs in your browser with no servers: a private, encrypted workspace running entirely on your own machine: no account, no setup, no server to run.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/aperturerobotics/bifrost
