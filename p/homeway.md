# Homeway

> homeway.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/homeway/ | JSON https://fshy.ajam.dev/api/v1/entity/homeway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Homeway

- `egress/homeway` | fails-egress | evidence documented | binding volume-quota | category home assistant remote access tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.938Z (live) | stale on 2026-12-20
- url https://homeway.io/pricing
- price USD 0 (supporter USD 3.49/month) | parsed USD 3.49/mo
- free tier: You account gets one Home Assistant server for free, empowered with remote access, Sage AI, and more. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The pricing page read publishes no byte figure. The aggregator's sentence is 'The free tier has a monthly data limit cap, but unlimited data is only $2.49/month'.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account, one Home Assistant server per account on free; more servers need a supporter plan. | country: None
- interface: rest
- limits:
  - volume-quota (binding): The free tier is one server with a data cap the page does not quantify, so a byte quota is what fails, and its size is unknown. Protocol is the second wall: Home Assistant remote access is HTTP and WebSocket, so there is no UDP path at any price. [1]
- binding note: The free tier is one server with a data cap the page does not quantify, so a byte quota is what fails, and its size is unknown. Protocol is the second wall: Home Assistant remote access is HTTP and WebSocket, so there is no UDP path at any price.
- interface detail: Home Assistant add-on.
- tooling: Home Assistant integration.
- composes with: Nothing to chain: it is not a general tunnel.
- reliability: Scoped to one application; nothing else can be published through it.
- notes: Application-specific tunnel for Home Assistant remote access. Does not provide arbitrary Layer 4 port forwarding.
- evidence note: The first-party pricing page read on 2026-11-19 states one free Home Assistant server and lists 'Unthrottled Bandwidth' as a supporter perk, but publishes no byte figure for the free tier; the monthly-cap sentence is third-party. A sign-in would be needed to read account limits.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: The pricing page read publishes no byte figure. The aggregator's sentence is 'The free tier has a monthly data limit cap, but unlimited data is only $2.49/month'.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: one free Home Assistant server with remote access; supporter plans USD 3.49 and USD 6.99 per month for more servers
  - [2] 2026-10-23: 'The free tier has a monthly data limit cap, but unlimited data is only $2.49/month' (third party)
  - [1] 2026-11-19: the first-party pricing page confirms one free Home Assistant server and publishes no byte allowance | capture: sha256:d827cbd681bdbcb94c78febd89427746d31bbaf3990bf063bfc8f09e433912aa | quote: You account gets one Home Assistant server for free, empowered with remote access, Sage AI, and more.
  - [1] 2026-11-19: the first-party pricing page confirms one free server and states no byte figure | capture: sha256:d827cbd681bdbcb94c78febd89427746d31bbaf3990bf063bfc8f09e433912aa | quote: You account gets one Home Assistant server for free, empowered with remote access, Sage AI, and more.
- sources:
  - [1] https://homeway.io/pricing
  - [2] https://github.com/anderspitman/awesome-tunneling
