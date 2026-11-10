# tunnel.pyjam.as

> pyjam.as | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pyjam/ | JSON https://fshy.ajam.dev/api/v1/entity/pyjam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnel.pyjam.as

- `egress/tunnel-pyjam-as` | fails-egress | evidence documented | binding none | category http tunnel over a wireguard link issued by curl | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnel.pyjam.as/
- price USD 0
- free tier: SSL-terminated HTTP tunnels to your local machine - no custom software required, thanks to Wireguard | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance or price is published; the page is four lines long.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account: the curl request is the whole signup. | country: None
- interface: cli
- binding note: Single-operator hobby tunnel. Ingress is restricted to HTTPS; raw TCP and UDP port forwarding to origin services are not supported.
- interface detail: curl plus wg-quick
- tooling: curl and wg-quick.
- composes with: Carries HTTP only; the WG link is the transport, not the ingress.
- reliability: One community host with no stated capacity or SLA.
- notes: The most interesting no-account entry in the sweep: a WireGuard config with zero registration, but the far side terminates HTTPS so the WireGuard link carries only HTTP. The same request shape would not forward a raw UDP port.
- evidence note: The page sets no quota, so only a live transfer shows the real tolerance; the risk is that a shared community endpoint disappears.
- extras:
  - wg_path: registration-api
  - wg_detail: The registration endpoint is the URL itself: 'curl https://tunnel.pyjam.as/8080 > tunnel.conf && wg-quick up ./tunnel.conf'. The port in the path is the local service, and the response is a wg-quick config.
  - ingress: http-only
  - volume_stated: No allowance or price is published; the page is four lines long.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'curl https://tunnel.pyjam.as/8080 > tunnel.conf && wg-quick up ./tunnel.conf'; 'You can now access ... on https://<unique_slug>.tunnel.pyjam.as/'
- sources:
  - [1] https://tunnel.pyjam.as/
