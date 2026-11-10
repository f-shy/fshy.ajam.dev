# DailyUploads

> dailyuploads.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dailyuploads/ | JSON https://fshy.ajam.dev/api/v1/entity/dailyuploads.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DailyUploads

- `debrid/dailyuploads` | qualifies-with-caveat | evidence measured | binding request-rate | category premium file host (XFileSharing), retrieval target | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:31:02.558Z (live) | stale on 2026-11-23
- url https://dailyuploads.net/premium/
- price USD 12.99 per 30 days (Standard) | parsed USD 12.99/mo
- free tier: no free tier is priced or quantified on the premium page; a 16.5 MB file downloaded anonymously with 4 usable connections and no server-side wait | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not stated on the premium page read; a 17,269,804 byte object served intact | source: [1]
- retention: not stated on the pages read; the object measured was uploaded 2024-07-07 and still served | source: [1]
- egress: free downloads are shaped and capped by connection count: 0.824 MiB/s and 1.117 MiB/s on one connection, 4 of 8 parallel requests served, and 32 parallel requests answered with HTTP 520 | metered: yes | free allowance: not published on the free path | price per TB: USD 12.99 per 30 days on the cheapest plan, which is labelled 'Download speed Standard' | source: [1]
- identity: anonymous | detail: no account or cookie was needed: two POSTs to the public page produced a working CDN token, and the file downloaded twice
- interface: rest, cli
- limits:
  - per-ip-shaping: 0.824-1.117 MiB/s on one connection; 4 of 8 parallel ranged requests served probe:https://dailyuploads.net/38hab1frtnb8
  - request-rate (binding): concurrency above 4: the extra requests are answered with a 102,800-byte HTML page under HTTP 200, and at 32 with HTTP 520 probe:https://dailyuploads.net/38hab1frtnb8
  - volume-quota: 300 GB/day of premium bandwidth [2]
  - per-object-cap: 4 GB per file free, 80 GB per file premium [3]
  - per-ip-shaping: free tier measured at 3.0 MB/s = 2.86 MiB/s [4]
- binding note: The CDN refuses the 5th parallel request with an HTML body under a 200, so a client configured for 8 connections silently receives 102,800-byte error pages in place of data. That failure arrives before any byte quota does.
- interface detail: two-step XFileSharing form (op=download1 then op=download2) mints a cdn89.files-cdn.com token that streams and honours Range; the 60 s countdown on the page is client-side only
- tooling: JDownloader, aria2 and a scripted form post; no API
- composes with: a 4-connection free ceiling means 1 TiB is 12 days at 1 MiB/s or 4.6 days at the measured 2.6 MiB/s aggregate, so it is a mirror, not a source
- reliability: The 60 s countdown is decorative; the real limit is a 4-connection cap that returns HTTP 200 with an HTML body for the refused connections, and HTTP 520 above that.
- notes: Single connection speeds measured at 0.824-1.117 MiB/s, while 4 connections achieve approximately 2.5 MiB/s. Free tier allows high-volume downloads, though the file network is smaller than major file hosts.
- evidence note: Full 16.47 MiB object downloaded and hashed twice with probe, then two ranged concurrency runs. What confirms the cap: a run at 5 and 6 connections to find the exact threshold.
- extras:
  - measured_mib_s.c1: 0.824
  - measured_mib_s.c1_second: 1.117
  - measured_mib_s.c8_data_only: 2.52
  - measured_mib_s.c8_probe_field: 2.636
  - measured_mib_s.c32: 0.873
  - c8_note: the probe's own aggregate is 2.636 MiB/s and it counts four 102,800-byte HTML refusals as bytes; data only is 4 x 2,158,725 bytes over 3,273.3 ms = 2.52 MiB/s
  - object_bytes: 17269804
  - object_sha256: 62f24489d49b95bf3587f8a3ec9a325fd34098e9ec2bbb2853ce1bafe3559cb9
  - connections: 1/8/32 connections
  - client_countdown_s: 60
  - server_wait_observed: none
  - cdn: cdn89.files-cdn.com
  - free_speed_mib_s: 2.861
  - premium_parallel: unlimited
  - max_file_free: 4 GB
  - max_file_premium: 80 GB
  - api: no
  - price_30d_usd: 12.99
  - price_ladder_reported: USD 12.99 / 30 days; USD 29.99 / 90 days; USD 49.99 / 180 days; a 365-day plan is listed
  - volume_tib_month: 1.0
- evidence:
  - probe:https://dailyuploads.net/38hab1frtnb8 2026-10-23: 17,269,804 bytes, sha256 62f24489d49b95bf3587f8a3ec9a325fd34098e9ec2bbb2853ce1bafe3559cb9 in 19,980.4 ms (0.824 MiB/s); a second download 15 min later 14,739.9 ms (1.117 MiB/s); 8 connections 3,273.3 ms with 4 of 8 ranges honoured; 32 connections HTTP 520 on all 32
  - probe:https://dailyuploads.net/38hab1frtnb8?op=download2 2026-10-23: the download2 form URL resolves to a CDN token that answers 206 with 'bytes 0-0/17269804' and content-disposition attachment
  - [1] 2026-10-23: 30 days USD 12.99 'Download speed Standard', 90 days USD 29.99 'Turbo', 365 days USD 89.99 'Max', one-time payments
  - [2] 2026-10-23: 30 days $12.99, 90 days $29.99, 180 days $49.99; '300 GB daily bandwidth'; 'Up to 80 GB / file'; 'Unlimited parallel downloads'
  - [3] 2026-10-23: 'Upload up to 4 GB for free'
  - [4] 2026-10-23: JD2 34.0 MB/s, browser 12.6 MB/s, free 3.0 MB/s
- sources:
  - [1] https://dailyuploads.net/premium/
  - [2] https://dailyuploads.net/?op=payments
  - [3] https://dailyuploads.net/
  - [4] https://filehostreviews.com/best-file-hosting-services/
