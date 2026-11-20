# krakenfiles.com

> krakencloud.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/krakencloud/ | JSON https://fshy.ajam.dev/api/v1/entity/krakencloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## krakenfiles.com

- `storage/krakenfiles-com` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:07.478Z (live) | stale on 2026-12-04
- url https://hs6.krakencloud.net/_uploader/gallery/upload
- free tier: none reachable: Upload backend is unreachable: the uploader posts to https://hs6.krakencloud.net/_uploader/gallery/upload, which fails to connect on :443 (21 s). The front page returns a 1 GB limit banner, | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Upload backend is unreachable: the uploader posts to https://hs6.krakencloud.net/_uploader/gallery/upload, which fails to connect on :443 (21 s). The front page returns a 1 GB limit banner,
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Upload backend is unreachable: the uploader posts to https://hs6.krakencloud.net/_uploader/gallery/upload, which fails to connect on:443 (21 s). The front page returns a 1 GB limit banner
  - [2] 2026-10-21: cited as the basis of the rejection: Upload backend is unreachable: the uploader posts to https://hs6.krakencloud.net/_uploader/gallery/upload, which fails to connect on:443 (21 s). The front page returns a 1 GB limit banner
  - probe:https://hs6.krakencloud.net/_uploader/gallery/upload 2026-11-19: the upload backend host is unreachable on 2026-11-19 | capture: sha256:2822a165c097930b357885091e41f4814979dda7f38c317442bf405853b670de | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 502 upstream unreachable>"
  - [3] 2026-11-19: the first-party front page states a 5GB per-file cap for premium users | capture: sha256:4c4e1d905916cb80272cd66cc60fcb3481771259f567e4d0b5e7a6c4845b110e | quote: Upload up to 5GB (per file) for premium users
- sources:
  - [1] https://hs6.krakencloud.net/_uploader/gallery/upload
  - [2] https://krakenfiles.com/upload
  - [3] https://krakenfiles.com/
