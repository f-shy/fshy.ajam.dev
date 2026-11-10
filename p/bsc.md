# BSC Dataverse

> bsc.es | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bsc/ | JSON https://fshy.ajam.dev/api/v1/entity/bsc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BSC Dataverse (Barcelona Supercomputing Center)

- `storage/bsc-dataverse` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.bsc.es
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Open local signup at a supercomputing centre. The operator demographic most likely to have real disk behind the instance.
- reliability: Also offers ORCID login; no published storage policy page found.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://dataverse.bsc.es/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200; loginpage also advertises ORCID
- sources:
  - [1] https://dataverse.bsc.es/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dataverse.bsc.es/api/info/version
  - [3] https://dataverse.bsc.es/dataverseuser.xhtml?editMode=CREATE
