# iodine

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-yarrick/ | JSON https://fshy.ajam.dev/api/v1/entity/github-yarrick.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iodine

- `egress/iodine` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.939Z (live) | stale on 2026-12-20
- url https://github.com/yarrick/iodine
- price USD 0
- free tier: Tunnel IPv4 over DNS to reach the internet through restrictive networks where only DNS queries are permitted. ISC License. Written in C. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. IPv4 over DNS; needs a server and a domain.
- interface detail: not established
- tooling: The user compiles and runs iodined on a public-IP server and controls a domain; no hosted endpoint is published.
- reliability: the same as interface detail
- notes: IPv4 over DNS; needs a server and a domain. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read on 2026-11-19; it requires a user-controlled domain and a public-IP server running iodined, and publishes no hosted endpoint or byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Tunnel IPv4 over DNS to reach the internet through restrictive networks where only DNS queries are permitted. ISC License. Written in C.
  - [2] 2026-11-19: the first-party README requires the user to supply a domain and a public-IP server, with no hosted endpoint or byte allowance | capture: sha256:09297427043bcf3ef103e570000ac5737d275b0ed1b84ef398135cfce894a25f | quote: To use this tunnel, you need control over a real domain (like `mydomain.com`), and a server with a public IP address to run `iodined` on.
  - [2] 2026-11-19: the first-party README requires a user-supplied domain and server | capture: sha256:09297427043bcf3ef103e570000ac5737d275b0ed1b84ef398135cfce894a25f | quote: To use this tunnel, you need control over a real domain (like `mydomain.com`), and a server with a public IP address to run `iodined` on.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis | capture: sha256:09297427043bcf3ef103e570000ac5737d275b0ed1b84ef398135cfce894a25f | quote: This is a piece of software that lets you tunnel IPv4 data through a DNS server.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/yarrick/iodine
