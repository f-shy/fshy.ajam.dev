# nport.link

> nport.link | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nport/ | JSON https://fshy.ajam.dev/api/v1/entity/nport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nport.link

- `egress/nport` | qualifies-with-caveat | evidence reported | binding retention-clamped | category relay (hosted, HTTPS tunnel, Cloudflare-backed) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-10T03:20:00.000Z (live) | stale on 2026-11-25
- url https://nport.link/
- free tier: Free with no sign-up: a stable https://user-<n>.nport.link URL over HTTP/HTTPS and WebSocket, served from Cloudflare's edge. The harness measured a 4-hour session cap and confirmed the CLI spawns a bundled cloudflared. | unit: hours | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a tunnel, not an object | source: [1]
- retention: not applicable: a live tunnel; the harness measured a 4-hour session cap | source: probe:https://user-8740.nport.link/
- egress: no byte quota is published; the tunnel is a Cloudflare edge in front of a bundled cloudflared, so Cloudflare's terms and edge limits apply | metered: no | source: [1]
- identity: anonymous | detail: no sign-up: the page says 'No sign-up required', and the harness registered a tunnel with zero credentials
- interface: cli
- limits:
  - retention-clamped (binding): a 4-hour session cap probe:https://user-8740.nport.link/
- binding note: the 4-hour session cap fails first; the edge is Cloudflare's, so its limits also apply underneath.
- interface detail: nport 8080 registers a stable https://user-<n>.nport.link name and runs a bundled cloudflared tunnel to it
- tooling: the nport npm CLI, which spawns a bundled cloudflared binary
- composes with: it adds a stable name and a session cap over a Cloudflare quick tunnel rather than an independent relay network; a reader who excludes Cloudflare from the threat model excludes this too
- reliability: nport is a wrapper around cloudflared and the public edge is Cloudflare's, so an outage or a policy change at Cloudflare reaches it; the harness measured a 4-hour session cap
- notes: A stable-name wrapper around a Cloudflare quick tunnel: the naming is its own, the edge is not. The 4-hour session cap and the Cloudflare dependency are the two facts a reader needs.
- evidence note: the no-sign-up and Cloudflare claims are read from the vendor page; the 4-hour cap is a sandbox measurement, so the record is reported
- evidence:
  - [1] 2026-11-10: no sign-up is required | capture: sha256:86237d429bb66455614f7322db3273895262b8695973f20a58de8a9db2ec7688 | quote: No sign-up required.
  - [1] 2026-11-10: the tunnel edge is Cloudflare's | capture: sha256:86237d429bb66455614f7322db3273895262b8695973f20a58de8a9db2ec7688 | quote: Powered by Cloudflare
  - probe:https://user-8740.nport.link/ 2026-11-05: the harness measured a 4-hour session cap | capture: sha256:5190691e81bec69ed84140fb9825e0f900cc171d64ef00f0c39bc893fea73290 | quote: 4 h session cap
- sources:
  - [1] https://nport.link/
