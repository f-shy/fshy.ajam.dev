# dspace.org/instances

> dspace.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dspace/ | JSON https://fshy.ajam.dev/api/v1/entity/dspace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dspace.org/instances

- `storage/dspace-org-instances` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:44.043Z (live) | stale on 2026-12-04
- url https://dspace.org/instances
- free tier: none reachable: The old /instances path is no longer the live registry; the active registry at dspace.org/registry/ lists 3,496 entries on 2026-11-19. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Old registry URL returned HTTP 404. The active registry is located at dspace.org/registry/ with 3,485 directory entries.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: 404 — the registry moved. The live registry is dspace.org/registry/ (3,485 entries, 35 pages).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 404 — the registry moved. The live registry is dspace.org/registry/ (3,485 entries, 35 pages).
  - [2] 2026-10-21: cited as the basis of the rejection: 404 — the registry moved. The live registry is dspace.org/registry/ (3,485 entries, 35 pages).
  - [2] 2026-11-19: the live DSpace registry lists 3,496 entries on 2026-11-19 | capture: sha256:bcbae21e5c978934f94fde0bcd508252ad4930971598f229551d16b8f1118fd1 | quote: Displaying 1 - 100 of 3,496
  - probe:https://dspace.org/instances 2026-11-19: the old /instances path answered HTTP 403 on 2026-11-19 | capture: sha256:a3208be40e8b2f2032e60bcd50a11501c690ff5da5272f8a08a2c7527ad5cd39 | quote: "status": 403
- sources:
  - [1] https://dspace.org/instances
  - [2] https://dspace.org/registry/
