# CyVerse Data

> cyverse.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyverse/ | JSON https://fshy.ajam.dev/api/v1/entity/cyverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CyVerse

- `compute/cyverse` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:18.802Z (live) | stale on 2026-12-05
- url https://cyverse.org/subscribe
- free tier: The free Basic tier is 5 GB of Data Store storage, 200 compute units per year and 1 concurrent job, where the page states "1 Compute Unit equals 1 Core Hour on a CPU". Paid individual tiers are Regular at USD 200 per year for 50 GB, 1,000 compute units and 2 concurrent jobs, and Pro at USD 400 per year for 4 TB, 25,000 compute units and 4 concurrent jobs, with GPU access by request on the two paid tiers only. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-small-tier
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: webdav, sftp, cli, rest
- limits:
  - volume-quota (binding): 5 GB of storage and 200 core-hours a year on the free tier, enforced since 1 March 2025, and the user portal states that data above quota is deleted and is not recoverable. [1]
- limits note: 5 GB of storage and 200 core-hours a year on the free tier, enforced since 1 March 2025, and the user portal states that data above quota is deleted and is not recoverable.
- binding note: the same as limits note
- interface detail: Data Store: WebDAV, SFTP, iCommands and GoCommands command-line tools, and the Discovery Environment web console; Terrain REST API, where the subscription page lists Advanced Features & APIs for Pro and Commercial only
- tooling: GoCommands and iCommands command-line tools for the Data Store, and the Terrain REST API; Discovery Environment web console
- composes with: CyVerse is the funding parent of the Galaxy Main hardware allocation, so the two accounts sit on overlapping machines; the useful composition is the paid Pro tier, where USD 400 a year buys 25,000 core-hours and 4 TB on the same infrastructure that hosts Galaxy, which is a batch analysis machine with a shell rather than Galaxy wrappers.
- reliability: no reliability event recorded
- notes: The free tier is small enough that recording it as capacity would mislead: 200 core-hours a year is one afternoon of a single core. Its value is the paid tier as a price floor, and the enforcement history as a reliability fact. It is not the cheapest cost per core-hour in the file: the DesignSafe record carries a TACC purchase rate near USD 0.008 to USD 0.01 per core-hour, but that is a quote-based purchase from a national laboratory rather than a published annual plan. CyVerse also removes accounts for inactivity, announced on its own 404 page, which is a fact a reader storing data there needs.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-small-tier
- evidence:
  - [1] 2026-10-22: tier table: Basic free with 5 GB, 200 compute units per year, 1 concurrent job; Regular USD 200 per year with 50 GB and 1,000 units; Pro USD 400 per year with 4 TB and 25,000 units, quoted
  - [1] 2026-10-22: "1 Compute Unit equals 1 Core Hour on a CPU", quoted
  - [2] 2026-10-22: "Starting March 1, 2025, we will begin to enforce data storage quotas and limits on all Basic (free) and paid subscription accounts"; "data exceeding your storage quota will be removed. Deleted data are not recoverable", quoted
  - [3] 2026-10-22: "All domestic and international CyVerse account holders receive a default allocation of 5GB of storage at no cost", quoted
  - [4] 2026-11-03: WebDAV access exists | capture: sha256:72a4d8f279169c1de51b78874eb98108a2eb272bf54c982b86629d52b50946f8 | quote: | WebDAV | Web & Command line | Any | Both | No | Yes (No for public data) | No limit |
  - [1] 2026-11-03: APIs are listed for Pro and Commercial only, not Basic | capture: sha256:b5d1e8b16870f145d8ec767e72fe3cfd741e33be3b2fed5a811c228733fbe552 | quote: | Advanced Features & APIs | - | - | Yes | Yes |
  - [4] 2026-11-03: SFTP access exists | capture: sha256:72a4d8f279169c1de51b78874eb98108a2eb272bf54c982b86629d52b50946f8 | quote: | SFTP | Desktop App & Command line | Any | Both | No (Yes for desktop app) | Yes (No for public data) | No limit |
  - [4] 2026-11-03: iCommands CLI exists | capture: sha256:72a4d8f279169c1de51b78874eb98108a2eb272bf54c982b86629d52b50946f8 | quote: | iCommands | Command line | Linux & macOS | Both | Yes | Yes (No for public data) | No limit |
  - [5] 2026-11-03: a Terrain API exists | capture: sha256:12300c2bb50610345c08c17d9d45be0ef4fe52827831ea0137b0406428e8a5f4 | quote: - [api/](https://docs.cyverse.org/api/) - the Terrain API and its endpoints
  - [4] 2026-11-04: the Data Store docs name the iCommands client; GoCommands is named in the same page | capture: sha256:bcb387d35a69eec6ae3727fc22c2ed93e9531b590fefa4c41789495d8f1bdba2 | quote: iCommands is a powerful command-line tool designed for data management in iRODS.
- sources:
  - [1] https://cyverse.org/subscribe
  - [2] https://cyverse.org/quota-enforce
  - [3] https://cyverse.org/policies/data
  - [4] https://learning.cyverse.org/ds/
  - [5] https://docs.cyverse.org/

## CyVerse Data Store

- `storage/cyverse-data-store` | fails-quota | evidence reported | binding write-gated | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cyverse.org/policies/data
- price $10.42/TB/month single-copy ($125/TB/yr), $8.75/TB/month above 4 TB, $20.83/TB/month double-copy. | parsed USD 8.75/TB-mo
- free tier: 5 GB default for every account, explicitly for 'all domestic and international CyVerse account holders'. Above that it is paid: $125/TB/year single-copy up to 4 TB, $105/TB/year beyond, and $250/TB/year for 2025 double-copy. Community Data folders can be granted larger allocations on application, and published data in the Data Commons can be larger. But the free self-serve number is 5 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: US NSF-funded, data mirrored at Arizona and TACC. Explicitly not an archive: 'The Data Store is not intended for permanent, archival storage.' | source: [1] | note: not stated
- egress: Free. IRODS-backed, anonymous public links for published data; the Data Commons is browsable without an account. | metered: no
- identity: email | detail: email
- interface: s3, rest, webdav, rclone
- limits:
  - write-gated (binding): Application, and published data in the Data Commons can be larger. But the free self-serve. [1]
- limits note: Free tier allocation is limited, and paid storage costs $125 per TB per year (approximately $10.40 per TB per month). Community Released Data folders require a current paid subscription.
- interface detail: rest
- tooling: iRODS with iCommands, plus a REST API and the Discovery Environment UI. Mature and scriptable, but the data model is iRODS rather than S3/WebDAV, so rclone needs the iRODS plugin rather than a stock backend.
- composes with: 5 GB per account is trivially repeatable in principle, but each account needs its own email and the allocation is tied to identity, so it does not compose into anything large without deliberate account farming. Community Data folders are the only legitimate multiplier and they are reviewed.
- reliability: US NSF-funded, data mirrored at Arizona and TACC. Explicitly not an archive: 'The Data Store is not intended for permanent, archival storage.'
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: 5 GB default for every account, explicitly for 'all domestic and international CyVerse account holders'. Above that it is paid: $125/TB/year single-copy up to 4 TB, $105/TB/year beyond, and $250/TB/year for 2025 double-copy. Community Data folders can be granted larger allocations on application, and published data in the Data Commons can be larger — but the free self-serve number is 5 GB.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $10.42/TB/month single-copy ($125/TB/yr), $8.75/TB/month above 4 TB, $20.83/TB/month double-copy.
- evidence:
  - [1] 2026-10-21: opened: 'All domestic and international CyVerse account holders receive a default allocation of 5GB of storage at no cost'; '$125 USD per TB per year for single-copy for up to 4TB'; 'For 2025, a flat rate of $250 USD/TB/year … (double-copy)'; 'The Data Store is not intended for permanent, archival storage.'
  - [1] 2026-10-21: same page, Community Released Data: 'The person requesting the Community Released Data Folder must have a current paid subscription to CyVerse (Reg, Pro, Commercial).'
- sources:
  - [1] https://cyverse.org/policies/data
