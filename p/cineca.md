# CINECA ISCRA

> cineca.it | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cineca/ | JSON https://fshy.ajam.dev/api/v1/entity/cineca.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CINECA ISCRA

- `compute/cineca-iscra` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hpc.cineca.it/hpc-access/access-cineca-resources/iscra-projects/iscra-project-size/
- free tier: ISCRA Class C awards up to 10,000 GPU hours on Leonardo Booster over a maximum of nine months, and Class B up to 250,000 GPU hours or 3,600,000 core hours over 12 months; a try project is granted by email for about 10% of a Class C project and activated within 10 days. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: continuous small allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): ISCRA opens only to researchers affiliated to an Italian research organisation, with the PI expected to be affiliated to an Italian institution and the work performed at one, so nationality is irrelevant but the Italian affiliation is not. [1]
- limits note: ISCRA opens only to researchers affiliated to an Italian research organisation, with the PI expected to be affiliated to an Italian institution and the work performed at one, so nationality is irrelevant but the Italian affiliation is not.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The try project needs only an email and a UserDB registration, so it is the lowest-friction route to a Leonardo benchmark number found in evaluated benchmarks, but it composes into nothing without the Italian affiliation the Class C application then requires.
- reliability: no reliability event recorded
- notes: The try-project route is the closest thing to an email-only tier discovered anywhere in evaluated benchmarks: no form, no committee, about 10% of a Class C project (so roughly 1,000 Leonardo GPU hours), activated in 10 days. The Italian-affiliation gate appears in the general information page rather than in the try-project sentence, so a reconciler should read this as 'email-only request, but eligibility still Italian'. CINECA states it awards in excess of 500 million core processor hours nationally each year and about 1,700 million counting EuroHPC participation. The ISCRA pages return upstream_status 403 to automated retrieval while still serving content through the provider's cache, so the text is documented but the origin refused a direct read.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: continuous small allocation
  - facets.shape.gpu_class: NVIDIA A100 64 GB (Leonardo Booster)
- evidence:
  - [1] 2026-10-22: 'On LEONARDO BOOSTER: up to 10.000 GPU hours. Maximum duration of 9 months'; Class B 'up to 250.000 GPU hours on LEONARDO BOOSTER machine OR 3.600.000 CORE hours', quoted
  - [1] 2026-10-22: 'Try projects can be requested for new users at [address removed]'; 'activated within 10 days after the request. Average duration of try projects is two months and the amount of resources 10% of an ISCRA ClassC project', quoted
  - [2] 2026-10-22: 'The CINECA program is open to all scientific researchers affiliated to an Italian research organization'; 'Projects' Principal Investigators are expected to be affiliated to an Italian institution', quoted
  - [2] 2026-10-22: Class C proposals 'may be submitted at any time of the year, basing on a system of continuous submission' with monthly evaluation and allocation within 45 days, quoted
- sources:
  - [1] https://www.hpc.cineca.it/hpc-access/access-cineca-resources/iscra-projects/iscra-project-size/
  - [2] https://www.hpc.cineca.it/hpc-access/access-cineca-resources/iscra-projects/iscra-general-informations/
