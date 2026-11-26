# idoud

> idoud.cc | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/idoud/ | JSON https://fshy.ajam.dev/api/v1/entity/idoud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## idoud (idoud.cc)

- `storage/idoud` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:04.773Z (inherited) | stale on 2026-12-04
- url https://idoud.cc/
- free tier: none reachable: mydearniko/idoud markets 'absolutely free, unlimited cloud storage' with a Go CLI and a curl-pipe installer, but both the site and the install host are down (530/502 in two separate probes). | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: mydearniko/idoud markets 'absolutely free, unlimited cloud storage' with a Go CLI and a curl-pipe installer, but both the site and the install host are down (530/502 in two separate probes).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: mydearniko/idoud markets 'absolutely free, unlimited cloud storage' with a Go CLI and a curl-pipe installer, but both the site and the install host are down (530/502 in two separate probes).
  - [2] 2026-10-21: cited as the basis of the rejection: mydearniko/idoud markets 'absolutely free, unlimited cloud storage' with a Go CLI and a curl-pipe installer, but both the site and the install host are down (530/502 in two separate probes).
  - [3] 2026-10-21: cited as the basis of the rejection: mydearniko/idoud markets 'absolutely free, unlimited cloud storage' with a Go CLI and a curl-pipe installer, but both the site and the install host are down (530/502 in two separate probes).
  - probe:idoud.cc 2026-11-19: the primary site still answers HTTP 530 and is unusable | capture: sha256:e48471df3dd2b2f8c841ac2501b858907b705b99ed25c0e9c47d6efa6c345d95 | quote: "status": 530
- sources:
  - [1] https://idoud.cc/
  - [2] https://idoud.com/
  - [3] https://github.com/mydearniko/idoud
