# Göttingen Research Online

> uni-bonn.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-bonn/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-bonn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Göttingen Research Online / bonndata (University of Bonn) — Anubis-walled pair

- `storage/g-ttingen-research-online-bonndata-anubis-walled-pair` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.7.1
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bonndata.uni-bonn.de
- free tier: No quota defined at root (bonndata). Same class of German university instance as Göttingen. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: The repository API enforces no explicit quota, while signup verification was obstructed by network proof-of-work challenges.
- reliability: Anubis proof-of-work on all HTML; API works.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://bonndata.uni-bonn.de/api/info/version — 6.7.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 but body is the 'Making sure you're not a bot!' Anubis page, so the form fields were NOT read
- sources:
  - [1] https://bonndata.uni-bonn.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://bonndata.uni-bonn.de/api/info/version
  - [3] https://bonndata.uni-bonn.de/dataverseuser.xhtml?editMode=CREATE
