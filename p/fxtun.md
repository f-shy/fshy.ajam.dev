# fxTunnel

> fxtun.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fxtun/ | JSON https://fshy.ajam.dev/api/v1/entity/fxtun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## fxTunnel

- `egress/fxtunnel` | fails-egress | evidence documented | binding none | category tunnel | tier free
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://fxtun.dev/pricing
- price USD 0
- free tier: Free / 1 active tunnel / Any subdomain / 0 reserved subdomains / 0 own domains / 1 access key / HTTP Inspector / TCP - on paid plans / UDP - on paid plans | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bez limitov na zaprosy i trafik (no limits on requests or traffic) on all plans, and Bez taimauta sessiy (no session timeout).; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The free plan issues 1 access key, which implies an account. The signup form was not read, so the exact identity requirement (email, OAuth, card) is not established. | country: None
- interface: cli
- limits:
  - volume-quota: no request or traffic limit stated on any plan [1]
  - per-object-cap: 1 active tunnel and 1 access key on Free [1]
- binding note: Volume is not the blocker: the page promises no traffic limit on every plan. What fails at the first byte of a UDP workload is protocol support, because TCP and UDP are listed as paid-only. Payment is in RUB through YuKassa, which is an access constraint the English blog does not mention.
- interface detail: curl -fsSL https://fxtun.dev/install.sh | bash, then fxtunnel http 8080.
- tooling: Vendor CLI installed by curl from fxtun.dev/install.sh; no rclone or WireGuard integration is claimed.
- composes with: Useful only as an HTTP webhook endpoint in front of a free VM; it cannot carry UDP or a WireGuard handshake.
- reliability: Single-vendor service with a Russian billing provider and no published SLA; the plan matrix changed between the English copy and the live page, so entitlement can move under the account.
- notes: Conflict recorded and unresolved: the English blog at fxtun.dev says the free tier includes TCP and UDP and that the free tier has no limits; the live pricing page (fxtun.dev/pricing redirecting to fxtun.ru/pricing, updated September 2026) puts TCP and UDP on paid plans and gives Free a single HTTP tunnel. A search-index copy of an English version of fxtun.dev/pricing says three active HTTP and TCP tunnels with UDP on paid plans, a third variant. The live page is treated as current. Billing is in RUB via YuKassa on the page read.
- evidence note: Tunnel parameters, pricing and protocol support are documented in vendor product manuals.
- extras:
  - wg_path: none
  - wg_detail: The free plan carries HTTP and HTTPS only; the page lists TCP and UDP as paid-plan features, so no UDP transport exists on free to carry a WireGuard datagram.
  - ingress: http-only
  - volume_stated: Bez limitov na zaprosy i trafik (no limits on requests or traffic) on all plans, and Bez taimauta sessiy (no session timeout).
  - bytes_transit: yes
  - transit_note: The vendor edge relays the bytes; an outbound connection is opened to it.
- evidence:
  - [1] 2026-10-23: Free plan: 1 active tunnel, HTTP Inspector, TCP and UDP on paid plans only; all plans have no request or traffic limit. The read redirected to fxtun.ru/pricing, updated September 2026.
  - [2] 2026-10-23: The English blog claims the free tier has no limits on traffic, connections or agents and that the tool supports HTTP, TCP and UDP, which conflicts with the live pricing page.
- sources:
  - [1] https://fxtun.dev/pricing
  - [2] https://fxtun.dev/blog/free-ngrok-alternatives-2026/
