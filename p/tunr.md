# tunr

> tunr.sh | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunr/ | JSON https://fshy.ajam.dev/api/v1/entity/tunr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunr

- `egress/tunr` | fails-egress | evidence documented | binding write-gated | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunr.sh/
- price USD 0
- free tier: Open-source CLI - Free tunnels - 3 free apps. The 3-second tunnel that started it all - still free, still first-class. HTTPS, WebSocket, TCP, UDP, TLS. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published. The deploy path caps the compressed upload at 50 MB, which is a deploy limit and not a tunnel allowance.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Deploying an app needs a dashboard account at app.tunr.sh; share tunnels appear usable from the CLI. The signup form was not read. | country: None
- interface: cli, rest
- limits:
  - write-gated (binding): UDP never reaches the wire: raw TCP and UDP are only framed onto a WebSocket, so a WireGuard client cannot dial it at all. That gate binds before any allowance. [1]
  - per-object-cap: compressed deploy upload limited to 50 MB [2]
  - volume-quota: no tunnel byte allowance published [1]
- binding note: UDP never reaches the wire: raw TCP and UDP are only framed onto a WebSocket, so a WireGuard client cannot dial it at all. That gate binds before any allowance.
- interface detail: tunr share --port 3000, tunr deploy, and an MCP tool surface.
- tooling: brew install ahmetvural79/tap/tunr, or go install; an MCP server exposes tunr_deploy.
- composes with: Replaces a free VM for static demos; cannot carry a WireGuard handshake or a raw game protocol.
- reliability: Deployed apps sleep when idle and wake in about 150 ms; the tunnel tier is a marketing on-ramp to the deploy product, so it can be repriced.
- notes: Launched 2026-06-21 as a 3-second tunnel and has since pivoted to an app-deploy platform. The homepage claim of TCP and UDP support is true only in the WebSocket-framing sense, which the docs admit.
- evidence note: A probe against a live tunnel would confirm the WebSocket-only framing; the docs state it plainly.
- extras:
  - wg_path: none
  - wg_detail: The relay has no raw UDP port yet: the docs say the relay exposes a raw tunnel only as a WebSocket stream at wss://<subdomain>.tunr.sh/tunnel/tcp (binary frames carry the bytes). There's no raw TCP/UDP port on the relay yet, so native clients like psql or ssh can't connect directly.
  - ingress: http-only
  - volume_stated: No byte allowance is published. The deploy path caps the compressed upload at 50 MB, which is a deploy limit and not a tunnel allowance.
  - bytes_transit: yes
  - transit_note: The tunr.sh edge relay carries the bytes over WebSocket.
- evidence:
  - [1] 2026-10-23: Free tunnels, 3 free apps, and the claim of HTTPS, WebSocket, TCP, UDP and TLS support.
  - [2] 2026-10-23: TCP, UDP and TLS are experimental and exposed only as a WebSocket stream; there is no raw TCP/UDP port on the relay yet.
  - [3] 2026-06-21: Show HN launch date.
- sources:
  - [1] https://tunr.sh/
  - [2] https://tunr.sh/docs.html
  - [3] https://news.ycombinator.com/item?id=48623146
