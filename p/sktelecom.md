# SKT

> sktelecom.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sktelecom/ | JSON https://fshy.ajam.dev/api/v1/entity/sktelecom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SKT (Haein Cluster)

- `compute/skt-haein` | paid-only | evidence reported | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:22.537Z (live) | stale on 2026-11-18
- url https://www.sktelecom.com/
- free tier: No free tier and no published rate: contact-based pricing for a 1,000-plus NVIDIA B200 GPU cluster in Seoul, sold as 1-year or longer dedicated reservations for enterprise use. None of the H100, A100 80 GB, L40S, RTX 4090 or L4 is listed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: not applicable | source: [1]
- egress: not published on the pages read | metered: no | source: [1]
- identity: institution | detail: unverified: the signup terms are not published. The index states contact-based pricing, 1-year or long-term enterprise reservations and a consultation and sizing step before provisioning. | country: a business entity; the operator is in South Korea
- interface: unknown
- limits note: No quota is stated and no price is published: the offer is an enterprise reservation quoted by sales.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: unverified: the index describes a Petasus virtualisation layer and an AI Cloud Manager scheduler; no API or CLI is documented on the pages read.
- composes with: An enterprise-only Blackwell cluster with no public price; it is not a source for small or short runs.
- reliability: No reliability event was observed; the index notes the cluster is operated from Seoul with limited multi-region options and 24/7 enterprise support with Penguin Solutions.
- notes: Found via computeprices (listed as SKT (Haein Cluster)). The first-party press page confirms the cluster; the price claim rests on the index and is reported.
- evidence:
  - [1] 2026-11-03: the index records no public hourly price for SKT's Haein GPUaaS cluster | capture: sha256:b33c51ba642b57c6a53b23340e38a20fe2839b43e89c9cf9f7473e05364c5df3 | quote: SKT (Haein Cluster) does not publish public hourly pricing.
  - [1] 2026-11-03: the offer is a Blackwell B200 cluster; no H100, A100, L40S, RTX 4090 or L4 is listed | capture: sha256:b33c51ba642b57c6a53b23340e38a20fe2839b43e89c9cf9f7473e05364c5df3 | quote: SK Telecom's GPUaaS infrastructure featuring over 1,000 NVIDIA Blackwell B200 GPUs in a single cluster, powered by proprietary Petasus virtualization for isolated, flexible AI training environments.
  - [1] 2026-11-03: pricing is by contact; there is no self-service | capture: sha256:b33c51ba642b57c6a53b23340e38a20fe2839b43e89c9cf9f7473e05364c5df3 | quote: - Contact-based pricing — no self-service or published rates
  - [1] 2026-11-03: capacity is sold as 1-year or longer dedicated reservations for enterprise use | capture: sha256:b33c51ba642b57c6a53b23340e38a20fe2839b43e89c9cf9f7473e05364c5df3 | quote: Reserved Commitments 1-year or long-term dedicated resource reservations for enterprise use
  - [2] 2026-11-03: the first-party press release confirms the Haein GPUaaS cluster launched on 2025-08-01 | capture: sha256:7d1fc2935c65e956e1ac1dda61959aa5510b1e0a1d6afa4c6320ae59026c94b0 | quote: SK Telecom today marked the six-month anniversary of Haein, its GPU cluster built for GPUaaS, launched on August 1, 2025, designed to support large-scale AI workloads and the development of advanced AI models.
- sources:
  - [1] https://computeprices.com/providers/skt
  - [2] https://news.sktelecom.com/en/tag/haein
