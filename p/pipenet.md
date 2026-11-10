# Pipenet

> pipenet.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pipenet/ | JSON https://fshy.ajam.dev/api/v1/entity/pipenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pipenet

- `egress/pipenet` | fails-egress | evidence documented | binding request-rate | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://pipenet.dev/
- price USD 0
- free tier: Open-source and 100% self-hostable. Public instance at *.pipenet.dev if you don't want to self-host. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published for the public instance.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account is described: the public instance is a hostname you point a client at. The README shows no signup. | country: None
- interface: cli, rest
- limits:
  - request-rate (binding): maxTcpSockets per client defaults to 10 [1]
- binding note: The only published control is a socket cap per client, so concurrency fails long before any byte allowance would. The transport is also HTTP-only, so a UDP datagram has no path at all.
- interface detail: Node client plus a REST status API at /api/status.
- tooling: npm client; self-hostable Node server.
- composes with: Only useful as an HTTP ingress for an MCP or webhook endpoint.
- reliability: Public instance is a courtesy run by the maintainer with no stated capacity or SLA.
- notes: Launched 2026-01-19. A localtunnel rewrite with multiplexing over one port, built for an MCP inspector. It is a software project with a courtesy public instance, not a capacity provider.
- evidence note: A measured run against the public instance would show whether it is still up and what it rate-limits; the UDP question is already answered by the maintainer.
- extras:
  - wg_path: none
  - wg_detail: HTTP-focused by the maintainer's own answer: The current implementation is HTTP-focused as that was the primary use case.
  - ingress: http-only
  - volume_stated: No allowance is published for the public instance.
  - bytes_transit: yes
  - transit_note: The pipenet.dev instance relays HTTP requests to the local client.
- evidence:
  - [1] 2026-10-23: Server options include maxTcpSockets default 10 and tunnelPort; the API is an HTTP tunnel server, no UDP or raw port.
  - [2] 2026-01-19: Launch post and maintainer reply that the implementation is HTTP-focused and UDP support is not planned.
- sources:
  - [1] https://pipenet.dev/
  - [2] https://news.ycombinator.com/item?id=46680597
