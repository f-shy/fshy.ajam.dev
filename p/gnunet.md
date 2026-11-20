# gnunet fs as a storage provider

> gnunet.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gnunet/ | JSON https://fshy.ajam.dev/api/v1/entity/gnunet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gnunet fs as a storage provider

- `storage/gnunet-fs-as-a-storage-provider` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.gnunet.org/master/users/configuration.html
- free tier: None reachable: Files are addressed by hash onto a DHT with no hosting guarantee. Retrievability requires live peers holding the blocks, and the local QUOTA setting governs only your own datastore. docs.gn. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Files are addressed by hash onto a DHT with no hosting guarantee — retrievability requires live peers holding the blocks, and the local QUOTA setting governs only your own datastore.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Files are addressed by hash onto a DHT with no hosting guarantee — retrievability requires live peers holding the blocks, and the local QUOTA setting governs only your own datastore.…
  - [2] 2026-10-21: cited as the basis of the rejection: Files are addressed by hash onto a DHT with no hosting guarantee — retrievability requires live peers holding the blocks, and the local QUOTA setting governs only your own datastore. docs.gn
- sources:
  - [1] https://docs.gnunet.org/master/users/configuration.html
  - [2] https://docs.gnunet.org/latest/users/fs.html
