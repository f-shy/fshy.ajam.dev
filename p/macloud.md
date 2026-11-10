# Macloud

> macloud.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macloud/ | JSON https://fshy.ajam.dev/api/v1/entity/macloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Macloud

- `compute/macloud` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://macloud.ru/vps-vds
- free tier: RUB 263 per day for the calculator's base configuration: 8 vCPU AMD EPYC up to 3.4 GHz, 16 GB RAM, 100 GB NVMe, 64 TB traffic, plus RUB 7 for one IPv4. Billing switches between day and month; the page defaulted to day and the month figure was not read. Component rates on the same configurator are RUB 10 per core, RUB 8 per GB of RAM and RUB 0.55 per GB of disk per day. The vps.today index row is a much smaller machine at RUB 150: 1 core at 3 GHz, 1 GB RAM, 10 GB NVMe, 1 TB traffic, 1 Gbit/s, Moscow. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 64 TB included on the base tariff, 1 Gbit/s port; the index row at RUB 150 states 1 TB | metered: yes | free allowance: 64 TB on the base tariff | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 64 TB of traffic is included with the base tariff, so the measured wall on the vendor page is the byte allowance and then the 1 Gbit/s port; the index row at RUB 150 carries 1 TB instead, so the allowance moves with the configuration rather than sitting at one number. [1]
- limits note: 64 TB of traffic is included with the base tariff, so the measured wall on the vendor page is the byte allowance and then the 1 Gbit/s port; the index row at RUB 150 carries 1 TB instead, so the allowance moves with the configuration rather than sitting at one number.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: own control panel, ISO mount, snapshots not stated; no public API documented on the page read
- composes with: The only plan on this page that reaches 8 cores and 16 GB is also the only one that states 64 TB, and it is billed per day, so it suits a short burst of indexing rather than an always-on archive node
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor configurator. The record is reported because the only figure the vendor prints for a small machine is a component rate, not a plan price; the RUB 150 row comes from the index. verification criteria: the month toggle's price for the smallest valid configuration, and whether the 64 TB is per day or per month. Rendering and provenance: currency written as RUB, the vendor's own ruble sign kept in the quote.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 16
  - facets.shape.disk_gib: 100
- evidence:
  - [1] 2026-10-23: configurator base tariff, quoted: 'Базовый тариф 256 ₽', 'vCPU 8 core, RAM 16 ГБ, NVMe 100 ГБ, Трафик 64 TБ', 'IPv4 1 шт 7 ₽', 'Итого: 263 ₽ / в день'; unit rates '10 ₽ за 1 core', '8 ₽ за 1 Gb', '0.55 ₽ за 1 Gb'; 'Скорость 1000 Мбит/сек. Локальная сеть 10 Гбит'; 'Серверы в московском дата-центре уровня TIER IV DataPro'
  - [2] 2026-10-23: index row quoted: 'Macloud | 10 GB NVMe | 1 GB | 1 x 3 GHz | 1 TB 1 000 Mbit/s | Россия (Москва) KVM IPv6 DDoS ПО ! | 150 руб.'
- sources:
  - [1] https://macloud.ru/vps-vds
  - [2] https://vps.today/
