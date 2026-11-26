# opencolorado.org

> opencolorado.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencolorado/ | JSON https://fshy.ajam.dev/api/v1/entity/opencolorado.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## opencolorado.org (regional CKAN, US)

- `storage/opencolorado-org` | fails-quota | evidence inferred | binding per-object-cap | category municipal-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://opencolorado.org/
- free tier: Historic operator statement: 100 GB total platform storage, individual uploads up to 50 MB, with the explicit goal of 'supporting data uploads which will make it much simpler for smaller organizations to participate'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 MB/file | bytes: 50000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: public. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): 50 MB/file [1]
- limits note: Per-object-cap 50 MB. Chunk-sized, not object-sized. Even if the instance were reachable, 50 MB/file and a 100 GB shared pool would need ~10,000 objects and would blow the pool.
- interface detail: CKAN.
- tooling: curl (currently blocked).
- composes with: n/a.
- reliability: unverified: Cloudflare hard-block ('Sorry, you have been blocked', Ray a4e337d6eef2ff1b).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Historic operator statement: 100 GB total platform storage, individual uploads up to 50 MB, with the explicit goal of 'supporting data uploads which will make it much simpler for smaller organizations to participate'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'At the present time we have 100GB of storage available and individual file uploads can be up to 50MB.'
  - [2] 2026-10-21: HTTP 403 Cloudflare block page
- sources:
  - [1] https://opencolorado.org/blog/opencolorado-is-hosting-data/
  - [2] https://opencolorado.org/
