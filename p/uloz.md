# Uloz.to Disk

> uloz.to | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uloz/ | JSON https://fshy.ajam.dev/api/v1/entity/uloz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uloz.to Disk (ULTRA 25 TB)

- `storage/uloz-to-disk` | fails-quota | evidence reported | binding none | category consumer cloud drive sold in 3/12/25/50 TB blocks
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uloz.to/koupit-disk
- price $1.28/TB/mo at the 25 TB tier ($32) and at the 50 TB tier ($64). at 5 TB: buy the 12 TB tier = $1.33/TB/mo. at 20 TB: buy the 25 TB tier = $1.28/TB/mo. | parsed USD 1.28/TB-mo
- free tier: PREMIUM 3 TB $6.50/mo · MAX 12 TB $16/mo · ULTRA 25 TB $32/mo · ULTIMATE 50 TB $64/mo | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: VERBATIM per-tier transfer allowance: PREMIUM "30 TB for data transfer/month", MAX "150 TB", ULTRA "300 TB", ULTIMATE "600 TB". So egress is ~12x stored capacity per month, resetting monthly. Not unlimited, but 12 full restores of the whole account per month is effectively unmetered for any read pattern the workload generates. | metered: no
- identity: email | detail: email
- interface: rest, webdav, rclone
- limits note: Rclone backend does NOT implement About/`--drive-*` free-space query (docs say the endpoint is not exposed in the API) so `mfs`/quota policies cannot see remaining space. Declare total size manually. No per-file size limit stated on the price page. No S3 API.
- interface detail: Native rclone backend (`ulozto`, added v1.66, Tier 3), REST/resumable upload API, CDN download links
- tooling: Rclone `ulozto:`. First-class, not a WebDAV fallback. Needs an app_token from https://uloz.to/upload-resumable-api-beta.
- composes with: rclone mount or `rclone serve s3`/`serve webdav` in front, then Cloudflare. Single namespace, no chunking needed.
- reliability: Czech provider (Uloz.to/Kramerius) that pivoted from a public file locker to a paid private drive after EU DSM pressure in 2023-24. rclone forum users report no download speed limits and working mounts; Assume the ladder can move.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: PREMIUM 3 TB $6.50/mo · MAX 12 TB $16/mo · ULTRA 25 TB $32/mo · ULTIMATE 50 TB $64/mo
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $1.28/TB/mo at the 25 TB tier ($32) and at the 50 TB tier ($64). at 5 TB: buy the 12 TB tier = $1.33/TB/mo. at 20 TB: buy the 25 TB tier = $1.28/TB/mo.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [3] 2026-10-21: user confirms 200 TB/$64 line and 'no file size restrictions', and 'they even give a discount for yearly payments'
  - [4] 2026-10-21: 
- sources:
  - [1] https://uloz.to/koupit-disk
  - [2] https://rclone.org/ulozto/
  - [3] https://forum.rclone.org/t/unlimited-alternatives-to-google-drive-what-are-the-options/36529?page=78
  - [4] https://uloz.to/
