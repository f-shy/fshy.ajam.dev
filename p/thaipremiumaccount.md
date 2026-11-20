# ThaiPremiumAccount

> thaipremiumaccount.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thaipremiumaccount/ | JSON https://fshy.ajam.dev/api/v1/entity/thaipremiumaccount.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ThaiPremiumAccount

- `debrid/thaipremiumaccount-com` | fails-identity | evidence documented | binding volume-quota | category premium-account reseller (Thai: per-host accounts in THB, bank-transfer fulfilment) | tier reseller
- needs card yes, phone yes, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.thaipremiumaccount.com/showroom/hot
- price THB 690 per 30 days for a 1 TB Rapidgator account; THB 890 for Fileboom
- free tier: No free tier. Catalogue prices: 'Rapidgator premium account 30 วัน ฿ 690.00', 'Fileboom premium account 30 วัน ฿ 890.00', and 'Fileboom premium account Pro 30 วัน' above those. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Four products on the best-seller page; the shop is a LnwShop storefront.
- per-object cap: not applicable; the host's cap applies (the Rapidgator listing advertises 1 TB total download) | source: [2]
- retention: not applicable: the account is the customer's own host account once upgraded | source: [2]
- egress: The host's own allowance, restated in Thai: 'สามารถดาวน์โหลดได้ทั้งหมด 1 TB' for the 30-day Rapidgator account, one device at a time: 'สามารถใช้งานได้ครั้งละ 1 เครื่องเท่านั้น'. | metered: yes | free allowance: 1 TB per 30-day Rapidgator account | source: [2]
- identity: card | detail: Fulfilment is a Thai bank transfer: the shop runs a 'แจ้งชำระเงิน' (payment-notification) page with 'รายละเอียดการโอนเงิน' and lists only a mobile number and a Gmail address for contact. No card or PayPal rail is named on the product or payment pages. | country: Thailand
- interface: rest
- limits:
  - volume-quota (binding): 1 TB per 30-day Rapidgator account [2]
  - write-gated: manual bank-transfer confirmation before delivery [3]
- limits note: The product page warns that some Thai ISPs block premium-account use ('อินเตอร์เน็ตบางสถานที่ อาทิ หอพัก, บริษัท, สถานศึกษา ... อาจมีการตั้งค่าป้องกันการใช้งาน Premium account').
- binding note: 1 TB per 30 days is just under the 1 TiB monthly volume, so a second account or a second host is required in the same month.
- interface detail: Buy on the web store; the account or code arrives by email ('จัดส่ง Rapidgator premium account ให้ทาง Email').
- tooling: Nothing to install; the buyer then uses the host's web download or IDM (the shop also sells IDM licences at ฿750).
- composes with: Thailand's retrieval layer is resale, not aggregation: one account per host, bought in baht. It does not compose with a debrid, and it is the only way to reach a host from a Thai card that the host's own checkout refuses.
- reliability: The shop disclaims all responsibility if the underlying host fails ('เว็บไซต์ดังกล่าวขัดข้อง/หยุดให้บริการ ทางร้านไม่รับเปลี่ยนหรือคืนเงินทุกกรณี'), and delivery depends on a human confirming a transfer.
- notes: Thailand has no local premium-link generator that the Thai-language queries surfaced; the market buys foreign host accounts from a Thai storefront instead. That absence is the finding: the Thai layer is a shop, not a service. Trigger condition: a Thai PLG with published pricing appears.
- evidence note: Catalogue, product and payment pages read. The absence of a card rail is an observation about those three pages, not proof that none exists at checkout.
- extras:
  - platform: LnwShop storefront
  - products: Rapidgator, Fileboom (standard and Pro), IDM licence
  - traffic: 309,734 page views, 140,771 visitors (counter on the payment page)
- evidence:
  - [1] 2026-10-23: 'Rapidgator premium account 30 วัน ฿ 690.00', 'Fileboom premium account 30 วัน ฿ 890.00', 'Internet download manager [License key] ฿ 750.00'
  - [2] 2026-10-23: 'สามารถดาวน์โหลดได้ทั้งหมด 1 TB'; 'สามารถใช้งานได้ครั้งละ 1 เครื่องเท่านั้น'; delivery by email; no-refund clause if the host stops
  - [3] 2026-10-23: bank-transfer flow: 'แจ้งชำระเงิน', 'รายละเอียดการโอนเงิน', contact '085-1862562', shop updated '19 ต.ค. 2569'
- sources:
  - [1] https://www.thaipremiumaccount.com/showroom/hot
  - [2] https://www.thaipremiumaccount.com/product/12/rapidgator-premium-account-30-%E0%B8%A7%E0%B8%B1%E0%B8%99
  - [3] https://www.thaipremiumaccount.com/informpayment
