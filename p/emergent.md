# Emergent

> emergent.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/emergent/ | JSON https://fshy.ajam.dev/api/v1/entity/emergent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Emergent

- `compute/emergent` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:52.067Z (live) | stale on 2026-12-05
- url https://help.emergent.sh/plans-the-free-tier
- free tier: Emergent Free: "10 credits on your first day", "Publish to production | no", and the note says the Free tier exists "to explore Emergent", quoted | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: the 10 credits are granted once on the first day and not refilled, so the second day has nothing; publishing also needs 50 credits, which free never reaches. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding): the 10 credits are granted once on the first day and not refilled, so the second day has nothing; publishing also needs 50 credits, which free never reaches. [1]
- limits note: the 10 credits are granted once on the first day and not refilled, so the second day has nothing; publishing also needs 50 credits, which free never reaches.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 10 credits is one exploration, not a workload; the only thing it produces is a judgement about whether the paid tier is worth USD 17 a month.
- reliability: no reliability event recorded
- notes: compute/emergent-ventures is a different entity: a grant fund, not this app builder. The two must not be merged on the shared word. A third-party review site states the free tier is 10 credits a month and calls it "Free forever"; the vendor page says first day. The conflict is recorded rather than resolved, because the vendor page is the stronger source and it does not say monthly.
- extras:
  - facets.class: trial
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: "Monthly credits | 10 credits on your first day" and "The Free tier gives you 10 credits on your first day", quoted
  - [1] 2026-10-22: "Publish to production | no" for Free, and "published app is credit-gated, requiring a minimum of 50 credits to start", quoted
  - [2] 2026-10-22: Standard is "$20 / month", "$17 / month" annual, with "100 credits per month", quoted
  - [1] 2026-11-03: usage is metered in credits; the plans page states no egress allowance or price | capture: sha256:8e5afe2dc9de6b73930730669ef0e48d2e40772a1e758ded6bc9496aff2ca1ed | quote: Every plan is credit-based: building, testing, and publishing your apps consumes credits.
- sources:
  - [1] https://help.emergent.sh/plans-the-free-tier
  - [2] https://emergent.sh/pricing
