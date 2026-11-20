# DATADOI

> datadoi.ee | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datadoi/ | JSON https://fshy.ajam.dev/api/v1/entity/datadoi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DATADOI (Estonian Data Archive, University of Tartu)

- `storage/datadoi` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:31.166Z (live) | stale on 2026-12-04
- url https://datadoi.ee
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1] | note: the quota endpoint names no storage number; no total quota is defined for the collection
- per-object cap: When uploading via a browser, the recommended size of one file is up to 10 GB and up to 1,000 files per upload. | source: [2] | note: a recommended size, not a stated maximum
- retention: Datasets are preserved until the end of the repository’s lifetime. | source: [2] | note: the retention period is the lifetime of the repository
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: the policies page recommends one file up to 10 GB and up to 1,000 files per upload
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Small national archive with an open local signup; a low-traffic instance is the likeliest kind to have left :MaxFileUploadSizeInBytes unset.
- reliability: Small operator; /api/builtin-users redirects to the front page, so account creation is UI-only.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No quota defined at root.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [3] 2026-10-21: https://datadoi.ee/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [4] 2026-10-21: HTTP 200 (native signup form present)
  - [1] 2026-11-09: the repository's own quota endpoint states this message and names no storage number | capture: sha256:627a0c166ef99595acfde854dc6a73248578ad7d7f2f064a30bcff617aede2c7 | quote: No quota defined for this collection
  - [2] 2026-11-09: the policies page states a recommended size of up to 10 GB per file and up to 1,000 files per upload | capture: sha256:ef53867866987fb391b0501199395bc497a7fc45c557765edfa5ebf5407e219f | quote: When uploading via a browser, the recommended size of one file is up to 10 GB and up to 1,000 files per upload.
  - [2] 2026-11-09: the preservation policy names the lifetime of the repository as the retention period | capture: sha256:ef53867866987fb391b0501199395bc497a7fc45c557765edfa5ebf5407e219f | quote: Datasets are preserved until the end of the repository’s lifetime.
  - [1] 2026-11-09: the quota endpoint returns this sentence | capture: sha256:dc3fdd9ff0ef37618c739371ab90ec4f1320f555260269f0eb34dc4d1c0ca88c | quote: No quota defined for this collection
  - [1] 2026-11-09: the captured endpoint body contains no storage number | capture: sha256:dc3fdd9ff0ef37618c739371ab90ec4f1320f555260269f0eb34dc4d1c0ca88c
  - [2] 2026-11-19: the first-party policy states the recommended per-file and per-upload sizes | capture: sha256:08e4b0303aca4644776148a39879a6d41601cf1242c75b787add34814d7ed594 | quote: When uploading via a browser, the recommended size of one file is up to 10 GB and up to 1,000 files per upload.
  - [2] 2026-11-19: the first-party policy states the retention period | capture: sha256:08e4b0303aca4644776148a39879a6d41601cf1242c75b787add34814d7ed594 | quote: Datasets are preserved until the end of the repository’s lifetime.
- sources:
  - [1] https://datadoi.ee/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://datadoi.ee/files/policies.pdf
  - [3] https://datadoi.ee/api/info/version
  - [4] https://datadoi.ee/dataverseuser.xhtml?editMode=CREATE
