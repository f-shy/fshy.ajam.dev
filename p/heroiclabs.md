# Heroic Labs

> heroiclabs.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heroiclabs/ | JSON https://fshy.ajam.dev/api/v1/entity/heroiclabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Heroic Labs

- `compute/heroic-labs` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:50.016Z (live) | stale on 2026-12-26
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
  - [1] 2026-11-25: the hosted product is a managed cloud reached through the Heroic Cloud signup, and the captured homepage states no free tier | capture: sha256:3ec820dda01b834fbe372a3adac0ab405c7908c6757a7390f607a8ce8f2818bf | quote: Deploy and scale your Heroic Gamestack on our managed cloud.
- sources:
  - [1] http://heroiclabs.com

## nakama / heroic cloud storage engine

- `storage/nakama-heroic-cloud-storage-engine` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:48.160Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: Heroic Labs still describes Nakama storage as unfit for a large object store | capture: sha256:00e1323d6e0deea02e9c01efef654f7221459a56fa1cd30b5c5c3b8e2c7030b0 | quote: our recommendation is still to use a large object store like S3. You may try using the storage engine however we don’t guarantee it will perform well at scale.
- sources:
  - [1] https://forum.heroiclabs.com/t/storage-max-size-in-megabytes/3459
