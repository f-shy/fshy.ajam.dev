# PageKite

> pagekite.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pagekite/ | JSON https://fshy.ajam.dev/api/v1/entity/pagekite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PageKite

- `egress/pagekite` | trial-only | evidence documented | binding volume-quota | category tunnel (hosted, trial-based) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://pagekite.net/pricing/
- price USD 0
- free tier: Trial period: 31 days & 2.5 GB | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Trial is 31 days and 2.5 GB; the cheapest paid plan is 15 GB monthly for USD 5.99, and the largest is 750 GB; ingress: tcp | metered: yes | free allowance: Trial is 31 days and 2.5 GB; the cheapest paid plan is 15 GB monthly for USD 5.99, and the largest is 750 GB | source: [2]
- identity: email | detail: an account on pagekite.net; the free offer is a trial, and the site also says a friendly message can earn free service | country: None
- interface: cli
- limits:
  - volume-quota (binding): 2.5 GB during a 31-day trial [1]
- binding note: The trial's 2.5 GB and its 31-day life both fail, and the largest paid plan at 750 GB is still under one TiB.
- interface detail: pagekite.py frontend:localport name.pagekite.me
- tooling: part of interface detail
- composes with: web and TCP ingress only
- reliability: new subscriptions are stated to be unavailable as of this reading
- notes: The signup page also states 'We are temporarily unable to process new subscriptions', which is a reliability fact about the paid path rather than the trial.
- evidence note: UDP support is unverified and not claimed: no PageKite page read mentions UDP. The verdict rests on the trial limits, which are explicit.
- extras:
  - wg_path: none
  - wg_detail: PageKite is an HTTP and TCP kite proxy with no documented UDP forward; the pricing page sells monthly traffic for web and TCP kites only
  - ingress: tcp
  - volume_tib_month: 0.002274
  - volume_stated: Trial is 31 days and 2.5 GB; the cheapest paid plan is 15 GB monthly for USD 5.99, and the largest is 750 GB
  - bytes_transit: yes
  - transit_note: PageKite relays the kite traffic
- evidence:
  - [1] 2026-10-23: 'Trial period: 31 days & 2.5 GB'; paid plans run 15 GB to 750 GB monthly
- sources:
  - [1] https://pagekite.net/signup/?more=bw
  - [2] https://pagekite.net/pricing/
