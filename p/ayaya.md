# ayaya.beauty

> ayaya.beauty | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ayaya/ | JSON https://fshy.ajam.dev/api/v1/entity/ayaya.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ayaya.beauty

- `storage/ayaya-beauty` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:04.425Z (live) | stale on 2026-12-04
- url https://ayaya.beauty
- free tier: no account; 4 GiB per file | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GiB per file | bytes: 4294967296 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered direct links, dedicated byte path | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 4 GiB per file [1]
  - per-object-cap (binding): 4 GiB/file [1]
- limits note: 1 GiB/file, 14-day expiry (per its own listing and form limits). No rate limit seen over 4-upload burst.
- interface detail: rest
- tooling: curl -F 'file=@x' https://ayaya.beauty/upload -> JSON; ShareX/Chatterino configs and linked source code published
- composes with: None. No accounts. N x 1 GiB, 14-day expiry.
- reliability: Small operator, but the byte path is clean and the API is documented + open source. Two URL shapes, only one serves bytes. Easy to get wrong.
- notes: no account; 1 GiB per file
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no account; 1 GiB per file
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST /upload -> 200 JSON with link + directLinkExt 'https://ayaya.beauty/-/file/462G4.bin'; GET directLinkExt -> 200, 32768 B, 'application/octet-stream; charset=binary', sha256 MATCH. NOTE: the pretty 'linkExt' URL (/-/ form omitted) returns 200 with 1259 bytes of HTML — you must use directLinkExt.
- evidence:
  - [1] 2026-10-21: 1 GiB / 14-day expiry, upload form
  - withheld 2026-10-21: probe: POST /upload -> JSON; GET directLinkExt -> 200 / 32768 B / sha256 match; GET linkExt -> 200 but 1259 B HTML (trap)
  - [1] 2026-11-19: the first-page states a 4 GiB maximum upload size | capture: sha256:87b30c97bb867696447558ebfe840fd052ebd8e3b81e87a6542f21aa887d82b5 | quote: The maximum upload size is 4GiB, and files expire after 14 days.
  - [1] 2026-11-19: the first-party page states a 4 GiB per-file upload cap | capture: sha256:87b30c97bb867696447558ebfe840fd052ebd8e3b81e87a6542f21aa887d82b5 | quote: The maximum upload size is 4GiB, and files expire after 14 days.
  - [1] 2026-11-19: the first-party page states a 4 GiB maximum upload size | capture: sha256:87b30c97bb867696447558ebfe840fd052ebd8e3b81e87a6542f21aa887d82b5 | quote: The maximum upload size is 4GiB, and files expire after 14 days.
  - [1] 2026-11-19: the first-party page states a 4 GiB maximum upload size and a 14-day expiry | capture: sha256:87b30c97bb867696447558ebfe840fd052ebd8e3b81e87a6542f21aa887d82b5 | quote: The maximum upload size is 4GiB, and files expire after 14 days.
- sources:
  - [1] https://ayaya.beauty/
