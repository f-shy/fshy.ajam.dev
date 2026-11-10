# CROSSDA

> crossda.hr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crossda/ | JSON https://fshy.ajam.dev/api/v1/entity/crossda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CROSSDA (Croatian Social Science Data Archive)

- `storage/crossda` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.2
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.crossda.hr
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Older 6.2 build that still exposes the quota endpoint and reports none. Confirms the pattern reaches back before 6.10.
- reliability: Version 6.2; expect a narrower API surface than 6.10+.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://data.crossda.hr/api/info/version — 6.2
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200
- sources:
  - [1] https://data.crossda.hr/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://data.crossda.hr/api/info/version
  - [3] https://data.crossda.hr/dataverseuser.xhtml?editMode=CREATE
