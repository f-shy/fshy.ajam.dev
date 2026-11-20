# proxy.py

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-abhinavsingh/ | JSON https://fshy.ajam.dev/api/v1/entity/github-abhinavsingh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## proxy.py

- `egress/proxy-py` | fails-egress | evidence documented | binding none | category tunnel software with a public relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.642Z (live) | stale on 2026-12-20
- url https://github.com/abhinavsingh/proxy.py
- price USD 0
- free tier: General-purpose HTTP/HTTPS proxy framework written in Python; since v2.4.9 it also bundles `grout`, an ngrok/frp-style tunnel that exposes local HTTP/HTTPS/WebSocket/TCP services at public URLs via the hosted Jaxl relay. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: A hosted relay exists: the first-party README states the grout thick client and servers are hosted at jaxl.io, while no byte allowance is published.; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: the hosted Jaxl relay carries the traffic of grout, the tunnel bundled in proxy.py; the list entry states no quota.
- interface detail: not established
- tooling: proxy.py (Python), which bundles the grout client
- composes with: grout reaches the hosted Jaxl relay outbound; no host is needed.
- reliability: the same as interface detail
- notes: Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub README read on 2026-11-19 states the grout thick client and servers are hosted at jaxl.io; the former no-hosted-service basis no longer stands. No byte allowance is published and no allowance was found on a first-party page, so the fails-egress verdict is kept and the list entry is superseded as the basis.
- self hosted: no
- extras:
  - wg_path: none
  - ingress: none
  - bytes_transit: no
  - transit_note: none
- evidence:
  - [1] 2026-10-23: list entry sentence: General-purpose HTTP/HTTPS proxy framework written in Python; since v2.4.9 it also bundles `grout`, an ngrok/frp-style tunnel that exposes local HTTP/HTTPS/WebS
  - [2] 2026-11-19: the first-party README states the grout thick client and servers are hosted at jaxl.io, so a hosted relay exists | capture: sha256:9dda94812ff34d62650d5c1709e4d98042d8ed35f4d24f8c6ba304d4da1df020
  - [2] 2026-11-19: the first-party README contradicts the former no-hosted-service claim by naming hosted grout servers at jaxl.io | capture: sha256:9dda94812ff34d62650d5c1709e4d98042d8ed35f4d24f8c6ba304d4da1df020
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis and names a hosted relay | capture: sha256:9dda94812ff34d62650d5c1709e4d98042d8ed35f4d24f8c6ba304d4da1df020
  - [2] 2026-11-19: the first-party README states the grout thick client and servers are hosted at jaxl.io | capture: sha256:9dda94812ff34d62650d5c1709e4d98042d8ed35f4d24f8c6ba304d4da1df020
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/abhinavsingh/proxy.py
