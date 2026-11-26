# chisel-operator

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-fyralabs/ | JSON https://fshy.ajam.dev/api/v1/entity/github-fyralabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## chisel-operator

- `egress/chisel-operator` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.878Z (live) | stale on 2026-12-20
- url https://github.com/FyraLabs/chisel-operator/
- price USD 0
- free tier: Kubernetes integration for Chisel. Similar functionality to inlets. MIT License. Written in Rust. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Kubernetes integration for Chisel.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Kubernetes integration for Chisel. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Kubernetes integration for Chisel. Similar functionality to inlets. MIT License. Written in Rust.
  - [2] 2026-11-19: the project README says an exit node must be a VPS or other machine supplied by the user; no hosted egress allowance is offered | capture: sha256:c9b799a05d8f91c72b5d982a263c178c60f720b0e2d048ac42a024b9229c0a2c | quote: Use a VPS (or any other machine) as a reverse proxy for your Kubernetes cluster, without paying the extra 25$ a month!
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/FyraLabs/chisel-operator/
