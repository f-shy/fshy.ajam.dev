# Tensorlake Sandboxes

> tensorlake.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensorlake/ | JSON https://fshy.ajam.dev/api/v1/entity/tensorlake.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tensorlake Sandboxes

- `compute/tensorlake` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.818Z (live) | stale on 2026-12-05
- url https://www.tensorlake.ai/pricing
- free tier: $5 to $20 prepaid credit packs to start, up to 100 concurrent sandboxes, on the same Firecracker microVMs as the paid tiers | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Network egress is free: the pricing page states no allowance cap and no per-GB price | metered: no | free allowance: no cap stated; egress is free | source: [1]
- identity: email
- interface: rest, cli, ssh, scp, sftp, rsync
- limits:
  - request-rate (binding): up to 100 concurrent sandboxes; prepaid credit packs start at $5 [1]
- interface detail: HTTP API, the `tl` CLI, Python and TypeScript SDKs, and standard SSH, scp, sftp and rsync into a sandbox
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The credit is prepaid rather than granted, which is a different product from a free tier and the record says so
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published
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
- sources:
  - [1] https://www.tensorlake.ai/pricing
  - [2] https://docs.tensorlake.ai/sandboxes/pty-sessions.md
  - [3] https://docs.tensorlake.ai/api-reference/v2/introduction.md
  - [4] https://docs.tensorlake.ai/llms.txt
