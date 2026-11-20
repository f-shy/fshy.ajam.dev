# AdminVPS

> adminvps.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adminvps/ | JSON https://fshy.ajam.dev/api/v1/entity/adminvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AdminVPS

- `compute/adminvps` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:13.245Z (live) | stale on 2026-12-05
- url https://adminvps.ru/vps/test_vps_hosting.php
- free tier: Seven days of any VPS tariff free, obtained by ordering the trial, registering and passing data validation, after which access is sent by email. The provider's knowledge base says the trial gives the full tariff except cron and all mail sending, both disabled. The trial server is deleted 24 hours after the period ends. The same catalogue also carries a first paid month free with the promo code ISP30DAY, and the cheapest paid VPS is one core at 3.6 GHz, 1 GB RAM, 15 GB disk, a 100 Mbit/s port and 1 TB of traffic a month for RUB 250 a month. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Traffic is metered with an included allowance of 1 TB per calendar month on the Lite tariff (the larger Windows tariffs list 10 TB, extendable to 42 TB); the price of traffic past the allowance is not on the page. | metered: yes | free allowance: 1 TB per calendar month (Lite tariff) | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): On the paid floor the 1 TB a month traffic allowance binds first: at the 100 Mbit/s port speed the same machine could move 1 TB in under a day, so the allowance is about 33 GB a day; on the trial the seven days and the disabled cron and SMTP are what fail first. [1]
- limits note: On the paid floor the 1 TB a month traffic allowance binds first: at the 100 Mbit/s port speed the same machine could move 1 TB in under a day, so the allowance is about 33 GB a day; on the trial the seven days and the disabled cron and SMTP are what fail first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The cheapest AdminVPS shape, RUB 250 a month for 1 vCPU and 1 GiB with a 100 Mbit/s port, is the cheapest addressed 24/7 machine evaluated providers found, and it composes with a free storage tier elsewhere: 1 TB a month of egress is enough to serve about 33 GB a day, so the pairing needs a CDN or an object store in front.
- reliability: no reliability event recorded
- notes: Aggregator sources disagree: if the trial is restricted to legal entities, the seven-day period is inaccessible to individual registrants, leaving only the ISP30DAY month.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 15
  - facets.shape.port_mbit: 100
- evidence:
  - [1] 2026-10-22: seven-day trial of any VPS or hosting tariff, ordered by pressing the trial button, registering and passing data validation, with the server deleted one day after the period ends, quoted and translated
  - [2] 2026-10-22: 'during the trial period the full tariff plan is available with all its functions, except cron and sending mail in any form, which is unavailable both from a php script and from a mailbox', quoted and translated
  - [3] 2026-10-22: price sheet: Lite at RUB 250 a month for 1 core at 3.6 GHz, 1 GB RAM, 15 GB disk, 100 Mbit/s port and 1 TB of traffic per calendar month; Promo at RUB 499 for 1 core, 2 GB RAM, 30 GB disk, up to 1 Gbit/s and 3 TB; first month free with promo code ISP30DAY, quoted
  - [4] 2026-10-22: an aggregator table claims AdminVPS gives a trial only to legal entities and only once, which contradicts the provider's own page addressing 'all our clients'; the provider page is preferred and the disagreement is recorded
  - [1] 2026-11-03: the Lite tariff row includes 1 TB of traffic per calendar month | capture: sha256:347f677a653b8b232f6c653ddca71a22daee9e84214ca70f792b10b08d6cea36 | quote: Включенный трафик на календарный месяц 1 ТБ
- sources:
  - [1] https://adminvps.ru/vps/test_vps_hosting.php
  - [2] https://my.adminvps.ru/knowledgebase/93/pravila-i-ogranicheniia-na-khostinge.html
  - [3] https://adminvps.ru/vps/
  - [4] https://hosters.ru/probnyi-vps.html
