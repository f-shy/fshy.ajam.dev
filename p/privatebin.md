# PrivateBin public instance network

> privatebin.info | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privatebin/ | JSON https://fshy.ajam.dev/api/v1/entity/privatebin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PrivateBin public instance network

- `storage/privatebin-public-instance-network` | fails-quota | evidence documented | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:57.980Z (live) | stale on 2026-12-04
- url https://privatebin.info/directory/
- free tier: 10 Megabytes (sizelimit = 10485760 bytes) per document or comment by default, set by each instance's operator; file upload is off by default (fileupload = false). | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 Megabytes per document or comment by default (sizelimit = 10485760 bytes); each instance's operator may change it. | bytes: 10485760 | source: [1] | note: not stated
- retention: Expiry is chosen per paste from options set by the instance operator: 5min (300 s), 10min, 1hour, 1day, 1week, 1month (30 days), 1year, and never (0, no expiry). | source: [1] | note: not stated
- egress: free, direct from each instance; most are Cloudflare-proxied (the directory lists CSP/Observatory ratings and uptime). | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 10485760 bytes per document or comment by default (sizelimit) [1]
- limits note: 10 MB per paste by default (per-instance override); file upload is disabled by default (fileupload = false) and about half the directory shows no file-upload support; burn-after-reading and expiry are server-configurable.
- binding note: each document or comment is capped at 10485760 bytes by default; there is no per-account quota because there are no accounts to meter, and each instance sets its own cap
- interface detail: rest
- tooling: Encrypted JSON POST to the instance root with X-Requested-With: JSONHttpRequest; official JS client plus community CLIs. github.com/PrivateBin/PrivateBin (8690 stars). Instances are independently operated.
- composes with: N instances x 10 MB, and each instance is a separate operator with separate rate policy. So this is the one pastebin class where horizontal sharding across operators is native. Still only ~50 instances, so the aggregate is single-digit GB per round.
- reliability: Instances are volunteer-run with visible uptime as low as 47-49% in the directory, so shard redundancy is mandatory. Content is client-side encrypted, so the operator cannot dedupe or scan. And cannot recover your key either.
- notes: 10 Megabytes (sizelimit = 10485760 bytes) per document or comment by default, set by each instance's operator.
- evidence note: vendor pages captured 2026-11-03: https://raw.githubusercontent.com/PrivateBin/PrivateBin/master/cfg/conf.sample.php, https://privatebin.info/directory/; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 MB per document by default (sizelimit = 10000000 in upstream conf.sample.php); ~30+ listed public instances, some with file upload enabled. No account, no quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: full instance table with version, file-upload flag, uptime (47%-100%), country; 2.1.0 is current
  - [1] 2026-10-21: 'size limit per document or comment in bytes, defaults to 10 Megabytes / sizelimit = 10000000', 'fileupload = false'
  - [3] 2026-10-21: probe: GET -> 200; https://bin.disroot.org/?jsonld -> 200; https://privatebin.cc/?jsonld -> 200 (three instances live)
  - [1] 2026-11-03: the default size limit is 10 Megabytes per document or comment, sizelimit = 10485760 bytes | capture: sha256:a7bc94662f89b498b05782909d9313ef59c4b0bcde9dbb8a514d17e0751f92c8 | quote: ; size limit per document or comment in bytes, defaults to 10 Megabytes sizelimit = 10485760
  - [1] 2026-11-03: the expiry options run from 5min to 1year and include never = 0 | capture: sha256:a7bc94662f89b498b05782909d9313ef59c4b0bcde9dbb8a514d17e0751f92c8 | quote: 5min = 300 10min = 600 1hour = 3600 1day = 86400 1week = 604800; Well this is not exactly one month, it's 30 days: 1month = 2592000 1year = 31536000 never = 0
  - [1] 2026-11-03: file upload is disabled by default (fileupload = false) | capture: sha256:a7bc94662f89b498b05782909d9313ef59c4b0bcde9dbb8a514d17e0751f92c8 | quote: ; enable or disable the file upload feature, defaults to false fileupload = false
  - [2] 2026-11-03: the public directory lists each instance with version, HTTPS, file upload support, uptime and country | capture: sha256:d06f6ab71faa80b8fc3ed1b6caa0e30d6bb399156408b56cc428a456f810d411 | quote: | Address | Version | HTTPS | HTTPS enforced | recommended CSP | Observatory Rating | File upload | Uptime | Country |
- sources:
  - [1] https://raw.githubusercontent.com/PrivateBin/PrivateBin/master/cfg/conf.sample.php
  - [2] https://privatebin.info/directory/
  - [3] https://privatebin.net/?jsonld
