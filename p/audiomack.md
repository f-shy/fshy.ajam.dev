# Audiomack

> audiomack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/audiomack/ | JSON https://fshy.ajam.dev/api/v1/entity/audiomack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Audiomack

- `storage/audiomack` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://audiomack.com
- free tier: Unlimited uploads, free forever: 'Audiomack is a FREE, limitless music sharing and discovery platform'; 'Whether you have 1 song or 1,000, Audiomack lets you host it all for free. No premium creator accounts ever!'. Per-file cap 250 MB (third-party spec sheet, not vendor-confirmed). | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MB per file | bytes: 250000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free streaming, no egress charge, no paid tier to buy. | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 250 MB per file [1]
- limits note: 250 MB per file (medium confidence. Audiohostings.com's October 2026 table, not Audiomack's own page); no published storage or bandwidth total.
- interface detail: wrapper-only
- tooling: Creator dashboard and mobile app; no public upload API found.
- composes with: Unlimited tracks per free artist account x N accounts; 250 MB/track means volume needs many tracks, not large files.
- reliability: Streaming-only platform: no original-file download path was found, so the payload is retrievable only as a transcode or not at all. The 'limitless' claim is about upload count, not about giving you a URL to your bytes.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Audiomack is a FREE, limitless music sharing and discovery platform'; 'No Premium Creator Accounts - Completely Free'; 'Whether you have 1 song or 1,000, Audiomack lets you host it all for free'
  - [2] 2026-10-21: Oct 2026 table: Audiomack max file size 250 MB, registration required (third-party)
- sources:
  - [1] https://creators.audiomack.com/about
  - [2] https://www.audiohostings.com/
