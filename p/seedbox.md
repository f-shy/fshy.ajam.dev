# seedbox.ch trialbox

> seedbox.ch | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/seedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## seedbox.ch trialbox

- `storage/seedbox-ch-trialbox` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:25.778Z (live) | stale on 2026-12-04
- url https://www.seedbox.ch/trialbox.php
- free tier: None reachable: 48-hour trial, 15 GB: 'Try a real managed seedbox free for 48 hours — no credit card. 15 GB'. Fails on both capacity and duration. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: Requires an e-mail address but no credit card: 'Just an e-mail — no credit card, no commitment.'
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 48-hour trial, 15 GB: 'Try a real managed seedbox free for 48 hours — no credit card. 15 GB'. Fails on both capacity and duration.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 48-hour trial, 15 GB: 'Try a real managed seedbox free for 48 hours — no credit card. 15 GB'. Fails on both capacity and duration.
  - [1] 2026-11-19: the trial signup asks for an e-mail address and no credit card | capture: sha256:a502fc8b116491243f9b61efdf1aa1c622c0640849087b49f2698df7aa6b9a7d | quote: Just an e-mail — no credit card, no commitment.
  - [1] 2026-11-19: the trial offers 15 GB of storage for 48 hours | capture: sha256:a502fc8b116491243f9b61efdf1aa1c622c0640849087b49f2698df7aa6b9a7d | quote: Free/ 48 hours - ✓15 GB storage
- sources:
  - [1] https://www.seedbox.ch/trialbox.php
