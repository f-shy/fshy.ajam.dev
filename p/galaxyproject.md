# Galaxy Europe

> galaxyproject.org | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/galaxyproject/ | JSON https://fshy.ajam.dev/api/v1/entity/galaxyproject.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Galaxy Europe

- `compute/galaxy-europe` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:45.575Z (live) | stale on 2026-12-05
- url https://galaxyproject.org/eu/storage/
- free tier: "On the European Galaxy server every user has a 250 GB quota. This means you can use 250 GB of storage for free." The storage is funded by the de.NBI cloud and the University of Freiburg compute centre, which held 4 PB of user data as of January 2025, and the page states the quota form for extra storage has been discontinued because storage "has become increasingly scarce and expensive". | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): the page states that at the limit no new jobs start. [1]
- limits note: the page states that at the limit no new jobs start.
- binding note: the same as limits note
- interface detail: REST API (Galaxy API), documented: the API documentation is at /api/docs or /api/redoc under the server base URL; the web interface is the other way in.
- tooling: BioBlend, the Python library for the Galaxy API (also blend4php, blend4j and a TypeScript schema); the REST API directly otherwise.
- composes with: Two independent Galaxy servers give two independent 250 GB quotas, because they are funded by different institutions and share no account system, so the pair composes to 500 GB of free storage for the same one email address and the same tool wrappers.
- reliability: no reliability event recorded
- notes: Recorded separately from Galaxy Main because the operator, the funder and the storage policy differ, and because the withdrawn quota form is a fact that applies only here. The compute behind the EU server is not quantified on the pages read, so vcpu and memory are null rather than copied from the US figures, which are TACC and Jetstream and do not describe this machine. A reader should treat 250 GB as long-term storage and note that short-term scratch storage and bring-your-own storage are offered as the route for larger jobs, which is what the page tells users to use instead of a quota increase.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-open-registration
- evidence:
  - [1] 2026-10-22: "On the European Galaxy server every user has a 250 GB quota. This means you can use 250 GB of storage for free", quoted
  - [1] 2026-10-22: "Thanks to the de.NBI cloud and the Uni-Freiburg compute center the European Galaxy server is managing 4PB of data today (2025/01)", quoted
  - [1] 2026-10-22: "we can no longer increase individual quotas through the quota-request form. The standard 250 GB quota therefore remains available to every user, but the quota-request form for additional storage has been discontinued", quoted
  - [1] 2026-10-22: "Once you reach this limit you cannot start new jobs", quoted
  - [2] 2026-11-03: every Galaxy server exposes a REST API documented at its /api/docs path | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [2] 2026-11-04: the Galaxy REST API documentation lives under each server base URL | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [3] 2026-11-04: BioBlend is the documented Python client for the Galaxy API | capture: sha256:9e170edbc1055deb78880e9c0ccd1f1cd14277c0066f155bbf2d9782c2c605ac | quote: BioBlend is a Python library for interacting with the Galaxy API.
- sources:
  - [1] https://galaxyproject.org/eu/storage/
  - [2] https://docs.galaxyproject.org/en/master/api_doc.html
  - [3] https://bioblend.readthedocs.io/en/latest/

## Galaxy Main

- `compute/galaxy-main` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:45.575Z (live) | stale on 2026-12-05
- url https://galaxyproject.org/main/
- free tier: "The main Galaxy site at https://usegalaxy.org [...] has been available since 2007 for anyone to analyze their data free of charge." "Anyone can use the public servers, with or without an account" and registration is "email, password, user name and go". A registered account gets 250 GB of storage and 6 concurrent jobs; an unregistered one gets 5 GB and 1 job. The hardware is not Galaxy's own: most jobs take 1 core and 8 GB on the dedicated Galaxy cluster at TACC, multi-core tools take 6 cores and 30 GB there or 10 cores and 30 GB on Jetstream m1.xlarge, and assembly jobs are routed to PSC Bridges (240 GB to 960 GB of memory, 5 to 20 cores, 24 to 96 hours) or TACC Stampede2 SKX (48 cores, 192 GB, 48 hours). | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): 250 GB of stored data per account is the wall that stops work: reaching it halts new jobs until data is purged, and the 6-concurrent-job cap and the 36 to 48 hour walltime sit behind it. [1]
- limits note: 250 GB of stored data per account is the wall that stops work: reaching it halts new jobs until data is purged, and the 6-concurrent-job cap and the 36 to 48 hour walltime sit behind it.
- binding note: the same as limits note
- interface detail: REST API (Galaxy API), documented: the API documentation is at /api/docs or /api/redoc under the server base URL; the web interface is the other way in.
- tooling: BioBlend, the Python library for the Galaxy API (also blend4php, blend4j and a TypeScript schema); the REST API directly otherwise.
- composes with: Galaxy provides access to TACC, Jetstream and PSC Bridges compute through tool wrappers without requiring a direct US institutional appointment.
- reliability: no reliability event recorded
- notes: Galaxy provides batch scientific analysis workflows rather than general-purpose virtual machines: no root access or arbitrary inbound networking.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-open-registration
  - facets.shape.vcpu: 10
  - facets.shape.ram_gib: 30
- evidence:
  - [1] 2026-10-22: "this site has been available since 2007 for anyone to analyze their data free of charge"; "Anyone can use the public servers, with or without an account", quoted
  - [1] 2026-10-22: "It is sustained by Texas Advanced Computing Center (TACC) hardware using allocation generously provided by the CyVerse project", quoted
  - [1] 2026-10-22: quota table: 250GB registered and 5GB unregistered, 6 concurrent jobs registered and 1 unregistered, quoted
  - [1] 2026-10-22: compute resource table: Jetstream 36 hour walltime, 10 cores, 30 GB; TACC Stampede2 SKX 48 hour walltime, 48 cores, 192 GB; PSC Bridges 240 GB to 960 GB and 5 to 20 cores, quoted
  - [2] 2026-10-22: "each registered account is granted 250 GB of quota space" at Galaxy Main, quoted
  - [3] 2026-11-03: every Galaxy server exposes a REST API documented at its /api/docs path | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [3] 2026-11-04: the Galaxy REST API documentation lives under each server base URL | capture: sha256:315b5f5c6f09dc7b9bf743f9413eab352f2d8b5f2336d9b70adedbbe05fe6179 | quote: The up-to-date Galaxy API documentation can be accessed by appending `/api/docs` or `/api/redoc` to the base URL of a Galaxy server
  - [4] 2026-11-04: BioBlend is the documented Python client for the Galaxy API | capture: sha256:9e170edbc1055deb78880e9c0ccd1f1cd14277c0066f155bbf2d9782c2c605ac | quote: BioBlend is a Python library for interacting with the Galaxy API.
- sources:
  - [1] https://galaxyproject.org/main/
  - [2] https://galaxyproject.org/support/account-quotas/
  - [3] https://docs.galaxyproject.org/en/master/api_doc.html
  - [4] https://bioblend.readthedocs.io/en/latest/
