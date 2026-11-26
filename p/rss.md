# RSS.com

> rss.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rss/ | JSON https://fshy.ajam.dev/api/v1/entity/rss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RSS.com — Free plan

- `storage/rss-com-free-plan` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:19.659Z (live) | stale on 2026-12-10
- url https://rss.com
- free tier: Unlimited episodes and unlimited audio, with no storage cap | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Maximum audio file size: 2 GB. | bytes: 2000000000 | source: [1] | note: Maximum audio file size: 2 GB.
- retention: Your episodes are never deleted | source: [1] | note: Your episodes are never deleted
- egress: Publish with unlimited episodes, audio and downloads. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): Max file size 2 GB [1]
- limits note: 2 GB per episode; one podcast per account; card on file; re-encoded to 128 kbps stereo (see reliability_note). API rate limit ~15 consecutive writes then HTTP 429 with no Retry-After header.
- interface detail: rest
- tooling: Official public REST API (api.rss.com/v4, X-Api-Key header, 10 keys/account) that 'create[s] new episodes, upload[s] audio'. But it is gated to the Max plan, NOT Free. On Free the only path is the web UI (no public upload endpoint verified). Third-party native integrations exist (Hindenburg, Auphonic, Zapier) but likewise target paid/API plans.
- composes with: N free accounts x unlimited episodes x 2 GB. Card required 'to verify the account' (never charged) is the only friction, so accounts are not trivially mass-produced the way an email-only signup would be. Also accepts .mkv/.mp4/.flac/.wav/.aiff/.ogg/.aac, so non-audio payloads pass the extension filter.
- reliability: RE-ENCODES. Verified live: enclosure https://content.rss.com/episodes/207227/3249482/diveclub/2026_10_20_...mp3 -> 307 -> https://rsscom.pdn.tritondigital.com/v1/download/... with a signed query string carrying br=128000 and dr=3522 (duration). 56,367,272 bytes / 3522 s = 128,035 bps, i.e. exactly 128 kbps — the original upload is NOT retrievable. Enclosure URL is permanent on content.rss.com but every fetch redirects through a signed token, so the bytes are CDN-served re-encodes, not your file.
- notes: Unlimited. Free plan: 'Unlimited episodes and unlimited audio, with no storage cap', 'no trial and no expiry date', 'Your episodes are never deleted'. Only three stated limits: one podcast per account, 30 days of analytics history, one voicemail. Max file size 2 GB per episode. With unlimited episodes that is unbounded total capacity.
- evidence note: the free-plan article states unlimited episodes and audio with no storage cap
- evidence:
  - [1] 2026-10-21: 'Unlimited episodes and unlimited audio, with no storage cap'; 'Your episodes are never deleted'; 'we do not insert our own ads'; one podcast per account
  - [2] 2026-10-21: 'Max file size: 2GB'
  - [3] 2026-10-21: accepts .wav .mp3 .aac .aiff .mp4 .m4a .flac .ogg .mkv
  - withheld 2026-10-21: probe: GET media.rss.com/diveclub/feed.xml -> 200, 499,415 bytes, enclosures on content.rss.com; GET enclosure -L -> 307 -> 302 -> 206, Content-Range bytes 0-2047/56367272, token contains br=128000&dr=3522
  - [4] 2026-10-21: Free $0 '/mo. No trial. No expiration. Always free. Unlimited episodes and downloads'
  - [1] 2026-11-09: the free-plan article states unlimited episodes and audio with no storage cap | capture: sha256:deb08cb2100a1e7b945bcfaffb063c4a8db88db12104da21fc1a7c7b94478057 | quote: Unlimited episodes and unlimited audio, with no storage cap
  - [1] 2026-11-09: the free-plan article states that episodes are never deleted | capture: sha256:deb08cb2100a1e7b945bcfaffb063c4a8db88db12104da21fc1a7c7b94478057 | quote: Your episodes are never deleted
  - [2] 2026-11-09: the first-episode article states a 2 GB maximum audio file size | capture: sha256:587b3ebfd46540cd9118dca6bc2188f938809c4a2097dee3554d0aab1745be99 | quote: Maximum audio file size: 2 GB.
  - [2] 2026-11-25: the first-episode article states a 2 GB maximum audio file size | capture: sha256:587b3ebfd46540cd9118dca6bc2188f938809c4a2097dee3554d0aab1745be99 | quote: Maximum audio file size: 2 GB.
  - [1] 2026-11-25: the free-plan article states that episodes are not deleted | capture: sha256:deb08cb2100a1e7b945bcfaffb063c4a8db88db12104da21fc1a7c7b94478057 | quote: Your episodes are never deleted
  - [4] 2026-11-25: the pricing page states unlimited downloads for the free plan | capture: sha256:14537f1acdb9aac64f25df2ee591e1333ab7cb87a39ffcab6491876bc49e95cb | quote: Publish with unlimited episodes, audio and downloads.
  - [1] 2026-11-25: the free-plan article states unlimited episodes and audio with no storage cap | capture: sha256:deb08cb2100a1e7b945bcfaffb063c4a8db88db12104da21fc1a7c7b94478057 | quote: Unlimited episodes and unlimited audio, with no storage cap
- sources:
  - [1] https://help.rss.com/en/support/solutions/articles/44002697443-the-free-plan
  - [2] https://help.rss.com/en/support/solutions/articles/44000495445-how-do-i-create-my-first-episode-
  - [3] https://help.rss.com/en/support/solutions/articles/44000493026-which-audio-file-formats-does-rss-com-support-
  - [4] https://rss.com/pricing/
