# zazzle

> zazzle.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zazzle/ | JSON https://fshy.ajam.dev/api/v1/entity/zazzle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zazzle

- `storage/zazzle` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:34.053Z (live) | stale on 2026-12-04
- url https://community.zazzle.com/t/png-file-sizes/13224
- free tier: none reachable: Uploads fail above ~3-4 MB in practice with no error message; 'no limits to the number of images' but each is tiny. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Uploads fail above ~3-4 MB in practice with no error message; 'no limits to the number of images' but each is tiny.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Uploads fail above ~3-4 MB in practice with no error message; 'no limits to the number of images' but each is tiny.
  - [2] 2026-10-21: cited as the basis of the rejection: Uploads fail above ~3-4 MB in practice with no error message; 'no limits to the number of images' but each is tiny.
  - [1] 2026-11-19: the first-party community thread documents upload failures above roughly 3-4 MB | capture: sha256:2d4eefd5857e34300f19df025a2e2fb1dbb48745ff79e0acf3ba364527b37b2f | quote: For months I have been unable to upload a PNG file above 3 - 4MB. Sometimes larger but not always. An error message appears and times out.
- sources:
  - [1] https://community.zazzle.com/t/png-file-sizes/13224
  - [2] https://www.zazzle.co.uk/hc/article/frequently_asked_questions-115000209913
