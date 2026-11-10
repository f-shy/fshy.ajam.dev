# Teleport

> goteleport.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goteleport/ | JSON https://fshy.ajam.dev/api/v1/entity/goteleport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Teleport

- `egress/teleport` | paid-only | evidence unverified | binding none | category zero-trust access platform (community edition plus paid cloud) | tier paid
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:52:58.388Z (live) | stale on 2026-11-19
- url https://goteleport.com/
- price paid cloud
- free tier: No price is published: the pricing page is a 'Get Pricing' form and states 'Pay only for what you use: active users and protected resources.' A free Enterprise trial is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published on the page read.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: the cloud product is priced per resource; the community edition is free software that needs a host. | country: None
- interface: cli
- binding note: No hosted free endpoint: the community edition's capacity is whoever hosts it, and the cloud is paid. Application access is TCP/HTTP, no UDP.
- interface detail: tsh, web UI
- tooling: tsh CLI, agents.
- composes with: Needs a host for the community edition.
- reliability: n/a
- notes: Recorded from the aggregator's sentence plus an empty pricing read; the verdict rests on the cloud being a paid product.
- evidence note: The pricing page publishes no tier prices, only a Get Pricing form; paid prices stay unverified.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No allowance is published on the page read.
  - bytes_transit: yes
- evidence:
  - [2] 2026-10-23: page returned 1845 bytes of navigation and no plan table
  - [2] 2026-11-04: the pricing page states a usage-based model and shows only a Get Pricing form | capture: sha256:1c7aac8eb8546b02cf259069d4d4326e34fa54a406127a69445aa346a0373c40 | quote: Transparent Pricing. Pay only for what you use: active users and protected resources.
  - [3] 2026-11-04: the sign-up page offers a free 14-day trial of the Enterprise edition | capture: sha256:b7086f1c5fbc3c2ca81e36987cb168b5c732b59dc48d53c6cd17f563a5feaddd | quote: Free, 14-day trial of Teleport Enterprise
- sources:
  - [1] https://goteleport.com/
  - [2] https://goteleport.com/pricing/
  - [3] https://goteleport.com/signup/
