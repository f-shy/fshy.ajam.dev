# Vers

> vers.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vers/ | JSON https://fshy.ajam.dev/api/v1/entity/vers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vers

- `compute/vers` | trial-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:47.110Z (live) | stale on 2026-12-05
- url https://vers.sh/pricing
- free tier: A single metered rate of USD 0.04 per vCPU-hour, billed per second, with memory included and no tiers. Paused VMs, stopped VMs, commits, snapshots and branches do not accrue compute. No monthly minimum and no per-fork fee. 'New accounts get credits to prototype and run small experiments before a card is required' (amount not stated). | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: starting-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: The credit amount is not stated, and which identifier the account is created with is not stated in the evidence
- interface: cli, ssh
- limits note: No session cap, no idle reap and no monthly minimum are published; the first thing that actually stops a fleet is the monthly card charge for whatever ran, since paused VMs accrue nothing.
- binding note: the same as limits note
- interface detail: The docs.vers.sh CLI reference documents the standalone vers CLI binary (HTTPS control plane) and an SSH gateway at try.vers.sh; no REST API reference or SDK was read on that page.
- tooling: The vers CLI, a standalone Rust binary installed locally, and the ssh try.vers.sh gateway; the CLI reference page names no SDK or API library.
- composes with: Paused VMs are free, so the shape that pays off is a fleet of branched computers parked between agent steps: 100 paused branches cost nothing, and only the one being worked on bills at USD 0.04 per vCPU-hour.
- reliability: no reliability event recorded
- notes: Storage for kept commits is billed and its rate is not on the pricing page. Isolation is a full VM rather than a microVM or container. For a month of 24/7 at the CLI default of 2 vCPU / 4 GiB the arithmetic is 2 x 730 x 0.04 = USD 58.40, which sits between bunny.net (USD 43.80 at 2 core / 4 GB) and inis.run (about USD 29.50 equivalent).
- extras:
  - facets.class: per-second-vm
  - facets.free_tier_kind: starting-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
- evidence:
  - [1] 2026-10-22: USD 0.04 per vCPU-hour, 1 second granularity, no per-branch fee, paused and stopped VMs do not accrue, 4 vCPUs 24x7 for a month is USD 116.80, and new accounts get credits before a card is required
  - [2] 2026-10-22: CLI defaults are 2 vCPUs and 4096 MiB memory, so the default computer costs USD 0.08 per hour at the published rate
  - [1] 2026-10-22: 
  - [2] 2026-11-03: an SSH gateway is a documented interface next to the CLI | capture: sha256:3dbd07e2e943584653e10836777eca4a993d31927ffc8cf88182474f07c2c568 | quote: ssh try.vers.sh ssh devbox
  - [2] 2026-11-04: the provider documents an SSH gateway at try.vers.sh | capture: sha256:3dbd07e2e943584653e10836777eca4a993d31927ffc8cf88182474f07c2c568 | quote: ssh try.vers.sh ssh devbox
  - [2] 2026-11-04: the provider documents a standalone vers CLI binary against an HTTPS control plane | capture: sha256:3dbd07e2e943584653e10836777eca4a993d31927ffc8cf88182474f07c2c568 | quote: The standalone `vers` binary talks directly to the HTTPS control plane.
- sources:
  - [1] https://vers.sh/pricing
  - [2] https://docs.vers.sh/cli-reference/overview.md
