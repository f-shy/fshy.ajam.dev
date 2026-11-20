# instances.social

> fedidb.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fedidb/ | JSON https://fshy.ajam.dev/api/v1/entity/fedidb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## instances.social / fediverse.observer / fedidb.org — the three instance-ind

- `storage/instances-social-fediverse-observer-fedidb-org-the-three` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.634Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/fedidb.md
- free tier: none reachable: All three were unreachable at probe time, so the sweep had to be done host-by-host. instances.social requires a manually-issued OAuth token and its list API is gone; api.fediverse.observer… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party page states no per-object size cap | note: not applicable
- retention: stated-absent: the first-party page states no retention period for user bytes; the pages publish instance metadata
- egress: stated-absent: the first-party page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party page states no storage client interface on the instance-finder page or the FediDB metadata API
- tooling: not documented
- composes with: stated-absent: the first-party page states no way to chain byte storage with other services; the API serves instance metadata
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: All three were unreachable at probe time, so the sweep had to be done host-by-host. instances.social requires a manually-issued OAuth token and its list API is gone; api.fediverse.observer…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All three were unreachable at probe time, so the sweep had to be done host-by-host. instances.social requires a manually-issued OAuth token and its list API is gone; api.fediverse.observer…
  - [1] 2026-11-19: FediDB is live with a public API, so the blanket three-host dead grouping no longer holds for this host | capture: sha256:093e041c048f1dea2e6ca9876c5a774cad45d51ff1e882b4552b81de949c996c | quote: Every number on this site comes from the public API. No key, no signup.
  - [2] 2026-11-19: the instances.social first-party home page is an instance-finding tool, not a byte store | capture: sha256:948a381ee9efedaedbbf6613ec371636fb21e6f32f5d46fd3f06fe448ddde43a | quote: Let me help you choose an instance
  - [3] 2026-11-19: the FediDB first-party home page describes a free public API over fediverse server metadata | capture: sha256:3255a867204a3a93fb4c2dc30816e413371d9ad4528185782ece73e726931213 | quote: FediDB indexes 43,242 servers across 673 software projects, checks every one of them each day, and publishes all of it through a free public API.
  - [4] 2026-11-19: the FediDB first-party API docs describe a JSON API returning server entities | capture: sha256:98b1d27ebefce829855c8ff9142a5bba7398a3c866387a7bb145774b85b8a733 | quote: A single server, as returned by the server endpoints.
- sources:
  - [1] https://fedidb.org/
  - [2] https://instances.social/
  - [3] https://fedidb.com/
  - [4] https://fedidb.com/resources/api-docs
