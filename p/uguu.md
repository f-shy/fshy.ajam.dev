# Uguu

> uguu.se | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uguu/ | JSON https://fshy.ajam.dev/api/v1/entity/uguu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uguu

- `storage/uguu` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uguu.se
- free tier: no account; 128 MiB max upload | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 128 MiB/file | bytes: 134217728 | source: [1] | note: not stated
- retention: 128 MiB/file, expires after 3 hours (homepage: 'Max upload size is 128 MiB & files expire after 3 hours') | days: 0 | source: [1] | note: not stated
- egress: unmetered direct links on d.uguu.se / n.uguu.se, plain GET, no gate | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 128 MiB/file [1]
  - retention-clamped: expires after 3 hours [1]
  - retention-clamped: expire after 3 hours [1]
- limits note: 128 MiB/file, expires after 3 hours (homepage: 'Max upload size is 128 MiB & files expire after 3 hours'). 15-upload burst all 200.
- interface detail: rest
- tooling: curl -F 'files[]=@x' 'https://uguu.se/upload?output=text'
- composes with: None. Per-file, no accounts. N x 128 MiB.
- reliability: The canonical 'it just works' endpoint. 3-hour retention makes it useless as storage, fine as a transport shim.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: quota
  - dead_end.why: no account; 128 MiB max upload
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST /upload?output=text -> 200 'https://n.uguu.se/gsrTFZov.bin'; GET -> 200, 32768 bytes, application/octet-stream (nginx, Accept-Ranges), sha256 MATCH. Second run returned d.uguu.se host — both work.
- evidence:
  - [1] 2026-10-21: 'Max upload size is 128 MiB & files expire after 3 hours'
  - withheld 2026-10-21: probe: POST /upload -> 200 + d.uguu.se URL; GET -> 200 / 32768 B / sha256 match
- sources:
  - [1] https://uguu.se/
