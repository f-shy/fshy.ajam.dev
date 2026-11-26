# CyberDrop

> cyberdrop.cr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyberdrop/ | JSON https://fshy.ajam.dev/api/v1/entity/cyberdrop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CyberDrop

- `storage/cyberdrop` | qualifies-with-caveat | evidence reported | binding none | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-25T04:14:18.949Z (live) | stale on 2026-12-10
- url https://cyberdrop.cr
- free tier: Not stated numerically. 'Will you keep my files forever? Yes'. No published storage ceiling found; account creation is unverified and email-less. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB per file; 50 MB per URL upload | source: [1] | note: the beta REST API has a separate 100 MB per-upload cap
- retention: Yes, we also offer a temporary uploads feature which will automatically delete your files after a certain period of time. | source: [1] | note: the FAQ offers temporary uploads that are deleted after a period it does not quantify; no numeric expiry is published on the pages read
- egress: No stated cap; files served directly. | metered: no
- identity: anonymous | detail: registration asks for a username and a password of 6-72 characters, explicitly does not use email, and is open
- interface: rest
- limits note: Strict extension allowlist: only video/audio/image/archive/doc extensions (.mp4 .mkv .mp3 .flac .png .pdf .zip .7z .tar .iso .torrent .kdbx ..). No .bin/.parquet/.npy. This kills it as a raw dataset store. CSAM scanning via Cloudflare tooling purges the entire account on any hit.
- interface detail: rest
- tooling: the FAQ documents a beta REST API with a personal token header, node discovery, multipart upload and uploaded-file listing; web upload is also available
- composes with: Unlimited email-less accounts x no stated quota x permanent retention. The classic anonfiles shape.
- reliability: Retention claims 'forever' and has been stable for years, but the extension allowlist and account-wide purge on a single CSAM hash match are real technical failure modes. Domain has rotated (.me -> .cr) more than once.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Will you keep my files forever? Yes, we also offer a temporary uploads feature'; allowed-extension list quoted in full
  - [2] 2026-10-21: probe: GET -> 200 (cyberdrop.me is dead: DNS NXDOMAIN / CF 1016)
  - [1] 2026-11-11: the FAQ answers that files are kept and only temporary uploads are deleted | capture: sha256:a23b5c755a15fb73dc3c33a655eb85c18ff3c78b6371afc38afde5ac81399b37 | quote: Yes, we also offer a temporary uploads feature which will automatically delete your files after a certain period of time.
  - [2] 2026-11-25: the home page states a 500 MB ceiling per uploaded file and a 50 MB ceiling for URL uploads | capture: sha256:effb24345d27b53e0ecb072a107d3d73ffd2ad925bbca0a2303bb1a9d0933cc9 | quote: ### Maximum upload size per file is 500 MB
  - [1] 2026-11-25: the FAQ states a 100 MB cap for the beta API upload path | capture: sha256:f2d96825689bca6238f1344b01efd9c14c22afc6cf18733124ebfad48b5eadcf | quote: Please note that our `API` is currently in BETA and has a MAX UPLOAD SIZE of `100 MB`. You will not be able to upload files larger than `100MB`.
  - [1] 2026-11-25: the FAQ confirms automatic deletion of temporary uploads without stating a numeric period | capture: sha256:993c003152c6d7c0509ebe0e644df774697567253880822a2f0dd394a0298e5c | quote: Yes, we also offer a temporary uploads feature which will automatically delete your files after a certain period of time.
  - [3] 2026-11-25: the registration page states a password-length rule and a username requirement | capture: sha256:606ed092b308c0796e4142016823e498c9a907673006c7c531c7e65b27427297 | quote: - Password must be 6-72 characters
  - [3] 2026-11-25: registration explicitly does not use an email address | capture: sha256:606ed092b308c0796e4142016823e498c9a907673006c7c531c7e65b27427297 | quote: Do not use email
  - [1] 2026-11-25: the FAQ documents a token-authenticated REST API for uploads and file listing | capture: sha256:f2d96825689bca6238f1344b01efd9c14c22afc6cf18733124ebfad48b5eadcf | quote: - Provide your personal `token` as an HTTP header. Register, and you'll get a token.
  - [2] 2026-11-25: the home page still states the 500 MB per-file ceiling | capture: sha256:effb24345d27b53e0ecb072a107d3d73ffd2ad925bbca0a2303bb1a9d0933cc9 | quote: ### Maximum upload size per file is 500 MB
  - [1] 2026-11-25: the FAQ still documents the token-based API and its 100 MB cap | capture: sha256:f2d96825689bca6238f1344b01efd9c14c22afc6cf18733124ebfad48b5eadcf | quote: Please note that our `API` is currently in BETA and has a MAX UPLOAD SIZE of `100 MB`. You will not be able to upload files larger than `100MB`.
  - [1] 2026-11-25: the FAQ still states that temporary uploads are automatically deleted | capture: sha256:993c003152c6d7c0509ebe0e644df774697567253880822a2f0dd394a0298e5c | quote: Yes, we also offer a temporary uploads feature which will automatically delete your files after a certain period of time.
  - [3] 2026-11-25: the registration page still states that email is not used | capture: sha256:606ed092b308c0796e4142016823e498c9a907673006c7c531c7e65b27427297 | quote: Do not use email
- sources:
  - [1] https://cyberdrop.cr/faq
  - [2] https://cyberdrop.cr/
  - [3] https://cyberdrop.cr/auth
