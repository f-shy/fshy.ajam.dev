# AllFiles.org

> allfiles.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/allfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/allfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AllFiles.org

- `storage/allfiles-org` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://allfiles.org
- free tier: 'Upload, store, and send files up to 200 GB for free'. 100 GB per file, 200 GB per transfer, 30-day retention, no registration. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB per file | bytes: 100000000000 | source: [1] | note: not stated
- retention: 'Upload, store, and send files up to 200 GB for free'. 100 GB per file, 200 GB per transfer, 30-day retention, no registration. | days: 30 | source: [1] | note: not stated
- egress: Claims 'up to 1000 Mbit/s for both uploading and downloading', no meter mentioned. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-ip-shaping: 1000 Mbit/s [1]
  - per-object-cap (binding): 100 GB per file [1]
- limits note: per-object-cap 100 GB; 200 GB aggregate per transfer; retention 'до 30 дней' then automatic deletion.
- interface detail: rest
- tooling: Web form. No API documented.
- composes with: 100 GB x unlimited objects, 30-day expiry. A re-upload loop with an unusually large per-object ceiling for the retention class.
- reliability: Presents as a multi-language generic transfer host (identical copy in RU and EN). Small operator, no track record. The 1000 Mbit/s claim is unverified.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Поддерживается загрузка до 100 GB на один файл и до 200 GB в общей передаче', 'Загруженные файлы сохраняются до 30 дней'
  - [2] 2026-10-21: (EN) — 'Upload, store, and send files up to 200 GB for free. No-registration file hosting service'
- sources:
  - [1] https://allfiles.org/ru
  - [2] https://allfiles.org/
