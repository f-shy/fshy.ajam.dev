# ApexWeave

> apexweave.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apexweave/ | JSON https://fshy.ajam.dev/api/v1/entity/apexweave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ApexWeave

- `compute/apexweave` | trial-only | evidence documented | binding retention-clamped | category platform host
- needs card no, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://apexweave.com/free-tier
- free tier: 'a 14-day live trial plus a 120-day grace period during which your app keeps serving traffic while you decide', with a 'Managed Postgres database - Postgres 16, daily snapshots, automatic backups', 'Free SSL certificate', 'Git push deploys' and 'No credit card up front'. Paid plans are flat monthly and start at 'Starter plans for indie developers' without a published entry price on the free-tier page. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: the free window is a clock, 14 days of trial followed by 120 days of grace, and no CPU, memory or storage figure is published for it, so capacity cannot be the named constraint. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card at signup: the free-tier page and the pricing page both state 'No credit card up front', so no authorisation or hold is taken and debit or prepaid acceptance does not arise. The pages describe the trial window (14 days plus 120 days of grace) but not the signup form, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: git
- limits:
  - retention-clamped (binding): the free window is a clock, 14 days of trial followed by 120 days of grace, and no CPU, memory or storage figure is published for it, so capacity cannot be the named constraint. [1]
- limits note: the free window is a clock, 14 days of trial followed by 120 days of grace, and no CPU, memory or storage figure is published for it, so capacity cannot be the named constraint.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 134 days of a running app plus Postgres for nothing is the longest free window found among evaluated providers and covers a competition entry or a paper's demo period without a card, after which the app must move or be paid for.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: dalisoft/awesome-hosting lists 'ApexWeave | Plans (5 USD/m) | Trial yes | Free yes | Dynamic'. The trial-plus-grace shape is confirmed by the vendor, and the USD 5 figure is the aggregator's, not the vendor's: neither the pricing page nor the free-tier page publishes a plan price, so it is not recorded. Capacity is the real unknown: no vCPU, memory or disk figure appears on either page, and the comparison page describes the service in prose only. A probe of a deployed app would be needed to size it.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: 'a 14-day live trial plus a 120-day grace period during which your app keeps serving traffic while you decide', quoted
  - [1] 2026-10-22: 'Managed Postgres database - Postgres 16, daily snapshots, automatic backups' and 'No credit card up front', quoted
  - [2] 2026-10-22: '14-day full production trial, then 120-day grace period. Includes a managed Postgres database, free SSL, and full git push workflow. No credit card up front.', quoted
- sources:
  - [1] https://apexweave.com/free-tier
  - [2] https://apexweave.com/pricing
