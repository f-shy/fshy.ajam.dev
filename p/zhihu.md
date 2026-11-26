# Zhihu image hosting

> zhihu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zhihu/ | JSON https://fshy.ajam.dev/api/v1/entity/zhihu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zhihu image hosting

- `storage/zhihu-image-hosting` | fails-quota | evidence inferred | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://zhihu.com
- free tier: no vendor page found; user reports cluster at 2-10 MB per image | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free CDN (pic1.zhimg.com etc.) but with Referer checks on hotlink | metered: no
- identity: email
- interface: unknown
- limits note: unverified; multiple users report failures under 2 MB and 10 MB, suggesting a small, elastic cap
- interface detail: wrapper-only
- tooling: no public API; zhihu-oauth projects are abandoned. Web editor only
- composes with: Unverified. Per-image cap too small and per-account behaviour too opaque to model.
- reliability: no usable vendor documentation exists for the cap; images are stripped from answers that get moderated. Treat as unusable
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no vendor page found; user reports cluster at 2-10 MB per image
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: user reports: 'a picture that is less than 10MB can't be uploaded'; 'ensuring it is less than 2MB'
  - withheld 2026-10-21: 
- sources:
  - [1] https://www.zhihu.com/en/answer/1983511455
