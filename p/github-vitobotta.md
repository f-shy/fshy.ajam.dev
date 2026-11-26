# docker-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-vitobotta/ | JSON https://fshy.ajam.dev/api/v1/entity/github-vitobotta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## docker-tunnel

- `egress/docker-tunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.879Z (live) | stale on 2026-12-20
- url https://github.com/vitobotta/docker-tunnel
- price USD 0
- free tier: Simple Docker-based nginx+SSH solution. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. nginx plus SSH.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: nginx plus SSH. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Simple Docker-based nginx+SSH solution.
  - [2] 2026-11-19: the project README labels the tool self-hosted and describes running the proxy on a host the user supplies; no hosted egress allowance is offered | capture: sha256:d900cdbb09e9a8873dbf226b2d7ade69c8759f3b5b87c71acb5f855ecec34abf | quote: This is a Docker-based, self hosted alternative to [Ngrok](https://ngrok.com/).
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/vitobotta/docker-tunnel
