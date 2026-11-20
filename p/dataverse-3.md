# DataverseNO

> dataverse.no | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-3/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseNO (UiT The Arctic University of Norway, national consortium)

- `storage/dataverseno` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.11
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.166Z (live) | stale on 2026-12-04
- url https://dataverse.no
- disagrees on identity_kind: `storage/dataverseno` says institution, `storage/dataverseno-2` says email
- disagrees on verdict: `storage/dataverseno` says fails-identity, `storage/dataverseno-2` says fails-quota
- free tier: If you are affiliated with a Norwegian research institution that is not a DataverseNO partner, you can receive up to 10 GB storage space free of charge. | unit: GB | metered on: stored-bytes | read on: 2026-11-09 | source: [1] | note: If you are affiliated with a DataverseNO partner institution, there are currently no limitations to the amount of data you can archive and share in the repository
- per-object cap: Individual files should preferably not exceed 100 GB. | source: [2] | note: a recommendation, not a stated maximum
- retention: source: [3] | note: not stated
- egress: Cloudflare-fronted, 1.39 s. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits:
  - volume-quota: up to 10 GB storage space free of charge for researchers at a Norwegian non-partner institution [1]
  - per-object-cap: Individual files should preferably not exceed 100 GB [2]
- limits note: the same as the free tier
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: The no-quota half is true and large; the identity half closes the door. Login page reads 'Log in or sign up with your institutional account' and the signup route 302s to the Shibboleth IdP selector. Native username/email is listed only under 'Other options' and the create form does not resolve.
- reliability: Signup gated on eduGAIN/Shibboleth institutional identity.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No quota defined at root — 2,311 datasets, 32 collections.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [4] 2026-10-21: https://dataverse.no/api/info/version — 6.11
  - [3] 2026-10-21: 'No quota defined for this collection'
  - [5] 2026-10-21: 'Log in or sign up with your institutional account — more information about account creation'; IdP selector with eduGAIN
  - [6] 2026-10-21: HTTP 302 to loginpage.xhtml
  - [7] 2026-10-21: 'Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge'
  - [1] 2026-11-09: the who-can-use page states that researchers at a Norwegian non-partner institution receive up to 10 GB of storage free of charge | capture: sha256:fe77d0f92211c0c919de819ab23f933b97c0fbf21e7835a88dc4ba40cebb2662 | quote: If you are affiliated with a Norwegian research institution that is not a DataverseNO partner, you can receive up to 10 GB storage space free of charge.
  - [1] 2026-11-09: the who-can-use page states that partner-institution researchers have no limit on the amount of data they can archive and share | capture: sha256:fe77d0f92211c0c919de819ab23f933b97c0fbf21e7835a88dc4ba40cebb2662 | quote: If you are affiliated with a DataverseNO partner institution, there are currently no limitations to the amount of data you can archive and share in the repository
  - [2] 2026-11-09: the prepare-your-data page recommends that individual files not exceed 100 GB | capture: sha256:6a6999edef0725bcd847e4e3d300ae9c506b2d41a5c616f8a1d9bc85c4d5cc13 | quote: Individual files should preferably not exceed 100 GB.
  - [3] 2026-11-09: the root collection's quota endpoint states that no quota is defined for this collection | capture: sha256:f13d7f2bf7b4e7486a2ad8a9ae13f48f0692d280f1317b4cfc76a459e1fb739e | quote: No quota defined for this collection
  - [1] 2026-11-19: the first-party who-can-use page states the 10 GB free allocation for non-partner Norwegian researchers | capture: sha256:f507520d9ed762a9615d139bf832d34b5c4a9269cf01baa69975e85f73873905 | quote: If you are affiliated with a Norwegian research institution that is not a DataverseNO partner, you can receive up to 10 GB storage space free of charge.
  - [2] 2026-11-19: the first-party guidance states the recommended per-file size | capture: sha256:e4ffaf078c06a13ae552fabdfdf8ded451d80ab4d05fd8b7d614d389e5fb195a | quote: Individual files should preferably not exceed 100 GB.
- sources:
  - [1] https://info.dataverse.no/about/who-can-use-dataverseno/
  - [2] https://info.dataverse.no/deposit/prepare-your-data/
  - [3] https://dataverse.no/api/dataverses/root/storage/quota?showInherited=true
  - [4] https://dataverse.no/api/info/version
  - [5] https://dataverse.no/loginpage.xhtml
  - [6] https://dataverse.no/dataverseuser.xhtml?editMode=CREATE
  - [7] https://dataverse.no/

## dataverseno (norway)

- `storage/dataverseno-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:33.499Z (live) | stale on 2026-12-04
- url https://dataverse.no/
- disagrees on identity_kind: `storage/dataverseno` says institution, `storage/dataverseno-2` says email
- disagrees on verdict: `storage/dataverseno` says fails-identity, `storage/dataverseno-2` says fails-quota
- free tier: none reachable: Explicitly affiliation-gated: 'Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge at DataverseNO.' External depositors are out unless… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Explicitly affiliation-gated: 'Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge at DataverseNO.' External depositors are out unless…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly affiliation-gated: 'Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge at DataverseNO.' External depositors are out unless…
  - [1] 2026-11-19: deposit is restricted to affiliates of Norwegian research institutions | capture: sha256:b840720030cfce1b4ce586f8b67ee40db4ab3e48f6c59fe7f0112b54b3caef71 | quote: Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge, at DataverseNO.
- sources:
  - [1] https://dataverse.no/
