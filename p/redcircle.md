# RedCircle

> redcircle.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/redcircle/ | JSON https://fshy.ajam.dev/api/v1/entity/redcircle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RedCircle — Core (free) plan

- `storage/redcircle-core-plan` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://redcircle.com
- free tier: Unlimited. Core is 'our entirely free option ... host one podcast with unlimited storage, bandwidth, episodes, and downloads'. Pricing page comparison table confirms storage / bandwidth / episodes / downloads all 'Unlimited' on Core. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unlimited / unmetered. The plan table lists 'bandwidth: Unlimited' and 'Number of Downloads: Unlimited'. No egress pricing exists at any tier. | metered: no
- identity: country-phone
- interface: unknown
- limits note: 200 MB per audio file on Core (250 MB on Pro/Enterprise); 10 GB for video, but video upload is Pro/Enterprise only. 1 podcast on Core. Feed refreshes periodically, so a new episode is not instantly in the RSS.
- interface detail: wrapper-only
- tooling: No public upload API found (search surfaced only third-party 'integration' marketing pages). Web dashboard only for uploads; the RSS feed itself is a plain GET, so read-side automation is trivial. Public feed format: https://feeds.redcircle.com/<show-uuid> (documented in RedCircle's own Apple distribution guide).
- composes with: 1 podcast per free account, but unlimited episodes per podcast and unlimited storage. So capacity is per-account, not per-episode: N accounts x unbounded. 200 MB/episode is the only multiplier, so large volumes need many episodes rather than few large files (200 MB x unlimited episodes is still unbounded).
- reliability: Serves a dynamic-ad-inserted stream, not your file. Verified live: feed enclosure https://audio3.redcircle.com/episodes/de9e4cc6-.../stream.mp3 -> 302 to media.redcircle.com -> 206, Content-Range 0-1023/60125855, while the feed declared length=60122174 — an 3,681-byte difference, i.e. the served object differs from the declared one (insertion points get stitched in). Audio is 128 kbps stereo joint. RedCircle's own help says 'Episodes are downloaded with Insertion Points, so you may download ads and other custom audio' — confirming the delivered bytes are not the uploaded bytes.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'this is our totally free option. With this plan, you're able to host one podcast with unlimited storage, bandwidth, episodes, and downloads'
  - [2] 2026-10-21: Core column: storage Unlimited, bandwidth Unlimited, Number of Episodes Unlimited, Number of Downloads Unlimited
  - withheld 2026-10-21: probe: GET feeds.redcircle.com/511adffa-88d0-4cb5-b77b-06edc73ff3fa -> 200, 763,958 bytes; enclosure audio3.redcircle.com/.../stream.mp3 length=60122174
  - withheld 2026-10-21: probe: GET that enclosure -L -> 206, Content-Range 0-1023/60125855 (spooled size ≠ declared size), ID3v2 present, MPEG1 Layer III 128 kbps 44.1 kHz joint stereo
  - [3] 2026-10-21: 'the maximum audio file size is 200MB (250MB if you're on our Pro or Enterprise plans)'
- sources:
  - [1] https://support.redcircle.com/articles/7581935770-redcircle-account-plans
  - [2] https://redcircle.com/pricing
  - [3] https://support.redcircle.com/articles/1629272190-uploading-an-episode
