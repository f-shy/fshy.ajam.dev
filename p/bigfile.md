# BigFile.net

> bigfile.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bigfile/ | JSON https://fshy.ajam.dev/api/v1/entity/bigfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BigFile.net

- `storage/bigfile-net` | qualifies | evidence documented | binding per-object-cap | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:04.787Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.bigfile.net
- free tier: No account and no published total quota. Storage is per-object and unbounded in count. 'Up to 256 GB per single file. No limit on batch uploads as long as each file is under 256 GB.'. | unit: GB | metered on: stored-bytes | read on: 2026-11-01 | source: [1]
- per-object cap: 256 GB per single file | bytes: 256000000000 | source: [1] | note: not stated
- retention: Uploaded files are kept for at least 365 days. Files that have not been downloaded for more than 365 days will be automatically deleted. | days: 365 | source: [1] | note: not stated
- egress: Unmetered. 'No speed limits. Speeds depend solely on your network bandwidth. We don't impose any artificial throttling.' Downloads served from Cloudflare with `Cache-Control: public, max-age=3600`. | metered: no
- identity: anonymous | detail: No registration is required and the vendor states that no email, phone or personal information is needed; uploads are handled anonymously.
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 256 GB per single file [1]
  - retention-clamped: Uploaded files are kept for at least 365 days; files not downloaded for more than 365 days are automatically deleted [1]
- limits note: Per-object-cap 256 GB. Retention: 'Uploaded files are kept for at least 365 days. Files that have not been downloaded for more than 365 days will be automatically deleted'. A sliding window, not a hard expiry, so a monthly GET sweep keeps everything alive indefinitely. No auth, no rate limit observed: 4 concurrent ranged GETs all returned 200 in 1.7-3.3 s.
- interface detail: rest
- tooling: Undocumented but functional chunked HTTP API, reverse-engineered from the site's own uploader JS: `POST https://u1.bigfile.net/v1/upload` with header `Content-Range: start-end`, header `Hash: <sha256 of whole file encoded base62>`, raw body = the chunk; response `{"status":true,"uri":"/d/<base62hash>"}`. Read path: `GET https://www.bigfile.net/d/<base62hash>` (direct octet-stream), plus `GET /d/<hash>/list.json` for multi-file shares. Uploader parallelises across `u1..uN.bigfile.net`. No rclone backend.
- composes with: Allows unlimited uploads per IP address with up to 256 GB per object. Objects have 365-day sliding retention based on access activity. Content addressing allows re-uploading identical hashes to refresh retention.
- reliability: Upload and read verified by SHA-256 on 2026-11-01. Site advertises a zero-database architecture without persistent file inventories. Lost hashes cannot be enumerated or recovered due to the lack of user accounts.
- notes: the same as the free tier
- evidence note: re-read on 2026-10-22 (HTTP 200, 1419 bytes, sha256 f960ea350c861ede). The page states the number in the record. The claim is documented, not measured.
- extras:
  - verified[0].url: https://www.bigfile.net/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 1419
  - verified[0].sha256: f960ea350c861edea0c897303ec4cc0c8591c2ff94eacc3789c5ec2dd75fecbe
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-22: the host answers at all. Re-read https://www.bigfile.net/: HTTP 200, 1419 bytes, sha256 f960ea350c861ede. Quoted: --- title: "Send Large Files Online Fast, Free & Secure" author: "BigFile.net" language: "en_US" description: "Upload and share your large files quickly and securely with BigFile.net – Free, high-speed bandwidth, anywhere online. No registration required." word
  - [2] 2026-10-21: probe: POST (102400 B, Content-Range 0-102399, Hash=9MHqkCQPcrV15ACXrzfQN9bIeE5hYm5PGk0hy6qXO2C) -> 200 {"status":true,"uri":"/d/9MHqkCQPcrV15ACXrzfQN9bIeE5hYm5PGk0hy6qXO2C"}; GET that URI -> 200, Content-Length 102400, sha256 matches upload exactly
  - withheld 2026-10-21: probe: second round with 3145728 B random payload -> upload 200, download 200, sha256 521fa7603ab4955cd275eac71d5419f09d8951a6a08a777f8997ccd1554afbf4 identical on both sides
  - [1] 2026-10-21: 'Up to 256 GB per single file. No limit on batch uploads', 'kept for at least 365 days', 'No registration required. No email, phone, or personal info needed'
  - [1] 2026-11-01: retention is a 365-day idle window, not a hard expiry, and the deletion rule is stated in full | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: Uploaded files are kept for at least 365 days. Files that have not been downloaded for more than 365 days will be automatically deleted.
  - [1] 2026-11-01: the retention-clamped limit is a 365-day idle window | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: Uploaded files are kept for at least 365 days. Files that have not been downloaded for more than 365 days will be automatically deleted.
  - [1] 2026-11-01: registration asks for nothing: anonymous is the stated identity cost | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: No registration required. No email, phone, or personal info needed. All uploads handled directly.
  - [1] 2026-11-01: the vendor page still describes an account-less single-link upload service, so the recorded REST client remains the only route | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: BigFile.net is a free large file sharing service that lets you upload and share large files with a single link. No registration, no account required.
  - [1] 2026-11-01: the vendor page as served on 2026-11-01 states the same per-object cap and batch rule | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: Up to 256 GB per single file. No limit on batch uploads as long as each file is under 256 GB.
  - [1] 2026-11-01: egress stays unmetered with no throttling; the same page states the 256 GB per-object cap, the 365-day idle window and the no-registration terms | capture: sha256:8a80bf4666632c6fc6afc95ac616ceb1fe2ef92ebbd3122288d2324bbe8d189d | quote: No speed limits. Speeds depend solely on your network bandwidth. We don't impose any artificial throttling.
- sources:
  - [1] https://www.bigfile.net/
  - [2] https://u1.bigfile.net/v1/upload
