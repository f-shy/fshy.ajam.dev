# University of Ljubljana ADP Dataverse

> uni-lj.si | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-lj/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-lj.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## University of Ljubljana ADP Dataverse (Slovenian Social Science Data Archive)

- `storage/university-of-ljubljana-adp-dataverse` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.9
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.adp.fdv.uni-lj.si
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Open signup form is reachable but the operator runs an Anubis proof-of-work wall on the UI, so the honest reading is: no quota confirmed at the API, signup form exists, UI is PoW-walled.
- reliability: Anubis proof-of-work (Techaro BotStopper) on HTML pages; API is unaffected.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://dataverse.adp.fdv.uni-lj.si/api/info/version — 6.9
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200, but body is the Anubis PoW interstitial
- sources:
  - [1] https://dataverse.adp.fdv.uni-lj.si/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dataverse.adp.fdv.uni-lj.si/api/info/version
  - [3] https://dataverse.adp.fdv.uni-lj.si/dataverseuser.xhtml?editMode=CREATE
