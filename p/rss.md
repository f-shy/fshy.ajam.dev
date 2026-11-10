# RSS.com

> rss.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rss/ | JSON https://fshy.ajam.dev/api/v1/entity/rss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RSS.com — Free plan

- `storage/rss-com-free-plan` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://rss.com
- free tier: Unlimited. Free plan: 'Unlimited episodes and unlimited audio, with no storage cap', 'no trial and no expiry date', 'Your episodes are never deleted'. Only three stated limits: one podcast per account, 30 days of analytics history, one voicemail. Max file size 2 GB per episode. With unlimited episodes that is unbounded total capacity. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Max file size 2 GB | bytes: 2000000000 | source: [1] | note: not stated
- retention: Unlimited. Free plan: 'Unlimited episodes and unlimited audio, with no storage cap', 'no trial and no expiry date', 'Your episodes are never deleted' | source: [1] | note: not stated
- egress: Free and unmetered. No bandwidth line anywhere in the Free plan or the pricing page; delivery is offloaded to Triton Digital's CDN (rsscom.pdn.tritondigital.com) behind CloudFront. Zero egress pricing to the account holder. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): Max file size 2 GB [1]
- limits note: 2 GB per episode; one podcast per account; card on file; re-encoded to 128 kbps stereo (see reliability_note). API rate limit ~15 consecutive writes then HTTP 429 with no Retry-After header.
- interface detail: rest
- tooling: Official public REST API (api.rss.com/v4, X-Api-Key header, 10 keys/account) that 'create[s] new episodes, upload[s] audio'. But it is gated to the Max plan, NOT Free. On Free the only path is the web UI (no public upload endpoint verified). Third-party native integrations exist (Hindenburg, Auphonic, Zapier) but likewise target paid/API plans.
- composes with: N free accounts x unlimited episodes x 2 GB. Card required 'to verify the account' (never charged) is the only friction, so accounts are not trivially mass-produced the way an email-only signup would be. Also accepts .mkv/.mp4/.flac/.wav/.aiff/.ogg/.aac, so non-audio payloads pass the extension filter.
- reliability: RE-ENCODES. Verified live: enclosure https://content.rss.com/episodes/207227/3249482/diveclub/2026_10_20_...mp3 -> 307 -> https://rsscom.pdn.tritondigital.com/v1/download/... with a signed query string carrying br=128000 and dr=3522 (duration). 56,367,272 bytes / 3522 s = 128,035 bps, i.e. exactly 128 kbps — the original upload is NOT retrievable. Enclosure URL is permanent on content.rss.com but every fetch redirects through a signed token, so the bytes are CDN-served re-encodes, not your file.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Unlimited episodes and unlimited audio, with no storage cap'; 'Your episodes are never deleted'; 'we do not insert our own ads'; one podcast per account
  - [2] 2026-10-21: 'Max file size: 2GB'
  - [3] 2026-10-21: accepts .wav .mp3 .aac .aiff .mp4 .m4a .flac .ogg .mkv
  - withheld 2026-10-21: probe: GET media.rss.com/diveclub/feed.xml -> 200, 499,415 bytes, enclosures on content.rss.com; GET enclosure -L -> 307 -> 302 -> 206, Content-Range bytes 0-2047/56367272, token contains br=128000&dr=3522
  - [4] 2026-10-21: Free $0 '/mo. No trial. No expiration. Always free. Unlimited episodes and downloads'
- sources:
  - [1] https://help.rss.com/en/support/solutions/articles/44002697443-the-free-plan
  - [2] https://help.rss.com/en/support/solutions/articles/44000495445-how-do-i-create-my-first-episode-
  - [3] https://help.rss.com/en/support/solutions/articles/44000493026-which-audio-file-formats-does-rss-com-support-
  - [4] https://rss.com/pricing/
