# ImgBB

> imgbb.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imgbb/ | JSON https://fshy.ajam.dev/api/v1/entity/imgbb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ImgBB

- `storage/imgbb` | qualifies | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://imgbb.com
- free tier: Unlimited/indefinite storage for free accounts; no published total-byte cap. Third-party trackers consistently report 'unlimited storage, permanent hosting'. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Unlimited/indefinite storage for free accounts; no published total-byte cap | source: [1] | note: not stated
- egress: Free, unmetered direct links on i.ibb.co. No bandwidth quota published, no hotlink restriction. | metered: no
- identity: institution
- interface: rest
- limits note: 32 MB/image via API (binary, base64, or image URL). Optional 'expiration' 60-15,552,000 s. The anonymous upload endpoint needs a session token, so automation must use the API-key path.
- interface detail: rest
- tooling: Official API v1 at api.imgbb.com. POST multipart or GET with base64/URL, single 'key' param. ShareX, PicGo and Flameshot all ship ImgBB destinations.
- composes with: Unlimited free accounts, each with its own API key. Each upload returns a delete_url, so per-file turnover is scriptable.
- reliability: No re-compression documented and large JPEGs survive byte-for-byte. No inactivity deletion. Long Cache-Control (10y) means deletions propagate slowly.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'image (required) A binary file, base64 data, or an image URL (up to 32 MB)'
  - [1] 2026-10-21: '32 MB limit. Direct image links, BBCode, and HTML thumbnails.'
  - withheld 2026-10-21: probe: HEAD i.ibb.co/20z1mhT/0004-016.jpg -> 200, Content-Length 125707, image/jpeg — matches the 125.7 KB the site records for the original, i.e. no re-encode; Expires 2037
- sources:
  - [1] https://imgbb.com/
  - [2] https://api.imgbb.com/
