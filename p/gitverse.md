# GitVerse

> gitverse.ru | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitverse/ | JSON https://fshy.ajam.dev/api/v1/entity/gitverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gitverse (gitverse.ru)

- `storage/gitverse-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitverse.ru/docs/limits-lfs-cicd/limits-lfs
- free tier: none reachable: 2 GB/month LFS storage per user AND per organization, 100 MB per file over HTTP, 1 GB per file over SSH. Too small, hard-capped, monthly. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 2 GB/month LFS storage per user AND per organization, 100 MB per file over HTTP, 1 GB per file over SSH. Too small, hard-capped, monthly.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 2 GB/month LFS storage per user AND per organization, 100 MB per file over HTTP, 1 GB per file over SSH. Too small, hard-capped, monthly.
- sources:
  - [1] https://gitverse.ru/docs/limits-lfs-cicd/limits-lfs

## GitVerse (Sber git hosting: LFS + releases + packages)

- `storage/gitverse` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitverse.ru
- free tier: 2 GB Git LFS per user AND per org (monthly), 4 GB release assets per user/org, 500 MB packages per user/org | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free clone/download from the platform, no egress billing published | metered: no
- identity: email
- interface: ssh, git
- limits:
  - per-object-cap (binding): 100 MB per file [1]
- limits note: 2 GB LFS/mo; 4 GB releases; 500 MB packages; 100 MB per file via HTTP, 1 GB via SSH; max 5 files and 500 MB per release upload batch
- interface detail: git
- tooling: standard git + git-lfs over HTTPS/SSH; registries for npm, PyPI, Maven, Go, NuGet, Docker, Generic, Helm, deb, rpm
- composes with: Caps are per user/org TOTAL, not per repo. Unlimited repos x 4 GB does NOT multiply. Only new orgs/users do: 4 GB per org. 20 TiB would need 5 000 orgs.
- reliability: Hard global caps per identity with no top-up path; exceeding them blocks new uploads entirely rather than throttling. Quota stays with the original owner after repo transfer.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 GB Git LFS per user AND per org (monthly), 4 GB release assets per user/org, 500 MB packages per user/org
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'каждому пользователю и каждой организации предоставляется ежемесячный лимит хранения объемом 2 ГБ'
  - [1] 2026-10-21: 'Суммарный лимит для релизов на пользователя или организацию составляет 4 ГБ', 'Максимальный размер одного файла — 100 Мбайт'
  - [3] 2026-10-21: 'Суммарный лимит для пакетов на пользователя или организацию составляет 500 Мбайт'
- sources:
  - [1] https://gitverse.ru/docs/limits-lfs-cicd/limits-releases
  - [2] https://gitverse.ru/docs/limits-lfs-cicd/limits-lfs
  - [3] https://gitverse.ru/docs/limits-lfs-cicd/limits-packages

## sberdisk / gitverse (sber)

- `storage/sberdisk-gitverse` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitverse.ru/
- free tier: none reachable: Both authenticate through Sber ID, which is phone+SMS ('Введите свой номер телефона... или отсканируйте QR-код в приложении Сбербанк Онлайн'), and GitVerse's own sign-in endpoint answers… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Both authenticate through Sber ID, which is phone+SMS ('Введите свой номер телефона... или отсканируйте QR-код в приложении Сбербанк Онлайн'), and GitVerse's own sign-in endpoint answers…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both authenticate through Sber ID, which is phone+SMS ('Введите свой номер телефона... или отсканируйте QR-код в приложении Сбербанк Онлайн'), and GitVerse's own sign-in endpoint answers…
  - [2] 2026-10-21: cited as the basis of the rejection: Both authenticate through Sber ID, which is phone+SMS ('Введите свой номер телефона... или отсканируйте QR-код в приложении Сбербанк Онлайн'), and GitVerse's own sign-in endpoint answers 401
- sources:
  - [1] https://gitverse.ru/
  - [2] https://disk.sber.ru/
