# groups.io free

> groups.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/groups/ | JSON https://fshy.ajam.dev/api/v1/entity/groups.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## groups.io free (1 gb, and files is premium-only)

- `storage/groups-io-free` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:42.832Z (live) | stale on 2026-12-04
- url https://groups.io/helpcenter/single/storagespace/storagespace_allotted.htm
- free tier: none reachable: Basic plans: 1 GB. Worse, the storage is unreachable on a new free group: "Restriction: This feature is available only in Premium groups, Enterprise groups, and legacy Free groups." Groups… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Basic plans: 1 GB. Worse, the storage is unreachable on a new free group: "Restriction: This feature is available only in Premium groups, Enterprise groups, and legacy Free groups." Groups…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Basic plans: 1 GB. Worse, the storage is unreachable on a new free group: "Restriction: This feature is available only in Premium groups, Enterprise groups, and legacy Free groups." Groups…
  - [2] 2026-10-21: cited as the basis of the rejection: Basic plans: 1 GB. Worse, the storage is unreachable on a new free group: "Restriction: This feature is available only in Premium groups, Enterprise groups, and legacy Free groups." Groups c
  - [1] 2026-11-19: the first-party help centre still lists 1GB for Basic plans | capture: sha256:6962c8437c674a873c1ce94fdf3a2a0bb3c7723628e6188fb493be135301313a | quote: Basic plans: 1GB
  - [2] 2026-11-19: the Files feature is still restricted, with a 2GB per-file cap, so it is not free-group storage | capture: sha256:434a264dbe545efeaf5416a5bc5551a94818057acb683f3803a7f0c4eaa37529 | quote: Restriction: This feature is available only in
- sources:
  - [1] https://groups.io/helpcenter/single/storagespace/storagespace_allotted.htm
  - [2] https://groups.io/helpcenter/single/files/files_about.htm
