# freidata

> uni-freiburg.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-freiburg/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-freiburg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freidata (university of freiburg, inveniordm)

- `storage/freidata` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://freidata.uni-freiburg.de/api/records?size=1
- free tier: none reachable: Endpoint freidata.uni-freiburg.de port 443 failed TLS handshake negotiation with connection timeout. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Unreachable — the host stopped completing TLS handshakes mid-research (curl: 'Failed to connect to freidata.uni-freiburg.de port 443 after 21086 ms'). It answered the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Unreachable — the host stopped completing TLS handshakes mid-research (curl: 'Failed to connect to freidata.uni-freiburg.de port 443 after 21086 ms'). It answered the API
- sources:
  - [1] https://freidata.uni-freiburg.de/api/records?size=1
