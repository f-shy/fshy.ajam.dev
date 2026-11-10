# runners.io

> runners.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runners/ | JSON https://fshy.ajam.dev/api/v1/entity/runners.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## runners.io

- `ci-cd-runners/runners-io` | qualifies-with-caveat | evidence documented | binding request-rate | category CI runner (hosted, GitHub Actions-compatible)
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T02:39:57.489Z (live) | stale on 2026-12-11
- url https://www.runners.io/pricing
- free tier: 3,000 run-minutes included every month for every organisation, with no monthly fee; beyond that USD 0.0040 a run-minute. A run-minute is one minute of a 2 vCPU Linux x64 machine, so a 4 vCPU job spends two run-minutes a minute and a 1 vCPU job spends half of one. | unit: minutes | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a job is bounded by the runner size, and the meter is weighted by vCPU count rather than capped per job
- retention: not applicable: a job runs and is destroyed; state that is kept is priced separately at USD 0.50 a GB-month
- egress: no bandwidth charge is published: the pricing page lists queue wait, cold start, control-plane calls and state reads and writes as not billed, and the homepage says the customer pays only for the minutes jobs run | metered: no
- identity: card | detail: a card: the homepage and the pricing page both say "Card required", and the card is charged for the minutes jobs run
- interface: git
- limits:
  - request-rate (binding): 3,000 run-minutes a month included, then USD 0.0040 a run-minute [1]
  - per-object-cap: state that is kept is USD 0.50 a GB-month [1]
  - request-rate (binding): a priority label costs twice the run-minutes and twice the rate of the same label [1]
- limits note: the meter is weighted by vCPU: 1 vCPU spends 0.5 run-minutes a minute, 4 vCPU spends 2, 8 vCPU spends 4, Linux ARM64 is 0.625x the same size on x64, and Windows is 2.5x
- binding note: 3,000 run-minutes is the first thing to fail, and the vCPU weighting makes it smaller than it looks: on a 4 vCPU runner it is 1,500 wall-clock minutes a month, and the card requirement gates the account before the pool is spent.
- interface detail: a GitHub Actions workflow changes its runs-on label to a runners.io label such as runnersio-2vcpu-ubuntu-2404; every job runs in its own fresh virtual machine
- tooling: a one-line runs-on change on an existing GitHub Actions workflow; no agent or self-hosted runner is needed
- composes with: GitHub Actions on a public repository stays free and comes first; runners.io buys private-repository minutes at USD 0.0040 for 2 vCPU against GitHub list price of USD 0.0060, and the 3,000 included run-minutes cover a small private pipeline, but a card is required before the first job
- reliability: the page publishes no job wall clock and no concurrency cap; the meter is weighted by vCPU, so a wider runner spends the pool faster, and a priority label doubles both the rate and the run-minutes
- notes: A hosted GitHub Actions runner market that includes 3,000 run-minutes a month for every organisation and meters by vCPU-weighted time rather than by seat. The weighting is the fact a reader must carry: 3,000 run-minutes is 1,500 wall-clock minutes on a 4 vCPU runner and 6,000 on a 1 vCPU one. A card is required before the first job, so this is not a no-card lane.
- evidence note: The included pool, the run-minute definition, the weighting and the card requirement are read from the vendor own pages. Raise by running one job on the included pool and reading the run-minute counter and the first invoice line.
- evidence:
  - [1] 2026-11-10: 3,000 run-minutes are included every month for every organisation | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: No monthly fee. 3,000 run-minutes included every month, for every organisation.
  - [1] 2026-11-10: a run-minute is one minute of a 2 vCPU machine | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: 1 run-minute = one minute of a 2 vCPU machine (Linux x64)
  - [1] 2026-11-10: state that is kept is priced at USD 0.50 a GB-month | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: $0.50/GB-month
  - [1] 2026-11-10: the customer pays only for the minutes jobs run | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: You pay only for the minutes your jobs run.
  - [2] 2026-11-10: a workflow targets the runners by changing its runs-on label | capture: sha256:638be05a65e0f1226330a34eca2ac1fd95a3748e92c46ff63dcb8d53a8a0a5d3 | quote: runs-on: runnersio-2vcpu-ubuntu-2404
  - [2] 2026-11-10: every job runs in its own fresh virtual machine | capture: sha256:638be05a65e0f1226330a34eca2ac1fd95a3748e92c46ff63dcb8d53a8a0a5d3 | quote: Change runs-on and every job runs in its own fresh virtual machine.
  - [1] 2026-11-10: the 2 vCPU rate is USD 0.0040 a run-minute | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: $0.0040 a run-minute
  - [1] 2026-11-10: a priority label costs twice the run-minutes | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: Priority = 2x the run-minutes
  - [1] 2026-11-10: a 4 vCPU job spends two run-minutes a minute | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: 4 vCPU = 2 run-minutes per minute
  - [1] 2026-11-10: a card is required before the first job | capture: sha256:274e8f57a099500a31aa0078f27afba097f1325997e9d90def1c49a524a7eef9 | quote: Card required.
- sources:
  - [1] https://www.runners.io/pricing
  - [2] https://www.runners.io/
