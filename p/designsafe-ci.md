# DesignSafe-CI

> designsafe-ci.org | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/designsafe-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/designsafe-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## designsafe-ci / nheri data depot (tacc)

- `storage/designsafe-ci-nheri-data-depot` | qualifies-with-caveat | evidence documented | binding write-gated | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T01:24:11.235Z (live) | stale on 2026-12-05
- url https://www.designsafe-ci.org/user-guide/curating/policies/
- free tier: Publishing: no size restriction on published datasets ('Currently we do not impose restrictions on the size of the datasets that can be published'); the largest published datasets are about 5 TB. Accepted content is limited to natural-hazards research datasets. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: no restriction on dataset size is imposed; the largest published datasets are about 5 TB | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution | detail: the sign-up form asks for an email affiliated with a trusted institution, plus institution name, country, URL and address; an institution outside the trusted list gives limited access to TACC resources and no eligibility to be a project's principal investigator (whether a limited account can publish is unverified) | country: research institution (a trusted-institution list applies)
- interface: unknown
- limits:
  - write-gated (binding): publication accepts natural-hazards research datasets only, and each dataset is curated before it receives a DOI [1]
- binding note: no size cap applies, but only natural-hazards research datasets are accepted and each is curated before a DOI is issued; the account asks for a trusted-institution email
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The repository is supported by the NSF through March of 2027; TACC has formally committed to preserving published data with landing pages and DOIs indefinitely if the program ends.
- notes: Publishing is genuinely uncapped. 'Currently we do not impose restrictions on the size of the datasets that can be published .. Largest published datasets in DDR are ~5 TB'. But it is a c.
- evidence note: The curation policies page and the registration page of designsafe-ci.org, re-read on 2026-11-03, state no size restriction on published datasets, the natural-hazards scope, and the trusted-institution registration notice. Whether a limited account can publish is not stated and stays unverified.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Publishing is genuinely uncapped — 'Currently we do not impose restrictions on the size of the datasets that can be published ... Largest published datasets in DDR are ~5 TB' — but it is a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Publishing is genuinely uncapped — 'Currently we do not impose restrictions on the size of the datasets that can be published ... Largest published datasets in DDR are ~5 TB' — but it is a…
  - [1] 2026-11-03: published dataset size is unrestricted | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: Currently we do not impose restrictions on the size of the datasets that can be published.
  - [1] 2026-11-03: the repository accepts natural-hazards datasets only | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: We accept engineering and social and behavioural sciences datasets conducted in the context of natural hazards regarding the impacts of wind, earthquake, storm surge, wildfires, and sustainable materials management.
  - [2] 2026-11-03: registration asks for an institution and limits an account whose institution is not on the trusted list | capture: sha256:9949560792a5e930fe348ae56513841143f50a5d8b2e2537aaa550a88ce65fe1 | quote: I understand the institution I have entered is not included in our list of trusted institutions. My account will have limited access to TACC resources. I will be ineligible to become a project's principle investigator.
  - [1] 2026-11-03: published dataset size is unrestricted, so the allowance reaches 10 TiB and 20 TiB | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: Currently we do not impose restrictions on the size of the datasets that can be published.
  - [1] 2026-11-03: TACC commits to indefinite preservation of published data | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: TACC has formally committed to preserving the data with landing pages and corresponding DOIs indefinitely.
  - [1] 2026-11-03: the policies page states no dataset size restriction | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: Currently we do not impose restrictions on the size of the datasets that can be published.
  - [1] 2026-11-04: published dataset size is unrestricted | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: Currently we do not impose restrictions on the size of the datasets that can be published.
  - [1] 2026-11-04: the repository accepts natural-hazards datasets only | capture: sha256:09175ba0c68c45d461f826c744025b077191eca2dc646bb0e928851624e4c1d3 | quote: We accept engineering and social and behavioural sciences datasets conducted in the context of natural hazards regarding the impacts of wind, earthquake, storm surge, wildfires, and sustainable materials management. In the area of engineering, the primary focus is on data generated through
  - [2] 2026-11-04: registration asks for an institution and limits an account whose institution is not on the trusted list | capture: sha256:9949560792a5e930fe348ae56513841143f50a5d8b2e2537aaa550a88ce65fe1 | quote: I understand the institution I have entered is not included in our list of trusted institutions. My account will have limited access to TACC resources. I will be ineligible to become a project's principle investigator. I may edit my profile after creation with trusted credentials to remove
- sources:
  - [1] https://www.designsafe-ci.org/user-guide/curating/policies/
  - [2] https://www.designsafe-ci.org/account/register/

## DesignSafe-CI Data Depot (NSF NHERI / TACC) - no published cap on published datasets

- `storage/designsafe-ci-data-depot-no-published-cap-on-published-d` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:17.594Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.designsafe-ci.org/
- free tier: No published cap on published dataset size or file count: 'right now there is no limit to the amount of files that can be published in DesignSafe'. Policies page describes largest published datasets as ~5 TB (CoreTrustSeal submission: 'Publications range up to a maximum of 5TB; seven current published datasets are over 1TB'), while a 2025 Frontiers paper reports individual datasets 'as large as 26' TB. Private working space ('My Data' / 'My Projects') is separate and unlimited in policy terms; uploads of 1 TB+ require a support ticket first. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Globus and HTTPS downloads from public Data Depot. Zip downloads are capped at 2 GB per request. Public metadata API endpoints return complete file manifests with lengths and paths. | metered: no
- identity: email | detail: a TACC account is created at the TACC Accounts form with a first and last name, an email address, a password, and an institution the form looks up by name or accepts typed in, with that institution's country, URL and postal address. The form asks for an email affiliated with the institution; an address whose domain does not match the selected institution is still accepted but 'will require administrative approval', and an institution outside the trusted list gives an account 'limited access to TACC resources' that cannot become a project's principal investigator. No card and no phone number is asked for.
- interface: rest
- limits:
  - write-gated (binding): approval [1]
- limits note: Write access requires a free self-registered TACC account and editorial curation approval. Datasets must fall within natural-hazards engineering and social science research scope. Unauthenticated direct HTTP download paths remain unverified.
- interface detail: rest
- tooling: Tapis/Agave REST API + dapi Python client (dapi.publications), Globus, JupyterHub, and the Data Depot browser. Public metadata endpoints need no token; the dapi client expects a Tapis token even for public listings, and the unauthenticated /api/files/v2/ media path 404s - so treat the byte-read path as authenticated-or-Globus until proven otherwise.
- composes with: Per published project, and there is no documented per-project ceiling, so the multiplier is projects. NSF-funded continuity: data transfers to a successor awardee and TACC commits to keeping landing pages and DOIs indefinitely.
- reliability: CoreTrustSeal-certified, two-region replication (Corral + Ranch tape). Downloads over ~2 GB need Globus, which is a client install, not a URL.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'While right now there is no limit to the amount of files that can be published in DesignSafe...'
  - [2] 2026-10-21: TACC Corral + Ranch, replication, DOIs, continuity plan
  - [3] 2026-10-21: 'Publications range up to a maximum of 5TB; seven current published datasets are over 1TB'
  - [4] 2026-10-21: 'Please submit a ticket to notify us prior to uploading 1TB or more of data'
  - [5] 2026-10-21: 200, full fileObjs with system 'designsafe.storage.published' and per-file length (e.g. 3019136 bytes)
  - [6] 2026-10-21: ... - 404 on every unauthenticated variant tried (media, download, list)
  - [7] 2026-11-01: an institution outside the trusted list is accepted with limited access, and no card or phone field appears on the form | capture: sha256:9949560792a5e930fe348ae56513841143f50a5d8b2e2537aaa550a88ce65fe1 | quote: I understand the institution I have entered is not included in our list of trusted institutions. My account will have limited access to TACC resources.
  - [8] 2026-11-01: the published file count is still uncapped, as the record states | capture: sha256:f64f2f593ce5d3619ed1785a4d3ce11a249553d63853bd80c8c9c0cdb90160e7 | quote: no limit to the amount of files that can be published in DesignSafe
- sources:
  - [1] https://designsafe-ci.org/user-guide/curating/faq/
  - [2] https://designsafe-ci.org/user-guide/curating/policies/
  - [3] https://www.coretrustseal.org/wp-content/uploads/2023/01/20230126-designsafe_final.pdf
  - [4] https://designsafe-ci.org/user-guide/managingdata/datatransfer/
  - [5] https://www.designsafe-ci.org/api/publications/v2/PRJ-6238/
  - [6] https://www.designsafe-ci.org/api/files/v2/media/system/designsafe.storage.published/
  - [7] https://www.designsafe-ci.org/account/register/
  - [8] https://www.designsafe-ci.org/user-guide/curating/faq/

## DesignSafe-CI

- `compute/designsafe-ci` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://designsafe-ci.org/user-guide/tools/advanced/hpcallocations/
- free tier: A Startup Allocation may request up to 20,000 node-hours annually with fast-track review acted on within two weeks, a Research Allocation up to 100,000 node-hours annually, and an Educational Allocation up to 10,000 node-hours, all provided through NSF funding "at no direct cost to the end user". Unfunded exploratory research is explicitly allowed on a Startup Allocation. Users outside the NSF eligibility categories may buy time from TACC at approximately USD 0.50 per node-hour and storage at approximately USD 60 per TB per year. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The PI is "typically a faculty member or research scientist at a US-based academic institution" and the enumerated alternatives are all US organisations, agencies, school districts, museums or companies; a self-employed person outside the US appears in no category, and foreign collaborators reach the machine only through a US PI's allocation. [1]
- limits note: The PI is "typically a faculty member or research scientist at a US-based academic institution" and the enumerated alternatives are all US organisations, agencies, school districts, museums or companies; a self-employed person outside the US appears in no category, and foreign collaborators reach the machine only through a US PI's allocation.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The purchased route is the composition worth noting: USD 0.50 per node-hour buys a TACC node of 48 to 64 cores, so roughly USD 0.008 to USD 0.01 per core-hour with no affiliation and no review, which is the cheapest way out of the identity gate found among evaluated providers and does not depend on the NSF eligibility categories at all.
- reliability: no reliability event recorded
- notes: The account is open to anyone, but the account alone does not reach the HPC queue: portal tools are capped by "built-in constraints that limit the amount of compute time" with no published ceiling, and command-line access needs the allocation. Startup review skips the Allocation Advisory Board and is decided within two weeks, which makes 20,000 node-hours the realistic ask rather than the 100,000. Node-hour to core-hour conversion depends on the TACC system assigned, which the page does not name, so no conversion is published here.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-reviewed-allocation
- evidence:
  - [1] 2026-10-22: "A Startup Allocation may request up to 20,000 node-hours annually"; "A Research allocation has a maximum size of 100,000 node-hours annually"; "An Educational allocation may request up to 10,000 node-hours", quoted
  - [1] 2026-10-22: "an additional allocation via DesignSafe is headed by a project PI, typically a faculty member or research scientist at a US-based academic institution"; "foreign collaborators are eligible to make use of that allocation", quoted
  - [1] 2026-10-22: "Allocations are provided through NSF funding at no direct cost to the end user"; purchase rates "approximately $0.50 per node hour" for compute and "approximately $60/TB/year" for storage, dated January 2024 in the text, quoted
  - [1] 2026-10-22: "DesignSafe is broadly available to any researcher or practitioner working in open Natural Hazards Engineering and Social Science research", quoted
  - [2] 2026-10-22: services, including HPC resources and data publication, are described as operating during a no-cost extension, quoted
- sources:
  - [1] https://designsafe-ci.org/user-guide/tools/advanced/hpcallocations/
  - [2] https://www.designsafe-ci.org/community/news/2025/july/message-from-the-nheri-council/
