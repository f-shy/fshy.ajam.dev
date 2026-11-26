# sish

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-antoniomika/ | JSON https://fshy.ajam.dev/api/v1/entity/github-antoniomika.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sish

- `egress/sish` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-11-20
- url https://github.com/antoniomika/sish
- price USD 0
- free tier: Open source ngrok/serveo alternative. SSH-based but uses a custom server written in Go. Supports WebSocket tunneling. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. SSH remote forwarding, HTTP and WebSocket.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the hosted ssi.sh requires password auth or a pre-registered key on ports 22 and 2222, because the authless demo was disabled 'due to abuse'; the authless path exists only self-hosted.
- notes: SSH remote forwarding, HTTP and WebSocket. Classified from the aggregator's own sentence; no vendor page was fetched for this name. The hosted ssi.sh refuses anonymous users on ports 22 and 2222, so the authless path is self-hosted only (measured 2026-11-05).
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Open source ngrok/serveo alternative. SSH-based but uses a custom server written in Go. Supports WebSocket tunneling.
  - probe:ssi.sh:22 2026-11-05: the hosted demo requires password auth or a pre-registered key because the authless demo was disabled | capture: sha256:04dbd5acc3aa861bfa07a37171a2f92f873d470b8e48732f5f6e3d5ae81f0396 | quote: due to abuse
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/antoniomika/sish
