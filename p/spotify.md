# Spotify for Creators

> spotify.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spotify/ | JSON https://fshy.ajam.dev/api/v1/entity/spotify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spotify for Creators (formerly Anchor)

- `storage/spotify-for-creators` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://creators.spotify.com
- free tier: Free hosting with no stated numeric cap. Spotify's own episode-publishing doc: 'We don't have a file size limit'. The video doc repeats it: 'Spotify for Creators doesn't have a file size limit'. No episode count, storage or bandwidth cap is published anywhere. Free, no paid tier, ad-revenue share is upside not a paywall. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Second caveat: anchor.fm enclosures are 402/302 chains through anchor.fm/s/<id>/podcast/play/<n>/<urlencoded origin>, so the enclosure URL is a redirector with the object path embedded. Permanent, but the served object is always the transcode. | source: [1] | note: not stated
- egress: Free and unmetered via Spotify's own CDN (d3ctxlq1ktw2nl.cloudfront.net). No egress meter, no per-download charge, no plan upgrade that changes it. | metered: no
- identity: institution
- interface: rest
- limits note: Format allowlist is narrow: audio must be MP3, M4A or WAV, mono or stereo; video MOV/MPG/MP4. Uploads are single-shot HTTP from the browser, so a dropped connection mid-upload fails the episode ('higher chance of failing if your internet connection is interrupted'). There is no resumable/chunked API, which is the real ceiling on file size in practice.
- interface detail: rest
- tooling: No documented public upload API. Content uploads are restricted to web and mobile dashboard interfaces. Read access is available via public podcast RSS feeds (`https://anchor.fm/s/<showid>/podcast/rss`) without authentication.
- composes with: Unlimited shows per Spotify account (the UI has 'Add a new show' with no published cap) x unlimited episodes x no file-size limit. Also accepts video (MP4/MOV/MPG) on the same free tier, so the payload need not be audio at all.
- reliability: RE-ENCODES everything to 128 kbps stereo. Verified live: enclosure for an episode with itunes:duration 00:52:22 declared length=50272965; the staging object at d3ctxlq1ktw2nl.cloudfront.net/staging/2026-9-21/434650861-44100-2-6d67ddd17af0f.mp3 returns 206, Content-Range 0-1023/50272965, and its first 1 KB is a bare MPEG frame with no ID3 header at all. 50,272,965 x 8 / 3142 s = 128,003 bps. Exactly 128 kbps CBR. The '-44100-2-' in the filename is the ingest normaliser's fingerprint (44.1 kHz, 2 channels). Your WAV or 320k MP3 does not survive. Second caveat: anchor.fm enclosures are 402/302 chains through anchor.fm/s/<id>/podcast/play/<n>/<urlencoded origin>, so the enclosure URL is a redirector with the object path embedded. Permanent, but the served object is always the transcode.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'We don't have a file size limit'; 'We support MP3, M4A, and WAV file types. Files will need to be either in mono or stereo'
  - [2] 2026-10-21: 'Spotify for Creators doesn't have a file size limit'; supports MOV, MPG, MP4
  - withheld 2026-10-21: probe: GET anchor.fm/s/7d083a4/podcast/rss -> 200, 5,215,282 bytes, enclosures redirect through anchor.fm/.../play/... to d3ctxlq1ktw2nl.cloudfront.net/staging/
  - withheld 2026-10-21: probe: GET d3ctxlq1ktw2nl.cloudfront.net/staging/2026-9-21/434650861-44100-2-6d67ddd17af0f.mp3 -r 0-1023 -> 206, Content-Range 0-1023/50272965, first frame 0xFFFB9000 = MPEG1 L3 128 kbps 44.1 kHz stereo, no ID3v2 tag
  - [3] 2026-10-21: Oct 2026, 'its own page offers free hosting with "unlimited hosting" ... it states no upload or episode cap'
- sources:
  - [1] https://support.spotify.com/us/creators/article/publishing-audio-episodes/
  - [2] https://support.spotify.com/us/creators/article/publishing-videos/
  - [3] https://toolradar.com/guides/best-free-podcast-hosting
