# Buddy Sandboxes

> buddy.works | CI runners, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buddy/ | JSON https://fshy.ajam.dev/api/v1/entity/buddy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Buddy

- `ci-cd-runners/buddy` | qualifies-with-caveat | evidence documented | binding volume-quota | category CI runner | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:52:06.675Z (live) | stale on 2026-12-20
- url https://buddy.works/pricing
- free tier: Free plan at EUR 0: 1 seat, 2 concurrents, USD 1 of usage credit per month for compute and storage, and 1 GB of pipeline cache; all features except SSO and advanced permissions | unit: credits | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: the USD 1 credit buys CPU-minutes, GB-minutes and GB-hours at the published rates, so the free allowance is a dollar budget rather than a fixed minute count; 1 GB of pipeline cache is included on top
- per-object cap: no per-object cap stated; the free plan includes 1 GB of pipeline cache | source: [2]
- retention: a free workspace with no login is frozen after 60 days and permanently terminated if no action is taken in the following 30 days; pipeline runs alone do not count as activity | days: 90 | source: [2] | note: the 90 days is the sum of the 60-day inactivity window and the following 30 days before permanent termination: 60 + 30 = 90
- egress: no egress allowance or per-GB price is published; storage is billed per GB-hour at USD 0.00011 for sandbox and artifact storage and USD 0.00068 for the pipeline cache | metered: no | source: [3]
- identity: email | detail: the signup page offers GitHub, GitLab, Google or Bitbucket sign-in, or a work email address, full name and a password of at least 15 characters or 7 including a number; no phone number or card is asked for on that page, and the pricing page states 'No credit card required'
- interface: git, rest, cli
- limits:
  - volume-quota (binding): USD 1 of usage credit per month on Free, spent on CPU-minutes, GB-minutes and GB-hours; no pay-as-you-go billing on Free [3]
  - request-rate: 2 concurrent pipeline runs on Free, a hard limit with no extra concurrents sold [1]
  - per-object-cap: 1 seat and 1 GB of pipeline cache on Free [1]
  - retention-clamped: a free workspace is frozen after 60 days with no login and permanently terminated if no action is taken in the following 30 days [2]
- limits note: the USD 1 credit buys 4,166 CPU-minutes or GB-minutes at the container rate of USD 0.00024 each: USD 1 / USD 0.00024 = 4,166.67; a macOS VM runs at USD 0.00144 per GB-minute, about six times faster; storage at USD 0.00011 per GB-hour also draws from the same credit
- binding note: the USD 1 monthly credit binds first: a free pipeline stops when the credit is used up and cannot be extended with pay-as-you-go, before 2 concurrent runs or the 60-day inactivity window matter
- interface detail: the REST API is described by an OpenAPI 3 specification and is reached at api.buddy.works, api.eu.buddy.works or api.asia.buddy.works with an OAuth2 bearer token; pipelines are defined in the web editor, in YAML or imported from YAML, and the bdy CLI starts and follows pipeline runs
- endpoint: https://api.buddy.works
- tooling: a browser-based visual pipeline builder, YAML pipeline definitions, the bdy CLI and a REST API with an OpenAPI 3 specification; pipelines run in containers or Linux, Windows and macOS VMs with x64 or ARM64 CPUs; self-hosted Buddy installations exist but are software the reader installs and runs and come after this hosted offer
- composes with: a Git push, pull request, schedule or webhook starts a pipeline; containers make up over 90% of actions and consume the USD 1 monthly credit at USD 0.00024 per CPU-minute and GB-minute, with higher GB-minute multipliers for Windows and macOS; a free pipeline stops once the credit is used up and resumes when it renews
- reliability: unverified: no suspension or data-loss event is stated on the pages read; a free workspace is frozen after 60 days without a login and terminated 30 days later, and pipelines and sandboxes stop when the monthly credit runs out
- notes: Buddy's hosted CI/CD service is the subject of this record. A separate record, compute/buddy, holds the Buddy Sandboxes container and VM sandbox offer under the compute topic, and a domain-collision open question is filed. The free USD 1 monthly credit buys a variable number of minutes depending on the action type, so the allowance is a budget rather than a fixed minute count. Self-hosted Buddy installations are software the reader installs and runs, listed after this hosted offer. No pipeline was run, so the CPU, memory and disk of a run and the build log retention period are unverified.
- evidence note: the Buddy pricing page, plans-and-features doc, usage doc, signup page, API overview and pipeline UI doc were read and quoted on 2026-11-19; no pipeline was run, so the CPU, memory and disk of a pipeline run and the exact build log retention period are unverified
- self hosted: no
- evidence:
  - [1] 2026-11-19: the free plan allows 2 concurrent pipeline runs with no option to buy more | capture: sha256:85bc5f92472aab8f1e4d3868af5099f12de42545e72da0d2fe193f3016c4083b | quote: - 2 concurrents (no extra concurrents)
  - [1] 2026-11-19: the free plan includes USD 1 of monthly compute and storage credit | capture: sha256:85bc5f92472aab8f1e4d3868af5099f12de42545e72da0d2fe193f3016c4083b | quote: - $1/mo. usage credit (compute & storage)
  - [2] 2026-11-19: the free plan has 1 seat, 2 concurrents, USD 1 monthly credit and all features except SSO and advanced permissions | capture: sha256:1dccd78896efdac1d6b0d34039da225606003daebe3061c9920699b5dcbe69a4 | quote: The Free plan gives you access to all the features of Buddy except SSO and advanced permissions. It is limited to 1 seat and 2 concurrents and includes $1 of usage credit every month.
  - [2] 2026-11-19: a free workspace is frozen after 60 days without activity and terminated 30 days later | capture: sha256:1dccd78896efdac1d6b0d34039da225606003daebe3061c9920699b5dcbe69a4 | quote: Free workspaces are a subjet to inactivity termination. After a period of 60 days with no activity, the workspace will be frozen and subsequently terminated permanently if no action is taken within the following 30 days.
  - [3] 2026-11-19: the free plan has no pay-as-you-go billing and stops when the USD 1 credit is used up | capture: sha256:e4794b639bd8fa02b2d2f411079104e1784b83a4c698529bce409ba7e088b6fe | quote: The Free plan has no pay-as-you-go billing. Instead, it includes $1 of usage credit every month, spent at the rates above, and 1 GB of pipeline cache.
  - [3] 2026-11-19: compute is billed at USD 0.00024 per CPU-minute and GB-minute | capture: sha256:e4794b639bd8fa02b2d2f411079104e1784b83a4c698529bce409ba7e088b6fe | quote: Both CPU-minutes and GB-minutes cost $0.00024.
  - [3] 2026-11-19: a macOS VM GB-minute costs USD 0.00144, six times the container rate | capture: sha256:e4794b639bd8fa02b2d2f411079104e1784b83a4c698529bce409ba7e088b6fe | quote: | macOS VM | 6 | $0.00144 |
  - [4] 2026-11-19: the signup form asks for an email address | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: Your work email
  - [4] 2026-11-19: the signup form asks for a password with a stated complexity rule | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: Password: at least 15 characters or 7 including a number
  - [5] 2026-11-19: a documented REST API is available for programmatic access | capture: sha256:721ac293ac5c11cf9a58da23cb7f72910b4903e4f82608bfe945828759de93a8 | quote: The Buddy REST API is described by an OpenAPI 3 specification.
  - [5] 2026-11-19: self-hosted Buddy installations exist beside the hosted cloud service | capture: sha256:721ac293ac5c11cf9a58da23cb7f72910b4903e4f82608bfe945828759de93a8 | quote: For self-hosted installations of Buddy:
  - [6] 2026-11-19: a pipeline can target x64 or ARM64 CPUs | capture: sha256:fbc8eb66ff9c90e40979614f92f3d9bfd2949b209c8ebfe38afcce86d8f0cfa9 | quote: You can choose between x64 and ARM64
- sources:
  - [1] https://buddy.works/pricing
  - [2] https://buddy.works/docs/basics/billing-and-usage/features
  - [3] https://buddy.works/docs/basics/billing-and-usage/gbmin
  - [4] https://buddy.works/sign-up
  - [5] https://buddy.works/docs/api
  - [6] https://buddy.works/docs/pipelines/introduction/creating-pipeline/pipeline-ui

## Buddy Sandboxes

- `compute/buddy` | trial-only | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T11:38:11.105Z (live) | stale on 2026-12-25
- url https://buddy.works/pricing
- free tier: a free Trial with 1 seat, 2 concurrents, USD 5 of usage credit for compute and storage and 10 GB of pipeline cache; the page states 'Credit card required' | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page lists seats, concurrents, a $1 monthly usage credit and a pay-as-you-go rate per CPU-minute and GB-minute, with no egress allowance or overage | metered: no | source: [1]
- identity: card | detail: the sign-up form collects 'Your work email', 'Full Name' and a password, with GitHub, GitLab, Google or Bitbucket sign-in beside it; the free Trial states 'Credit card required' and no phone number is asked for.
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): 2 concurrent pipelines on Free, with no option to buy more [1]
  - per-object-cap: 1 seat, USD 5 of usage credit covering compute and storage, and 10 GB of pipeline cache on the free Trial [1]
- interface detail: web UI, the bdy CLI, a TypeScript SDK, a REST API, YAML pipeline definitions and SSH from an IDE
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-11-24 and states the free tier's three limits and the USD 5 usage credit
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no timeout unless the caller sets one; the machine persists with no automatic idle reap
  - free_tier_kind: recurring-credit
  - burst_x: 1.0
  - ps.price: $0.00024 per GB-minute from the credit
  - ps.durability: workspace storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the workspace exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '2 concurrents (no extra concurrents)' with a '$1/mo. usage credit (compute & storage)' and '1 seat', against 'Pay-as-you-go usage (from $0.00024 per CPU-minute / GB-minute)', quoted
  - [2] 2026-11-04: Sandboxes have a REST API | capture: sha256:cd60e701b06bc8b0ee9b94ddad63caf87b2ea9144e78b63ed4e2c48f108febd5 | quote: | REST API | Any language, any automation | [API reference](https://buddy.works/docs/api/sandboxes) |
  - [2] 2026-11-04: Sandboxes are reachable over SSH | capture: sha256:cd60e701b06bc8b0ee9b94ddad63caf87b2ea9144e78b63ed4e2c48f108febd5 | quote: - Remote development - reachable over SSH from your IDE.
  - [1] 2026-11-04: usage is priced per CPU-minute and GB-minute, with no network row | capture: sha256:8ada3ee74545ff56db005f3b3eb18602471f26f355872143575d33eb6bc36023 | quote: Pay-as-you-go usage (from $0.00024 per CPU-minute / GB-minute)
  - [3] 2026-11-04: the registration form collects an email address | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: Your work email
  - [4] 2026-11-04: the free start is advertised without a card | capture: sha256:d3b7e04f0ccd791efeabf3330ac0bc63dbf718e6de4fc3392c79e67b1cacf03b | quote: No credit card required.
  - [3] 2026-11-04: four OAuth sign-ins sit beside the email form | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: GitHub GitLab Google Bitbucket
  - [5] 2026-11-18:  | capture: sha256:2881edce29684c601db3f9404a1819ab822fd805a45d1a205e02bad5e9e90520 | quote: Hosting an application** - a Sandbox has no timeout unless you set one, so it simply keeps running.
  - [1] 2026-11-24: the free Trial gives 1 seat, 2 concurrents and a USD 5 usage credit but requires a card | capture: sha256:8166acc5ad5891a59aa23fbc16e6fdb41957b8d142f711a3aa9b22adbdc37a17 | quote: - Credit card required ... - 1 seat (extra seats free) ... - 2 concurrents (no extra concurrents) ... - $5 usage credit (compute & storage) ... - 10 GB of pipeline cache
  - [1] 2026-11-24: the Trial's usage credit is USD 5 | capture: sha256:8166acc5ad5891a59aa23fbc16e6fdb41957b8d142f711a3aa9b22adbdc37a17 | quote: - $5 usage credit (compute & storage)
  - [1] 2026-11-24: a card is required for the Trial | capture: sha256:8166acc5ad5891a59aa23fbc16e6fdb41957b8d142f711a3aa9b22adbdc37a17 | quote: - Credit card required
  - [3] 2026-11-24: registration collects an email address, a full name and a password and offers four OAuth sign-ins | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: Your work email ... Full Name ... Password: at least 15 characters or 7 including a number
  - [1] 2026-11-24: the only free offer is a card-gated Trial, not a card-free tier | capture: sha256:8166acc5ad5891a59aa23fbc16e6fdb41957b8d142f711a3aa9b22adbdc37a17 | quote: - Credit card required
  - [1] 2026-11-24: usage is priced per CPU-minute and GB-minute with no egress row on the plan table | capture: sha256:8166acc5ad5891a59aa23fbc16e6fdb41957b8d142f711a3aa9b22adbdc37a17 | quote: Pay-as-you-go usage (from $0.00024 per CPU-minute / GB-minute)
  - [4] 2026-11-24: the advertised trial is card-gated and lasts 14 days | capture: sha256:a5fa65e84ed3818437fc062f7bac9f5b7b28f2377819175da3ee6a1050d19ee1 | quote: 14-day trial with all Team features. Credit card required.
  - [2] 2026-11-24: Sandboxes have a REST API | capture: sha256:cd60e701b06bc8b0ee9b94ddad63caf87b2ea9144e78b63ed4e2c48f108febd5 | quote: | REST API | Any language, any automation | [API reference](https://buddy.works/docs/api/sandboxes) |
- sources:
  - [1] https://buddy.works/pricing
  - [2] https://buddy.works/docs/sandboxes/introduction
  - [3] https://buddy.works/sign-up
  - [4] https://buddy.works/react
  - [5] https://buddy.works/docs/sandboxes/introduction.md
