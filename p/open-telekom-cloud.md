# Open Telekom Cloud

> open-telekom-cloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/open-telekom-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/open-telekom-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Telekom Cloud / T Cloud Public

- `compute/open-telekom-cloud` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-11-06T17:42:12.765Z (live) | stale on 2026-12-07
- url https://www.open-telekom-cloud.com/en/prices
- free tier: EUR 250 of starting credit on a booked contract, redeemable until 2026-12-31 and expiring two months after the contract starts | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: institution | detail: institution: the contract is sold to a business, not to a consumer. The FAQ states 'Please bear in mind that T Cloud Public is only offered to business users in Europe.' The general terms require that the customer 'declares that they obtain all services that are provided under this agreement for the purposes of their company', and an EU customer outside Germany must 'communicate a valid VAT ID number issued by the tax authority of their state of residence before the first bill is issued.' Card: not published: https://www.t-cloud-public.com/en/support/faq (2026-11-06) states no card requirement, and the eShop cart it names as the ordering route did not render on 2026-11-06. Phone: not published: the same page states no phone requirement. | country: a business entity in Europe; an EU customer outside Germany must give a VAT ID before the first bill
- interface: unknown
- limits:
  - request-rate: EUR 250 of starting credit on a contract [1]
  - retention-clamped (binding): the voucher must be redeemed by 2026-12-31 and expires two months after the contract begins [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the price page was read on 2026-10-22 and states the EUR 250 voucher, its redemption deadline and its two-month life. The record's USD 284.45 was a conversion of that figure
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: instances bill monthly; the voucher's two-month life is the clock, not a machine
  - free_tier_kind: trial
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: storage is priced on its own page
  - ps.durability: managed storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the contract runs
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Book now and claim 250 EUR starting credit' with 'Voucher can be redeemed until 31 December 2026 and expires two months after conclusion of the contract' and monthly PDF and CSV billing, quoted
  - [2] 2026-11-04: the contract is with a business customer and not with a consumer, so a business identity is the gate | capture: sha256:7275b722450e64fc51316b7dfb3e98806560f7657dae1d2cfadcfb24b3525822 | quote: and the customer, who is not a consumer as defined in
  - [2] 2026-11-04: the customer must declare a company purpose, which is the business gate | capture: sha256:7275b722450e64fc51316b7dfb3e98806560f7657dae1d2cfadcfb24b3525822 | quote: declares that they obtain all services that are provided under this agreement for the purposes of their company
  - [2] 2026-11-04: the institution class is a company of any country, with a VAT ID required for an EU customer outside Germany | capture: sha256:7275b722450e64fc51316b7dfb3e98806560f7657dae1d2cfadcfb24b3525822 | quote: the customer must communicate a valid VAT ID number issued by the tax authority of their state of residence before the first bill is issued
  - [3] 2026-11-04: the eShop cart sells a T Cloud Public tenant to a registered customer and states no card field | capture: sha256:e5bef988a7bb16d7cabe34a3d5b86e665f8b125d1bbb8a3af2d606dcc2e86179 | quote: Register with a few clicks
  - [2] 2026-11-04: the business-only contract is unchanged | capture: sha256:7275b722450e64fc51316b7dfb3e98806560f7657dae1d2cfadcfb24b3525822 | quote: and the customer, who is not a consumer as defined in
  - [4] 2026-11-06: the offer is limited to business users in Europe, which is the institution gate and the country | capture: sha256:396ec400176d4f85b7425c150cfc0e0300fecd60f4ddbe788724aef285364ce7 | quote: Please bear in mind that T Cloud Public is only offered to business users in Europe.
  - [4] 2026-11-06: the offer is limited to business users in Europe, not to any country | capture: sha256:396ec400176d4f85b7425c150cfc0e0300fecd60f4ddbe788724aef285364ce7 | quote: Please bear in mind that T Cloud Public is only offered to business users in Europe.
- sources:
  - [1] https://www.open-telekom-cloud.com/en/prices
  - [2] https://shop.t-systems.de/eshop/medias/tcp-GTC-TSI.pdf
  - [3] https://shop.t-systems.de/eshop/agb/en/product/T_CLOUD_PUBLIC/TSI
  - [4] https://www.t-cloud-public.com/en/support/faq
