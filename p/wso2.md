# WSO2 Choreo

> wso2.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wso2/ | JSON https://fshy.ajam.dev/api/v1/entity/wso2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WSO2 Choreo

- `compute/wso2-choreo` | trial-only | evidence documented | binding retention-clamped | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:26.169Z (live) | stale on 2026-12-05
- url https://wso2.com/choreo/pricing/
- free tier: The free plan is gone from the pricing page. The published plans are 'Team USD 150/component per month' with 'Infrastructure quota (soft limits) CPU - 25 RAM - 128GB Storage - 500GB Network - 500GB', 500 builds and 500 deployments a month, and 'Enterprise - Custom'. The only free route is 'Start 2 Week Free Trial'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: there is no perpetual allowance: the trial is a 14-day clock, and after it a component costs USD 150 a month. | source: [1]
- egress: unverified: https://wso2.com/choreo/pricing/ now serves a marketing page with no plan table (read 2026-11-03); the earlier read of the Team plan quoted a soft Network quota, not… | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding): there is no perpetual allowance: the trial is a 14-day clock, and after it a component costs USD 150 a month. [1]
- limits note: there is no perpetual allowance: the trial is a 14-day clock, and after it a component costs USD 150 a month.
- binding note: the same as limits note
- interface detail: unverified: no CLI, SSH or SDK page was reachable (the choreo-cli reference was not found on 2026-11-03)
- tooling: not stated
- composes with: two weeks is enough to run a build-and-deploy cycle end to end inside a platform that would cost USD 150 a month per component afterwards, so it is a testing venue, not a home.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'The free tier includes up to 5 components and USD 100 credits per month'. That plan is not on the pricing page today; the page lists Team and Enterprise only and offers a 2-week trial. This is a refutation of a widely repeated free tier, and the next reader should not budget for it. A free tier may still exist behind the console signup, which was not entered.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: 'Team USD 150/component per month' and 'Enterprise Custom' are the only two plans in the comparison table, quoted
  - [1] 2026-10-22: the page's only entry point is 'Start 2 Week Free Trial', quoted
  - [1] 2026-10-22: Team quota row: 'Infrastructure quota (soft limits) | CPU - 25 RAM - 128GB Storage - 500GB Network - 500GB', quoted
  - [1] 2026-11-03: the pricing URL now serves a marketing page for the renamed platform | capture: sha256:106becf13937971fcb105ea4480e46bdefcf72f002bb2d925008cf3cb85284ca | quote: Automate workflows, reduce complexity, and empower teams to build, secure, and deploy at scale with the all-in-one ready-to-use AI-native WSO2 Developer Platform (formerly known as Choreo).
- sources:
  - [1] https://wso2.com/choreo/pricing/
