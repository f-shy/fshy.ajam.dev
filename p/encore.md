# Encore Cloud

> encore.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/encore/ | JSON https://fshy.ajam.dev/api/v1/entity/encore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Encore Cloud

- `compute/encore-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:20.285Z (live) | stale on 2026-12-05
- url https://encore.dev/pricing
- free tier: The Starter plan is free forever with no time limit: 2 development environments on Encore Cloud, 1M tracing events a month, 7-day log and trace retention, 1 concurrent build. Applications hosted on Encore Cloud carry fair-use limits per application on every plan: 100,000 requests a day, 100,000 Pub/Sub messages a day, 1 GB of database storage, 1 GB of object storage, and cron jobs no more often than once an hour. | unit: requests | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): 100,000 requests a day is the ceiling, about 1.16 requests a second averaged, and cron at most hourly means a polling loop cannot be tightened. [1]
- limits note: 100,000 requests a day is the ceiling, about 1.16 requests a second averaged, and cron at most hourly means a polling loop cannot be tightened.
- binding note: the same as limits note
- interface detail: the encore CLI, documented in the CLI reference at encore.dev/docs/ts/cli/cli-reference
- tooling: the Encore CLI (encore auth login; git push encore to deploy; encore gen client generates Go, TypeScript and JavaScript API clients)
- composes with: 100k requests a day of a free hosted Go or TypeScript API with 1 GB of managed Postgres behind it is a whole small service for nothing; the hourly-cron ceiling means a tighter loop has to move, and on Pro the compute moves to the user's own AWS account.
- reliability: no reliability event recorded
- notes: The unit is requests, not compute: Encore publishes no vCPU or memory allowance for the free hosted environment, so the shape is null rather than guessed. Possibilities: (a) the free tier is local only; refuted, the fair-use limits are stated for environments hosted on Encore Cloud on every plan and Starter includes 2 dev environments there. (b) Starter cannot deploy to Encore Cloud; not established, since the page names deployment to your own cloud as a Pro feature without saying Starter is blocked from Encore Cloud hosting. That is the open question and it moves the verdict between qualifies and trial-only.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: perpetual-allowance
- evidence:
  - [1] 2026-10-22: Starter is free forever with no time limit; 2 dev environments on Encore Cloud, 1M tracing events/month, 7-day retention, 1 concurrent build, quoted
  - [1] 2026-10-22: Environments hosted on Encore Cloud follow Fair Use limits on every plan, per application: 100,000 requests/day, 100,000 Pub/Sub messages/day, 1 GB database storage and 1 GB object storage, cron jobs at most once an hour, quoted
  - [1] 2026-10-22: Pro is USD 49 per team member per month plus USD 99 per AWS/GCP environment and USD 2.50 per resource; Pro deploys into the customer's own AWS or GCP account, quoted
  - [1] 2026-11-03: the pricing page states no egress allowance or price; Pro deploys into the customer's own cloud account | capture: sha256:e19edb711428d79fc61ccc7903ea69c0997e4d82c40e5ef5fbe1932a64517b66 | quote: You deploy to your own AWS or GCP account, so you own and control your infrastructure with no proprietary runtime dependencies on Encore.
  - [2] 2026-11-03: a documented CLI exists | capture: sha256:64265ffce74636e8d34fb72d4ee0f37e9e3061f27db1e2fe12ac51a6eff0a494 | quote: The Encore CLI lets you run your local environment and much more.
  - [2] 2026-11-04: the Encore CLI is documented | capture: sha256:64265ffce74636e8d34fb72d4ee0f37e9e3061f27db1e2fe12ac51a6eff0a494 | quote: The Encore CLI lets you run your local environment and much more.
  - [2] 2026-11-04: the CLI logs in and deploys through a git remote | capture: sha256:64265ffce74636e8d34fb72d4ee0f37e9e3061f27db1e2fe12ac51a6eff0a494 | quote: Requires `encore auth login`. Clones into a directory named after the app ID by default, with a git remote named `encore`, so you can deploy changes with `git push encore`.
- sources:
  - [1] https://encore.dev/pricing
  - [2] https://encore.dev/docs/ts/cli/cli-reference
