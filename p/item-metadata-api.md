# Item Metadata API

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/item-metadata-api/ | JSON https://fshy.ajam.dev/api/v1/entity/item-metadata-api.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Item Metadata API (MDAPI) as free key-value/JSON store

- `storage/item-metadata-api-as-free-key-value-json-store` | fails-quota | evidence reported | binding request-rate | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:26.502Z (live) | stale on 2026-11-19
- url https://archive.org/developers/metadata.html
- free tier: No per-item metadata size is published; unlimited items x one JSON doc each, transaction-safe, free. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free reads (public items), gzip/deflate supported | metered: no
- identity: email | detail: Internet Archive account (email address, screen name, password); the S3 keys used for MDAPI writes come from that account.
- interface: rest
- limits:
  - request-rate (binding): unverified: writes are tasks limited per user over a period, HTTP 429 Too Many Requests at the threshold; the threshold is not published [2]
- limits note: One item per call, no wildcarding; custom fields must follow XML naming; writes are queued like any other item transaction; not intended for bulk blob data.
- binding note: writes are tasks limited per user over a period (HTTP 429); the threshold is not published
- interface detail: rest
- tooling: ia metadata -m / Python MDAPI; auth via the same IAS3 keys (Authorization: LOW)
- composes with: Side-car index for the 20TiB: one small JSON doc per item holding checksums, shard maps, source URLs. Solves IAS3's 'cannot list all my items' problem without running your own database.
- reliability: Safe for bookkeeping, useless for bytes; concurrent writers need the documented concurrency pattern or they clobber metadata.
- notes: the same as the free tier
- evidence note: reported: vendor pages read on 2026-11-03 show the sign-up fields (https://archive.org/account/signup), the per-user write task limit (https://archive.org/developers/md-write.html) and the one-item-per-call rule (https://archive.org/developers/metadata.html). The free allowance and the write threshold are not stated there; retention and per-object cap were not read.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No per-item metadata size is published; unlimited items x one JSON doc each, transaction-safe, free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: (snapshot 2026-02-04) — 'may even store ad hoc JSON data in a transaction-safe manner', 'MDAPI cannot operate on more than one item at a time. There is no wildcarding'
  - [3] 2026-10-21: S3 keys sent with 'Authorization: LOW' are accepted by MDAPI write
  - [4] 2026-11-03: the Internet Archive sign-up asks for an email address, a screen name and a password | capture: sha256:4b8b71aa7dd07a92b006c16919f3bc85576963d0e7852ea30ce4dd5b0a6cafee | quote: Enter your email address
  - [2] 2026-11-03: metadata writes are rate limited per user; the threshold is not given | capture: sha256:12173a1463a5c31c1f168dd4b704d4605bf21270762c3acdb5e82c0ba0522405 | quote: Users are limited in the number of tasks they may submit over a period of time.
  - [1] 2026-11-03: one item per call, no wildcarding | capture: sha256:7f8c886c76904cef1f82cfd19f9414ab36249fcfbe8572a03651904efc284daa | quote: MDAPI cannot operate on more than one item at a time.
  - [1] 2026-11-03: S3 keys authorize MDAPI calls with Authorization: LOW | capture: sha256:7f8c886c76904cef1f82cfd19f9414ab36249fcfbe8572a03651904efc284daa | quote: Internet Archive’s S3 keys can be sent using the `Authorization: LOW` header.
  - [2] 2026-11-04: metadata writes are rate limited per user; the threshold is not given | capture: sha256:12173a1463a5c31c1f168dd4b704d4605bf21270762c3acdb5e82c0ba0522405 | quote: Users are limited in the number of tasks they may submit over a period of time.
  - [1] 2026-11-04: one item per call, no wildcarding | capture: sha256:7f8c886c76904cef1f82cfd19f9414ab36249fcfbe8572a03651904efc284daa | quote: MDAPI cannot operate on more than one item at a time.
  - [4] 2026-11-04: the sign-up asks for an email address | capture: sha256:4b8b71aa7dd07a92b006c16919f3bc85576963d0e7852ea30ce4dd5b0a6cafee | quote: Enter your email address
- sources:
  - [1] https://archive.org/developers/metadata.html
  - [2] https://archive.org/developers/md-write.html
  - [3] https://archive.org/developers/ias3.html
  - [4] https://archive.org/account/signup
