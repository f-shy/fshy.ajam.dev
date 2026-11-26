# AirCloud

> aieev.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aieev/ | JSON https://fshy.ajam.dev/api/v1/entity/aieev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AirCloud

- `compute/aircloud` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-06T19:39:36.652Z (live) | stale on 2026-12-07
- url https://www.aieev.com/mwc-aieev
- free tier: Hourly GPU rental with published per-model rates: RTX 4090 24 GB at USD 0.51 an hour, RTX 5090 32 GB at USD 0.76, RTX PRO 6000 96 GB at USD 1.60, each also quoted as an annual figure (USD 4,497, 6,673 and 13,998). Payment is by prepaid credit, where 1 C equals KRW 1 of supply price in the Korean region, the minimum top-up is 10,000 C, VAT is added at 10 percent, and usage is metered in ten-minute intervals. Rentals of a month or more are discounted, up to 25 percent on annual terms. | unit: gpu-hours | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: payment is by prepaid credit before any workload runs: the billing documentation states purchases run from 10,000 C to 10,000,000 C, that 1 C equals KRW 1 of supply price in the Korean region, and that 10 percent VAT applies, so the minimum entry is KRW 10,000 plus VAT; the rail that funds the balance is not named, so whether a card is required rather than a bank transfer, whether debit or prepaid is accepted, and any authorisation hold are unknown, and the record does not state whether signup asks for an email, a phone or an ID document
- interface: unknown
- limits:
  - volume-quota (binding): The balance is the quota: when credit runs out the workload is terminated rather than suspended, and the minimum purchase is 10,000 C, so the practical entry cost is KRW 10,000 plus VAT rather than one hour of GPU time. [1]
- limits note: The balance is the quota: when credit runs out the workload is terminated rather than suspended, and the minimum purchase is 10,000 C, so the practical entry cost is KRW 10,000 plus VAT rather than one hour of GPU time.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At USD 0.51 an hour for a 24 GB card this is the cheapest verified GPU rate found among evaluated providers, and it composes with a Korean VPS: rent the 4090 by the hour, keep the data on a KRW 5,600 iwinv box, and pay nothing between jobs.
- reliability: no reliability event recorded
- notes: Two cautionary facts belong with the price: the Zero tier runs on hardware contributed by individuals and PC cafes, which is an availability risk rather than a capacity gain, and the terms state that training workloads may be throttled because the service is tuned for inference. The student programme seen in a forum post ended on 2026-05-31 and is not counted as a live free tier. Prices are quoted in USD on the vendor page while billing is in KRW credits, so a Korean buyer sees an exchange-rate exposure on every invoice.
- extras:
  - facets.class: gpu-hourly
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 58
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: the page lists RTX PRO 6000 at USD 1.60 an hour and USD 13,998.83 a year, RTX 5090 32GB at USD 0.76 an hour and USD 6,673.02 a year, and RTX 4090 24GB at USD 0.51 an hour and USD 4,497.03 a year, with a note that prices follow exchange rates
  - [2] 2026-10-22: the billing documentation states that credits carry the unit C, that 1 C equals KRW 1 of supply price in the Korean region, that purchases are between 10,000 C and 10,000,000 C, that 10 percent VAT applies, and that workloads may be terminated when credit is exhausted
  - [3] 2026-10-22: the instance table gives RTX 4070 Super as 12 GB VRAM with 9 GB system memory and 8 vCPUs, RTX 4090 as 24 GB with 58 GB and 8 vCPUs, RTX 5090 as 32 GB with 58 GB and 16 vCPUs, and RTX PRO 6000 as 96 GB with 58 GB and 16 vCPUs, and states that a small tier called AirCloud Zero uses infrastructure contributed by individuals and PC cafes
  - [4] 2026-10-22: a Korean PyTorch forum post from AIEEV advertises a student and research-lab programme giving 10,000 AU of credit at signup, with a deadline of 2026-05-31; that deadline has passed, so it is recorded as a closed promotion rather than a live one
  - [1] 2026-11-06: the vendor page still offers USD 20 of PoC credit | capture: sha256:f9e475ba2018e81da97ed57dd53d126399c6cb9e7ad34c0a08e6ffb2aee198e7 | quote: Start a small PoC with $20 free credits!
  - [1] 2026-11-06: the RTX 5090 32GB is USD 0.76 an hour | capture: sha256:f9e475ba2018e81da97ed57dd53d126399c6cb9e7ad34c0a08e6ffb2aee198e7 | quote: $0.76
  - [1] 2026-11-06: the RTX PRO 6000 is USD 1.60 an hour | capture: sha256:f9e475ba2018e81da97ed57dd53d126399c6cb9e7ad34c0a08e6ffb2aee198e7 | quote: $1.60
  - [1] 2026-11-06: the page prices three cards and sends any other GPU or NPU to a contact form | capture: sha256:f9e475ba2018e81da97ed57dd53d126399c6cb9e7ad34c0a08e6ffb2aee198e7 | quote: Looking for a specific GPU or NPU?
  - [1] 2026-11-06: the RTX 5090 32GB is priced at USD 0.76 per GPU-hour | capture: sha256:f9e475ba2018e81da97ed57dd53d126399c6cb9e7ad34c0a08e6ffb2aee198e7 | quote: $0.76 /hour
  - [3] 2026-11-06: the AirCloud Zero tier runs on hardware contributed by individuals, PC cafes and infrastructure partners | capture: sha256:690b7a2a98e6f41bc7cde7eb038699577e07b150ae9253ce3478b22ed705f8a3 | quote: Uses infrastructure contributed by individuals, PC cafés, and infrastructure partners.
- sources:
  - [1] https://www.aieev.com/mwc-aieev
  - [2] https://docs.aieev.com/docs/console/billing
  - [3] https://docs.aieev.com/docs/reference/infrastructure-and-resource-types
  - [4] https://discuss.pytorch.kr/t/gpu/10167
