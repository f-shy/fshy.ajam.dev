# dans data

> knaw.nl | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/knaw/ | JSON https://fshy.ajam.dev/api/v1/entity/knaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dans data stations (knaw, netherlands) / dataversenl

- `storage/dans-data-stations-dataversenl` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dans.knaw.nl/en/deposit/
- free tier: none reachable: Both sit behind Anubis proof-of-work ('Beveiligde verbinding wordt gecontroleerd...'), and DANS deposit is scope- and institution-oriented (archaeology, SSH, life sciences) with no open… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both sit behind Anubis proof-of-work ('Beveiligde verbinding wordt gecontroleerd...'), and DANS deposit is scope- and institution-oriented (archaeology, SSH, life sciences) with no open…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both sit behind Anubis proof-of-work ('Beveiligde verbinding wordt gecontroleerd...'), and DANS deposit is scope- and institution-oriented (archaeology, SSH, life sciences) with no open…
  - [2] 2026-10-21: cited as the basis of the rejection: Both sit behind Anubis proof-of-work ('Beveiligde verbinding wordt gecontroleerd...'), and DANS deposit is scope- and institution-oriented (archaeology, SSH, life sciences) with no open bulk
- sources:
  - [1] https://dans.knaw.nl/en/deposit/
  - [2] https://dataverse.nl/

## dans easy (legacy)

- `storage/dans-easy` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://easy.dans.knaw.nl/
- free tier: None reachable: Retired. 'As of 2 December 2024, EASY will no longer be accessible'. Datasets migrated to the domain-specific DANS Data Stations. Any EASY quota figure found in third-party guides is dead. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Retired. 'As of 2 December 2024, EASY will no longer be accessible' — datasets migrated to the domain-specific DANS Data Stations. Any EASY quota figure found in third-party guides is dead.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Retired. 'As of 2 December 2024, EASY will no longer be accessible' — datasets migrated to the domain-specific DANS Data Stations. Any EASY quota figure found in third-party guides is dead.
- sources:
  - [1] https://easy.dans.knaw.nl/
