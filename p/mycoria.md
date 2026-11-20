# Mycoria

> mycoria.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mycoria/ | JSON https://fshy.ajam.dev/api/v1/entity/mycoria.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mycoria

- `egress/mycoria` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category ipv6 overlay software (self-hosted routers) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.342Z (live) | stale on 2026-12-20
- url https://mycoria.org/
- price USD 0
- free tier: Mycoria is an open and secure overlay network that connects all participants. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance or hosted relay is published.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: the IPv6 address is the key; no account is described. | country: None
- interface: cli
- binding note: Software only: joining the overlay requires a host running the daemon, and the address is not a public ingress for anyone outside the overlay.
- interface detail: part of binding note
- tooling: mycoria daemon.
- reliability: Self-operated routers.
- notes: Classified from the landing page; no hosted capacity.
- evidence note: First-party site read on 2026-11-19; it describes an open overlay network with self-operated routers and no hosted relay or byte allowance, so the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance or hosted relay is published.
  - bytes_transit: overlay-only
  - transit_note: peer routers
- evidence:
  - [1] 2026-10-23: 'open and secure overlay network that connects all participants'
  - [1] 2026-11-19: the first-party site describes an overlay network of self-operated routers with no hosted relay or published allowance | capture: sha256:59f95b3affd39b6c3a41926235192c832a94844f7ef6dd2cfdb1136fc6901e09 | quote: Mycoria is an open and secure overlay network that connects all participants.
  - [1] 2026-11-19: the first-party site replaces the list sentence as the basis for the egress finding | capture: sha256:59f95b3affd39b6c3a41926235192c832a94844f7ef6dd2cfdb1136fc6901e09 | quote: Mycoria is an open and secure overlay network that connects all participants.
  - [1] 2026-11-19: the first-party site describes overlay software with no hosted relay | capture: sha256:59f95b3affd39b6c3a41926235192c832a94844f7ef6dd2cfdb1136fc6901e09 | quote: Mycoria is an open and secure overlay network that connects all participants.
- sources:
  - [1] https://mycoria.org/
