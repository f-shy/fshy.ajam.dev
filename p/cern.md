# cern open data portal

> cern.ch | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cern/ | JSON https://fshy.ajam.dev/api/v1/entity/cern.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cern open data portal

- `storage/cern-open-data-portal` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://opendata.cern.ch/docs/terms-of-use
- free tier: none reachable: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity…
  - [2] 2026-10-21: cited as the basis of the rejection: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity, s
- sources:
  - [1] https://opendata.cern.ch/docs/terms-of-use
  - [2] https://opendata.cern.ch/docs/about

## cern open data portal / cern document server as writable storage

- `storage/cern-open-data-portal-cern-document-server-as-writable-s` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- page https://fshy.ajam.dev/p/cern.md
- free tier: none reachable: Read-only dissemination platform for external users. Submissions require internal CERN accounts, with no public deposit path. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not recorded | note: not applicable
- retention: not recorded
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
  - dead_end.why: Read-only dissemination for outsiders; CDS submissions are internal. No deposit path for a non-CERN account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Read-only dissemination for outsiders; CDS submissions are internal. No deposit path for a non-CERN account.
