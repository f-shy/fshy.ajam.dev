# c-v.sh

> c-v.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/c-v/ | JSON https://fshy.ajam.dev/api/v1/entity/c-v.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## c-v.sh

- `storage/c-v-sh` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.018Z (live) | stale on 2026-12-04
- url https://c-v.sh/?token=
- free tier: 512 MiB maximum per file; files expire 5 to 365 days by size. The first-party usage page documents curl -F upload to https://c-v.sh/?token= and a secret token requested from audron | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: 512 MiB maximum per file with size-dependent expiry of 5 to 365 days; a secret token is requested from audron and uploads use curl -F with that token
- notes: 512 MiB maximum per file with size-dependent expiry of 5 to 365 days; upload via curl -F to https://c-v.sh/?token= with a secret token requested from audron
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Advertised as a 'pastor' 512 MiB temporary host, but the documented upload form requires an Authorization header ('Header of type `authorization` was missing' -> 400) and PUT to /<name>…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Advertised as a 'pastor' 512 MiB temporary host, but the documented upload form requires an Authorization header ('Header of type `authorization` was missing' -> 400) and PUT to /<name>…
  - [1] 2026-11-19: the first-party usage page documents a 512 MiB maximum size and 5 to 365 day expiry | capture: sha256:1be1529a9c20004e80cb7846746599add741e52bc6cb80f8376188fbbb063585 | quote: Where min_age is 5 days, max_age is 365 days, and the maximum size is 512MiB.
  - [1] 2026-11-19: the first-party usage page documents a 512 MiB cap and size-dependent expiry | capture: sha256:1be1529a9c20004e80cb7846746599add741e52bc6cb80f8376188fbbb063585 | quote: Where min_age is 5 days, max_age is 365 days, and the maximum size is 512MiB.
  - [1] 2026-11-19: the first-party usage page documents a curl -F multipart upload to the /?token= endpoint | capture: sha256:1be1529a9c20004e80cb7846746599add741e52bc6cb80f8376188fbbb063585 | quote: $ curl -F a=@vim.png b=@vim2.png https://c-v.sh/?token=
  - [1] 2026-11-19: the first-party usage page was re-read and its 512 MiB cap and expiry confirmed | capture: sha256:1be1529a9c20004e80cb7846746599add741e52bc6cb80f8376188fbbb063585 | quote: Where min_age is 5 days, max_age is 365 days, and the maximum size is 512MiB.
- sources:
  - [1] https://c-v.sh/?token=
