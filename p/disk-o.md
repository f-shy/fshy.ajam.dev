# disk-o

> disk-o.cloud | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/disk-o/ | JSON https://fshy.ajam.dev/api/v1/entity/disk-o.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## disk-o (mail) as a storage source

- `storage/disk-o-as-a-storage-source` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.058Z (live) | stale on 2026-12-04
- url https://disk-o.cloud/en/
- free tier: None reachable: It is a multi-cloud client/aggregator for Yandex Disk, Google Drive, Dropbox, Mail.ru etc. It owns no storage and adds no quota, so it can only ever surface the 5-8 GB free tiers it aggreg. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: It is a multi-cloud client/aggregator for Yandex Disk, Google Drive, Dropbox, Mail.ru etc. — it owns no storage and adds no quota, so it can only ever surface the 5-8 GB free tiers it…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is a multi-cloud client/aggregator for Yandex Disk, Google Drive, Dropbox, Mail.ru etc. — it owns no storage and adds no quota, so it can only ever surface the 5-8 GB free tiers it…
  - [2] 2026-10-21: cited as the basis of the rejection: It is a multi-cloud client/aggregator for Yandex Disk, Google Drive, Dropbox, Mail.ru etc. — it owns no storage and adds no quota, so it can only ever surface the 5-8 GB free tiers it aggreg
  - [1] 2026-11-19: Disk-O is a manager that connects to other cloud storage platforms | capture: sha256:5d7a4d8efcf61ea0e3ad999e3280d8fbcb0477baa471e1690a1cc12edd16d2cf | quote: Disk-O: allows you to connect all of the most popular cloud storage platforms and work with them in a single interface.
  - [1] 2026-11-19: Disk-O owns no storage; uploads are limited by the connected cloud's volume | capture: sha256:5d7a4d8efcf61ea0e3ad999e3280d8fbcb0477baa471e1690a1cc12edd16d2cf | quote: Using Disk-O: you can upload as many files as the volume of the clouds allows, without taking up space on your computer's memory.
- sources:
  - [1] https://disk-o.cloud/en/
  - [2] https://help.mail.ru/disko/faq/what/

## disk-o (disk-o.cloud)

- `storage/disk-o` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://disk-o.cloud/
- free tier: None reachable: Not a storage provider. A desktop aggregator client that mounts other clouds (its own copy: 'Переносите файлы из любых подключенных хранилищ в Облако Mail.ru'). It contributes zero bytes. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not a storage provider — a desktop aggregator client that mounts other clouds (its own copy: 'Переносите файлы из любых подключенных хранилищ в Облако Mail.ru'). It contributes zero bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a storage provider — a desktop aggregator client that mounts other clouds (its own copy: 'Переносите файлы из любых подключенных хранилищ в Облако Mail.ru'). It contributes zero bytes.
- sources:
  - [1] https://disk-o.cloud/
