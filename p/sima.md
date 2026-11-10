# SiMa.ai Edgematic

> sima.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sima/ | JSON https://fshy.ajam.dev/api/v1/entity/sima.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SiMa.ai Edgematic

- `compute/sima-ai-edgematic` | qualifies-with-caveat | evidence documented | binding retention-clamped | category cloud VM
- needs card yes, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.sima.ai/pages/overview/hello_sima/run_demos.html
- free tier: A free cloud lane onto SiMa.ai MLSoC and MLSoC Modalix silicon: 'Currently Edgematic is in beta and available for free on the Amazon Web Services (AWS) Marketplace. To obtain access, click link. To sign up, you will need an AWS account.' The architecture guide states the point: Edgematic 'provides a cloud-based, low-code environment where users can design, deploy, and benchmark pipelines', with 'No Hardware Requirements: Allows developers to test and optimize pipelines without purchasing a SiMa DevKit'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-beta-cloud
- per-object cap: not applicable | source: [1]
- retention: the beta is the clock and it has no committed end date; each run allocates one device and the job is a GStreamer pipeline, not a general compute job. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: an AWS account: 'Currently Edgematic is in beta and available for free on the Amazon Web Services (AWS) Marketplace... To sign up, you will need an AWS account', so the identity gate belongs to AWS rather than to SiMa. No evidence row states what AWS requires for that account - card, phone number or ID document - or whether any hold is taken: unknown. The record's notes record the card kind as an inference about AWS Marketplace subscriptions, not as a reading.
- interface: unknown
- limits:
  - retention-clamped (binding): the beta is the clock and it has no committed end date; each run allocates one device and the job is a GStreamer pipeline, not a general compute job. [1]
- limits note: the beta is the clock and it has no committed end date; each run allocates one device and the job is a GStreamer pipeline, not a general compute job.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Composes with an AWS account that exists for other reasons: the same account that runs a free-tier instance can subscribe at no stated cost. It breaks at the model boundary, because the pipeline must be a graph of compiled models, so arbitrary training is out of reach.
- reliability: no reliability event recorded
- notes: SiMa.ai Edgematic offers ML evaluation environments via AWS Marketplace. Account setup and billing follow standard AWS Marketplace subscription terms.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: free-beta-cloud
  - facets.shape.gpu_class: SiMa.ai MLSoC / MLSoC Modalix edge NPU
- evidence:
  - [1] 2026-10-22: 'Currently Edgematic is in beta and available for free on the Amazon Web Services (AWS) Marketplace... To sign up, you will need an AWS account', quoted
  - [2] 2026-10-22: 'provides a cloud-based, low-code environment where users can design, deploy, and benchmark pipelines' and 'No Hardware Requirements', quoted
  - [3] 2026-10-22: the workflow includes 'How to allocate a device for running the pipeline', so the accelerator is cloud-allocated
  - [4] 2026-10-22: 
- sources:
  - [1] https://docs.sima.ai/pages/overview/hello_sima/run_demos.html
  - [2] https://docs.sima.ai/pages/overview/target_architectures.html
  - [3] https://docs.sima.ai/pages/edgematic/introduction.html
  - [4] https://aws.amazon.com/marketplace/pp/prodview-a4upqs5h7v4la
