# Portal

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-gosuda/ | JSON https://fshy.ajam.dev/api/v1/entity/github-gosuda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Portal

- `egress/portal` | fails-egress | evidence documented | binding none | category tunnel software with a public relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.145Z (live) | stale on 2026-12-20
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
- tooling: The user installs and runs the portal client, which connects to public community relays; a relay can also be self-hosted.
- composes with: Reaches a community relay outbound; no host is needed unless a self-hosted relay is chosen.
- reliability: the same as interface detail
- notes: Raw TCP/UDP over community or self-hosted relays. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes a user-installed client and public community relays, with no accounts and no published byte allowance. The first-party source supersedes the aggregator list sentence.
- self hosted: no
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hostable relay tunnel (MIT, Go). `portal expose 3000` publishes a localhost service at a public HTTPS URL through community or self-hosted relays; outbound
  - [2] 2026-11-19: the first-party README describes a tunnel client and a public relay network with no published byte allowance | capture: sha256:504cc70e765e5664a184a83846a9b97c906de338f7294222c0794e59da2db1eb | quote: Expose local services through self-hosted or public relays.
  - [2] 2026-11-19: the first-party README gives install steps for a user-installed client | capture: sha256:504cc70e765e5664a184a83846a9b97c906de338f7294222c0794e59da2db1eb | quote: curl -fsSL https://github.com/gosuda/portal-tunnel/releases/latest/download/install.sh | bash
  - [2] 2026-11-19: the first-party README describes an anonymous user-installed client and public relays | capture: sha256:504cc70e765e5664a184a83846a9b97c906de338f7294222c0794e59da2db1eb | quote: No port forwarding. No inbound firewall rules. No manual DNS setup. No accounts.
  - [2] 2026-11-19: the first-party README describes a user-installed client and public relays with no published byte allowance | capture: sha256:504cc70e765e5664a184a83846a9b97c906de338f7294222c0794e59da2db1eb | quote: Expose local services through self-hosted or public relays.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/gosuda/portal-tunnel
