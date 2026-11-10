# CloudVPS

> cloudvps.by | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudvps/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudVPS

- `compute/cloudvps` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:13.246Z (live) | stale on 2026-12-05
- url https://cloudvps.by/servers/cloud/cloud_vps.php
- free tier: A 7-day free VPS test: fill in a form with the chosen configuration, the application is checked, credentials arrive by email, and the server runs free for seven days. The paid catalogue starts at BYN 19.99 a month for the cloud Micro shape of one core at 3.6 GHz, 1 GB RAM and 15 GB NVMe on a 200 Mbit/s port, shown at BYN 14.99 a month with a 25 percent discount applied on the page, with 5 TB of traffic included per calendar month and expansion to 37 TB. Payment is accepted by international and Russian cards in any currency, and the provider states it. A separate VPS line in Belarus starts at BYN 29.99 a month for 1 core, 2 GB RAM and 30 GB disk. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Traffic is metered with an included allowance of 5 TB per calendar month on the cloud tariffs, expandable to 37 TB; the price of the expansion is not on the page. | metered: yes | free allowance: 5 TB per calendar month, expandable to 37 TB | source: [1]
- identity: card | detail: the free seven-day test needs an application form and nothing else that is stated: the trial page says choose a configuration and fill in a simple form, with credentials arriving by email once the application is checked, and it names no card, phone or identity document. The card statement belongs to the paid catalogue, where payment "is accepted by international and Russian cards in any currency"; no hold or authorisation is stated, whether debit or prepaid cards are accepted is not stated, and whether the trial repeats once per person is not established
- interface: unknown
- limits:
  - volume-quota (binding): Five terabytes a month is the ceiling on the cheapest shape and it is generous for the price, so what fails first is not the link but the monthly allowance: 5 TB is about 167 GB a day, and the daily test volume is 500 GB to 1 TB, so the smallest shape carries roughly a fifth of the daily load before the port at 200 Mbit/s becomes the limit. [1]
- limits note: Five terabytes a month is the ceiling on the cheapest shape and it is generous for the price, so what fails first is not the link but the monthly allowance: 5 TB is about 167 GB a day, and the daily test volume is 500 GB to 1 TB, so the smallest shape carries roughly a fifth of the daily load before the port at 200 Mbit/s becomes the limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the one shape in evaluated offerings that composes with a foreign payment instrument and a real traffic allowance at the same time: 5 TB a month at 200 Mbit/s for BYN 14.99 is enough to move a working dataset, and the 7-day test costs a form rather than a card authorisation, so the transfer can be measured before anything is bought.
- reliability: no reliability event recorded
- notes: CloudVPS provides regional VPS hosting in Belarus.
- extras:
  - facets.class: regional-low-floor
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 15
  - facets.shape.port_mbit: 200
- evidence:
  - [2] 2026-10-22: 7-day free test VPS: choose a configuration, press try for free, fill in a simple form, credentials arrive by email after the application is checked, quoted and translated
  - [1] 2026-10-22: cloud Micro at BYN 19.99 a month, BYN 14.99 with 25 percent applied, for 1 core at 3.6 GHz, 1 GB RAM, 15 GB NVMe, 200 Mbit/s and 5 TB of included traffic expandable to 37 TB; the page states payment is accepted by international and Russian cards in any currency, quoted and translated
  - [3] 2026-10-22: the Belarus VPS line starts at BYN 29.99 a month for 1 core, 2 GB RAM and 30 GB disk, with a Standart shape at BYN 54.99 for 2 cores, 4 GB and 60 GB
  - [1] 2026-11-03: the cloud tariffs include 5 TB per calendar month, expandable to 37 TB | capture: sha256:a01bea8dbcd981296894bbc4fc2b3b2faaa3f0ae2a9941455b1777805ef2f26b | quote: Включенный трафик на календарный месяц 5 ТБ c возможностью расширения до 37 ТБ
- sources:
  - [1] https://cloudvps.by/servers/cloud/cloud_vps.php
  - [2] https://cloudvps.by/servers/vps/test_vps_hosting.php
  - [3] https://client.cloudvps.by/store/vps-v-belarusi
