# LocalXpose

> localxpose.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localxpose/ | JSON https://fshy.ajam.dev/api/v1/entity/localxpose.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LocalXpose

- `egress/localxpose-free` | qualifies-with-caveat | evidence documented | binding request-rate | category tunnel (hosted)
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://localxpose.io/pricing
- free tier: 2 active HTTP and HTTPS tunnels, no time limit | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: not applicable: no session cap on the free tier | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: a LocalXpose account
- interface: cli
- limits note: counts of things, not rates, so no vocabulary kind names them: 2 concurrently active tunnels; an active tunnel is any tunnel currently running
- binding note: The free plan publishes no bandwidth figure at all: the pricing page lists 'Unlimited bandwidth' under the USD 8 Pro row only, and the free row's stated negatives are 'Time limits' and 'Interstitial warning page'. UDP and TCP forwarding are Pro features, so the ingress test fails before a byte is counted and the volume question never arises.
- interface detail: loclx tunnel http
- tooling: part of interface detail
- composes with: a free persistent tunnel for two services with no published byte quota, so it composes with an origin and cannot be sized in advance.
- reliability: Free tunnels are HTTP and HTTPS only, time limited, and serve an interstitial warning page to visitors
- notes: No byte quota is published, and none is needed to decide: the free tier cannot carry UDP. The vendor's own pages disagree on whether free bandwidth is unlimited, which is why the number is not recorded as such: a January 2026 blog post says '2 HTTP tunnels with unlimited bandwidth', while the September 2026 free-port-forwarding page says raw TCP and UDP forwarding and unlimited bandwidth are Pro. Unmeasured. Records the vendor's internal contradiction instead of silently picking a side.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the tunnel relays the origin's bytes; no byte quota is published
  - ingress: http-only
- evidence:
  - [1] 2026-10-22: 2 active HTTP/HTTPS tunnels on the free tier and the definition of an active tunnel
  - [1] 2026-10-23: Starter lists HTTP and HTTPS tunnels only; PRO adds 'HTTP, HTTPS, TCP, TLS, UDP tunneling' and 'TCP, UDP port forwarding'
- sources:
  - [1] https://localxpose.io/pricing
