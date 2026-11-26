# mexashare

> mexashare.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mexashare/ | JSON https://fshy.ajam.dev/api/v1/entity/mexashare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mexashare

- `storage/mexashare` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mexashare.com/
- free tier: none reachable: Every provider in the read walk failed with dial-failed / 502; origin unreachable. Cannot verify limits. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Origin unreachable on 2026-11-19: GET https://www.mexashare.com/ returned HTTP 522 with retry-after 120, so no limits can be read.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Every provider in the read walk failed with dial-failed / 502; origin unreachable. Cannot verify limits.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Every provider in the read walk failed with dial-failed / 502; origin unreachable. Cannot verify limits.
  - probe:https://www.mexashare.com/ 2026-11-19: the host did not answer with content; an HTTP 522 was recorded on 2026-11-19 | capture: sha256:ba770b8bebcfdd4e08367507a42507c740691bc5b1e0c977c59f364596ea1efe | quote: "status": 522
  - probe:https://www.mexashare.com/ 2026-11-19: the host returned no content (HTTP 522, retry-after 120) on 2026-11-19 | capture: sha256:ba770b8bebcfdd4e08367507a42507c740691bc5b1e0c977c59f364596ea1efe | quote: "status": 522
- sources:
  - [1] https://www.mexashare.com/
