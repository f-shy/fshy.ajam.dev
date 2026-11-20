# Pixiv

> pixiv.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixiv/ | JSON https://fshy.ajam.dev/api/v1/entity/pixiv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pixiv

- `storage/pixiv` | fails-egress | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:39.877Z (live) | stale on 2026-12-04
- url https://www.pixiv.net
- free tier: No published total quota; per-post caps only. Effectively unlimited posts. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free viewing, but images are re-encoded and served via i.pximg.net with a Referer check that blocks hotlinking from other origins. Not a usable direct-link CDN. | metered: no
- identity: email
- interface: unknown
- limits note: Profile images are limited to 5 MB per image; illustration posts can be a maximum of 32 MB; all images in a manga post must be 200 MB or less; profile workspace and design images up to 1 MB. There are no limits on the number of works or posts.
- interface detail: wrapper-only
- tooling: No official public upload API. pixivpy works for read; upload requires session-cookie replay and 2FA-prone flows.
- composes with: Unlimited accounts x unlimited posts x 32 MB. The 32 MB per-illustration cap is generous for an image host.
- reliability: Referer-gated CDN means links are not freely hotlinkable, and re-encode is standard. Fails direct-link permanence.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published total quota; per-post caps only. Effectively unlimited posts.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Profile images are limited to 5 MB per image. Illustration posts can be a maximum of 32 MB.'
  - [2] 2026-11-19: no published total quota; effectively unlimited posts, unchanged | capture: sha256:f3b8c1f7ce79ac53f2d3fdb433780fe4e8b3285b386ea1442343522d870541fb | quote: There are no limits on the number of works you can post or the number of posts a single account can make.
  - [2] 2026-11-19: the help centre states the manga cap is 200 MB, not the 30 MB per post in the old field | capture: sha256:f3b8c1f7ce79ac53f2d3fdb433780fe4e8b3285b386ea1442343522d870541fb | quote: Profile images are limited to 5 MB per image. Illustration posts can be a maximum of 32 MB. All images in a manga post must be 200 MB or less. Images of your profile's workspace and design images can be up to 1 MB. There are no limits on the number of works you can post or the number of posts a single account can make.
- sources:
  - [1] https://www.pixiv.help/hc/en-us/articles/235645687
  - [2] https://www.pixiv.help/hc/en-us/articles/235645687-Are-there-any-limits-on-image-file-size
