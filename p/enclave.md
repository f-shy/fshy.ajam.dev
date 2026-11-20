# Enclave

> enclave.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/enclave/ | JSON https://fshy.ajam.dev/api/v1/entity/enclave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Enclave

- `egress/enclave` | fails-egress | evidence documented | binding request-rate | category zero trust overlay (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://enclave.io/pricing/
- price USD 8 per system per month
- free tier: 'Enclave is free for personal and home use for up to 5 systems.' | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published; the plan is priced per enrolled system at USD 8.00 per system per month MSRP.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a licence key applied to each enrolled system; contact sales for discounts, so the signup is an email and a key | country: None
- interface: cli
- limits:
  - request-rate (binding): The 5-system cap is the only free meter and the vocabulary has no token for a device count, so request-rate is the nearest. It is moot for this test: there is no public ingress to spend 1 TiB through. [1]
- binding note: The 5-system cap is the only free meter and the vocabulary has no token for a device count, so request-rate is the nearest. It is moot for this test: there is no public ingress to spend 1 TiB through.
- interface detail: agent install plus a licence key
- tooling: the Enclave agent; no .conf documented
- composes with: a private overlay for a private set of machines, so it sits behind whatever public ingress is chosen
- reliability: the licence key is per system; a sixth system stops enrolling rather than throttling
- notes: Zero-trust overlay network designed for private mesh connectivity with closed inbound ports.
- evidence note: Closed firewall design and outbound-only connectivity model are documented in product technical specifications.
- extras:
  - wg_path: unknown
  - wg_detail: The pricing page names no tunnelling protocol, and no protocol page was read, so whether a .conf can be derived is open. The agent model is stated: 'An enrolled system is counted as a single machine, device, computer or container on which the Enclave agent software has been installed'.
  - ingress: none
  - volume_stated: No byte allowance is published; the plan is priced per enrolled system at USD 8.00 per system per month MSRP.
  - bytes_transit: overlay-only
  - transit_note: peer-to-peer between enrolled systems through the Trust Broker's policy
- evidence:
  - [1] 2026-10-23: 'Enclave is free for personal and home use for up to 5 systems'; USD 8.00 per enrolled system per month MSRP
  - [1] 2026-10-23: 'cloaking systems via a Trust Broker that verifies the identity, context and policy for each user' and 'firewalls are closed; no more access control lists or public VPN servers'
- sources:
  - [1] https://enclave.io/pricing/
