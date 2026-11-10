# PANGAEA

> pangaea.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pangaea/ | JSON https://fshy.ajam.dev/api/v1/entity/pangaea.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PANGAEA (Data Publisher for Earth & Environmental Science)

- `storage/pangaea` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.pangaea.de
- free tier: Free to publish ('PANGAEA can be used free of charge'; a voluntary 500 EUR contribution is appreciated, not required). No total-volume cap found; the stated cap is per file. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 'Individual files must be less than 15 GB | bytes: 15000000000 | source: [1] | note: not stated
- retention: per-object-cap: 'Individual files must be less than 15 GB in size.' Retention: permanent (WDS member, DOI per dataset) | source: [1] | note: not stated
- egress: Free, anonymous, direct HTTPS with `Accept-Ranges: bytes` and `Access-Control-Allow-Origin: *`. Originals served from download.pangaea.de. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 'Individual files must be less than 15 GB [1]
- limits note: Per-object-cap: 'Individual files must be less than 15 GB in size.' Retention: permanent (WDS member, DOI per dataset). Between per-file cap and total there is a human editorial gate. 'might take up to several weeks'. Read constraint: no rate limit observed; the per-dataset bundle zip (allfiles.zip) is 401-gated while individual originals are 200.
- interface detail: rest
- tooling: No upload API. Submission is a web form + editor-issued upload link. Read side is fully scriptable: `https://download.pangaea.de/dataset/<ID>/files/<FILENAME>`, allfiles.zip/tar, and `?format=textfile|metadata_jsonl|linkset_json` on the DOI resolver. Works with plain curl/wget (the documented 'download multiple files' page is a file list).
- composes with: Unlimited datasets per login; each DOI mints a fresh dataset directory with independent quota. Originals are addressable per-file, so a caller can pull exactly the bytes wanted rather than the whole bundle.
- reliability: Submission queue is weeks long and editor-mediated; data may be reformatted on ingest for tabular submissions (originals are kept as binary objects and served byte-for-byte).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Individual files must be less than 15 GB in size'
  - [2] 2026-10-21: 'PANGAEA can be used free of charge'; 'might take up to several weeks'
  - [3] 2026-10-21: probe: GET -> 200, Content-Length 1962969, downloaded 1962969 bytes, body starts ffd8ff (real JPEG, original retrievable)
  - [4] 2026-10-21: probe: GET -> 401 Unauthorized (bundle gated, individual files not)
- sources:
  - [1] https://wiki.pangaea.de/wiki/Binary_objects
  - [2] https://www.pangaea.de/submit/index.php
  - [3] https://download.pangaea.de/dataset/958362/files/PS122_1_6_16_20191105_1_ROV_still_image_20191105T025942_IMG_8059.JPG
  - [4] https://download.pangaea.de/dataset/958362/allfiles.zip
