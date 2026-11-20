# Aethir

> dappatlas.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dappatlas/ | JSON https://fshy.ajam.dev/api/v1/entity/dappatlas.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aethir

- `compute/aethir` | fails-identity | evidence reported | binding write-gated | category GPU cloud
- needs card unknown, phone unknown, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://dappatlas.com/projects/aethir/
- free tier: No free lane for an individual. Access is by application: quoted, 'To use Aethir Cloud, you apply through the Cloud Customer Application Form, acquire ATH to pay for compute, then rent an Aethir Earth GPU server'. Credits appear only as partner grants, quoted from a partner page: 'Up to USD 10,000 in compute credits' for 'Selected Teams'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: access runs through the Cloud Customer Application Form plus prepaid ATH, so there is no self-service signup, and a real-name KYC check is a second gate that attaches to moving funds rather than to the form: 'KYC is required before claiming or withdrawing ATH from Aethir products', run through ComPilot and Sumsub. No card, hold, debit or prepaid term is stated, and whether the application form itself asks for an email, a phone or a document is not stated.
- interface: unknown
- limits:
  - write-gated (binding): The application form fails first, then KYC: withdrawal requires identity verification run through ComPilot and Sumsub, which is a real-name check that a registrant without verified identity cannot complete. [1]
- limits note: The application form fails first, then KYC: withdrawal requires identity verification run through ComPilot and Sumsub, which is a real-name check that a registrant without verified identity cannot complete.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. The USD 10,000 partner grant is recorded here so the subsequent evaluation can see the number beside the reason it is unreachable.
- reliability: no reliability event recorded
- notes: This is the door-not-number case required. Aethir advertises up to USD 10,000 in compute credits through partner ecosystems and a USD 100 million fund, which looks large in a roundup. Every named route to it is an application or a selection, and the account itself needs a real-name KYC before funds can move. The USD 10,000 is real and belongs to an institution, a named partner team, or nobody.
- extras:
  - facets.class: decentralized-gpu-cloud
  - facets.shape.gpu_class: H200-class enterprise; entry rate around USD 1.25 per hour
- evidence:
  - [1] 2026-10-22: quoted: access requires a Cloud Customer Application Form and prepaid ATH; 'KYC is required before claiming or withdrawing ATH from Aethir products'; KYC runs through ComPilot and Sumsub
  - [2] 2026-10-22: quoted: 'Up to USD 10,000 in compute credits' but only for 'Selected Teams' in a named partner ecosystem
  - [3] 2026-10-22: quoted: a USD 100 million Ecosystem Fund provides 'compute grants for promising AI agent projects', which is a selection process and not a signup offer
  - [4] 2026-10-22: independent listing states 'Free trial: No' and 'Free plan: No'
- sources:
  - [1] https://dappatlas.com/projects/aethir/
  - [2] https://builders.weatherxm.com/aethir
  - [3] https://ecosystem.aethir.com/blog-posts/ai-agent-development-powering-innovation-with-aethirs-100m-ecosystem-fund
  - [4] https://www.cubbie.com/products/aethir
