# dans data

> knaw.nl | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/knaw/ | JSON https://fshy.ajam.dev/api/v1/entity/knaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dans data stations (knaw, netherlands) / dataversenl

- `storage/dans-data-stations-dataversenl` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.378Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: DANS deposit is domain-specific and researcher-oriented, with no general bulk-deposit offer | capture: sha256:bd3e3c62eb111fc82ec1d624370a7305d8162688ad0740bb8694791a6e0a4675 | quote: From 11 December 2023, it will no longer be possible to deposit data in EASY. Researchers, groups of researchers and data professionals can archive and publish their data in one of the four domain-specific DANS Data Stations.
- sources:
  - [1] https://dans.knaw.nl/en/deposit/
  - [2] https://dataverse.nl/

## dans easy (legacy)

- `storage/dans-easy` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:43.469Z (live) | stale on 2026-12-04
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
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Retired. 'As of 2 December 2024, EASY will no longer be accessible' — datasets migrated to the domain-specific DANS Data Stations. Any EASY quota figure found in third-party guides is dead.
  - [1] 2026-11-19: the EASY service is retired and datasets moved to the DANS Data Stations | capture: sha256:28bdf5798e1d274a0b47b86493755640b8b77ac8600612eaa30820ea01f03e49 | quote: As of 2 December 2024, EASY will no longer be accessible. Almost all datasets previously deposited in EASY have been successfully migrated to the new domain-specific DANS Data Stations
  - [1] 2026-11-19: the first-party page confirms EASY is no longer accessible | capture: sha256:28bdf5798e1d274a0b47b86493755640b8b77ac8600612eaa30820ea01f03e49 | quote: As of 2 December 2024, EASY will no longer be accessible.
- sources:
  - [1] https://easy.dans.knaw.nl/
