# Proxidize

> proxidize.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxidize/ | JSON https://fshy.ajam.dev/api/v1/entity/proxidize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxidize

- `ip-proxy/proxidize-mobile` | fails-identity | evidence documented | binding volume-quota | category mobile proxy | tier mobile proxy: per-GB metered and per-proxy monthly, both sold on the same page
- needs card no, phone no, ID yes, institution no | verified 2026-10-24T10:07:11.000Z (live) | stale on 2026-11-24
- url https://proxidize.com/mobile-proxy-pricing/
- price not quoted per TB: USD 2.00 per GB flat metered, or USD 59 per proxy per month with a 50 GB fair-use threshold
- free tier: No free tier on the cited pages. Per GB USD 2.00 flat, sold in blocks: USD 50/25 GB, USD 100/50 GB, USD 200/100 GB, USD 400/200 GB. Per proxy USD 59/proxy/month with unlimited bandwidth and a 50 GB fair-use threshold per proxy per month. | unit: mixed | metered on: unstated | read on: 2026-10-24 | source: [1] | note: Two units on one page: the per-GB plan is denominated in GB, the per-proxy plan in proxies per month with a byte threshold attached. Neither page says which direction the GB counts, hence metered_on unstated.
- per-object cap: not applicable: a proxy endpoint, not an object | source: [1] | note: The nearest thing to a per-object ceiling is the 50 GB fair-use threshold per proxy per month, recorded in limits[].
- retention: not applicable: a live proxy session, not stored bytes | source: [1]
- egress: Per-proxy plan: unlimited bandwidth, qualified by a 50 GB fair-use threshold per proxy per month. Per-GB plan: the traffic is the product, USD 2.00/GB flat in prepaid blocks of 25, 50, 100 and 200 GB. | metered: yes | free allowance: 50 GB per proxy per month on the USD 59/proxy/month plan; none on the per-GB plan, where every GB is bought | price per TB: not quoted per TB: the vendor's unit is USD 2.00 per GB flat | source: [1]
- identity: national-id | detail: KYC is mandatory before first use: You must complete identity verification (Tier 1) before you can use the proxies. The check is a document check against a national id, so the account is bound to one named person. The tier label implies further levels above Tier 1; those were not read. No second gate such as a card is recorded on the cited pages.
- interface: unknown
- limits:
  - volume-quota (binding): 50 GB fair-use threshold per proxy per month on the USD 59/proxy/month unlimited-bandwidth plan [2]
  - volume-quota (binding): USD 2.00 per GB flat, prepaid in blocks of 25 GB (USD 50), 50 GB (USD 100), 100 GB (USD 200) and 200 GB (USD 400): bytes past a block are another purchase [1]
- limits note: The national-id KYC gate is a real constraint but is not one of the seven limit kinds; it lives in identity_cost and is the reason for the verdict. No request-rate, per-IP-shaping or pull-count limit appears on the three pages read.
- binding note: At 45 GB a month the byte meter is the only constraint the pages state, and it fails first: one proxy's 50 GB fair-use ceiling covers the workload with 5 GB of headroom, so a month that runs hot needs a second proxy, and the per-GB plan turns the same 45 GB into about USD 90 a month. No request-rate or per-IP limit is published, so none can fail before it.
- interface detail: The three cited pages price the product and state the KYC gate; none of them records the wire protocol or a public API, so this record does not assert socks5 or http-proxy. The token list is left at unknown rather than guessed.
- tooling: The cited pages describe no SDK, CLI or rclone-style backend, and no wrapper is needed to judge the provider: what stands in the way is the identity gate, not tooling. Whether a given client can dial the issued endpoint is unestablished here, because the protocol is not recorded.
- composes with: An egress hop in front of the Workers AI gateway: about 45 GB a month across about 599,000 requests leaves through a proxy endpoint, so the per-proxy plan's 50 GB fair-use ceiling per proxy sits 5 GB above the whole workload, and the per-GB plan would bill about USD 90 a month at USD 2.00/GB.
- reliability: Their marketing graphic shows the exit 100.64.12.7 AS21928, but 100.64.12.7 is RFC 6598 carrier-shared space and RIPE returns no ASN for it, so that address is an illustration rather than a dialable exit; their other displayed exit, 172.58.14.102, does resolve to AS21928 T-Mobile USA, so the carrier claim holds where the sample address does not.
- notes: Two pricing shapes are kept in one record because they are the same product and the difference is the point: the per-proxy plan's unlimited bandwidth is bounded by a 50 GB fair-use threshold, which is the number that matters at 45 GB a month, and splitting the record would hide that. The address finding rests on one lookup per address on 2026-10-24, taken from RIPE Stat's prefix-overview rather than from a request through an issued endpoint; A third-party comparison blog (caproxy, 2025-12-08) claims a free version covering up to 5 ports; no vendor page read here confirms it, so free_tier records what the vendor prices and nothing more, and a vendor page naming a free plan would move it.
- evidence note: Every field the verdict rests on is read from the vendor's own pages on 2026-10-24: the price, the 50 GB fair-use threshold and the Tier 1 KYC sentence. The only measurement here is the two-address RIPE lookup, which settles the graphic and not the verdict. Measured would need an approved Tier 1 account, a session through an issued endpoint and a byte count.
- extras:
  - rung: 5
  - rung_note: The exit sits in a carrier's mobile address pool (AS21928 T-Mobile USA) and the gate is a national-id KYC rather than a carrier contract, so the distinguishing property is the address registration class, one rung above a bare ASN.
  - exit_samples[0].address: 100.64.12.7
  - exit_samples[0].claim: shown as an exit in their marketing graphic with AS21928
  - exit_samples[0].check: RFC 6598 shared space, not announced, no ASN at RIPE; an illustration
  - exit_samples[1].address: 172.58.14.102
  - exit_samples[1].claim: shown as an exit
  - exit_samples[1].check: aligned to 172.58.8.0/21, AS21928 T-Mobile USA
- evidence:
  - [1] 2026-10-24: Per GB USD 2.00 flat with block prices USD 50/25 GB, USD 100/50 GB, USD 200/100 GB and USD 400/200 GB; per proxy USD 59/proxy/month with unlimited bandwidth and a 50 GB fair-use threshold per proxy per month.
  - [3] 2026-10-24: Identity verification is a required step of getting an account, which makes this a national-id class registration rather than an email or phone signup.
  - [2] 2026-10-24: The per-proxy plan's unlimited bandwidth is qualified by a 50 GB fair-use threshold per proxy per month, and the page carries the sentence You must complete identity verification (Tier 1) before you can use the proxies.
  - probe:ripe-prefix-overview/100.64.12.7 2026-10-24: RIPE Stat returns announced:false and an empty asns[] for 100.64.12.7 and places it in 100.64.0.0/10 Shared Address Space (according to [RFC 6598]), so the address in the graphic cannot be an exit.
  - probe:ripe-prefix-overview/172.58.14.102 2026-10-24: RIPE Stat aligns 172.58.14.102 to the less-specific 172.58.8.0/21 and returns asn 21928, holder T-MOBILE-AS21928 - T-Mobile USA, so the carrier behind the other displayed exit is real.
- sources:
  - [1] https://proxidize.com/mobile-proxy-pricing/
  - [2] https://help.proxidize.com/proxidize-proxies/mobile-proxies/mobile-per-proxy
  - [3] https://proxidize.com/kyc/
