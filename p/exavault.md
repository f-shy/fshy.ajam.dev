# ExaVault

> exavault.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exavault/ | JSON https://fshy.ajam.dev/api/v1/entity/exavault.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExaVault (Files.com) — free self-hosted appliance

- `storage/exavault-free-self-hosted-appliance` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category iaas
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-11-19
- url https://www.exavault.com/pricing
- free tier: ExaVault Cloud, the hosted product, was sunset. The on-premise appliance is still maintained and is free for up to 50 users with no expiry and no throttling. Capacity is the disk the user attaches to a machine they run; there is no hosted storage. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A. Egress is your own VM's bandwidth. Note: 'Encryption at rest comes from your VM environment'. | metered: no
- identity: card | detail: unverified: how the free image and its license key are obtained was not seen; a valid license key file is required for free and paid installations
- interface: rest, webdav, sftp, ftp
- limits note: per-object-cap none imposed by the software; retention none; the binding constraints become your VM's disk and network. Paid tier adds SSO/2FA/syslog and >50 users ($99/mo per 50-user pack).
- interface detail: sftp / ftp / webdav / rest (web manager, share links)
- tooling: the user installs and runs the appliance image (VMware OVA, AWS Marketplace or GCP Marketplace image) on a rented or free machine; 4 CPU / 12 GB RAM / 100 GB primary disk plus a sized data drive; every installation needs outbound HTTPS to a license service and one source IP address
- composes with: Unlimited free 'accounts' (appliance deployments) x whatever disk you attach. This is not free storage. It is free software for storage you already pay for. Worth recording because the category's free tier has structurally migrated here: the vendor monetises seats and support, not bytes.
- reliability: Free tier is 'never feature-degraded and never throttled' but ships no support channel and manual updates only.
- notes: The hosted product is gone. What is free is the appliance: unlimited capacity on your own disk, licensed for up to 50 users, no expiry, no throttling. There is no free hosted storage at all.
- evidence note: Re-read on 2026-11-04: https://www.exavault.com/ (hosted cloud sunset, appliance maintained), https://www.exavault.com/pricing (free up to 50 users, no expiry), https://docs.exavault.com/administration/license-keys.md (license key file required) and https://docs.exavault.com/ (the user operates the deployment). How the free image and its license key are obtained was not seen, so confidence stays at reported.
- self hosted: yes
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The hosted product is gone. What is free is the appliance: unlimited capacity on your own disk, licensed for up to 50 users, no expiry, no throttling. There is no free hosted storage at all.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The ExaVault on-prem appliance is free for deployments up to 50 users', 'The Free tier never expires, is never feature-degraded, and is never throttled', 'Because the appliance runs in your environment, the compliance posture ... is your scope'
  - [2] 2026-10-21: 'Free SFTP & FTP Server · ExaVault by Files.com'
  - [2] 2026-11-03: the hosted ExaVault Cloud product was sunset | capture: sha256:f2f6d0583966d191ca978031aa3aa6f3371566f088b85529b1043846fd7ec21f | quote: ExaVault Cloud was sunset and its mission carried forward by Files.com
  - [1] 2026-11-03: system requirements of the appliance | capture: sha256:f503077f3967da0aabdf62f28738a1a5a8baadfd45c99c51efffcfd12df21eb2 | quote: System requirements: 64-bit Intel, 4 CPU / 12 GB RAM / 100 GB primary disk plus a sized data drive.
  - [3] 2026-11-03: free installations need a license key file | capture: sha256:86ea836739fb85235a580e7730d2845085547af50cf22148d396b98af468da68 | quote: a valid license key file is required for both free and paid usage.
  - [1] 2026-11-03: the free appliance has no expiry or throttle and is licensed for up to 50 users | capture: sha256:f503077f3967da0aabdf62f28738a1a5a8baadfd45c99c51efffcfd12df21eb2 | quote: No. The Free tier never expires, is never feature-degraded, and is never throttled — it is the full appliance, licensed for up to 50 users, and you can run it in production as long as you like.
  - [2] 2026-11-03: the on-premise appliance is still maintained | capture: sha256:f2f6d0583966d191ca978031aa3aa6f3371566f088b85529b1043846fd7ec21f | quote: The on-premise appliance is still maintained by Files.com for self-hosted shops
  - [1] 2026-11-03: image formats | capture: sha256:f503077f3967da0aabdf62f28738a1a5a8baadfd45c99c51efffcfd12df21eb2 | quote: The appliance ships as a VMware OVA, an AWS Marketplace image, and a GCP Marketplace image.
  - [4] 2026-11-03: the user deploys and operates the appliance and its storage | capture: sha256:ec5cde714776d3f9fbc909e45c6b03250d66bac5485f237144fc4cf7fd5c211e | quote: You deploy ExaVault in your cloud account or virtual-machine environment and operate the compute, storage, network, firewall, backups, and availability of that deployment.
  - [3] 2026-11-03: one source IP address per installation | capture: sha256:86ea836739fb85235a580e7730d2845085547af50cf22148d396b98af468da68 | quote: each ExaVault installation must be associated with a single IP address at any given time.
  - [1] 2026-11-04: the free appliance has no expiry or throttle and is licensed for up to 50 users | capture: sha256:f503077f3967da0aabdf62f28738a1a5a8baadfd45c99c51efffcfd12df21eb2 | quote: No. The Free tier never expires, is never feature-degraded, and is never throttled — it is the full appliance, licensed for up to 50 users, and you can run it in production as long as you like.
- sources:
  - [1] https://www.exavault.com/pricing
  - [2] https://www.exavault.com/
  - [3] https://docs.exavault.com/administration/license-keys.md
  - [4] https://docs.exavault.com/
