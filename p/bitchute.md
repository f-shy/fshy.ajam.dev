# BitChute

> bitchute.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitchute/ | JSON https://fshy.ajam.dev/api/v1/entity/bitchute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BitChute

- `storage/bitchute` | fails-quota | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.bitchute.com
- free tier: No published total cap; free-tier per-file upload limit reported around 2 GB, higher for paid members (membership page advertises 'Higher Upload Limits' without a number). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2 GB/file | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; BitChute serves via its own infrastructure and WebTorrent. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB/file [1]
- limits note: ~2 GB/file free. BitChute's own docs deliberately omit the number and upsell membership for 'greater file sizes', which means the free cap is a soft, changeable policy rather than a published quota.
- interface detail: rest
- tooling: Yt-dlp `BitChute` / `BitChuteChannel` extractors (verified present). No upload API. Web form only.
- composes with: Unlimited accounts x ~2 GB. Weak multiplier because the per-file cap is small and there is no API to automate ingestion.
- reliability: Evidence is weak: the official upload page never states a size, and the 2 GB figure comes from a creator video complaining about it. Treat as unverified.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published total cap; free-tier per-file upload limit reported around 2 GB, higher for paid members (membership page advertises 'Higher Upload Limits' without a number).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Members enjoy greater file sizes, resolutions and upload priority' (no free-tier number given)
  - [2] 2026-10-21: creator complaint: 'This 2GB upload limit is extremely frustrating'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors` -> BitChute, BitChuteChannel present
- sources:
  - [1] https://support.bitchute.com/creators/how-to-upload-a-video
  - [2] https://www.bitchute.com/video/pcZ5UUinyByc/
