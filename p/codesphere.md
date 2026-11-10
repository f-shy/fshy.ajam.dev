# Codesphere

> codesphere.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codesphere/ | JSON https://fshy.ajam.dev/api/v1/entity/codesphere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codesphere

- `compute/codesphere` | fails-quota | evidence documented | binding pull-count | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://codesphere.dev/pricing
- free tier: A Free plan at USD 0 that publishes exactly one metered allowance: 5 commits a month, with basic features and community support. The page states no vCPU, memory, storage or wall-clock figure for the free plan, and Pro is USD 20 a month for unlimited commits. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - pull-count (binding): 5 commits a month is the published ceiling and there is no published compute allowance to spend it on, so a workspace that needs a sixth deploy waits for the next cycle. [1]
- limits note: 5 commits a month is the published ceiling and there is no published compute allowance to spend it on, so a workspace that needs a sixth deploy waits for the next cycle.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 5 commits a month with unpublished resources is a demo slot, not a host; the standby mode means a free workspace answers the first request after a restart delay, so it can serve a rarely visited page and nothing else.
- reliability: no reliability event recorded
- notes: This is a partial by design: the free plan is real and the capacity is not published, so the shape is null rather than the 2 vCPU / 4 GB that older third-party lists still quote for Codesphere. Possible, and it would make the verdict qualifies-with-caveat, but no page read states a resource figure. (b) codesphere.dev is a different product from codesphere.com; unresolved, since codesphere.com/pricing returns 404 and the dev domain is the only pricing page that answered.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: perpetual-allowance
- evidence:
  - [1] 2026-10-22: Free USD 0: '5 commits per month', basic features, community support; Pro USD 20/month for unlimited commits, quoted
  - [2] 2026-10-22: free plans always run in the standby-when-unused deployment mode, where a workspace sleeps after about 60 minutes of inactivity and restarts on the next request, quoted
  - [3] 2026-10-22: a free tier exists with a limit on how many free plan workspaces can run in parallel, quoted
- sources:
  - [1] https://codesphere.dev/pricing
  - [2] https://ai.codesphere.com/pricing
  - [3] https://codesphere.ghost.io/free-tier-launch/
