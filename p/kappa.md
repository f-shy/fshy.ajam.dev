# kappa.lol

> kappa.lol | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kappa/ | JSON https://fshy.ajam.dev/api/v1/entity/kappa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## kappa.lol (page title: segs.lol)

- `debrid/kappa-lol` | qualifies-with-caveat | evidence measured | binding none | category anonymous pomf-style file host with a JSON upload API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://kappa.lol/
- price USD 0
- free tier: No account and no stated per-file cap on the page read; the upload API takes a multipart 'file' field and answers with JSON. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The homepage publishes no number for size or retention, so the free tier is documented as unstated rather than guessed.
- per-object cap: unverified: no cap is published on the page; 1 MiB was accepted | source: [1] | note: The ceiling was not found, so the field stays null. A 1 GiB push would find it.
- retention: unverified: no expiry is published and the upload reply carries no expiry field | source: [1] | note: Retention is the one fact this service does not state anywhere on the page.
- egress: Downloads are served from kappa.lol; no byte counter and no download counter are published. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: One multipart POST with no cookie and no account returned a link; the reply also carries a delete URL, which is the only control the uploader gets.
- interface: rest, cli
- limits:
  - per-object-cap: not published; 1 MiB accepted probe:https://kappa.lol/api/upload
- limits note: The page title is 'segs.lol', not the host name: the brand and the domain disagree, which is the kind of drift that breaks a hard-coded allow-list.
- binding note: No documented constraint exists to name. At 1 TiB a month nothing in the seven-value vocabulary was observed to bind, because neither a cap nor a retention limit nor a rate is published; the honest answer is that the ceiling is unmeasured, not absent.
- interface detail: POST https://kappa.lol/api/upload multipart field 'file'. JSON reply: id, ext, type, checksum (MD5), key, link, delete.
- endpoint: part of interface detail
- tooling: An official uploader exists at github.com/Mald-Entertainment-Studio/uploader; curl works with one multipart POST
- composes with: A stored URL with no extension is a clean drop for a script that only needs a link a human can open; it pairs with a checksum check from the client side because the service returns MD5 itself.
- reliability: The reply URL carries no file extension (https://kappa.lol/P224n5), so a client that infers type from the URL gets application/octet-stream regardless of the real bytes.
- notes: Useful as a one-line anonymous store, unusable as an archive until the cap and retention are measured. The absent extension in the returned URL is the practical trap: a resumption test keyed on Content-Type will see application/octet-stream for every file.
- evidence note: Upload, read-back and SHA-256 match in on 2026-10-23. The record stays at measured even though the cap and retention are unverified, because neither is claimed as a number here.
- probe:
  - upload_bytes: 1048576
  - download_bytes: 1048576
  - match: yes
  - status: 200
- extras:
  - md5_echoed: 0316a02c6c0e8b28ad82065de17289c4
  - delete_url_in_reply: yes
- evidence:
  - probe:https://kappa.lol/api/upload 2026-10-23: POST of 1 048 576 bytes -> HTTP 200, JSON {'id':'P224n5','ext':'.bin','checksum':'0316a02c6c0e8b28ad82065de17289c4','link':'https://kappa.lol/P224n5'}; the checksum equals the MD5 of the uploaded file
  - probe:https://kappa.lol/P224n5 2026-10-23: read-back 1 048 576 bytes, sha256 da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9, full-body hash matched
  - [1] 2026-10-23: the page <title> is 'segs.lol'; no size or retention number appears on the page
- sources:
  - [1] https://kappa.lol/
