# ngtor

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-theborakompanioni/ | JSON https://fshy.ajam.dev/api/v1/entity/github-theborakompanioni.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ngtor

- `egress/ngtor` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.740Z (live) | stale on 2026-12-20
- url https://github.com/theborakompanioni/ngtor
- price USD 0
- free tier: Easily expose local services via Tor. Written in Java. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Tor hidden services.
- interface detail: not established
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: Tor hidden services. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it documents a Java binary the user downloads and runs to serve local ports as Tor hidden services, with no hosted endpoint or byte allowance. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Easily expose local services via Tor. Written in Java.
  - [2] 2026-11-19: the first-party README presents the tool as software for exposing local services, with no hosted endpoint | capture: sha256:87d4ca021cd395888d1dda14abd0605c09a4c0d7eb37c0cc1ad1d17815cfc721 | quote: Easily expose local services via Tor
  - [2] 2026-11-19: the first-party README distributes a binary the user runs locally | capture: sha256:87d4ca021cd395888d1dda14abd0605c09a4c0d7eb37c0cc1ad1d17815cfc721 | quote: Easily expose local services via Tor
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:87d4ca021cd395888d1dda14abd0605c09a4c0d7eb37c0cc1ad1d17815cfc721 | quote: Easily expose local services via Tor
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/theborakompanioni/ngtor
