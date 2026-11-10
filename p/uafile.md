# UAFile

> uafile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uafile/ | JSON https://fshy.ajam.dev/api/v1/entity/uafile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UAFile

- `debrid/uafile` | fails-quota | evidence documented | binding per-ip-shaping | category file host (anonymous, per-IP spacing) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://www.uafile.com/
- free tier: Free upload, 100 MB per file, files deleted after 30 days if nobody downloads them; one new upload per 3 minutes and one new download per 5 minutes per IP. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 100 МБ (100 MB) per file | source: [1]
- retention: 30 days without a download; files up to 500 KB can stay longer | days: 30 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page shows no login step.
- interface: rest
- limits:
  - per-object-cap: 100 MB per file [1]
  - per-ip-shaping (binding): one new upload per 3 minutes and one new download per 5 minutes per IP [1]
  - retention-clamped: deleted after 30 days if nobody downloads [1]
- binding note: One download per 5 minutes per IP binds a batch retrieval before the 100 MB cap matters.
- interface detail: Web upload; no API was read.
- tooling: Browser upload.
- composes with: Per-IP spacing of 3 minutes between uploads and 5 minutes between downloads limits scripted retrieval.
- reliability: Files are also removed when disk space runs out.
- evidence note: Rules read on the vendor home page (Ukrainian text).
- evidence:
  - [1] 2026-11-03: per-file cap is 100 MB | capture: sha256:3296773e0ed5f73cdea5b49521baf1c41a4643d27e9768fab6e81fedf119f0ec | quote: - Максимум 100 МБ на один файл
  - [1] 2026-11-03: a file is deleted after 30 days without downloads | capture: sha256:3296773e0ed5f73cdea5b49521baf1c41a4643d27e9768fab6e81fedf119f0ec | quote: - Файл видаляється через 30 днів, якщо ніхто не завантажує
  - [1] 2026-11-03: one upload per 3 minutes per IP | capture: sha256:3296773e0ed5f73cdea5b49521baf1c41a4643d27e9768fab6e81fedf119f0ec | quote: - Нове завантаження раз на 3 хвилини для одного IP
  - [1] 2026-11-03: one download per 5 minutes per IP | capture: sha256:3296773e0ed5f73cdea5b49521baf1c41a4643d27e9768fab6e81fedf119f0ec | quote: - Нове скачування раз на 5 хвилин для одного IP
- sources:
  - [1] https://www.uafile.com/
