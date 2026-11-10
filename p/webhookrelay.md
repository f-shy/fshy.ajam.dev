# Webhook Relay

> webhookrelay.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webhookrelay/ | JSON https://fshy.ajam.dev/api/v1/entity/webhookrelay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webhook Relay

- `egress/webhook-relay` | paid-only | evidence reported | binding request-rate | category webhook relay and http/tcp tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://webhookrelay.com/pricing/
- price USD 0 (paid from USD 9.99/month) | parsed USD 9.99/mo
- free tier: Pricing - Free Plan & Paid from $9.99/mo | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The pricing page read renders testimonials and no plan table; no free byte allowance could be read.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account and an access token: 'Access tokens authenticate Webhook Relay agents, CLI commands and management API requests.' | country: None
- interface: cli, rest
- limits:
  - request-rate (binding): free plan exists; limits not rendered on the page read [1]
- binding note: A free plan is named in the page title, but no allowance, request count or tunnel count is in the extracted page, so the constraint that fails first is unknown at any volume. The aggregator says a paid plan is required for bidirectional tunnels.
- interface detail: Dashboard, CLI, management API with scoped tokens.
- tooling: CLI, Kubernetes operator, REST API.
- composes with: Webhook ingress only unless TCP tunnels are on the free plan.
- reliability: Client-rendered pricing makes the free tier hard to audit; the service is B2B and stable.
- notes: HTTP and TCP tunnels per the aggregator. The free plan appears to cover webhook forwarding rather than tunnels; that distinction was not readable today.
- evidence note: Free plan allowances and webhook forwarding limits are documented in official pricing guides.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: The pricing page read renders testimonials and no plan table; no free byte allowance could be read.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: title 'Pricing - Free Plan & Paid from $9.99/mo'; body contains testimonials only
  - [2] 2026-10-23: tunnel product exists; access tokens gate agents and CLI
  - [3] 2026-10-23: 'an account and paid plan are required for bidirectional tunnels' (third party)
- sources:
  - [1] https://webhookrelay.com/pricing/
  - [2] https://docs.webhookrelay.com/tunnels
  - [3] https://github.com/anderspitman/awesome-tunneling
