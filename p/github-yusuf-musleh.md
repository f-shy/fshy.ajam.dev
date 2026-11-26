# mmar

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-yusuf-musleh/ | JSON https://fshy.ajam.dev/api/v1/entity/github-yusuf-musleh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mmar

- `egress/mmar` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.341Z (live) | stale on 2026-12-20
- url https://github.com/yusuf-musleh/mmar
- price USD 0
- free tier: A zero-dependency, self-hostable, cross-platform HTTP tunnel that exposes your localhost to the world on a public URL. AGPL-3.0 License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. HTTP tunnel.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: HTTP tunnel. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub README read on 2026-11-19; the tool is self-hosted software the user installs and runs. The README also advertises a free hosted tunnel at mmar.dev with a 10mb request-size limit and 5 tunnels per IP, so a small hosted egress allowance is published; the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: A zero-dependency, self-hostable, cross-platform HTTP tunnel that exposes your localhost to the world on a public URL. AGPL-3.0 License. Written in Go.
  - [2] 2026-11-19: the first-party README describes a self-hosted tunnel the user installs and runs, with no hosted egress the user can rely on | capture: sha256:9eade64f049ffc6bb9ee93e1e9794edcc1bb82203273fb1f114ee0d454585173 | quote: Self-host your own mmar server to have full control
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis and names a hosted tier | capture: sha256:9eade64f049ffc6bb9ee93e1e9794edcc1bb82203273fb1f114ee0d454585173 | quote: Self-host your own mmar server to have full control
  - [2] 2026-11-19: the first-party README describes self-hosted software the user installs and runs | capture: sha256:9eade64f049ffc6bb9ee93e1e9794edcc1bb82203273fb1f114ee0d454585173 | quote: Self-host your own mmar server to have full control
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/yusuf-musleh/mmar
