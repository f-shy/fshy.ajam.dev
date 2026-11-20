# Fluence

> fluence.network | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fluence-2/ | JSON https://fshy.ajam.dev/api/v1/entity/fluence-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fluence

- `compute/fluence` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://fluence.network/
- free tier: A multi-provider neocloud selling CPU and GPU capacity through one console, advertising '2 vCPU, 2 GB RAM, 25 GB Storage' at USD 2.54 per month against Hetzner at USD 14.00 and DigitalOcean at USD 31.50, and an NVIDIA H200 at USD 2.80 per hour against CoreWeave at USD 6.30, with zero egress fees. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: unverified: no page stating the signup requirement was read; the record's evidence covers Fluence's self-published price comparison, the 404 at /pricing and the login wall on console.fluence.network. The record's binding note says the console requires an account, but states nothing about what creating one asks for
- interface: unknown
- limits:
  - volume-quota (binding): No free allowance is advertised anywhere on the public site; the console requires an account and the pricing path returns 404, so the real admission gate could not be read. [1]
- limits note: No free allowance is advertised anywhere on the public site; the console requires an account and the pricing path returns 404, so the real admission gate could not be read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At USD 2.54 per month for 2 vCPU and 2 GB this is the cheapest persistent small VM found among evaluated providers, which composes with a free control plane and the free inference lanes for model calls.
- reliability: no reliability event recorded
- notes: The comparison figures are Fluence's own and are documented only for Fluence; the peer prices are its claims and were not checked. Whether USD 2.54 is a floor, a promotional rate or a commitment is not stated. A free tier may exist behind signup and was not reachable.
- extras:
  - facets.class: paid-cloud
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
- evidence:
  - [1] 2026-10-22: self-published comparison: 2 vCPU/2 GB/25 GB at USD 2.54 per month versus Hetzner USD 14.00, DigitalOcean USD 31.50, AWS USD 53.50; H200 at USD 2.80 per hour versus CoreWeave USD 6.30
  - [2] 2026-10-22: returns 404 and redirects to fluence.ai, so no rate card or free tier is published at that path
  - [3] 2026-10-22: 
- sources:
  - [1] https://fluence.network/
  - [2] https://fluence.network/pricing
  - [3] https://console.fluence.network/
