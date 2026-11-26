# transfer.sh

> transfer.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfer-2/ | JSON https://fshy.ajam.dev/api/v1/entity/transfer-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## transfer.sh (the original)

- `storage/transfer-sh` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://transfer.sh/
- free tier: The brand is dead; only community… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: the same as the free tier
- notes: the same as the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The brand is dead; only community…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: The brand is dead; only community m
  - probe:https://transfer.sh/ 2026-11-19: a direct GET of transfer.sh returned no HTTP status: the proxy tunnel failed with 502 upstream unreachable on 2026-11-19 | capture: sha256:e19a4d0ef0a5a2b8f700b46ef8385e959644ef5ce08e23da7caf0be8decbd8cb | quote: "status": null
- sources:
  - [1] https://transfer.sh/
