# JSC Test

> fz-juelich.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fz-juelich/ | JSON https://fshy.ajam.dev/api/v1/entity/fz-juelich.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JSC Test

- `compute/jsc-test` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.fz-juelich.de/en/jsc/systems/supercomputers/call-for-applications-for-test-projects-with-jsc-supercomputing-and-support-resources
- free tier: Test projects grant a computing-time budget on JURECA, the JUWELS cluster or the JUPITER Booster for up to four months, optionally with about two person-weeks of expert support from a JSC Simulation and Data Lab, with applications accepted throughout the year. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / test allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Applications may be filed only by applicants employed at a university or research facility in Germany, so the nationality bar is zero and the German employment bar is absolute. [1]
- limits note: Applications may be filed only by applicants employed at a university or research facility in Germany, so the nationality bar is zero and the German employment bar is absolute.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The two person-weeks of SDL porting support is worth more than the node hours for a solo applicant, and it is the one JSC tier that would help a code become competitive, but it is behind German employment.
- reliability: no reliability event recorded
- notes: JSC publishes no core-hour figure for test projects: the page says 'a certain number of core-hours' and never quantifies it, so the field is null rather than guessed. The extended-support variant is the unusual offer, because a Simulation and Data Lab contributes staff time, which is the scarce input for a solo researcher. The explicit sentence that nationality is irrelevant while German employment is required is the cleanest statement of the binding constraint found in the German stack.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / test allocation
  - facets.shape.gpu_class: NVIDIA A100 (JURECA-DC, JUWELS Booster), GH200 (JUPITER)
- evidence:
  - [1] 2026-10-22: 'applications for test projects with or without extended support may be filed by applicants who are employed at a university or research facility in Germany (irrespective of the applicant's nationality)', quoted
  - [1] 2026-10-22: 'a period of up to four months'; 'Applications for test projects on JSC resources may be submitted throughout the year'; SDL support 'around 2 person-weeks per project', quoted
  - [2] 2026-10-22: 'Eligible are scientists with affiliations of German universities or research facilities. Here, the nationality of the applicant is irrelevant'; 'Test access to JUWELS for the preparation of Regular Project applications is available', quoted
- sources:
  - [1] https://www.fz-juelich.de/en/jsc/systems/supercomputers/call-for-applications-for-test-projects-with-jsc-supercomputing-and-support-resources
  - [2] https://www.john-von-neumann-institut.de/en/links/gcs-nic-computing-time-projects
