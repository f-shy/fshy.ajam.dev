# ephemeral-hidden-service

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-aurelg/ | JSON https://fshy.ajam.dev/api/v1/entity/github-aurelg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ephemeral-hidden-service

- `egress/ephemeral-hidden-service` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.217Z (live) | stale on 2026-12-20
- url https://github.com/aurelg/ephemeral-hidden-service
- price USD 0
- free tier: Create ephemeral Tor hidden services from the command line. Written in Python. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Tor hidden services.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Tor hidden services. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Create ephemeral Tor hidden services from the command line. Written in Python.
  - [2] 2026-11-19: the project README requires the user to install and run Tor locally, so the tool runs on a user-supplied machine; no hosted egress allowance is offered | capture: sha256:c1f8574aeb92d55bde83aa8891415003d555707fe7c8695abb25bac9ad181019 | quote: Tor must be installed and running on your machine. Its controller port must be accessible.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/aurelg/ephemeral-hidden-service
