# timvisee Send instances

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-timvisee/ | JSON https://fshy.ajam.dev/api/v1/entity/github-timvisee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## timvisee Send instances (Firefox Send forks)

- `storage/timvisee-send-instances` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/timvisee/send-instances
- free tier: Per-instance. Public table (read live) includes send.cyberjake.xyz at 10 GiB / 30 days / 100 downloads and send.adminforge.de at 8 GiB / 7 days / 1,000 downloads. The listed send.skylerszijjarto.com at 250 GiB / 7 days / 10,000 downloads and send.hostnetwork.xyz at 2.5 GiB / 999,999 downloads are the two outliers. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: the table's Size limit column (2.5 GiB | bytes: 2684354560 | source: [1] | note: not stated
- retention: Retention: the Time limit column (3 to 30 days), MAX_EXPIRE_SECONDS on the server | days: 30 | source: [1] | note: not stated
- egress: unmetered; direct file URLs on the instance host, no egress pricing. | metered: no
- identity: email
- interface: rest, cli
- limits:
  - retention-clamped: Retention: the Time limit column (3 to 30 days [1]
  - per-object-cap (binding): per-object-cap: the table's Size limit column (2.5 GiB [1]
- limits note: Per-object-cap: the table's Size limit column (2.5 GiB to 250 GiB). Retention: the Time limit column (3 to 30 days), MAX_EXPIRE_SECONDS on the server. pull-count: the DL limit column. Adminforge allows 1,000, hostnetwork 999,999, but most sit at 10-100. The pull cap, not bytes, is the real bind on the E8 workload.
- interface detail: rest
- tooling: Ffsend (github.com/timvisee/ffsend). Real CLI with --host URL. Server is a self-hostable Rust binary, so the config (MAX_FILE_SIZE, MAX_EXPIRE_SECONDS) is public per instance.
- composes with: 15+ public instances in the table, each an independent operator with its own quota => shard across instances rather than accounts. Since the server is self-hostable, the ceiling on an instance you run is only your own disk.
- reliability: All files are E2E encrypted client-side and deleted on expiry; no originals re-encode.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 
  - [3] 2026-10-21: probe: GET -> 200 6176 bytes, page says 'send up to 10GB'
  - [4] 2026-10-21: probe: GET -> 530 465; GET https://send.adminforge.de/ -> 525 (both dead at probe time)
- sources:
  - [1] https://github.com/timvisee/send-instances/blob/master/README.md
  - [2] https://github.com/timvisee/send-instances
  - [3] https://send.cyberjake.xyz/
  - [4] https://send.skylerszijjarto.com/
