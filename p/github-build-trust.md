# Portals for Mac

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-build-trust/ | JSON https://fshy.ajam.dev/api/v1/entity/github-build-trust.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Portals for Mac

- `egress/portals-for-mac` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-20T04:02:26.717Z (live) | stale on 2026-12-05
- url https://github.com/build-trust/ockam/blob/develop/examples/app/portals/README.md
- price USD 0
- free tier: A Mac app that uses the library to privately share a service on your Mac to anyone, anywhere. The service is shared securely over an end-to-end encrypted Ockam Portal. Apache 2.0 License. Written in Rust. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: unverified: the first-party README URL answered HTTP 404 on 2026-11-19; routes tried: a page read, a registered live probe, the raw-file URL, Wayback blob replay and raw snapshots; no first-party page was available to re-check the egress restriction
- notes: Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - bytes_transit: no
  - transit_note: none
- evidence:
  - [1] 2026-10-23: list entry sentence: A Mac app that uses the library to privately share a service on your Mac to anyone, anywhere. The service is shared securely over an end-to-end encrypted Ockam
  - probe:https://github.com/build-trust/ockam/blob/develop/examples/app/portals/README.md 2026-11-19: the first-party README URL answered HTTP 404 on 2026-11-19 | capture: sha256:06fbc6c31482e728771dbaba4274da92d4eb60129f27adf41ad6176f58af71d2 | quote: "status": 404
  - [2] 2026-11-20: a live 2026-11-20 probe of the first-party Ockam README URL answered HTTP 404 | capture: sha256:22c30861388209443d5c3d422b42a0a1da5386ecd8f7014684a0425946de1f42 | quote: "status": 404
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/build-trust/ockam/blob/develop/examples/app/portals/README.md
