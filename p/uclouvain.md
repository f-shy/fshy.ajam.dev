# UCLouvain Dataverse

> uclouvain.be | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uclouvain/ | JSON https://fshy.ajam.dev/api/v1/entity/uclouvain.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UCLouvain Dataverse (Open Data @ UCLouvain)

- `storage/uclouvain-dataverse` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.x
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.uclouvain.be
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Another open-signup, no-quota national instance.
- reliability: Login page advertises both institutional and native login.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [2] 2026-10-21: HTTP 200
  - [3] 2026-10-21: offers institutional login plus builtin
- sources:
  - [1] https://dataverse.uclouvain.be/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dataverse.uclouvain.be/dataverseuser.xhtml?editMode=CREATE
  - [3] https://dataverse.uclouvain.be/loginpage.xhtml
