# tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-koding/ | JSON https://fshy.ajam.dev/api/v1/entity/github-koding.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnel

- `egress/tunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.297Z (live) | stale on 2026-12-20
- url https://github.com/koding/tunnel
- price USD 0
- free tier: This one is a Golang library, not a program you can just run. However, it looks easy to use for creating custom solutions. Uses a single TCP socket, and for multiplexing. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README describes a server/client package the user hosts; no hosted endpoint is offered.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - bytes_transit: no
  - transit_note: none
- evidence:
  - [1] 2026-10-23: list entry sentence: This one is a Golang library, not a program you can just run. However, it looks easy to use for creating custom solutions. Uses a single TCP socket, and for mul
  - [2] 2026-11-19: the first-party project README describes a server/client package the user deploys, with no hosted endpoint offered | capture: sha256:f771a3ab950521702d9187aff9d64fa710fb6e31eddb8b897b807589fa6717b3 | quote: Tunnel is a server/client package that enables to proxy public connections to your local machine over a tunnel connection from the local machine to the public server.
  - [2] 2026-11-19: the first-party README has the user run the server and client, so egress begins with a host the user supplies | capture: sha256:f771a3ab950521702d9187aff9d64fa710fb6e31eddb8b897b807589fa6717b3 | quote: The tunnel package consists of two parts. The `server` and the `client`.
  - [2] 2026-11-19: the first-party README confirms a self-hosted server/client package | capture: sha256:f771a3ab950521702d9187aff9d64fa710fb6e31eddb8b897b807589fa6717b3 | quote: Tunnel is a server/client package that enables to proxy public connections to your local machine over a tunnel connection from the local machine to the public server.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/koding/tunnel
