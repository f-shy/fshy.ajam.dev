# Bentaus

> bentaus.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bentaus/ | JSON https://fshy.ajam.dev/api/v1/entity/bentaus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bentaus

- `compute/bentaus` | paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-06T18:39:12.193Z (live) | stale on 2026-12-07
- url https://www.bentaus.com/nvidia-b300
- free tier: no free tier and no credit on the B300 page: capacity is sold on demand at USD 6.50 to 8.50 per GPU-hour, reserved at USD 4.35 to 6.50, or as a custom AI factory. H100 is named in the page's spec comparison with no rate; A100 80 GB, L40S, RTX 4090 and L4: not listed. | unit: none | metered on: wall-clock | read on: 2026-11-06 | source: [1]
- per-object cap: not applicable | source: [1] | note: the unit is an 8-GPU node
- retention: not applicable | source: [1] | note: a machine record
- egress: not published on the pages read: no egress term was found, so nothing is asserted | metered: no | source: [1]
- identity: email | detail: unverified: the contact page is an email address and the Order Now control leads to an order form that was not readable; no card, phone or ID requirement is published, and whether a company is required is not stated. `email` is the lowest kind that reaches a sales contact.
- interface: unknown
- limits:
  - write-gated (binding): orders go through an order form and a solutions architect; the node is 8 GPUs, B300 on-demand is a range of USD 6.50 to 8.50 per GPU-hour, and no H100, A100, L40S, RTX 4090 or L4 rate is published [1]
- limits note: sales-gated 8-GPU nodes only
- binding note: the same as limits note
- interface detail: no console, API or CLI is documented on the pages read; ordering is a form and a sales contact
- tooling: not stated: the pages read document no client; orders go through an order form and a solutions architect
- composes with: An 8-GPU B300 or MI325X node is the smallest unit; the per-GPU-hour rate is published as a range. It does not offer single-GPU or older-generation cards on the pages read, so it does not serve a small job.
- reliability: unverified: no status page or incident history was read; capacity is described as available now on the B300 page
- notes: The AMD Instinct MI325X is sold on its own page at USD 2.25 per GPU-hour on demand and USD 1.95 reserved, as an 8-GPU node. A100 80 GB, L40S, RTX 4090 and L4 are not named on either page; H100 appears only in the B300 page's spec comparison, with no rate. A third-party index reports the minimum order as one eight-GPU node.
- evidence:
  - [1] 2026-11-03: on-demand B300 is USD 6.50 to 8.50 per GPU-hour | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: $6.50 - $8.50 / GPU hour NVIDIA B300 Blackwell Ultra
  - [1] 2026-11-03: reserved B300 is USD 4.35 to 6.50 per GPU-hour | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: $4.35 - $6.50 /GPU hour
  - [2] 2026-11-03: on-demand MI325X is USD 2.25 per hour per GPU, reserved USD 1.95 per GPU-hour | capture: sha256:f2bb4df07932b4e7cd856a8a57ad74ae3285892908da44dd22285003e7838524 | quote: $2.25 On-Demand Access · MI325X · Per Hour
  - [1] 2026-11-03: the B300 is sold as an 8-GPU node | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: 8x GPU NODE, Bandwith, 8 TB/s, HBM3E, 288 GB
  - [1] 2026-11-03: deployment goes through a solutions architect | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: Our solution architects are ready to help you design, configure, and deploy now.
  - [3] 2026-11-03: the contact page is an email address with no form fields or signup | capture: sha256:2b197d8218ab544c4e29caf79aa988ed438e4c6361d79f44aa5150d1e888cd42 | quote: Whether you're ready to build or simply exploring what's possible, reach out and our team will respond promptly.
  - [4] 2026-11-03: a third-party index states the minimum order is one eight-GPU node, provisioned through sales | capture: sha256:574dcde089c58fc535a8bbb902a39023ba3233824af6c4391c676fedf5ae1cf2 | quote: Orders start at one eight-GPU node and are provisioned through a solutions architect rather than a self-service console.
  - [1] 2026-11-06: on-demand B300 is USD 6.50 to 8.50 per GPU-hour | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: #### $6.50 - $8.50 / GPU hour NVIDIA B300 Blackwell Ultra
  - [2] 2026-11-06: the MI325X page states USD 2.25 per GPU-hour on demand, and USD 1.95 reserved, on its own page | capture: sha256:f2bb4df07932b4e7cd856a8a57ad74ae3285892908da44dd22285003e7838524 | quote: #### $2.25 On-Demand Access · MI325X · Per Hour
  - [1] 2026-11-06: reserved B300 is USD 4.35 to 6.50 per GPU-hour | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: $4.35 - $6.50 /GPU hour
  - [2] 2026-11-06: the MI325X on-demand rate is USD 2.25 per GPU-hour on the MI325X page | capture: sha256:f2bb4df07932b4e7cd856a8a57ad74ae3285892908da44dd22285003e7838524 | quote: #### $2.25 On-Demand Access · MI325X · Per Hour
  - [1] 2026-11-06: the B300 on-demand range is unchanged | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: $6.50 - $8.50 / GPU hour
  - [1] 2026-11-06: H100 is named in the page's spec comparison, and no rate is attached to it | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: ## HGX B300 vs H200 vs H100
  - [1] 2026-11-06: the B300 page prices on-demand B300 at USD 6.50 to 8.50 per GPU-hour | capture: sha256:0420099156ad4fed9e6d6da300edb26bdd463f8ce995f36529644217dd130f55 | quote: #### $6.50 - $8.50
- sources:
  - [1] https://www.bentaus.com/nvidia-b300
  - [2] https://www.bentaus.com/amd-mi325x
  - [3] https://www.bentaus.com/contact
  - [4] https://computeprices.com/providers/bentaus
