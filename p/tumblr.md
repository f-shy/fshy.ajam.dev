# tumblr

> tumblr.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tumblr/ | JSON https://fshy.ajam.dev/api/v1/entity/tumblr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tumblr

- `storage/tumblr` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.930Z (live) | stale on 2026-12-04
- url https://help.tumblr.com/knowledge-base/adding-photos/
- free tier: none reachable: photo posts only, re-encoded and resized; help centre has moved to a new knowledge-base structure and none of the image pages state a byte limit. Legacy API is unmaintained | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: photo posts only, re-encoded and resized; help centre has moved to a new knowledge-base structure and none of the image pages state a byte limit. Legacy API is unmaintained
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: photo posts only, re-encoded and resized; help centre has moved to a new knowledge-base structure and none of the image pages state a byte limit. Legacy API is unmaintained
  - [1] 2026-11-19: Tumblr's help centre still documents photo posts with no byte limit stated | capture: sha256:9a9c47db6ffaaa6d1df4269a812d835fc1bbd5f2ab676c5d5d5427113ebbe1e6 | quote: To add a photo anywhere in any post, click the photo icon:
- sources:
  - [1] https://help.tumblr.com/knowledge-base/adding-photos/
