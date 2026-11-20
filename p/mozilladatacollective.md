# Mozilla Data Collective

> mozilladatacollective.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mozilladatacollective/ | JSON https://fshy.ajam.dev/api/v1/entity/mozilladatacollective.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mozilla Data Collective (MDC)

- `storage/mozilla-data-collective` | qualifies-with-caveat | evidence reported | binding per-object-cap | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:01.148Z (live) | stale on 2026-12-04
- url https://mozilladatacollective.com
- free tier: 150 GB per uploaded file. Raised from a lower value in the Python SDK on 2026-03-24 ('Increase upload file size limit to 150GB'). No published per-account or total quota anywhere in the provider terms, FAQ, or API reference; the archive in the public catalogue runs to multi-GB objects (one measured dataset is 9,786,006,314 bytes = 9.79 GB as a single .tar.gz). Uploads are multipart with a hard 10,000-part ceiling, so a 1 TB object would need ≥100 MB parts. The SDK enforces this and names the minimum part size rather than failing mid-upload. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 150 GB per upload | bytes: 150000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free to the consumer; downloads are short-lived presigned URLs, and downloads are limited to 7 per organisation per day (429 beyond that). | metered: no
- identity: email | detail: email
- interface: s3, rest
- limits:
  - request-rate: 7 downloads/day [1]
  - per-object-cap (binding): 150 GB per upload [1]
  - pull-count: 7 downloads/day [1]
  - write-gated: Review every request to upload'. You file a Request to Upload, wait days, and are int. [1]
  - write-gated: skipping the approval flow ends the account [1]
- limits note: Write-gated, hard. 'we manually review every request to upload'. You file a Request to Upload, wait days, and are interviewed by email. Every dataset must carry a datasheet. API upload calls are rate-limited at their discretion and skipping the approval flow ends the account. Downloads are limited to 7 per organisation per day.
- interface detail: rest + s3
- tooling: Best-in-slot for a scripted pipeline: a documented REST API at https://mozilladatacollective.com/api (bearer API key), plus a first-party Python SDK with resumable multipart uploads, configurable part_size and max_workers, and a .mdc-sample-upload.json resume-state file. Verified live: GET /api/health -> 200 (15 bytes), GET /api/datasets?limit=1 -> 200 with full metadata including sizeBytes and a SHA-256 checksum field.
- composes with: One dataset = one submission = one archive file plus one sample file. Nothing in the published terms caps the number of submissions per account, so the multiplier is submissions. The catalogue is browsable and enumerable anonymously through /api/datasets, which means the read side can be driven entirely from a script.
- reliability: The gate is a human reviewer, not a form. Treat acceptance as the scarce resource. 7 downloads/day/org will throttle any mirroring plan. Hash field is present in metadata, so a checksum roundtrip is cheap to automate.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: opened: 'In order to ensure that the datasets hosted in our platform are aligned with the Mozilla Data Collective values & manifesto we manually review every request to upload'; 'please allow for a few days to get back to you'.
  - [3] 2026-10-21: opened: commit 'Increase upload file size limit to 150GB' dated 2026-03-24. This is the only published per-file number and it is a code change, not marketing copy.
  - [1] 2026-10-21: opened: 'A single upload can have at most 10,000 parts … a 1 TB file needs parts of at least ~100 MB'; multipart, resumable, part floor 5 MB.
  - [4] 2026-10-21: opened: POST /datasets/{datasetId}/download returns a presigned downloadUrl with expiresAt, sizeBytes and checksum; 'Organizations are limited to 30 dataset downloads per day … 429'; 'Returns a presigned storage URL.'
  - [5] 2026-10-21: opened: 'MDC reserves the right to implement and enforce limits on MDC API upload calls'; subprocessor table lists 'Cloudflare R2 — Dataset storage of uploaded files — EU' and AWS Ireland.
  - [6] 2026-10-21: PROBED: curl -> HTTP 200, 15 bytes. curl https://mozilladatacollective.com/api/datasets?limit=1 -> HTTP 200, 1,626 bytes, real JSON. The API is live and needs no key for the catalogue.
  - withheld 2026-10-21: PROBED: GET /api/datasets/bibletts-luo-aligned-bible-speech-4118962a -> 200, datasetUrl, filename bibletts-luo-aligned-bible-speech-4118962a.tar.gz, sizeBytes 9786006314, checksum 221a7218f72a8fd106459d95dfd9341d3ff626e7456c2912336c0047bc96143f, isPaid false. Proves multi-GB single-object hosting actually exists on the platform.
  - [1] 2026-11-19: the SDK documents a 10,000-part ceiling per upload | capture: sha256:efbbb87a54af7c95489b4c2d40fde94033b0b8e18a2a02281025ec2a9c34816e | quote: A single upload can have at most 10,000 parts.
  - [4] 2026-11-19: the API reference states a 7-download-per-day organization limit | capture: sha256:24dc85524373ad18b992c173619381013cd758d825b011362e9146fc6c250b5b | quote: By Default, Organizations are limited to 7 dataset downloads per day. The limit resets at midnight UTC. When exceeded, the API responds with a 429 error.
- sources:
  - [1] https://mozilla-data-collective.github.io/datacollective-python/upload/
  - [2] https://community.mozilladatacollective.com/uploading-your-dataset-to-the-mozilla-data-collective-platform/
  - [3] https://github.com/Mozilla-Data-Collective/datacollective-python/compare/0.4.3...0.4.4
  - [4] https://mozilladatacollective.com/api-reference/docs
  - [5] https://mozilladatacollective.com/terms/providers
  - [6] https://mozilladatacollective.com/api/health
