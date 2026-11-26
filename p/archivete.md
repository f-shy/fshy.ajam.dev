# transfer.archivete.am

> archivete.am | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archivete/ | JSON https://fshy.ajam.dev/api/v1/entity/archivete.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## transfer.archivete.am

- `storage/transfer-archivete-am` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.437Z (live) | stale on 2026-12-04
- url https://transfer.archivete.am
- free tier: no account; no published per-file cap (transfer.sh successor, same DutchCoders codebase) | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered direct links; plain GET returns bytes | metered: no
- identity: anonymous
- interface: rest, cli
- limits note: Retention not stated on the landing page (unverified); transfer.sh lineage default was 14 days. No rate limit observed.
- interface detail: rest
- tooling: Curl --upload-file ./f https://transfer.archivete.am/f. The original transfer.sh CLI contract, unchanged. Also supports /virustotal and /scan suffixes.
- composes with: None. Per-file only, no account surface. N files with independent expiry.
- reliability: THE transfer.sh successor that actually answers. This is the one live instance found; the long list of 'transfer.sh alternatives' blogs mostly point at dead clones.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no account; no published per-file cap (transfer.sh successor, same DutchCoders codebase)
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: PUT --upload-file probe.bin -> 200, body 'https://transfer.archivete.am/8Rt07/probe.bin', header X-Url-Delete present; GET that URL -> 200, 32768 B, application/octet-stream, sha256 MATCH
- evidence:
  - [1] 2026-10-21: 'Easy file sharing from the command line', curl upload/download examples
  - withheld 2026-10-21: probe: PUT --upload-file -> 200 + URL + X-Url-Delete; GET -> 200 / 32768 B / sha256 match
  - [1] 2026-11-19: the first-party page still documents the curl PUT --upload-file REST upload contract | capture: sha256:3178041b1bf3f2ee6c55c5ef0ac6e0fdf125f1cbb514863c6fdc4635450ca469 | quote: $ curl -X PUT --upload-file "-" https://transfer.archivete.am/test.txt
- sources:
  - [1] https://transfer.archivete.am/
