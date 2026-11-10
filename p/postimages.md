# Postimages

> postimages.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/postimages/ | JSON https://fshy.ajam.dev/api/v1/entity/postimages.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Postimages (postimages.org / postimg.cc)

- `storage/postimages` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://postimages.org
- free tier: No storage cap stated: 'we do not impose strict limits on our users... Some users store and share tens of thousands of images'. Explicitly 'you will never have to worry about your images being removed due to inactivity'. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 32 MB/file | bytes: 32000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, unmetered hotlinking, CDN-served, no published bandwidth tier. Only soft pressure: if you use 'a really large amount' of disk/bandwidth without linking back they reserve the right to contact you. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 32 MB/file [1]
- limits note: 32 MB/file and 10,000x10,000 px for free and anonymous; Premium 96 MB / 65,535 px. EXIF preserved by default (evidence of no re-encode). Programmatic upload only via the token API, not the web endpoint.
- interface detail: rest
- tooling: Documented token API. Their own upload endpoint says 'Please use the official API: https://api.postimages.org/'. ShareX ships a Postimages destination keyed on an account API key from the profile page; npm 'postimages-upload'.
- composes with: Unlimited free accounts, each with unlimited images. Gallery per account, 1,000 images per batch (batch size, not a cap).
- reliability: Web endpoint blocks scripted uploads with 403 'Automated uploads are not allowed via the website'. Must use the token API. Otherwise durable, no inactivity deletion.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'limited to a file size of 32Mb and maximum dimensions of 10000 x 10000 pixels'; 'unlimited number of images per post... never have to worry about your images being removed due to inactivity'; 'By default, Postimages keeps the original EXIF data embedded'
  - [2] 2026-10-21: probe: POST postimages.org/json/rr with anonymous token -> 403 {"error":{"message":"Automated uploads are not allowed via the website. Please use the official API: ","code":403}}
  - withheld 2026-10-21: probe: HEAD api.postimages.org -> 301 nginx (endpoint exists; no human-readable docs page published)
- sources:
  - [1] https://postimages.org/faq
  - [2] https://api.postimages.org/
