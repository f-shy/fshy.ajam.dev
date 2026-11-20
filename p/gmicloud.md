# GMI Cloud SCALE

> gmicloud.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gmicloud/ | JSON https://fshy.ajam.dev/api/v1/entity/gmicloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GMI Cloud SCALE

- `compute/gmi-cloud-scale` | fails-identity | evidence documented | binding write-gated | category inference API | tier SCALE startup cohort
- identity a placeholder: card and phone unknown | verified 2026-11-03T10:14:36.706Z (live) | stale on 2026-12-04
- url https://www.gmicloud.ai/en/company/scale
- free tier: a six-week equity-free cohort for AI startups: USD 500 of model-as-a-service credits on acceptance, 1:1 credit matching up to USD 4,500 for money the team adds, 20% off dedicated endpoints for teams with steady volume, a GPU voucher after completing the program (no amount is stated on the page), and partner credits the vendor totals at 'Up to $40K from all GMI partners'. The page says Cohort 3 credit terms will be confirmed before kickoff. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: admission is by application to a selected cohort of AI startups ('Apply to Cohort 3'); the application form's fields (email, company, stage) were not read: unverified: the form is behind the apply link.
- interface: rest
- limits:
  - write-gated (binding): cohort admission is the gate: an application ('Apply to Cohort 3'), a small cohort of technical founders (the page counts 25 AI companies in Cohort 01), and a team building an AI product. The 1:1 match is USD 1 of credit for each USD 1 the team adds to MaaS, up to USD 4,500, so the headline credit is not the credit received. [1]
- limits note: cohort admission is the gate: an application form, a selected cohort of about 25 companies a cycle, and a team that is building a product. The USD 4,500 match also requires the team to spend USD 4,500 first, so the headline credit is not the credit received.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: unverified: the page states a GPU voucher on completing the program but no amount, and says Cohort 3 credit terms will be confirmed before kickoff, so no GPU-hour figure can be derived from it.
- reliability: no reliability event recorded
- notes: The 1:1 match is credit given for credit the team adds to MaaS, not a grant. The partner figure aggregates credits from other vendors, so it is not GMI compute. The vendor's on-demand GPU rental is a separate paid-only offer and not part of this cohort. The page lists Cohort 01 as complete (Apr-May 2026) and Cohort 3 for Spring 2027 (Mar-May) with applications open on 2026-11-03.
- extras:
  - facets.class: startup-cohort
  - facets.free_tier_kind: grant
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: '6-week Equity-Free Startup Program for AI-native teams'; 'Up to $40K+ in Structured Credits'; 'Phase 1 - Onboarding Credits $500 MaaS Credits on acceptance'; '1:1 credit matching up to $4,500'; 'For every $1 you add to MaaS, GMI matches $1 in credits', quoted
  - [2] 2026-10-22: on-demand rates 'NVIDIA H100 GPU from $2.60/GPU-hour', 'H200 from $3.20/GPU-hour', 'B200 from $5.00/GPU-hour', 'GB200 from $8.00/GPU-hour', quoted
  - [1] 2026-11-03: the credit terms of the open Cohort 3 are not final on the page, and the page names no USD amount for the GPU voucher (the program highlight says 'earn a GPU voucher after completing the program') | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Cohort 3 credit terms will be confirmed before kickoff.
  - [1] 2026-11-03: the GPU voucher is named without an amount | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Onboard fast with MaaS credits, unlock 1:1 matching as you scale, and earn a GPU voucher after completing the program.
  - [1] 2026-11-03: the page counts 25 AI companies in the cohort; admission is by application | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Five weeks. 25 AI companies. Real infra, real raises, real demos.
  - [1] 2026-11-03: the offer is the SCALE startup cohort, entered by application, and is not the vendor's on-demand GPU rental | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Apply to Cohort 3
  - [1] 2026-11-03: Cohort 3 applications were open on the read date | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Cohort 03 applications open
  - [1] 2026-11-03: the cohort is a selected group of founders, entered by application | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: We work with a small cohort of technical founders
  - [1] 2026-11-03: the offer is a program entered by application to a selected cohort, so the verdict fails-identity (institution) stands | capture: sha256:1549357e8e178cef6b8b7627a50c94fe21ee8eceba4f219cb12a0b6e1d769e8b | quote: Apply to Cohort 3
- sources:
  - [1] https://www.gmicloud.ai/en/company/scale
  - [2] https://www.gmicloud.ai/en/pricing
