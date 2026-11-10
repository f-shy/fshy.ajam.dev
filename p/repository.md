# cern document server

> repository.cern | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/repository/ | JSON https://fshy.ajam.dev/api/v1/entity/repository.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cern document server (repository.cern, inveniordm)

- `storage/cern-document-server` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://repository.cern/api/records?q=files.size:[1000000000
- free tier: None reachable: CERN institutional repository. Submissions are internal. Also holds no large files: querying files.size >= 1GB returned 0 records out of 73,837, so even as a read source it offers nothing f. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: CERN institutional repository — submissions are internal. Also holds no large files: querying files.size >= 1GB returned 0 records out of 73,837, so even as a read source it offers nothing…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: CERN institutional repository — submissions are internal. Also holds no large files: querying files.size >= 1GB returned 0 records out of 73,837, so even as a read source it offers nothing…
  - [2] 2026-10-21: cited as the basis of the rejection: CERN institutional repository — submissions are internal. Also holds no large files: querying files.size >= 1GB returned 0 records out of 73,837, so even as a read source it offers nothing f
  - [3] 2026-10-21: cited as the basis of the rejection: CERN institutional repository — submissions are internal. Also holds no large files: querying files.size >= 1GB returned 0 records out of 73,837, so even as a read source it offers nothing f
- sources:
  - [1] https://repository.cern/api/records?q=files.size:[1000000000
  - [2] https://repository.cern/api/records?size=1
  - [3] https://inveniosoftware.org/showcase/
