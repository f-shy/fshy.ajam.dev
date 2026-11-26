# DesignSafe-CI

> designsafe-ci.org | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/designsafe-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/designsafe-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## designsafe-ci / nheri data depot (tacc)

- `storage/designsafe-ci-nheri-data-depot` | qualifies-with-caveat | evidence documented | binding write-gated | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T01:53:16.160Z (live) | stale on 2026-12-26
- url https://www.designsafe-ci.org/user-guide/curating/policies/
- free tier: Publishing: no size restriction on published datasets ('Currently we do not impose restrictions on the size of the datasets that can be published'); the largest published datasets are about 5 TB. Accepted content is limited to natural-hazards research datasets. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: no restriction on dataset size is imposed; the largest published datasets are about 5 TB | source: [1] | note: not applicable
- retention: TACC has formally committed to preserving the data with landing pages and corresponding DOIs indefinitely; DDR does not delete data or conduct deaccessions. | source: [1]
- egress: No transfer charge is stated on the Data Depot pages; downloads can go through the browser, Globus, Cyberduck or the TAPIS API. | metered: no
- identity: institution | detail: the sign-up form asks for an email affiliated with a trusted institution, plus institution name, country, URL and address; an institution outside the trusted list gives limited access to TACC resources and no eligibility to be a project's principal investigator (whether a limited account can publish is unverified) | country: research institution (a trusted-institution list applies)
- interface: browser, cli, rest
- limits:
  - write-gated (binding): publication accepts natural-hazards research datasets only, and each dataset is curated before it receives a DOI [1]
- binding note: no size cap applies, but only natural-hazards research datasets are accepted and each is curated before a DOI is issued; the account asks for a trusted-institution email
- interface detail: not documented
- tooling: the same as interface detail
- composes with: Data can be moved out through Globus, Cyberduck, scp, rsync or the TAPIS API, and shared with other cyberinfrastructure resources at TACC and other research centers.
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
  - [1] 2026-11-25: the curation policies state indefinite preservation of published data | capture: sha256:5735e33e81f95d0d2d23800ee2ff78209d0a2c4ed85ce864bf412c7bd7c5b1e0 | quote: TACC has formally committed to preserving the data with landing pages and corresponding DOIs indefinitely.
  - [3] 2026-11-25: the transfer guide documents a browser interface and a programmatic TAPIS API | capture: sha256:0a81eff486160be27bb76c4fbeb5b94ad4064bfeeb6ab5d36e0377e953b2927b | quote: For automated or large-scale data transfers, DesignSafe provides programmatic access through the TAPIS API. This method is particularly useful for:
  - [3] 2026-11-25: the transfer guide documents multiple export paths and states no transfer charge | capture: sha256:0a81eff486160be27bb76c4fbeb5b94ad4064bfeeb6ab5d36e0377e953b2927b | quote: Globus supplies high speed, reliable, and asynchronous transfers to DesignSafe. Once set up, Globus will allow you to not only transfer files to and from DesignSafe, but also other cyberinfrastructure resources at TACC and other research centers.
  - [3] 2026-11-25: the transfer guide documents chaining DesignSafe with other research cyberinfrastructure | capture: sha256:0a81eff486160be27bb76c4fbeb5b94ad4064bfeeb6ab5d36e0377e953b2927b | quote: Globus supplies high speed, reliable, and asynchronous transfers to DesignSafe. Once set up, Globus will allow you to not only transfer files to and from DesignSafe, but also other cyberinfrastructure resources at TACC and other research centers.
  - [1] 2026-11-25: the policies page states that published data is not deleted | capture: sha256:5735e33e81f95d0d2d23800ee2ff78209d0a2c4ed85ce864bf412c7bd7c5b1e0 | quote: DDR does not conduct re-appraisals or deaccessions, and does not delete data. In cases of tombstones, data is withdrawn from public access but it is not deleted.
  - [3] 2026-11-25: the transfer guide documents browser, CLI, Globus and API access with no stated transfer charge | capture: sha256:0a81eff486160be27bb76c4fbeb5b94ad4064bfeeb6ab5d36e0377e953b2927b | quote: For automated or large-scale data transfers, DesignSafe provides programmatic access through the TAPIS API. This method is particularly useful for:
- sources:
  - [1] https://www.designsafe-ci.org/user-guide/curating/policies/
  - [2] https://www.designsafe-ci.org/account/register/
  - [3] https://www.designsafe-ci.org/user-guide/managingdata/datatransfer/

## DesignSafe-CI Data Depot (NSF NHERI / TACC) - no published cap on published datasets

- `storage/designsafe-ci-data-depot-no-published-cap-on-published-d` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-25T04:14:20.834Z (live) | stale on 2026-12-10
- url https://www.designsafe-ci.org/
- free tier: right now there is no limit to the amount of files that can be published in DesignSafe | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: No per-object cap published; the data-curation FAQ states no limit on the number of files that can be published, and the policies page states no published-dataset size restriction, with largest published datasets at ~5 TB.
- retention: DDR does not conduct re-appraisals or deaccessions, and does not delete data. | source: [2] | note: Published data is preserved with no deletion or deaccession; TACC commits to keeping landing pages and DOIs indefinitely, with an archive copy on Ranch if resources are constrained.
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
- notes: No published cap on published dataset size or file count: 'right now there is no limit to the amount of files that can be published in DesignSafe'. Policies page describes largest published datasets as ~5 TB (CoreTrustSeal submission: 'Publications range up to a maximum of 5TB; seven current published datasets are over 1TB'), while a 2025 Frontiers paper reports individual datasets 'as large as 26' TB. Private working space ('My Data' / 'My Projects') is separate and unlimited in policy terms; uploads of 1 TB+ require a support ticket first.
- evidence note: the data-curation FAQ states that there is no limit to the amount of files that can be published in DesignSafe
- evidence:
  - [1] 2026-10-21: 'While right now there is no limit to the amount of files that can be published in DesignSafe...'
  - [2] 2026-10-21: TACC Corral + Ranch, replication, DOIs, continuity plan
  - [3] 2026-10-21: 'Publications range up to a maximum of 5TB; seven current published datasets are over 1TB'
  - [4] 2026-10-21: 'Please submit a ticket to notify us prior to uploading 1TB or more of data'
  - [5] 2026-10-21: 200, full fileObjs with system 'designsafe.storage.published' and per-file length (e.g. 3019136 bytes)
  - [6] 2026-10-21: ... - 404 on every unauthenticated variant tried (media, download, list)
  - [7] 2026-11-01: an institution outside the trusted list is accepted with limited access, and no card or phone field appears on the form | capture: sha256:9949560792a5e930fe348ae56513841143f50a5d8b2e2537aaa550a88ce65fe1 | quote: I understand the institution I have entered is not included in our list of trusted institutions. My account will have limited access to TACC resources.
  - [8] 2026-11-01: the published file count is still uncapped, as the record states | capture: sha256:f64f2f593ce5d3619ed1785a4d3ce11a249553d63853bd80c8c9c0cdb90160e7 | quote: no limit to the amount of files that can be published in DesignSafe
  - [1] 2026-11-09: the data-curation FAQ states that the number of files published in DesignSafe is unlimited | capture: sha256:851accda894279bac0bef5f3e86e77a309fa5870356cc6464d88ee043ab9fe85 | quote: While right now there is no limit to the amount of files that can be published in DesignSafe, the comprehension and reuse potential of the data should be important considerations when selecting what data can be published.
  - [2] 2026-11-25: The published-data policy sets no size restriction and reports the largest published datasets at ~5 TB. | capture: sha256:03b81c82591d4f3ef6351711b98f5d7607bfae0b6ead43adaf71ad93e757ea82 | quote: Currently we do not impose restrictions on the size of the datasets that can be published. This approach recognizes the necessity of comprehensive data collection and the increasingly large sizes of datasets in natural hazards research. Largest published datasets in DDR are ~5 TB.
  - [2] 2026-11-25: Published data is not deleted or deaccessioned by DDR. | capture: sha256:03b81c82591d4f3ef6351711b98f5d7607bfae0b6ead43adaf71ad93e757ea82 | quote: DDR does not conduct re-appraisals or deaccessions, and does not delete data.
  - [2] 2026-11-25: Published data is retained without deletion or deaccession. | capture: sha256:03b81c82591d4f3ef6351711b98f5d7607bfae0b6ead43adaf71ad93e757ea82 | quote: DDR does not conduct re-appraisals or deaccessions, and does not delete data.
  - [2] 2026-11-25: The policies page is the source of the retention statement. | capture: sha256:03b81c82591d4f3ef6351711b98f5d7607bfae0b6ead43adaf71ad93e757ea82 | quote: DDR does not conduct re-appraisals or deaccessions, and does not delete data.
  - [1] 2026-11-25: The published file count is not capped. | capture: sha256:851accda894279bac0bef5f3e86e77a309fa5870356cc6464d88ee043ab9fe85 | quote: While right now there is no limit to the amount of files that can be published in DesignSafe, the comprehension and reuse potential of the data should be important considerations when selecting what data can be published.
  - [2] 2026-11-25: Published data and DOIs are preserved indefinitely; the continuity plan backs the chaining field. | capture: sha256:03b81c82591d4f3ef6351711b98f5d7607bfae0b6ead43adaf71ad93e757ea82 | quote: TACC has formally committed to preserving the data with landing pages and corresponding DOIs indefinitely.
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
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T11:17:24.267Z (live) | stale on 2026-12-26
- url https://designsafe-ci.org/user-guide/tools/advanced/hpcallocations/
- free tier: A Startup Allocation may request up to 20,000 node-hours annually, a Research Allocation has a maximum size of 100,000 node-hours annually, and an Educational Allocation may request up to 10,000 node-hours. 'Allocations are provided through NSF funding at no direct cost to the end user to anyone who meets the eligibility criteria above.' 'Startup and Educational Allocation requests receive a fast track review, bypassing the Allocation Advisory Board' and 'DesignSafe project staff will review these requests according to the merit review criteria above, and will act on these requests within two weeks of their submission.' 'Startup Allocations may be for unfunded exploratory research'. 'Users who are not eligible for an NSF-provided allocation, may choose to purchase additional compute time or storage capacity from TACC' at rates of 'approximately $60/TB/year' for storage and 'approximately $0.50 per node hour' for compute as of January 2024. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed-allocation
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
  - [1] 2026-11-25: the allocation page states the annual node-hour ceilings of the Startup, Research and Educational allocations | capture: sha256:453505d51c55fd0affd7ca80e0bff1c10cea32ec0aef27164d733cec868360fc | quote: A Startup Allocation may request up to 20,000 node-hours annually. ... A Research allocation has a maximum size of 100,000 node-hours annually. ... An Educational allocation may request up to 10,000 node-hours. ... Educational Allocations receive fast track review. ... will act on these requests within two weeks of their submission. ... Startup Allocations may be for unfunded exploratory research
  - [1] 2026-11-25: the allocation page still states the three annual node-hour ceilings and the Educational fast-track review | capture: sha256:453505d51c55fd0affd7ca80e0bff1c10cea32ec0aef27164d733cec868360fc | quote: A Startup Allocation may request up to 20,000 node-hours annually. ... A Research allocation has a maximum size of 100,000 node-hours annually. ... An Educational allocation may request up to 10,000 node-hours. ... Educational Allocations receive fast track review. ... will act on these requests within two weeks of their submission. ... Startup Allocations may be for unfunded exploratory research
- sources:
  - [1] https://designsafe-ci.org/user-guide/tools/advanced/hpcallocations/
  - [2] https://www.designsafe-ci.org/community/news/2025/july/message-from-the-nheri-council/
