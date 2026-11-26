# OpenZiti

> openziti.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openziti/ | JSON https://fshy.ajam.dev/api/v1/entity/openziti.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenZiti

- `egress/openziti` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category zero trust overlay (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://openziti.io/docs/learn/introduction/
- price USD 0
- free tier: 'OpenZiti is a free, open-source zero trust networking platform that makes network services invisible to unauthorized users.' Self-hosted; the software imposes no quota. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance: controllers and routers run on self-hosted infrastructure.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: self-hosted; every endpoint is an identity with a certificate issued by the operator's controller | country: None
- interface: cli, rest
- binding note: Nothing counts bytes and every service is reachable only by an enrolled identity, so a public reader cannot start a transfer at all.
- interface detail: ziti CLI and SDKs, plus the controller's REST API
- tooling: ziti CLI, controller, routers, tunnelers, SDKs
- composes with: a private fabric under zrok; it composes with a public ingress and adds none
- reliability: the controller is a single point of failure the operator must run
- notes: Recorded separately from zrok, which is OpenZiti's hosted share front end and already has two records. The distinction that matters: zrok's 5 GB/day is NetFoundry's controller policy, while OpenZiti itself has no meter and no public listener.
- evidence note: A public-router configuration read would confirm that no unauthenticated listener exists; the introduction page states the model but not the router options.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: No WireGuard: 'controllers, routers, tunnelers, and SDKs', with 'Every identity requires a certificate'. No .conf exists.
  - ingress: none
  - bytes_transit: overlay-only
  - transit_note: routers relay between authenticated identities
- evidence:
  - [1] 2026-10-23: 'a free, open-source zero trust networking platform that makes network services invisible to unauthorized users'; 'Every identity requires a certificate'
- sources:
  - [1] https://openziti.io/docs/learn/introduction/
