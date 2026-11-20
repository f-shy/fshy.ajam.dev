# DataverseLV

> dataverse.lv | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-4/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseLV (Latvian national Dataverse)

- `storage/dataverselv` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.11
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:26.681Z (live) | stale on 2026-12-04
- url https://dv.dataverse.lv
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted; the apex dataverse.lv is Cloudflare-challenged but dv.dataverse.lv answers the API cleanly. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: the same as the free tier
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: National instance, open local signup, no quota object.
- reliability: Apex domain serves a Cloudflare interstitial; use the dv. hostname for API work.
- notes: The quota endpoint states "No quota defined for this collection".
- evidence:
  - [2] 2026-10-21: 6.11, build master-dd1859d
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
  - [1] 2026-11-09: the repository's quota endpoint states no quota is defined, so no numeric quota is published | capture: sha256:4e6b7acfb388a3c3ae8e318134efbee7b4a8bf236976f8b32f189458a64cb17f | quote: No quota defined for this collection
  - [1] 2026-11-09: the repository's quota endpoint states that no quota is defined for the collection | capture: sha256:5e766b7c3a45c26b8b5d1fb53a6a107e37c378dcd3ecd29ecfeb52d36b321b92
  - [1] 2026-11-19: the repository's quota endpoint still reports no quota defined for the collection | capture: sha256:92e8a23f8d2593525bb2e79bf51735a708c6e24f2801ac21bc162790ca0e0aa5 | quote: No quota defined for this collection
- sources:
  - [1] https://dv.dataverse.lv/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dv.dataverse.lv/api/info/version
  - [3] https://dv.dataverse.lv/dataverseuser.xhtml?editMode=CREATE
