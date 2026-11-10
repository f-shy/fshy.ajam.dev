# RunMyJob

> runjob.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runjob/ | JSON https://fshy.ajam.dev/api/v1/entity/runjob.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunMyJob

- `compute/runmyjob` | qualifies-with-caveat | evidence documented | binding volume-quota | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:36:18.029Z (live) | stale on 2026-12-05
- url https://runjob.eu/
- free tier: The brand is now RunJob, and the read of https://runmyjob.io/ redirects to https://runjob.eu/, whose own title is 'Pay for CI Usage, Not Idle Time!' and which describes 'Cloud runners for GitHub Actions and GitLab CI'. A directory record states the move, quoted: 'RunMyJob has rebranded as RunJob and moved to runjob.eu'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): The free plan is metered in CPU-seconds and GB-seconds, not in runner-hours, so a 12 vCPU job burns the monthly allowance at twelve times the wall-clock rate, and the allowance figure cannot be read as hours. [1]
- limits note: The free plan is metered in CPU-seconds and GB-seconds, not in runner-hours, so a 12 vCPU job burns the monthly allowance at twelve times the wall-clock rate, and the allowance figure cannot be read as hours.
- binding note: the same as limits note
- interface detail: a dashboard and a declarative API for managing runners; Kubernetes API access and Terraform modules for scaling; jobs arrive through the GitHub Actions or GitLab CI runner integration. No page read names REST.
- tooling: not stated
- composes with: A free CI runner with per-second load metering is a place to run a burst without a card, and it composes with a public GitHub repository the same way the GitHub-hosted runner does, but with a meter.
- reliability: no reliability event recorded
- notes: The free plan's metering unit is the finding, because a 'free' CI runner that meters CPU-seconds is not comparable to a GitHub public-repository runner that meters nothing. The figures here come from a third-party directory and the vendor's own marketing copy; the free plan's allowance number was not read from a first-party pricing page and stays `unverified`.
- extras:
  - facets.class: verification
  - facets.free_tier_kind: perpetual-allowance
  - facets.shape.vcpu: 12
  - facets.shape.ram_gib: 32
- evidence:
  - [2] 2026-10-22: HTTP 404 Not Found: the earlier URL of the free plan no longer exists
  - [3] 2026-10-22: redirects to runjob.eu; the page reads 'Cloud runners for GitHub Actions and GitLab CI' and 'Pay only for actual CPU and memory load'
  - [4] 2026-08-01: quoted: 'RunMyJob has rebranded as RunJob and moved to runjob.eu' [date precision: month precision]
  - [3] 2026-10-22: Free plan EUR 0/m: 1 integration with GitLab or GitHub organization, 10 concurrent jobs, 12 vCPU and 32 GB memory per job, 400 vCPU-minutes included monthly, quoted
  - [3] 2026-10-22: usage price over the allowance is EUR 0.00002 per vCPU-second and EUR 0.000001 per GB-second, quoted
  - [5] 2026-10-22: 
  - [6] 2026-11-04: Terraform modules and Kubernetes API access are offered | capture: sha256:0c9066265889a2168b26f52bbd75b068bb078774d93032b187a7ad55b6f41965 | quote: the service does provide Terraform modules and Kubernetes API access as an advantage for those who wish to utilize it to scale up and manage their operations with ease.
  - [1] 2026-11-04: runners are managed through a dashboard or a declarative API; no protocol is named | capture: sha256:ff4a8e74f1492585bc5e827331113da5dc09f1b5f5f3867d3b579c5424aa4481 | quote: Manage your runners via dashboard or declarative API
- sources:
  - [1] https://runjob.eu/
  - [2] https://runmyjob.io/pricing
  - [3] https://runmyjob.io/
  - [4] https://app.dealroom.co/news/feed/runjob-launches-spike-instances-with-load-based-billing-for-european-ci-infrastructure
  - [5] https://euro-stack.com/solutions/runmyjob-io
  - [6] https://runjob.eu/docs
