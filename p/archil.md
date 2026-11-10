# Archil

> archil.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archil/ | JSON https://fshy.ajam.dev/api/v1/entity/archil.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Archil

- `compute/archil` | qualifies-with-caveat | evidence documented | binding per-object-cap | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T15:51:56.484Z (live) | stale on 2026-12-05
- url https://archil.com/pricing
- free tier: Free includes 5 disks of up to 10 GB each, 1,000 serverless tool calls, and 1 hour of sandbox compute a month (1 vCPU-hour and 2 GiB-hours), with up to 5 concurrent sandboxes and sessions of up to 30 minutes, as hard caps with no overage | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: data transfer out of Archil is $0.07 per GB on Developer and Team, not included on Free, custom on Enterprise; transfer within Archil is free | metered: yes | free allowance: none stated: Free does not include data transfer out; Developer and Team list no included volume | price per TB: $70 per TB ($0.07 per GB on Developer and Team) | source: [1]
- identity: email | detail: an email address and nothing further: 'Signing up for Archil is free with no credit card required.', and a console session is opened with 'Enter the email address associated with your Archil account, then enter the verification code we send you.' The pricing page prints 'No credit card required.' for the Free plan, and an API key is created from the console after sign-up.
- interface: s3-compatible, cli, rest
- limits:
  - request-rate: 1,000 serverless tool calls and 30 minutes of sandbox compute on Free [1]
  - per-object-cap (binding): 5 disks of up to 10 GB each on Free [1]
  - request-rate: 5 concurrent sandboxes on Free, 250 on Team [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: S3 API and a REST API, the `disk` and `archil` CLIs, TypeScript and Python SDKs; disks mount as local folders on Linux
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free allowances as hard caps with no overage, plus the metered paid rates. The disk count and per-disk cap are the two numbers a storage reader needs
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 30 minutes of sandbox compute in total on Free, as a hard cap with no overage
  - free_tier_kind: allowance
  - burst_x: 1.0
  - ps.gib: 10
  - ps.price: included within Free's hard caps; $0.025 a GB-month of archive storage on paid plans
  - ps.durability: disk, synchronised to a customer-owned bucket if configured
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the disk exists
  - net.out: yes
  - net.in: yes
  - net.allowance: $0.07 a GB of egress on paid plans; transfer within Archil is free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free includes 5 disks of up to 10 GB each, 1,000 serverless tool calls, and 30 minutes of sandbox compute, with up to 5 concurrent sandboxes. These are hard caps, with no overage.' and 'On Developer and Team, CPU is metered at $0.055 per vCPU-hour and memory at $0.020 per GiB-hour', quoted
  - [1] 2026-11-04: data transfer out is not included on Free and costs $0.07 per GB on Developer and Team | capture: sha256:8799c616dd075f5300a7f9aeb697919f3feb29a289988981b2e0f4ef76aea07a | quote: | Data transfer out of Archil | –Not included | $0.07 / GB | $0.07 / GB | Custom |
  - [2] 2026-11-04: egress is $0.07 per GB | capture: sha256:34f7558cc16ebdc3ec1220acbbfc6f3074485e9af4b1d7720604819528a40d05 | quote: Data leaving Archil, including delivery to external compute, costs \$0.07 per GB.
  - [3] 2026-11-04: managed disks are reachable over an S3 API | capture: sha256:e5bc0dfab54890c468397acf975b47c8e4d4d236494e279082bbe8726b850db1 | quote: Managed disks export with any S3 client over the [S3 API](https://docs.archil.com/protocols/s3-api.md).
  - [4] 2026-11-04: a disk CLI exists | capture: sha256:c0ed40e6aee3d8d88000ef72bae3c19fd50737b9b577fc3ec27b5568cc6764ea | quote: [`disk` CLI](https://docs.archil.com/reference/disk-cli.md): Reference for the Node CLI that creates disks, runs `disk exec`, and manages API keys.
  - [1] 2026-11-04: Free gives 1 hour of sandbox compute a month, 30 minutes per session | capture: sha256:8799c616dd075f5300a7f9aeb697919f3feb29a289988981b2e0f4ef76aea07a | quote: Free includes 5 disks of up to 10 GB each, 1,000 serverless tool calls, and 1 hour of sandbox compute a month
  - [5] 2026-11-04: sign-up is free and takes no credit card; an account is still created to hold the API key | capture: sha256:62e69cb6d7ff5056815e659ed0c990284fdcaaf1fa8d2c4f658fbb07442e0406 | quote: Signing up for Archil is free with no credit card required.
  - [1] 2026-11-04: the Free plan is advertised without a card | capture: sha256:8799c616dd075f5300a7f9aeb697919f3feb29a289988981b2e0f4ef76aea07a | quote: No credit card required.
  - [6] 2026-11-04: the account is keyed to an email address and its code | capture: sha256:47d6b7e06b637519bf759455eec38e93504751b8916e6cdcc304b45a3d9c4c3f | quote: Enter the email address associated with your Archil account, then enter the verification code we send you.
- sources:
  - [1] https://archil.com/pricing
  - [2] https://docs.archil.com/administration/billing.md
  - [3] https://docs.archil.com
  - [4] https://docs.archil.com/llms.txt
  - [5] https://docs.archil.com/api-reference/introduction
  - [6] https://docs.archil.com/mounting/macos
