# Beeceptor Local Tunnel

> beeceptor.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beeceptor/ | JSON https://fshy.ajam.dev/api/v1/entity/beeceptor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Beeceptor Local Tunnel

- `egress/beeceptor` | fails-egress | evidence documented | binding request-rate | category http tunnel and mock server | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://beeceptor.com/local-tunnel/
- price USD 0
- free tier: Setup a tunnel and get a public URL. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published on the local-tunnel page.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account owns the endpoint name; the page does not state terms. | country: None
- interface: cli, rest
- limits:
  - request-rate (binding): The product counts intercepted requests and mock rules, not bytes, and publishes neither on this page. Transport is HTTP over a socket tunnel, so no UDP. [1]
- binding note: The product counts intercepted requests and mock rules, not bytes, and publishes neither on this page. Transport is HTTP over a socket tunnel, so no UDP.
- interface detail: CLI plus mock rules in the dashboard.
- tooling: CLI plus web console.
- composes with: none for bulk egress.
- reliability: Designed for API mocking and inspection.
- notes: Mock-server first, tunnel second.
- evidence note: A published request quota would sharpen the binding.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance is published on the local-tunnel page.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'Beeceptor's Local Tunnel uses secure HTTP Sockets to punch through firewalls and NATs'
- sources:
  - [1] https://beeceptor.com/local-tunnel/
