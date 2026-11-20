# Svix Play

> svix.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/svix/ | JSON https://fshy.ajam.dev/api/v1/entity/svix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Svix Play

- `egress/svix-play` | fails-egress | evidence documented | binding request-rate | category webhook relay (http only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.svix.com/play/
- price USD 0
- free tier: Easily inspect, test, and debug incoming webhooks with the free Svix Play webhook tester & debugger. | unit: requests | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published; the unit is webhook requests, and the page gives no count.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Free, no-signup hosted webhook relay' per the aggregator; a URL is generated on demand. | country: None
- interface: cli
- limits:
  - request-rate (binding): Requests rather than bytes are what the service counts, and no count is published, so an unpublished request cap is what fails. Transport fails first in practice: a webhook endpoint, not a port. [1]
- binding note: Requests rather than bytes are what the service counts, and no count is published, so an unpublished request cap is what fails. Transport fails first in practice: a webhook endpoint, not a port.
- interface detail: svix listen URL
- tooling: svix CLI.
- composes with: none for bulk egress.
- reliability: Intended for development; no delivery guarantee published.
- notes: Free and accountless, which is why it is recorded rather than skipped, but it carries HTTP POST bodies only.
- evidence note: Nothing would raise it; the product is a webhook debugger.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance is published; the unit is webhook requests, and the page gives no count.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'free Svix Play webhook tester & debugger'; 'Use the Svix CLI for a free and secure public URL that relays webhooks'
- sources:
  - [1] https://www.svix.com/play/
