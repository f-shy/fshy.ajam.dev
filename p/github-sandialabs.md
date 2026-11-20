# Wiretap

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-sandialabs/ | JSON https://fshy.ajam.dev/api/v1/entity/github-sandialabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wiretap

- `egress/wiretap` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.707Z (live) | stale on 2026-12-20
- url https://github.com/sandialabs/wiretap
- price USD 0
- free tier: Transparent tunneling over WireGuard (UDP) using userspace network stack. Root not required on server. Supports multiple clients and servers. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Transparent tunnelling over WireGuard (UDP) with a userspace stack.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Transparent tunnelling over WireGuard (UDP) with a userspace stack. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party README states the exit node is any machine running the Wiretap binary and relaying traffic for clients; no hosted egress allowance is offered.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Transparent tunneling over WireGuard (UDP) using userspace network stack. Root not required on server. Supports multiple clients and servers. Written in Go.
  - [2] 2026-11-19: the exit node is a user-run Wiretap binary; no hosted egress allowance is offered | capture: sha256:a1c5f0edcd2ce3a551f0909de972048b3140f66820b2e668d9a5211ce3053a5b | quote: A Wiretap Server is any machine where a Wiretap binary is running the `serve` command. Servers receive and relay network traffic on behalf of Wiretap Clients, acting like a VPN "exit node."
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/sandialabs/wiretap
