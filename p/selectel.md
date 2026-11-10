# Selectel Object

> selectel.ru | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/selectel/ | JSON https://fshy.ajam.dev/api/v1/entity/selectel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Selectel

- `compute/selectel` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://selectel.ru/services/cloud/servers/
- free tier: No free test. The provider's own FAQ states outright that there is no free testing for cloud servers and that the minimum way to evaluate one is to top up RUB 100 and run it hourly; a separate grant of up to RUB 30,000 exists but only for legal entities and sole proprietors. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - volume-quota (binding): There is no free lane for an individual at all: the RUB 30,000 grant is restricted to legal entities and individual entrepreneurs, and everything else starts at a RUB 100 balance. [1]
- limits note: There is no free lane for an individual at all: the RUB 30,000 grant is restricted to legal entities and individual entrepreneurs, and everything else starts at a RUB 100 balance.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 3 TB of pooled free egress across all projects is the durable item here, and it composes with any Russian-hosted workload; the compute itself has no free lane at all.
- reliability: no reliability event recorded
- notes: Selectel is one of the two largest Russian clouds and it publishes the opposite, in plain words, which is more useful than a page that hides it.
- extras:
  - facets.class: regional-paid
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the FAQ on the cloud server page states, in Russian, that Selectel has no free testing, and that to evaluate a server it is enough to top the balance up by the minimum amount of RUB 100; the page then explains that a 2 vCPU and 4 GB server can be judged that way
  - [2] 2026-10-22: the grant page states, in Russian, that registering in the control panel yields a grant of up to RUB 30,000 in bonuses for testing cloud services over one month, and that the offer is available to legal entities and individual entrepreneurs
  - [3] 2026-10-22: the billing documentation states, in Russian, that pay-as-you-go billing deducts hourly for the previous hour of resources plus external traffic consumed above the free allowance of 3 TB across all projects of the account
- sources:
  - [1] https://selectel.ru/services/cloud/servers/
  - [2] https://selectel.ru/services/cloud/grant/
  - [3] https://docs.selectel.ru/cloud-servers/about/payment/

## Selectel Object Storage (Russia) — coldest tier is cheap, the traffic is not

- `storage/selectel-object-storage-coldest-tier-is-cheap-the-traffi` | fails-egress | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://selectel.ru/services/cloud/storage/
- price Ice: $11.04/TB/mo storage PLUS $24.31/TB for every full read-back (₽1.96/GB × 1024) — so one complete retrieval costs 2.2 months of storage. Realistic cold-archive usage (store 1 TB, read 250 GB per month): $11.04 + $6.08 = $17.12/TB/mo. At 50 % monthly read: $23.19/TB/mo. Identical at 5 TB and… | parsed USD 11.04/TB-mo
- free tier: Ice (ледяное) ₽0.89/GB/mo; Cold ₽1.26/GB/mo; Standard ₽2.57/GB/mo. Volume ladder: up to 10 TB ₽1.35, 10-50 TB ₽1.31, 50 TB+ lower (per Selectel's own price-change digest). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: METERED at ₽1.96/GB on every class, plus paid requests. Ice requests are the most expensive in the set at ₽361 per 1 M GET/HEAD and ₽3,009 per 1 M PUT (`serverdelo.ru` table, prices verified 2026-10-03). This is the trap: the cheapest storage line in Russia pairs with the most expensive retrieval. Selectel's OWN promotional tariff does waive it. «не платите за исходящий трафик и запросы весь год». But only at ₽2/GB storage plus a ₽10,000/month platform fee, i.e. you prepay ₽120,000/yr to buy out the egress. | metered: yes
- identity: card | detail: card
- interface: s3-compatible, rclone, cli
- limits note: Ice storage enforces minimum storage durations and retrieval fees. Operations are billed per million requests, with GET operations priced at 361 RUB per million. Outbound egress is billed at 1.96 RUB per gigabyte (~$24.31 per terabyte).
- interface detail: s3 + swift
- tooling: S3-compatible with IAM, S3 endpoint live (`https://s3.ru-7.storage.selcloud.ru/` -> 403 for anonymous list, expected). rclone `s3`, aws-cli, Terraform.
- composes with: Volume ladder is shallow (₽1.35 → ₽1.31 from 10 TB to 50 TB, a 3 % step). No meaningful economy of scale.
- reliability: Tier-1 Russian provider, 152-FZ/PCI DSS/ISO 27001/27017/27018, three copies across racks. No reliability concern; the concern is purely the egress and per-request structure.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Ice (ледяное) ₽0.89/GB/mo; Cold ₽1.26/GB/mo; Standard ₽2.57/GB/mo. Volume ladder: up to 10 TB ₽1.35, 10-50 TB ₽1.31, 50 TB+ lower (per Selectel's own price-change digest).
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: Ice: $11.04/TB/mo storage PLUS $24.31/TB for every full read-back (₽1.96/GB × 1024) — so one complete retrieval costs 2.2 months of storage. Realistic cold-archive usage (store 1 TB, read 250 GB per month): $11.04 + $6.08 = $17.12/TB/mo. At 50 % monthly read: $23.19/TB/mo. Identical at 5 TB and 20 TB because storage is per-GB with only a 3 % volume step (₽1.35 → ₽1.31 above 10 TB). Standard class: $31.87/TB/mo storage + $17.11/TB per read-back. Ice request billing is the harsher trap for small objects: ₽361 per 1 M GET/HEAD = $4.37 per million, so a 20 TiB corpus of 1 MB shards (20 M GETs) incurs $87 in requests alone per full pass. Promo tariff (egress waived, archived capture): ₽2/GB + ₽10,000/mo flat = $36.91/TB/mo at 10 TB, $30.86/TB/mo at 20 TB, i.e. 4.0×/3.3× OVH One-Zone — the…
- evidence:
  - [2] 2026-10-21: «Цены сверены с сайтами провайдеров 3 октября 2026 года»: «Selectel, ледяное | 0,89 ₽ | 1,96 ₽ | 361 ₽ и 3 009 ₽»; «Selectel, холодное | 1,26 ₽ | 1,96 ₽ | 224 ₽ и 2 040 ₽»; «Selectel, стандартное | 2,57 ₽ | 1,38 ₽ | 54 ₽ и 714 ₽»
  - [1] 2026-10-21: three-copy storage across racks, unlimited volume, S3 API, IAM, 152-FZ/PCI DSS/ISO 27001/27017/27018
  - [3] 2026-10-21: > replay of 20250615190112: «До 31 августа подключите стандартное объектное хранилище по специальному тарифу и не платите за исходящий трафик и запросы весь год … 2 ₽ за хранение 1 ГБ данных; 10 000 ₽ за подключение ежемесячно. Исходящий трафик и запросы к API — бесплатные»
  - [4] 2026-10-21: volume ladder «До 10 ТБ 1,63 ₽ → 1,35 ₽; От 10 до 50 ТБ → 1,31 ₽»
  - [5] 2026-10-21: probe: curl -o /dev/null -w '%{http_code}' -> 403
- sources:
  - [1] https://selectel.ru/services/cloud/storage/
  - [2] https://serverdelo.ru/rejtingi/s3-hranilishche/
  - [3] https://web.archive.org/web/202606/selectel.ru/services/cloud/storage/special-tariff/
  - [4] https://selectel.ru/blog/digest08_23/
  - [5] https://s3.ru-7.storage.selcloud.ru/
