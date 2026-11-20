# Enterprise Compute Initiative

> disg.gov.sg | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/disg-gov-sg/ | JSON https://fshy.ajam.dev/api/v1/entity/disg-gov-sg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Enterprise Compute Initiative

- `compute/enterprise-compute-initiative` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.disg.gov.sg/eci/cloud-service-providers/
- free tier: A SGD 150 million programme that passes cloud credits through four providers to Singapore-based companies: AWS 'Up to S$350,000 in dedicated AI Springboard cloud credits and training, with support of up to S$600,000 through complementary AWS support programmes'; Microsoft 'Up to S$250,000 of Azure cloud credits ... with support of up to S$700,000 in services'; Oracle 'Up to S$250,000 per company through Oracle Cloud Universal Credits ... and up to S$1.9 million for enterprises that require private cloud infrastructure'; Google 'Up to S$200,000 worth of on-demand training licences and additional financial incentives'. Consultancy is separately capped at SGD 150,000 with 70 percent support up to SGD 105,000 per company. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: partner-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Eligibility requires 'A business entity registered or incorporated and is physically present in Singapore', 'Total organisation headcount based in Singapore should be at least 10 pax' and 'a tech team of 2 or more pax', so a sole founder fails the headcount test even after incorporating. [1]
- limits note: Eligibility requires 'A business entity registered or incorporated and is physically present in Singapore', 'Total organisation headcount based in Singapore should be at least 10 pax' and 'a tech team of 2 or more pax', so a sole founder fails the headcount test even after incorporating.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The four offers are alternatives rather than a sum: a company picks one CSP and its consultant partner, so the realistic ceiling is the AWS package at SGD 350,000 of credits rather than the SGD 850,000 that adding the four numbers suggests. The consultancy subsidy is separate and stackable with the credits, which is what makes the programme pay for the people as well as the compute.
- reliability: no reliability event recorded
- notes: A company cannot claim more than one CSP package: the programme pairs each participant with one CSP and its partners. The SGD 350,000 is plausibly a credit on a billing account: the text says 'dedicated AI Springboard cloud credits', though the AWS page is the authoritative source and was not read. Whether the 10-person headcount is waivable for a high-impact use case is unresolved: the baseline criteria are listed without an exception clause, but the assessment section is explicitly discretionary on use-case impact. The headcount rule is the highest personnel gate among the programmes read and it disqualifies a single-person operator.
- extras:
  - facets.class: government-credit
  - facets.free_tier_kind: partner-credit
  - facets.shape.gpu_class: provider-dependent (Amazon Bedrock, SageMaker, Azure, Oracle Cloud, Google Cloud)
- evidence:
  - [1] 2026-10-22: AWS 'Up to S$350,000 in dedicated AI Springboard cloud credits and training, with support of up to S$600,000'; Microsoft 'Up to S$250,000 of Azure cloud credits ... with support of up to S$700,000 in services'; Oracle 'Up to S$250,000 per company through Oracle Cloud Universal Credits', quoted
  - [1] 2026-10-22: Google Cloud AI CTO 'Up to S$200,000 worth of on-demand training licences and additional financial incentives', quoted
  - [2] 2026-10-22: 'set aside up to $150 million for the Enterprise Compute Initiative (ECI)'; 'The total supportable consulting cost is capped at S$150,000, with DISG supporting 70% of actual costs, capped at S$105,000 per company', quoted
  - [2] 2026-10-22: 'Total organisation headcount based in Singapore should be at least 10 pax'; 'The organisation should have a tech team of 2 or more pax'; 'A business entity registered or incorporated and is physically present in Singapore', quoted
  - [2] 2026-10-22: 'The programme will run for one year from the respective launch dates of each CSP, with multiple cohorts being deployed by different CSPs on a staggered timeline', quoted
- sources:
  - [1] https://www.disg.gov.sg/eci/cloud-service-providers/
  - [2] https://www.disg.gov.sg/enterprise-compute-initiative/
