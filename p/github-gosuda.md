# Portal

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-gosuda/ | JSON https://fshy.ajam.dev/api/v1/entity/github-gosuda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Portal

- `egress/portal` | fails-egress | evidence reported | binding none | category tunnel software with a public relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/gosuda/portal-tunnel
- price USD 0
- free tier: Self-hostable relay tunnel (MIT, Go). `portal expose 3000` publishes a localhost service at a public HTTPS URL through community or self-hosted relays; outbound-only, no account, raw TCP/UDP, SNI-based routing, tenant-side TLS termination. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: community relays carry the traffic, outbound only and with no account; the list entry states no quota. Raw TCP/UDP. A self-hosted relay is the last resort.
- interface detail: not established
- tooling: the portal client (MIT, Go): portal expose PORT
- composes with: Reaches a community relay outbound; no host is needed unless a self-hosted relay is chosen.
- reliability: the same as interface detail
- notes: Raw TCP/UDP over community or self-hosted relays. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: no
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hostable relay tunnel (MIT, Go). `portal expose 3000` publishes a localhost service at a public HTTPS URL through community or self-hosted relays; outbound
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/gosuda/portal-tunnel
