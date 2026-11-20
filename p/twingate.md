# Twingate

> twingate.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/twingate/ | JSON https://fshy.ajam.dev/api/v1/entity/twingate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Twingate

- `egress/twingate` | fails-egress | evidence documented | binding request-rate | category zero trust access (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.twingate.com/pricing
- price USD 0
- free tier: Starter: 'Free per user / month', 'Up to 5 users'. | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published; the plan is priced per user.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a Twingate account at auth.twingate.com | country: None
- interface: cli
- limits:
  - request-rate (binding): The only published meter is the 5-user cap, and the vocabulary has no token for an identity count; request-rate is the nearest. It is also moot: with no public ingress there is no 1 TiB/month to spend. [1]
- binding note: The only published meter is the 5-user cap, and the vocabulary has no token for an identity count; request-rate is the nearest. It is also moot: with no public ingress there is no 1 TiB/month to spend.
- interface detail: the Twingate client on each device and the Connector in the private network
- tooling: Twingate client and Connector
- composes with: carries nothing on its own; it is a private access layer, so it composes with a public ingress rather than replacing one
- reliability: Relays carry traffic only when peer-to-peer fails, and the free plan is bounded by users rather than bytes
- notes: Fails the ingress test by design: every path needs a Twingate client and an ACL issued by the Controller. The Connector does proxy 'TCP and UDP traffic for protected Resources', which is why UDP appears in the product and still carries nothing to a public reader.
- evidence note: A live attempt to reach a Resource without the Twingate client would confirm the private-only claim.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard. 'A user is responsible for establishing an encrypted tunnel with the appropriate Connector to access a protected Resource. This TLS tunnel is established based on the anonymous, unique Connector ID'. No .conf exists.
  - ingress: none
  - volume_stated: No byte allowance is published; the plan is priced per user.
  - bytes_transit: unknown
  - transit_note: peer-to-peer between client and Connector where possible, with a Relay as backup
- evidence:
  - [1] 2026-10-23: Starter is 'Free per user / month' with 'Up to 5 users'
  - [2] 2026-10-23: 'The Connector is intended to be deployed behind the firewall of a private Remote network'; the client-to-connector path is a 'certificate-pinned TLS tunnel'
- sources:
  - [1] https://www.twingate.com/pricing
  - [2] https://www.twingate.com/docs/how-twingate-works
