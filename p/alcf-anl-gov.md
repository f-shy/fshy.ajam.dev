# ALCF Director's Discretionary

> alcf.anl.gov | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alcf-anl-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/alcf-anl-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ALCF Director's Discretionary

- `compute/alcf-director-s-discretionary` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.alcf.anl.gov/science/directors-discretionary-allocation-program
- free tier: A rolling award available year-round, usually three to six months, renewable, open to researchers from universities, industry and government agencies with no DOE sponsorship required, and also the documented route to the ALCF AI Testbed accelerators (Groq, Graphcore, SambaNova, Cerebras) via the same allocation request form. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / startup allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The DD award itself waives the institutional user agreement that INCITE, ALCC and OLCF DD all require, but the account application still asks for an employer and every non-US citizen must obtain DOE foreign-national authorisation through an ANL-593 request with passport and CV, so a person with no employer and no affiliation has nothing to put in the required field and no sponsor for the request. [1]
- limits note: The DD award itself waives the institutional user agreement that INCITE, ALCC and OLCF DD all require, but the account application still asks for an employer and every non-US citizen must obtain DOE foreign-national authorisation through an ANL-593 request with passport and CV, so a person with no employer and no affiliation has nothing to put in the required field and no sponsor for the request.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The AI Testbed variants are the unusual part: one rolling form reaches Groq, Graphcore, Cerebras and SambaNova, accelerator classes no cloud free tier offers. With one named institutional collaborator this becomes the cheapest entry to exascale-class silicon in earlier readings.
- reliability: no reliability event recorded
- notes: This is the single most valuable structural finding in the DOE stack: ALCF DD is the only tier found anywhere in this survey where the institutional user agreement is explicitly waived, which removes the signature that blocks INCITE and OLCF DD. What remains is an employer field and a DOE foreign-national authorisation (ANL-593) under DOE Order 142.3, which is a process rather than a contract. If a collaborating organisation can be named, ALCF DD is the lowest-friction route to an exascale-class GPU allocation that this survey found. ALCF publishes no node-hour range ('Award size: Small', 'The size of the award varies'), so the 20,000 node-hour figure belongs to OLCF and must not be carried across. The AI Testbed accelerators (Groq, Graphcore, Cerebras, SambaNova) are reached through the same rolling form and are the only route found to non-NVIDIA accelerator classes.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / startup allocation
  - facets.shape.gpu_class: Intel Data Center GPU Max (Aurora), NVIDIA A100 (Polaris), Groq/Graphcore/SambaNova/Cerebras (AI Testbed)
- evidence:
  - [1] 2026-10-22: 'Open to researchers from industry, academia, and government agencies, DD awards are available year-round on a rolling basis and are usually between three and six months in duration. The size of the award varies based on the application and its readiness/ability to scale', quoted
  - [1] 2026-10-22: 'DOE sponsorship is not required'; award size 'Small'; quarterly reports no; end-of-allocation reports no, quoted
  - [2] 2026-10-22: 'Researchers can now submit project proposals for the Groq, Graphcore, and Cerebras CS-3 platforms via the ALCF's Director's Discretionary program. There is no submission deadline', quoted
  - [3] 2026-10-22: 'User Agreement for INCITE, ALCC, and ADSP ... Note: This does not apply to Director's Discretionary awards', quoted; the Institution Master Agreement section carries the same exemption
  - [4] 2026-10-22: account request requires 'the name of your employer'; 'Foreign nationals must provide their passport number, their USCIS documents, and a PDF of their CV', quoted
- sources:
  - [1] https://www.alcf.anl.gov/science/directors-discretionary-allocation-program
  - [2] https://www.alcf.anl.gov/alcf-ai-testbed
  - [3] https://docs.alcf.anl.gov/account-project-management/project-management/starting-alcf-award/
  - [4] https://www.alcf.anl.gov/support-center/get-started/request-account
