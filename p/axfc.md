# Axfc Uploader

> axfc.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/axfc/ | JSON https://fshy.ajam.dev/api/v1/entity/axfc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Axfc Uploader (あぷろだ / axfc.net)

- `storage/axfc-uploader` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.axfc.net
- free tier: No account, no total quota. Per-object only. '1ファイル最大128 GiB。複数ファイルも順番にアップロードできます' (max 128 GiB per file, multiple files uploaded in sequence). Upload form constant `data-max="137438953472"` = 128 GiB, confirming the number in the markup. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 128 GiB per file | bytes: 137438953472 | source: [1] | note: not stated
- retention: per-object-cap 128 GiB. Retention is client-chosen (published-until field showed 'No limit' on a live file) and additionally bounded by a download-count cap the uploader may set | source: [1] | note: not stated
- egress: No egress meter or paid bandwidth product; the whole service is stated free ('本サービスは、別途明示する場合を除き無料です'). | metered: no
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 128 GiB per file [1]
- limits note: Per-object cap is 128 GiB. Retention is user-selected with optional download-count limits. Read path requires POST operations: GET requests to /download return HTTP 405 with Allow: POST, and a tokenized POST returns HTTP 302 redirecting to the share page requiring form interaction.
- interface detail: rest
- tooling: No public API and no rclone backend. Form-POST only, behind a Laravel CSRF token (`_token`) plus a session cookie, with `delpass` (delete key, >=8 chars) and optional `expiry_datetime`/`maxcount`. The legacy numbered URLs (`/u/4144979`) still resolve; new uploads get random `/u/f_<22-char>` URLs.
- composes with: Account-less: unlimited objects per IP x 128 GiB each, with 'No limit' available as the expiry. Chain is a re-upload loop only if you set an expiry; with expiry unset the object has no scheduled deletion.
- reliability: This is the legendary Japanese uploader and it is emphatically alive: the public file list was showing uploads from minutes earlier on the day of this run. But it has already had at least one near-death outage that lost voicebanks (UTAU Wiki recorded the site going dark and coming back with a broken certificate), and its own terms say no-expiry is 'not a promise of permanent storage'. Treat it as a live service with a history of vanishing.
- notes: the same as the free tier
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
  - [2] 2026-10-22: 128 GiB per file, no registration. Re-read https://www.axfc.net/: HTTP 200, 1911 bytes, sha256 313b5538c03c1b34. Quoted: 登録不要。小さな資料から大きなファイルまで。リンクひとつで、いつものように。 [ファイルを共有する ↗](https://www.axfc.net/upload)[ファイルを探す →](https://www.axfc.net/files) ✓ 会員登録なし✓ リンクで限定共有 ファイルをドラッグ＆ドロップまたはファイルを選ぶ1ファイル最大128 GiB。複数ファイルも順番にアップロードできます。 広告 ## 最近の公開ファイル [一覧を見る →](https://www.axfc.net/files) アップロードした人が公開一覧への掲載を選んだファイルです。 [ZIPMedaBotsMugen.zipe17.7 MBOct 21, 2026, 23:07 UTC ↗](https://www.axfc.net/u/f_WH2-GZn7xyM_yFqIUbsiAw) ZIP261021-6.zip261021-6237.1 M
  - [1] 2026-10-21: '1ファイル最大128 GiB', form constant data-max="137438953472"
  - [3] 2026-10-21: live share page reads 'Available until: No limit'; 'Published Oct 21, 2026'
  - [4] 2026-10-21: public listing shows uploads timestamped the same day (Oct 21 2026, 14:55 UTC), so the service is actively receiving files
  - withheld 2026-10-21: probe: GET /download?tg=4144979 -> HTTP 405, Allow: POST; POST with a valid _token -> 302 back to /u/4144979 (needs a JS-driven second step)
- sources:
  - [1] https://www.axfc.net/upload
  - [2] https://www.axfc.net/
  - [3] https://www.axfc.net/u/4144979
  - [4] https://www.axfc.net/files
