# Castbox Creator Studio

> castbox.fm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/castbox/ | JSON https://fshy.ajam.dev/api/v1/entity/castbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Castbox Creator Studio

- `storage/castbox-creator-studio` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://castbox.fm
- free tier: 'There is no limit on uploading storage (total) for a channel.' Per-file cap 400 MB, from a help page last updated 7 years ago ('Updated: 7 years ago'). The 400 MB figure is stale and should be treated as unverified. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 400 MB per file | bytes: 400000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published; no egress charge surfaced in any Castbox creator doc. | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 400 MB per file [1]
- limits note: 400 MB per file (2019-era doc); accepted WAV/MP3/MP4/AAC/M4A. No retention or bandwidth figure published anywhere.
- interface detail: wrapper-only
- tooling: Creator Studio web dashboard only; no API. Castbox is primarily a player, so its hosting is a sideline.
- composes with: Unlimited channels x unlimited episodes, if the 'no limit on total storage' line still holds. Multiple accounts are email-only.
- reliability: Unverifiable. The hosting doc carries no date beyond 'Page updated' and the file-type doc says 'Updated: 7 years ago'.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'There is no limit on uploading storage (total) for a channel.'
  - [2] 2026-10-21: 'the maximum file size is 400M'; 'Updated: 7 years ago'
  - withheld 2026-10-21: probe: GET castbox.fm/rss/3678725 -> 302 -> castbox.fm/404.html (no public enclosure path found)
- sources:
  - [1] https://sites.google.com/castbox.fm/castbox-help-center/podcasters/getting-started/2-start-a-podcast-hosted-on-castbox-for-free
  - [2] https://helpcenter.castbox.fm/portal/en/kb/articles/file-types-when-uploading
