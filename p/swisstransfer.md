# SwissTransfer

> swisstransfer.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swisstransfer/ | JSON https://fshy.ajam.dev/api/v1/entity/swisstransfer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SwissTransfer (Infomaniak)

- `storage/swisstransfer` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:23.062Z (live) | stale on 2026-12-10
- url https://www.swisstransfer.com
- free tier: 50 GB | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB | bytes: 50000000000 | source: [1] | note: SwissTransfer accepts files up to 50 GB in size.
- retention: Retention: 15 days by default; 30 only if the SENDER accepts an extension email on day 12 (offer open 3 days) | days: 15 | source: [1] | note: When choosing 30 days, files are automatically deleted after 15 days; the extension is offered to the sender by email on the 12th day and remains available for 3 days.
- egress: If the archive exceeds 10 GB, you will need to download the data files one by one. | metered: no
- identity: institution
- interface: rest, cli
- limits:
  - retention-clamped: Retention: 15 days [1]
  - retention-clamped: deletes at 15 days [1]
  - per-object-cap (binding): per-object-cap: 50 GB [1]
- limits note: Per-object-cap: 50 GB per transfer (combined, not per file). Retention: 15 days by default; 30 only if the SENDER accepts an extension email on day 12 (offer open 3 days). After expiry Infomaniak states a link cannot be reactivated or extended. pull-count: download cap selectable at 1/20/100/250. 'unlimited' requires a paid plan. Request-rate: the container-create endpoint enforces a reCAPTCHA field (see reliability note).
- interface detail: rest
- tooling: Swissfer (github.com/Blutsh/swissfer, 44 stars, pushed 2026-10-21). Rust CLI, upload AND download, email-confirmed sender. First upload requires a 6-character code emailed to you, then cached. Upstream `send`-style clients do not work.
- composes with: A send is free, needs no account and transfers up to 50 Go.
- reliability: The write path requires human verification at the API: POST /api/containers without a recaptcha field returns 400 'The recaptcha field is required. (and 1 more error)'. swissfer routes around this with an emailed 6-char confirmation, not with a token. The 30-day option is a trap. It silently deletes at 15 days unless the sender acts on day 12.
- notes: 50 GB per transfer, all files combined, no account required. Hosted in Infomaniak's own Swiss datacentres. One notable global property: the source is open (Infomaniak android/iOS/multiplatform clients on GitHub) and there is a working CLI.
- evidence:
  - [1] 2026-10-21: '50 GB', retention table, download caps, 'cannot be reactivated or extended'
  - [2] 2026-10-21: probe: POST -> 400 {'message':'The recaptcha field is required. (and 1 more error)'}
  - [3] 2026-10-21: (Oct 2026) — independent confirmation of the day-12 extension mechanics
  - [1] 2026-11-09: the FAQ states SwissTransfer accepts files up to 50 GB | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: SwissTransfer accepts files up to 50 GB in size, which is particularly useful for large files that cannot be sent as email attachments or by other traditional means.
  - [1] 2026-11-09: the FAQ states files are automatically deleted after 15 days, with an extension offered on day 12 | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: When choosing 30 days, files are automatically deleted after 15 days, but an extension is offered to the sender by email on the 12th day, and remains available for 3 days, in order to extend the availability up to the desired 30 days.
  - [1] 2026-11-25: the Infomaniak FAQ states a 50 GB file size limit | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: SwissTransfer accepts files up to 50 GB in size, which is particularly useful for large files that cannot be sent as email attachments or by other traditional means.
  - [1] 2026-11-25: the FAQ states the 50 GB figure | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: SwissTransfer accepts files up to 50 GB in size, which is particularly useful for large files that cannot be sent as email attachments or by other traditional means.
  - [1] 2026-11-25: the FAQ states the 15-day deletion and the day-12 extension window for a 30-day selection | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: When choosing 30 days, files are automatically deleted after 15 days, but an extension is offered to the sender by email on the 12th day, and remains available for 3 days, in order to extend the availability up to the desired 30 days.
  - [1] 2026-11-25: the FAQ still states the 15-day deletion and day-12 extension | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: When choosing 30 days, files are automatically deleted after 15 days, but an extension is offered to the sender by email on the 12th day, and remains available for 3 days, in order to extend the availability up to the desired 30 days.
  - [1] 2026-11-25: the FAQ states the 10 GB archive threshold for one-by-one downloads | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: If the archive exceeds 10 GB, you will need to download the data files one by one.
  - [1] 2026-11-25: the FAQ still states the 10 GB archive threshold | capture: sha256:c647b8b285893bc7cd98c552b0e659b441cde645fc14d44f7d83bd7f5798df6c | quote: If the archive exceeds 10 GB, you will need to download the data files one by one.
  - [4] 2026-11-25: the product page states a free 50 Go send with no account | capture: sha256:fcd4dca58e37fd7a2fc709474982984ea3f6694fbb1209ceeb5b9c0e8c26d9ca | quote: SwissTransfer permet de transférer jusqu'à 50 Go par envoi, gratuitement, sans créer de compte.
  - [4] 2026-11-25: the product page still states a free no-account 50 Go send | capture: sha256:fcd4dca58e37fd7a2fc709474982984ea3f6694fbb1209ceeb5b9c0e8c26d9ca | quote: SwissTransfer permet de transférer jusqu'à 50 Go par envoi, gratuitement, sans créer de compte.
- sources:
  - [1] https://www.infomaniak.com/en/support/faq/2929/understanding-swisstransfer-data-limits
  - [2] https://www.swisstransfer.com/api/containers
  - [3] https://linkinseconds.com/blog/swisstransfer-limits
  - [4] https://www.swisstransfer.com/
