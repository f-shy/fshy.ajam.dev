# DataverseNO

> dataverse.no | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseNO (UiT The Arctic University of Norway, national consortium)

- `storage/dataverseno` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.11
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.no
- disagrees on identity_kind: `storage/dataverseno` says institution, `storage/dataverseno-2` says email
- disagrees on verdict: `storage/dataverseno` says fails-identity, `storage/dataverseno-2` says fails-quota
- free tier: No quota defined at root. 2,311 datasets, 32 collections. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted, 1.39 s. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits note: No published cap.
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
  - [2] 2026-10-21: https://dataverse.no/api/info/version — 6.11
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: 'Log in or sign up with your institutional account — more information about account creation'; IdP selector with eduGAIN
  - [4] 2026-10-21: HTTP 302 to loginpage.xhtml
  - [5] 2026-10-21: 'Anyone affiliated with a Norwegian research institution can deposit their research data, free of charge'
- sources:
  - [1] https://dataverse.no/api/dataverses/root/storage/quota?showInherited=true
  - [2] https://dataverse.no/api/info/version
  - [3] https://dataverse.no/loginpage.xhtml
  - [4] https://dataverse.no/dataverseuser.xhtml?editMode=CREATE
  - [5] https://dataverse.no/

## dataverseno (norway)

- `storage/dataverseno-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://dataverse.no/
