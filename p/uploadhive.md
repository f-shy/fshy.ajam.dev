# UploadHive

> uploadhive.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadhive/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadhive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UploadHive

- `storage/uploadhive` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uploadhive.com
- free tier: Free tier published table: max upload file size 'Unlimited', download volume 'Unlimited', storage column '-' (no storage cap published), files deleted 50 days after last download | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Free tier published table: max upload file size 'Unlimited', download volume 'Unlimited', storage column '-' (no storage cap published), files deleted 50 days after last download | days: 50 | source: [1] | note: not stated
- egress: 'Download volume: Unlimited' on the free row; direct fs430.uploadhive.com/cgi-bin/dl.cgi/<key>/<name> links | metered: no
- identity: institution
- interface: rest
- limits:
  - retention-clamped (binding): deleted 50 days [1]
- limits note: unlimited per file; 50 days after last download for free; no API key needed for anonymous upload
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: XFileSharing Pro family (sibsoft.net/xfilesharing.html). Same shape as ~hundreds of hosts, so one client works across all of them; discovery is GET /server -> {"url":"https://fs430.uploadhive.com/cgi-bin"} then POST upload.cgi with utype=anon; also used by PolyUploader (github.com/spel987/PolyUploader).
- composes with: 3 layers: (a) files per host carry no stated limit, (b) 50-day retention resets on download so a periodic re-fetch keeps data alive indefinitely, (c) the whole XFileSharing family is the multiplier. Each host takes one free registration with its own 100s-of-GB-to-2TB pool (see UpZur/FileAxa/Mega4up entries).
- reliability: Dl.cgi returned 'Wrong IP' on every download attempt regardless of referer/cookies. Downloads appear bound to the uploading IP, so a distributed fetch layer needs matching egress IPs.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: Free row: Max upload file size 'Unlimited', Download volume 'Unlimited', deletion '50 days after last download'
  - [2] 2026-10-21: 'Powered by XFileSharing Pro'
  - [3] 2026-10-21: probe: POST (utype=anon, sess_id=, file_0) -> 200 [{"file_code":"6wpsyu0nx862","file_status":"OK"}]
  - [4] 2026-10-21: probe: POST /6wpsyu0nx862 op=download2 -> 200 page containing ; GET that -> 200 body 'Wrong IP' (8 bytes)
- sources:
  - [1] https://uploadhive.com/premium
  - [2] https://uploadhive.com/pages/faq/
  - [3] https://fs430.uploadhive.com/cgi-bin/upload.cgi
  - [4] https://fs430.uploadhive.com/cgi-bin/dl.cgi/<key>/probe.bin
