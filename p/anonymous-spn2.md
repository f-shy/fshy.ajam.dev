# anonymous spn2

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonymous-spn2/ | JSON https://fshy.ajam.dev/api/v1/entity/anonymous-spn2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## anonymous spn2 (no account) capture

- `storage/anonymous-spn2-capture` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:54.755Z (live) | stale on 2026-12-04
- url https://web.archive.org/save
- free tier: live endpoint now refuses all anonymous writes with 401 and the GET form 429s. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Internet Archive Save Page Now page | source: [1] | note: not applicable
- retention: not stated on the Internet Archive Save Page Now page | source: [1]
- egress: not stated on the Internet Archive Save Page Now page | metered: no
- identity: email
- interface: browser
- interface detail: A Save Page Now browser form for capturing web pages; no programmatic storage interface is described.
- tooling: not documented
- composes with: Captures a web page into the Internet Archive; not stated on the Save Page Now page as chaining to other storage services.
- reliability: The Save Page Now GET form is served on the first-party page as of 2026-11-19. The former claim that anonymous writes and the GET form returned HTTP errors, and an advertised daily anonymous capture allowance, are not shown on the live first-party page and were not reproduced: the GET form rendered, and an anonymous write was not attempted (unverified: anonymous write not re-tested).
- notes: Live endpoint now refuses all anonymous writes with 401 and the GET form 429s.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Live endpoint now refuses all anonymous writes with 401 and the GET form 429s.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: live endpoint now refuses all anonymous writes with 401 and the GET form 429s.
  - [1] 2026-11-19: the Save Page Now GET form is still served on the first-party page | capture: sha256:1a5e715019e6ba789c3d37a1291a97604ead62d23c37719b8eccf08975ec68e5 | quote: Capture a web page as it appears now for use as a trusted citation in the future.
  - probe:https://web.archive.org/save 2026-11-19: a probe of the Save Page Now URL returned HTTP 200 with no challenge detected on 2026-11-19 | capture: sha256:f552b6e76a3abaf5f6d57a079fb5105523bb46780da1b3f0021a4417ce4c78d1 | quote: "status": 200
- sources:
  - [1] https://web.archive.org/save
