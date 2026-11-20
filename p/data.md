# Data

> data.gouv.fr | Storage; 3 records: free tier, limits, identity cost and evidence.

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
- reliability: unverified: the guide and FAQ pages answered HTTP 503 on 2026-11-19 and the site showed a maintenance page; routes tried: a direct read, pinned jina-keyless, cfbr, firecrawl, browserless, zenrows and scrapedo, a header dump, a 2026-10 archive lookup, and an HTTP probe. A separate probe of the Dataverse version endpoint answered HTTP 200.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB max per file via the deposit interface; institutional datasets carry an agreement limit 'currently 5 TB'; datasets over 50 GB are explicitly supported via DVUploader and the S3 direct-upload API, and TB-range datasets are handled by arrangement
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'the maximum file size limit is 50 GB ... For institutional datasets, please ensure compliance with the limit set by your agreement (currently 5 TB)' and 'Do not split large files to bypass the 50 GB limit. Instead, use the DVUploader application' (the provider's own rule: a file above 50 GB goes through DVUploader and is not split)
  - [2] 2026-10-21: read live: 'Only research data produced by research teams with at least one collaborator affiliated to an institution belonging to the French public research community are accepted by right'
  - [3] 2026-10-21: probe: GET -> 200 {"status":"OK","data":{"version":"6.0"}}
  - probe:https://recherche.data.gouv.fr/en/guide/recommendations-on-large-datasets 2026-11-19: the guide URL answered HTTP 503 on 2026-11-19; the whole site served a maintenance page | capture: sha256:fa171d58ea27e49f179899472a0a1978e1958ffc79cdabafb21710edc50cf467 | quote: "status": 503
- sources:
  - [1] https://recherche.data.gouv.fr/en/guide/recommendations-on-large-datasets
  - [2] https://recherche.data.gouv.fr/en/faq
  - [3] https://entrepot.recherche.data.gouv.fr/api/info/version

## recherche data gouv (france)

- `storage/recherche-data-gouv-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.551Z (live) | stale on 2026-12-04
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
  - [2] 2026-11-19: the live Dataverse API still requires deposits into an institutional space, confirming the rejection | capture: sha256:ca57207a0e865cfe440e581c35ed3a8932d58779f4ee0624b87cb406f950c382 | quote: Data should be deposited in the space assigned to an institution which one of the contributor belongs to. A generic space is available for data produced by institutions which do not such a space yet themselves.
  - [1] 2026-11-19: the repository still runs Dataverse 6.0, matching the record's note | capture: sha256:6103dde37141c44923206ebde938b8f5052b94abbec5dfcd49ef69123ad796ff | quote: {"status":"OK","data":{"version":"6.0","build":"289a22c"}}
- sources:
  - [1] https://entrepot.recherche.data.gouv.fr/api/info/version
  - [2] https://entrepot.recherche.data.gouv.fr/api/dataverses/1
  - [3] https://recherche.data.gouv.fr/en/category/9/guide/all-you-need-to-know-about-the-recherche-data-gouv-repository

## dati.gov.it, data.overheid.nl, data.gouv.fr, data.vic.gov.au, data.nsw.gov.

- `storage/dati-gov-it-data-overheid-nl-data-gouv-fr-data-vic-gov-a` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.062Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/data.md
- free tier: None reachable: A cluster of national/state portals that fail at the very first probe. 404 on the CKAN action API and either 404/403 on /user/register. data.gouv.fr has its own API (not CKAN); data.overhei. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the data.gouv.fr and dati.gov.it first-party API pages state no per-object size cap | note: not applicable
- retention: stated-absent: the data.gouv.fr and dati.gov.it first-party API pages state no retention period for stored data
- egress: stated-absent: the data.gouv.fr and dati.gov.it first-party API pages state no egress terms for stored data | metered: no
- identity: email
- interface: rest
- interface detail: A cluster of government open-data portals; data.gouv.fr exposes a catalogue API for metadata and resource links, and dati.gov.it exposes CKAN API endpoints returning JSON.
- tooling: not documented
- composes with: stated-absent: these government catalogue APIs publish metadata and links to data and state no way to chain byte storage into other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: A cluster of national/state portals that fail at the very first probe — 404 on the CKAN action API and either 404/403 on /user/register. data.gouv.fr has its own API (not CKAN)…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: A cluster of national/state portals that fail at the very first probe — 404 on the CKAN action API and either 404/403 on /user/register. data.gouv.fr has its own API (not CKAN)…
  - probe:https://data.gov.it/api/3/action/package_list 2026-11-19: data.gov.it CKAN API gave no HTTP status on 2026-11-19 | capture: sha256:cd616a35f3cfc9e81b44e9dc8f437de239a5dcccf375ea305d07f95ebe574b0b | quote: "status": null
  - [1] 2026-11-19: data.gouv.fr exposes an HTTP API to consult catalogue metadata and links to data | capture: sha256:f34c04c397ddaf203c34cc7eb800c625ddea7d9f883bc8cc6c106054f8361d07 | quote: L'API permet de consulter les métadonnées ainsi que d'avoir un lien vers les données.
  - [2] 2026-11-19: dati.gov.it supports CKAN API requests returning JSON | capture: sha256:76fcb045c86b0d07d14e49fc4931386b77430cca820c2c1eaf49e645cd3474e7 | quote: Il portale supporta le API di CKAN che possono essere utilizzate attraverso richieste che forniscono i risultati formattati in JSON.
- sources:
  - [1] https://www.data.gouv.fr/dataservices/api-catalogue-des-donnees-ouvertes-data-gouv-fr
  - [2] https://www.dati.gov.it/api
