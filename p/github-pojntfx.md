# weron

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-pojntfx/ | JSON https://fshy.ajam.dev/api/v1/entity/github-pojntfx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## weron

- `egress/weron` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.707Z (live) | stale on 2026-12-20
- url https://github.com/pojntfx/weron
- price USD 0
- free tier: Built on WebRTC. Can create Layer 2 and Layer 3 networks. NAT traversal via STUN and TURN. AGPL-3.0 license. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Layer 2/3 over WebRTC with STUN/TURN.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Layer 2/3 over WebRTC with STUN/TURN. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party README describes a hosted signaling server and states that hosting it yourself has benefits including lower latency and better privacy; no hosted egress allowance is published.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Built on WebRTC. Can create Layer 2 and Layer 3 networks. NAT traversal via STUN and TURN. AGPL-3.0 license. Written in Go.
  - [2] 2026-11-19: a hosted signaling server exists and self-hosting has benefits; no egress allowance is published | capture: sha256:43f2412e108c87ac95172f78fa1596c28c78cf09e20e96ffe5783a881c733877 | quote: to use the hosted signaling server at `wss://weron.up.railway.app/`, hosting it yourself has many benefits, such as lower latency and even better privacy.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/pojntfx/weron
