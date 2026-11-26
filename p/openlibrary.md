# open library

> openlibrary.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openlibrary/ | JSON https://fshy.ajam.dev/api/v1/entity/openlibrary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## open library

- `storage/open-library` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.274Z (live) | stale on 2026-12-04
- url https://openlibrary.org/help/faq/editing
- free tier: none reachable: Not a file store: the only user upload is cover images capped at 30 MB, and bulk book import requires a privileged account via the JSON import API. Records point at Internet Archive items… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Not a file store: the only user upload is cover images capped at 30 MB, and bulk book import requires a privileged account via the JSON import API. Records point at Internet Archive items…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a file store: the only user upload is cover images capped at 30 MB, and bulk book import requires a privileged account via the JSON import API. Records point at Internet Archive items…
  - [2] 2026-10-21: cited as the basis of the rejection: Not a file store: the only user upload is cover images capped at 30 MB, and bulk book import requires a privileged account via the JSON import API. Records point at Internet Archive items ra
  - [1] 2026-11-19: the only user upload is a cover image with a 30 MB limit; the page is about editing bibliographic records | capture: sha256:09708bdeee001f31b1c2159154f7e7f563f265be727dd809cce31a5d46191043 | quote: Size limit for images is 30 MB. ... You can add cover images and author photos to Open Library.
- sources:
  - [1] https://openlibrary.org/help/faq/editing
  - [2] https://docs.openlibrary.org/advanced/data-importing.html
