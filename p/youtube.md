# YouTube

> youtube.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/youtube/ | JSON https://fshy.ajam.dev/api/v1/entity/youtube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YouTube (unlisted) — with DCT/fountain-coded payload

- `storage/youtube-with-dct-fountain-coded-payload` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.youtube.com
- free tier: No total storage cap. Per-upload max 256 GB or 12 hours, whichever is less. Unverified accounts are limited to 15-minute videos; phone verification lifts that. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered. Playback and yt-dlp retrieval are served from Google's CDN at no cost; there is no egress meter on the account. | metered: no
- identity: institution
- interface: rest
- limits:
  - request-rate: 6 uploads/day [1]
  - request-rate: 1600 quota units each against a 10,000/day [1]
  - per-ip-shaping (binding): 47 Mbps [1]
- limits note: A daily upload-count cap exists but Google does not publish the number; its own tier page only distinguishes 'limited daily limit' (unverified) from 'higher daily limit' (phone-verified). The Data API v3 path is capped near 6 uploads/day (~1600 quota units each against a 10,000/day budget). 12-hour duration ceiling means a 256 GB file must average 47 Mbps to be reachable.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: yt-dlp (youtube extractor, verified present in `yt-dlp --list-extractors`; 1752 extractors total). Binary-in-video: freddiev4/yts3 (FFV1/DCT + fountain codes, 2 stars, pushed 2026-02), KKarmugil/Infinite_Storage_Glitch (188 stars, Python ISG port), karaketir16/file2video (70 stars).
- composes with: Unlimited files per channel x unlimited free Google accounts. Each upload is independently 256 GB-capped, so capacity = N accounts x M videos x 256 GB. Upload throughput, not quota, is the binding constraint.
- reliability: From a datacenter IP, yt-dlp hit `Sign in to confirm you're not a bot` on 2 of 3 probe videos and HTTP 429 on the watch page. Retrieval reliably needs cookies or a residential egress. Data does not vanish, but the account can be terminated and the whole channel with it.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'The maximum file size you can upload is 256 GB or 12 hours, whichever is less'; 15-minute default for unverified accounts
  - [2] 2026-10-21: 'There's a limit to how many videos a channel can upload each day'; no number given
  - [3] 2026-10-21: probe: `yt-dlp -F -> 720p/1080p/1440p/2160p renditions only (av01, vp9, avc1), no original stream
  - [4] 2026-10-21: 'converts any file into an FFV1/MKV lossless video ... embedding data into 8x8 DCT blocks', fountain codes 'for surviving re-encoding'
- sources:
  - [1] https://support.google.com/youtube/answer/71673
  - [2] https://support.google.com/youtube/answer/57407
  - [3] https://www.youtube.com/watch?v=dQw4w9WgXcQ`
  - [4] https://github.com/freddiev4/yts3
