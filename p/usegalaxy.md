# Galaxy Australia

> usegalaxy.org.au | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usegalaxy/ | JSON https://fshy.ajam.dev/api/v1/entity/usegalaxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Galaxy Australia

- `compute/galaxy-australia` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:20.287Z (live) | stale on 2026-12-05
- url https://site.usegalaxy.org.au/about
- free tier: "Galaxy Australia is one of the international UseGalaxy servers that provide a common core set of tools and reference genomes, and are open to anyone." A non-Australian registered account carries a 100 GB data hosting quota and a 365 day hosted data retention period; an account registered with an address from the Australian research institution list carries 600 GB. Anonymous users get 5 GB and lose it when the browser session expires, and cannot create workflows or share content. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): 100 GB of hosted data for a non-Australian account, with the data removed 365 days after upload, so a dataset held for a year is a dataset that disappears rather than a dataset that is billed. [1]
- limits note: 100 GB of hosted data for a non-Australian account, with the data removed 365 days after upload, so a dataset held for a year is a dataset that disappears rather than a dataset that is billed.
- binding note: the same as limits note
- interface detail: REST API, documented per server at /api/docs and /api/redoc, plus the Galaxy web interface
- tooling: BioBlend, the Python library for the Galaxy API (blend4php, blend4j and TypeScript bindings also exist)
- composes with: Three Galaxy servers now give three independent quotas for one email address: 250 GB at Galaxy Main, 250 GB at Galaxy Europe and 100 GB here, which is 600 GB of free hosted storage across three different national funders, with no shared account system and no card.
- reliability: no reliability event recorded
- notes: Compute quotas on Galaxy Australia are not published in documentation; only storage quotas are quantified.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-open-registration
- evidence:
  - [1] 2026-10-22: "Galaxy Australia is one of the international UseGalaxy servers that provide a common core set of tools and reference genomes, and are open to anyone", quoted
  - [1] 2026-10-22: quota table: 600 GB for Registered Australian Researchers, 100 GB for other registered accounts, 5 GB anonymous; hosted data retention 365 days for the two registered classes, quoted
  - [2] 2026-10-22: storage quota and retention table repeats 600 GB and 100 GB with a 1 year (52 weeks) data retention period, quoted
  - [3] 2026-10-22: registered user quota is 600 GB or 100 GB with 90 days from last activity as the retention trigger in this training table, quoted
  - [4] 2026-11-03: every Galaxy server exposes a REST API documented at its /api/docs path | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [4] 2026-11-04: REST API docs per server | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [5] 2026-11-04: BioBlend is the Python client | capture: sha256:9e170edbc1055deb78880e9c0ccd1f1cd14277c0066f155bbf2d9782c2c605ac | quote: [BioBlend](https://bioblend.readthedocs.io/) is a Python library for interacting with the [Galaxy](https://galaxyproject.org/) API.
- sources:
  - [1] https://site.usegalaxy.org.au/about
  - [2] https://usegalaxy-au.github.io/galaxy/data-policy.html
  - [3] https://galaxy-au-training.github.io/tutorials/modules/galaxy-data/
  - [4] https://docs.galaxyproject.org/en/master/api_doc.html
  - [5] https://bioblend.readthedocs.io/en/latest/
