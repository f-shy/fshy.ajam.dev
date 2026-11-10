# Heroic Labs

> heroiclabs.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heroiclabs/ | JSON https://fshy.ajam.dev/api/v1/entity/heroiclabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Heroic Labs

- `compute/heroic-labs` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:01.212Z (live) | stale on 2026-11-22
- url http://heroiclabs.com
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price: the hosted product is reached by signup, and the framework itself is open source and run locally [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and presents an open-source backend with a managed cloud signup. No plan or price appears, which confirms paid-only for the hosted product and leaves the open-source half as software
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Nakama: the hugely popular open source game backend framework' with 'Take back control of your game backend and own your data' and a Heroic Cloud signup, quoted; no plan and no price on the page
- sources:
  - [1] http://heroiclabs.com

## nakama / heroic cloud storage engine

- `storage/nakama-heroic-cloud-storage-engine` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://forum.heroiclabs.com/t/storage-max-size-in-megabytes/3459
- free tier: None reachable: Storage objects are jsonb rows in Postgres. 'theoretically store up to 255 megabytes' but Heroic Labs explicitly advises against it ('we don't guarantee it will perform well at scale'). No. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Storage objects are jsonb rows in Postgres — 'theoretically store up to 255 megabytes' but Heroic Labs explicitly advises against it ('we don't guarantee it will perform well at scale'). No
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Storage objects are jsonb rows in Postgres — 'theoretically store up to 255 megabytes' but Heroic Labs explicitly advises against it ('we don't guarantee it will perform well at scale'). No
- sources:
  - [1] https://forum.heroiclabs.com/t/storage-max-size-in-megabytes/3459
