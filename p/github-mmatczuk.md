# go-http-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mmatczuk/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mmatczuk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## go-http-tunnel

- `egress/go-http-tunnel` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.567Z (live) | stale on 2026-12-20
- url https://github.com/mmatczuk/go-http-tunnel
- price USD 0
- free tier: Uses a single HTTP/2 connection for muxing. Need to manually generate certs for server and clients. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. HTTP/2 muxing.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: HTTP/2 muxing. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Uses a single HTTP/2 connection for muxing. Need to manually generate certs for server and clients.
  - [2] 2026-11-19: the project README says the tunnel server runs on a publicly available host the user supplies; no hosted egress allowance is offered | capture: sha256:e8daab2e31ba67a0678d9e2650fe0aa8656c523fdaceb04b18442eefc21b08d5 | quote: - `tunneld` - the tunnel server, to be run on publicly available host like AWS or GCE
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/mmatczuk/go-http-tunnel
