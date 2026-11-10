# GoCloud

> gocloud.africa | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gocloud/ | JSON https://fshy.ajam.dev/api/v1/entity/gocloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GoCloud

- `compute/gocloud` | trial-only | evidence unverified | binding volume-quota | category cloud VM
- needs card unknown, phone no, ID no, institution no | verified 2026-11-06T15:56:55.347Z (live) | stale on 2026-11-21
- url https://gocloud.africa/
- free tier: Homepage badge row only: 'No credit card required $300 startup credits Free migration'. No page states the credit in a sentence, no expiry is published, and no signup form was reachable. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: not established: /signup, /register, /startups, /free-trial and /terms all return 116-word shells with no form, and the homepage's 'No credit card' claim cannot be tested without one
- interface: unknown
- limits:
  - volume-quota (binding): USD 300 of startup credits claimed on the homepage; expiry not stated [1]
- limits note: no credits page, no terms and no application form were reachable on 2026-10-23
- binding note: a USD 300 balance with no published expiry is the offer, but nothing establishes how to claim it
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 300 at USD 6 a month is 50 months of the smallest VM in nominal terms, but the credit is a trial balance with an unstated expiry, so the real composition is a few months of a Lagos-hosted box with 500 GiB of transfer.
- reliability: no reliability event recorded
- notes: The smallest published machine is the Basic VM at USD 0.00595/hour or USD 6.00 a month, 1 vCPU, 512 MiB, 10 GiB and 500 GiB of transfer, read on 2026-10-24 from gocloud.africa/services. The entry-tier figure is superseded by the named Basic VM. A vGPU line is listed with no price and no spec. The docs send API calls to api.gocloud.ng, a different TLD that did not answer. Not ranked.
- evidence note: the amount is a badge on the vendor's own homepage and the Basic VM price is quoted from /services; identity is the weakest field, because /signup and /pricing answer with the shared navigation and footer only and carry no form, so no registration gate was read and the rung stays unverified
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-23: quoted badge: 'No credit card required $300 startup credits Free migration'
  - [2] 2026-10-23: 200 with a 24-word shell; no prices
  - [3] 2026-10-23: 200 with a 116-word shell; no form
  - [4] 2026-10-24: quoted: 'From $6/month', 'Basic VM: $0.00595/hr' and '$6.00/mo', '1 vCPU 512 MiB Memory 10 GiB SSD Storage 500 GiB Transfer', 'vGPU Computing' listed with no price or spec
  - [1] 2026-11-06: the homepage badge row still carries the USD 300 startup credit | capture: sha256:fb5ba4598880ba5acf0b0e5282cc821a1b9d553055a22f407015fe0275aabba2 | quote: $300 startup credits
  - [4] 2026-11-06: the named Basic VM is still priced at USD 6.00 a month | capture: sha256:0aade3edec477a08e48df07389b5d40be10eaee3bbea8326257b68467841ee4f | quote: Basic VM: $0.00595/hr • $6.00/mo
  - [4] 2026-11-06: the Basic VM still carries 500 GiB of transfer | capture: sha256:0aade3edec477a08e48df07389b5d40be10eaee3bbea8326257b68467841ee4f | quote: 500 GiB Transfer
  - [3] 2026-11-06: /signup answers 200 with the shared navigation and footer only, 1,619 bytes and no form field, so no registration gate is readable | capture: sha256:e9ded85df8b912f70a587201ebfadb43653f80048b69593d1e8b56a88528f42f | quote: Get updates on new datacentres, features, and African cloud insights.
  - [2] 2026-11-06: /pricing answers with the footer only, no price and no form | capture: sha256:367def810c63080009edab288ec6c762629f73fec1f95ff818aed7eea9d9396a | quote: © 2024 GoCloud Africa. All rights reserved.
- sources:
  - [1] https://gocloud.africa/
  - [2] https://gocloud.africa/pricing
  - [3] https://gocloud.africa/signup
  - [4] https://gocloud.africa/services
