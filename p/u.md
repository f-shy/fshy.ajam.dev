# U.UA

> u.ua | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/u/ | JSON https://fshy.ajam.dev/api/v1/entity/u.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## U.UA (u.ua)

- `storage/u-ua` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:34.761Z (live) | stale on 2026-11-25
- url https://u.ua
- free tier: С помощью нашего сервиса вы можете легко и безопасно загружать и отправлять файлы объемом до 50 GB. | unit: GB | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: файлы объемом до 50 GB | bytes: 50000000000 | source: [1] | note: not stated
- retention: Все загруженные файлы хранятся на наших серверах в течение 7 дней, после чего они автоматически удаляются. | days: 7 | source: [1] | note: not stated
- egress: Мы не ограничиваем количество загружаемых файлов, вы можете пользоваться сервисом совершенно бесплатно. | metered: no
- identity: anonymous | detail: для использования U.UA не требуется создавать учетную запись
- interface: rest
- limits:
  - per-object-cap (binding): файлы объемом до 50 GB [1]
  - retention-clamped: в течение 7 дней [1]
- limits note: per-object-cap 50 GB; retention 7 days then automatic deletion. That 7-day window is the binding constraint, not the 50 GB.
- interface detail: rest
- tooling: Web form, folder upload supported. No API.
- composes with: 50 GB x unlimited drops, 7 days. A high-throughput transfer pipe, not storage.
- reliability: Ukrainian file-exchange site, appears healthy. Useful as an egress-firehose (large objects, fast) rather than as a store.
- notes: 50 GB per file, unlimited file count, no registration, 7 days storage.
- evidence note: the u.ua page states files up to 50 GB can be uploaded and sent
- evidence:
  - [1] 2026-10-21: 'вы можете легко и безопасно загружать и отправлять файлы объемом до 50 GB', 'Хранение до 7 дней', 'Удобство без регистрации'
  - [1] 2026-11-09: the page states files up to 50 GB can be uploaded | capture: sha256:3abd3c05f5e4ac680f229aa4e9fcdadf4ea865af878a338022b006b539178862 | quote: С помощью нашего сервиса вы можете легко и безопасно загружать и отправлять файлы объемом до 50 GB.
  - [1] 2026-11-09: the page states files are stored 7 days then deleted | capture: sha256:3abd3c05f5e4ac680f229aa4e9fcdadf4ea865af878a338022b006b539178862 | quote: Все загруженные файлы хранятся на наших серверах в течение 7 дней, после чего они автоматически удаляются.
  - [1] 2026-11-09: the page states no account is needed | capture: sha256:3abd3c05f5e4ac680f229aa4e9fcdadf4ea865af878a338022b006b539178862 | quote: для использования U.UA не требуется создавать учетную запись
  - [1] 2026-11-09: the page states the number of uploaded files is not limited | capture: sha256:3abd3c05f5e4ac680f229aa4e9fcdadf4ea865af878a338022b006b539178862 | quote: Мы не ограничиваем количество загружаемых файлов, вы можете пользоваться сервисом совершенно бесплатно.
- sources:
  - [1] https://u.ua/ru/
