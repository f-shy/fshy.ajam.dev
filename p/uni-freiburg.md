# freidata

> uni-freiburg.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-freiburg/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-freiburg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freidata (university of freiburg, inveniordm)

- `storage/freidata` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:38.678Z (inherited) | stale on 2026-12-04
- url https://freidata.uni-freiburg.de/api/records?size=1
- free tier: none reachable: the endpoint answers again. A GET to freidata.uni-freiburg.de/api/records?size=1 returned HTTP 200 with a published InvenioRDM records listing on 2026-11-19, ending the TLS failure recorded previously. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Endpoint freidata.uni-freiburg.de answered HTTP 200 on 2026-11-19; the previously recorded TLS handshake failure no longer reproduces.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Unreachable — the host stopped completing TLS handshakes mid-research (curl: 'Failed to connect to freidata.uni-freiburg.de port 443 after 21086 ms'). It answered the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Unreachable — the host stopped completing TLS handshakes mid-research (curl: 'Failed to connect to freidata.uni-freiburg.de port 443 after 21086 ms'). It answered the API
  - probe:freidata.uni-freiburg.de/api/records?size=1 2026-11-19: the endpoint returned HTTP 200, so the recorded TLS failure no longer holds | capture: sha256:d0f9f309f45a891d5d643bc823bd01bdf53bb736dce375ecf191a87eb069c0d1 | quote: "status": 200
  - probe:freidata.uni-freiburg.de/api/records?size=1 2026-11-19: the endpoint answered HTTP 200, contradicting the recorded TLS failure | capture: sha256:d0f9f309f45a891d5d643bc823bd01bdf53bb736dce375ecf191a87eb069c0d1 | quote: "status": 200
  - probe:freidata.uni-freiburg.de/api/records?size=1 2026-11-19: the endpoint answered HTTP 200 on the re-check | capture: sha256:d0f9f309f45a891d5d643bc823bd01bdf53bb736dce375ecf191a87eb069c0d1 | quote: "status": 200
- sources:
  - [1] https://freidata.uni-freiburg.de/api/records?size=1
