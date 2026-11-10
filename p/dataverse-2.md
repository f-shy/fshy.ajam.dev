# DataverseLV

> dataverse.lv | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-2/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseLV (Latvian national Dataverse)

- `storage/dataverselv` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.11
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dv.dataverse.lv
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted; the apex dataverse.lv is Cloudflare-challenged but dv.dataverse.lv answers the API cleanly. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: National instance, open local signup, no quota object.
- reliability: Apex domain serves a Cloudflare interstitial; use the dv. hostname for API work.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 6.11, build master-dd1859d
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
- sources:
  - [1] https://dv.dataverse.lv/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dv.dataverse.lv/api/info/version
  - [3] https://dv.dataverse.lv/dataverseuser.xhtml?editMode=CREATE
