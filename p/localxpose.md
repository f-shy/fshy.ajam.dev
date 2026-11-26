# LocalXpose

> localxpose.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localxpose/ | JSON https://fshy.ajam.dev/api/v1/entity/localxpose.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LocalXpose

- `egress/localxpose-free` | fails-egress | evidence documented | binding write-gated | category tunnel (hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T17:26:44.696Z (live) | stale on 2026-12-26
- url https://localxpose.io/pricing
- free tier: 2 active HTTP, HTTPS tunnels | unit: objects | metered on: object-count | read on: 2026-10-22 | source: [1] | note: The Starter plan's published negatives are 'Time limits' and 'Interstitial warning page'; no bandwidth figure is published for it.
- per-object cap: not applicable: a stream
- retention: not applicable: a live tunnel, not stored bytes; the Starter plan is time limited. | source: [1]
- egress: not published: the Starter plan carries HTTP and HTTPS tunnels only, and no bandwidth figure; UDP needs PRO at USD 8 a month. | metered: no | source: [1]
- identity: email | detail: a LocalXpose account
- interface: cli
- limits:
  - write-gated (binding): UDP tunneling and TCP/UDP port forwarding are PRO features at USD 8 a month [1]
- limits note: The Starter plan also caps concurrently active tunnels at 2; an active tunnel is any tunnel currently running, and no vocabulary kind names a count of tunnels.
- binding note: The Starter plan carries HTTP and HTTPS only; a UDP path needs PRO at USD 8 a month, so the plan is what fails first, not a byte allowance.
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
  - [1] 2026-11-25: TCP and UDP tunneling are PRO features, so the free plan has no UDP path | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: HTTP, HTTPS, TCP, TLS, UDP tunneling
  - [1] 2026-11-25: the free plan allows two active HTTP and HTTPS tunnels | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: 2 active HTTP, HTTPS tunnels
  - [1] 2026-11-25: the free plan is time limited | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: Time limits
  - [1] 2026-11-25: the free allowance is a count of active tunnels | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: 2 active HTTP, HTTPS tunnels
  - [1] 2026-11-25: TCP and UDP tunneling are PRO features | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: HTTP, HTTPS, TCP, TLS, UDP tunneling
  - [1] 2026-11-25: TCP and UDP tunneling are PRO features at USD 8 a month | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: HTTP, HTTPS, TCP, TLS, UDP tunneling
  - [1] 2026-11-25: TCP and UDP tunneling are PRO features, so the plan is what binds | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: HTTP, HTTPS, TCP, TLS, UDP tunneling
  - [1] 2026-11-25: the free plan allows two active tunnels | capture: sha256:8a0a85f771e8d37e23dae85e3bffe49c8044f874e6fd0a867d8ed9ce01427fe5 | quote: 2 active HTTP, HTTPS tunnels
- sources:
  - [1] https://localxpose.io/pricing
