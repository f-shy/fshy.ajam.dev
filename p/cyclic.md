# Cyclic

> cyclic.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyclic/ | JSON https://fshy.ajam.dev/api/v1/entity/cyclic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cyclic

- `compute/cyclic` | dead | evidence documented | binding retention-clamped | category platform host | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://www.cyclic.sh/posts/cyclic-is-shutting-down
- free tier: shut down: the shutdown post is dated 26 April 2024 and the marketing site still serves a free-tier pitch on 2026-10-24, which is a live trap | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: all usage was turned off in 2024; nothing remains
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: not applicable: signup is closed
- interface: rest
- limits:
  - retention-clamped (binding): the shutdown post is dated 26 Apr 2024 while the site still markets the product [1]
- limits note: there is no allowance: the service stopped in May 2024.
- binding note: the service ended; the website did not.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: inactive offering.
- reliability: the marketing page still renders 'Git push to go live in under 10 seconds' with no shutdown notice
- notes: The pair is the finding: a shutdown post and a live sales page on the same domain, two years apart.
- evidence note: the shutdown post and the live marketing page were both read
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - facets.shape.ram_gib: 1
  - billing_model: none
  - term: none
  - price_arithmetic: none
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: dead
- evidence:
  - [1] 2026-10-22: 'Effective immediately we are turning off signups by new users. In two weeks, May 10th, we will begin turning off free tier usage. We will begin turning off all usage May 31', dated 26 Apr 2024, quoted
  - [2] 2026-10-22: the pricing page as indexed still lists 'Free Forever: 1 app, No inactivity delay, No hourly limit, 1024 MB RAM', with no shutdown notice on that page
  - [3] 2026-10-22: 
  - [1] 2026-10-24: quoted: '# Cyclic is Shutting Down / 26 Apr 2024 / Dear Users, We are shutting down Cyclic.'
  - [3] 2026-10-24: the marketing page still reads 'Escape infrastructure. Unleash ideas. Build and run modern cloud-native serverless applications', with no shutdown notice
- sources:
  - [1] https://www.cyclic.sh/posts/cyclic-is-shutting-down
  - [2] https://www.cyclic.sh/pricing
  - [3] https://www.cyclic.sh/
