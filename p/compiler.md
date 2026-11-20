# compiler.dev

> compiler.dev | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/compiler/ | JSON https://fshy.ajam.dev/api/v1/entity/compiler.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## compiler.dev

- `ci-cd-runners/compiler-dev` | trial-only | evidence documented | binding retention-clamped | category CI runner (hosted, GitHub Actions-compatible)
- needs card no, phone no, ID no, institution no | verified 2026-11-10T02:39:57.591Z (live) | stale on 2026-12-11
- url https://compiler.dev/pricing
- free tier: 200 free minutes over 14 days, up to 8 jobs at once, Linux only, with no card; a card is needed only when the minutes run out. Beyond the trial the Basic plan is USD 0.001 a core-minute, so a 2-core runner is USD 0.002 a minute and an 8-core runner USD 0.008. | unit: minutes | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a job is bounded by the runner size, chosen with a label such as compiler-8cpu
- retention: not applicable: a job runs and is destroyed; the trial itself ends after 14 days
- egress: not stated: the page prices compute per core-minute and publishes no egress allowance or egress charge | metered: no
- identity: email | detail: an email and a GitHub account, with no card for the trial: "No card needed: the trial starts when you install the App"; a card is added only when the 200 minutes run out
- interface: git
- limits:
  - request-rate: 200 free minutes over 14 days, up to 8 concurrent jobs, Linux only [1]
  - request-rate: USD 0.001 a core-minute on Basic, USD 0.00175 on Pro and USD 0.043 on Turbo [1]
  - retention-clamped (binding): the free window is 14 days; prepaid credit never expires and unused credit is refunded on request [1]
- limits note: prepaid credit is sold in USD 20, USD 100 (which buys USD 110) and USD 500 (which buys USD 600) blocks that never expire; Turbo runs on dedicated machines and is arranged with the vendor
- binding note: The 14-day window fails before the 200 minutes for most pipelines: the trial is a comparison allowance, and a project that wants to keep using it must add a card and buy prepaid credit.
- interface detail: a GitHub Actions workflow names a compiler.dev runner label such as compiler-2cpu or compiler-8cpu; the trial starts when the GitHub App is installed
- tooling: a GitHub App installation and a runs-on label change on an existing workflow; no agent or self-hosted runner is needed
- composes with: GitHub Actions on a public repository stays free and comes first; compiler.dev sells private-repository minutes at USD 0.001 a core-minute, which is USD 0.002 for 2 cores against GitHub list price of USD 0.006, and the 200 free minutes are enough to compare one pipeline before a card is added
- reliability: the trial is capped at 8 concurrent jobs and Linux only; the page publishes no job wall clock and no queue limit
- notes: A per-core-minute hosted runner with a small no-card trial: 200 minutes over 14 days, 8 concurrent jobs, Linux only. The rate is the lowest published core-minute price in this topic, and the trial is sized for a comparison rather than for a workload.
- evidence note: The trial terms, the three rates and the credit terms are read from the vendor own pricing page. Raise by running a job in the trial and reading the minute counter and the first prepaid-credit line.
- evidence:
  - [1] 2026-11-10: the trial is 200 free minutes over 14 days with no card | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: 200 free minutes over 14 days, up to 8 jobs at once, Linux only.
  - [1] 2026-11-10: the price is per core-minute | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: One price: $0.001 per core-minute.
  - [1] 2026-11-10: a job is bounded by the runner size | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: `compiler-8cpu` (8 vCPU)
  - [1] 2026-11-10: the trial itself ends after 14 days | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: 200 free minutes over 14 days
  - [1] 2026-11-10: no egress allowance or charge is published | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: One price: $0.001 per core-minute.
  - [1] 2026-11-10: a job targets a runner by its runs-on label | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: `compiler-8cpu` (8 vCPU)
  - [1] 2026-11-10: the trial starts when the GitHub App is installed | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: the trial starts when you install the App
  - [1] 2026-11-10: the Basic rate is USD 0.001 a core-minute | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: One price: $0.001 per core-minute.
  - [1] 2026-11-10: the free window is 14 days | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: 200 free minutes over 14 days
  - [1] 2026-11-10: prepaid credit never expires | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: Never expires; unused credit refunded on request.
  - [1] 2026-11-10: no card is needed for the trial | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: Start with 200 free minutes. No card.
  - [1] 2026-11-10: the trial is capped at 8 concurrent jobs | capture: sha256:ff3c78c6ee986744d1fd45ceb1a0fa23813a9ad0f9e6d63f0f92f3a8a869678d | quote: up to 8 jobs at once, Linux only
- sources:
  - [1] https://compiler.dev/pricing
