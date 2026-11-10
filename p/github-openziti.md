# zrok

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-openziti/ | JSON https://fshy.ajam.dev/api/v1/entity/github-openziti.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zrok (self-hosted)

- `egress/zrok-selfhost` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category tunnel (self-hosted software)
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://github.com/openziti/zrok
- free tier: Apache-2.0; no limit imposed by the software | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [2]
- egress: whatever the host's NIC and the hosting bill allow | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: cli
- binding note: the software imposes no byte meter; what runs out is the monthly egress allowance of the host it runs on, and that host is a separate provider
- interface detail: zrok share public against your own controller
- tooling: part of interface detail
- composes with: the front half of the self-hosted tunnel chain: your controller, your frontend, and then a plain VPS bill. The relay software is free and the egress is not.
- reliability: Self-hosted deployment requires managing control plane uptime and host egress bandwidth.
- notes: The hosted limits are NetFoundry's policy; a default self-hosted controller has no bandwidth journal configured. Re-graded 2026-10-23: the software is free and the path is not, because it needs a host. The finding is the host.
- evidence note: Architecture and self-hosting deployment requirements are documented in official zrok manuals.
- self hosted: yes
- extras:
  - stale_after_days: 180
  - bytes_transit: self-hosted
  - transit_note: the software runs on the operator's host and the bytes transit that host's NIC
  - hosting_requirement: a rented or free compute service; no local machine is assumed
- evidence:
  - [1] 2026-10-22: 'Run Zrok on your own infrastructure with no limits'
  - [2] 2026-10-22: Apache-2.0 repository; docs/current/ holds the bandwidth-limit journal and relax cycle, so the hosted limits are controller policy rather than protocol
- sources:
  - [1] https://zrok.io/pricing/
  - [2] https://github.com/openziti/zrok
