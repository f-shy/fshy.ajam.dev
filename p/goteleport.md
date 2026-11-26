# Teleport

> goteleport.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goteleport/ | JSON https://fshy.ajam.dev/api/v1/entity/goteleport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Teleport

- `egress/teleport` | paid-only | evidence unverified | binding none | category zero-trust access platform (community edition plus paid cloud) | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:43:51.888Z (live) | stale on 2026-12-10
- url https://goteleport.com/
- price paid cloud
- free tier: A free 14-day trial of Teleport Enterprise is offered; no free plan is stated. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published on the page read.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: the pricing page states usage-based pricing on active users and protected resources | country: None
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
  - [3] 2026-10-23: page returned 1845 bytes of navigation and no plan table
  - [3] 2026-11-04: the pricing page states a usage-based model and shows only a Get Pricing form | capture: sha256:1c7aac8eb8546b02cf259069d4d4326e34fa54a406127a69445aa346a0373c40 | quote: Transparent Pricing. Pay only for what you use: active users and protected resources.
  - [1] 2026-11-04: the sign-up page offers a free 14-day trial of the Enterprise edition | capture: sha256:b7086f1c5fbc3c2ca81e36987cb168b5c732b59dc48d53c6cd17f563a5feaddd | quote: Free, 14-day trial of Teleport Enterprise
  - [1] 2026-11-25: the sign-up page offers a free 14-day Enterprise trial | capture: sha256:b7086f1c5fbc3c2ca81e36987cb168b5c732b59dc48d53c6cd17f563a5feaddd | quote: Free, 14-day trial of Teleport Enterprise
  - [3] 2026-11-25: pricing is by active users and protected resources | capture: sha256:1c7aac8eb8546b02cf259069d4d4326e34fa54a406127a69445aa346a0373c40 | quote: Transparent Pricing. Pay only for what you use: active users and protected resources.
  - [1] 2026-11-25: the trial is requested through an activation link; no card is stated | capture: sha256:b7086f1c5fbc3c2ca81e36987cb168b5c732b59dc48d53c6cd17f563a5feaddd
  - [3] 2026-11-25: the pricing page publishes a usage-based model and no free plan | capture: sha256:1c7aac8eb8546b02cf259069d4d4326e34fa54a406127a69445aa346a0373c40 | quote: Transparent Pricing. Pay only for what you use: active users and protected resources.
- sources:
  - [1] https://goteleport.com/signup/
  - [2] https://goteleport.com/
  - [3] https://goteleport.com/pricing/
