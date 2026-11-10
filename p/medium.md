# Medium image hosting

> medium.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/medium/ | JSON https://fshy.ajam.dev/api/v1/entity/medium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Medium image hosting

- `storage/medium-image-hosting` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://medium.com
- free tier: 25 MB per image, images only | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free CDN links on miro.medium.com, no hotlink restriction | metered: no
- identity: institution
- interface: unknown
- limits note: 25 MB; JPG/JPEG/GIF/PNG only ('The editor supports images up to 25MB in the .JPG, .JPEG, .GIF, and .PNG formats'); no API at all
- interface detail: wrapper-only
- tooling: no upload API since the 2023 Integration Tokens removal; editor-only. Third-party 'publish to Medium' tooling is dead
- composes with: 25 MB x unlimited images x unlimited stories; but images-only means it is a photo host, not a data store
- reliability: Medium re-encodes and resizes; URLs are stable but content is not byte-exact. No API = hard fail on criterion (c)
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 25 MB per image, images only
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The editor supports images up to 25MB in the .JPG, .JPEG, .GIF, and .PNG formats'
- sources:
  - [1] https://help.medium.com/hc/en-us/articles/215679797-Using-images
