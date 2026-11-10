# holepunch

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-cypherpunkarmory/ | JSON https://fshy.ajam.dev/api/v1/entity/github-cypherpunkarmory.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## holepunch

- `egress/holepunch` | self-hosted, last resort | verdict dead | evidence reported | binding none | category tunnel software (self-hosted) | tier n/a
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:45:51.744Z (live) | stale on 2026-11-18
- url https://github.com/CypherpunkArmory/holepunch
- price USD 0
- free tier: Uses SSH for muxing. Domain has expired. AGP-3.0 Licensed. Written in Python. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the hosted API host api.holepunch.io does not resolve in DNS (checked 2026-11-03); the list entry records that the domain has expired
- notes: The aggregator records that the domain has expired. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: The aggregator records that the domain has expired. Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - bytes_transit: no
  - transit_note: none
- evidence:
  - [1] 2026-10-23: list entry sentence: Uses SSH for muxing. Domain has expired. AGP-3.0 Licensed. Written in Python.
  - probe:api.holepunch.io 2026-11-03: api.holepunch.io, the hosted API this code runs, does not resolve in DNS on 2026-11-03 | capture: sha256:38bf9afa49d550d12293fa1e7901c1e8931b07a88f1bc603e4b63bde46932133 | quote: "error": "dns"
  - [2] 2026-11-03: the repository is the code of a hosted API at api.holepunch.io, not a standalone tunnel offer | capture: sha256:c5151454493ea99594684ff41b068fa377b06228323a0bf065dc57bea7ca0e97 | quote: This is the code used to run [api.holepunch.io](https://api.holepunch.io/)
  - [1] 2026-11-03: the list entry for holepunch records that its domain has expired | capture: sha256:0b8d7e63a0b5f0d1c151e57df1a8c1833894a0a586959c99a78ac5e6d7c612ab | quote: Uses SSH for muxing. Domain has expired. AGP-3.0 Licensed. Written in Python.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/CypherpunkArmory/holepunch
