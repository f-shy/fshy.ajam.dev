# Infomaniak

> infomaniak.com | Egress and tunnels, Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infomaniak/ | JSON https://fshy.ajam.dev/api/v1/entity/infomaniak.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infomaniak

- `egress/infomaniak-vps-lite` | paid-only | evidence documented | binding none | category origin VM (paid VPS) | tier VPS Lite
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:55:18.737Z (live) | stale on 2026-12-05
- url https://www.infomaniak.com/en/hosting/vps-lite
- price CHF 2.70 a month on a 12-month term paid upfront, with unlimited traffic at 500 Mb/s
- free tier: no free plan: VPS Lite is 'From CHF 2.70 /month' on an annual commitment with 'Unlimited traffic with 500 Mb/s bandwidth' | unit: unlimited | metered on: none | read on: 2026-11-04 | source: [1] | note: A third-party index reports no trial for VPS Lite; the CHF 300 credit applies to Public Cloud only.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited traffic at 500 Mb/s; a third-party index adds 'limited by port speed and fair use'; the monthly price assumes 12 months paid in one payment; inbound UDP policy is not stated on the pages read | metered: no | free allowance: none published | source: [1]
- identity: card | detail: VPS payment methods are cards, PostFinance, bank transfer, PayPal, Twint or a prepaid balance; an order flagged for spam or fraud needs an ID check with a selfie through the kCheck app (third-party index); the vendor's order page was not read | country: None
- interface: ssh
- limits:
  - per-ip-shaping: 500 Mb/s bandwidth with unlimited traffic; 'limited by port speed and fair use' on a third-party index [1]
- binding note: at 1 TiB a month no byte quota is published; 500 Mb/s would carry about 160 TB a month, so the 12-month prepayment is the first cost to bite, not a limit
- interface detail: SSH to the VPS public IPv4 address
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a CHF 2.70 a month origin in Switzerland with no byte cap; the cost is a 12-month prepayment and the wall is the 500 Mb/s port
- reliability: unverified: no suspension, throttle or data-loss behaviour is stated on the pages read; VPS Lite is unmanaged
- notes: Plans run from 1 vCPU / 2 GB / 20 GB at CHF 2.70 to 4 vCPU / 8 GB / 160 GB at CHF 18.00 a month with the annual commitment; the 6- and 8-vCPU offers are also available with a monthly commitment. The existing Infomaniak Public Cloud record is a different product.
- evidence note: price, term and port are quoted from the vendor's VPS Lite page read on 2026-11-04; payment and ID-check rules rest on a third-party index and are reported; no server was ordered and no port was probed
- extras:
  - wg_path: native-conf
  - wg_detail: a VPS with a public IPv4 and root; wg-quick binds UDP natively unless the vendor firewall blocks it; inbound UDP was not probed
  - ingress: unverified: no inbound UDP port policy is stated on the pages read
  - volume_stated: unlimited traffic at 500 Mb/s
  - bytes_transit: yes
  - transit_note: bytes leave through the VPS's own public address on Infomaniak's Swiss network
- evidence:
  - [1] 2026-11-04: the entry plan is CHF 2.70 a month | capture: sha256:26dd52fd91439ff102aa03e028baf9f0f7dd69b8baa4146f8085b5f4a6dac07b | quote: From CHF 2.70 /&nbspmonth
  - [1] 2026-11-04: traffic is unlimited at 500 Mb/s bandwidth | capture: sha256:26dd52fd91439ff102aa03e028baf9f0f7dd69b8baa4146f8085b5f4a6dac07b | quote: Unlimited traffic with 500 Mb/s bandwidth
  - [1] 2026-11-04: the monthly price assumes an annual commitment paid in one payment for 12 months | capture: sha256:26dd52fd91439ff102aa03e028baf9f0f7dd69b8baa4146f8085b5f4a6dac07b | quote: Monthly price with an annual commitment, payable in a single payment for 12 months.
  - [2] 2026-11-04: a third-party index lists transfer as unmetered, limited by port speed and fair use | capture: sha256:b2222c535ae27cccacda9c38aed50bef181a8fb5c0ab7e7e625bbd50d867a981 | quote: Unmetered (limited by port speed and fair use)
  - [3] 2026-11-04: a third-party index lists the VPS payment methods | capture: sha256:3c8de1587a11e9f06c8ce0a90a89c0eccd1370b819c92bdc64b77536118c694d | quote: VPS: Visa, Mastercard and CB cards, PostFinance card (CHF only), IBAN bank transfer, PayPal, Twint, or a prepaid account balance.
  - [3] 2026-11-04: a third-party index reports a kCheck ID check on flagged orders | capture: sha256:3c8de1587a11e9f06c8ce0a90a89c0eccd1370b819c92bdc64b77536118c694d | quote: ID check via the kCheck app (ID plus selfie) when an order is flagged for suspected spam or fraud, or for account unblocking.
  - [3] 2026-11-04: a third-party index reports no trial for VPS Lite | capture: sha256:3c8de1587a11e9f06c8ce0a90a89c0eccd1370b819c92bdc64b77536118c694d | quote: No trial for VPS Cloud or VPS Lite.
- sources:
  - [1] https://www.infomaniak.com/en/hosting/vps-lite
  - [2] https://serverworth.com/plans/infomaniak/vps-lite-1c-2g/
  - [3] https://serverworth.com/providers/infomaniak/

## Infomaniak Public Cloud

- `compute/infomaniak-public-cloud` | fails-identity | evidence documented | binding write-gated | category VPS | tier Public Cloud trial credit
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T06:27:00.000Z (live) | stale on 2026-11-24
- url https://www.infomaniak.com/en/hosting/public-cloud
- free tier: 'Get started free of charge with CHF 300.- credits to be used within 3 months.' The credits are once per customer and restricted to 35 named countries, and a card with a CHF 20 preauthorisation is required to take them. | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: once per customer: 'this offer is available in the following countries ... once per customer'
- retention: the credits expire: 'CHF 300 of credits for the Public Cloud product for 3 months'. Instances bill by the hour on the median of the hour's use; storage is separate and 10 TB a month of outgoing traffic is included per organisation.
- egress: 'the incoming and outgoing traffic is free. With regard to storage, 10 TB are included per month and per organisation for outgoing traffic (the rate indicated on this page then applies).' | metered: yes | free allowance: 10 TB per month per organisation | source: [2]
- identity: card | detail: card required, CHF 20 authorisation hold: quoted 'A bank card is also required. Infomaniak will place a preauthorisation hold of CHF 20 on your card. Your card will not be debited; the amount will be released by your bank according to its own terms (usually within 7 days).' The page says 'bank card' rather than 'credit card', which suggests a debit card is accepted, but it does not say so explicitly and no card-type list is published on the page read.
- interface: ssh, rest
- limits:
  - write-gated (binding): a bank card with a CHF 20 preauthorisation hold, released by the bank usually within 7 days [2]
  - volume-quota: CHF 300 of credit once per customer, expiring after 3 months [1]
  - per-ip-shaping: the trial is limited to 35 named countries [2]
- binding note: The CHF 20 preauthorisation is the first thing that fails: no card, no trial, regardless of the CHF 300 on offer.
- interface detail: OpenStack Nova instances with SSH, a console and an OpenStack API; block storage on Ceph/Cinder
- tooling: any SSH client; the OpenStack CLI or the vendor console
- composes with: A Swiss OpenStack cloud with real VM shapes and 10 TB a month of egress, but the CHF 20 hold is exactly the pattern earlier readings flags, and it is restricted to 35 countries.
- reliability: no reliability event recorded
- notes: Rejected on the card. The hold is CHF 20, not USD 50, so the USD 50 figure is not literally reproduced here; it is the same mechanism at a smaller amount. The 35-country allowlist is a second gate that no amount of card solves, and it excludes China. Instance shapes and hourly rates were behind a table that did not render through automated retrieval, so no shape and no USD-per-month figure are recorded rather than guessed. Not previously in earlier readings.
- evidence note: The CHF 300, the 3-month expiry, the 35-country list, the CHF 20 hold and the 10 TB egress allowance are all quoted from Infomaniak's own public-cloud pages read. The instance shapes and hourly rates were behind a JavaScript table that did not render, so no shape is recorded.
- extras:
  - shape.note: the price table did not render; only a 'Memory 8 GB / Storage 50 GB' fragment appeared without its vCPU count or rate
  - billing_model: hourly
  - term: hourly, billed monthly in arrears
  - price_arithmetic: not computable: no hourly rate was readable today
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: OpenStack security groups; a floating IP is a separate allocation
  - session_cap.restart_required: no
  - session_cap.note: the credits expire at 3 months; no per-instance reap is published
  - signup_url: https://shop.infomaniak.com/order/public_cloud
  - credit_hours_at_shape: not computable: the credit is CHF 300 and no hourly rate was readable, so no hour count can be derived without inventing the rate
  - card_hold_note: CHF 20 preauthorisation, not USD; no FX rate was recorded so it is not converted
  - payment_methods: 'bank card'; the card type list is not published on the page read
- evidence:
  - [1] 2026-10-24: quoted: 'Get started free of charge with CHF 300.- credits to be used within 3 months.'
  - [2] 2026-10-24: quoted: 'The trial offer provides access to CHF 300 of credits for the Public Cloud product for 3 months, once per customer.'
  - [2] 2026-10-24: quoted: 'A bank card is also required. Infomaniak will place a preauthorisation hold of CHF 20 on your card. Your card will not be debited; the amount will be released by your bank according to its own terms (usually within 7 days).'
  - [2] 2026-10-24: quoted: 'Generally speaking, the incoming and outgoing traffic is free. With regard to storage, 10 TB are included per month and per organisation for outgoing traffic'
  - [2] 2026-10-24: quoted: 'This offer is available in the following countries: Switzerland, France, Belgium, Luxembourg, Germany, Italy, Austria, Spain, Portugal, Monaco, Australia, Canada, Chile, South Korea, Denmark, Estonia, the United States, Finland, Greece, Hungary, Ireland, Iceland, Israel, Japan, Latvia, Lithuania, Mexico, Norway, New Zealand, the Netherlands, Poland, the Slovak Republic, the Czech Republic, the United Kingdom, Slovenia, Sweden and Turkey.'
- sources:
  - [1] https://www.infomaniak.com/en/hosting/public-cloud
  - [2] https://www.infomaniak.com/en/hosting/public-cloud/prices

## kdrive (infomaniak)

- `storage/kdrive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.infomaniak.com/en/free-cloud
- free tier: none reachable: THE textbook geo-fenced signup. The free offer is limited to a published 37-country list (CH, FR, BE, LU, DE, IT, AT, ES, PT, MC, AU, CA, CL, KR, DK, EE, US, FI, GR, HU, IE, IS, IL, JP, LV, | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: THE textbook geo-fenced signup. The free offer is limited to a published 37-country list (CH, FR, BE, LU, DE, IT, AT, ES, PT, MC, AU, CA, CL, KR, DK, EE, US, FI, GR, HU, IE, IS, IL, JP, LV,
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: THE textbook geo-fenced signup. The free offer is limited to a published 37-country list CH, FR, BE, LU, DE, IT, AT, ES, PT, MC, AU, CA, CL, KR, DK, EE, US, FI, GR, HU, IE, IS, IL, JP, LV
  - [2] 2026-10-21: cited as the basis of the rejection: THE textbook geo-fenced signup. The free offer is limited to a published 37-country list CH, FR, BE, LU, DE, IT, AT, ES, PT, MC, AU, CA, CL, KR, DK, EE, US, FI, GR, HU, IE, IS, IL, JP, LV
  - [3] 2026-10-21: cited as the basis of the rejection: THE textbook geo-fenced signup. The free offer is limited to a published 37-country list CH, FR, BE, LU, DE, IT, AT, ES, PT, MC, AU, CA, CL, KR, DK, EE, US, FI, GR, HU, IE, IS, IL, JP, LV
- sources:
  - [1] https://www.infomaniak.com/en/free-cloud
  - [2] https://www.infomaniak.com/en/support/faq/2409/connect-to-kdrive-via-webdav
  - [3] https://github.com/rclone/rclone/pull/8941

## swisstransfer 30-day option

- `storage/swisstransfer-30-day-option` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.infomaniak.com/en/support/faq/2929/understanding-swisstransfer-data-limits
- free tier: none reachable: The 30-day selection is not a 30-day retention. Files are deleted at 15 days unless the sender clicks an extension email on day 12, and the offer closes 3 days later. 'Once expired, a link… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: The 30-day selection is not a 30-day retention. Files are deleted at 15 days unless the sender clicks an extension email on day 12, and the offer closes 3 days later. 'Once expired, a link…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 30-day selection is not a 30-day retention. Files are deleted at 15 days unless the sender clicks an extension email on day 12, and the offer closes 3 days later. 'Once expired, a link…
- sources:
  - [1] https://www.infomaniak.com/en/support/faq/2929/understanding-swisstransfer-data-limits
