# Avian Compute

> avian.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/avian/ | JSON https://fshy.ajam.dev/api/v1/entity/avian.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Avian Compute

- `compute/avian-compute` | paid-only | evidence documented | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-06T18:39:12.192Z (live) | stale on 2026-12-07
- url https://avian.io/compute/
- free tier: No free tier and no credit on the compute page: every rate is per GPU-hour, prepaid for a whole term, on complete 8-GPU HGX nodes with a one-node minimum. B200 USD 4.32 per GPU-hour on a 12-month term, against USD 5.40 on 1 month and USD 3.42 on 36 months; B300 USD 4.95 on 12 months and USD 5.40 on 1 month. H100, A100 80 GB, L40S and L4: not listed; RTX 4090: not listed. | unit: hours | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits note: no transfer quota is stated. The binding term is the commitment: one 8-GPU HGX node minimum, prepaid for the whole term on a 730 hour per GPU per month basis, and the 1, 3 and 6 month rows are sold out, so the shortest term on offer is 12 months at USD 4.32 a GPU-hour for a B200.
- binding note: the commitment binds: a whole-term prepayment on at least eight cards, USD 302,746 upfront for a 12-month B200 node, in place of any quota the page states.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the provider description states it offers 'a range of AI models accessible via a single API key, billed on a pay-per-token basis or through long-term reservations'
- composes with: USD 4.32 per GPU-hour for a B200 with 180 GB is the cheapest Blackwell rate among evaluated providers, and it is also the least reachable: the commitment is twelve months on eight cards. An 8x B200 node at that rate is the machine for a training run that will not fit on a rented 48 GB card, not a machine for a single inference job, and the pay-per-token API on the same provider is the row to price for the small job.
- reliability: no reliability event recorded
- notes: The vendor page prices two cards, both as prepaid reservations on 8-GPU nodes: a 730 hour per GPU per month basis, a one-node minimum, the US region, and sales tax or VAT extra. The per-token inference API is a separate offer priced per million tokens.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 128
  - facets.shape.ram_gib: 2048
  - facets.shape.gpu_class: NVIDIA B200 180GB
  - facets.shape.gpu_count: 8
- evidence:
  - [2] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): [B200] | $4.32/hr | 180GB | 8x | 128 | 2048 GB | 10/21/2026, with the rows tags reading Reserved - 12mo' and 'North America'
  - [2] 2026-10-22: second row fields, transcribed and joined (unquoted values are not verbatim): [HGX B300] | $4.95/hr | 288GB | 8x | 192 | 4096 GB | 10/21/2026 with the same Reserved - 12mo and 'North America' tags; provider described as 'Avian Compute provides AI inference and dedicated GPU compute services through NVIDIA B200 and B300 HGX nodes'
  - [1] 2026-11-06: the B200 effective rate is USD 4.32 per GPU-hour on a 730 hour per month basis | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: Effective rate: $4.32/GPU·hr · 730 hr/mo basis
  - [1] 2026-11-06: the term table states the per-GPU-hour rate and the whole-term payment for each card | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: | 12 months | $4.32/GPU-hr$302,746 per node, whole term | $4.95/GPU-hr$346,896 per node, whole term |
  - [1] 2026-11-06: the billing unit is one GPU-hour prepaid for a whole term, with a one-node minimum | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: Sold as complete 8-GPU HGX nodes, one node minimum. All rates are per GPU, per hour, prepaid for the full term
  - [1] 2026-11-06: the 6-month term is sold out, so the shortest purchasable term is the 12-month row | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: | 6 months | $4.77/GPU-hr$167,141 per node, whole term | $5.15/GPU-hr$180,456 per node, whole term | Sold out |
  - [1] 2026-11-06: the 12-month B200 node is one upfront payment of USD 302,746 | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: $302,746 one payment, upfront
  - [1] 2026-11-06: the per-hour figure divides a whole-term payment over 730 hours a month | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: 730 hr/GPU/month basis
  - [1] 2026-11-06: the minimum order is one eight-GPU node | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: Sold as complete 8-GPU HGX nodes, one node minimum.
  - [1] 2026-11-06: the vendor page is the pricing page the numbers now come from | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: ## Dedicated B200 & B300, prepaid per term
  - [1] 2026-11-06: the term table has two GPU columns, B200 and B300, so no H100, A100 80 GB, L40S, RTX 4090 or L4 is priced | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: | Term | NVIDIA B200 | NVIDIA B300 | Request |
  - [1] 2026-11-06: every rate is per GPU-hour, prepaid for a whole term, on 8-GPU nodes | capture: sha256:f586c58853040b235bbda9e443ef6edd565cc966eb07dd4da170df114178db24 | quote: Sold as complete 8-GPU HGX nodes, one node minimum. All rates are per GPU, per hour, prepaid for the full term
- sources:
  - [1] https://avian.io/compute/
  - [2] https://computeprices.com/providers/avian
