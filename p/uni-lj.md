# University of Ljubljana ADP Dataverse

> uni-lj.si | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-lj/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-lj.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## University of Ljubljana ADP Dataverse (Slovenian Social Science Data Archive)

- `storage/university-of-ljubljana-adp-dataverse` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.9
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:22.054Z (live) | stale on 2026-12-04
- url https://dataverse.adp.fdv.uni-lj.si
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: the same as the free tier
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Open signup form is reachable but the operator runs an Anubis proof-of-work wall on the UI, so the honest reading is: no quota confirmed at the API, signup form exists, UI is PoW-walled.
- reliability: Anubis proof-of-work (Techaro BotStopper) on HTML pages; API is unaffected.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://dataverse.adp.fdv.uni-lj.si/api/info/version — 6.9
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200, but body is the Anubis PoW interstitial
  - [1] 2026-11-09: the repository's quota endpoint states that no quota is defined for the root collection | capture: sha256:29ef4551b3d86a41f8a16618ee481d39c87797b5bf3cc7a1b54036606d75257d
  - [1] 2026-11-19: the root collection's quota endpoint states no quota is defined for this collection | capture: sha256:f4faf331ebb90ba7132f9d23829ca7bfd7bfbb938acdf61a873e91bb9bd95645
- sources:
  - [1] https://dataverse.adp.fdv.uni-lj.si/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dataverse.adp.fdv.uni-lj.si/api/info/version
  - [3] https://dataverse.adp.fdv.uni-lj.si/dataverseuser.xhtml?editMode=CREATE
