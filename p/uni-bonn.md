# Göttingen Research Online

> uni-bonn.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-bonn/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-bonn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Göttingen Research Online / bonndata (University of Bonn) — Anubis-walled pair

- `storage/g-ttingen-research-online-bonndata-anubis-walled-pair` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.12.1
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:27.693Z (live) | stale on 2026-12-04
- url https://bonndata.uni-bonn.de
- free tier: No quota defined at root (bonndata). Same class of German university instance as Göttingen. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: The amount of data to be stored will be flexible and can be over 100 GB (on request) per researcher.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: The repository API enforces no explicit quota, while signup verification was obstructed by network proof-of-work challenges.
- reliability: Anubis proof-of-work on all HTML; API works.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://bonndata.uni-bonn.de/api/info/version — 6.7.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 but body is the 'Making sure you're not a bot!' Anubis page, so the form fields were NOT read
  - [4] 2026-11-09: the University of Bonn service page states a flexible allocation of over 100 GB per researcher on request | capture: sha256:714f2bb7d4fd873e2d3b597aa056ace83406ffdd36b1eed028ecf0eac1acf49c | quote: The amount of data to be stored will be flexible and can be over 100 GB (on request) per researcher.
  - [2] 2026-11-19: the live Dataverse version endpoint reports 6.12.1 | capture: sha256:a2adbe1e1242f10a3797fbd7895849921b738990334ca5ee2d8c2b6cba93ee25 | quote: {"status":"OK","data":{"version":"6.12.1","build":"master-bddc062-1"}}
  - [1] 2026-11-19: the root dataverse still has no defined quota | capture: sha256:1d14c5194b2c5c58390cdcc09b32ac730f21d5c174b178eafc04b15bcbb9ab14
  - [4] 2026-11-19: the service page still states a flexible allocation over 100 GB per researcher on request | capture: sha256:2d7890df8c25a746c0113e67049f78933c290872551032478ca1da984c0f2f4e | quote: The amount of data to be stored will be flexible and can be over 100 GB (on request) per researcher.
- sources:
  - [1] https://bonndata.uni-bonn.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://bonndata.uni-bonn.de/api/info/version
  - [3] https://bonndata.uni-bonn.de/dataverseuser.xhtml?editMode=CREATE
  - [4] https://www.hrz.uni-bonn.de/en/all-services/data-storage-fileservices/bonndata
