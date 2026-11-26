# IDCloudHost

> biznetgio.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/biznetgio/ | JSON https://fshy.ajam.dev/api/v1/entity/biznetgio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IDCloudHost

- `compute/idcloudhost` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T11:17:28.101Z (live) | stale on 2026-12-26
- url https://www.biznetgio.com/product/vps-murah-indonesia/
- free tier: IDCloudHost's promo: 'Mulai dari Rp 55.000,- Dapatkan Bonus Saldo Rp 100.000,- untuk Top Up Pertamamu!' and 'Cukup Top Up saldo pertamamu minimal Rp 55.000,- dan dapatkan total saldo Rp 155.000,- di billing mu.' 'Saldo gratis diberikan setelah Top Up minimal Rp 55.000' — the balance requires a payment first. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: NEO Lite KVM VPS starts at IDR 50,000 a month with 60 GB SSD and free bandwidth, which is a paid product | metered: no | source: [2]
- identity: institution
- interface: unknown
- limits note: Both are paid: the Indonesian free credit is a top-up bonus that requires paying first, and the cheapest instance is IDR 50,000 a month rather than zero.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A cheap regional IPv4 with local peering, not free capacity. It is useful only where latency inside Indonesia matters.
- reliability: no reliability event recorded
- notes: A promo code (clouduntukbangsa) granting IDR 50,000 of credit was reported by a third party and was not confirmed on the vendor page. The registration identity step was not verified.
- extras:
  - facets.class: refutation-no-free-vm
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
- evidence:
  - [3] 2026-10-22: promo requires a first top-up of at least IDR 55,000 to receive IDR 100,000 of bonus balance, valid to 2026-10-31, quoted
  - [2] 2026-10-22: NEO Lite KVM VPS starts at IDR 50,000 a month with 60 GB SSD and free bandwidth, which is a paid product
  - [4] 2026-10-22: third-party price check dated 2026-10-17: Biznet Gio NEO Lite from IDR 59,000 for 1 vCPU / 1 GB / 60 GB, IDCloudHost from IDR 87,000 a month for 2 vCPU / 2 GB / 20 GB
  - [3] 2026-11-25: the promo grants a total balance of Rp 155,000 only after a first top-up of at least Rp 55,000 | capture: sha256:6ca556efe007ad8dd6fb97ee9aba8649d6a22d1402fb5506697aefbb7ed479fd | quote: Cukup Top Up saldo pertamamu minimal Rp 55.000,- dan dapatkan total saldo Rp 155.000,- di billing mu.
  - [3] 2026-11-25: the promo offers an Rp 100,000 bonus on a first top-up starting from Rp 55,000 | capture: sha256:6ca556efe007ad8dd6fb97ee9aba8649d6a22d1402fb5506697aefbb7ed479fd | quote: Mulai dari Rp 55.000,- Dapatkan Bonus Saldo Rp 100.000,- untuk Top Up Pertamamu!
  - [3] 2026-11-25: the bonus balance is released only after a top-up of at least Rp 55,000 | capture: sha256:6ca556efe007ad8dd6fb97ee9aba8649d6a22d1402fb5506697aefbb7ed479fd | quote: Saldo gratis diberikan setelah Top Up minimal Rp 55.000
- sources:
  - [1] https://www.biznetgio.com/product/vps-murah-indonesia/
  - [2] https://www.biznetgio.com/promo/diskon-vps-termurah/
  - [3] https://idcloudhost.com/promo/cloud-vps/
  - [4] https://www.matthewswong.com/id/blog/biznet-gio-vs-idcloudhost-indonesia-cloud/
