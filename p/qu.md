# qu.ax

> qu.ax | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qu/ | JSON https://fshy.ajam.dev/api/v1/entity/qu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## qu.ax

- `debrid/qu-ax` | qualifies-with-caveat | evidence measured | binding retention-clamped | category anonymous temporary file host (pomf-style POST API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://qu.ax/
- price USD 0
- free tier: Max upload size is 256MB. Expiry is chosen per upload from 1 day, 7 days or 30 days; no account and no email are asked for. | unit: bytes | metered on: none | read on: 2026-10-23 | source: [1] | note: The offer is a per-object cap and a retention choice, not a byte allowance.
- per-object cap: Max upload size is 256MB | bytes: 256000000 | source: [1] | note: The page writes 256MB; the measured rejection point was not pushed to, so 256e6 is the page's decimal reading, not a measured byte boundary.
- retention: 1 day / 7 days / 30 days selected at upload. The default (no expiry field sent) produced expires=1795313693, which is 2026-11-22T02:14:53Z, exactly 30 days after the upload. | days: 30 | source: [1] | note: Measured from the epoch the API returned, not from the page.
- egress: Downloads are served from qu.ax itself; no byte allowance, no account and no published download counter. Nothing on the page meters traffic out. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account, no email, no cookie was sent; the upload was one POST from a bare HTTP client and a URL came back.
- interface: rest, cli
- limits:
  - per-object-cap: 256 MB per file [1]
  - retention-clamped (binding): 30 days maximum; the expiry is fixed at upload and cannot be extended measured: expires=1795313693 in the upload reply
- limits note: A file type allow-list runs before the size check: the same 1 MiB payload sent as payload-1mib.bin was refused with HTTP 400 {"message":"file type is not allowed","success":false}, and accepted once renamed to .txt. The download side is referer-gated: GET /x/leM7o.txt without a Referer answers 200 with an 8 254-byte HTML page, and the same request with Referer: https://qu.ax/leM7o answers 200 with the 1 048 576 bytes.
- binding note: At 1 TiB a month the 256 MB cap only means 4 000 uploads, which a loop handles; the hard stop is that nothing on the service extends a file past 30 days, so a re-fetch after a month needs the original bytes, which is no longer held if this was the only copy.
- interface detail: POST https://qu.ax/upload.php as multipart/form-data, field name 'files[]'. The reply is JSON: files[0].url, .size, .hash (SHA-1), .expires (epoch seconds).
- endpoint: part of interface detail
- tooling: curl -F 'files[]=@file' https://qu.ax/upload.php; a ShareX .sxcu is published at /static/quax.sxcu
- composes with: A 30-day, 256 MB anonymous mirror is the cheap middle tier of an archive: big enough for a single dataset shard, long enough to outlive a scrape job, and reachable by one curl line, so it composes with a scheduler and no credential store.
- reliability: Two gates before the bytes: an extension allow-list refuses .bin outright, and the raw path /x/<id>.<ext> serves a 200 HTML landing page unless the request carries a Referer header from the file page. Both produce HTTP 200, so a client that trusts status alone reads an error page as a download.
- notes: The caveat is the extension allow-list, the 30-day ceiling and the referer-gated download. For an archive of 20 TiB this is a distribution mirror, not storage: 80 000 files at 256 MB.
- evidence note: Upload, read-back and digest all happened in on 2026-10-23: 1 048 576 bytes posted, 1 048 576 bytes fetched from /x/leM7o.txt with the Referer header, SHA-256 matched. A push against the 256 MB edge would raise the cap from documented to measured.
- probe:
  - upload_bytes: 1048576
  - download_bytes: 1048576
  - sha256_expected: da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9
  - sha256_observed: da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9
  - match: yes
  - status: 200
  - download_requirements: Referer header; the API URL itself is a landing page
- extras:
  - api_reply_fields: files[0].url, .file_name, .hash (sha1), .size, .expires
  - largest_upload_tested_bytes: 1048576
- evidence:
  - probe:https://qu.ax/ 2026-10-23: POST of 1 048 576 bytes as payload-1mib.bin -> HTTP 400 {'message':'file type is not allowed','success':false}; the same bytes as .txt -> HTTP 200 with files[0].url=https://qu.ax/leM7o and expires=1795313693 (2026-11-22T02:14:53Z)
  - probe:https://qu.ax/leM7o 2026-10-23: the URL the API returned serves HTTP 200 with 8 254 bytes of text/html - the file page, not the file; its only download href is /x/leM7o.txt, which 302s back to the page when a Referer is absent
  - probe:https://qu.ax/x/leM7o.txt 2026-10-23: with 'Referer: https://qu.ax/leM7o' the same path returns 1 048 576 bytes of text/plain, sha256 da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9, full-body hash matched the uploaded file
  - [1] 2026-10-23: 'Max upload size is 256MB' and the 1 day / 7 days / 30 days expiry choices
- sources:
  - [1] https://qu.ax/
