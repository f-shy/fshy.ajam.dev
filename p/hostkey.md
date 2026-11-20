# HOSTKEY

> hostkey.ru | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostkey/ | JSON https://fshy.ajam.dev/api/v1/entity/hostkey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HOSTKEY (vm.v2-medium)

- `compute/hostkey-windows` | qualifies-with-caveat | evidence documented | binding volume-quota | category Windows VPS | tier vm.v2-medium
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T13:30:00.000Z (live) | stale on 2026-11-26
- url https://hostkey.ru/vps/
- price parsed USD 15.67/mo
- disagrees on verdict: `compute/hostkey` says paid-only, `compute/hostkey-windows` says qualifies-with-caveat
- free tier: no free tier; EUR 14.00 a month on the English Windows storefront for 8 vCPU, 16 GB of RAM, 160 GB of NVMe and 3 TB of transfer on a 1 Gbit/s port, read from the page's JSON-LD in an HTTP 200 response of 2,731,056 bytes at 12:18Z on 2026-10-26, with vm.v3-medium at EUR 16.00 for the same shape. A re-read at about 15:20Z returned HTTP 403, and the Russian storefront prints RUB 3,390 for the same shape, which is USD 42.02 at 0.012396 | unit: none | metered on: none | read on: 2026-10-26 | source: [1] | note: the EUR 14.00 is the documented English price and the RUB 3,390 the documented Russian price for one shape; the 403 re-read is recorded beside the first read and does not withdraw it
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 3 TB a month included on a 1 Gbit/s port, printed on the plan card | metered: yes | free allowance: 3 TB per month | source: [2]
- identity: card | detail: an account and a payment method at order; the storefront is region-split, so which entity and currency a buyer transacts with depends on the domain used
- interface: rest, cli
- limits:
  - volume-quota (binding): 3 TB a month [2]
  - per-ip-shaping: 1 Gbit/s port [2]
- limits note: the 3 TB allowance is the smallest in the qualifying set and is reached before the port becomes the constraint for a busy mirror. The plan card also prints one IPv4 included. No Windows surcharge is printed on the card or anywhere in the price flow read.
- binding note: 3 TB a month decides the row for any high-transfer workload; a backup or build box will not reach it.
- interface detail: RDP with administrator access on a dedicated IPv4; the control panel offers a console, an OS reinstall and an ISO library with per-file size and mount-time limits
- tooling: any RDP client; the HOSTKEY control panel, which mounts a buyer's ISO from its own library or from a URL
- composes with: the widest 16 GB shape in the set on paper. Two storefronts of one vendor price the same shape at EUR 14.00 and RUB 3,390, a gap of about 2.7 times that neither page explains, so the row carries both numbers with their currencies and dates and is ranked in the document on the Euro figure.
- reliability: no reliability event observed. The English storefront answered HTTP 200 to the 12:18Z fetch and HTTP 403 to a re-read at about 15:20Z, and automated HTTP request returned with a stored provider copy whose own header records upstream_status 403, so the Euro figure rests on the first read and the failed re-read is recorded beside it.
- notes: Two storefronts of one vendor price the same shape differently, and both numbers are recorded rather than one being picked as the truth. The English Windows page printed EUR 14.00 a month for vm.v2-medium, read from its JSON-LD in the 12:18Z fetch on 2026-10-26 (HTTP 200, 2,731,056 bytes), with vm.v3-medium at EUR 16.00. A re-read of that page at about 15:20Z answered HTTP 403, the English catalogue path answered HTTP 403 in 5,680 bytes, and automated HTTP request returned with a stored provider copy whose own header recorded the 403, which is not citable. The Russian storefront prints RUB 3,390 for the same 8 vCPU, 16 GiB and 160 GB shape, which is USD 42.02 at 0.012396, so the two storefronts differ by about 2.7 times and neither page explains the gap. The mechanism by which the two can be confused is worth naming: the.ru page's own product JSON uses a key named eurbase to hold 3390 while the same page's JSON-LD labels the figure as EUR, so a reader scanning structured data can lift a ruble card as a Euro price. The licence is sold separately on both storefronts and its price is unpublished, which is why the all-in cost cannot be stated.
- evidence note: the shape, the 3 TB allowance, the 1 Gbit/s port and the RUB 3,390 monthly price are read from the RU plan card on 2026-10-26, in a 3,045,248-byte page. The EUR 14.00 is read from the EN page's JSON-LD in a 2,731,056-byte HTTP 200 response at 12:18Z the same day, with EUR 16.00 for vm.v3-medium; a re-read at about 15:20Z returned 403, and both reads are dated evidence, so the Euro figure is documented rather than unresolved. The Windows surcharge is unpublished on both storefronts, which is why this row's all-in cost cannot be stated.
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 16
  - shape.disk_gib: 160
  - billing_model: monthly
  - term: none
  - monthly_eur: 14.0
  - monthly_usd: 15.67
  - monthly_rub: 3390.0
  - monthly_rub_usd: 42.02
  - v3_monthly_eur: 16.0
  - setup_fee_eur: 0.0
  - windows_licence: sold separately, price unpublished on both storefronts
  - windows_images: Windows Server 2019; Windows Server 2022 Datacenter; Windows Server 2025
  - jsonld_currency_bug: on the .ru page a ruble card is labelled priceCurrency EUR in the structured data, which is how a RUB 3,390 plan can be misread as a Euro plan
  - ipv4_included: yes
  - port_mbps: 1000
  - traffic: 3 TB/month
  - fx: RUB 80.673994 per USD, open.er-api.com, 2026-10-26
  - en_read: HTTP 200, 2,731,056 bytes at 12:18Z on https://hostkey.com/vps/windows/; JSON-LD price 14.00 for vm.v2-medium and 16.00 for vm.v3-medium
  - en_reread: HTTP 403 at about 15:20Z on a re-read of the same page
  - en_catalogue_403: https://hostkey.com/vps/ returned HTTP 403 in 5,680 bytes
  - ru_url: https://hostkey.ru/vps/
  - en_url: https://hostkey.com/vps/windows/
  - en_catalogue_url: https://hostkey.com/vps/
- evidence:
  - [1] 2026-10-26: HTTP 200, 2,731,056 bytes at 12:18Z; the page's JSON-LD carries price 14.00 with priceCurrency EUR for vm.v2-medium and 16.00 for vm.v3-medium
  - [2] 2026-10-26: quoted from the vm.v2-medium card: vCPU 8, RAM 16 Gb, 160 GB NVMe, IPv4, 1 Gbit/s, 3 TB, at 3390 with the per-month marker
  - [2] 2026-10-26: the page's product JSON for that card carries "currency":"rub" and a prices object holding 3390, while the adjacent JSON-LD block labels the same 3390 as "priceCurrency":"EUR"; the 1510 value that also carries EUR belongs to a preceding 12 GiB card
  - [1] 2026-10-26: HTTP 403 on a re-read at about 15:20Z, so the English Windows page could not be re-confirmed after the 12:18Z read
  - [3] 2026-10-26: HTTP 403, 5,680 bytes to a direct fetch with a browser user agent, so the English catalogue path did not answer either
  - [3] 2026-10-26: 
  - [2] 2026-10-26: the .ru page mentions Windows only in the what-is-included list as 'Operatsionnye sistemy UNIX i WINDOWS'; no licence price is printed on the card or in the price flow
  - [2] 2026-10-26: RUB 3,390 converted at 0.012396 per ruble is USD 42.02 a month
- sources:
  - [1] https://hostkey.com/vps/windows/
  - [2] https://hostkey.ru/vps/
  - [3] https://hostkey.com/vps/

## HOSTKEY (compute/hostkey)

- `compute/hostkey` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://hostkey.ru/vps/vps-vds-testovyy-period/
- disagrees on verdict: `compute/hostkey` says paid-only, `compute/hostkey-windows` says qualifies-with-caveat
- free tier: No free trial, stated in the provider's own words on two pages, while a third page offers three days of free access and the refund documentation invites a request to discuss free testing, so the provider publishes two answers at once. What is real is hourly billing on every virtual server: the machine is charged from delivery to cancellation, so a few hours of a full machine cost a few roubles and the unused remainder of a month returns to the balance as credit rather than as money. The cheapest shape is vm.v2-pico at 1 vCPU, 1 GB RAM, 40 GB SSD, a 1 Gbit/s port and 3 TB of traffic included, for RUB 490 a month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: Payment is in roubles by Russian bank cards including Mir, by bank transfer and by electronic payment systems, so a card is one accepted rail rather than a stated requirement; there is no free tier to gate. The record does not state whether signup asks for an email, a phone or an ID document, whether a card issued outside Russia works. Its notes say the payment page names Mir and Russian transfers only. Or any hold, debit or prepaid answer.
- interface: unknown
- limits:
  - volume-quota (binding): The included traffic is the first thing to fail at the high volume: 3 TB a month is about 100 GB a day, and the port at 1 Gbit/s could move thirty times that, so the allowance rather than the link is the ceiling. [1]
- limits note: The included traffic is the first thing to fail at the high volume: 3 TB a month is about 100 GB a day, and the port at 1 Gbit/s could move thirty times that, so the allowance rather than the link is the ceiling.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Hourly billing is the composition this provider offers: at RUB 490 a month a machine costs about RUB 0.67 an hour, so the whole catalogue can be benchmarked for the price of a coffee, and 3 TB of included traffic on a 1 Gbit/s port is the cheapest per-terabyte allowance found among evaluated providers at RUB 163 a terabyte.
- reliability: no reliability event recorded
- notes: The three-day claim on the marketing page is not a contract and is contradicted twice on the same domain, so a reader should treat it as copy rather than as an offer. Arithmetic: 490 / 730 = 0.67 RUB an hour; 490 / 3 = 163 RUB a terabyte. Not established: which of the two trial statements is honoured in practice, since that needs an account and a support conversation, and whether foreign cards work (the payment page names Mir and Russian transfers only).
- extras:
  - facets.class: regional-no-trial
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 40
  - facets.shape.port_mbit: 1000
- evidence:
  - [1] 2026-10-22: 'We do not provide a free trial period for virtual machines', followed on the same page by a trial that requires paying for one month and cancelling, with the remainder returned to the balance, quoted and translated
  - [2] 2026-10-22: 'Yes. We give free access to the chosen server for three days', which contradicts the trial page and the FAQ on the same site
  - [3] 2026-10-22: 'We do not provide a trial period for our servers. You can order a server for the minimum period and then refuse it, paying only for the time of actual use', quoted and translated
  - [4] 2026-10-22: cheapest plan vm.v2-pico: 1 vCPU, 1 GB RAM, 40 GB SSD, 1 Gbit/s port with 3 TB of included traffic, RUB 490 a month, quoted
  - [5] 2026-10-22: payment is in roubles by Russian bank cards including Mir, by bank transfer and by electronic payment systems, with locations in Moscow, Europe, Turkey and the United States
- sources:
  - [1] https://hostkey.ru/vps/vps-vds-testovyy-period/
  - [2] https://hostkey.ru/vps/arenda-virtualnoy-mashiny/
  - [3] https://hostkey.ru/documentation/faq/server_rental/
  - [4] https://hostkey.ru/vps/deshevyj/
  - [5] https://hostkey.ru/vps/s-testovym-periodom/
