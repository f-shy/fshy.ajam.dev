# AgenPremium

> agenpremium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agenpremium/ | JSON https://fshy.ajam.dev/api/v1/entity/agenpremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AgenPremium

- `debrid/agenpremium-com` | fails-identity | evidence documented | binding volume-quota | category premium-account reseller (Indonesian: rupiah prices, six named Indonesian banks) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://agenpremium.com/id/debridlink.html
- price IDR 85,000 per 30 days for Debrid-Link (Rp 2,833/day) | parsed USD 4.7/mo
- free tier: No free tier. Debrid-Link terms in rupiah: 'Premium 15 hari Rp 62.000', 'Premium 30 hari Rp 85.000', 'Premium 90 hari Rp 186.000', 'Premium 180 hari Rp 350.000', 'Premium 360 hari Rp 618.000'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Prices are the reseller's; it also prints a per-day figure (Rp 2.833/day at 30 days).
- per-object cap: not applicable; the reseller restates Debrid-Link's own limit as 'Bandwidth Limit 400 GB/hari' | source: [1]
- retention: not applicable: 15-360 day entitlement | source: [1]
- egress: Debrid-Link's own: the reseller's data sheet says 'Bandwidth Limit 400 GB/hari' with parallel downloads, resume and torrent download supported. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Payment is by Indonesian bank only. The site's rail logos are 'BCA, Bank Mandiri, CIMB Niaga, Bank Jago, blu, SeaBank', and Debrid-Link's own reseller directory lists this shop as 'Indonesian - Bank BCA, Bank BNI, Bank CIMB, Bank Mandiri, Local Bank'. A domestic bank account is the gate. | country: Indonesia
- interface: rest
- limits:
  - volume-quota (binding): 400 GB/day (Debrid-Link, restated) [1]
  - write-gated: manual order; 'Proses 10-30 mnt' on the 360-day tier [1]
- limits note: The shop prints no-refund terms for missing or blocked files: 'kami tidak menerima refund jika file tidak ada atau file diblokir'.
- binding note: Debrid-Link's 400 GB/day is the first number that matters and it is well above 34 GB/day, so 1 TiB of monthly transfer would not hit it; the resale rail is the practical limit.
- interface detail: Web shop in Indonesian; order confirmation by WhatsApp ('JIKA ADA MASALAH TRANSAKSI, KONFIRMASI, GAGAL EMAIL, SEGERA WA' followed by a phone number).
- tooling: Debrid-Link's own web app, API and JDownloader integration after activation; the reseller adds only payment.
- composes with: The Indonesian on-ramp to Debrid-Link at Rp 85,000/month, which is the same service 247PremiumCart sells in India for ₹750 and Debrid-Link sells in euros. Useful as a price comparison across the three resale markets rather than as a distinct capability.
- reliability: Manual fulfilment with a WhatsApp confirmation path, no refunds for missing or blocked files, and a maintenance banner recording an outage that ended 30 May 2026; the shop is a payment front, not an operator.
- notes: The cleanest evidence that the Indonesian gate is a bank, not a card: six named domestic banks and no card logo. Trigger condition: a card rail appears on the site or in Debrid-Link's directory.
- evidence note: Price table and rail list read, and the rail list is corroborated independently by Debrid-Link's own reseller directory. Whether a foreign card can be used at all is unstated; the bank-only rail list suggests not.
- extras:
  - provider_directory_row: Debrid-Link lists it as an Indonesian-language reseller with local banks
  - confirmation_channel: WhatsApp, a mobile number
  - per_day: Rp 2.833/day at 30 days, Rp 1.717/day at 360 days
- evidence:
  - [1] 2026-10-23: price table: 'Premium 15 hari Rp 62.000', 'Premium 30 hari Rp 85.000', 'Premium 90 hari Rp 186.000', 'Premium 180 hari Rp 350.000', 'Premium 360 hari Rp 618.000'; 'Bandwidth Limit 400 GB/hari'
  - [1] 2026-10-23: rails: 'BCA | Bank Mandiri | CIMB Niaga | Bank Jago | blu | SeaBank'; 'kami tidak menerima refund jika file tidak ada atau file diblokir'
  - [2] 2026-10-23: 'AgenPremium | Indonesian | Bank BCA, Bank BNI, Bank CIMB, Bank Mandiri, Local Bank' - the provider's own directory confirms the rail set
- sources:
  - [1] https://agenpremium.com/id/debridlink.html
  - [2] https://www.debrid-link.com/resellers
