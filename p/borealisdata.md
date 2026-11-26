# Borealis

> borealisdata.ca | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/borealisdata/ | JSON https://fshy.ajam.dev/api/v1/entity/borealisdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Borealis (Canadian Dataverse Repository, University of Toronto / Scholars Portal)

- `storage/borealis` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.8.4-SP
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:00.039Z (live) | stale on 2026-12-04
- url https://borealisdata.ca
- free tier: Institutional collections are provided with between 1 TB and 10 TB of storage, with the option to increase that space as needed; non-affiliated users cannot deposit data by default. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted; answered the version API in 0.77 s, the fastest of the six majors tested. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No per-file or per-account figure published; no quota endpoint returns a number. Platform default applies (unlimited unless :MaxFileUploadSizeInBytes is set).
- interface detail: REST (native Dataverse API v1), SWORD
- tooling: curl against /api/; same client code as Harvard
- composes with: Native email registration with no explicit byte quota published in user accounts. Houses large research collections with multi-gigabyte datasets.
- reliability: The repository now runs v6.12.1.3-SP, so the previously announced upgrade has shipped.
- notes: No quota object. Not a policy number either. Nothing published. 24,727 datasets across 1,858 collections, all unmetered by the platform.
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
  - [4] 2026-11-19: Borealis now publishes a 1-10 TB per-institution storage allocation | capture: sha256:84292e2c248d05a09b6dae5d8b502d42618e035d519b506ad80e9cb468fbf4b1 | quote: Provided with an institutional collection and storage space in Borealis (between 1 TB and 10 TB), with the option to increase that space as needed;
  - [4] 2026-11-19:  | capture: sha256:84292e2c248d05a09b6dae5d8b502d42618e035d519b506ad80e9cb468fbf4b1 | quote: Provided with an institutional collection and storage space in Borealis (between 1 TB and 10 TB), with the option to increase that space as needed;
  - [4] 2026-11-19: the published allocation is denominated in TB | capture: sha256:84292e2c248d05a09b6dae5d8b502d42618e035d519b506ad80e9cb468fbf4b1 | quote: Provided with an institutional collection and storage space in Borealis (between 1 TB and 10 TB), with the option to increase that space as needed;
  - [1] 2026-11-19: the root collection still returns no quota object | capture: sha256:271c768532f370268d4a01df581b64a8766e61dd3a60ec84e933dde61334b97d
  - [2] 2026-11-19: the live version endpoint reports v6.12.1.3-SP | capture: sha256:13aea0841c94dc41ad5e299a86ac80b29dd7934add070be2d90935423c1a99f7 | quote: {"status":"OK","data":{"version":"v6.12.1.3-SP","build":null}}
- sources:
  - [1] https://borealisdata.ca/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://borealisdata.ca/api/info/version
  - [3] https://borealisdata.ca/dataverseuser.xhtml?editMode=CREATE
  - [4] https://borealisdata.ca/technology/
  - [5] https://borealisdata.ca/api/search?q=*&type=dataset&per_page=1
