# EGI Cloud Compute

> egi.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/egi/ | JSON https://fshy.ajam.dev/api/v1/entity/egi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EGI Cloud Compute

- `compute/egi-cloud-compute` | trial-only | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.egi.eu/services/cloud-compute/
- free tier: "Trial access: Try the service, prototype and validate applications and services. The EGI grant includes up to 4 vCPU cores, 8GB of RAM and 100GB of block storage." The service runs on the federated infrastructure of the EGI Federation and is part of the EGI EOSC Node offering, with standard API access to virtual machines carrying guaranteed resources. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): The trial is capped at 4 vCPU, 8 GB of RAM and 100 GB of block storage, and it is requested through a contact form rather than self-service, so a human decides when the grant starts and what it renews into. [1]
- limits note: The trial is capped at 4 vCPU, 8 GB of RAM and 100 GB of block storage, and it is requested through a contact form rather than self-service, so a human decides when the grant starts and what it renews into.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 4 vCPU / 8 GB / 100 GB VM is exactly the shape that fills the gaps other records leave: the HPC programmes here allocate wall-clock on a queue, and this gives an always-on address, so the pair composes into a control node that submits to a batch system and keeps state.
- reliability: no reliability event recorded
- notes: Duration and renewal terms for the trial are not published in documentation.
- extras:
  - facets.class: open-science-grid
  - facets.free_tier_kind: trial-grant
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 8
- evidence:
  - [1] 2026-10-22: "Trial access Try the service, prototype and validate applications and services. The EGI grant includes up to 4 vCPU cores, 8GB of RAM and 100GB of block storage", quoted
  - [1] 2026-10-22: "This service is part of the EGI EOSC Node service offering"
  - [1] 2026-10-22: custom access is described as "Long-term access, service level guarantees, dedicated support" and both routes point at the same service-contact form, quoted
- sources:
  - [1] https://www.egi.eu/services/cloud-compute/
