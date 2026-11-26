# openport.io

> openport.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openport/ | JSON https://fshy.ajam.dev/api/v1/entity/openport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## openport.io

- `egress/openport-io` | fails-quota | evidence documented | binding volume-quota | category udp port forward (hosted, commercial) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://openport.io/pricing
- price USD 0
- free tier: free, $0 per month: 1 device, 1 connection per device, 10 MB transfer per month, 1 day connection timeout, No API access | unit: MB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 MB transfer per month on the free plan; 1,000 MB on Home at USD 5/month; 10,000 MB on the educational plan; ingress: tcp | metered: yes | free allowance: 10 MB transfer per month on the free plan; 1,000 MB on Home at USD 5/month; 10,000 MB on the educational plan | source: [1]
- identity: email | detail: a sign-up account and a monthly plan table; the CLI prints a monthly transfer allowance at connect time | country: None
- interface: cli
- limits:
  - volume-quota (binding): 10 MB transfer per month [1]
  - retention-clamped: 1 day connection timeout [1]
- binding note: Free bandwidth is capped at 10 MB and temporary tunnel sessions terminate after 24 hours.
- interface detail: openport 22 after installing the package
- tooling: openport client .deb and a REST API behind a subscription
- composes with: not usable at this volume
- reliability: free connections are terminated after one day
- notes: Not the same service as openport.pw, which is a different free service with a persistent port and no signup.
- evidence note: Distinct from openport.pw, which is a different operator and already has a record. The homepage CLI transcript shows a 976.6 GB monthly figure for a paid state, which is not the free plan.
- extras:
  - wg_path: none
  - wg_detail: the free plan's 1-day connection timeout ends the forward, so no endpoint outlives a day even if the port were stable
  - ingress: tcp
  - volume_tib_month: 9e-06
  - volume_stated: 10 MB transfer per month on the free plan; 1,000 MB on Home at USD 5/month; 10,000 MB on the educational plan
  - bytes_transit: yes
  - transit_note: openport.io terminates and forwards the connection
- evidence:
  - [1] 2026-10-23: free plan: 10 MB transfer per month and a 1 day connection timeout; Home USD 5/month for 1,000 MB
  - [2] 2026-10-23: the product forwards a TCP port: 'openport.io:12345 to localhost:22'
- sources:
  - [1] https://openport.io/pricing
  - [2] https://openport.io/
