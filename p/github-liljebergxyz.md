# tnnlink

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-liljebergxyz/ | JSON https://fshy.ajam.dev/api/v1/entity/github-liljebergxyz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tnnlink

- `egress/tnnlink` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.296Z (live) | stale on 2026-12-20
- url https://github.com/LiljebergXYZ/tnnlink
- price USD 0
- free tier: SSH-based. Golang. Not maintained. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. SSH-based, unmaintained.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: SSH-based, unmaintained. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README describes the offer as a self-hosted ngrok alternative; no hosted endpoint is offered.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: SSH-based. Golang. Not maintained.
  - [2] 2026-11-19: the first-party project README labels tnnlink self-hosted software, with no hosted endpoint offered | capture: sha256:6591b6599ba63fcbe59af1328b8263280d0bab6650110325fb705e88246c0e12 | quote: Self-hosted ngrok alternative.
  - [2] 2026-11-19: the first-party README describes SSH tunneling the user runs, so egress begins with a host the user supplies | capture: sha256:6591b6599ba63fcbe59af1328b8263280d0bab6650110325fb705e88246c0e12 | quote: Simple HTTP tunneling using SSH, authorized using github public keys.
  - [2] 2026-11-19: the first-party README confirms tnnlink is self-hosted software | capture: sha256:6591b6599ba63fcbe59af1328b8263280d0bab6650110325fb705e88246c0e12 | quote: Self-hosted ngrok alternative.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/LiljebergXYZ/tnnlink
