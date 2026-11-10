# Val Town

> val.town | Compute, Developer services, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/val/ | JSON https://fshy.ajam.dev/api/v1/entity/val.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Val Town (Compute)

- `compute/val-town` | qualifies-with-caveat | evidence documented | binding retention-clamped | category serverless runtime
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:50:59.432Z (live) | stale on 2026-12-01
- url https://www.val.town/limits
- duplicate of `dev-services/val-town`
- free tier: A free plan whose crons run every 15 minutes at minimum and whose workers are killed after 10 seconds idle, with a hard 6-hour ceiling on any worker: quoted 'Worker idle timeout | 10 sec' and 'Worker runtime | 6 hrs Absolute ceiling on a single worker's lifetime, regardless of plan'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: The 10-second idle timeout ends any process that is not answering requests, so the host is a scheduler and not a machine: what survives is the cron every 15 minutes, not a daemon. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: The sign-up page offers GitHub, Google or email and shows no card field.
- interface: rest
- limits:
  - retention-clamped (binding): worker idle timeout 10 sec; worker runtime at most 6 hrs on any plan; execution timeout 1 min per run on the Free plan [1]
- limits note: Free plan: minimum cron interval 15 min, execution timeout 1 min per run, 1,000 authenticated API requests per minute and 0 private vals; a worker has 4 GiB of memory.
- binding note: The 10-second idle timeout ends any process that is not answering requests, so the host is a scheduler and not a machine: what survives is the cron every 15 minutes, not a daemon.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 15-minute cron with 100,000 runs a day at no charge provides scheduled execution, and Email yourself provides an alerting mechanism for external services.
- reliability: no reliability event recorded
- notes: The home record of this offer is dev-services/val-town; its blob storage is storage/val-town. A worker lives 10 sec past its last request and at most 6 hrs on any plan, so nothing daemon-shaped runs here. The Free plan has 0 private vals.
- extras:
  - facets.class: paas-never-sleep
  - facets.free_tier_kind: perpetual
  - facets.shape.ram_gib: 4
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Worker idle timeout | 10 sec How long a worker waits for more requests before shutting down' and 'Worker runtime | 6 hrs Absolute ceiling on a single worker's lifetime, regardless of plan' and 'Worker memory | 4 GiB', quoted
  - [1] 2026-10-22: 'Minimum cron interval | 15 min' on Free, 'Execution timeout | 1 min' on Free, 'API requests per minute | 1,000' on Free, 'Crons per val | 10', quoted
  - [2] 2026-10-22: the Free column: '$0', '15 min cron intervals', '1 min wall clock time / run', 'Unlimited public vals', '100,000 runs / day', 'Email yourself', quoted
  - [3] 2026-10-31: the sign-up page offers email, beside GitHub and Google | capture: sha256:5500f1e84e1296210098ae8ad59089cdd6ab74121449b2b2ae379e482842f57f | quote: Continue with email
  - [1] 2026-10-31: a worker shuts down 10 seconds after its last request | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Worker idle timeout | 10 sec How long a worker waits for more requests before shutting down. |
  - [1] 2026-10-31: the minimum cron interval on the Free plan is 15 minutes | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Minimum cron interval Shortest delay between scheduled runs of a single val. | 15 min | 1 min | 1 min |
  - [1] 2026-10-31: a worker lives at most 6 hours on any plan | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Worker runtime | 6 hrs Absolute ceiling on a single worker's lifetime, regardless of plan. |
- sources:
  - [1] https://www.val.town/limits
  - [2] https://www.val.town/pricing
  - [3] https://www.val.town/auth/signup

## Val Town (free)

- `dev-services/val-town` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted serverless TypeScript runtime with crons and HTTP endpoints | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:43:09.670Z (live) | stale on 2026-12-01
- url https://www.val.town/pricing
- free tier: Free plan at USD 0: 100,000 runs / day, 15 min cron intervals, 1 min wall clock time / run, unlimited public vals, 3 days log retention, email to the account's own address and MCP integration | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: Free accounts have 0 private vals and 2,500 vals in all; the Val Town API takes 1,000 authenticated calls a minute; a worker has 4 GiB of memory.
- per-object cap: 80,000 characters per source file in a val; 30 MiB per incoming email | source: [2]
- retention: 3 days of logs on the Free plan | days: 3 | source: [2]
- egress: not stated: the pricing and limits pages name no charge or cap on traffic out of a val | metered: no | source: [2]
- identity: email | detail: The sign-up page offers GitHub, Google or email; the form has no card field.
- interface: rest
- limits:
  - request-rate (binding): 100,000 runs per day [1]
  - request-rate (binding): minimum cron interval of 15 min per val [2]
  - request-rate (binding): 1,000 authenticated API requests per minute [2]
- limits note: Each run stops at 1 min of wall-clock time on the Free plan; a worker shuts down 10 seconds after its last request and lives at most 6 hours on any plan.
- binding note: The 15-minute minimum cron interval decides what can be scheduled; the 1-minute cap per run, in limits_note, decides what fits in one run.
- interface detail: The REST API manages vals, blob storage, sqlite databases and other account resources, with a TypeScript SDK over it; vals also serve their own HTTP endpoints
- tooling: the Val Town web editor, the REST API and its TypeScript SDK, and MCP integration
- composes with: A cron every 15 minutes with up to one minute per run, free, serves as a heartbeat and poller for jobs on other hosts, with mail to the account owner as the alert path.
- reliability: no reliability event recorded
- notes: The same offer is also recorded as compute/val-town; its blob storage is storage/val-town.
- evidence:
  - [1] 2026-10-31: the Free plan allows 100,000 runs a day | capture: sha256:765ff78f8deea0e778f1e1e7749dcfb829e0f9e351736151b22f0e8af2fc5e75 | quote: 100,000 runs / day
  - [1] 2026-10-31: the Free plan keeps logs 3 days | capture: sha256:765ff78f8deea0e778f1e1e7749dcfb829e0f9e351736151b22f0e8af2fc5e75 | quote: 3 days log retention
  - [1] 2026-10-31: the Free plan sends email only to the account's own address | capture: sha256:765ff78f8deea0e778f1e1e7749dcfb829e0f9e351736151b22f0e8af2fc5e75 | quote: Email yourself
  - [2] 2026-10-31: logs are kept 3 days on Free against 10 on paid plans | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Log retention | 3 days | 10 days | 10 days |
  - [2] 2026-10-31: the minimum cron interval on Free is 15 minutes | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Minimum cron interval Shortest delay between scheduled runs of a single val. | 15 min | 1 min | 1 min |
  - [2] 2026-10-31: a single run on Free stops at 1 minute of wall-clock time | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Execution timeout Maximum wall-clock time for a single val run. | 1 min | 10 min | 10 min |
  - [2] 2026-10-31: the API takes 1,000 authenticated requests a minute on Free | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | API requests per minute Authenticated Val Town API calls. | 1,000 | 10,000 | 10,000 |
  - [2] 2026-10-31: the Free plan has no private vals | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Private vals | 0 | 2,000 | 2,000 |
  - [2] 2026-10-31: a source file in a val is capped at 80,000 characters | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | File size | 80,000 characters Per-file limit. Applies to source files in a val. |
  - [2] 2026-10-31: a worker has 4 GiB of memory | capture: sha256:a3c8c1f3ee5a35323ce06b1923b32119b8c0c5c8afe6585d1352043ae369fda2 | quote: | Worker memory | 4 GiB |
  - [3] 2026-10-31: the sign-up page offers GitHub | capture: sha256:78f7bba2e90f3175e9ee2160142a8cf7d7bc65bcd66799148d4b9ca26fbeca80 | quote: Continue with GitHub
  - [3] 2026-10-31: the sign-up page offers Google | capture: sha256:78f7bba2e90f3175e9ee2160142a8cf7d7bc65bcd66799148d4b9ca26fbeca80 | quote: Continue with Google
  - [3] 2026-10-31: the sign-up page offers email | capture: sha256:78f7bba2e90f3175e9ee2160142a8cf7d7bc65bcd66799148d4b9ca26fbeca80 | quote: Continue with email
  - [4] 2026-10-31: a REST API manages vals, blob storage, sqlite databases and other resources | capture: sha256:ac7ea44775b486772a948241eae82bbc4d98150f1b9b880eccb5255d96256632 | quote: Val Town's REST API allows you to programmatically manage your account and its resources: vals, blob storage, sqlite databases, likes, comments, and more.
- sources:
  - [1] https://www.val.town/pricing
  - [2] https://www.val.town/limits
  - [3] https://www.val.town/auth/signup
  - [4] https://docs.val.town/reference/api/

## Val Town (Storage)

- `storage/val-town` | fails-quota | evidence reported | binding none | category serverless
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://val.town
- free tier: Free plan blob storage: '10mb on the free plan and 1gb on pro'. Pro is the ceiling, so there is no free path to bulk. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Vals serve HTTP by default with no transfer meter. The serving side is genuinely free. | metered: no
- identity: email
- interface: s3, rest
- limits note: 10 MB total blob storage on Free; 1 min execution timeout; 100,000 runs/day; 80,000 character per-file source limit.
- interface detail: rest
- tooling: `std/blob` TypeScript API (scoped blobs on S3, global blobs on Cloudflare R2); vals themselves are HTTP endpoints at `<val>.web.val.run`.
- composes with: Val creation is capped at 2,500 vals on Free with a 10 MB account-wide blob pool. The pool is per account, not per val, so it does not multiply.
- reliability: The R2/S3 backing is real and fast; the quota is the blocker, not the tech.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Free plan blob storage: '10mb on the free plan and 1gb on pro'. Pro is the ceiling, so there is no free path to bulk.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Blob-stored data counts towards your total Val Town storage – 10mb on the free plan and 1gb on pro' (page last updated September 10, 2026)
  - [2] 2026-10-21: Free: 2,500 vals, 1 min execution timeout, 100,000 runs/day
- sources:
  - [1] https://docs.val.town/std/blob/
  - [2] https://www.val.town/limits

## val town — blob storage

- `storage/val-town-blob-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.val.town/std/blob/
- free tier: none reachable: Blob storage counts against total Val Town storage, which is tiny: 'Blob-stored data counts towards your total Val Town storage – 10mb on the free plan and 1gb on pro.' Three orders of… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Blob storage counts against total Val Town storage, which is tiny: 'Blob-stored data counts towards your total Val Town storage – 10mb on the free plan and 1gb on pro.' Three orders of…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Blob storage counts against total Val Town storage, which is tiny: 'Blob-stored data counts towards your total Val Town storage – 10mb on the free plan and 1gb on pro.' Three orders of…
  - [2] 2026-10-21: cited as the basis of the rejection: Blob storage counts against total Val Town storage, which is tiny: 'Blob-stored data counts towards your total Val Town storage – 10mb on the free plan and 1gb on pro.' Three orders of magni
- sources:
  - [1] https://docs.val.town/std/blob/
  - [2] https://www.val.town/pricing
