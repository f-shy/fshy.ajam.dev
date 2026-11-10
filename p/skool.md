# Skool native video hosting

> skool.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/skool/ | JSON https://fshy.ajam.dev/api/v1/entity/skool.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Skool native video hosting

- `storage/skool-native-video-hosting` | trial-only | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.skool.com
- free tier: 30 GB per uploaded video file, with no documented community-level storage cap. Course/lesson file attachments are separate and much smaller (images 413 above ~10 MB). | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 30 GB per upload | bytes: 30000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free/unmetered playback from Skool's CDN. Private files on `assets.skool.com` return 403 and get signed URLs minted on download, so the read path is not a public CDN. | metered: no
- identity: card
- interface: unknown
- limits:
  - per-object-cap (binding): 30 GB per upload [1]
  - per-object-cap (binding): 30 GB/file [1]
- limits note: 30 GB per video file; ~10 MB per image; uploads only through the web/mobile UI; private assets require on-demand signed URLs.
- interface detail: wrapper-only
- tooling: No official API. A community reverse-engineering effort exists (skool-api.cristiantala.com) using playwright + Google's Browserless actor with cookie auth; the `files:uploadImage` actor is documented empirically, not by Skool.
- composes with: N free communities? No. Skool is $9/mo hobby or $99/mo pro after a 14-day trial, so the multiplier is paid seats, which fails the 'free' premise.
- reliability: Paid commercial platform without programmatic API upload endpoints. Supports up to 30 GB per uploaded video file.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 30 GB per uploaded video file, with no documented community-level storage cap. Course/lesson file attachments are separate and much smaller (images 413 above ~10 MB).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The file size limit is 30GB'
  - [2] 2026-10-21: 'Skool accepts up to ~10 MB per image (empirically — not documented). Above that, the upload returns a 413.'; 'assets.skool.com/... URLs for private files return 403'
- sources:
  - [1] https://www.skool.com/educate/native-video-hosting-is-here
  - [2] https://skool-api.cristiantala.com/docs/files/
