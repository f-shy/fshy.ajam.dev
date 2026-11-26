# timvisee Send instances

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-timvisee/ | JSON https://fshy.ajam.dev/api/v1/entity/github-timvisee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## timvisee Send instances (Firefox Send forks)

- `storage/timvisee-send-instances` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:24.770Z (live) | stale on 2026-12-10
- url https://github.com/timvisee/send-instances
- free tier: send.cyberjake.xyz: size limit 10GiB, time limit 30 days, DL limit 100 | unit: GiB | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: 250GiB on send.skylerszijjarto.com | bytes: 268435456000 | source: [1] | note: Size limit 250GiB on send.skylerszijjarto.com; DL limit 10,000.
- retention: 30 days on send.cyberjake.xyz | days: 30 | source: [1] | note: 30 days time limit on send.cyberjake.xyz; DL limit 100.
- egress: unmetered; direct file URLs on the instance host, no egress pricing. | metered: no
- identity: email | detail: unverified: the public instance table states no registration requirement
- interface: rest, cli
- limits:
  - retention-clamped: 30 days on send.cyberjake.xyz [1]
  - per-object-cap (binding): 250GiB on send.skylerszijjarto.com [1]
- limits note: Per-object-cap: the table's Size limit column (2.5 GiB to 250 GiB). Retention: the Time limit column (3 to 30 days), MAX_EXPIRE_SECONDS on the server. pull-count: the DL limit column. Adminforge allows 1,000, hostnetwork 999,999, but most sit at 10-100. The pull cap, not bytes, is the real bind on the E8 workload.
- interface detail: rest
- tooling: Ffsend (github.com/timvisee/ffsend). Real CLI with --host URL. Server is a self-hostable Rust binary, so the config (MAX_FILE_SIZE, MAX_EXPIRE_SECONDS) is public per instance.
- composes with: 15+ public instances in the table, each an independent operator with its own quota => shard across instances rather than accounts. Since the server is self-hostable, the ceiling on an instance you run is only your own disk.
- reliability: All files are E2E encrypted client-side and deleted on expiry; no originals re-encode.
- notes: Per-instance. Public table (read live) includes send.cyberjake.xyz at 10 GiB / 30 days / 100 downloads and send.adminforge.de at 8 GiB / 7 days / 1,000 downloads. The listed send.skylerszijjarto.com at 250 GiB / 7 days / 10,000 downloads and send.hostnetwork.xyz at 2.5 GiB / 999,999 downloads are the two outliers.
- evidence note: the send-instances README states it holds a list of public Send instances
- evidence:
  - [2] 2026-10-21: 
  - [3] 2026-10-21: probe: GET -> 200 6176 bytes, page says 'send up to 10GB'
  - [4] 2026-10-21: probe: GET -> 530 465; GET https://send.adminforge.de/ -> 525 (both dead at probe time)
  - [1] 2026-11-09: the public table lists send.cyberjake.xyz at 10GiB, 30 days and a 100 download limit | capture: sha256:d44d2aea7e75b1a2c27348a38c07df92b1d81a124d81f27ad9c26527f897cb92 | quote: | [https://send.cyberjake.xyz](https://send.cyberjake.xyz/) | 10GiB | 30 days | 100 |
  - [1] 2026-11-09: the table lists send.skylerszijjarto.com at a 250GiB size limit | capture: sha256:d44d2aea7e75b1a2c27348a38c07df92b1d81a124d81f27ad9c26527f897cb92 | quote: | [https://send.skylerszijjarto.com](https://send.skylerszijjarto.com/) | 250GiB | 7 days | 10,000 |
  - [1] 2026-11-09: the page is the public instance table | capture: sha256:d44d2aea7e75b1a2c27348a38c07df92b1d81a124d81f27ad9c26527f897cb92 | quote: This page holds a list of public [Send](https://github.com/timvisee/send) instances.
  - [1] 2026-11-25: the instance table gives 250GiB size and 10,000 downloads for send.skylerszijjarto.com | capture: sha256:914fd168a16fe6d98341b9acb4317521f8cc2d24eef54e63a875cfa65b21737e | quote: | [https://send.skylerszijjarto.com](https://send.skylerszijjarto.com/) | 250GiB | 7 days | 10,000 |
  - [1] 2026-11-25: the instance table gives 30 days time and 100 downloads for send.cyberjake.xyz | capture: sha256:914fd168a16fe6d98341b9acb4317521f8cc2d24eef54e63a875cfa65b21737e | quote: | [https://send.cyberjake.xyz](https://send.cyberjake.xyz/) | 10GiB | 30 days | 100 |
  - [1] 2026-11-25: the instance table gives 10GiB size, 30 days time and 100 downloads for send.cyberjake.xyz | capture: sha256:914fd168a16fe6d98341b9acb4317521f8cc2d24eef54e63a875cfa65b21737e | quote: | [https://send.cyberjake.xyz](https://send.cyberjake.xyz/) | 10GiB | 30 days | 100 |
  - [1] 2026-11-25: the documented command-line client is ffsend with the --host URL flag | capture: sha256:914fd168a16fe6d98341b9acb4317521f8cc2d24eef54e63a875cfa65b21737e | quote: To use a specific instance from the command line with [ffsend](https://github.com/timvisee/ffsend), provide the `--host URL` flag while uploading.
- sources:
  - [1] https://github.com/timvisee/send-instances/blob/master/README.md
  - [2] https://github.com/timvisee/send-instances
  - [3] https://send.cyberjake.xyz/
  - [4] https://send.skylerszijjarto.com/
