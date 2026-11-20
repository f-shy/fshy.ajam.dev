# bitrise artifacts

> bitrise.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitrise/ | JSON https://fshy.ajam.dev/api/v1/entity/bitrise.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bitrise (mobile CI)

- `compute/bitrise` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-18T04:58:12.810Z (live) | stale on 2026-12-19
- url https://bitrise.io/pricing
- free tier: a Free plan with build credits for a small project a few times a month, recommended up to 100 builds a month; no credit count is published | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not stated | metered: no | price per TB: cache only: USD 0.12 per GB non-Bitrise-CI egress | source: [1]
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
  - [1] 2026-11-18: not stated | capture: sha256:3f1d18ce1709ce470980438a3b6c01fd90934d0f1d7f2f83275a373dea331c3c | quote: # Plans for mobile engineering teams of every size
- sources:
  - [1] https://bitrise.io/pricing

## bitrise artifacts

- `storage/bitrise-artifacts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.621Z (live) | stale on 2026-12-04
- url https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
- free tier: none reachable: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Bitrise artifact retention policy page | source: [1] | note: not stated on the Bitrise artifact retention policy page
- retention: Bitrise stores both build artifacts and build logs for a limited amount of time. The retention period varies by artifact type to balance storage costs with typical usage patterns. | source: [1] | note: per-type periods are listed in the retention table; removal is permanent with no recovery
- egress: not stated on the Bitrise artifact retention policy page | metered: no
- identity: email
- interface: rest
- interface detail: Bitrise API for listing and downloading build artifacts
- tooling: Bitrise API calls to list builds, list artifacts and fetch download URLs
- composes with: archive artifacts to the user's own storage via the API download URLs to outlive retention
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
  - [1] 2026-11-19: installable artifacts are retained for 150 days | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: | Installable artifacts (.ipa, .akp and .aab files) | 150 days | Available for Enterprise customers |
  - [1] 2026-11-19: artifact removal is permanent with no recovery | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: When artifacts are removed, they are permanently deleted with no way to recover them.
  - [1] 2026-11-19: the interface is the Bitrise HTTP API | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: You can download build artifacts via the Bitrise API in order to store them
  - [1] 2026-11-19: the documented tool is the Bitrise API | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: To keep artifacts beyond the retention period, archive them using the Bitrise API:
  - [1] 2026-11-19: no per-file cap appears in the retention policy | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: Bitrise stores both build artifacts and build logs for a limited amount of time.
  - [1] 2026-11-19: artifact retention is time-boxed and varies by artifact type | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: Bitrise stores both build artifacts and build logs for a limited amount of time. The retention period varies by artifact type to balance storage costs with typical usage patterns.
- sources:
  - [1] https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
