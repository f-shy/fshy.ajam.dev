# thingiverse

> thingiverse.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thingiverse/ | JSON https://fshy.ajam.dev/api/v1/entity/thingiverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## thingiverse

- `storage/thingiverse` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:28.945Z (live) | stale on 2026-12-04
- url https://forum.thingiverse.com/t/is-there-a-maximum-file-size-for-thingiverse-uploads/622
- free tier: None reachable: No published limit but uploads stall/fail on large files with no progress indicator. Unreliable rather than capped. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published limit but uploads stall/fail on large files with no progress indicator — unreliable rather than capped.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No published limit but uploads stall/fail on large files with no progress indicator — unreliable rather than capped.
  - [1] 2026-11-19: the first-party forum still documents uploads stalling with no progress indicator | capture: sha256:bb76e97e4b2533e05d96ac69d489b500e056fd165ea1a50efd198d57d53253ee | quote: The upload has been running for over 20 minutes, with no progress indicator or error message.
- sources:
  - [1] https://forum.thingiverse.com/t/is-there-a-maximum-file-size-for-thingiverse-uploads/622
