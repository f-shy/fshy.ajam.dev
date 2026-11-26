# expose

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-exposedev/ | JSON https://fshy.ajam.dev/api/v1/entity/github-exposedev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## expose

- `egress/expose-php` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.217Z (live) | stale on 2026-12-20
- url https://github.com/exposedev/expose
- price USD 0
- free tier: ngrok alternative written in PHP. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. PHP ngrok alternative, HTTP.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: PHP ngrok alternative, HTTP. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: ngrok alternative written in PHP.
  - [3] 2026-11-19: the official product page states the managed Expose service carries no UDP, so the fails-egress verdict still holds | capture: sha256:ff6fa85704b3675c18e158201dd68cee075389af4b126c485f121eaa99592536 | quote: Expose doesn't tunnel UDP, so it can't host a game server or a WireGuard endpoint.
  - [2] 2026-11-19: the first-party repository README now advertises a managed hosted tier and a free EU test server | capture: sha256:73df19b340c16060ce00de8cd3e54c16c54bbae0094a34e5be5983e74f047e2d | quote: You can use a managed version with our proprietary platform and our free (EU) test server at the official website.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/exposedev/expose
  - [3] https://expose.dev
