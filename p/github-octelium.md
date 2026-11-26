# Octelium

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-octelium/ | JSON https://fshy.ajam.dev/api/v1/entity/github-octelium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Octelium

- `egress/octelium` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.741Z (live) | stale on 2026-12-20
- url https://github.com/octelium/octelium
- price USD 0
- free tier: A FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an and a homelab infrastructure. AGPL-3.0 and Apache-2.0 Licenses. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Self-hosted ZTNA with an ngrok-style HTTP path.
- interface detail: not established
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: Self-hosted ZTNA with an ngrok-style HTTP path. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes free open-source software designed for single-tenant self-hosting with no proprietary cloud-based control plane, so no hosted endpoint or byte allowance is published. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: A FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an and a home
  - [2] 2026-11-19: the first-party README states the platform has no hosted control plane and is self-hosted | capture: sha256:438ab42e11f7ca7168804a54eb3780b6d8ece3752a4498450503a2dcd2b0f889 | quote: There is no proprietary cloud-based control plane, nor is this some crippled demo open source version of a separate fully functional SaaS paid service.
  - [2] 2026-11-19: the first-party README directs the user to install a cluster on a user-supplied VM or machine | capture: sha256:438ab42e11f7ca7168804a54eb3780b6d8ece3752a4498450503a2dcd2b0f889 | quote: There is no proprietary cloud-based control plane, nor is this some crippled demo open source version of a separate fully functional SaaS paid service.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:438ab42e11f7ca7168804a54eb3780b6d8ece3752a4498450503a2dcd2b0f889 | quote: There is no proprietary cloud-based control plane, nor is this some crippled demo open source version of a separate fully functional SaaS paid service.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/octelium/octelium
