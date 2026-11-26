# PANGAEA

> pangaea.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pangaea/ | JSON https://fshy.ajam.dev/api/v1/entity/pangaea.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PANGAEA (Data Publisher for Earth & Environmental Science)

- `storage/pangaea` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:16.851Z (live) | stale on 2026-12-10
- url https://www.pangaea.de
- free tier: Free to publish ('PANGAEA can be used free of charge'; a voluntary 500 EUR contribution is appreciated, not required). No total-volume cap found; the stated cap is per file. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Individual files must be less than 15 GB in size. | bytes: 15000000000 | source: [1] | note: Individual files must be less than 15 GB in size.
- retention: per-object-cap: 'Individual files must be less than 15 GB in size.' Retention: permanent (WDS member, DOI per dataset) | source: [1] | note: PANGAEA guarantees long-term availability of its content for at least 10 years (~75% is actually older than that).
- egress: Free, anonymous, direct HTTPS with `Accept-Ranges: bytes` and `Access-Control-Allow-Origin: *`. Originals served from download.pangaea.de. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits:
  - per-object-cap (binding): Individual files must be less than 15 GB in size. [1]
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
  - [1] 2026-11-11: individual files must be less than 15 GB in size | capture: sha256:641892cb8d021357ebcfc5a2583d89066f495ad362c6a5878f25b9ba827352ec | quote: Individual files must be less than 15 GB in size.
  - [1] 2026-11-19: the 15 GB per-file limit is unchanged | capture: sha256:be00948db0d3361f0dcbca64e66b603f5d0baea9f9230354e4653583dd24973f | quote: Individual files must be less than 15 GB in size.
  - [2] 2026-11-19: PANGAEA is still free of charge | capture: sha256:2b35573676c777decf9a578890fec267d50fd8abe5639a4a15d98a80142c3266 | quote: Check Costs. PANGAEA can be used free of charge. Nevertheless, we appreciate any possible financial support
  - [1] 2026-11-25: the PANGAEA binary objects page states a 15 GB per-file cap | capture: sha256:be00948db0d3361f0dcbca64e66b603f5d0baea9f9230354e4653583dd24973f | quote: Individual files must be less than 15 GB in size.
  - [5] 2026-11-25: the PANGAEA data submission page states long-term availability for at least 10 years | capture: sha256:f05a46d00b787246aad7d667986676904ef7be4ddba28ed294dbb2d658d1063f | quote: PANGAEA guarantees long-term availability of its content for at least 10 years (~75% is actually older than that).
  - [1] 2026-11-25: the PANGAEA binary objects page states the 15 GB per-file cap | capture: sha256:be00948db0d3361f0dcbca64e66b603f5d0baea9f9230354e4653583dd24973f | quote: Individual files must be less than 15 GB in size.
- sources:
  - [1] https://wiki.pangaea.de/wiki/Binary_objects
  - [2] https://www.pangaea.de/submit/index.php
  - [3] https://download.pangaea.de/dataset/958362/files/PS122_1_6_16_20191105_1_ROV_still_image_20191105T025942_IMG_8059.JPG
  - [4] https://download.pangaea.de/dataset/958362/allfiles.zip
  - [5] https://wiki.pangaea.de/wiki/Data_submission
