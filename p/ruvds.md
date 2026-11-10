# RUVDS "Большой

> ruvds.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ruvds/ | JSON https://fshy.ajam.dev/api/v1/entity/ruvds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RUVDS "Большой диск" / СХД — Russian flat-rate disk VPS with unlimited traffic

- `storage/ruvds-russian-flat-rate-disk-vps-with-unlimited-traffic` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ruvds.com/ru/huge-disk/
- price $11.50/TB/mo at 2 TB ($23.00/mo) and 4 TB ($46.00/mo); $12.39/TB/mo at 1 TB ($12.39/mo). At 20 TB: ~$11.50/TB/mo if two 10 TB-class configs are assembled ($230/mo), derived not quoted. Unlimited traffic, $0 egress. | parsed USD 11.5/TB-mo
- free tier: СХД Старт 1,023 ₽/mo for 1,024 GB; СХД Стандарт 1,899 ₽/mo for 2,048 GB; СХД Премиум 3,798 ₽/mo for 4,096 GB. Line advertised «от 1 до 18 Терабайт». Landing headline: «всего 500₽ за 1 Тб/мес». | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unlimited. Every СХД configuration lists its channel (up to 100 Mbit/s on the entry tiers) with no traffic meter, and the service is sold as a VPS so the rail is the VPS's own port. No per-GB charge exists. | metered: no
- identity: card | detail: card
- interface: s3, sftp, rsync, smb, nfs, ssh, rclone
- limits:
  - per-ip-shaping (binding): 100 Mbit/s [1]
  - per-ip-shaping (binding): 1 TB/day [1]
- limits note: The 500 RUB per 1 TB monthly headline is not the direct price of storage plans. The lowest standalone 1 TB plan costs 1,023 RUB. The 500 RUB rate refers to a base VPS plus an add-on disk in the configurator. Network port is 100 Mbit/s on the entry tier, providing approximately 1 TB per day theoretical bandwidth (~32 TB per month).
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: ssh + sftp
- tooling: Full KVM virtual private server supporting SSH, SFTP, rsync, rclone, NFS, Samba, and self-hosted services like MinIO or Nextcloud. Users manage the complete software stack.
- composes with: Config-doubling ladder up to 18 TB; 20 TB requires two units or a different product. Each 1 TB step costs the same per TB from 2 TB upward.
- reliability: Long-established Russian host (ruvds.com), KVM, own DCs. No independent benchmark of the СХД disk subsystem was found.
- notes: the same as the free tier
- extras:
  - price_verbatim: $11.50/TB/mo at 2 TB ($23.00/mo) and 4 TB ($46.00/mo); $12.39/TB/mo at 1 TB ($12.39/mo). At 20 TB: ~$11.50/TB/mo if two 10 TB-class configs are assembled ($230/mo), derived not quoted. Unlimited traffic, $0 egress.
- evidence:
  - [1] 2026-10-21: «Классический VPS с облачным хранилищем всего 500₽ за 1 Тб/мес»; «СХД Старт 1 023 ₽ в месяц» with «hugeDriveCapacity=1024»; «СХД Стандарт 1 899 ₽» (2048); «СХД Премиум 3 798 ₽» (4096)
  - withheld 2026-10-21: same page — «полноценное хранилище (СХД) размером от 1 до 18 Терабайт со всем привычным функционалом VPS-сервера»
  - [2] 2026-10-21: used only as the FX/units sanity check; RUVDS figures converted at 0.012111 USD/RUB
- sources:
  - [1] https://ruvds.com/ru/huge-disk/
  - [2] https://www.ovhcloud.com/pl/public-cloud/prices/

## RUVDS

- `compute/ruvds` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T02:23:57.259Z (live) | stale on 2026-12-05
- url https://ruvds.com/vps_test/
- free tier: A 3-day free trial of any configuration costing under RUB 3,000 a month, including a hand-built configuration, with one IP address and any data-centre location in the configurator. A new user needs only a phone number and an email address to register and the trial is switched on with a toggle at order time. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: The trial is three days and one IP address on a server priced under RUB 3,000 a month, so it is long enough to measure latency and short enough to build nothing on. | source: [1]
- egress: unlimited traffic, no overage price: the page states a channel of up to 300 Mbit/s with unlimited traffic (Russian: безлимитным трафиком) | metered: no | source: [1]
- identity: any-phone | detail: a phone number and an email address, and nothing more: the trial page states registration needs only a phone number and email, and the trial is switched on with a toggle at order time. No card is required for the trial, so no hold exists. Whether the phone must be Russian is not stated in the evidence; the record's notes call it an any-phone gate, which is why the kind is not country-phone. For paid plans a third party reports foreign cards are accepted through a 'Card PaymentNut' option settling in USD, covering Visa, MasterCard, AMEX, JCB, UnionPay, Discover and Diners, reported
- interface: unknown
- limits:
  - retention-clamped (binding): The trial is three days and one IP address on a server priced under RUB 3,000 a month, so it is long enough to measure latency and short enough to build nothing on. [1]
- limits note: The trial is three days and one IP address on a server priced under RUB 3,000 a month, so it is long enough to measure latency and short enough to build nothing on.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Three days on a 2-vCPU / 2-GiB Russian box is enough to measure round-trip time from a target market and to confirm whether an outbound route exists, and it is not enough to run a crawl.
- reliability: no reliability event recorded
- notes: The identity cost is the notable part: this is an any-phone gate, not a passport gate, which makes it one of the few Russian providers an individual outside Russia can reach at all. The trial needs no card, which is unusual. It is still a 3-day window, so it is a measurement tool rather than capacity.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: ' 3000 3 ' (build any tariff up to RUB 3,000 and test free for 3 days), ' - ' (register with only a phone number and email), ' ? 3 ' and ' IP- ', quoted
  - [2] 2026-10-22: ' 3 ' and that Windows-licensed tariffs are included in the trial, quoted
  - [3] 2026-10-22: a third party states that foreign cards are accepted through a 'Card PaymentNut' option settling in USD via a Canadian processor, covering Visa, MasterCard, AMEX, JCB, UnionPay, Discover and Diners, reported
  - [1] 2026-11-03: unlimited traffic on a channel of up to 300 Mbit/s | capture: sha256:933673bf51a680159b523d2ca1997d117c8444dbfdce84772b9bf944c9be611e | quote: Это позволяет обеспечить VPS интернет-каналом со скоростью до 300 Мбит/с с лучшим доступом и безлимитным трафиком.
  - [1] 2026-11-03: the page advertises unlimited traffic | capture: sha256:933673bf51a680159b523d2ca1997d117c8444dbfdce84772b9bf944c9be611e | quote: Неограниченый трафик Неограниченый трафик
- sources:
  - [1] https://ruvds.com/vps_test/
  - [2] https://ruvds.com/ru/windows/
  - [3] https://russiable.com/russian-vps-hosting/
