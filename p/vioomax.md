# ViooMax

> vioomax.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vioomax/ | JSON https://fshy.ajam.dev/api/v1/entity/vioomax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ViooMax (resale)

- `debrid/vioomax` | fails-identity | evidence reported | binding write-gated | category debrid resale - Indonesian agent that upgrades the buyer's account by hand | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:57.799Z (live) | stale on 2026-11-18
- url https://vioomax.com/realdebrid.htm
- disagrees on identity_kind: `debrid/vioomax` says email, `debrid/vioomax-com` says card
- free tier: No free tier. Four terms offered (30 / 90 / 180 / 365 days) with the price printed as 'Rp Call.000' - i.e. by quotation, no number published. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the page's own notice: 'Sistem Payment produk ini belum otomatis, pelanggan harus mengirimkan userlogin dan password untuk kami upgrade secara manual. Estimasi waktu upgrade 1 s/d 48 jam'
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance published; the page sells 'download speed unlimited' as a vendor feature | metered: no | free allowance: not published | source: [1]
- identity: email | detail: local Indonesian bank transfer (ATM, mobile banking, e-banking), no card and no PayPal; the order is a message in the format 'EMAIL // NAMA LENGKAP // MERK ACCOUNT // DURASI PAKET // NAMA BANK TUJUAN' (email, full name, product, term, bank) | country: Indonesia
- interface: rest
- limits:
  - write-gated (binding): manual upgrade, 1-48 h on working days, after the buyer sends username and password [1]
  - per-ip-shaping: the seller logs in from Indonesia to perform the upgrade; the buyer logs in from elsewhere [2]
- binding note: The seller must hold the buyer's credentials to deliver at all, and the vendor records connections: the delivery itself is the sharing event the terms describe.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Handing the seller the account password is the failure: the vendor's new-location check emails a PIN to the account's mailbox, and a login from the seller's IP is exactly the pattern its terms suspend.
- notes: The only shop found whose delivery method requires the buyer's password. That makes it the clearest case of the category: the resale is not of days but of access, and access is what the vendor's identity checks are built to stop.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: the manual-upgrade notice requiring username and password, the 1-48 h window, 'Rp Call.000' placeholders, and the nine-year trading claim
  - [2] 2026-10-23: 
  - [1] 2026-11-03: the order message carries email, full name, product, term and bank name | capture: sha256:e79290de7db9729bf85a64b8295ff3a11d94daf6e7f02a5f91f2b78adf93cc09 | quote: EMAIL // NAMA LENGKAP // MERK ACCOUNT // DURASI PAKET // NAMA BANK TUJUAN
  - [1] 2026-11-03: payment is a rupiah transfer from a local Indonesian bank, without a credit card | capture: sha256:e79290de7db9729bf85a64b8295ff3a11d94daf6e7f02a5f91f2b78adf93cc09 | quote: Cukup transfer rupiah dari bank lokal melalui ATM, Mobile Banking, atau ebanking di Indonesia maka
  - [1] 2026-11-03: payment is manual: the buyer sends login and password and the upgrade takes 1 to 48 hours on working days; the four terms still show 'Rp Call.000' | capture: sha256:e79290de7db9729bf85a64b8295ff3a11d94daf6e7f02a5f91f2b78adf93cc09 | quote: Sistem Payment produk ini belum otomatis, pelanggan harus mengirimkan userlogin dan password untuk kami upgrade secara manual. Estimasi waktu upgrade 1 s/d 48 jam pada hari kerja.
- sources:
  - [1] https://vioomax.com/realdebrid.htm
  - [2] https://real-debrid.com/terms

## ViooMax (reseller)

- `debrid/vioomax-com` | fails-identity | evidence documented | binding none | category premium-account and voucher reseller (Indonesian: IDR pricing, local bank transfer) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://vioomax.com/indoleech.htm
- price IDR 30,000 per 30 days for a 10 GB Indoleech slot; IDR 440,000 for 1 TB | parsed USD 165.84/TB-mo
- disagrees on identity_kind: `debrid/vioomax` says email, `debrid/vioomax-com` says card
- free tier: No free tier of its own; it resells the vendor's free slot: 'Free - 150 MB, 1 Active, 1 Mbit/s, Free'. Its paid Indoleech ladder runs Rp 30,000 (10 GB) to Rp 440,000 (1024 GB) per 30 days. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Prices are quoted in thousands of rupiah without the 'Rp' prefix in the table ('30.000' = Rp 30,000).
- per-object cap: not applicable: it sells the vendor's entitlement | source: [1]
- retention: not applicable | source: [1]
- egress: Whatever the underlying service grants; ViooMax's own table restates 1 Gbit/s paid and unlimited download. | metered: no | free allowance: none of its own | source: [1]
- identity: card | detail: The site's selling point is the absence of international rails: 'pengguna ... Indonesia bisa memiliki account Indoleech Premium tanpa kartu kredit / credit card, tidak perlu akun Paypol, dll. Cukup transfer rupiah dari bank lokal melalui ATM, Mobile Banking, atau ebanking di Indonesia'. In practice that means an Indonesian bank account is required, which is the gate for anyone outside Indonesia. | country: Indonesia
- interface: rest
- limits:
  - write-gated: manual order process; prices 'sewaktu-waktu bisa berubah karena perubahan kurs' [1]
- limits note: Ordering is by contact form, not self-service checkout, so delivery depends on an operator.
- binding note: The reseller imposes no technical limit; whatever it resells binds after purchase.
- interface detail: Web catalogue with an order form; the reseller describes buying by 'transfer rupiah dari bank lokal melalui ATM, Mobile Banking, atau ebanking'.
- tooling: None to install; the buyer receives an account or voucher for the underlying service.
- composes with: The workaround layer for the Indonesian payment gate: it converts an IDR bank transfer into a foreign service's premium entitlement. It chains with nothing itself and it exists only because the underlying sites cannot be paid for locally.
- reliability: Exchange-rate repricing is stated openly, delivery is manual, and the site's own copy is written for search engines rather than customers; there is no published refund or replacement policy on the page read.
- notes: Cleanest example of a payment gate producing a local middleman: the reseller's entire pitch is 'no credit card, no PayPal'. It also resells Debrid-Link, LinkSnappy and Katfile, so it is the Indonesian on-ramp to the global debrid market.
- evidence note: The reseller page and its price table were read. Whether it accepts a foreign card is not stated anywhere on the page and is treated as unknown, not as accepted.
- extras:
  - resells: Indoleech, Debrid-Link, LinkSnappy, Katfile, and others
  - ordering: contact form / WhatsApp-style manual order
  - self_description: 'reseller / agen resmi Account Premium berlisensi di Indonesia'
- evidence:
  - [1] 2026-10-23: 'tanpa kartu kredit / credit card, tidak perlu akun Paypol, dll. Cukup transfer rupiah dari bank lokal melalui ATM, Mobile Banking, atau ebanking di Indonesia'
  - [1] 2026-10-23: price ladder: 'Torrent 10G 30.000 / 85.000 / 162.000 / 300.000', 'Torrent 1000G 1024 GB 30 Active 440.000 / 1.250.000 / 2.400.000 / 4.400.000'; 'Harga di atas sewaktu-waktu bisa berubah karena perubahan kurs'
- sources:
  - [1] https://vioomax.com/indoleech.htm
