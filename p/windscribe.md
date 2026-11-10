# Windscribe

> windscribe.com | IP and proxies, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/windscribe/ | JSON https://fshy.ajam.dev/api/v1/entity/windscribe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Windscribe (paid)

- `ip-proxy/windscribe-vpn` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category VPN subscription (exit source) | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-24T10:07:11.000Z (live) | stale on 2026-11-24
- url https://windscribe.com/upgrade
- price USD 9.00 per month list; USD 39 per year on sale; static IP USD 24 per year data centre and USD 96 per year residential | parsed USD 9/mo
- free tier: Free plan carries 2 to 10 GB per month and is reachable with no card. Paid plan is USD 9.00 per month list, or USD 39 per year on sale. | unit: GB | metered on: unstated | read on: 2026-10-24 | source: [1] | note: Vendor documentation specifies a free allowance between 2 and 10 GB per month without explicitly distinguishing transfer direction. metered_on is unstated.
- per-object cap: not applicable | source: [2]
- retention: not applicable: an address, not an object | source: [2] | note: The address is held for as long as the subscription that carries it; the facts give no term, so no number is recorded.
- egress: Paid plans are sold by the month and the facts record no byte cap on them; the free plan is quota'd at 2 to 10 GB per month. The vendor's own words on the address: We do not offer dedicated IPs for privacy reasons ... we allocate a single IP address to a handful of customers, so your activity can still be lost in the crowd. | metered: no | free allowance: free plan: 2 to 10 GB per month; no byte cap published for the paid plan in the facts this record rests on | source: [2]
- identity: email | detail: Email registration. The free plan is reached with no card, and the paid plan and any static IP are bought against that account. The facts record no phone, no card at signup and no national identity.
- interface: rest
- limits:
  - volume-quota: Free plan provides 2 to 10 GB per month. [1]
  - per-ip-shaping (binding): no dedicated IP is sold: we allocate a single IP address to a handful of customers, so a static IP is a shared address and any per-IP limit or reputation at the destination applies to the whole group [2]
- limits note: Two constraints the vocabulary does not name. First, the residential static is sold in three cities only (Chicago, Dallas, Toronto), so the residential option is a location choice rather than a pool. Second, the 58 ASNs are unevenly weighted: AS212238 Datacamp holds 62 of the 239 /24s, 26% of the pool, so a selection that does not spread deliberately will over-sample one network. The 239 /24s count is primary IPs only, so secondary addresses on the same servers are not in it.
- binding note: The free byte quota is real but is resolved by paying USD 9.00 a month, so it is not what fails at 45 GB/month; what remains is that no customer can hold a private address, because the vendor allocates one IP to a handful of customers, so destination-side per-IP limits and reputation apply to every caller sharing the address, and the 599,000 requests a month are what meet them.
- interface detail: The only programmatic surface the facts establish is the published server list, an HTTPS JSON document at https://assets.windscribe.com/serverlist/openvpn/1/1, whose path names the OpenVPN config family.
- tooling: A program would read the published server list and select exits from it itself, then hold a tunnel with the vendor's own client or a config generated from the account. No wrapper is named in the facts, and a missing wrapper is a tooling note rather than a rejection: the resource exists and the selection layer is the part that has to be written.
- composes with: Sits in front of the Workers AI gateway as the exit for requests that must leave from a named network: a /24 drawn from the 58-ASN pool for breadth across carriers, or the residential static in one of three cities when a residential-looking address matters more than choice of network.
- reliability: No dedicated address by design: a static IP is one address allocated to a handful of customers, so a block or a challenge aimed at that address is shared with them, and the largest single ASN carries 26% of the pool so an undirected selection can land on one network repeatedly.
- notes: What was considered. All three hold, and the caveat is the same for each: nothing here is exclusive. The decisive sentence settles what a buyer gets, and it is the vendor's own: we allocate a single IP address to a handful of customers. A static IP therefore buys stability of address, not privacy of address, and it does not buy an address nobody else uses. Ruled out as a reason to reject: that no wrapper exists for the server list, which is a tooling note, and that the residential static covers three cities, which is a scope limit recorded in limits_note rather than a defect. The static IP prices are USD 24 per year for a data centre address and USD 96 per year for a residential one, read from windscribe.com/staticips on 2026-10-24, so the egress record's unknown is answered and its cheapest-stable-address figure should read USD 24 per year plus the subscription. On the annual price the two records disagree and this one does not resolve it: the egress record read USD 69 per year, this record reads USD 39 per year on sale, and a sale price and a list annual price are both possible readings of a page that shows one number at a time. The disagreement is recorded here rather than smoothed, because the cheaper of the two is the one a reader would act on. What rests on one sample. The whole ASN figure is one fetch of one document on one day. It measures what the vendor publishes, not what answers on connect: a server listed in 58 ASNs can still route a given session through one of them, and the record cannot show that a client choosing an ASN actually lands in it. That gap is what a probe would close, and it is the reason the ASN claim is stated as a property of the published list everywhere it appears rather than as a property of a connection. The 239 /24s count is also primary IPs only, so it is a floor on the address count, not the count. The ASN-per-dollar comparison is the source facts' own sentence: 58 ASNs for USD 5.75 a month is the best ratio found. The per-month figure is not stated anywhere in this record's evidence and its basis is not given, so it is carried as a comparison attributed to the facts rather than as a number this record computed; the annual rates the evidence does carry are USD 39 on sale and USD 69 in the sibling record. The claim that the residential static at USD 96 per year is the only residential static exit sold at a published price is likewise the facts' claim about a search, not a finding of this record, and it can only be falsified by another vendor publishing one. The interface token mismatch is a defect in the repository, not in the provider. This record was asked for tokens api, cli, rest, socks5, http-proxy, wireguard, openvpn, web-ui or none; The truthful member of the enumerated set is rest, for the published server list, and the protocol and client surface are in interface_detail and extras so nothing is lost. The token list wants a topic-shaped enum before the next ip-proxy record is written. The three evidence URLs arrived as a set. This record maps the plan prices to /upgrade, the static IP prices and the allocation sentence to /staticips, and the ASN counts to the server list.
- evidence note: The ASN diversity is measured, from the published server list on 2026-10-24, and is the strongest field here. The verdict also rests on the price and on email-only registration, both read from vendor pages, so documented is the weakest rung that decides it. Moving up would need a connection made from the pool and a request and byte count taken through it.
- extras:
  - rung: 4
  - rung_note: The pool is characterised at the ASN rung, 239 /24s across 58 distinct ASNs measured from the published server list on 2026-10-24; registration class is rung 5 and is recorded as email, but it does not decide the verdict here because an email costs nothing.
  - rung_registration: 5
  - prefix_count: 239
  - prefix_scope: primary IP only
  - asn_count: 58
  - largest_asn: AS212238 Datacamp, 62 /24s, 26% of the pool
  - eyeball_asns_confirmed: AS45899 VNPT; AS9318 SK Broadband; AS3786 LG DACOM; AS3216 Vimpelcom; AS1257 Tele2; AS6866 Cyta
  - measured_on: 2026-10-24
  - measurement_source: https://assets.windscribe.com/serverlist/openvpn/1/1
  - measurement_limit: a property of the published server list, not of a connection made from it
  - static_ip_datacenter_usd_year: 24
  - static_ip_residential_usd_year: 96
  - static_ip_residential_cities: Chicago, Dallas, Toronto
  - decisive_quote: We do not offer dedicated IPs for privacy reasons ... we allocate a single IP address to a handful of customers, so your activity can still be lost in the crowd.
  - decisive_quote_source: https://windscribe.com/staticips
  - asn_per_dollar: 58 ASNs for USD 5.75 a month is the best ASN-per-dollar ratio found; the basis of the per-month figure is not stated in this record's evidence
  - interface_enum_gap: protocol and client surface are recorded here instead
- evidence:
  - [1] 2026-10-24: The prices this record is priced at: USD 9.00 per month list and USD 39 per year on sale, and the free plan's 2 to 10 GB per month reachable with no card.
  - [2] 2026-10-24: Static IP add-on prices, USD 24 per year for a data centre address and USD 96 per year for a residential address, sold in three cities, and the allocation rule quoted in egress.terms: no dedicated IPs, one IP shared by a handful of customers.
  - [3] 2026-10-24: Measured exit diversity: 239 /24s on primary IPs only, spread across 58 distinct ASNs, largest AS212238 Datacamp at 62 /24s or 26%, with eyeball carriers AS45899 VNPT, AS9318 SK Broadband, AS3786 LG DACOM, AS3216 Vimpelcom, AS1257 Tele2 and AS6866 Cyta present.
- sources:
  - [1] https://windscribe.com/upgrade
  - [2] https://windscribe.com/staticips
  - [3] https://assets.windscribe.com/serverlist/openvpn/1/1

## Windscribe (pro)

- `egress/windscribe` | paid-only | evidence documented | binding retention-clamped | category vpn port forward | tier pro
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:29:40.635Z (live) | stale on 2026-12-05
- url https://windscribe.com/features/port-forwarding
- price USD 9 per month; USD 69 per year; static IP charged separately | parsed USD 9/mo
- free tier: Port forwarding is only included on Windscribe's paid plans. The free plan carries 2 GB per month, or 10 GB per month with a confirmed email, and reaches servers in 10 countries, not all locations. Pro: $9/month or $69/year ($5.75/month). | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Users get unlimited bandwidth to use and can connect to all 69+ countries. This also provides access to all features including the fully customizable R.O.B.E.R.T., port forwarding, as well as custom configs for all locations.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An account for any persistent configuration; the free tier is reachable without payment and the site advertises No credit card, no logs, no catch. | country: None
- interface: cli
- limits:
  - retention-clamped (binding): ephemeral port lasts 7 days: The Windscribe Pro Plan includes support for ephemeral port forwarding, which lasts for 7 days at a time. All users requesting ephemeral port forwarding configurations will be granted one for 1 week before being cleared out. [1]
  - write-gated: a permanent port requires a separately charged static IP: If you prefer a permanent port, you can get one with a static IP charged separately to a Pro subscription. [1]
- binding note: Volume does not bind because Pro is unlimited. What fails first is the 7-day reclaim: the port is explicitly cleared and reissued, so a long-running service loses its address weekly unless a static IP is bought on top of Pro.
- interface detail: Dashboard request for a port; configs downloaded from the account. Protocols: WireGuard, OpenVPN (UDP or TCP), IKEv2, Stealth and WStunnel. Obfuscation: Stealth and WStunnel, plus a Circumvent Censorship option. Hosted SOCKS5 servers were discontinued; desktop apps host a local SOCKS5 or HTTP proxy through Proxy Gateway. P2P is allowed except on locations marked with a crossed-out P2P label.
- tooling: Official app and account dashboard; WireGuard custom configs on Pro.
- composes with: Useful as a short-lived test endpoint for a free VM; not a fixed address without the static IP add-on.
- reliability: Port reclaimed every 7 days by design; a client that does not re-request loses ingress with no error at the service.
- notes: The static IP is the real product for ingress here, and its price is on a separate page that did not read, so the cheapest stable-port figure for Windscribe is unknown rather than zero. A 7-day port is enough for a demo and not enough for a service with a DNS record.
- evidence note: Measured would need a Pro account and a byte count. The 7-day reclaim sentence is the vendor's own FAQ answer, read.
- extras:
  - wg_path: native-conf
  - wg_detail: Custom configurations are a Pro feature per the pricing article: access to all features including the fully customizable R.O.B.E.R.T., port forwarding, as well as custom configs for all locations. The port itself is requested from the account dashboard.
  - ingress: tcp+udp
  - volume_stated: Users get unlimited bandwidth to use and can connect to all 69+ countries. This also provides access to all features including the fully customizable R.O.B.E.R.T., port forwarding, as well as custom configs for all locations.
  - bytes_transit: yes
  - transit_note: Traffic crosses Windscribe servers on the chosen location.
- evidence:
  - [1] 2026-10-23: Port forwarding is Pro only, ephemeral ports last 7 days, a permanent port needs a static IP add-on, and free plans get no forwarding.
  - [2] 2026-10-23: Pro is $9 per month or $69 per year and includes port forwarding; the free plan carries 2 to 10 GB per month.
  - [3] 2026-10-23: The free tier exists with no card and 10 global locations, which is why the paid tier is the one that forwards.
  - [2] 2026-11-04: Pro is $69 per year | capture: sha256:50171ce5e9b3a93850a8a55c49aa6ea0912b635e65f0ce3682954b6a67563cad | quote: Pro can be purchased for $9/month on a monthly basis or $69/year ($5.75/month) on a yearly plan.
  - [4] 2026-11-04: Windscribe offers six protocols incl. OpenVPN over UDP and TCP | capture: sha256:f44b2bc9332898dcc120b8ec14b0232104acd2a1c08246997899eb089824936a | quote: Six connection protocols: WireGuard, OpenVPN (UDP/TCP)
  - [5] 2026-11-04: hosted SOCKS5 is discontinued | capture: sha256:4d4ecbef6b4b98ebd56d7281179b54bc983e8cc6c622469835aa305f2d3813cf | quote: As of April 30, 2022 Windscribe no longer supports or hosts SOCKS5 servers.
  - [5] 2026-11-04: Proxy Gateway hosts a SOCKS5 server on the user's machine | capture: sha256:4d4ecbef6b4b98ebd56d7281179b54bc983e8cc6c622469835aa305f2d3813cf | quote: Our desktop apps support the Proxy Gateway feature, which allows you to setup your own SOCKS5 server, right on your machine that's running Windscribe.
  - [6] 2026-11-04: WStunnel is an obfuscation protocol alongside Stealth | capture: sha256:5e3659bd51b33b94a8718e814c43b82cac49baad8130b38895d38c8a739be0ea | quote: This protocol is very similar to Stealth but has its own nuances.
  - [7] 2026-11-04: Circumvent Censorship obfuscates WireGuard, OpenVPN and Stealth | capture: sha256:52421c388d6c07ff5bc1ce9ca9a20477f256ef257ab65ce978930bb219752d3a | quote: Applies protocol-level adjustments for [WireGuard®](https://windscribe.com/features/flexible-connectivity/), OpenVPN, and Stealth
  - [8] 2026-11-04: torrenting is allowed except on marked locations | capture: sha256:b08f50592d2266f0d1a2c3182a0a11e81ae322a383be46777651daefa9859d6f | quote: Locations that do not allow torrenting are marked with a crossed-out
  - [2] 2026-11-04: Free reaches 10 countries and is capped at 10 GB per month with a confirmed email | capture: sha256:50171ce5e9b3a93850a8a55c49aa6ea0912b635e65f0ce3682954b6a67563cad | quote: Free users can access servers in 10 different countries and with a confirmed email address, with data usage capped at 10GB/month.
  - [3] 2026-11-04: Free is 10 country servers with no card required | capture: sha256:5e9a3766efc1ecadf07458145b795a06528dd2040eb2be106373721d6b9eab19 | quote: Either way, it's 10 country servers, unlimited devices on one account, and no card unless you want to.
- sources:
  - [1] https://windscribe.com/features/port-forwarding
  - [2] https://windscribe.com/knowledge-base/articles/how-much-does-it-cost-to-use-windscribe
  - [3] https://windscribe.com/features/use-for-free
  - [4] https://windscribe.com/llm-info
  - [5] https://windscribe.com/knowledge-base/articles/why-was-socks5-discontinued
  - [6] https://windscribe.com/knowledge-base/articles/what-is-the-wstunnel-protocol
  - [7] https://windscribe.com/features/circumvent-censorship
  - [8] https://windscribe.com/knowledge-base/articles/how-to-use-windscribe-with-deluge
