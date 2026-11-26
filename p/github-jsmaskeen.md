# maverick1983/google-drive-service-account 45 tb recipe

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jsmaskeen/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jsmaskeen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## maverick1983/google-drive-service-account 45 tb recipe

- `storage/maverick1983-google-drive-service-account-45-tb-recipe-t` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.635Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-jsmaskeen.md
- free tier: none reachable: The arithmetic (30 projects x 100 SAs x 15 GB = 45 TB) is no longer executable: service accounts report storageQuota limit '0' and every upload returns 403 storageQuotaExceeded. The repo's… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party page states no per-object size cap; the README states only a 15 GB per-service-account quota | note: not applicable
- retention: stated-absent: the first-party page states no retention period in the recipe README; it describes capacity arithmetic only
- egress: stated-absent: the first-party page states no egress terms in the recipe README | metered: no
- identity: email
- interface: rest, cli
- interface detail: Google Drive API accessed through Google IAM service accounts; no dedicated storage client is published by the recipe
- tooling: not documented
- composes with: Chains 30 projects x 100 service accounts x 15 GB each into one 45 TB pool; uploaded files are owned by the uploading service account.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The arithmetic (30 projects x 100 SAs x 15 GB = 45 TB) is no longer executable: service accounts report storageQuota limit '0' and every upload returns 403 storageQuotaExceeded. The repo's…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The arithmetic (30 projects x 100 SAs x 15 GB = 45 TB) is no longer executable: service accounts report storageQuota limit '0' and every upload returns 403 storageQuotaExceeded. The repo's…
  - [1] 2026-11-19: new service accounts no longer receive the 15GiB that the 45 TB arithmetic depends on | capture: sha256:354cdec0705352eca638d7a559de4c58aeec440764b4cf5a06081576757d75f5 | quote: Note: As of April 15 2025, New service accounts will not have 15GiB of Google Drive Storage, hence this repository is specifically targeted at those users who have service accounts generated before April 15 2025, and wish to combine their storage into a unified place.
  - [2] 2026-11-19: the recipe's first-party README describes the Google Drive via service-account offer | capture: sha256:9c8e8cafcb206af97442ee5c43364c119c12b5087431dbef33eca9e8d22847e9 | quote: It is possible to use Google Cloud, for free, and use Google Drive up to 45 TB, through the Google IAM Service Accounts
  - [2] 2026-11-19: the recipe README states uploaded files are owned by the uploading account | capture: sha256:9c8e8cafcb206af97442ee5c43364c119c12b5087431dbef33eca9e8d22847e9 | quote: The owner account appears to be the one who uploaded the file.
- sources:
  - [1] https://github.com/jsmaskeen/sa-drive
  - [2] https://github.com/Maverick1983/google-drive-service-account
