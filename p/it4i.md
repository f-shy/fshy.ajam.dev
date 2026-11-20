# IT4Innovations Open Access

> it4i.cz | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/it4i/ | JSON https://fshy.ajam.dev/api/v1/entity/it4i.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IT4Innovations Open Access

- `compute/it4innovations-open-access` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.it4i.cz/en/for-users/open-access-competition
- free tier: The 39th Open Access Grant Competition distributes up to 956,000 Karolina CPU node-hours, 103,000 Karolina GPU node-hours, 149,000 LUMI-C and 155,000 LUMI-G node-hours, plus 1,982,000 QPU seconds on the VLQ quantum computer, with each request capped at 10 percent of the resource, so a single request may ask for 95,600 Karolina CPU node-hours, 10,300 Karolina GPU node-hours, 15,500 LUMI-G node-hours or 198,200 QPU seconds. It runs three times a year, in February, June and October. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-competitive-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): "Eligible applicant: Employee of a Czech research organisation", so the 10,300 Karolina GPU node-hours, which is 82,400 A100-hours at eight GPUs per node, are closed to anyone without Czech employment. [1]
- limits note: "Eligible applicant: Employee of a Czech research organisation", so the 10,300 Karolina GPU node-hours, which is 82,400 A100-hours at eight GPUs per node, are closed to anyone without Czech employment.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The quantum allocation is the unusual component: 198,200 QPU seconds on the VLQ machine in one request is several orders of magnitude beyond the three-job queue that Quantum Inspire offers, which makes this the only route in the file to sustained quantum time, and it is closed on nationality of employment rather than on merit.
- reliability: no reliability event recorded
- notes: The per-request cap is what makes this record worth carrying: 10,300 Karolina GPU node-hours at eight A100s per node is 82,400 A100-hours, computed here from the two published figures, which is roughly thirteen times the 6,250 A100-hours an ACCESS Explore allocation buys. Note the eligibility sentence says employee of a Czech research organisation rather than Czech national, which is a weaker gate than several national centres impose and is worth rechecking for any applicant who holds an EU appointment.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: recurring-competitive-allocation
  - facets.shape.gpu_class: NVIDIA A100 40 GB (Karolina, 8 per node)
  - facets.shape.gpu_count: 8
- evidence:
  - [1] 2026-10-22: 39th call resources: Barbora NG 203,000 node hours with a 20,300 maximum per request; Karolina CPU 956,000 with 95,600; Karolina GPU 103,000 with 10,300; LUMI-C 149,000 with 14,900; LUMI-G 155,000 with 15,500; VLQ 1,982,000 QPU seconds with 198,200, quoted
  - [1] 2026-10-22: "Eligible applicant: Employee of a Czech research organisation", quoted
  - [1] 2026-10-22: Karolina has 720 compute nodes without accelerators and 72 nodes with 8x NVIDIA A100 GPU accelerators of 40 GB HBM2; LUMI-G nodes carry one 64-core AMD Trento CPU and four AMD MI250X GPUs, quoted
  - [2] 2026-10-22: the same competition is announced three times a year and reports up to 10 percent of node hours of each resource available per request, quoted
  - [1] 2026-10-22: new applicants without prior experience must first apply through Fast Track Access, quoted
- sources:
  - [1] https://www.it4i.cz/en/for-users/open-access-competition
  - [2] https://metavo.metacentrum.cz/en/news/novinka_2025_0010.html
