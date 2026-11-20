# Malai

> malai.sh | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/malai/ | JSON https://fshy.ajam.dev/api/v1/entity/malai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Malai

- `egress/malai` | dead | evidence documented | binding none | category p2p tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://malai.sh/
- price USD 0
- free tier: The deployment is paused. The last public offer was: No signup, no accounts, and you can self-host your own http bridge if you want. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Nothing is served: malai.sh answers with This deployment is temporarily paused.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No signup and no accounts were required when it ran. | country: None
- interface: cli
- limits:
  - volume-quota: service offline [1]
- binding note: A paused deployment fails before any quota applies.
- interface detail: malai http 3000 --public, or malai http-bridge to run a bridge.
- tooling: malai CLI; self-hostable http-bridge.
- composes with: Would have shared a free VM's HTTP port over iroh; nothing to chain while the bridge is paused.
- reliability: Hosted bridge is inactive. Software is open source and supports self-hosting.
- notes: The pattern, an iroh relay plus a community bridge, recurs in several 2025-2026 launches and the bridge is the part that dies. Historical citation moved out of evidence because it no longer proves the present claim: 'Launch: share a dev server over P2P on the iroh stack, no signup, public bridge at kulfi.site.' (https://news.ycombinator.com/item?id=43844500, 2025-04-30).
- evidence note: A later read of malai.sh would show whether it returned; the pause notice is the current state.
- extras:
  - wg_path: none
  - wg_detail: It carried HTTP and, from 0.2.5, TCP. No UDP path was announced, and the hosted bridge is down.
  - ingress: none
  - volume_stated: Nothing is served: malai.sh answers with This deployment is temporarily paused.
  - bytes_transit: overlay-only
  - transit_note: iroh relay and direct P2P; no relay is currently operated by the project.
- evidence:
  - [1] 2026-10-23: This deployment is temporarily paused, with an HTTP 402 from the host.
  - [2] 2026-10-23: TCP support added in 0.2.5; no UDP support claimed.
  - [1] 2026-10-23: the page returns upstream status 402 with the title 'Deployment Paused', which confirms the service is not running
- sources:
  - [1] https://malai.sh/
  - [2] https://news.ycombinator.com/item?id=44107393
