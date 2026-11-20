# Axfc Uploader

> axfc.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/axfc/ | JSON https://fshy.ajam.dev/api/v1/entity/axfc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Axfc Uploader (あぷろだ / axfc.net)

- `storage/axfc-uploader` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:09.752Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.axfc.net
- free tier: 1ファイル最大128 GiB。最大3ファイルを同時にアップロードできます。 | unit: GiB | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: 1ファイル最大128 GiB。最大3ファイルを同時にアップロードできます。 | bytes: 137438953472 | source: [1] | note: not stated
- retention: per-object-cap 128 GiB. Retention is client-chosen (published-until field showed 'No limit' on a live file) and additionally bounded by a download-count cap the uploader may set | source: [1] | note: unverified: the cited axfc share page now answers HTTP 404, so the recorded 'No limit' retention statement cannot be re-read
- egress: No egress meter or paid bandwidth product; the whole service is stated free ('本サービスは、別途明示する場合を除き無料です'). | metered: no
- identity: anonymous | detail: 登録不要
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 1ファイル最大128 GiB。最大3ファイルを同時にアップロードできます。 [1]
- limits note: Per-object cap is 128 GiB. Retention is user-selected with optional download-count limits. Read path requires POST operations: GET requests to /download return HTTP 405 with Allow: POST, and a tokenized POST returns HTTP 302 redirecting to the share page requiring form interaction.
- interface detail: rest
- tooling: No public API and no rclone backend. Form-POST only, behind a Laravel CSRF token (`_token`) plus a session cookie, with `delpass` (delete key, >=8 chars) and optional `expiry_datetime`/`maxcount`. The legacy numbered URLs (`/u/4144979`) still resolve; new uploads get random `/u/f_<22-char>` URLs.
- composes with: Account-less: unlimited objects per IP x 128 GiB each, with 'No limit' available as the expiry. Chain is a re-upload loop only if you set an expiry; with expiry unset the object has no scheduled deletion.
- reliability: This is the legendary Japanese uploader and it is emphatically alive: the public file list was showing uploads from minutes earlier on the day of this run. But it has already had at least one near-death outage that lost voicebanks (UTAU Wiki recorded the site going dark and coming back with a broken certificate), and its own terms say no-expiry is 'not a promise of permanent storage'. Treat it as a live service with a history of vanishing.
- notes: No account, no total quota. Per-object only. '1ファイル最大128 GiB。複数ファイルも順番にアップロードできます' (max 128 GiB per file, multiple files uploaded in sequence). Upload form constant `data-max="137438953472"` = 128 GiB, confirming the number in the markup.
- evidence note: re-read on 2026-10-22 (HTTP 200, 1911 bytes, sha256 313b5538c03c1b34). The page states the number in the record. The claim is documented, not measured.
- extras:
  - verified[0].url: https://www.axfc.net/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 1911
  - verified[0].sha256: 313b5538c03c1b34fec046f4e8f898aaa7ff9f108bf963a2210a1895a939e415
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-21: '1ファイル最大128 GiB', form constant data-max="137438953472"
  - [2] 2026-10-21: live share page reads 'Available until: No limit'; 'Published Oct 21, 2026'
  - [3] 2026-10-21: public listing shows uploads timestamped the same day (Oct 21 2026, 14:55 UTC), so the service is actively receiving files
  - withheld 2026-10-21: probe: GET /download?tg=4144979 -> HTTP 405, Allow: POST; POST with a valid _token -> 302 back to /u/4144979 (needs a JS-driven second step)
  - [1] 2026-11-09: the upload page states the 128 GiB per-file cap and three files at a time | capture: sha256:d1880ca8f26344af561f37732c6642118c96181ded9d9e68684dc6b36929cd7e | quote: 1ファイル最大128 GiB。最大3ファイルを同時にアップロードできます。
  - [4] 2026-11-09: the homepage states the service is free and needs no registration | capture: sha256:b21d363cc10b2d9177c95c61a16c3a544d63a0fd408612f65d01c47497bf75c9 | quote: ファイルの作成・編集も、送受信・共有も、登録不要・無料で利用できます。
  - [2] 2026-11-09: the share page cited for retention is gone and answered HTTP 404 | capture: sha256:183731f1c5315725e34e9183fd5eeb9ec9be47907ec1ece17668e301a1dd2da9 | quote: HTTP 404
  - [3] 2026-11-09: the public listing shows uploads dated 2026-11-09, so the service is active | capture: sha256:9ab8cf4a9096a2ca309de2caace91c74a819555f948bb054a0089b9098e865d0 | quote: ZIP261109-6.zip261109-6111.5 MBNov 9, 2026, 14:08 UTC ↗
- sources:
  - [1] https://www.axfc.net/upload
  - [2] https://www.axfc.net/u/4144979
  - [3] https://www.axfc.net/files
  - [4] https://www.axfc.net/
