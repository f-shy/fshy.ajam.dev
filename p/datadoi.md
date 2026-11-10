# DATADOI

> datadoi.ee | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datadoi/ | JSON https://fshy.ajam.dev/api/v1/entity/datadoi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DATADOI (Estonian Data Archive, University of Tartu)

- `storage/datadoi` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datadoi.ee
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
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
  - [2] 2026-10-21: https://datadoi.ee/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
- sources:
  - [1] https://datadoi.ee/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://datadoi.ee/api/info/version
  - [3] https://datadoi.ee/dataverseuser.xhtml?editMode=CREATE
