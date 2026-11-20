# Zoltan's FLOPs GPU

> tcz.hu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tcz/ | JSON https://fshy.ajam.dev/api/v1/entity/tcz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zoltan's FLOPs GPU

- `compute/zoltan-s-flops-gpu` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://tcz.hu/zoltans-flops
- free tier: 'Zoltan's FLOPs is a mini-grant program for GPU computing projects. The goal is to provide small-scale funding to help researchers and developers access GPU compute time on modern hardware.' Size, quoted: 'Total grant budget this iteration: $5,000', and '1-5 projects will be selected, depending on their compute requirements. The selected projects will get a portion of the total grant budget and can spend it on Vast.ai to provision on-demand GPU instances.' The gate is the whole point, quoted: 'Anyone can apply by filling out a simple form. There is no geographical restriction.' Selection, quoted: 'The selection criteria are purely based on my personal judgment, taking into account the project proposal, the background of the applicant, and the computing requirements.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): one person's judgement decides it: between one and five projects share USD 5,000, the deadline for the first iteration was April 15, 2025, and the page now reads 'Applications closed. Watch this site for results and future iterations.' [1]
- limits note: one person's judgement decides it: between one and five projects share USD 5,000, the deadline for the first iteration was April 15, 2025, and the page now reads 'Applications closed. Watch this site for results and future iterations.'
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The only grant in this category with no geography clause, no entity clause and no institutional sponsor: USD 5,000 at Lambda's documented on-demand rate of USD 3.99 per H100 GPU-hour (compute/lambda) is about 1,253 H100-hours, which is more than enough for one reproducible experiment on a competition dataset. It composes with Zindi and DrivenData competitions, where the compute cost of entry is exactly this size.
- reliability: no reliability event recorded
- notes: Zoltan's FLOPS GPU grants provide up to USD 5,000 in GPU marketplace credits for independent researchers, distributed via application review.
- extras:
  - facets.class: community-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'Total grant budget this iteration: $5,000'; 'Anyone can apply by filling out a simple form. There is no geographical restriction. The deadline is the 15th of April, 2025'; '1-5 projects will be selected'; 'can spend it on Vast.ai to provision on-demand GPU instances'; 'Applications closed. Watch this site for results and future iterations'; 'This iteration received 29 applications'; page 200
  - [2] 2026-10-22: the announcement post by the programme's author dated 'March 10, 2025, 2:02pm UTC', quoted: 'Today, I'm starting a mini-grant for GPU computation.' and 'In the first iteration of this mini-grant, I hope to support projects where knowledge isn't the bottleneck; computing is.'; page 200
- sources:
  - [1] https://tcz.hu/zoltans-flops
  - [2] https://discuss.huggingface.co/t/zoltans-flops-gpu-mini-grant-1st-iteration/145030
