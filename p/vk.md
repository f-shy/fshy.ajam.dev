# VK Cloud

> vk.ru | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vk/ | JSON https://fshy.ajam.dev/api/v1/entity/vk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VK Cloud

- `compute/vk-cloud` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://cloud.vk.ru/bonus/
- free tier: RUB 5,000 of welcome bonuses for an individual account and RUB 12,000 for a legal entity, valid 60 days once credited. Of the RUB 5,000 for an individual, RUB 2,000 is usable on virtual machines and their backups and RUB 3,000 on other services; licensed products, the marketplace and CDN are excluded. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The bonus is conditioned on the account being registered from an IP address in Russia and on a corporate-domain email address being confirmed, so the individual RUB 5,000 lane is closed to a registrant outside Russia even though no passport is asked for. [1]
- limits note: The bonus is conditioned on the account being registered from an IP address in Russia and on a corporate-domain email address being confirmed, so the individual RUB 5,000 lane is closed to a registrant outside Russia even though no passport is asked for.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: RUB 2,000 of VM-only bonus at the Russian CPU rate is a few weeks of a 2-vCPU box, and the RUB 3,000 half cannot be spent on the VM, so the effective VM credit is 40 per cent of the headline.
- reliability: no reliability event recorded
- notes: The useful number here is not the RUB 5,000 but the split: 40 per cent of the individual bonus reaches virtual machines. The startup grant is the large figure (up to RUB 2,000,000, with RUB 500,000 for months one and two and up to RUB 1,500,000 for months three to six) and it is entity-gated, so it is fails-identity with the number beside the reason. The IP-in-Russia condition is the constraint no identity document satisfies, which is unusual: most Russian providers gate on the phone, this one gates on the network.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: ' VK Cloud: 5000 12 000 - ' (RUB 5,000 for individuals, RUB 12,000 for legal entities), ' IP- , ' (the account must be registered on a corporate domain from an IP address in Russia), ' 60 ' (valid 60 days), quoted
  - [1] 2026-10-22: ' 5000 2000 - , 3000 - ' (of the 5,000, 2,000 is usable on VMs and backups), and the RUB 12,000 entity tier requires ' ', ' ', ' ' for sole traders, quoted
  - [2] 2026-10-22: ' 5000 VK Cloud, 60 ' (after activation we contact you and credit RUB 5,000 for 60 days), quoted
  - [3] 2026-10-22: ' VK Cloud 2026 ' (the account must be registered to a legal entity or sole trader in 2026) for the startup grant of up to RUB 2,000,000 over six months, quoted
- sources:
  - [1] https://cloud.vk.ru/bonus/
  - [2] https://cloud.vk.ru/pricing/
  - [3] https://cloud.vk.ru/startup/

## VK Cloud Object Storage

- `storage/vk-cloud-object-storage` | fails-egress | evidence reported | binding retention-clamped | category iaas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloud.vk.ru/storage/
- free tier: No perpetual free volume. Pay-as-you-go per GB, per storage class (Hotbox/Icebox/Backup). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: bonus expires in 60 days and unused balance is revoked; bonus cannot be spent on CDN, licences or marketplace | days: 60 | source: [1] | note: not stated
- egress: Metered: 'Outgoing traffic is any downloading of information from the bucket .. In both cases, the bucket is accessed using an external IP address'. Charged per GB on Hotbox and Icebox; only incoming traffic and API calls are free. | metered: yes
- identity: email
- interface: s3-compatible, rclone
- limits:
  - retention-clamped (binding): expires in 60 days [1]
- limits note: bonus expires in 60 days and unused balance is revoked; bonus cannot be spent on CDN, licences or marketplace
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: s3
- tooling: S3-compatible API, rclone via S3 backend; the only free axis is the 5 000 RUB (individual) / 12 000 RUB (legal entity) welcome bonus, 60 days
- composes with: welcome bonus only: 5 000 RUB per individual, one-time, 60-day expiry, requires a corporate-domain email and an RF IP; = N identities x ~60 days of storage, not perpetual
- reliability: Promotional credit model expires after 60 days unless upgraded to paid tiers. Outbound egress is billed at metered per-gigabyte rates.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no perpetual free volume — pay-as-you-go per GB, per storage class (Hotbox/Icebox/Backup)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Outgoing traffic is any downloading of information from the bucket ... you pay for: Volume of stored data (per GB). Outgoing traffic (per GB)'
  - [2] 2026-10-21: '5000 бонусных рублей для физических лиц и 12 000 — для юридических лиц', 'Бонус выдается на срок 60 дней'
  - [3] 2026-10-21: 
- sources:
  - [1] https://cloud.vk.ru/docs/en/storage/s3/tariffication
  - [2] https://cloud.vk.ru/bonus/
  - [3] https://hb.ru-msk.vkcloud-storage.ru/
