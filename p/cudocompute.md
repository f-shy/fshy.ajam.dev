# Cudo Compute

> cudocompute.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cudocompute/ | JSON https://fshy.ajam.dev/api/v1/entity/cudocompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cudo Compute

- `compute/cudo-compute` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:26.530Z (live) | stale on 2026-12-04
- url https://www.cudocompute.com/pricing
- free tier: no free lane and no published rate. The pricing page is a commercial-models page: every accelerator row reads 'Quote on request' with an 'Enquire' button, from B300 and GB300 down to H100 PCIe. There is no signup form, no trial and no hourly price. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): there is no self-serve purchase: capacity is quoted through a sales enquiry, so a single person cannot open an account and start a GPU at all. [1]
- limits note: there is no self-serve purchase: capacity is quoted through a sales enquiry, so a single person cannot open an account and start a GPU at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: a quote-gated vendor cannot be chained with anything because there is no account to chain into.
- reliability: no reliability event recorded
- notes: Cudo was a self-serve marketplace of smaller GPU hosts with published hourly rates. The page read here is an enterprise commercial page, so the record is paid-only and the useful fact is the absence of a price, not a price. Anyone citing Cudo's old hourly figures is citing a page that no longer exists. Worth re-checking in a quarter: if self-serve returns, this record changes.
- extras:
  - facets.class: paid-gpu
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: 'Commercial models for enterprise AI infrastructure'; each product row carries 'Quote on request' and 'Enquire'; 'Explore flexible commercial models for dedicated GPU clusters and AI infrastructure', quoted
  - [2] 2026-10-22: the H100 product page carries no hourly rate in its 353 words, only a description of the architecture, observed
  - [3] 2026-10-22: homepage describes land, power and cluster commissioning for enterprise AI; no self-serve pricing
  - [3] 2026-10-22: page metadata dated 2026-03-17, so the current positioning is recent
  - [1] 2026-11-03: the pricing page lists B300, GB300, VR200, H100 PCIe, H100 SXM, H200, HGX B200 and GB200 NVL72, each at Quote on request with an Enquire button; it lists no A100, L40S, RTX 4090 or L4 and no hourly price for any card | capture: sha256:554ea23f068a87d130184f038aae96129b3e52b424f1bd39e6cda0a950adf984 | quote: ### H100 SXM 80GB HBM2e (3.35 TB/s bandwidth) Quote on request
- sources:
  - [1] https://www.cudocompute.com/pricing
  - [2] https://www.cudocompute.com/products/nvidia-h100
  - [3] https://www.cudocompute.com/
