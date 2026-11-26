# 24fire

> 24fire.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/24fire/ | JSON https://fshy.ajam.dev/api/v1/entity/24fire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 24fire

- `compute/24fire-kvm-borse-xeon-8gb` | qualifies-with-caveat | evidence documented | binding volume-quota | category VPS | tier Xeon Deal #1 (KVM Boerse)
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T06:30:00.000Z (live) | stale on 2026-11-24
- url https://24fire.de/kvmserver/boerse
- price parsed USD 4.6/mo
- free tier: no free tier; the Boerse rotates a small set of prepaid KVM deals and the cheapest on the page is the 4 GB at EUR 7.33 | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: '100% zwanglos dank Prepaid-System' (no commitment, prepaid) and 'Keine Vertrage' (no contracts)
- egress: 'Unlimited Traffic (FairUse)' on a port quoted as 'Bis zu 5.000 Mbit/s' | metered: no | free allowance: unlimited under fair use | source: [1]
- identity: email | detail: No ID document and no company. No card hold is stated: unverified rather than none.
- interface: ssh
- limits:
  - volume-quota (binding): traffic stated as unlimited under fair use; no number is published [1]
- binding note: the traffic term is a fair-use word rather than a number, so the real ceiling is the vendor's enforcement, not a published quota.
- interface detail: root SSH on KVM, provisioned 'In unter 60 Sekunden online'
- tooling: any SSH client; the vendor's prepaid panel
- composes with: 8 GiB ECC and 2 Xeon cores in Frankfurt for EUR 4.11 a month with a stated permanent price guarantee
- reliability: the deal rotates: the page states 'Diese Angebote sind bis zum nachsten Wechsel um 20:00 Uhr verfugbar' (available until the next rotation at 20:00) and 'Preise konnen sich im Laufe des Tages dynamisch verandern', so the price is not stable across a day
- notes: Hardware specification: 2 Xeon E5-2697 v4 cores, 8 GB DDR4 ECC, 50 GB NVMe, and unlimited fair-use traffic at EUR 4.11 a month (USD 4.60 at the ECB rate). The vendor terms state a permanent price guarantee ('dauerhaft' with 'permanente Preisgarantie') against a standard EUR 7.39 price. Offers rotate dynamically throughout the day, and checkout requires client-side execution.
- evidence note: price, shape, the price-guarantee wording and the rotation policy are quoted from the vendor's own Boerse page read. The cart itself is JS-only and could not be read.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 8
  - shape.disk_gib: 50
  - billing_model: prepaid, monthly
  - term: monthly, prepaid
  - m10h_usd: 4.6
  - m24h_usd: 4.6
  - price_arithmetic: EUR 4.11 a month x 1.1193 (ECB reference, 2026-10-23) = USD 4.600, rounded USD 4.60. It is a VPS on a prepaid monthly period, so no 730-hour multiplication. The struck-through comparison on the card is EUR 7.39, which is USD 8.27.
  - out_of_pocket_usd: 4.6
  - signup_url: https://24fire.de/register
  - renewal_usd: 4.6
  - renewal_note: published as a permanent price, not a promo: the card reads 'dauerhaft 4,11 EUR pro Monat / permanente Preisgarantie' (permanently EUR 4.11 a month, permanent price guarantee). So the renewal is the same EUR 4.11 unless the guarantee is broken, and the comparison price it is struck against is EUR 7.39.
  - promo: no
  - worst_case_exposure_x: 1.8
  - worst_case_note: 7.39 / 4.11 = 1.80x if the permanent guarantee does not hold and the plan reverts to the struck-through comparison price.
  - fx.pair: EUR/USD
  - fx.rate: 1.1193
  - fx.date: 2026-10-23
  - port_mbps: 5000
  - ipv4_included: yes
  - ipv6: /64
  - stock: unknown: the card renders an active 'In den Warenkorb' button and no sold-out flag, but the page states the deal is only available 'bis zum nachsten Wechsel um 20:00 Uhr', so availability is time-bounded rather than a stock counter. Read at https://24fire.de/kvmserver/boerse
  - deal_id: 234
  - cart_readable: no
  - cart_note: the add-to-cart control is a JS button carrying 'data-deal-content' with a base64 product id (234 for this deal); the checkout at /checkout is client-rendered, so no server-side cart price was readable. The price recorded is the page's.
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS on a prepaid monthly period
  - vat: German consumer pricing; the page prints '4,11 EUR' with no VAT qualifier, and the vendor is a GmbH, so the figure is treated as consumer-gross. Not verified in a cart
- evidence:
  - [1] 2026-10-24: quoted from the Xeon Deal #1 card: 'statt 7,39 EUR dauerhaft 4,11 EUR pro Monat / permanente Preisgarantie / 2 Kerne Intel Xeon E5-2697 v4 / 8 GB RAM DDR4 ECC 2400 MHz / 50 GB NVMe SSD / Bis zu 5.000 Mbit/s Netzwerkgeschwindigkeit / Unlimited Traffic (FairUse) / 1 IPv4 + IPv6/64 IP-Netz / NTT Rechenzentrum, Frankfurt a.M.'
  - [1] 2026-10-24: quoted: 'Diese Angebote sind bis zum nachsten Wechsel um 20:00 Uhr verfugbar. Preise konnen sich im Laufe des Tages dynamisch verandern.'
  - [1] 2026-10-24: quoted FAQ answer on payment: 'Wie gewohnt uber dein 24fire-Guthaben oder verfugbare Zahlungsanbieter wie PayPal oder Kreditkarte. Es bleibt vollstandig Prepaid.'
  - [2] 2026-10-24: 
  - [2] 2026-10-24: 
  - [3] 2026-10-24: time='2026-10-23' currency='USD' rate='1.1193'
- sources:
  - [1] https://24fire.de/kvmserver/boerse
  - [2] https://24fire.de/agb
  - [3] https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
