# NeevCloud

> neevcloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neevcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/neevcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeevCloud

- `compute/neevcloud` | trial-only | evidence documented | binding retention-clamped | category GPU cloud
- needs card no, phone no, ID yes, institution no | verified 2026-11-25T05:18:13.619Z (live) | stale on 2026-12-26
- url https://www.neevcloud.com/
- free tier: When you sign up on NeevCloud, your account is credited with 10 free credits to help you explore and deploy your first GPU instance. As you begin using resources, credits are deducted automatically based on your instance's hourly usage until the free balance is exhausted. You can then recharge your wallet anytime to continue using services. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: The CPU credit burns in 7 days and covers CPU only, while the GPU lane gives 10 credits with no published rate, so the two halves never meet: a GPU instance cannot be run on the INR 2,000 and the CPU credit expires before a training job finishes. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: The sign-up page shows four steps: Email, Mobile, KYC, Password, and states 'No credit card required to start' alongside '₹15,000 free credits — valid 7 days after you sign up'. Credits apply instantly after verification. A card, bank or UPI payment is needed only when adding funds to the wallet.
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
  - [2] 2026-11-25: signup grants 10 free credits for the first GPU instance | capture: sha256:57a8ebc1ab1e8ac1ae8f6711ddddeb80167aaab2bc214ce24513116dc1e1490b | quote: When you sign up on NeevCloud, your account is credited with 10 free credits to help you explore and deploy your first GPU instance.
  - [5] 2026-11-24: the current sign-up page advertises INR 15,000 in free credits valid for seven days | capture: sha256:855ce760067441d3c9655100ac73056c4cc73f7277fd95b61d540dc47ba0ed39 | quote: Claim <span class="font-bold text-[#007a65]">₹15,000 free credits</span> — valid 7 days after you sign up.
  - [2] 2026-11-24: sign-up still credits 10 free GPU credits on the wallet | capture: sha256:57a8ebc1ab1e8ac1ae8f6711ddddeb80167aaab2bc214ce24513116dc1e1490b | quote: When you sign up on NeevCloud, your account is credited with 10 free credits to help you explore and deploy your first GPU instance.
  - [5] 2026-11-24: the sign-up flow has a KYC step between mobile verification and password creation | capture: sha256:855ce760067441d3c9655100ac73056c4cc73f7277fd95b61d540dc47ba0ed39 | quote: text-slate-400">KYC</span>
  - [5] 2026-11-24: the sign-up flow explicitly states that no card is required to start | capture: sha256:855ce760067441d3c9655100ac73056c4cc73f7277fd95b61d540dc47ba0ed39 | quote: No credit card required to start
  - [5] 2026-11-24: the sign-up flow includes a mobile-number step | capture: sha256:855ce760067441d3c9655100ac73056c4cc73f7277fd95b61d540dc47ba0ed39 | quote: text-slate-400">Mobile</span>
  - [1] 2026-11-24: NeevCloud publishes OpenAI- and Anthropic-compatible REST endpoints | capture: sha256:51e0c4a844c482077f2bae78836a761a7f2f3a285f77bf72f83e2c273a0064ed | quote: OpenAI- and Anthropic-compatible endpoints · Hourly or reserved GPUs · Sandboxes that pause billing
- sources:
  - [1] https://www.neevcloud.com/
  - [2] https://docs.ai.neevcloud.com/getting-started/billing-wallet
  - [3] https://code.neevcloud.com/
  - [4] https://www.neevcloud.com/gpu-cluster/
  - [5] https://signup.neevcloud.com/
