# Pixiv

> pixiv.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixiv/ | JSON https://fshy.ajam.dev/api/v1/entity/pixiv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pixiv

- `storage/pixiv` | fails-egress | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.pixiv.net
- free tier: No published total quota; per-post caps only. Effectively unlimited posts. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free viewing, but images are re-encoded and served via i.pximg.net with a Referer check that blocks hotlinking from other origins. Not a usable direct-link CDN. | metered: no
- identity: email
- interface: unknown
- limits note: 32 MB per illustration post, 5 MB profile image; manga 32 MB/image and 30 MB per post total. Region-locked (JP login often required).
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
- sources:
  - [1] https://www.pixiv.help/hc/en-us/articles/235645687
  - [2] https://www.pixiv.help/hc/en-us/articles/235645687-Are-there-any-limits-on-image-file-size
