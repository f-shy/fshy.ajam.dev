# strada

> strada.tech | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/strada/ | JSON https://fshy.ajam.dev/api/v1/entity/strada.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## strada

- `storage/strada` | self-hosted, last resort | verdict fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.356Z (live) | stale on 2026-12-05
- url https://strada.tech/
- free tier: none: Strada does not rent storage; the Free plan ($0) connects unlimited computers and unlimited storage, for file review. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- binding note: no byte allowance exists because the vendor does not rent storage
- interface detail: not documented
- tooling: The user installs and runs the Strada app (macOS 13+, Windows 11, iOS, Android), which mounts a remote drive as a virtual drive; the storage itself is supplied by the user.
- composes with: not recorded
- reliability: Strada mounts a drive held by the sharer on the editor's computer over a peer-to-peer connection with no cloud in between, so the bytes stay on the sharer's own drive.
- notes: Paid plans are per user per month: Basic $8 (file editing and transfer, remote editing with Strada Connect) and Pro $24; the Free plan ($0) is for file review. A 7-day free trial is offered.
- evidence note: re-read on 2026-11-03: the vendor pages https://strada.tech/, https://strada.tech/pricing and https://strada.tech/downloads; they state that the vendor does not rent storage, that remote editing runs peer to peer with no cloud in between, and the plan prices; the app platforms are listed on the downloads page
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Real iroh-shaped product (remote editing off somebody else's hard drive, 'upload nothing', 7 TB of source media over home internet per their case study) but it is an app, not a storage…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Real iroh-shaped product (remote editing off somebody else's hard drive, 'upload nothing', 7 TB of source media over home internet per their case study) but it is an app, not a storage…
  - [2] 2026-10-21: cited as the basis of the rejection: Real iroh-shaped product (remote editing off somebody else's hard drive, 'upload nothing', 7 TB of source media over home internet per their case study) but it is an app, not a storage provi
  - [3] 2026-10-21: cited as the basis of the rejection: Real iroh-shaped product (remote editing off somebody else's hard drive, 'upload nothing', 7 TB of source media over home internet per their case study) but it is an app, not a storage provi
  - [3] 2026-11-03: the vendor supplies no storage | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
  - [1] 2026-11-03: peer-to-peer mount, no hosted storage | capture: sha256:3726579210fe9678ee9ddb93d230c30af3355427ef597514fb0b61bd68f6b329 | quote: Your footage stays on your hard drive, wherever your editor is. Strada mounts it on their computer over a peer-to-peer connection, with no cloud in between.
  - [2] 2026-11-03: Basic plan price | capture: sha256:012ea9650c7481464266656186645b24abb7fc8637c161b8a3cc6d5616e471fa | quote: Basic For file editing & transfer ## $8 per user per month
  - [2] 2026-11-03: Pro plan price | capture: sha256:012ea9650c7481464266656186645b24abb7fc8637c161b8a3cc6d5616e471fa | quote: Pro Get the most out of Strada Recommended ## $24 per user per month
  - [2] 2026-11-03: Free plan price | capture: sha256:012ea9650c7481464266656186645b24abb7fc8637c161b8a3cc6d5616e471fa | quote: For file review ## $0
  - [1] 2026-11-03: free trial length | capture: sha256:3726579210fe9678ee9ddb93d230c30af3355427ef597514fb0b61bd68f6b329 | quote: Try it free for 7 days.
  - [2] 2026-11-03: remote editing is in the priced plans; no plan includes storage | capture: sha256:012ea9650c7481464266656186645b24abb7fc8637c161b8a3cc6d5616e471fa | quote: Basic For file editing & transfer ## $8 per user per month
  - [3] 2026-11-03: app mounts remote storage as a virtual drive | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: Mount remote storage as a virtual drive. Edit, share, and collaborate on remote media as if it lives on your desk.
  - [3] 2026-11-03: no storage is supplied | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
  - [3] 2026-11-03: no hosted storage is offered | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
  - [3] 2026-11-03: no plan of the vendor, free or paid, supplies storage, so the storage allowance is none; paid plans sell remote editing, not capacity | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
  - [3] 2026-11-03: the vendor supplies no storage; the free tier holds none | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
  - [3] 2026-11-04: the vendor supplies no storage | capture: sha256:b4d4efa28311ba890d6a7ba4dbd9ff2e85d9a63ea4ae5caf6e54d83c1d1704f5 | quote: We don't rent storage.
- sources:
  - [1] https://strada.tech/
  - [2] https://strada.tech/pricing
  - [3] https://strada.tech/downloads
