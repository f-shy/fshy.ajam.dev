# Moore Threads AI

> mthreads.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mthreads/ | JSON https://fshy.ajam.dev/api/v1/entity/mthreads.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Moore Threads AI

- `compute/moore-threads-ai` | trial-only | evidence reported | binding request-rate | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://code.mthreads.com/
- free tier: The vendor page advertises, translated from Chinese: 'domestic compute with a domestic model, a limited-time 30-day free trial', and 'Free Trial: CNY 0, limited to 100 developers a day', served on MTT S5000 GPUs with the GLM-4.7 model and reachable from Claude Code, Cursor, OpenCode, Cline and similar tools. The page also states the offer is built on the MTT S5000 and that the model is GLM-4.7. Three paid tiers are shown for comparison: Lite at CNY 120 a quarter, Pro at CNY 600 a quarter, Max at CNY 1200 a quarter. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-window
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | country: CN
- interface: rest
- limits:
  - request-rate (binding): 100 signups a day is the first wall, then a 30-day clock; the page states no token allowance, so the daily quota is the constraint that visibly fails first. [1]
- limits note: 100 signups a day is the first wall, then a 30-day clock; the page states no token allowance, so the daily quota is the constraint that visibly fails first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It composes with any coding client that speaks an OpenAI-compatible or Anthropic-compatible endpoint, which is why the vendor lists Claude Code and Cline. It breaks at the identity step and at the daily cap, and the 30 days do not renew.
- reliability: no reliability event recorded
- notes: The vendor page states no signup gate at all, so the Chinese-mobile requirement is reported by a third party and not confirmed here; that is why the rung is reported and not documented. The prompt allowance inside the free window is not published; The Chinese source text is quoted here in translation to keep the file ASCII.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: trial-window
  - facets.shape.gpu_class: Moore Threads MTT S5000
- evidence:
  - [1] 2026-10-22: 'domestic compute with a domestic model, a limited-time 30-day free trial' and 'Free Trial: CNY 0, limited to 100 developers a day', translated from the live page read
  - [1] 2026-10-22: the page states the service runs on MTT S5000 GPUs and serves GLM-4.7, translated, so the offer is accelerator-hosted inference rather than a resold third-party API
  - [2] 2026-10-22: a deal aggregator records the gate as a Chinese mobile number and reports the vendor page did not state one; the aggregator dates the offer at 2026-10-11
- sources:
  - [1] https://code.mthreads.com/
  - [2] https://lanmao.ai/zh/o/mthreads-ai-coding-plan-free-trial/
