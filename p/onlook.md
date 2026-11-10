# Onlook

> onlook.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onlook/ | JSON https://fshy.ajam.dev/api/v1/entity/onlook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Onlook

- `compute/onlook` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.onlook.com/pricing
- free tier: Onlook "Free" is a download, not a hosted allowance: "Download Onlook and start designing in your code", and "For the hosted cloud version, please contact our team or book a demo", quoted | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-product
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous | detail: anonymous for the free form: the Free card is 'Download Onlook and start designing in your code' with no usage allowance, and 'Yes, Onlook can be self-hosted for free on GitHub', so no account is created and no identity is checked. The hosted cloud lane publishes no signup at all - 'please contact our team or book a demo' - so what it would require is unknown. No card, hold, phone number or ID document is stated.
- interface: unknown
- limits:
  - write-gated (binding): the hosted lane has no self-serve price at all, so the only free path is running the desktop app locally. [1]
- limits note: the hosted lane has no self-serve price at all, so the only free path is running the desktop app locally.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The open-source build can be deployed on self-hosted or remote infrastructure, but as sold it provides no hosted compute and no allowance.
- reliability: no reliability event recorded
- notes: The repository has 26.0k stars on the page's own count.
- self hosted: yes
- extras:
  - facets.class: paid
  - facets.free_tier_kind: free-product
- evidence:
  - [1] 2026-10-22: the Free card is "Download Onlook and start designing in your code" with no usage allowance, quoted
  - [1] 2026-10-22: "Yes, Onlook can be self-hosted for free on GitHub. For the hosted cloud version, please contact our team or book a demo." quoted
- sources:
  - [1] https://www.onlook.com/pricing
