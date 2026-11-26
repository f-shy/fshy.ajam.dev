# Punchmole

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-degola/ | JSON https://fshy.ajam.dev/api/v1/entity/github-degola.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Punchmole

- `egress/punchmole` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.643Z (live) | stale on 2026-12-20
- url https://github.com/Degola/punchmole/
- price USD 0
- free tier: Can be integrated directly into an existing Node.js project. Written in JavaScript. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Embedded Node.js tunnel.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Embedded Node.js tunnel. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub README read on 2026-11-19; it describes a tool with a locally run client and a server deployed by the user behind a reverse proxy, with no hosted egress allowance, so the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Can be integrated directly into an existing Node.js project. Written in JavaScript.
  - [2] 2026-11-19: the first-party README describes self-hosted tunnel software the user installs and runs, with no hosted egress allowance stated | capture: sha256:20853012f9b2ce855925e559488a75fa9697a10e4b696dfbc3818bfd0a4ff3d6 | quote: Punchmole is a simple tool to give your locally running HTTP(s) servers a public URL and is an easy to self-host alternative to `ngrok` and/or `tunnelmole`.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:20853012f9b2ce855925e559488a75fa9697a10e4b696dfbc3818bfd0a4ff3d6 | quote: Punchmole is a simple tool to give your locally running HTTP(s) servers a public URL and is an easy to self-host alternative to `ngrok` and/or `tunnelmole`.
  - [2] 2026-11-19: the first-party README describes self-hosted tunnel software with no hosted egress allowance | capture: sha256:20853012f9b2ce855925e559488a75fa9697a10e4b696dfbc3818bfd0a4ff3d6 | quote: Punchmole is a simple tool to give your locally running HTTP(s) servers a public URL and is an easy to self-host alternative to `ngrok` and/or `tunnelmole`.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/Degola/punchmole/
