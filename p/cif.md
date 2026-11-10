# PeerTube

> cif.su | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cif/ | JSON https://fshy.ajam.dev/api/v1/entity/cif.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PeerTube — peertube.cif.su (open registration, unlimited quota)

- `storage/peertube-peertube-cif-su` | qualifies-with-caveat | evidence reported | binding write-gated | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://peertube.cif.su
- free tier: Unlimited total quota (`user.videoQuota: -1`), 5 GiB per day (`videoQuotaDaily: 5368709120`). Registration open, no approval, no email verification. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Instance serves HTTP + WebTorrent/HLS; no egress meter. Peers can also seed via BitTorrent, offloading the host. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-ip-shaping: 5 GiB per day [1]
  - per-ip-shaping: 5 GiB/day [1]
  - write-gated (binding): approval, no email verification [1]
  - write-gated (binding): approval-gated and not open-signup [1]
- limits note: 5 GiB/day at cif.su is the binding constraint (a two-year fill for 3 TiB). Per-file cap is the global `video.file` size limit, not separately published; accepted containers include mkv/mov/avi/flac, so arbitrary-ish binaries can be wrapped. Some instances (diode.zone) are unlimited but approval-gated and not open-signup.
- interface detail: rest
- tooling: yt-dlp `PeerTube` extractor (verified present). Native REST API v1: `/api/v1/videos`, `/api/v1/users/me`, resumable upload via `X-Upload-Content-Length`. rclone has no native backend; a shell/curl wrapper is trivial.
- composes with: cif.su alone is 5 GiB/day = ~1.8 TiB/year per account with no total ceiling. Multiply across the ~15 open-signup instances in the index and across accounts. hittube.fr is a flat 50 GiB with unlimited daily; arkcast.mycreationhaven.com is 5 GiB with unlimited daily.
- reliability: Volunteer-run instances disappear without notice. A single admin's disk decision deletes the archive. `videoFile.update` is disabled on cif.su, so you cannot patch an upload in place.
- notes: the same as the free tier
- evidence:
  - withheld 2026-10-21: probe: GET peertube.cif.su/api/v1/config -> {"signup":{"allowed":true,"requiresApproval":false,"requiresEmailVerification":false},"user":{"videoQuota":-1,"videoQuotaDaily":5368709120}}
  - withheld 2026-10-21: probe: GET instances.joinpeertube.org/api/v1/instances?count=100 -> 1,783 instances indexed; open-signup with quota: hittube.fr 53687091200, arkcast 5368709120, cif.su -1
  - withheld 2026-10-21: probe: GET peertube.cif.su/api/v1/videos/<uuid> -> files[] = {fileUrl: .../static/web-videos/<uuid>-0.mp4, size, resolution}, downloadEnabled: true
- sources:
  - [1] https://peertube.cif.su/api/v1/config
