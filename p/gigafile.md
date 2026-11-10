# gigafile member

> gigafile.nu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gigafile/ | JSON https://fshy.ajam.dev/api/v1/entity/gigafile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GigaFile (ギガファイル便)

- `storage/gigafile` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://gigafile.nu
- free tier: 300 GB per file, unlimited number of files, no account required ('1ファイル300Gまで、個数無制限') | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 300 GB per file | bytes: 300000000000 | source: [1] | note: not stated
- retention: 300 GB/file; retention selectable 3/5/7/14/30/60/100 days (default 5); 2 GB/day download per file per IP; optional 4-char download key and email notification; files expire hard after retention, no inactivity reset | days: 100 | source: [1] | note: not stated
- egress: free direct download via /download.php?file=<id>; no metering page exists, no bandwidth cap published; per-IP daily cap = 2 GB per file (5 downloads/day of the same file) | metered: no
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-ip-shaping: 2 GB/day [1]
  - per-object-cap (binding): 300 GB per file [1]
  - per-object-cap (binding): 300 GB/file [1]
  - retention-clamped: retention selectable 3/5/7/14/30/60/100 days [1]
- limits note: 300 GB/file; retention selectable 3/5/7/14/30/60/100 days (default 5); 2 GB/day download per file per IP; optional 4-char download key and email notification; files expire hard after retention, no inactivity reset
- interface detail: rest
- tooling: no rclone backend; plain multipart POST to https://<nn>.gigafile.nu/upload_chunk.php (id, name, chunk, chunks, lifetime, file); chunk_size=100mb, max_size=300gb are published as JS vars in the page source; own client is ~40 lines of python/curl
- composes with: Quota is per record, not per account. 10 TiB = 35 uploads of 300 GB, 20 TiB = ~70; no account, no identity, so nothing to register and nothing to shard around. Only the 100-day retention forces a re-upload cycle.
- reliability: Download endpoint only serves when called with the referer/cookie chain from the file page (a bare GET returns an 'open the proper download screen' interstitial); datacenter IPs are ad-walled but the byte path itself worked
- notes: the same as the free tier
- evidence note: The per-object cap and the retention band are stated on the page as read on 2026-10-21. Was reported, now documented.
- evidence:
  - [1] 2026-10-21: '1ファイル300Gまで、個数無制限' (up to 300G per file, unlimited count), retention 3–100 days
  - [1] 2026-10-21: page source of — var max_size = "300gb"; var chunk_size = "100mb"; var server = "10.gigafile.nu"
  - [2] 2026-10-21: probe: POST (id,name,chunk=0,chunks=1,lifetime=7,file=probe.bin) -> 200 {"status":0,"url":"https://10.gigafile.nu/1029-b775394042aa285673c0da77eb508b1b5","delkey":"62fb"}
  - [3] 2026-10-21: probe: GET ... with referer+session cookie -> 200, application/octet-stream, 2048 bytes, byte-identical to uploaded file
  - [1] 2026-10-22: 200, 48,407 B on 2026-10-22; page description: '3 days to 100 days, seven selectable retention periods' and '300G per file'
- sources:
  - [1] https://gigafile.nu/
  - [2] https://10.gigafile.nu/upload_chunk.php
  - [3] https://10.gigafile.nu/download.php?file=1029-b77

## gigafile member / paid plan

- `storage/gigafile-member-paid-plan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ck.gigafile.nu/gigafile-member_1
- free tier: none reachable: The paid tier buys ad removal, not capacity. Verbatim from the member page: joining a paid plan gives '広告なしでファイルをアップロード / 広告なしでダウンロード' (upload and download without ads), plus playback and… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The paid tier buys ad removal, not capacity. Verbatim from the member page: joining a paid plan gives '広告なしでファイルをアップロード / 広告なしでダウンロード' (upload and download without ads), plus playback and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The paid tier buys ad removal, not capacity. Verbatim from the member page: joining a paid plan gives '広告なしでファイルをアップロード / 広告なしでダウンロード' (upload and download without ads), plus playback and…
  - [2] 2026-10-21: cited as the basis of the rejection: The paid tier buys ad removal, not capacity. Verbatim from the member page: joining a paid plan gives '広告なしでファイルをアップロード / 広告なしでダウンロード' (upload and download without ads), plus playback and fi
- sources:
  - [1] https://ck.gigafile.nu/gigafile-member_1
  - [2] https://gigafile.nu/
