# K-Cloud

> caveduck.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/caveduck/ | JSON https://fshy.ajam.dev/api/v1/entity/caveduck.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## K-Cloud

- `compute/k-cloud` | fails-identity | evidence reported | binding write-gated | category cloud VM
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-11-25T05:18:12.887Z (live) | stale on 2026-12-10
- url https://blog.caveduck.io/posts/modernbert-on-rebellions-npu/
- free tier: A published technical account states that the 'K-Cloud Project (MSIT · NIPA, 3 years from 2023)' builds a domestic-NPU cloud through a consortium of three CSPs and three chip makers, and that the 'High-Performance Computing Support Program (MSIT · NIPA, ~16.7B KRW in 2026): provides domestic NPU servers free of charge to selected demand companies'. 'Gabia, for instance, provides Rebellions ATOM-Max at no cost.' 'We too obtained 4× ATOM+ cards through one of these paths, in the form of KT Cloud’s AI Nexus (Backend.AI-based under the hood).' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: government-provisioned
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a company selected into a Korean government programme, not an individual signup: capacity goes to 'selected demand companies', and the one documented route to hardware is '4x ATOM+ cards through one of these paths, in the form of KT Cloud's AI Nexus', a rented cloud account. What the KT Cloud account itself requires (a card, a Korean phone number, a business registration number) is not stated in this record's evidence, and no hold, debit or prepaid term is stated.
- interface: unknown
- limits:
  - write-gated (binding): allocation is by selection as a demand company inside a national programme, so the gate is a legal entity in Korea plus a review, not a quota. [1]
- limits note: allocation is by selection as a demand company inside a national programme, so the gate is a legal entity in Korea plus a review, not a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The four cards arrived inside KT Cloud's AI Nexus, a rented cloud account with government funding behind it, and the compiler on top is free. It does not chain for a non-Korean individual: the free path exists only as a selection decision.
- reliability: no reliability event recorded
- notes: This is the largest free accelerator allocation that is not a trial, and it is unreachable for the reason every national allocation is. Confidence is reported because the primary sources are programme notices plus one operator account.
- extras:
  - facets.class: national-programme
  - facets.free_tier_kind: government-provisioned
  - facets.shape.gpu_class: Rebellions ATOM+ RBLN-CA22
  - facets.shape.gpu_count: 4
- evidence:
  - [1] 2026-10-22: published 2026-07-07: both programme descriptions, 'about 16.7B KRW in 2026', and 'We too obtained 4x ATOM+ cards through one of these paths, in the form of KT Cloud's AI Nexus', all quoted
  - [2] 2026-10-22: KT Cloud launched an NPU Server on Rebellions chips for public institutions, the first Korean NPUaaS provider with CSAP certification
  - [3] 2026-10-22: the RBLN SDK, compiler, runtime and a 300-model zoo are published for developers at no stated price
  - [1] 2026-11-25: a Korean government programme gives domestic NPU servers free of charge to selected demand companies | capture: sha256:5c4576e3014096ca59f858d07776ffb0a753e8dbe3bb972ab4987dd9db248f1a | quote: High-Performance Computing Support Program (MSIT · NIPA, ~16.7B KRW in 2026): provides domestic NPU servers free of charge to selected demand companies.
  - [1] 2026-11-25: the account still states that the programme supplies NPU servers free of charge to selected demand companies | capture: sha256:5c4576e3014096ca59f858d07776ffb0a753e8dbe3bb972ab4987dd9db248f1a | quote: High-Performance Computing Support Program (MSIT · NIPA, ~16.7B KRW in 2026): provides domestic NPU servers free of charge to selected demand companies.
- sources:
  - [1] https://blog.caveduck.io/posts/modernbert-on-rebellions-npu/
  - [2] https://en.sedaily.com/technology/2026/06/04/kt-cloud-launches-public-sector-npu-server-using-rebellions
  - [3] https://rebellions.ai/developers/
