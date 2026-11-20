# Tunnelmole

> tunnelmole.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelmole/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelmole.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnelmole

- `egress/tunnelmole` | fails-egress | evidence documented | binding none | category tunnel (hosted and self-hosted, HTTP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnelmole.com/
- price USD 0
- free tier: No signup. Run npx tunnelmole 3000 and get a public URL for your local server instantly. Open source, client and server, and self-hostable. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no quota published; the offer is an instant public https URL with no signup; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'No signup' | country: None
- interface: cli
- binding note: No byte quota is published and none is needed: an HTTP-only tunnel cannot carry a WireGuard datagram.
- interface detail: part of the free tier
- tooling: part of the free tier
- composes with: HTTP ingress only
- reliability: free service is a courtesy; the software is self-hostable which moves the cost to a VM
- notes: Open-source tunneling client written in TypeScript. Provides public URLs for local HTTP servers.
- evidence note: Page is short and states the shape plainly. Self-hosting the server would still be an HTTP terminator.
- self hosted: no
- extras:
  - wg_path: none
  - wg_detail: the product is an HTTPS URL issuer for a web server; no TCP or UDP forward is described
  - ingress: http-only
  - volume_stated: no quota published; the offer is an instant public https URL with no signup
  - bytes_transit: yes
  - transit_note: the Tunnelmole service carries the HTTPS traffic
- evidence:
  - [1] 2026-10-23: 'With a public https url just a single command away' and 'No signup'
- sources:
  - [1] https://tunnelmole.com/
