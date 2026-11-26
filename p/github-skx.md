# tunneller

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-skx/ | JSON https://fshy.ajam.dev/api/v1/entity/github-skx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunneller

- `egress/tunneller` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.706Z (live) | stale on 2026-12-20
- url https://github.com/skx/tunneller
- price USD 0
- free tier: Open source. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. SSH-based TCP.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: SSH-based TCP. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party README read; it states the project is a self-hosted alternative to ngrok, so the no-hosted-egress-allowance restriction holds.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Open source. Written in Go.
  - [2] 2026-11-19: the project is a self-hosted tunnel, so no hosted egress allowance exists | capture: sha256:981962c2604ea1027750f679a8367cfb502b27a63b5ff614f255edb562e02417 | quote: In short this project is designed to be a self-hosted alternative to software such as `ngrok`.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/skx/tunneller
