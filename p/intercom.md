# Intercom

> intercom.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/intercom/ | JSON https://fshy.ajam.dev/api/v1/entity/intercom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Intercom (article/Messenger attachments)

- `storage/intercom` | trial-only | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.intercom.com
- free tier: 'The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.' No account storage figure published. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: Fetching the same object with the signature stripped and the filename changed still returned 200 with the identical 498,804 bytes. So Intercom CDN URLs are effectively unauthenticated and permanent, which is a reusable pattern (and means 'signed' URLs elsewhere may also be decorative). | source: [1] | note: not stated
- egress: Free, Intercom CDN. Signed URLs with `expires` + `signature` params. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 100 MB [1]
- limits note: per-object-cap: 100 MB (Messenger), 20 MB total per incoming email including all files. request-rate: Intercom API rate limits apply. Retention: no expiry documented.
- interface detail: rest
- tooling: Intercom REST API (`/articles`, `/files`), official SDKs.
- composes with: 100 MB x unlimited attachments would be per-record-unlimited, but there is no free plan. All tiers start with 'Start free trial'. Cannot be multiplied into free storage.
- reliability: Important control: the CDN `signature` is NOT verified. Fetching the same object with the signature stripped and the filename changed still returned 200 with the identical 498,804 bytes. So Intercom CDN URLs are effectively unauthenticated and permanent, which is a reusable pattern (and means 'signed' URLs elsewhere may also be decorative).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.' No account storage figure published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'no limit on the number of attachments that can be uploaded'
  - [2] 2026-10-21: probe: GET ... -> 200, 498,804 bytes
  - withheld 2026-10-21: probe: same path with no query string and a truncated filename -> 200, 498,804 bytes, byte-identical — signature not enforced
  - [3] 2026-10-21: no free plan; every tier shows 'Start free trial'
- sources:
  - [1] https://www.intercom.com/help/en/articles/2339426-control-how-attachments-are-uploaded-and-used
  - [2] https://downloads.intercomcdn.com/i/o/tx2p130c/.../CleanShot...png?expires=...&signature=
  - [3] https://www.intercom.com/pricing
