# Upsun

> upsun.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upsun/ | JSON https://fshy.ajam.dev/api/v1/entity/upsun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Upsun

- `compute/upsun` | trial-only | evidence documented | binding retention-clamped | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:20:49.285Z (live) | stale on 2026-12-05
- url https://upsun.com/pricing/
- free tier: A 15-day free trial with no credit card, then a monthly credit that covers one project fee (EUR 9) and one user license (EUR 10) for as long as the account exists. Compute is not covered: shared CPU is EUR 0.033 per hour, guaranteed CPU EUR 0.100 per hour and memory EUR 0.013 per GB per hour, billed on provisioned resources. | unit: users | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: 15 days is the free compute window; afterwards the standing credit covers only the platform fee and the seat, so a running app bills from the first provisioned CPU-hour at EUR 0.033. | source: [1]
- egress: Included egress transfer: 10 GB per project per month; additional egress transfer EUR 0.03 per GB. | metered: yes | free allowance: 10 GB per project per month | source: [1]
- identity: email | detail: no card: the pricing page states 'No credit card required' for the 15-day free trial, and the standing monthly credit covers one project fee and one user license. No hold exists because no payment method is taken. The signup fields are not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: cli, ssh
- limits:
  - retention-clamped (binding): 15 days is the free compute window; afterwards the standing credit covers only the platform fee and the seat, so a running app bills from the first provisioned CPU-hour at EUR 0.033. [1]
- limits note: 15 days is the free compute window; afterwards the standing credit covers only the platform fee and the seat, so a running app bills from the first provisioned CPU-hour at EUR 0.033.
- binding note: the same as limits note
- interface detail: Upsun Cloud CLI (the upsun command), documented at docs.upsun.com/administration/cli.html: manages projects, pushes code, opens SSH into environments and automates workflows; API tokens authenticate it for CI systems and cron jobs.
- tooling: Upsun Cloud CLI (the upsun command; API tokens authenticate it for CI/CD and automation)
- composes with: 15 days with no card is enough to measure whether a containerised app builds and runs on the platform, and the standing credit keeps the project record alive afterwards so the 15 days can be repeated later without a new account.
- reliability: no reliability event recorded
- notes: Upsun is the successor brand to Platform.sh, and platform.sh pricing redirects into this page. Open: whether the 15 days can be renewed per project, which the page does not say.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: '15-day free trial', 'Monthly credit covering 1 project fee + 1 user license', 'No credit card required', quoted
  - [1] 2026-10-22: Application shared CPU EUR 0.033/hour, guaranteed CPU EUR 0.100/hour, memory EUR 0.013 per GB/hour; project fee EUR 9.00/project/month; user license EUR 10.00/user/month, quoted
  - [1] 2026-10-22: object storage is not available on trial projects, quoted
  - [1] 2026-11-04: 10 GB per project per month included, EUR 0.03 per GB beyond | capture: sha256:90d2a17157d4265f94ea8d6dfd3640b24eace727cbc57ec4bfa41164d35cca15 | quote: Included egress transfer: 10 GB/project/month Additional egress transfer: €0.03/GB
  - [2] 2026-11-04: the Upsun Cloud CLI manages projects and opens SSH into environments | capture: sha256:efcd7010c75afe6d904df906778598564b4025a6316984b2187ae15fa87348eb | quote: Manage projects, push code, SSH into environments, and automate workflows.
  - [2] 2026-11-04: the page documents the Upsun Cloud CLI | capture: sha256:efcd7010c75afe6d904df906778598564b4025a6316984b2187ae15fa87348eb | quote: The full power of Upsun Cloud in your terminal. Manage projects, push code, SSH into environments, and automate workflows.
  - [2] 2026-11-04: the CLI page documents the upsun CLI for managing projects, pushing code, SSH and automation | capture: sha256:efcd7010c75afe6d904df906778598564b4025a6316984b2187ae15fa87348eb | quote: The full power of Upsun Cloud in your terminal. Manage projects, push code, SSH into environments, and automate workflows.
  - [3] 2026-11-04: API tokens authenticate the Upsun Cloud CLI for CI and cron automation | capture: sha256:a999a48e131648c9ac05ef3af45e6efcfeb557e6be49cc6a1013ed9dd0499008 | quote: You need to set up an API token to authenticate the Upsun Cloud CLI for any of the following tasks:
- sources:
  - [1] https://upsun.com/pricing/
  - [2] https://docs.upsun.com/administration/cli.html
  - [3] https://docs.upsun.com/administration/cli/api-tokens.html
