# DANS Data Stations

> datastations.nl | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datastations/ | JSON https://fshy.ajam.dev/api/v1/entity/datastations.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DANS Data Stations (ssh.datastations.nl / DataverseNL)

- `storage/dans-data-stations` | fails-identity | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ssh.datastations.nl
- free tier: 9.3 GB maximum per file, no per-dataset or per-collection quota configured. Dutch national repository (KNAW/NWO); deposit is free for researchers at Dutch institutions and for EASY-migrated data. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 9.3 GB maximum per file | bytes: 9300000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, unmetered; Dataverse-native presigned S3 redirect for public files. No egress pricing. | metered: no
- identity: institution
- interface: rest, ssh
- limits:
  - per-object-cap: 9.3 GB per file [1]
- limits note: 9.3 GB per file; UI upload must finish within 1.5 h; 2,000 files max inside a zip; 1,000 files per UI batch; 100-minute session timeout. Access is gated on affiliation in practice (DANS is for Dutch-institution research).
- interface detail: rest
- tooling: Full Dataverse REST API (probe: GET https://ssh.datastations.nl/api/info/version -> 200; DataverseNL -> '6.10.1 DANS-DataStation-PATCH-9'), SWORD v2, OAI-PMH.
- composes with: 9.3 GB/file x unlimited files per dataset x unlimited datasets. No enforced collection quota on either :root or the SSH station: GET /api/dataverses/root/storage/quota?showInherited=true -> 'No quota defined'. 2,200 files = 20 TB.
- reliability: Tightly coupled to Dutch institutional eligibility, so account supply is the limit rather than bytes; otherwise a mature Dataverse instance with no storage cliff.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 9.3 GB maximum per file, no per-dataset or per-collection quota configured. Dutch national repository (KNAW/NWO); deposit is free for researchers at Dutch institutions and for EASY-migrated data.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Yes, a file can be 9,3 GB max. But you can upload as many files as you want to a dataset.'
  - [2] 2026-10-21: (28/03/2024) — 9.3 GB/file, 2000 files per zip, 1.5 h UI timeout
  - [3] 2026-10-21: probe: GET -> 'No quota defined for this collection'
- sources:
  - [1] https://support.dans.knaw.nl/en/support/solutions/articles/80000969618-is-there-a-maximum-upload-size-per-file-
  - [2] https://support.dans.knaw.nl/en/support/solutions/articles/80001022346-upload-of-large-files-a-lot-of-files-in-dataversenl
  - [3] https://dataverse.nl/api/dataverses/root/storage/quota?showInherited=true
