# Rayobyte

> rayobyte.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rayobyte/ | JSON https://fshy.ajam.dev/api/v1/entity/rayobyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rayobyte

- `debrid/rayobyte` | qualifies-with-caveat | evidence reported | binding volume-quota | category residential egress: rotating residential, metered per GB, with a disputed headline rate | tier Residential, pay as you go
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:21:34.000Z (live) | stale on 2026-11-07
- url https://rayobyte.com/pricing/
- price USD 3,584 per TiB by the pay-as-you-go ladder; USD 9.73 per TiB by the disputed headline
- free tier: No residential allowance published; the page's free offer is a web-unblocker trial ('free $0 for 48 browser hours'), not proxy bytes. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a byte stream, not an object | source: [1]
- retention: not applicable: a live endpoint, not stored bytes | source: [1]
- egress: Pay-as-you-go residential is a four-rung ladder, '$3.50/GB', '$2/GB', '$1.50/GB', '$0.70/GB', 'from $0.50/GB'. The same page also headlines 'Residential Proxies from $0.0095/GB' and shows monthly plans such as '$100/mo - 6,600 GB' at '$0.0150/GB'. The two statements differ by a factor of 233. | metered: yes | free allowance: none | price per TB: USD 3.50/GB at entry by the ladder, i.e. USD 3,584 per TiB; the headline rate implies USD 9.73 per TiB | source: [1]
- identity: card | detail: Self-service registration at app.rayobyte.com; the Scale tier opens 'after a compliance review', which is an extra gate on the cheap rates.
- interface: rest
- limits:
  - volume-quota (binding): pay-as-you-go ladder $3.50 to $0.50/GB; monthly plans advertised at $0.0150-$0.0095/GB with '1 concurrent request per $1 of plan' [1]
- limits note: The plan table's own wording ties plan size to concurrent requests ('A $100 plan runs 100 concurrent requests'), which is a concurrency product. A rate of $0.0095/GB for residential bytes would be 180 times cheaper than the cheapest credible rate in the market, so the two readings cannot both be about the same unit.
- binding note: Whichever reading is right, the product is sold against a byte or a slot counter; the conservative ladder is the one to price against until the unit is settled.
- interface detail: HTTP(S) and SOCKS5 endpoints; monthly plans meter concurrency as '1 concurrent request per $1 of plan'.
- endpoint: https://app.rayobyte.com/
- tooling: any HTTP/SOCKS5 client
- composes with: Documented as a warning rather than a price: the page's own headline rate is two orders of magnitude below every other vendor in the market read on 2026-10-23, and its table appears to price requests or concurrent slots rather than bytes.
- reliability: The cheap monthly rates are gated behind 'verified businesses' and a compliance review, so a single-person client is routed to the pay-as-you-go ladder, which is the expensive one.
- notes: The conservative number is kept and the contradiction is recorded, per published records rule on two sources disagreeing. The existence of a $0.0095/GB headline is itself useful: it is the kind of number a price index would lift into a comparison table and a reader would act on.
- evidence note: Both numbers are on the vendor page, but they contradict each other and the low one is not credible against four other vendors read the same day. Reported rather than documented because the unit is unresolved; a support answer confirms the threshold.
- extras:
  - ladder: 3.50 / 2.00 / 1.50 / 0.70 / from 0.50 USD per GB
  - disputed_headline: $0.0095/GB on the $5,000 plan
  - plan_meter: 1 concurrent request per $1 of plan
  - gating: verified businesses; compliance review
- evidence:
  - [1] 2026-10-23: 'Residential Proxies from $0.0095/GB' and '$100/mo - 6,600 GB $0.0150/GB' beside the ladder '$3.50/GB $2/GB $1.50/GB $0.70/GB from $0.50/GB'; also 'for verified businesses', 'Scale opens after a compliance review', and 'A $100 plan runs 100 concurrent requests'
- sources:
  - [1] https://rayobyte.com/pricing/
