# AceCloud

> acecloud.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/acecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/acecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AceCloud

- `compute/acecloud` | trial-only | evidence documented | binding volume-quota | category GPU cloud
- needs card yes, phone yes, ID no, institution no | verified 2026-11-03T07:36:20.827Z (live) | stale on 2026-12-04
- url https://acecloud.ai/cloud/gpu/
- free tier: No standing free tier. The L40S page says new customers can claim free credits, for example up to INR 20,000 in India or USD 200 globally, for a limited period; the credit is requested through a details form that sends access steps by email. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [2] | note: a machine record: the ceiling that matters is the flavour shape (vCPU, RAM, GPU count) listed in notes
- retention: not applicable | source: [3] | note: hourly billing stops when the server is deprovisioned; monthly plans bill for the whole month
- egress: AceCloud offers unmetered bandwidth and does not charge for data transfers. | metered: no | free allowance: unmetered | source: [3]
- identity: any-phone | detail: The account-creation form asks for first name, last name, a phone number verified by a one-time code ('Verify your phone number to continue'), email and password. Payment is by UPI, credit card or debit card for customers in India and by credit or debit card only for international customers. Whether a card must be on file before a GPU can be launched is unverified: behind a sign-up. Whether the phone check accepts a non-Indian number is unverified.
- interface: rest
- limits:
  - volume-quota (binding): the only free capacity is a one-off credit of up to INR 20,000 in India or USD 200 globally for a limited period, against a 1x H100 at INR 180,000 a month, a 1x A100 80GB at INR 90,000 a month and an L40S from INR 142.12 an hour [2]
- limits note: the credit is a trial amount that cannot carry a month of any datacenter card; the H100 has no hourly rate on the pricing table
- binding note: the same as limits note
- interface detail: the L40S page states instances launch through the AceCloud console or via API; the API was not probed
- tooling: a customer console at customer.acecloud.ai; the L40S page states instances can be launched 'through the AceCloud console or via API'. No client library or CLI is named on the pages read.
- composes with: GPU capacity is sold in INR with hourly billing on select cards (L40S from INR 142.12 an hour on-demand, L4 from INR 30 an hour on Spot) and monthly flavours for the datacenter cards. It composes with its own unmetered egress for jobs that move a lot of data; it does not give a free GPU beyond a one-off credit of up to INR 20,000 or USD 200.
- reliability: unverified: no status page or incident history was read
- notes: Per-card rates on the vendor's own pages, all in INR and excluding taxes. H100 80GB HGX: INR 180,000 a month for 1x (26 vCPU, 250 GB RAM), no hourly rate published (the Hourly column reads '---'). A100 80GB: INR 90,000 a month for 1x (16 vCPU, 128 GB RAM). L40S 48GB: INR 142.12 an hour 'starting at' on-demand, INR 83,000 a month for 1x (16 vCPU, 64 GB RAM). L4 24GB: INR 30 an hour 'starting at' on Spot (reclaimable), INR 36,730 a month for 1x (8 vCPU, 32 GB RAM). RTX 4090: not offered on the pages read. The Noida data center prices are shown; Mumbai, Atlanta and custom quotes are on the main pricing page. A third-party index (reported) lists the 1x L40S at USD 1.87 an hour. Egress is free and unmetered.
- evidence:
  - [2] 2026-11-03: the vendor GPU page lists a 1x NVIDIA H100 HGX 80GB instance (26 vCPU, 250 GB RAM) at INR 180,000 a month | capture: sha256:7e64c93575bc22fc1dfad5df6763cdb76cb7cd01a3c805d4e458ce8d14930034 | quote: 80GB | LLM training | 1× GPU · 26 vCPU · 250GB RAM | ₹180,000/mo Save ₹216,000 annually
  - [4] 2026-11-03: the H100 HGX pricing table has an Hourly column before the Monthly column and the 1x flavour shows '---' there, so no hourly H100 rate is published; monthly INR 180,000, 6-month INR 1,026,000, 12-month INR 1,944,000 | capture: sha256:b590aa40ec0a1744e4b6a8720efff696db1ce59b6d16b9fbb1722eaf816e2155 | quote: N.HGXH100.250 | 1x | 26 | 250 | --- | ₹180,000 | ₹1,026,000 | ₹1,944,000
  - [2] 2026-11-03: the vendor GPU page lists a 1x NVIDIA A100 80GB instance (16 vCPU, 128 GB RAM) at INR 90,000 a month | capture: sha256:7e64c93575bc22fc1dfad5df6763cdb76cb7cd01a3c805d4e458ce8d14930034 | quote: 80GB HBM2 | AI supercomputing | 1× GPU · 16 vCPU · 128GB RAM | ₹90,000/mo Save ₹108,000 annually
  - [2] 2026-11-03: the On-Demand GPUs block, 'Billed per hour, no commitment', starts the NVIDIA L40S at INR 142.12 an hour | capture: sha256:7e64c93575bc22fc1dfad5df6763cdb76cb7cd01a3c805d4e458ce8d14930034 | quote: NVIDIA L40S ₹142.12 /hr
  - [1] 2026-11-03: the L40S pricing table lists a 1x L40S (16 vCPU, 64 GB RAM) at INR 83,000 a month for the Noida data center, excluding taxes | capture: sha256:6f349f09a7afddac0a1012a34d2429be6d737b103a1776704f8cc0a278cae31a | quote: | N.L40S.64 | 1x | 16 | 64 | ₹83,000 |
  - [2] 2026-11-03: the Spot GPUs block ('Up to 67% below list rates', 'Can be reclaimed') starts the NVIDIA L4 at INR 30 an hour | capture: sha256:7e64c93575bc22fc1dfad5df6763cdb76cb7cd01a3c805d4e458ce8d14930034 | quote: NVIDIA L4 ₹30 /hr
  - [5] 2026-11-03: the L4 pricing table lists a 1x L4 (8 vCPU, 32 GB RAM) at INR 36,730 a month | capture: sha256:66060f7bcdd11aa77c4541007c8f8063758bb2ded2e8ef1c0944d33cd304913d | quote: | N.L4.32 | 1x | 8 | 32 | ₹36,730 |
  - [2] 2026-11-03: the GPU page names its hourly and monthly range as L4, A30, A100, H100 and H200; an RTX 4090 is not named | capture: sha256:7e64c93575bc22fc1dfad5df6763cdb76cb7cd01a3c805d4e458ce8d14930034 | quote: options ranging from L4 and A30 to A100, H100 and H200
  - [1] 2026-11-03: new customers can claim free credits of up to INR 20,000 in India or USD 200 globally for a limited period | capture: sha256:6f349f09a7afddac0a1012a34d2429be6d737b103a1776704f8cc0a278cae31a | quote: New customers can claim free credits (for example, up to ₹20,000 in India or $200 globally for a limited period)
  - [6] 2026-11-03: the account-creation form requires a phone number verified by a one-time code, alongside first name, last name, email and password | capture: sha256:92fc745bb159222c03438441620a3f5d85dcbdae2f5ca14cae70b280c3af447c | quote: Create account Verify your phone number to continue
  - [3] 2026-11-03: payment methods: UPI, credit and debit cards in India; credit and debit cards only for international customers | capture: sha256:7c03d4b366f18d13f1dd36f856536bcac380b9519ba42209a81abfe15e856676 | quote: For customers in India, we currently accept UPI, credit cards and debit cards. For international customers, we accept credit cards and debit cards only.
  - [3] 2026-11-03: bandwidth is unmetered and data transfer, ingress and egress, is not charged | capture: sha256:7c03d4b366f18d13f1dd36f856536bcac380b9519ba42209a81abfe15e856676 | quote: AceCloud offers unmetered bandwidth and does not charge for data transfers.
  - [7] 2026-11-03: a third-party price index lists the 1x L40S at USD 1.87 an hour, derived from the vendor's monthly rate | capture: sha256:c1574357488f65fa44697ed9f7df861860979f6164d52512fefb3f26ed8cf50b | quote: | $1.87/hr | 48GB | 1× | 16 | 64 GB | 11/3/2026 |
- sources:
  - [1] https://acecloud.ai/cloud/gpu/nvidia-l40s/
  - [2] https://acecloud.ai/cloud/gpu/
  - [3] https://acecloud.ai/pricing/
  - [4] https://acecloud.ai/pricing/linux/inr/noida/nvidia-h100-hgx/
  - [5] https://acecloud.ai/cloud/gpu/nvidia-l4/
  - [6] https://customer.acecloud.ai/v1/en/register
  - [7] https://computeprices.com/providers/acecloud
