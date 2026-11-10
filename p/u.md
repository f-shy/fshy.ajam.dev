# U.UA

> u.ua | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/u/ | JSON https://fshy.ajam.dev/api/v1/entity/u.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## U.UA (u.ua)

- `storage/u-ua` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://u.ua
- free tier: 50 GB per file, unlimited file count, no registration, 7 days storage. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB per file | bytes: 50000000000 | source: [1] | note: not stated
- retention: per-object-cap 50 GB; retention 7 days then automatic deletion | days: 7 | source: [1] | note: not stated
- egress: No meter stated; 'мы не ограничиваем количество загружаемых файлов'. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 50 GB per file [1]
  - retention-clamped: retention 7 days [1]
- limits note: per-object-cap 50 GB; retention 7 days then automatic deletion. That 7-day window is the binding constraint, not the 50 GB.
- interface detail: rest
- tooling: Web form, folder upload supported. No API.
- composes with: 50 GB x unlimited drops, 7 days. A high-throughput transfer pipe, not storage.
- reliability: Ukrainian file-exchange site, appears healthy. Useful as an egress-firehose (large objects, fast) rather than as a store.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'вы можете легко и безопасно загружать и отправлять файлы объемом до 50 GB', 'Хранение до 7 дней', 'Удобство без регистрации'
- sources:
  - [1] https://u.ua/ru/
