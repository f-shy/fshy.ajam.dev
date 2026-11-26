# NPS Enhanced

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-djylb/ | JSON https://fshy.ajam.dev/api/v1/entity/github-djylb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NPS Enhanced

- `egress/nps-enhanced` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.741Z (live) | stale on 2026-12-20
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
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: HTTP/HTTPS and TCP/UDP forwarding in a self-hosted server. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it documents a NAT traversal and reverse proxy server the user deploys via Docker or a Linux/Windows install, with no hosted endpoint or byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hosted NAT traversal and reverse proxy with a Web UI, HTTP/HTTPS and TCP/UDP forwarding, and automatic certificate support. GPL-3.0 Licensed. Written in Go
  - [2] 2026-11-19: the first-party README presents the tool as user-deployed NAT traversal software with no hosted endpoint | capture: sha256:67b8d86b0cdd6e1b60b6d30cd152c9cee8a2b36e17aabc65c4f39e76bc185903 | quote: NPS is a lightweight and efficient NAT traversal and reverse proxy system for exposing services behind NAT or firewalls.
  - [2] 2026-11-19: the first-party README documents Docker and Linux/Windows deployment the user performs | capture: sha256:67b8d86b0cdd6e1b60b6d30cd152c9cee8a2b36e17aabc65c4f39e76bc185903 | quote: NPS is a lightweight and efficient NAT traversal and reverse proxy system for exposing services behind NAT or firewalls.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:67b8d86b0cdd6e1b60b6d30cd152c9cee8a2b36e17aabc65c4f39e76bc185903 | quote: NPS is a lightweight and efficient NAT traversal and reverse proxy system for exposing services behind NAT or firewalls.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/djylb/nps
