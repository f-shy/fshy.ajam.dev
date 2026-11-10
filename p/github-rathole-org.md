# rathole

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-rathole-org/ | JSON https://fshy.ajam.dev/api/v1/entity/github-rathole-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rathole

- `egress/rathole` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/rathole-org/rathole
- price USD 0
- free tier: Similar to frp, including the config format, but with improved performance. Low resource consumption. Hot reload. Written in Rust. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. frp-shaped config; TCP only per the aggregator.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: frp-shaped config; TCP only per the aggregator. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Similar to frp, including the config format, but with improved performance. Low resource consumption. Hot reload. Written in Rust.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/rathole-org/rathole
