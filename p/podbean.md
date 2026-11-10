# Podbean

> podbean.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/podbean/ | JSON https://fshy.ajam.dev/api/v1/entity/podbean.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Podbean — Basic Free plan

- `storage/podbean-basic-free-plan` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.podbean.com
- free tier: 5 hours / 500 MB TOTAL, not monthly: 'Total storage: 5 hours (500MB). Note: Storage does not reset monthly.' Help centre adds: 'The total file size should not exceed 500MB' and 'The total length of the file should not exceed 5 hours'. Both accumulate and block further uploads when either is hit. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: file size should not exceed 500MB | bytes: 500000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 100 GB per month on Free ('Monthly bandwidth: 100GB'), unmetered beyond that in the sense of no per-GB charge but the account stalls at the cap. Paid Unlimited Audio ($12/mo) is 'Unmetered bandwidth'. | metered: no | free allowance: 100 GB per month
- identity: country-phone
- interface: rest
- limits:
  - per-object-cap (binding): file size should not exceed 500MB [1]
- limits note: 3 episodes/day; 100 MB single file on Free (3 GB on paid); RSS feed exposes only the most recent 20 episodes on Free; formats on Free are MP3 and M4A only (paid adds ogg/zip/pdf/pptx/docx/xml. Note zip is a paid-plan format, so Free cannot take archives at all).
- interface detail: rest
- tooling: No public upload API on Free (Podbean developer docs exist for read/embed; upload is dashboard). Migration-in by RSS is one click and is explicitly free, which is a heavier hammer than a per-episode upload.
- composes with: 5 hours / 500 MB per free account, 100 GB/mo bandwidth. At ~128 kbps that is ~9 hours of audio; at 500 MB hard cap the file-size ceiling bites first for anything lossless. Genuinely small. Only interesting multiplied across many accounts, and each account needs an email + verification.
- reliability: Likely re-encodes. Verified live: enclosure https://mcdn.podbean.com/mf/web/rhvxkzpmimms9sf5/riverside_....mp3 -> 302 -> 206, Content-Range 0-1023/73948726; declared length 73948726 for a 3081 s episode = 191,988 bps, i.e. exactly 192 kbps CBR, and the ID3 tag names Lavf60.16.1 (ffmpeg) as the encoder. The upload was a 'riverside_..._processed.mp3' (Riverside's own processed export, normally 128 kbps), so 192k suggests Podbean re-encoded upward rather than storing as-is — unverified without an account, but the ffmpeg stamp plus exact CBR strongly implies server-side processing.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 hours / 500 MB TOTAL, not monthly: 'Total storage: 5 hours (500MB). Note: Storage does not reset monthly.' Help centre adds: 'The total file size should not exceed 500MB' and 'The total length of the file should not exceed 5 hours' — both accumulate and block further uploads when either is hit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Total storage: 5 hours (500MB)'; 'Storage does not reset monthly'; 'Monthly bandwidth: 100GB'; 'Maximum of 3 episodes ... per day'; 'Single file size limit: 100MB'; 'Displays up to 20 episodes in the RSS feed'
  - [2] 2026-10-21: 'The total file size should not exceed 500MB'; 'Total file length = actual used length + estimated length < 18000 seconds'
  - [3] 2026-10-21: 'Free plan: mp3, m4a'; 'The maximum allowed single file size: 3GB' (paid)
  - withheld 2026-10-21: probe: GET feed.podbean.com/jmonken/feed.xml -> 200; enclosure mcdn.podbean.com -> 302 -> 206, 73,948,726 bytes for 3081 s = 192 kbps, ID3 TSSE 'Lavf60.16.1'
- sources:
  - [1] https://help.podbean.com/support/solutions/articles/25000019893-basic-free-plan-features
  - [2] https://podbean.freshdesk.com/support/solutions/articles/25000029110-how-to-calculate-upload-space-free-account-upload-limits
  - [3] https://help.podbean.com/support/solutions/articles/25000005097-podbean-supported-file-formats-and-single-file-size-limit
