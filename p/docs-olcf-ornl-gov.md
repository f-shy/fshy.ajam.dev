# OLCF Director's Discretionary

> docs.olcf.ornl.gov | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs-olcf-ornl-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/docs-olcf-ornl-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OLCF Director's Discretionary

- `compute/olcf-director-s-discretionary` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.olcf.ornl.gov/accounts/accounts_and_projects.html
- free tier: The OLCF Director's Discretionary program allocates approximately 10% of the available Frontier hours in a calendar year, and a typical DD project is awarded between 15,000 and 20,000 node hours, applied for at any time and lasting up to 12 months. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / startup allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The PI must sign a PI Agreement, pass an ORNL export-control review and a Personnel Access System check, and have a User Agreement executed between UT-Battelle and the PI's institution, so a person with no institution has nothing to sign with. [1]
- limits note: The PI must sign a PI Agreement, pass an ORNL export-control review and a Personnel Access System check, and have a User Agreement executed between UT-Battelle and the PI's institution, so a person with no institution has nothing to sign with.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A DD award is the documented way to obtain the scaling data that an INCITE proposal requires, so it converts into the INCITE door rather than replacing it.
- reliability: no reliability event recorded
- notes: This is the highest-value low-friction tier found: 15,000 to 20,000 Frontier node-hours at 8 GCDs per node is roughly 120,000 to 160,000 GPU-hours and 960,000 to 1,280,000 core-hours per award. The GPU-hour conversion is arithmetic from the quoted node composition and the quoted node-hour range, not a vendor figure, so the node-hour numbers are documented and the converted ones are inferred. OLCF states there is no DOE sponsorship requirement. The barrier is institutional signature plus export control, not scientific merit at INCITE scale. A foreign national participant triggers an ORNL PAS request that takes 15 to 35 days.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / startup allocation
  - facets.shape.vcpu: 64
  - facets.shape.ram_gib: 512
  - facets.shape.gpu_class: AMD MI250X (8 GCDs per node)
  - facets.shape.gpu_count: 8
- evidence:
  - [1] 2026-10-22: 'The OLCF Director's Discretionary (DD) program allocates approximately 10% of the available Frontier hours in a calendar year. Frontier is allocated in node hours, and a typical DD project is awarded between 15,000 - 20,000 node hours', quoted
  - [1] 2026-10-22: Frontier node composition: 1x 64-core AMD EPYC CPU, 512 GB DDR4, 4x AMD MI250X each with 2 GCDs for 8 GCDs per node at 64 GB HBM2E, quoted
  - [1] 2026-10-22: 'A User Agreement/Appendix A or Subcontract must be executed between UT-Battelle and the PI's institution', quoted; also PI Agreement signed and ORNL PAS entry
  - [2] 2026-10-22: 'Director's Discretionary Allocation: Allocations (up to 20,000 node hours of compute time) for high impact science and engineering problems that exceed a company's internal computing capabilities', quoted
  - [1] 2026-10-22: DD applications accepted at any time, duration up to 12 months, no quarterly reports outside industry; reviewed by the OLCF Resource Utilization Council and independent referees
- sources:
  - [1] https://docs.olcf.ornl.gov/accounts/accounts_and_projects.html
  - [2] https://www.olcf.ornl.gov/about-olcf/accel/
