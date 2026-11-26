# Tensorlake Sandboxes

> tensorlake.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensorlake/ | JSON https://fshy.ajam.dev/api/v1/entity/tensorlake.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tensorlake Sandboxes

- `compute/tensorlake` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:21:05.671Z (live) | stale on 2026-12-25
- url https://www.tensorlake.ai/pricing
- free tier: a true Free tier at $0 forever with 1 sandbox at a time, 1 vCPU, 1 GB RAM, 10 GB disk, up to 2 hours per session, no credit card required; Usage Credits start at a $5 prepaid pack with up to 100 concurrent sandboxes and up to 24 hours per session; all tiers run on the same Firecracker microVMs | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: the pricing page's SOC 2 Type 2 card states 'Encrypted storage, 7 day retention' for the platform; no separate sandbox data-retention term is published | source: [1]
- egress: Network egress is free: the pricing page states no allowance cap and no per-GB price | metered: no | free allowance: no cap stated; egress is free | source: [1]
- identity: email | detail: the Free tier needs no credit card; unverified: the exact signup fields were not read, so the identity kind is not established beyond an email/account gate
- interface: rest, cli, ssh, scp, sftp, rsync
- limits:
  - request-rate (binding): the Free tier allows 1 sandbox at a time and up to 2 hours per session; Usage Credits allow up to 100 concurrent sandboxes and up to 24 hours per session from $5 prepaid packs [1]
- interface detail: HTTP API, the `tl` CLI, Python and TypeScript SDKs, and standard SSH, scp, sftp and rsync into a sandbox
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The credit is prepaid rather than granted, which is a different product from a free tier and the record says so
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.wall_clock_min: 120
  - session_cap.idle_reap_s: 600
  - session_cap.restart_required: no
  - session_cap.note: 2 hours maximum session on Free, 24 hours on Usage Credits and unlimited on Pro
  - free_tier_kind: prepaid-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free, add prepaid credits when you need more' and '$5 starting credit pack' with 'Up to 100 concurrent sandboxes' and 'Every tier runs on the same Firecracker microVMs', quoted
  - [1] 2026-11-03: no egress charge | capture: sha256:f6637c9bf1779ec7318dd046398728ebc1587d57e32d3c002ba7d20fd66ead09 | quote: Network egress is free.
  - [2] 2026-11-03: SSH, scp, sftp and rsync reach a sandbox | capture: sha256:46f8088cd2a3d948a7cf98e8eeec40f939f4b801740fbe015b1d891536da0bee | quote: connect with `ssh`, `scp`, `sftp`, `rsync`, VS Code Remote-SSH, JetBrains Gateway, and any other tool that speaks SSH
  - [3] 2026-11-03: a REST sandbox API exists | capture: sha256:c52bdb32c0d4784cb7fabebc86e5c07334ef636566f08b253f77677fe845c6b8 | quote: The Tensorlake Sandbox API lets you create isolated runtimes
  - [4] 2026-11-03: the tl CLI exists | capture: sha256:4c5f8049cbf3dfbf0490931d371562b85afc983813262ab4643f6da3e8221e3c | quote: Switch the tl CLI between projects and organizations with contexts, without a new login each time.
  - [5] 2026-11-18:  | capture: sha256:7a5956e446d40d532624355dea5123875837954f423197bd1fdc688102c60315 | quote: | Free | $0 forever | 1 | 1 vCPU, 1 GB RAM, 10 GB root disk | 2 hours |
  - [1] 2026-11-24: a free tier exists without a card | capture: sha256:40c260e03655d5ca9d5370ca8839b006f8b9ffb7d154343e3a606cadd129dff8 | quote: You can start on our Free tier and run 1 sandbox at a time — no credit card required.
  - [1] 2026-11-24: the Free tier states a 7-day retention period | capture: sha256:40c260e03655d5ca9d5370ca8839b006f8b9ffb7d154343e3a606cadd129dff8 | quote: 04SOC 2 Type 2 Encrypted storage, 7 day retention
  - [1] 2026-11-24: the retention period is 7 days | capture: sha256:40c260e03655d5ca9d5370ca8839b006f8b9ffb7d154343e3a606cadd129dff8 | quote: 04SOC 2 Type 2 Encrypted storage, 7 day retention
  - [5] 2026-11-24: the Usage Credits concurrency, resources and session duration | capture: sha256:7a5956e446d40d532624355dea5123875837954f423197bd1fdc688102c60315 | quote: | Usage Credits | Prepaid packs starting at \$5 | Up to 100 | 4 vCPU, 16 GB RAM, 100 GB root disk | 24 hours |
  - [1] 2026-11-24: no card is needed to start on the Free tier | capture: sha256:40c260e03655d5ca9d5370ca8839b006f8b9ffb7d154343e3a606cadd129dff8 | quote: You can start on our Free tier and run 1 sandbox at a time — no credit card required.
  - [1] 2026-11-24: egress is free and credits pay for the other resources | capture: sha256:40c260e03655d5ca9d5370ca8839b006f8b9ffb7d154343e3a606cadd129dff8 | quote: 1 CU = $0.01 of prepaid balance. Credits pay for sandbox CPU, memory, disk, and snapshot storage at the rates below. Network egress is free.
  - [5] 2026-11-24: the Free tier limits | capture: sha256:7a5956e446d40d532624355dea5123875837954f423197bd1fdc688102c60315 | quote: | Free | \$0 forever | 1 | 1 vCPU, 1 GB RAM, 10 GB root disk | 2 hours |
  - [2] 2026-11-24: SSH, scp, sftp and rsync reach a sandbox | capture: sha256:a35d3c69e80e40416f2e3846c4ed624763aafc3115b0dc0722cea536037a2ab1 | quote: * [SSH](#ssh): connect with `ssh`, `scp`, `sftp`, `rsync`, VS Code Remote-SSH, JetBrains Gateway, and any other tool that speaks SSH.
- sources:
  - [1] https://www.tensorlake.ai/pricing
  - [2] https://docs.tensorlake.ai/sandboxes/pty-sessions.md
  - [3] https://docs.tensorlake.ai/api-reference/v2/introduction.md
  - [4] https://docs.tensorlake.ai/llms.txt
  - [5] https://docs.tensorlake.ai/platform/billing.md
