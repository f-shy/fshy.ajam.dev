# NPS Enhanced

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-djylb/ | JSON https://fshy.ajam.dev/api/v1/entity/github-djylb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NPS Enhanced

- `egress/nps-enhanced` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/djylb/nps
- price USD 0
- free tier: Self-hosted NAT traversal and reverse proxy with a Web UI, HTTP/HTTPS and TCP/UDP forwarding, and automatic certificate support. GPL-3.0 Licensed. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. HTTP/HTTPS and TCP/UDP forwarding in a self-hosted server.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: HTTP/HTTPS and TCP/UDP forwarding in a self-hosted server. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hosted NAT traversal and reverse proxy with a Web UI, HTTP/HTTPS and TCP/UDP forwarding, and automatic certificate support. GPL-3.0 Licensed. Written in Go
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/djylb/nps
