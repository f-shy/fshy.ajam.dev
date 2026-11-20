# Octopus Cloud

> octopus.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/octopus/ | JSON https://fshy.ajam.dev/api/v1/entity/octopus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Octopus Cloud

- `ci-cd-runners/octopus-cloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted deployment automation and CI/CD orchestration | tier Free (USD 0 per year)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T07:00:00.000Z (live) | stale on 2026-12-20
- url https://octopus.com/pricing/overview
- free tier: a Free cloud tier at USD 0 per year with 10 projects, 10 tenants, 10 machines, 10 users, 1 space, 5 concurrent tasks, 1 TB file storage and 100 GB database storage | unit: users | metered on: request-count | read on: 2026-11-19 | source: [1]
- per-object cap: unverified: no per-object or build wall-clock cap stated in the first-party pages read | source: [1]
- retention: unverified: no number is stated in the first-party pages read | source: [1]
- egress: unverified: no egress allowance or price stated on the pricing page | metered: no | source: [1]
- identity: email | detail: a sign-up is needed for the free cloud tier; the exact form fields are unverified: behind a sign-up. The page names SSO through Google, Microsoft Azure or GitHub on paid plans.
- interface: browser, git, rest
- limits:
  - volume-quota (binding): Free cloud tier: 10 projects, 10 tenants, 10 machines, 1 space, 10 users and 5 concurrent tasks [1]
  - per-object-cap: Free cloud tier: 1 TB file storage and 100 GB database storage [1]
  - write-gated: a task is a deployment, runbook, health check or other operation; only 5 run concurrently on the free tier, up to 20 for an additional fee on paid plans [1]
- binding note: the free tier binds at 10 projects and 5 concurrent deployment tasks before any build minute allowance, and it is a deployment service rather than a source-code build runner
- interface detail: deployments, runbooks and environment promotions run in Octopus Cloud; build servers such as TeamCity, Azure DevOps, GitHub Actions and Jenkins integrate through build-server integrations; the free tier includes SSO and RBAC.
- endpoint: unverified: no public API endpoint stated on the pages read
- tooling: release snapshotting, config variables as secrets management, runbook automation and environment promotion with approvals
- composes with: a build server produces a release; Octopus Cloud deploys it through a pipeline with approvals and runbooks
- reliability: 
- notes: A hosted deployment and CI/CD orchestration service with a Free cloud tier at USD 0 per year. It is not a source-code build runner: builds come from integrated external build servers.
- evidence note: all values are quoted from the first-party pricing page read on 2026-11-19. The free tier is a cloud deployment service, not a source-code build runner; builds are integrated from external build servers. Concurrent tasks and storage are stated on the page.
- evidence:
  - [1] 2026-11-19: a Free cloud tier at USD 0 per year with 10 projects | capture: sha256:be1be1511f6025ae1fbdd6d4ddcf3b5f86ad7b32ae3ec4e6e8b6fdd7f0232144 | quote: $ 0 USD / year 10 projects
  - [1] 2026-11-19: the free tier allows 5 concurrent tasks | capture: sha256:be1be1511f6025ae1fbdd6d4ddcf3b5f86ad7b32ae3ec4e6e8b6fdd7f0232144 | quote: - 5 concurrent tasks
  - [1] 2026-11-19: the free tier states 1 TB file and 100 GB database storage | capture: sha256:be1be1511f6025ae1fbdd6d4ddcf3b5f86ad7b32ae3ec4e6e8b6fdd7f0232144 | quote: - 1TB file storage - 100GB database storage
- sources:
  - [1] https://octopus.com/pricing/overview
