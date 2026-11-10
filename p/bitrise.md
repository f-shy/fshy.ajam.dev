# bitrise artifacts

> bitrise.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitrise/ | JSON https://fshy.ajam.dev/api/v1/entity/bitrise.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bitrise (mobile CI)

- `compute/bitrise` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:22.309Z (live) | stale on 2026-11-22
- url https://bitrise.io/pricing
- free tier: a Free plan with build credits for a small project a few times a month, recommended up to 100 builds a month; no credit count is published | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): Free is described as enough credits for a few builds a month and recommended to 100 builds a month; no credit total is published [1]
  - write-gated: the 30-day trial is separate from the Free plan, which does not expire [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and describes the Free plan in words rather than a number: 'enough build credits ... a few times per month'. That is a discretionary allowance and the record says so instead of putting a figure on it
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states no build wall-clock cap; the credit total is what runs out
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free' plan described as 'Enough build credits for you to build your small project a few times per month' and 'Recommended up to 100 builds/month', with a 30-day trial and paid tiers at $99 and $218 a month, quoted
- sources:
  - [1] https://bitrise.io/pricing

## bitrise artifacts

- `storage/bitrise-artifacts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
- free tier: none reachable: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
- sources:
  - [1] https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
