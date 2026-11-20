# cactus-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jeffreytse/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jeffreytse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cactus-tunnel

- `egress/cactus-tunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.399Z (live) | stale on 2026-12-20
- url https://github.com/jeffreytse/cactus-tunnel
- price USD 0
- free tier: A charming TCP tunnel over WebSocket and Browser. Written in TypeScript. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. TCP over WebSocket.
- interface detail: not established
- tooling: The user installs and runs the cactus-tunnel package and a tunnel server; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: TCP over WebSocket. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it documents a tunnel server the user supplies (default 7800) and a client pointed at that server URL; no hosted endpoint or allowance is published.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: A charming TCP tunnel over WebSocket and Browser. Written in TypeScript.
  - [2] 2026-11-19:  | capture: sha256:1bc8fdefaff477f302cf95e4e7397451a7d1d2b4b9011a50a44dbdd794a9184c | quote: tunnel server url, empty is bridge mode, e.g. ws://your-tunnel-server:7800
  - [2] 2026-11-19: the user installs the package and runs the server and client | capture: sha256:1bc8fdefaff477f302cf95e4e7397451a7d1d2b4b9011a50a44dbdd794a9184c | quote: npm install -g cactus-tunnel
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:1bc8fdefaff477f302cf95e4e7397451a7d1d2b4b9011a50a44dbdd794a9184c | quote: tunnel server url, empty is bridge mode, e.g. ws://your-tunnel-server:7800
  - [2] 2026-11-19: the user supplies the tunnel server, so there is no hosted endpoint | capture: sha256:1bc8fdefaff477f302cf95e4e7397451a7d1d2b4b9011a50a44dbdd794a9184c | quote: tunnel server url, empty is bridge mode, e.g. ws://your-tunnel-server:7800
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/jeffreytse/cactus-tunnel
