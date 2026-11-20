# jkuri/bore

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jkuri/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jkuri.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## jkuri/bore

- `egress/jkuri-bore` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.939Z (live) | stale on 2026-12-20
- url https://github.com/jkuri/bore
- price USD 0
- free tier: Reverse HTTP/TCP proxy via SSH. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: A hosted bore.digital relay exists but publishes no byte allowance; no free hosted allowance reaches the volume bar. Reverse HTTP/TCP proxy via SSH; the user compiles the software and can run a private bore-server.
- interface detail: not established
- tooling: The user compiles and runs the bore client locally and can connect to the hosted bore.digital relay or run a private bore-server; no byte allowance is published.
- reliability: the same as interface detail
- notes: Reverse HTTP/TCP proxy via SSH. The first-party README was read on 2026-11-19; it documents a hosted bore.digital relay with no published byte allowance and a self-hosted bore-server option.
- evidence note: First-party project README read on 2026-11-19; it documents a hosted bore.digital relay with no published byte allowance and a self-hosted server. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Reverse HTTP/TCP proxy via SSH. Written in Go.
  - [2] 2026-11-19: the first-party README documents a hosted bore.digital server with no published byte allowance | capture: sha256:434fe517908081cf411c9ed29c31c25cb14c4f745ea6498c4616e8a1e715bfbb | quote: Note that for hosted bore you need to specify port in range 55000-65000.
  - [2] 2026-11-19: the first-party README describes a locally compiled client and a hosted or self-hosted server | capture: sha256:434fe517908081cf411c9ed29c31c25cb14c4f745ea6498c4616e8a1e715bfbb | quote: This will compile and install `bore` client locally.
  - [2] 2026-11-19: the hosted relay exists but publishes no byte allowance | capture: sha256:434fe517908081cf411c9ed29c31c25cb14c4f745ea6498c4616e8a1e715bfbb | quote: Note that for hosted bore you need to specify port in range 55000-65000.
  - [2] 2026-11-19: the first-party README establishes the hosted relay and self-host option | capture: sha256:434fe517908081cf411c9ed29c31c25cb14c4f745ea6498c4616e8a1e715bfbb | quote: Reverse HTTP/TCP proxy tunnel via secure SSH connections.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis | capture: sha256:434fe517908081cf411c9ed29c31c25cb14c4f745ea6498c4616e8a1e715bfbb | quote: Note that for hosted bore you need to specify port in range 55000-65000.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/jkuri/bore
