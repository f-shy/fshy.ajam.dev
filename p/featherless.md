# Featherless AI

> featherless.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/featherless/ | JSON https://fshy.ajam.dev/api/v1/entity/featherless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Featherless AI

- `compute/featherless-ai` | paid-only | evidence documented | binding request-rate | category inference API
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T16:38:10.688Z (live) | stale on 2026-12-26
- url https://featherless.ai/pricing
- free tier: No free tier: the pricing page lists only paid plans — Pay-As-You-Go from $5, Chat $25/mo, Business Custom. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: rest
- limits:
  - request-rate (binding): on the cheapest plan the context window and 4 concurrent units bind before anything else: 32K of context and four units in flight, with no production API on that tier at all. [1]
- limits note: on the cheapest plan the context window and 4 concurrent units bind before anything else: 32K of context and four units in flight, with no production API on that tier at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 25 a month for unlimited interactive chat tokens is the cheapest per-token cost in evaluated offerings if the workload is a single interactive chat; it buys nothing for an agent, because the Chat plan excludes API traffic and automation.
- reliability: no reliability event recorded
- notes: The word 'unlimited' is the trap: the same page's footnote restricts the Chat plan to human-driven use and excludes benchmarking, and the Developer plan is metered per token instead. So the free-looking offer is neither free nor unlimited for a programmatic workload. No free trial is published, which makes this a paid-only record rather than trial-only.
- extras:
  - facets.class: paid-inference
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the plan table's three columns are 'Chat $25/mo', 'Developer from $50/mo', 'Business Custom' with no free column; 'Credits expire: Never'; 'Token volume: Unlimited' on Chat and Business; 'Concurrent units: 4' on Chat, 100 on Developer, quoted
  - [2] 2026-10-22: 'Flat-rate pricing designed for scale with unlimited tokens'; 'Chat plan is for interactive, human-driven use by the purchaser. Not for reselling, app/API traffic, background automation, or benchmarking', quoted
  - [1] 2026-11-25: the Chat plan price is unchanged | capture: sha256:73eed77f6c27ea0129f8aaf104eb1cc1b8231213b1957cb827769c572ced4248 | quote: | Chat $25/mo |
  - [1] 2026-11-25: the pricing table has three paid plan columns and no free column; Chat is not the cheapest published plan | capture: sha256:73eed77f6c27ea0129f8aaf104eb1cc1b8231213b1957cb827769c572ced4248 | quote: | | Pay-As-You-Go from $5 | Chat $25/mo | Business Custom |
  - [1] 2026-11-25: the three published plans are all paid and no free tier is listed | capture: sha256:73eed77f6c27ea0129f8aaf104eb1cc1b8231213b1957cb827769c572ced4248 | quote: | | Pay-As-You-Go from $5 | Chat $25/mo | Business Custom |
- sources:
  - [1] https://featherless.ai/pricing
  - [2] https://featherless.ai/
