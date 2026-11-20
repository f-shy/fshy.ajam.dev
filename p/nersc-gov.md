# NERSC Exploratory

> nersc.gov | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nersc-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/nersc-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NERSC Exploratory

- `compute/nersc-exploratory` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.nersc.gov/users/become-a-nersc-user/working-with-us
- free tier: "Research projects that are new to NERSC and/or HPC may apply for small Exploratory awards, up to 250 node hours". Exploratory requests are accepted at any time, decided within four weeks of applying, and last 18 months. A Perlmutter CPU node is 2 AMD EPYC 7763 processors totalling 128 cores and 512 GB of memory, so 250 node-hours is 32,000 core-hours. The NERSC Director's Reserve, the other discretionary pool, is explicitly "not generally open to the public" and needs "prior arrangements with NERSC". | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: continuous-small-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): An Institutional User Agreement between Berkeley Lab and the PI's sponsoring organisation is required when the project is not federally (US) funded, so an unaffiliated applicant needs an organisation willing to sign a contract with a US national laboratory before any of the 32,000 core-hours exist. [1]
- limits note: An Institutional User Agreement between Berkeley Lab and the PI's sponsoring organisation is required when the project is not federally (US) funded, so an unaffiliated applicant needs an organisation willing to sign a contract with a US national laboratory before any of the 32,000 core-hours exist.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the clearest case in the file where the identity instrument is named rather than implied: an ORCID iD and an email get the account, and the Institutional User Agreement is the single document that stands between an unaffiliated person and 32,000 core-hours, so it composes only with an organisation willing to sign with Berkeley Lab.
- reliability: no reliability event recorded
- notes: The finding worth carrying is the refutation: NERSC's Director's Reserve is widely described as an open door and the vendor page says the opposite in one sentence, while the Exploratory award is the real small route and needs an agreement rather than a review panel. Foreign nationals are permitted under the appropriate use policy except in embargoed countries and on restricted party lists, which is a separate gate from the funding one.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: continuous-small-allocation
  - facets.shape.vcpu: 128
  - facets.shape.ram_gib: 512
  - facets.shape.gpu_class: NVIDIA A100 40 GB (Perlmutter GPU nodes)
- evidence:
  - [1] 2026-10-22: "Research projects that are new to NERSC and/or HPC may apply for small Exploratory awards, up to 250 node hours"; "exploratory and educational allocation requests may be submitted at any time"; decision "Within 4 weeks of applying (pending DOE approval for Exploratory)", quoted
  - [1] 2026-10-22: the DDR "is not generally open to the public" and "Proposals are accepted through ERCAP, but prior arrangements with NERSC are required", quoted
  - [2] 2026-10-22: CPU nodes carry 2x AMD EPYC 7763 with 64 cores per CPU and 512 GB of DDR4, quoted
  - [3] 2026-10-22: 3072 CPU-only Perlmutter nodes; 1794 GPU nodes with 1 EPYC 7763 and 4 NVIDIA A100 GPUs, 256 of them with 80 GB GPUs, quoted
  - [4] 2026-10-22: "An Institutional User Agreement between Berkeley Lab and the project's sponsoring organization (generally, the organization where the PI is employed) is required if the project is not federally (U.S.) funded", quoted
  - [5] 2026-10-22: "All NERSC users are required to have a valid ORCID id", quoted
- sources:
  - [1] https://www.nersc.gov/users/become-a-nersc-user/working-with-us
  - [2] https://docs.nersc.gov/systems/perlmutter/architecture/
  - [3] https://docs.nersc.gov/beginner-guide/nodetypesfig/
  - [4] https://iris.nersc.gov/aup
  - [5] https://iris.nersc.gov/add-pi
