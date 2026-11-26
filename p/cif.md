# PeerTube

> cif.su | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cif/ | JSON https://fshy.ajam.dev/api/v1/entity/cif.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PeerTube — peertube.cif.su (open registration, unlimited quota)

- `storage/peertube-peertube-cif-su` | qualifies-with-caveat | evidence reported | binding write-gated | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:14.042Z (live) | stale on 2026-12-10
- url https://peertube.cif.su
- free tier: Unlimited total quota (`user.videoQuota: -1`), 5 GiB per day (`videoQuotaDaily: 5368709120`). Registration open, no approval, no email verification. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: video.file publishes extensions but no size.max; the 8388608-byte size.max belongs to video.image.
- retention: source: [1] | note: unverified: no video retention period is published in the instance config
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
  - probe:https://peertube.cif.su/api/v1/config 2026-11-11: the instance config sets videoQuota -1 and videoQuotaDaily 5368709120, with signup allowed without approval or email verification | capture: sha256:31c3f79cff8627834e41a7d591172859c8febb94624fdaed6885cc0fac010030 | quote: "videoQuota":-1,"videoQuotaDaily":5368709120 ... "signup":{"allowed":true ... "requiresApproval":false,"requiresEmailVerification":false
  - [1] 2026-11-19: the instance config still sets videoQuota -1 and videoQuotaDaily 5368709120 | capture: sha256:89efcf3da41b704947fe2821b0c5618462beef96c9856c0fdef388b798d08cae | quote: "user":{"videoQuota":-1,"videoQuotaDaily":5368709120},"videoChannels":{"maxPerUser":10}
  - [1] 2026-11-19: signup is still allowed without approval or email verification | capture: sha256:89efcf3da41b704947fe2821b0c5618462beef96c9856c0fdef388b798d08cae | quote: "signup":{"allowed":true,"allowedForCurrentIP":true,"minimumAge":16,"requiresApproval":false,"requiresEmailVerification":false}
  - [1] 2026-11-25: the instance config puts the 8388608-byte size.max on video.image and gives video.file only an extensions list | capture: sha256:8f73e9b6a0642573981c0fa9138f730aaada38a32d495f4224d1f3e5e4133b6b | quote: "video":{"image":{"extensions":[".png",".jpg",".jpeg",".webp"],"size":{"max":8388608}},"file":{"extensions":[".webm" ... ".flac",".aac",".m4a",".m4b",".ac3"]}}
  - [1] 2026-11-25: the config confirms no size.max in video.file and the image size.max | capture: sha256:8f73e9b6a0642573981c0fa9138f730aaada38a32d495f4224d1f3e5e4133b6b | quote: "video":{"image":{"extensions":[".png",".jpg",".jpeg",".webp"],"size":{"max":8388608}},"file":{"extensions":[".webm" ... ".flac",".aac",".m4a",".m4b",".ac3"]}}
  - [1] 2026-11-25: the only expiration in the config is for user exports, not for stored videos | capture: sha256:8f73e9b6a0642573981c0fa9138f730aaada38a32d495f4224d1f3e5e4133b6b | quote: "export":{"users":{"enabled":true,"exportExpiration":172800000,"maxUserVideoQuota":107374182400}}
- sources:
  - [1] https://peertube.cif.su/api/v1/config
