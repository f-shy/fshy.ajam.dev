# Vers

> vers.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vers/ | JSON https://fshy.ajam.dev/api/v1/entity/vers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vers

- `compute/vers` | trial-only | evidence documented | binding none | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T14:51:50.059Z (live) | stale on 2026-12-25
- url https://vers.sh/pricing
- free tier: The pricing page states USD 0.04 per vCPU-hour plus USD 0.01 per GiB-hour of memory and USD 0.09 per GB of network traffic in and out, metered per MB. New organizations get USD 5 in usage credits and USD 50 more when they add a card. From December 1, 2026 disks and commits cost USD 0.10 per GiB-month. | unit: credits | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: starting-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: All network traffic in and out of VMs, in both directions, is metered per MB and billed at USD 0.09 per GB; there is no free allowance. | metered: yes | price per TB: USD 90 per TB | source: [1]
- identity: card | detail: New organizations receive USD 5 in usage credits without a card and USD 50 more when they add a card. The page does not state which identifier opens the account; prepaid credit is bought with a card and running computers are paused when the balance falls USD 5 below zero.
- interface: cli, ssh
- limits note: No session cap, no idle reap and no monthly minimum are published; the first thing that actually stops a fleet is the monthly card charge for whatever ran, since paused VMs accrue nothing.
- binding note: No monthly minimums, tier floors or annual commits are published. Vers is prepaid: usage is deducted hourly and new computers cannot start at a zero balance.
- interface detail: The docs.vers.sh CLI reference documents the standalone vers CLI binary (HTTPS control plane) and an SSH gateway at try.vers.sh; no REST API reference or SDK was read on that page.
- tooling: The vers CLI, a standalone Rust binary installed locally, and the ssh try.vers.sh gateway; the CLI reference page names no SDK or API library.
- composes with: Paused VMs are free, so the shape that pays off is a fleet of branched computers parked between agent steps: 100 paused branches cost nothing, and only the one being worked on bills at USD 0.04 per vCPU-hour.
- reliability: no reliability event recorded
- notes: The pricing page quantifies the starting credit as USD 5, plus USD 50 when a card is added. Storage is billed from December 1, 2026 at USD 0.10 per GiB-month for VM disks and commit snapshots. The CLI defaults to 2 vCPUs and 4096 MiB, so vCPU time alone at the published rate is USD 58.40 for 730 hours of 24/7 use.
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
  - [1] 2026-11-24: memory, network-traffic, storage and per-GB rates are stated on the pricing page | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: Plus $0.01 per GiB-hour of memory allocated to a running VM, billed per second, $0.09 per GB of network traffic in and out of your VMs, metered per MB, and from December 1, 2026 $0.10 per GiB-month for VM disks and commits.
  - [1] 2026-11-24: the free allowance is a credit amount, not hours | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: Yes. New organizations get $5 in usage credits, and $50 more when they add a card. Credits are applied automatically to compute, memory, and network traffic. When they run out, buy more with a card or turn on auto-reload.
  - [1] 2026-11-24: network traffic in both directions is metered per MB at USD 0.09 per GB | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: All data in and out of your VMs' network interfaces, in both directions, including traffic between your own VMs. It's metered per MB and billed at $0.09 per GB.
  - [1] 2026-11-24: network traffic is metered per MB | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: All data in and out of your VMs' network interfaces, in both directions, including traffic between your own VMs. It's metered per MB and billed at $0.09 per GB.
  - [1] 2026-11-24: the page states USD 0.09 per GB of network traffic | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: $0.09 per GB
  - [1] 2026-11-24: adding a card unlocks a further USD 50 of credit | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: Yes. New organizations get $5 in usage credits, and $50 more when they add a card. Credits are applied automatically to compute, memory, and network traffic. When they run out, buy more with a card or turn on auto-reload.
  - [1] 2026-11-24: the credit tiers depend on whether a card was added | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: Yes. New organizations get $5 in usage credits, and $50 more when they add a card. Credits are applied automatically to compute, memory, and network traffic. When they run out, buy more with a card or turn on auto-reload.
  - [1] 2026-11-24: no monthly minimums, tier floors or annual commits | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: No monthly minimums, no tier floors, no annual commits. Pay for what you use.
  - [1] 2026-11-24: storage is billed from December 1, 2026 at a stated per-GiB-month rate | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: from December 1, 2026 $0.10 per GiB-month for VM disks and commits
  - [1] 2026-11-24: vCPU time is billed per second and paused VMs and commits do not accrue | capture: sha256:6b25419d1c54fa3ff2d24cb8d1e020d087b5c7454b365e852e4080ec365cab8e | quote: Charged per second of wall-clock time a VM is allocated CPU. Paused VMs and commits don't accrue vCPU time.
  - [2] 2026-11-24: the locally installed CLI defaults to 2 vCPUs and 4096 MiB | capture: sha256:4b335ddc33334a2225989cce8b186408f8f3555e5639b5c5d78a449b09654f5b | quote: Defaults are 2 vCPUs, 4096 MiB memory, a 120-second wait, and the platform's managed default image.
- sources:
  - [1] https://vers.sh/pricing
  - [2] https://docs.vers.sh/cli-reference/overview.md
