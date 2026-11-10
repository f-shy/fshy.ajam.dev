# By-Hoster

> by-hoster.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/by-hoster/ | JSON https://fshy.ajam.dev/api/v1/entity/by-hoster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## By-Hoster

- `compute/by-hoster-windows` | qualifies-with-caveat | evidence documented | binding none | category Windows VPS | tier Windows - Plus
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:20:51.330Z (live) | stale on 2026-12-05
- url https://by-hoster.net/en/cheap-windows-vps
- price parsed USD 19.02/mo
- free tier: no free tier; Windows - Plus is EUR 16.99 a month for 8 vCores, 16 GB of RAM and 250 GB, quoted with tax included, and the yearly cycle takes 16.7 per cent off | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: not stated on the plan lines read: the page prints price, vCores, RAM and disk for each plan and no traffic volume, port speed or overage price | metered: no | source: [1]
- identity: card | detail: an account and a payment method at order
- interface: rest
- limits note: the page prints four cycles: monthly, quarterly, half-yearly and yearly, where quarterly and half-yearly are the monthly price multiplied with no discount and only the yearly payment applies -16.7 per cent. The 20 per cent VAT rate appears in the vendor's own worked example rather than as a line on the plan. No byte quota, port speed, request rate or object cap is printed, which is why limits[] is empty rather than padded with a kind the vocabulary does not cover.
- binding note: nothing in the seven-kind vocabulary binds, because the vendor publishes no quota of any kind. The constraint that decides the row is commercial rather than a limit: Windows installs at no charge but the key is the buyer's, and a licence channel costs more per month than the machine.
- interface detail: Windows is installed at checkout at no extra charge and the admin path is RDP on the issued address; the vendor states it neither supplies nor resells the Microsoft licence
- tooling: any RDP client on the issued address; a REST API for ordering and machine control (test and production keys) is documented for approved resellers, whose requests the vendor team reviews
- composes with: the cheapest 8 vCore, 16 GB row whose licence position is stated plainly rather than left blank, and the statement is bring-your-own. It pairs with a licence channel at about USD 14.17 a month, which puts the honest all-in figure near USD 33.21 rather than 19.02.
- reliability: no reliability event observed; the yearly discount is illustrated on the entry plan and the figure for Plus is arithmetic on the stated percentage rather than a printed total.
- notes: The EUR 16.99 is tax-inclusive, so it is not comparable with an ex-VAT figure without adjusting, and the USD 19.02 conversion inherits that basis. The yearly figure is EUR 14.15 a month equivalent, or USD 15.84, and the yearly invoice is EUR 169.83, which is USD 190.09 at 1.1193; the vendor illustrates the 16.7 per cent discount on its entry plan rather than on Plus, so the Plus figure is arithmetic on a printed percentage. The licence gate is the honest caveat: at USD 14.17 a month for a 16-core Standard licence channel the all-in cost is near USD 33.21, which is roughly what a licence-printed row costs.
- evidence note: the plan, its shape, the EUR 16.99 tax-inclusive price, the four cycles and the bring-your-own-licence sentence are read from the vendor page on 2026-10-26. Two derived numbers are weaker and labelled as arithmetic: the yearly equivalent of EUR 15.84 a month and the USD conversion at 1.1193. The 20 per cent VAT rate is the vendor's own example, not a printed line on this plan.
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 16
  - shape.disk_gib: 250
  - billing_model: monthly, quarterly, half-yearly or yearly
  - term: none monthly; yearly at 16.7 per cent off
  - monthly_eur: 16.99
  - monthly_usd: 19.02
  - yearly_monthly_eur: 14.153
  - yearly_monthly_usd: 15.84
  - yearly_first_payment_eur: 169.83
  - yearly_first_payment_usd: 190.09
  - setup_fee_eur: 0.0
  - vat_included: yes
  - vat_rate_example: 0.2
  - windows_licence: bring your own: installed at checkout at no charge, licence neither supplied nor resold
  - windows_images: buyer's choice at checkout, named per order rather than listed on the page
  - fx: EUR 1 = USD 1.1193, ECB reference rate, 2026-10-23
  - plan_url: https://by-hoster.net/en/cheap-windows-vps
- evidence:
  - [1] 2026-10-26: quoted: 'Windows - Plus EUR 16.99/mo (8 vCores, 16 GB, 250 GB)', beside 'Windows - Core EUR 9.99/mo (4 vCores, 8 GB, 100 GB)' and 'Windows - Max EUR 28.99/mo (16 vCores, 32 GB, 500 GB)'
  - [1] 2026-10-26: quoted on the licence: 'the Microsoft licence is not included: we install the system you choose at checkout at no extra charge, but we neither supply nor resell a licence'; the string BYOL does not occur and this sentence is the bring-your-own…
  - [1] 2026-10-26: quoted on cycles: 'Monthly, quarterly, half-yearly and yearly. Quarterly and half-yearly are simply the monthly price multiplied, with no discount: only yearly payment applies -16.7%'
  - [1] 2026-10-26: quoted on tax: 'our prices are shown with tax included' and the worked example 'An ex-VAT price of EUR 6.99 comes to EUR 8.39 including VAT', which is a 20 per cent rate applied by the vendor itself
  - [2] 2026-11-04: the vendor documents a REST API for ordering and machine control, with test and production keys | capture: sha256:9246074347808080f290424fafdf942303c2efa93614712c10e91c93f83f7536 | quote: REST API Catalogue at your prices, orders paid from credit, machine control. Test and production keys.
  - [2] 2026-11-04: reseller access, and so the API, is gated by a team review | capture: sha256:9246074347808080f290424fafdf942303c2efa93614712c10e91c93f83f7536 | quote: Every request is reviewed by our team.
- sources:
  - [1] https://by-hoster.net/en/cheap-windows-vps
  - [2] https://by-hoster.net/en/reseller-program
