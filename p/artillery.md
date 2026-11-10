# Artillery

> artillery.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/artillery/ | JSON https://fshy.ajam.dev/api/v1/entity/artillery.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Artillery

- `compute/artillery` | qualifies-with-caveat | evidence documented | binding request-rate | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:14.689Z (live) | stale on 2026-12-05
- url https://www.artillery.io/pricing
- free tier: Free tier with the quota row reading 'no limit' | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page quotas list test volume, retention, team members, workers, test duration and test cases, and no egress or bandwidth term | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): the Free tier's quota row reads 'no limit'; the page states no numeric ceiling [1]
- interface detail: the Artillery CLI and the Artillery Cloud web dashboard; a Stash API row appears in the plan table, with no REST reference read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a Free tier with 'no limit' in its quota row. 'No limit' is a claim about a missing sentence and is recorded as the unit unlimited, not multiplied into a capacity figure
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: Artillery runs a load test rather than hosting a machine, so there is no session to reap
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and lists a Free tier whose quota row reads 'no limit'; the page names no runtime hour cap
  - [1] 2026-11-03: the pricing page lists no egress or bandwidth term; the product is used through a CLI and a cloud dashboard | capture: sha256:538ff3a742f2d755392b1e6625e86e8e14e9839f08aa59a26b91330ba808cc49 | quote: An Artillery Cloud subscription covers the use of both the Artillery CLI and Artillery Cloud dashboard and services.
- sources:
  - [1] https://www.artillery.io/pricing
