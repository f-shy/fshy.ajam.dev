# hastebin.com

> toptal.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/toptal/ | JSON https://fshy.ajam.dev/api/v1/entity/toptal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hastebin.com (toptal)

- `storage/hastebin-com` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:03.729Z (live) | stale on 2026-12-04
- url https://www.toptal.com/developers/hastebin/documentation
- free tier: none reachable: API now requires a GitHub-issued access token, one token per user, 100 req/min, and content expires in 30 days even when authenticated (7 days otherwise). No anonymous writes. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: The API requires the user to sign in with a GitHub account and generate a token.
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: API now requires a GitHub-issued access token, one token per user, 100 req/min, and content expires in 30 days even when authenticated (7 days otherwise). No anonymous writes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: API now requires a GitHub-issued access token, one token per user, 100 req/min, and content expires in 30 days even when authenticated (7 days otherwise). No anonymous writes.
  - [1] 2026-11-19: pasted content expires after 30 days for authorized users and 7 days otherwise | capture: sha256:863cd7d7a1735c7622a8d455232d41810b376e3e1beebc929b97356b0af97a01 | quote: Pasted content will be available for 30 days for authorized users and 7 days otherwise.
  - [1] 2026-11-19: API access requires signing in with a GitHub account to generate a token | capture: sha256:863cd7d7a1735c7622a8d455232d41810b376e3e1beebc929b97356b0af97a01 | quote: Sign in with your Github account, generate a token and start using the Hastebin API.
- sources:
  - [1] https://www.toptal.com/developers/hastebin/documentation
