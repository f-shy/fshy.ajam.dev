# quora

> quora.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quora/ | JSON https://fshy.ajam.dev/api/v1/entity/quora.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## quora

- `storage/quora` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.012Z (live) | stale on 2026-12-04
- url https://www.quora.com/about/tos
- free tier: not stated: https://www.quora.com/about/tos prints no storage amount, per-file cap or period; users can add posts, text, photos, videos, links and other files to share with other users | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: no quota, per-file cap or retention period for user content is printed on the cited page
- per-object cap: not stated on https://www.quora.com/about/tos | source: [1] | note: not applicable
- retention: not stated on https://www.quora.com/about/tos | source: [1]
- egress: not stated on https://www.quora.com/about/tos | metered: no
- identity: email
- interface: browser
- interface detail: Website and applications; no public storage API is documented on the cited page.
- tooling: not documented
- composes with: Not stated on https://www.quora.com/about/tos; content is shared inside Quora rather than exposed as a store.
- reliability: No attachment/file hosting at all.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: the terms describe user content including photos, videos and other files, and print no storage amount | capture: sha256:40427a553233ba0c02d2da7817bca29381b4359ba2c16784a61022844ffaba2e | quote: Quora enables you to add posts, text, photos, videos, links, and other files and information to share with other users of Quora.
  - [1] 2026-11-19: the terms still describe user content as posts, text, photos, videos and files and print no storage amount | capture: sha256:f0d6975750b419358485a70b943cef19dfd561945abf45ff6124c6e95be115d7 | quote: Quora enables you to add posts, text, photos, videos, links, and other files and information to share with other users of Quora.
  - [1] 2026-11-19: the interface is a website and applications with no documented storage API | capture: sha256:f0d6975750b419358485a70b943cef19dfd561945abf45ff6124c6e95be115d7 | quote: empowering people to learn from others and better understand the world through our websites and applications
- sources:
  - [1] https://www.quora.com/about/tos
