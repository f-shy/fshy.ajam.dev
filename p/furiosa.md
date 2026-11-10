# FuriosaAI Furiosa Access

> furiosa.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/furiosa/ | JSON https://fshy.ajam.dev/api/v1/entity/furiosa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FuriosaAI Furiosa Access

- `compute/furiosaai-furiosa-access` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://furiosa.ai/request-access
- free tier: Hands-on RNGD evaluation exists and is gated by a sales form: the request page offers 'BARE METAL - Access dedicated RNGD hardware in a nearby data center to run your workloads' and 'API ENDPOINT - Connect your applications to RNGD-hosted models through APIs provided by our cloud partners', under the heading 'Start testing today', with the form requiring 'First name', 'Last name' and 'Business email' and a 'Talk to sales' link. No price, no trial duration, no allocation size and no self-serve signup is published. The vendor's own description of the programme is that it 'provides structured pathways for customers and partners to evaluate, integrate, qualify, and deploy Furiosa accelerators'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: sales-evaluation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): the gate is a business email and a sales conversation before any hardware is allocated; nothing about quota binds earlier because no quota is published. [1]
- limits note: the gate is a business email and a sales conversation before any hardware is allocated; nothing about quota binds earlier because no quota is published.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The API endpoint route chains with any OpenAI-compatible client once a partner host is chosen, which is the cheapest way to benchmark a RNGD endpoint. It does not chain into free capacity: every route ends in a sales contact or a marketplace subscription.
- reliability: no reliability event recorded
- notes: Documented so the subsequent evaluation does not read 'Start testing today' as a free tier. The hardware is real and the evaluation is free of charge in the sense that no price is quoted, but the door is a form and a call, and nothing about the size of the allocation is published. The compiler and developer documentation at developer.furiosa.ai are open and free, which is the part an individual can use without the gate.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: sales-evaluation
  - facets.shape.gpu_class: Furiosa RNGD PCIe inference accelerator, 180 W
- evidence:
  - [1] 2026-10-22: the request form requires a 'Business email' field and the page carries a 'Talk to sales' link, both read
  - [1] 2026-10-22: 'BARE METAL - Access dedicated RNGD hardware in a nearby data center to run your workloads' and 'API ENDPOINT - Connect your applications to RNGD-hosted models', quoted
  - [2] 2026-10-22: 'Furiosa Access Program provides structured pathways for customers and partners to evaluate, integrate, qualify, and deploy Furiosa accelerators', quoted
  - [3] 2026-10-22: a Furiosa Inference Cloud listing on Azure Marketplace serves pre-compiled Llama 3.1 models on RNGD, so the paid distribution route is a normal marketplace subscription
- sources:
  - [1] https://furiosa.ai/request-access
  - [2] https://lp.furiosa.ai/furiosa-access-program
  - [3] https://marketplace.microsoft.com/ms-my/product/saas/furiosa.furiosa-rngd-inference?tab=overview
