# Imgur

> imgur.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imgur/ | JSON https://fshy.ajam.dev/api/v1/entity/imgur.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## i.stack.imgur.com (legacy se host)

- `storage/i-stack-imgur-com` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://i.stack.imgur.com/mHJfs.jpg
- free tier: none reachable: still 302-redirects to i.sstatic.net but is no longer an upload target; agents that test the old host will mis-read a redirect as success | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: still 302-redirects to i.sstatic.net but is no longer an upload target; agents that test the old host will mis-read a redirect as success
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: still 302-redirects to i.sstatic.net but is no longer an upload target; agents that test the old host will mis-read a redirect as success
- sources:
  - [1] https://i.stack.imgur.com/mHJfs.jpg

## Imgur (anonymous + account uploads)

- `storage/imgur` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://imgur.com
- free tier: 50 MB per non-animated image, 200 MB per GIF/video; 'no upload limit per account'; 50 images/hour | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, direct i.imgur.com links, Fastly/Cloudflare CDN, no per-IP shaping observed; hotlinking is the product | metered: no
- identity: anonymous
- interface: rest, rclone, cli
- limits note: 50 images/hour; PNGs over 5 MB get converted to JPEG (destroys byte-exactness); images over 1 MB anonymous / 5 MB account are lossily recompressed; 'it's not possible to replace an image while keeping the same URL'
- interface detail: rest
- tooling: documented Imgur API v3 with Client-ID-only anonymous upload (POST /3/image); many CLI wrappers (imgur-screenshot, sharex, rclone has no backend but community scripts do)
- composes with: 50 images/hour x 50 MB = 2.5 GB/hour per IP, x multiple Client-IDs x multiple accounts. ~1.2 TB/month/IP at the hourly cap if you actually sustain it
- reliability: the big one: Imgur has purged anonymous/unviewed content in past cleanup rounds and the 50-per-hour cap is enforced per IP; recompression means you cannot treat it as a byte store at all
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 MB per non-animated image, 200 MB per GIF/video; 'no upload limit per account'; 50 images/hour
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '50MB' non-animated, '200MB' gif/video, 'There is an upload limit of 50 images per hour. There is no upload limit per account'
  - withheld 2026-10-21: same page — 'PNG files over 5MB will be converted to JPEGs'
- sources:
  - [1] https://help.imgur.com/hc/en-us/articles/26511665959579-What-files-can-I-upload-Is-there-a-size-limit

## imgur as byte-exact storage

- `storage/imgur-as-byte-exact-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.imgur.com/hc/en-us/articles/26511665959579-What-files-can-I-upload-Is-there-a-size-limit
- free tier: none reachable: PNG >5 MB converted to JPEG, >1 MB anonymous images lossily compressed, 50 uploads/hour. Good CDN, useless for data | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: PNG >5 MB converted to JPEG, >1 MB anonymous images lossily compressed, 50 uploads/hour. Good CDN, useless for data
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: PNG >5 MB converted to JPEG, >1 MB anonymous images lossily compressed, 50 uploads/hour. Good CDN, useless for data
- sources:
  - [1] https://help.imgur.com/hc/en-us/articles/26511665959579-What-files-can-I-upload-Is-there-a-size-limit
