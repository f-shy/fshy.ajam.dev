# reverse-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-snsinfu/ | JSON https://fshy.ajam.dev/api/v1/entity/github-snsinfu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## reverse-tunnel

- `egress/reverse-tunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.955Z (live) | stale on 2026-12-20
- url https://github.com/snsinfu/reverse-tunnel
- price USD 0
- free tier: Support TCP and UDP tunnels. Has docker images. Supports Let's Encrypt. MIT License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. TCP and UDP tunnels, self-hosted.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: TCP and UDP tunnels, self-hosted. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Support TCP and UDP tunnels. Has docker images. Supports Let's Encrypt. MIT License. Written in Go.
  - [2] 2026-11-19: First-party README: the gateway server is built and run by the user; the project offers no hosted endpoint. | capture: sha256:5dc00ae745696b900dc2d0dba93f0a16fc58f050aecc0c85b37b6dc4f02ff52c | quote: To build your own ones, clone the repository and make:
  - [2] 2026-11-19: The user creates and runs the gateway server, so the egress host is supplied separately. | capture: sha256:5dc00ae745696b900dc2d0dba93f0a16fc58f050aecc0c85b37b6dc4f02ff52c | quote: Create a configuration file named `rtun-server.yml`:
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/snsinfu/reverse-tunnel
