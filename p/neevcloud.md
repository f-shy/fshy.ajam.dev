# NeevCloud

> neevcloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neevcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/neevcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeevCloud

- `compute/neevcloud` | trial-only | evidence documented | binding retention-clamped | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.neevcloud.com/
- free tier: 'Sign up today and claim INR 2,000 in FREE CPU Cloud credits, valid for 7 days', and for the GPU side 'When you sign up on NeevCloud, your account is credited with 10 free credits to help you explore and deploy your first GPU instance'. The sibling product NeevCode advertises 'No credit card', 'Free GPU-min daily' and 'Free to start' on India-sovereign infrastructure. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: The CPU credit burns in 7 days and covers CPU only, while the GPU lane gives 10 credits with no published rate, so the two halves never meet: a GPU instance cannot be run on the INR 2,000 and the CPU credit expires before a training job finishes. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account is needed to claim the credit ('Sign up today and claim 2,000 in FREE CPU Cloud credits'), and no card is claimed on the free path: the sibling product's page states 'No credit card', which is a statement about NeevCode rather than about the NeevCloud signup form. The signup fields are not quoted, so the email requirement is inferred rather than read. No hold, debit or prepaid term is stated. Whether a company registration or an Indian number is asked for is not stated in the evidence read.
- interface: rest
- limits:
  - retention-clamped (binding): The CPU credit burns in 7 days and covers CPU only, while the GPU lane gives 10 credits with no published rate, so the two halves never meet: a GPU instance cannot be run on the INR 2,000 and the CPU credit expires before a training job finishes. [1]
- limits note: The CPU credit burns in 7 days and covers CPU only, while the GPU lane gives 10 credits with no published rate, so the two halves never meet: a GPU instance cannot be run on the INR 2,000 and the CPU credit expires before a training job finishes.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 7-day INR 2,000 CPU credit is enough to stand up an API service in an Indian region and measure latency from there, and that is the only thing it is good for: it cannot pay for the GPU that would make the region interesting.
- reliability: no reliability event recorded
- notes: India's GPU lane mostly fails on company registration, and this is the exception that still fails on arithmetic. The 10 GPU credits are the part worth watching because NeevCloud does not publish a credit-to-rupee rate on the wallet page, so the real GPU allowance is unknown until an account exists; a reader who signs up learns it in the confirmation email, which the credit-system doc says carries 'Credit amount', 'Eligible products' and 'Expiry date'. The H100 trial is a POC conversation, not a tier. Verified versus reported: the INR 2,000 figure is the vendor's own sentence, and the 10 credits are the vendor's own documentation; neither was probed.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: trial-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the site states 'Sign up today and claim 2,000 in FREE CPU Cloud credits, valid for 7 days', quoted, read search index because the landing page served no text to the reader
  - [2] 2026-10-22: 'When you sign up on NeevCloud, your account is credited with 10 free credits to help you explore and deploy your first GPU instance', and 'Each running instance deducts credits hourly, based on its pricing plan (On-Demand or Reserved)', quoted
  - [3] 2026-10-22: NeevCode's own claims: 'No credit card', 'Free GPU-min daily', 'Data stays in India', quoted
  - [4] 2026-10-22: H100 clusters at 'USD 2.99' per GPU-hour on demand with 'Free Trial available for H100 GPU Clusters. Contact Us Now', which is a sales conversation rather than a self-serve tier, quoted
- sources:
  - [1] https://www.neevcloud.com/
  - [2] https://docs.ai.neevcloud.com/getting-started/billing-wallet
  - [3] https://code.neevcloud.com/
  - [4] https://www.neevcloud.com/gpu-cluster/
