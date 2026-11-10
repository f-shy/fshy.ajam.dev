# Recherche Data

> data.gouv.fr | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data/ | JSON https://fshy.ajam.dev/api/v1/entity/data.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Recherche Data Gouv (French national Dataverse)

- `storage/recherche-data-gouv` | fails-identity | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://entrepot.recherche.data.gouv.fr
- disagrees on identity_kind: `storage/recherche-data-gouv` says institution, `storage/recherche-data-gouv-2` says email
- disagrees on verdict: `storage/recherche-data-gouv` says fails-identity, `storage/recherche-data-gouv-2` says fails-quota
- free tier: 50 GB max per file via the deposit interface; institutional datasets carry an agreement limit 'currently 5 TB'; datasets over 50 GB are explicitly supported via DVUploader and the S3 direct-upload API, and TB-range datasets are handled by arrangement | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB max per file | bytes: 50000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered, national infrastructure | metered: no
- identity: institution
- interface: s3, rest
- limits:
  - per-object-cap: 50 GB max per file [1]
- limits note: Deposit is restricted: 'Only research data produced by research teams with at least one collaborator affiliated to an institution belonging to the French public research community are accepted by right.' The 50 GB single-file cap is a hard interface limit (use DVUploader/S3 above it).
- interface detail: rest
- tooling: Dataverse REST + DVUploader + S3 direct upload (one-time upload URLs, multipart, /api/datasets/mpload). Same tooling chain as Harvard, so one client covers both.
- composes with: The 5 TB figure is per institutional agreement, i.e. per lab rather than per person. That is the shape that matters: one institution's allocation is 5 TB, not 500 GB
- reliability: Instance is healthy and live (Dataverse 6.0 at probe). The eligibility rule is an institutional gate, not a technical one. The API and storage behave normally for anyone who can authenticate.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB max per file via the deposit interface; institutional datasets carry an agreement limit 'currently 5 TB'; datasets over 50 GB are explicitly supported via DVUploader and the S3 direct-upload API, and TB-range datasets are handled by arrangement
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'the maximum file size limit is 50 GB ... For institutional datasets, please ensure compliance with the limit set by your agreement (currently 5 TB)' and 'Do not split large files to bypass the 50 GB limit. Instead, use the DVUploader application' (the provider's own rule: a file above 50 GB goes through DVUploader and is not split)
  - [2] 2026-10-21: read live: 'Only research data produced by research teams with at least one collaborator affiliated to an institution belonging to the French public research community are accepted by right'
  - [3] 2026-10-21: probe: GET -> 200 {"status":"OK","data":{"version":"6.0"}}
- sources:
  - [1] https://recherche.data.gouv.fr/en/guide/recommendations-on-large-datasets
  - [2] https://recherche.data.gouv.fr/en/faq
  - [3] https://entrepot.recherche.data.gouv.fr/api/info/version

## recherche data gouv (france)

- `storage/recherche-data-gouv-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://entrepot.recherche.data.gouv.fr/api/info/version
- disagrees on identity_kind: `storage/recherche-data-gouv` says institution, `storage/recherche-data-gouv-2` says email
- disagrees on verdict: `storage/recherche-data-gouv` says fails-identity, `storage/recherche-data-gouv-2` says fails-quota
- free tier: none reachable: Deposit must go into the institutional space of the establishment a contributor belongs to; the 'generic space' exists only for French institutions lacking their own space. Dataverse 6.0… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Deposit must go into the institutional space of the establishment a contributor belongs to; the 'generic space' exists only for French institutions lacking their own space. Dataverse 6.0…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Deposit must go into the institutional space of the establishment a contributor belongs to; the 'generic space' exists only for French institutions lacking their own space. Dataverse 6.0…
  - [2] 2026-10-21: cited as the basis of the rejection: Deposit must go into the institutional space of the establishment a contributor belongs to; the 'generic space' exists only for French institutions lacking their own space. Dataverse 6.0 nod
  - [3] 2026-10-21: cited as the basis of the rejection: Deposit must go into the institutional space of the establishment a contributor belongs to; the 'generic space' exists only for French institutions lacking their own space. Dataverse 6.0 nod
- sources:
  - [1] https://entrepot.recherche.data.gouv.fr/api/info/version
  - [2] https://entrepot.recherche.data.gouv.fr/api/dataverses/1
  - [3] https://recherche.data.gouv.fr/en/category/9/guide/all-you-need-to-know-about-the-recherche-data-gouv-repository
