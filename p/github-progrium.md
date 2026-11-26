# progrium/localtunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-progrium/ | JSON https://fshy.ajam.dev/api/v1/entity/github-progrium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## progrium/localtunnel

- `egress/progrium-localtunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.642Z (live) | stale on 2026-12-20
- url https://github.com/progrium/localtunnel
- price USD 0
- free tier: Open-source local tunnel software under MIT License, written in Go. No hosted service is provided. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Unmaintained HTTP tunnel.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Unmaintained HTTP tunnel. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub README read on 2026-11-19; it states there is no public server and that a Go toolchain is needed to build it, so no hosted egress allowance exists and the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: No longer maintained, but here for posterity. MIT License.
  - [2] 2026-11-19: the first-party README states there is no public server, so no hosted egress allowance exists | capture: sha256:9c068e5a60ccbf5712a37e61ed38da47dbec5f51ebc9f15ed17b1c94261fd464 | quote: Although usable, there is no public server and the scope of the project is pretty fixed where it is.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:9c068e5a60ccbf5712a37e61ed38da47dbec5f51ebc9f15ed17b1c94261fd464 | quote: Although usable, there is no public server and the scope of the project is pretty fixed where it is.
  - [2] 2026-11-19: the first-party README states there is no public server, so no hosted egress | capture: sha256:9c068e5a60ccbf5712a37e61ed38da47dbec5f51ebc9f15ed17b1c94261fd464 | quote: Although usable, there is no public server and the scope of the project is pretty fixed where it is.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/progrium/localtunnel
