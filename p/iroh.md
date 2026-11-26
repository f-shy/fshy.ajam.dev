# iroh

> iroh.computer | Egress and tunnels, Storage; 7 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iroh/ | JSON https://fshy.ajam.dev/api/v1/entity/iroh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iroh public relays

- `egress/iroh-public-relay` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category relay (hosted, unmetered by claim)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:53.814Z (live) | stale on 2026-12-20
- url https://docs.iroh.computer/relays/rate-limiting
- free tier: four public relay regions, no authentication, rate-limited per connection | unit: unlimited | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: not applicable | source: [1]
- egress: no byte quota; a per-connection rate limit that is retuned | metered: no | source: [1]
- identity: anonymous | detail: no authentication on the public relays
- interface: unknown
- limits:
  - per-ip-shaping (binding): per connection, value not published and retuned as needed [1]
- binding note: The public relays are rate-limited per connection and the exact rate is not published, so an unpublished per-connection rate cap binds before any byte quota; no volume quota is stated.
- interface detail: the n0 public relay preset, spoken over QUIC
- tooling: iroh
- composes with: a zero-cost relay for the connections that fail to hole-punch, which makes it a redundancy layer rather than a capacity layer.
- reliability: the documentation says not to rely on the public relays for production
- notes: A relay that transits bytes is metered by definition, and this one meters rate rather than volume. No number, so no capacity claim.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: a relay that transits bytes when hole-punching fails, at a per-connection rate it does not publish
- evidence:
  - [1] 2026-10-22: 'The exact rate limits aren't published today, as they get tuned as needed', plus the warning that public relays are not for production workloads
  - [1] 2026-11-19: the first-party docs state a per-connection rate limit on public relays whose exact rate is not published | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: The exact rate limits aren't published today, as they get tuned as needed.
  - [1] 2026-11-19: the public relays are still per-connection rate-limited with an unpublished rate | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: The exact rate limits aren't published today, as they get tuned as needed.
- sources:
  - [1] https://docs.iroh.computer/relays/rate-limiting

## iroh public relays (n0.computer)

- `storage/iroh-public-relays` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category relay/P2P — SIGNALLING with encrypted fallback transport
- needs card no, phone no, ID no, institution no | verified 2026-11-25T13:25:55.252Z (live) | stale on 2026-12-10
- url https://docs.iroh.computer/iroh-services/relays/public
- free tier: iroh includes a set of public relays provided by n0.computer, available to all iroh users at no cost. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Relays are stateless and store nothing; no retention period applies to relayed traffic. | source: [1] | note: unverified: no data retention period stated for relayed traffic
- egress: Public relays are free, open to every iroh endpoint, and rate-limited to prevent abuse of shared infrastructure. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - per-ip-shaping (binding): unverified: Community rate is Variable; 5 MB/s belongs to the Pro shared-relay tier [1]
  - per-ip-shaping (binding): unverified: Community connections are Rate limited; 10,000 belongs to the Pro shared-relay tier [1]
- limits note: Not a storage provider. Only relayed bytes hit the operator, hence the per-connection rate limit rather than a byte quota.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: An iroh connection is just a QUIC connection, using TLS and TLS ALPNs for protocol negotiation.
- tooling: `iroh` crate; relay is a library, not a service with an upload endpoint
- composes with: In practice, roughly 9 out of 10 connections go direct; the relay is only a stepping stone.
- reliability: 'The exact rate limits aren't published today, as they get tuned as needed' and 'Do not rely on it for production workloads'. The free tier is explicitly capacity-unstable by design.
- notes: No storage. Free, no account, no card. Public relays are rate-limited per connection but the rate limits are deliberately unpublished. The paid Shared tier is the only one with published figures: 100 GB relayed egress/month then $0.09/GB, 5 MB/s, 10,000 concurrent connections.
- evidence note: the public relays are stated as free to all iroh users on the Public Relays page
- evidence:
  - [2] 2026-10-21: 'The exact rate limits aren't published today, as they get tuned as needed ... applied per connection'; 'Do not rely on it for production workloads'
  - [1] 2026-10-21: Free: 'Rate limited' / 'Variable'; Pro $19/mo: 10,000 connections, shared relays, 5 MB/s; Dedicated $199/mo/region: unlimited
  - [3] 2026-10-21: '100 GB of relay egress per month, then $0.09/GB'; 'A 5 MB/s rate limit'
  - [4] 2026-10-21: worked example: 2,000 users x 10 GB/mo; 'if 98% of the traffic could travel directly ... only the remaining 2% (400 GB) would pass through'
  - [5] 2026-11-09: public relays are provided to all iroh users at no cost | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: iroh includes a set of public relays provided by n0.computer, available to all iroh users at no cost.
  - [5] 2026-11-09: any iroh endpoint may use the public relays without authentication | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: Public relays are open to every iroh endpoint and need no authentication.
  - [3] 2026-11-09: the paid shared-relay plan carries a 5 MB/s rate limit | capture: sha256:7e089d822035ba29472f90f0ffef5063dc248532d438998e9931cba99cef7717 | quote: A 5 MB/s rate limit
  - [3] 2026-11-09: the paid shared-relay plan allows up to 10,000 concurrent connections | capture: sha256:7e089d822035ba29472f90f0ffef5063dc248532d438998e9931cba99cef7717 | quote: Up to 10,000 concurrent connections
  - [1] 2026-11-25: the pricing table gives Community Variable and Pro 5 MB/s | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Rate limit | Variable | 5 MB/s | Unlimited | Custom |
  - [1] 2026-11-25: the pricing table gives Community Rate limited and Pro 10,000 concurrent connections | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Concurrent connections | Rate limited | 10,000then $0.003/endpoint | 60,000 | Custom |
  - [6] 2026-11-25: the FAQ describes the relay as a stepping stone for most connections | capture: sha256:f866778d2f3535c75cf89a4cf2a88dc365c13f1f95614c1b929989ab764d575d | quote: In practice, roughly 9 out of 10 connections go direct; the relay is only a stepping stone.
  - [2] 2026-11-25: the public relays are free and rate-limited | capture: sha256:bab3908108462149cd92a7d3a40119a96b6fd782d6fb1c25f2856cb0332c35f7 | quote: The [public relays](https://docs.iroh.computer/iroh-services/relays/public.md) n0.computer runs are free, open to every iroh endpoint, and rate-limited to prevent abuse of shared infrastructure.
  - [6] 2026-11-25: the FAQ describes the iroh connection protocol | capture: sha256:f866778d2f3535c75cf89a4cf2a88dc365c13f1f95614c1b929989ab764d575d | quote: An iroh connection is just a QUIC connection, using TLS and TLS ALPNs for protocol negotiation.
  - [6] 2026-11-25: relays do not store routed traffic | capture: sha256:f866778d2f3535c75cf89a4cf2a88dc365c13f1f95614c1b929989ab764d575d | quote: Because relays are stateless (they route encrypted packets but store nothing), they're cheap to run and easy to scale.
  - [5] 2026-11-25: public relays are available to all users at no cost | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: iroh includes a set of public relays provided by n0.computer, available to all iroh users at no cost. No setup required; they work out of the box.
  - [5] 2026-11-25: public relays need no account or authentication | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: Public relays are open to every iroh endpoint and need no authentication.
  - [2] 2026-11-25: the public relays are explicitly not for production workloads | capture: sha256:bab3908108462149cd92a7d3a40119a96b6fd782d6fb1c25f2856cb0332c35f7 | quote: This means that public infrastructure is meant for development and hobby use. Do not rely on it for production workloads, especially if your application is sensitive to rate limiting, uptime, or relay software version.
- sources:
  - [1] https://www.iroh.computer/pricing
  - [2] https://docs.iroh.computer/relays/rate-limiting
  - [3] https://docs.iroh.computer/iroh-services/relays/shared
  - [4] https://www.iroh.computer/blog/shared-relays
  - [5] https://docs.iroh.computer/iroh-services/relays/public
  - [6] https://docs.iroh.computer/about/faq

## iroh n0 public relays

- `storage/iroh-n0-public-relays` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:26.450Z (live) | stale on 2026-12-05
- url https://docs.iroh.computer/relays/rate-limiting
- free tier: Community plan, $0 per month: public relays in US, EU and Singapore, rate-limited traffic, no uptime guarantees, no auth; the rate limit is not published | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Public relays are rate-limited per connection with no published limit; the pricing page lists egress and rate limit as 'Variable'. Paid routes: Pro $19/month has a 5 MB/s rate limit and 100 GB egress then $0.09/GB; Dedicated adds $199/month per region with no rate limits and 250 GB egress then $0.09/GB. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free public relays: rate-limited traffic with an unpublished limit, no uptime guarantees, development and hobby use only; no published limit supports 1 TiB a day. The paid Dedicated route has no rate limit and bills $0.09/GB beyond 250 GB.
- notes: the same as reliability
- evidence note: documented from vendor pages read on 2026-11-03: the plan rates and egress (https://www.iroh.computer/pricing), and the rate limiting and hobby-use statements (https://docs.iroh.computer/iroh-services/relays/public and https://docs.iroh.computer/relays/rate-limiting). Identity, retention and per-object cap were not read.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free tier is 'rate-limited traffic' with 'No uptime guarantees' and the exact limits are deliberately unpublished ('The exact rate limits aren't published today, as they get tuned as needed'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free tier is 'rate-limited traffic' with 'No uptime guarantees' and the exact limits are deliberately unpublished 'The exact rate limits aren't published today, as they get tuned as needed'
  - [2] 2026-10-21: cited as the basis of the rejection: Free tier is 'rate-limited traffic' with 'No uptime guarantees' and the exact limits are deliberately unpublished 'The exact rate limits aren't published today, as they get tuned as needed'
  - [3] 2026-10-21: cited as the basis of the rejection: Free tier is 'rate-limited traffic' with 'No uptime guarantees' and the exact limits are deliberately unpublished 'The exact rate limits aren't published today, as they get tuned as needed'
  - [2] 2026-11-03: rate limit per plan: Variable on Community, 5 MB/s on Pro, Unlimited on Dedicated | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Rate limit | Variable | 5 MB/s | Unlimited | Custom |
  - [2] 2026-11-03: egress per plan: Variable on Community, 100 GB then $0.09/GB on Pro, 250 GB then $0.09/GB on Dedicated | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Egress | Variable | 100 GBthen $0.09/GB | 250 GBthen $0.09/GB | Custom |
  - [3] 2026-11-03: public relay traffic is rate-limited | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: Traffic is rate-limited to prevent abuse
  - [3] 2026-11-03: public relays are for development and hobby use only | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: Public relays are suitable for development and hobby use only.
  - [1] 2026-11-03: dedicated relays have no rate limits | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: dedicated relays remove rate limits entirely
  - [1] 2026-11-03: the public relays' rate limit has no published number | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: The exact rate limits aren't published today, as they get tuned as needed.
  - [2] 2026-11-03: the Community plan lists rate-limited traffic | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: Rate-limited traffic
  - [2] 2026-11-03: the Community plan row of the public relays carries no egress price and no volume quota; the $0.09/GB figures are on Pro and Dedicated | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Egress | Variable | 100 GBthen $0.09/GB | 250 GBthen $0.09/GB | Custom |
  - [1] 2026-11-03: the public relays' limit is a per-connection throttle, not a volume quota or a price | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: Rate limiting is a property of a single relay connection, not a global switch.
  - [3] 2026-11-03: the public relays have no price | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: available to all iroh users at no cost
  - [2] 2026-11-04: rate limit per plan: Variable on Community, 5 MB/s on Pro, Unlimited on Dedicated | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: | Rate limit | Variable | 5 MB/s | Unlimited | Custom |
  - [1] 2026-11-04: the public relays' rate limit has no published number | capture: sha256:962e4513e4dc6427b10423f4f41cdcb15196dba2bc4246ec17cd668e64d660cd | quote: The exact rate limits aren't published today, as they get tuned as needed.
  - [3] 2026-11-04: public relays are for development and hobby use only | capture: sha256:268dee5a141ea15ee40a7018f29bc473de3fb70f56c3c3a8a44fb1a9d0b8ecee | quote: Public relays are suitable for development and hobby use only.
- sources:
  - [1] https://docs.iroh.computer/relays/rate-limiting
  - [2] https://www.iroh.computer/pricing
  - [3] https://docs.iroh.computer/iroh-services/relays/public

## iroh Services — Community (free tier)

- `storage/iroh-services-community` | fails-egress | evidence reported | binding none | category Hosted coordination service (relays + metrics + diagnostics) — NOT storage
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:03.170Z (live) | stale on 2026-12-04
- url https://www.iroh.computer/pricing
- free tier: 0 bytes of storage. Free plan = public relays in US/EU/Singapore, 7-day metrics retention, no auth, rate-limited traffic, no uptime guarantee. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Free plan = public relays in US/EU/Singapore, 7-day metrics retention, no auth, rate-limited traffic, no uptime guarantee | days: 7 | source: [1] | note: not stated
- egress: Variable / unpublished (inherits public relay limits). | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Relay only. There is no pinning service, no blob hosting, no object storage SKU anywhere in n0's product line. The entire product is coordination plus egress.
- interface detail: Dashboard at services.iroh.computer + `iroh-services` crate; account is username + email + password.
- tooling: `iroh_services::Client` pushes endpoint metrics on an interval; net-diagnostics can dial back into your endpoint (requires granting `Caps::net_diagnostics_get_any()`).
- composes with: Free tier covers signalling and discovery for an unlimited number of endpoints. Which is exactly the part a self-hosted origin needs. It contributes nothing to bytes at rest or bytes served.
- reliability: Free tier requires an account only to see metrics; the relays themselves need no account at all.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 0 bytes of storage. Free plan = public relays in US/EU/Singapore, 7-day metrics retention, no auth, rate-limited traffic, no uptime guarantee.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: plan table: Free/Pro $19/Dedicated $199 per region/Enterprise; rows are Connections, Relays, Rate limit, Egress, Auth, Custom DNS, Metrics, Support. No storage row exists.
  - [2] 2026-10-21: Public free / Cloud $19+ / Open Source self-host. 'Hosting' here means relays and discovery.
  - [3] 2026-10-21: signup form is username + email + password (no card, no institution)
  - [1] 2026-11-19: the Community plan is free public relays with 7-day metrics retention and no storage | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: - Public relays in US, EU, Singapore - 7 day metrics retention - No auth, public only - Rate-limited traffic - No uptime guarantees
  - [3] 2026-11-19: the signup form asks for username, email and password and no card or phone | capture: sha256:0d174b6b6f7b0868caa24b1a3d5060d05053872d0963b9a762ce345e3f02acdc | quote: Username Email Address Choose a Password
- sources:
  - [1] https://www.iroh.computer/pricing
  - [2] https://www.iroh.computer/services/hosting
  - [3] https://services.iroh.computer/

## ipfs / shipyard

- `storage/ipfs-shipyard` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.853Z (live) | stale on 2026-12-04
- url https://www.iroh.computer/blog/iroh-global-content-discovery
- free tier: None reachable: The IPFS pinning lane is closing, not opening. And free IPFS pinning was already excluded at <=6 GB in earlier waves. iroh's own blog frames Mainline+blake3.net as the successor, which is w. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The IPFS pinning lane is closing, not opening — and free IPFS pinning was already excluded at <=6 GB in earlier waves. iroh's own blog frames Mainline+blake3.net as the successor, which is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The IPFS pinning lane is closing, not opening — and free IPFS pinning was already excluded at <=6 GB in earlier waves. iroh's own blog frames Mainline+blake3.net as the successor, which is…
  - [1] 2026-10-21: the iroh post the record cites is the source of the name; the provider name keeps the service and drops a personal note
  - [1] 2026-11-19: the IPFS pinning service shipyard is shutting down | capture: sha256:3a5cc6e430f0c5303387a8f85464f7051db06761cd74c10ae7362cbebafbdd81 | quote: IPFS shipyard is shutting down
  - [1] 2026-11-19: the iroh post frames Mainline plus blake3.net as the successor to shipyard pinning | capture: sha256:3a5cc6e430f0c5303387a8f85464f7051db06761cd74c10ae7362cbebafbdd81 | quote: This does not mean that IPFS will stop working, but it does not bode well for the future of the project.
- sources:
  - [1] https://www.iroh.computer/blog/iroh-global-content-discovery

## iroh Shared relay

- `egress/iroh-shared-relay` | fails-quota | evidence documented | binding volume-quota | category relay (metered, QUIC)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:04:40.149Z (live) | stale on 2026-12-26
- url https://docs.iroh.computer/iroh-services/relays/shared
- free tier: 100 GB relay egress per month, 10,000 concurrent connections, 5 MB/s rate | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a monthly allowance
- retention: not applicable | source: [1]
- egress: metered at 100 GB/month, which is 3.3 GB/day | metered: yes | free allowance: 100 GB/month | price per TB: USD 0.09/GB | source: [1]
- identity: email | detail: an n0 account and an API key
- interface: unknown
- limits:
  - per-ip-shaping: 5 MB/s rate limit per shared-relay connection [1]
  - volume-quota (binding): 100 GB of relay egress per month, then USD 0.09/GB [1]
- limits note: the allowance is a byte volume over a period, which none of the six kinds names; the number is in egress.free_allowance and binding names per-ip-shaping as the nearest kind
- binding note: the monthly byte allowance in egress.free_allowance is what runs out, and no kind in the six-value vocabulary names a byte volume over a period counted per account. per-ip-shaping is the closest, because it is the only kind that bounds a volume, and its subject here is the account rather than the caller's address
- interface detail: an iroh relay URL attached to a project, spoken over QUIC
- tooling: part of interface detail
- composes with: the paid fallback for the 7-10% of iroh connections that fail to hole-punch; it composes with the transport and not with a free budget.
- reliability: the allowance is a 30-day trial rather than a persistent free tier
- notes: The free public relays are a separate product with deliberately unpublished limits.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the paid relay transits bytes, which is why it meters them at 100 GB per month
- evidence:
  - [1] 2026-10-22: up to 10,000 concurrent connections, 100 GB relay egress per month then USD 0.09/GB, a 5 MB/s rate limit, and a 30-day trial on Pro
  - [1] 2026-11-25: the shared-relay page states a 100 GB monthly egress allowance | capture: sha256:81828ff88f339880ea478f7652cb36c6c7bda83c4942dccd75d23ed713756605 | quote: * 100 GB of relay egress per month, then \$0.09/GB
  - [1] 2026-11-25: the shared-relay page states a 5 MB/s rate limit | capture: sha256:81828ff88f339880ea478f7652cb36c6c7bda83c4942dccd75d23ed713756605 | quote: * A 5 MB/s rate limit
  - [1] 2026-11-25: the page documents relay access through the iroh client library, which the interface vocabulary has no token for | capture: sha256:81828ff88f339880ea478f7652cb36c6c7bda83c4942dccd75d23ed713756605 | quote: The Rust example uses [`iroh-services`](https://crates.io/crates/iroh-services).
- sources:
  - [1] https://docs.iroh.computer/iroh-services/relays/shared

## n0 hosted blob pinning / storage service

- `storage/n0-hosted-blob-pinning-storage-service` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:39.878Z (live) | stale on 2026-12-04
- url https://www.iroh.computer/pricing
- free tier: none reachable: Does not exist. n0 sells coordination (relays, metrics, diagnostics) and never bytes at rest. Checked the pricing table, the hosting page, the services dashboard, the org's 100-repo… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Does not exist. n0 sells coordination (relays, metrics, diagnostics) and never bytes at rest. Checked the pricing table, the hosting page, the services dashboard, the org's 100-repo…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Does not exist. n0 sells coordination (relays, metrics, diagnostics) and never bytes at rest. Checked the pricing table, the hosting page, the services dashboard, the org's 100-repo listing
  - [2] 2026-10-21: cited as the basis of the rejection: Does not exist. n0 sells coordination (relays, metrics, diagnostics) and never bytes at rest. Checked the pricing table, the hosting page, the services dashboard, the org's 100-repo listing
  - [3] 2026-10-21: cited as the basis of the rejection: Does not exist. n0 sells coordination (relays, metrics, diagnostics) and never bytes at rest. Checked the pricing table, the hosting page, the services dashboard, the org's 100-repo listing
  - [1] 2026-11-19: the Community tier sells public relays and metrics, not bytes at rest; no storage offer exists | capture: sha256:677a58c510e73c87a15e93ac568bdfb3937e2fa45690b989fa9ad94c9260551a | quote: No auth, public only
- sources:
  - [1] https://www.iroh.computer/pricing
  - [2] https://www.iroh.computer/services/hosting
  - [3] https://docs.iroh.computer/iroh-services/relays/shared
