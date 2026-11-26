# aispace.sh agent file drop

> aispace.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aispace/ | JSON https://fshy.ajam.dev/api/v1/entity/aispace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## aispace.sh agent file drop

- `storage/aispace-sh-agent-file-drop` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.938Z (live) | stale on 2026-12-04
- url https://aispace.sh/
- free tier: none reachable: Free tier is 10 MB of storage and 100 uploads/month, max 7-day file lifetime, explicitly 'nothing lingers'. Off by 5 orders of magnitude. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 5 MB max file on Free, 100 MB max file on Pro. | source: [1] | note: not applicable
- retention: Files last at most 7 days on free, 30 on Pro, and a link can never outlive the file it points to. Optional download caps. Nothing lingers; nothing to clean up. | source: [1]
- egress: Bandwidth is included — R2 egress is free. | metered: no
- identity: email
- interface: cli, rest
- interface detail: A CLI binary and an HTTP API: a key with a byte budget uploads a file and returns an expiring link.
- tooling: not documented
- composes with: A report should not stay trapped in the chat that created it. One LLM session or agent can upload it; another can pick it up later and keep going.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free tier is 10 MB of storage and 100 uploads/month, max 7-day file lifetime, explicitly 'nothing lingers'. Off by 5 orders of magnitude.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free tier is 10 MB of storage and 100 uploads/month, max 7-day file lifetime, explicitly 'nothing lingers'. Off by 5 orders of magnitude.
  - [1] 2026-11-19: the free allowance is 10 MB and 100 uploads per month | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: The account is created for you — 10 MB and 100 uploads a month, free. Sign in →
  - [1] 2026-11-19: the first-party page documents an HTTP API and a CLI binary | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: One key, one binary, plain HTTP.
  - [1] 2026-11-19: the first-party page documents posting to an API as an alternative to the CLI | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: Or skip the CLI entirely and post to the API.
  - [1] 2026-11-19: the first-party page states a 7-day free and 30-day Pro file lifetime | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: Files last at most 7 days on free, 30 on Pro, and a link can never outlive the file it points to.
  - [1] 2026-11-19: the first-party Free-plan list states a 5 MB maximum file size | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: 5 MB max file
  - [1] 2026-11-19: the first-party page describes passing files between agents via expiring links | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: A report should not stay trapped in the chat that created it. One LLM session or agent can upload it; another can pick it up later and keep going.
  - [1] 2026-11-19: the first-party page states that egress is free | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: Bandwidth is included — R2 egress is free.
  - [1] 2026-11-19: the first-party page confirms sign-in and agent key/link control | capture: sha256:6fd3897e9506a3e5e0f697c991fd98e501bb331963232c25b55cf04149c1dafc | quote: You sign in, see every file and link your agents made, and kill a key or a link in one click.
- sources:
  - [1] https://aispace.sh/
