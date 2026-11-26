# BitBang

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-richlegrand/ | JSON https://fshy.ajam.dev/api/v1/entity/github-richlegrand.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BitBang

- `egress/bitbang` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.398Z (live) | stale on 2026-12-20
- url https://github.com/richlegrand/bitbang-cli
- price USD 0
- free tier: Turn your machine into a URL. Your computer and browser connect peer-to-peer over WebRTC. Whoever opens the link needs no account and nothing installed. Shell, file sharing, and HTTP/WebSocket proxy over a single URL. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. WebRTC P2P with an HTTP/WebSocket proxy.
- interface detail: not established
- tooling: The user installs and runs the bitbang binary; the bitba.ng server only introduces the two ends.
- reliability: the same as interface detail
- notes: WebRTC P2P with an HTTP/WebSocket proxy. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it states the connection is peer-to-peer, the bitba.ng server only introduces the two ends and steps aside, and forwarding reaches hosts the listener can reach; no hosted byte allowance is published.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Turn your machine into a URL. Your computer and browser connect peer-to-peer over WebRTC. Whoever opens the link needs no account and nothing installed. Shell,
  - [2] 2026-11-19: the hosted server only introduces the two ends and carries no user bytes, so no hosted byte allowance is published | capture: sha256:5a4556f7ace0c0d93b841700d26425ad286939d9511011e4b8084af7d1f73fa9 | quote: The connection is end-to-end encrypted and peer-to-peer; the bitba.ng server introduces the two ends, then steps aside.
  - [2] 2026-11-19: the user installs and runs the binary while the server only introduces the ends | capture: sha256:5a4556f7ace0c0d93b841700d26425ad286939d9511011e4b8084af7d1f73fa9 | quote: The connection is end-to-end encrypted and peer-to-peer; the bitba.ng server introduces the two ends, then steps aside.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:5a4556f7ace0c0d93b841700d26425ad286939d9511011e4b8084af7d1f73fa9 | quote: The connection is end-to-end encrypted and peer-to-peer; the bitba.ng server introduces the two ends, then steps aside.
  - [2] 2026-11-19: the server carries no user bytes and the binary is installed and run by the user | capture: sha256:5a4556f7ace0c0d93b841700d26425ad286939d9511011e4b8084af7d1f73fa9 | quote: The connection is end-to-end encrypted and peer-to-peer; the bitba.ng server introduces the two ends, then steps aside.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/richlegrand/bitbang-cli
