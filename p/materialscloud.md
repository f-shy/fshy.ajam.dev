# Materials Cloud

> materialscloud.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/materialscloud/ | JSON https://fshy.ajam.dev/api/v1/entity/materialscloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Materials Cloud Archive (EPFL / NCCR MARVEL)

- `storage/materials-cloud-archive` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:00.435Z (live) | stale on 2026-12-04
- url https://archive.materialscloud.org
- disagrees on verdict: `storage/materials-cloud-archive` says qualifies-with-caveat, `storage/materials-cloud-archive-2` says fails-quota
- free tier: 5 GB for general materials science research data, 50 GB for AiiDA databases. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB for general materials science research data | bytes: 5000000000 | source: [1] | note: not stated
- retention: Items will be retained for the lifetime of the repository, but at least for 10 years after deposition (guaranteed by CSCS). | source: [1] | note: not stated
- egress: Access to metadata and data files is provided over standard protocols such as HTTP and OAI-PMH. | metered: no
- identity: email | detail: registration with an email address
- interface: rest
- limits:
  - write-gated: reviewed by the Materials Cloud moderators [1]
  - per-object-cap (binding): 5 GB for general materials science research data [1]
- limits note: Per-object-cap 5 GB / 50 GB per record; moderation gate ('Once you submit your record for publication it will be reviewed by the Materials Cloud moderators'), scope-gated to computational materials science, and moderators explicitly police 'excessive submission rate'.
- interface detail: rest
- tooling: Email self-registration with a personal work area; HTTP + OAI-PMH read; DOI minting per record; versioning of published records. AiiDA provenance integration is the native client for the 50 GB tier.
- composes with: Unlimited records x 5 GB (or 50 GB for AiiDA databases). 100 records at 5 GB = 500 GB; the 50 GB AiiDA tier halves that to 10 records.
- reliability: EPFL-hosted and stable, but moderation is substantive (refereeable-quality requirement) and rate-policed. The opposite of an anonymous dump. Data survives; throughput is editorially throttled.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Volume and size limitations: 5 GB for general materials science research data, 50 GB for AiiDA databases. For larger datasets please contact us'
  - [2] 2026-10-21: 'By registering with your email to the Materials Cloud Archive...' (open self-registration), moderated before publication
  - withheld 2026-10-21: probe: GET /record/2026.196 -> 200 (90,945 bytes); 1,551 published records live
  - [1] 2026-11-09: the information page states a 5 GB general-research limit | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: 5 GB for general materials science research data, 50 GB for AiiDA databases.
  - [1] 2026-11-09: the information page states the retention period | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: Items will be retained for the lifetime of the repository, but at least for 10 years after deposition (guaranteed by CSCS).
  - [1] 2026-11-09: the information page states the access protocols | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: Access to metadata and data files is provided over standard protocols such as HTTP and OAI-PMH.
  - [2] 2026-11-09: the help page states registration with an email address | capture: sha256:f956f8ad32806a89c3a86ae9b92048222a4ae7ce63dbbaf13e928e9695fb60ac | quote: By registering with your email to the Materials Cloud Archive, moderators can contact you for any comments/explanations prior to publication, and notifications can be sent to you regarding the status of your record throughout the entire submission process.
  - [2] 2026-11-09: the help page states the moderation review | capture: sha256:f956f8ad32806a89c3a86ae9b92048222a4ae7ce63dbbaf13e928e9695fb60ac | quote: Once you submit your record for publication it will be reviewed by the Materials Cloud moderators.
  - [1] 2026-11-19: the first-party information page confirms the 5 GB and 50 GB limits | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: 5 GB for general materials science research data, 50 GB for AiiDA databases.
  - [1] 2026-11-19: the information page states the retention period | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: Items will be retained for the lifetime of the repository, but at least for 10 years after deposition (guaranteed by CSCS).
  - [1] 2026-11-19: the information page states the access protocols | capture: sha256:f76c1ae567bbfc5d0c9ef7c7c884b2e6b853748e9a13ab19e4d5ad3223fa9837 | quote: Access to metadata and data files is provided over standard protocols such as HTTP and OAI-PMH.
  - [2] 2026-11-19: the help page confirms the moderation write gate | capture: sha256:f956f8ad32806a89c3a86ae9b92048222a4ae7ce63dbbaf13e928e9695fb60ac | quote: Once you submit your record for publication it will be reviewed by the Materials Cloud moderators.
  - [2] 2026-11-19: the help page confirms registration is by email address | capture: sha256:f956f8ad32806a89c3a86ae9b92048222a4ae7ce63dbbaf13e928e9695fb60ac | quote: By registering with your email to the Materials Cloud Archive, moderators can contact you for any comments/explanations prior to publication
- sources:
  - [1] https://archive.materialscloud.org/information
  - [2] https://archive.materialscloud.org/help

## materials cloud archive

- `storage/materials-cloud-archive-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:09.582Z (live) | stale on 2026-12-04
- url https://archive.materialscloud.org/uploads/new
- disagrees on verdict: `storage/materials-cloud-archive` says qualifies-with-caveat, `storage/materials-cloud-archive-2` says fails-quota
- free tier: none reachable: InvenioRDM node with a hard login wall before any upload; publishing is tied to a Materials Cloud workflow rather than open deposit. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: InvenioRDM node with a hard login wall before any upload; publishing is tied to a Materials Cloud workflow rather than open deposit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: InvenioRDM node with a hard login wall before any upload; publishing is tied to a Materials Cloud workflow rather than open deposit.
  - [2] 2026-10-21: cited as the basis of the rejection: InvenioRDM node with a hard login wall before any upload; publishing is tied to a Materials Cloud workflow rather than open deposit.
  - [1] 2026-11-19: the upload page redirects to a login wall before any upload | capture: sha256:f49c749de599cae9eebf7ca63f74630dbfa611e4a75a1b4a59ff82fcc988ba65 | quote: x-web-final-url: https://archive.materialscloud.org/login/?next=%2Fuploads%2Fnew
- sources:
  - [1] https://archive.materialscloud.org/uploads/new
  - [2] https://archive.materialscloud.org/api/records?size=1
