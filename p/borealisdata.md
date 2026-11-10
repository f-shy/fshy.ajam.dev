# Borealis

> borealisdata.ca | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/borealisdata/ | JSON https://fshy.ajam.dev/api/v1/entity/borealisdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Borealis (Canadian Dataverse Repository, University of Toronto / Scholars Portal)

- `storage/borealis` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.8.4-SP
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://borealisdata.ca
- free tier: No quota object. Not a policy number either. Nothing published. 24,727 datasets across 1,858 collections, all unmetered by the platform. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted; answered the version API in 0.77 s, the fastest of the six majors tested. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No per-file or per-account figure published; no quota endpoint returns a number. Platform default applies (unlimited unless :MaxFileUploadSizeInBytes is set).
- interface detail: REST (native Dataverse API v1), SWORD
- tooling: curl against /api/; same client code as Harvard
- composes with: Native email registration with no explicit byte quota published in user accounts. Houses large research collections with multi-gigabyte datasets.
- reliability: Scheduled upgrade to 6.12.1 with 7h downtime announced on the signup page itself — reads may be affected during maintenance windows.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No quota object. Not a policy number either — nothing published. 24,727 datasets across 1,858 collections, all unmetered by the platform.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: {"status":"OK","data":{"version":"v6.8.4-SP","build":null}}
  - [1] 2026-10-21: {"status":"OK","data":{"message":"No quota defined for this collection"}}
  - [3] 2026-10-21: HTTP 200, form served; fields dataverseUserForm:accountInfoView:{email,affiliation,userName,password}; none carry a required or aria-required attribute
  - [4] 2026-10-21: 'Users who wish to create collections and/or datasets and upload data and metadata must have a user acco...' (account required, no affiliation stated)
  - [5] 2026-10-21: 24,727 datasets; type=dataverse — 1,858
- sources:
  - [1] https://borealisdata.ca/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://borealisdata.ca/api/info/version
  - [3] https://borealisdata.ca/dataverseuser.xhtml?editMode=CREATE
  - [4] https://borealisdata.ca/technology/
  - [5] https://borealisdata.ca/api/search?q=*&type=dataset&per_page=1
