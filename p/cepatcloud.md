# CepatCloud.id

> cepatcloud.id | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cepatcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/cepatcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CepatCloud.id

- `compute/cepatcloud-id` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T05:43:09.217Z (live) | stale on 2026-12-05
- url https://cepatcloud.id/vps-gratis-selamanya/
- free tier: A perpetual free VPS: 15 GB SSD, 1 core, 2 GB RAM, 100 Mbit/s unlimited bandwidth, 1 IPv6 and 1 private IPv4, Ubuntu or Debian only, one per person, for Indonesian users only. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the 2026-04-17 Wayback capture of the offer page states 'Rp 0 selamanya', '15GB SSD Storage', '1 Core CPU 2GB Ram', '100Mb/s Unlimited Bandwidth', '1 IPv6 & 1 IPv4 Private', 'Ubuntu / Debian OS Only', and that the service is for Indonesian citizens, quoted | metered: yes | free allowance: unlimited bandwidth at 100 Mbit/s | price per TB: not published: the offer page states unlimited bandwidth and no overage price | source: [2]
- identity: any-phone | detail: email address plus a WhatsApp number: activation requires "Verifikasi alamat email dan Verifikasi nomor Whatsapp", and the front page lists "Email + WhatsApp Verification" as a requirement, so a number that receives WhatsApp is required as well as an email address; one free VPS per user. The offer is for Indonesian citizens, though the record does not state that the WhatsApp number must be Indonesian. No card is stated, no hold exists because no payment is taken, and debit or prepaid do not arise
- interface: unknown
- limits:
  - write-gated (binding): Activation requires email plus WhatsApp number verification in a format the operator sends by email, is granted at the operator's discretion, and users report no activation at all, so the constraint is a manual approval that may never come. [1]
- limits note: Activation requires email plus WhatsApp number verification in a format the operator sends by email, is granted at the operator's discretion, and users report no activation at all, so the constraint is a manual approval that may never come.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 2 GB RAM and 15 GB disk with unlimited bandwidth at zero cost is the largest free shape found in Indonesia, and it composes with anything that needs a small always-on Linux box; the practical break is that 2025 user reports show activation never completing.
- reliability: https://cepatcloud.id/ did not resolve on the probe date 2026-11-04 (DNS lookup failed, no HTTP response)
- notes: The live site answered 530 at automated retrieval, DNS failed at the probe, and the crawl returned no pages, so the specification here rests on the archived capture plus the terms page, which automated retrieval did read live. That makes the shape documented-from-archive and the operational status unverified. Two users reporting silence in 2025 is the strongest signal that this is a queued or dormant programme rather than a working one. Classified as qualifies-with-caveat rather than dead because the terms page still served and the vendor still publishes a paid line. The one recorded is the better-evidenced.
- extras:
  - facets.class: regional-vps
  - facets.free_tier_kind: perpetual
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
- evidence:
  - [3] 2026-10-22: 'Proses aktifasi memerlukan syarat tambahan yaitu Verifikasi alamat email dan Verifikasi nomor Whatsapp'; 'masing-masing user hanya bisa mendapatkan 1 layanan gratis VPS'; 'VPS yang terdeteksi tidak digunakan akan kami hapus'; 'Kami berhak penuh untuk mengaktifkan atau menonaktifkan layanan', quoted
  - [2] 2026-10-22: the 2026-04-17 Wayback capture of the offer page states 'Rp 0 selamanya', '15GB SSD Storage', '1 Core CPU 2GB Ram', '100Mb/s Unlimited Bandwidth', '1 IPv6 & 1 IPv4 Private', 'Ubuntu / Debian OS Only', and that the service is for Indonesian citizens, quoted
  - [4] 2026-10-22: two independent users in August 2025 report registering and receiving no activation email or response at all, and conclude the free service is 'slow respond atau udah nggak aktif'; a third replies that free services cannot be expected to deliver, reported
  - [5] 2026-10-22: vendor wording, translated: 'we cannot promise that a free service request can be activated as quickly as possible', with 15 GB SSD, 1 core, 2 GB RAM and 'Email + WhatsApp Verification' listed as the terms
  - [2] 2026-11-03: the offer page states unlimited bandwidth at 100 Mbit/s and no overage price | capture: sha256:c2207c0789a4dfa6776b01280b0673ae4bf676a384c4b226ebacfdf00319d675 | quote: - 100Mb/s Unlimited Bandwidth
  - probe:cepatcloud.id 2026-11-04: the live host failed DNS resolution on 2026-11-04 | capture: sha256:5d981816f9aa2c2c68a37e5ae961a0fe60b747a4dcf0094d81917830eeaa72c9 | quote: "error": "dns"
- sources:
  - [1] https://cepatcloud.id/vps-gratis-selamanya/
  - [2] https://web.archive.org/web/20260417002958/https://cepatcloud.id/vps-gratis-selamanya/?provider=wayback
  - [3] https://cepatcloud.id/terms-of-services/
  - [4] https://www.diskusiwebhosting.com/threads/vps-gratis-cepatcloudid-masih-jalan.39308/
  - [5] https://cepatcloud.id/
