# Digitkala

> digitkala.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/digitkala/ | JSON https://fshy.ajam.dev/api/v1/entity/digitkala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Digitkala (دیجیت کالا)

- `debrid/digitkala` | paid-only | evidence documented | binding write-gated | category account shop (Iran; Toman-priced premium accounts, including AllDebrid and host accounts) | tier retail
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://www.digitkala.net/index.php?product_id=111&route=product%2Fproduct
- free tier: not applicable: a shop, not a retrieval service. It sells 30-day AllDebrid accounts at 2,691,000 Toman and a long catalogue of host accounts. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The same shop lists 1fichier, Keep2Share, Filefactory, Filejoker, Nitroflare, Rapidgator-class hosts, AllDebrid, DebridItalia and Prembox accounts.
- per-object cap: not applicable: the shop resells an account whose caps belong to the upstream service. | source: [1]
- retention: not applicable: the entitlement is the resold account's term, 30 days for the product read. | source: [1]
- egress: not applicable: traffic is the upstream service's. The shop charges a Toman price for the account term. | metered: no | source: [1]
- identity: email | detail: A shop account is needed to check out (the page links 'حساب جدید باز نمایید'). The registration fields were not read. | country: Iran
- interface: unknown
- limits:
  - write-gated (binding): the account is released after the shop's own order process; the delivery step is not automated on the page read [1]
- limits note: The product page shows stock ('در انبار') and a review count, not a delivery SLA.
- binding note: Nothing technical binds at 1 TiB/month that the upstream AllDebrid record does not already carry; what binds here is that a human or an order step must release the credential.
- interface detail: A web storefront (OpenCart-style URLs). The account is delivered as credentials; how it is delivered was not read because the checkout requires an account.
- tooling: Browser only. No API for the shop itself.
- composes with: This is the Iranian rail for a foreign debrid service: the buyer pays Toman in Iran and receives a working AllDebrid account, so the foreign card that AllDebrid's own checkout needs is never touched.
- reliability: A resold account is tied to the shop's upstream purchase: if AllDebrid suspends the shop's account for sharing or payment reversal, the buyer's 30 days end early and the buyer has no contract with AllDebrid.
- notes: AllDebrid's own 30-day price on alldebrid.com/offer is EUR 2.99; the shop's 2,691,000 Toman is the rial price of the same 30 days. The gap between the two is the cost of the rail, and turning it into a percentage needs the day's free-market rate, which on 2026-10-23 did not measure. The same operator sells host accounts, which is the older Iranian pattern this shop grew from.
- evidence note: The product name, stock status and the 2,691,000 Toman price were read on the product page. The delivery mechanism and the shop's payment gateway were not read.
- evidence:
  - [1] 2026-10-23: 'اکانت 30 روزه AllDebrid', manufacturer AllDebrid, model AllDebrid30, in stock, price 2,691,000 Toman
  - [2] 2026-10-23: The catalogue is a host-account shelf (1fichier, Keep2Share, Filefactory, Filejoker, Nitroflare and others), not a retrieval service of its own
- sources:
  - [1] https://www.digitkala.net/index.php?product_id=111&route=product%2Fproduct
  - [2] https://www.digitkala.net/index.php?route=product/category&path=99
