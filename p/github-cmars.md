# onionpipe

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-cmars/ | JSON https://fshy.ajam.dev/api/v1/entity/github-cmars.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## onionpipe

- `egress/onionpipe` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.741Z (live) | stale on 2026-12-20
- url https://github.com/cmars/onionpipe
- price USD 0
- free tier: Onion addresses for anything. `onionpipe` forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Tor hidden services for TCP ports.
- interface detail: not established
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: Tor hidden services for TCP ports. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it documents a local binary or container the user builds and runs to forward ports over Tor, with no hosted endpoint or byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Onion addresses for anything. `onionpipe` forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa. Written in Go.
  - [2] 2026-11-19: the first-party README presents the tool as software the user runs locally, with no hosted endpoint | capture: sha256:8e8205e0a565306af7191a1e1982418794b012db4001f46c211b6c7cf8aecf1b | quote: onionpipe forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa.
  - [2] 2026-11-19: the first-party README documents a binary the user builds or runs in a container | capture: sha256:8e8205e0a565306af7191a1e1982418794b012db4001f46c211b6c7cf8aecf1b | quote: onionpipe forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:8e8205e0a565306af7191a1e1982418794b012db4001f46c211b6c7cf8aecf1b | quote: onionpipe forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/cmars/onionpipe
