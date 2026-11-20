# CROSSDA

> crossda.hr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crossda/ | JSON https://fshy.ajam.dev/api/v1/entity/crossda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CROSSDA (Croatian Social Science Data Archive)

- `storage/crossda` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.2
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:58.759Z (live) | stale on 2026-12-04
- url https://data.crossda.hr
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: the same as the free tier
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Older 6.2 build that still exposes the quota endpoint and reports none. Confirms the pattern reaches back before 6.10.
- reliability: Version 6.2; expect a narrower API surface than 6.10+.
- notes: The quota endpoint states "No quota defined for this collection".
- evidence:
  - [2] 2026-10-21: https://data.crossda.hr/api/info/version — 6.2
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200
  - [1] 2026-11-09: the repository's quota endpoint states no quota is defined for the collection | capture: sha256:627a0c166ef99595acfde854dc6a73248578ad7d7f2f064a30bcff617aede2c7 | quote: No quota defined for this collection
  - [1] 2026-11-09: the repository's quota endpoint states that no quota is defined for the collection | capture: sha256:1f7ac263b17126124af7332df235877b589c80a82ab18432f2551bc22c42aaef
  - [1] 2026-11-19: the repository's quota endpoint states no quota is defined | capture: sha256:1ce0d4dfbbace8de96c8a3174ee0435c6454fbf7ddbd9c2dcf8e80b2b5f98169 | quote: No quota defined for this collection
  - [2] 2026-11-19: the version endpoint reports Dataverse 6.2 | capture: sha256:75d16054f5124979c5910304efcdd84875113812ef66ee1759073cc91634febf | quote: {"status":"OK","data":{"version":"6.2","build":"1603-a218417"}}
  - [3] 2026-11-19: the account-creation page offers account creation with login options | capture: sha256:87f21bfde27385dcae91774a1bb7afa78b8e134cc4fb0e5c86260ed1de7a704c | quote: You can also create a Dataverse account with one of our other log in options.
- sources:
  - [1] https://data.crossda.hr/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://data.crossda.hr/api/info/version
  - [3] https://data.crossda.hr/dataverseuser.xhtml?editMode=CREATE
