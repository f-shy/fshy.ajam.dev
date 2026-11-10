# CircleCI

> circleci.com | Compute, CI runners, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/circleci/ | JSON https://fshy.ajam.dev/api/v1/entity/circleci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CircleCI

- `compute/circleci` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:31.498Z (live) | stale on 2026-11-22
- url https://circleci.com/pricing/price-list/
- duplicate of `ci-cd-runners/circleci-free`
- free tier: free tier published without a credit amount | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): machine time costs from 5 to 120 credits a minute depending on the resource class [1]
  - write-gated: the price list states no free plan; the free allowance is on a page this record does not cite [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the price list was read on 2026-10-22 and carries the machine rates as credits per minute. The free allowance is not on this page, so the record's free-tier claim is not settled by it and the rung stays `reported` on that field
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a job has its own timeout; the credit balance is what runs out
  - free_tier_kind: allowance
  - granularity.min_billed_s: 1
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the price list was read on 2026-10-22 and publishes per-minute credit costs from 5 credits a minute to 120: 'Cost (credits/min) 5 credits/min, 10, 15, 20, 40, 80, 100'. It states no free plan on this page
- sources:
  - [1] https://circleci.com/pricing/price-list/

## CircleCI Free

- `ci-cd-runners/circleci-free` | qualifies-with-caveat | evidence documented | binding request-rate | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-10-30T12:41:30.391Z (live) | stale on 2026-11-30
- url https://circleci.com/pricing/
- free tier: 30,000 credits a month on the Free plan, with up to 5 active users and 30x concurrency; open-source projects get up to 400,000 credits a month for Linux, Arm and Docker builds, and macOS and Windows open-source builds draw on the 30,000 | unit: credits | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: 1 hour maximum job runtime on the Free plan; 3 hours on Performance and 5 hours on Scale
- retention: credits expire monthly and do not roll over; caches and artifacts expire per configuration | source: [2]
- egress: network transfer is billed only for traffic from CircleCI to self-hosted runners; the Free plan includes 1 GB of network transfer and 2 GB-months of storage, and use beyond these draws from the monthly credits at 420 credits per GB | metered: no | source: [2]
- identity: email | detail: an email address and a password, verified by email, for GitHub, GitLab or Cursor Origin projects; a Bitbucket account for Bitbucket Cloud projects; the Free plan needs no credit card
- interface: git, cli
- limits:
  - request-rate (binding): 30,000 credits a month on Free; every credit expires at the end of the month [1]
  - request-rate (binding): 30x concurrency on Free, and 5 active users [1]
  - per-object-cap: 1 hour maximum job runtime on the Free plan [3]
- interface detail: a .circleci/config.yml pipeline; the CircleCI API and CLI
- tooling: the CircleCI convenience images; docker; any shell
- composes with: the largest credit pool of the hosted CI providers here, and the only one that scales with public rather than private visibility by a factor above ten
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: Every job on the Free plan stops at 1 hour, so both the 400,000-credit open-source pool and the 30,000-credit pool are spent in jobs of at most 1 hour. The vendor's credits page gives the macOS open-source allowance as 30,000 credits a month in one section and 25,000 in another, so that figure is unsettled.
- evidence note: the pricing page was read; the credits doc was read for the overage rate. The 5,000-credit figure in circulation is the pre-2025 plan.
- evidence:
  - [1] 2026-10-22: Free: 30,000 credits a month, 5 active users, 30x concurrency; 400,000 credits a month for public repositories
  - [2] 2026-10-22: credits are consumed by machine size and duration; network and storage beyond the threshold are 420 credits per GB
  - [1] 2026-10-30: the 400,000-credit pool is for open-source Linux, Arm and Docker builds | capture: sha256:9330f40ac10bbe3ec8e64ad253b39c6dbfbd87802d7d5717e4b0e83820ca648a | quote: Open source projects can access up to 400,000 credits per month (equivalent to 80,000 build minutes) to use on Linux, Arm, and Docker.
  - [1] 2026-10-30: the Free plan is metered in credits, 30,000 a month | capture: sha256:9330f40ac10bbe3ec8e64ad253b39c6dbfbd87802d7d5717e4b0e83820ca648a | quote: | Credits | 30,000 free credits/month | /month included | Custom |
  - [3] 2026-10-30: a job on the Free plan stops at 1 hour | capture: sha256:965521fedc2c9922515e97f80815a5be3ea8d6261ea0c100c613aabd2bf2b79f | quote: Jobs have a maximum runtime of 1 (Free), 3 (Performance), or 5 (Scale) hours depending on pricing plan.
  - [4] 2026-10-30: a build on the Free plan stops at 1 hour | capture: sha256:2be0afadc1f88f1c0558f0dfbd8cf5139f2b394824acceebbe7eb3491ffb4782 | quote: In particular, builds on the Free plan are limited to a maximum duration of 1 hour.
  - [2] 2026-10-30: the Free plan includes 1 GB of network transfer and 2 GB-months of storage | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: Free organizations also receive an included allotment of 1 GB of network transfer and 2 GB-months of storage.
  - [2] 2026-10-30: outbound traffic from a hosted job is not billed; only traffic to self-hosted runners is | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: Billing for network usage is only applicable to traffic from CircleCI to self-hosted runners.
  - [5] 2026-10-30: sign-up is by email address for GitHub, GitLab and Cursor Origin projects | capture: sha256:0ba35164d75f8b10097414bb916523baa0f95ea3883da2bee1d247882e875fb7 | quote: If you want to build mainly GitHub, GitLab, or Cursor Origin projects, sign up with your email address to create an account.
  - [5] 2026-10-30: Bitbucket Cloud projects sign up with a Bitbucket account | capture: sha256:0ba35164d75f8b10097414bb916523baa0f95ea3883da2bee1d247882e875fb7 | quote: If you want to primarily build Bitbucket Cloud projects, sign up with your Bitbucket account.
  - [1] 2026-10-30: the Free plan needs no credit card | capture: sha256:9330f40ac10bbe3ec8e64ad253b39c6dbfbd87802d7d5717e4b0e83820ca648a | quote: No credit card required.
  - [2] 2026-10-30: one section of the credits page gives the macOS open-source allowance as 25,000 credits a month | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: If you build on macOS, we also offer organizations on our Free Plan 25,000 free credits per month to use on macOS open source builds.
  - [1] 2026-10-30: Free-plan credits are monthly and do not roll over | capture: sha256:9330f40ac10bbe3ec8e64ad253b39c6dbfbd87802d7d5717e4b0e83820ca648a | quote: Credits on the Free plan expire after a month and do not roll over.
- sources:
  - [1] https://circleci.com/pricing/
  - [2] https://docs.circleci.com/guides/plans-pricing/credits
  - [3] https://support.circleci.com/en/articles/15091447-max-runtime-in-circleci-server
  - [4] https://support.circleci.com/hc/en-us/articles/4410707277083-Context-deadline-exceeded-after-1-hour-Build-timed-out-Free-tier-only
  - [5] https://circleci.com/docs/guides/getting-started/first-steps/

## CircleCI artifacts

- `storage/circleci-artifacts` | fails-quota | evidence reported | binding retention-clamped | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-03T01:28:30.555Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://circleci.com
- free tier: The Free plan (30,000 credits a month) includes 1 GB of network transfer and 2 GB-months of storage; storage beyond that draws from the monthly credits at 420 credits per GB-month. Artifact retention default and maximum is 30 days. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 3 GB maximum size for an individual artifact file | source: [1] | note: not stated
- retention: Artifact retention default AND maximum is 30 days on Cloud; storage usage is a billed meter, not an allowance | days: 30 | source: [1] | note: not stated
- egress: Free download from app.circleci.com; artifacts are 'protected with your CircleCI account for private projects'. Public-project artifacts are reachable, private are not. | metered: no
- identity: email | detail: an email address for GitHub, GitLab or Cursor Origin projects; a Bitbucket account for Bitbucket Cloud projects; the Free plan needs no credit card
- interface: s3, rest, rclone
- limits:
  - retention-clamped (binding): retention default AND maximum is 30 days [1]
  - retention-clamped (binding): retention 30 days [1]
- limits note: 3 GB max per individual artifact file; retention 30 days maximum (workspaces/caches 15 days max); storage beyond plan is billed.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: REST v2 artifacts endpoint; artifacts stored on Amazon S3 behind CircleCI. No rclone backend, no first-class bulk client.
- composes with: Unlimited projects x 3 GB per file, but the 30-day hard ceiling makes this a rolling buffer, not storage.
- reliability: 30-day deletion is unconditional and irreversible. Purely a CI convenience store.
- notes: No storage quota advertised on Free (30,000 credits/month). Artifact retention default AND maximum is 30 days on Cloud; storage usage is a billed meter, not an allowance.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No storage quota advertised on Free (30,000 credits/month). Artifact retention default AND maximum is 30 days on Cloud; storage usage is a billed meter, not an allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Individual artifact files have a maximum size limit of 3GB'; 'By default, artifact storage duration is set to 30 days ... Currently, 30 days is also the maximum storage duration you can set'
  - [2] 2026-10-21: 'Artifacts (default and maximum is 30 days)'
  - [3] 2026-10-21: Free plan, 30,000 credits
  - [4] 2026-11-03: the Free plan includes 2 GB-months of storage | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: Free organizations also receive an included allotment of 1 GB of network transfer and 2 GB-months of storage.
  - [4] 2026-11-03: storage usage beyond the allotment is paid from the monthly credits | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: Network and storage usage beyond these allotments draws from your monthly credits rather than being billed separately.
  - [4] 2026-11-03: overage is priced at 420 credits per GB-month | capture: sha256:0ffd874a0bf8cc540f5146b50da7f604a23275149ceadefdb336e93ed7abf334 | quote: Your overage (GB-Months/TB-Months) can be multiplied by 420 credits to estimate the total monthly costs.
  - [1] 2026-11-03: the per-file artifact cap is 3 GB | capture: sha256:7945368e8801131f8690eee883e20fe8c9dd2246c6286d3582027c3908666e84 | quote: Individual artifact files have a maximum size limit of 3GB.
  - [5] 2026-11-03: sign-up for GitHub, GitLab and Cursor Origin projects is by email address | capture: sha256:0ba35164d75f8b10097414bb916523baa0f95ea3883da2bee1d247882e875fb7 | quote: If you want to build mainly GitHub, GitLab, or Cursor Origin projects, sign up with your email address to create an account.
  - [3] 2026-11-03: the Free plan asks for no credit card | capture: sha256:9330f40ac10bbe3ec8e64ad253b39c6dbfbd87802d7d5717e4b0e83820ca648a | quote: No credit card required.
  - [1] 2026-11-03: artifact retention maximum is 30 days | capture: sha256:7945368e8801131f8690eee883e20fe8c9dd2246c6286d3582027c3908666e84 | quote: Currently, 30 days is also the maximum storage duration you can set.
- sources:
  - [1] https://circleci.com/docs/guides/optimize/artifacts/
  - [2] https://circleci.com/docs/guides/optimize/persist-data/
  - [3] https://circleci.com/pricing/
  - [4] https://docs.circleci.com/guides/plans-pricing/credits
  - [5] https://circleci.com/docs/guides/getting-started/first-steps/
