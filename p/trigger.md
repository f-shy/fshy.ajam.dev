# Trigger.dev

> trigger.dev | Compute, Developer services; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trigger/ | JSON https://fshy.ajam.dev/api/v1/entity/trigger.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trigger.dev (Compute)

- `compute/trigger-dev` | qualifies-with-caveat | evidence documented | binding volume-quota | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:50:59.430Z (live) | stale on 2026-12-01
- url https://trigger.dev/pricing
- duplicate of `dev-services/trigger-dev`
- free tier: $5 a month of free credits with 20 concurrent runs and unlimited tasks, no card | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: No credit card required; the login page offers GitHub, Google, SSO or email.
- interface: unknown
- limits:
  - volume-quota (binding): USD 5 of compute credits a month on the Free plan [1]
  - request-rate: 20 concurrent runs; 1,500 API requests per minute [1]
- binding note: The monthly USD 5 credit runs out first for a sustained workload: past it, tasks stop until the next month or an upgrade.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free tier is a monthly recurring credit, not a trial
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; the monthly credit bounds it
  - free_tier_kind: recurring-credit
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · No credit card required · $5 / month free credits · 20 concurrent runs · Unlimited tasks', quoted
  - [1] 2026-10-31: the Free plan gives USD 5 of compute credits a month and 20 concurrent runs | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: The Free plan includes $5 of compute credits every month and 20 concurrent runs.
  - [1] 2026-10-31: every plan, the Free plan included, is limited to 1,500 API requests a minute | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: All plans are limited to 1,500 API requests per minute, and you can request a higher limit on paid plans.
  - [1] 2026-10-31: tasks stop once the monthly credit is spent | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: Once those credits are used, you'll need to upgrade to keep running tasks.
  - [2] 2026-10-31: the login page offers sign-up by email, beside GitHub, Google and SSO | capture: sha256:d076aa24d81babdf45711c31d7a4c68eb769eb86886d707332eb4d634c19ade2 | quote: Continue with Email
  - [1] 2026-10-31: the Free plan needs no credit card | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: No credit card required
- sources:
  - [1] https://trigger.dev/pricing
  - [2] https://cloud.trigger.dev/login

## Trigger.dev (free)

- `dev-services/trigger-dev` | qualifies-with-caveat | evidence documented | binding volume-quota | category background job and workflow runner (hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:43:09.670Z (live) | stale on 2026-12-01
- url https://trigger.dev/pricing
- free tier: Free plan at USD 0 a month with no credit card: USD 5 of compute credits every month, 20 concurrent runs, unlimited tasks, 5 team members, 10 schedules, 1 day log retention and 10 concurrent Realtime connections | unit: credits | metered on: wall-clock | read on: 2026-10-31 | source: [1] | note: The credit pays for seconds of compute by machine size plus an invocation charge per run (USD 0.000025); runs in the DEV environment are not charged. Once the credit is used, tasks stop until the next month or an upgrade.
- per-object cap: 3MB per single trigger payload | source: [2]
- retention: 1 day of logs on the Free plan; a queued run expires after the 14-day maximum TTL | days: 1 | source: [2]
- egress: not stated: the pricing page charges compute seconds and runs and names no charge on traffic out of a task | metered: no | source: [1]
- identity: email | detail: No credit card required; the login page offers GitHub, Google, SSO or email.
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 5 of compute credits a month (a monetary credit, not bytes) [1]
  - request-rate: 1,500 API requests per minute [1]
  - request-rate: 20 concurrent runs [1]
  - retention-clamped: 1 day of logs; queued runs expire after 14 days [2]
- limits note: 10 schedules and 10 concurrent Realtime connections on the Free plan.
- binding note: The monthly USD 5 credit runs out first for a sustained workload: past it, tasks stop until the next month or an upgrade.
- interface detail: The management API at api.trigger.dev takes an environment API key or a personal access token as a Bearer token, and the @trigger.dev/sdk package wraps it; the CLI runs tasks locally with hot reloading
- tooling: the @trigger.dev/sdk package, the CLI and the web dashboard
- composes with: A hosted runner for TypeScript tasks with no maximum run duration, so a long crawl or a chain of model calls runs off any free host until USD 5 of compute is spent.
- reliability: no reliability event recorded; once the monthly credit is spent, tasks stop running until the next month or an upgrade
- notes: The same offer is also recorded as compute/trigger-dev. At USD 0.0000338 a second for the Small 1x machine (0.5 vCPU, 0.5 GB), USD 5 buys about 147,929 seconds, or 41 hours, a month before invocation charges.
- self hosted: no
- evidence:
  - [1] 2026-10-31: the Free plan includes USD 5 of compute credits every month and 20 concurrent runs | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: The Free plan includes $5 of compute credits every month and 20 concurrent runs.
  - [1] 2026-10-31: the Free plan needs no credit card | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: No credit card required
  - [1] 2026-10-31: the Free plan keeps logs for 1 day | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: 1 day log retention
  - [1] 2026-10-31: the Free plan has 10 schedules | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: 10 schedules
  - [1] 2026-10-31: tasks stop once the monthly credit is used | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: Once those credits are used, you'll need to upgrade to keep running tasks.
  - [1] 2026-10-31: every plan is limited to 1,500 API requests a minute | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: All plans are limited to 1,500 API requests per minute, and you can request a higher limit on paid plans.
  - [1] 2026-10-31: each run on managed workers carries an invocation charge on top of compute | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: Every run that starts executing on our managed workers is charged an invocation cost in addition to compute costs.
  - [1] 2026-10-31: a CLI runs tasks locally | capture: sha256:7c263b6d2d0beda7a224b05c240bd7d4dacd8c85e4ee9c9ff1523512cffb0a7e | quote: Using our CLI you develop your tasks locally with hot reloading.
  - [2] 2026-10-31: queued runs on Trigger.dev Cloud expire after a 14-day maximum TTL | capture: sha256:8422a61915b7758ba7bd5bb33e026bf1eff2d7f132e50e875bde4d5ff9c4b20b | quote: On Trigger.dev Cloud, all runs have an enforced maximum TTL of 14 days.
  - [2] 2026-10-31: a single trigger payload is capped at 3MB | capture: sha256:8422a61915b7758ba7bd5bb33e026bf1eff2d7f132e50e875bde4d5ff9c4b20b | quote: | Single trigger payload | Must not exceed 3MB |
  - [3] 2026-10-31: the login page offers GitHub and Google sign-in | capture: sha256:d076aa24d81babdf45711c31d7a4c68eb769eb86886d707332eb4d634c19ade2 | quote: Continue with GitHub Continue with Google
  - [3] 2026-10-31: the login page offers sign-in by email | capture: sha256:d076aa24d81babdf45711c31d7a4c68eb769eb86886d707332eb4d634c19ade2 | quote: Continue with Email
  - [4] 2026-10-31: the management API takes an environment API key or a personal access token | capture: sha256:adb769243106bac756930f4d2ac917ff6a3b4284c4a6f00528742eaaefeef654 | quote: There are two methods of authenticating with the management API: using a named API key associated with a specific environment in a project, or using a personal access token (PAT).
  - [4] 2026-10-31: the management API is served at api.trigger.dev | capture: sha256:adb769243106bac756930f4d2ac917ff6a3b4284c4a6f00528742eaaefeef654 | quote: --url https://api.trigger.dev/api/v1/projects/{projectRef}/envvars/preview/DATABASE_URL
- sources:
  - [1] https://trigger.dev/pricing
  - [2] https://trigger.dev/docs/limits
  - [3] https://cloud.trigger.dev/login
  - [4] https://trigger.dev/docs/management/authentication
