# UploadFlix

> uploadflix.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadflix/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadflix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UploadFlix

- `debrid/uploadflix` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host with paid premium tier (English UI, crypto checkout) | tier Premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:53.663Z (live) | stale on 2026-12-04
- url https://www.uploadflix.com/buy_premium.html
- price USD 10 per month, USD 48 for 1 year (vendor premium page); no per-GB price and no byte allowance is stated | parsed USD 10/mo
- free tier: 'Upload files up to 5 GB each without any restrictions' and 'Long-term Storage - We promise to keep your files as long-term in our servers without any premium or subscription'. | unit: GB | metered on: object-count | read on: 2026-10-23 | source: [1] | note: The 5 GB is a per-file upload cap, not a total. The site claims unlimited storage on the free tier.
- per-object cap: 5 GB per file free; 'Upload Up to 10 GB' on premium | bytes: 5000000000 | source: [2] | note: The premium page states the 10 GB figure; the 5 GB free figure is from the site's own feature list.
- retention: 'Very Long-term Files Storage - Your files are safely stored for a long time'. No day count, no inactivity rule published. | source: [2] | note: The FAQ says a file with a lost delete code is removed when it expires ('wait until the file expires'), so an expiry exists; its length is not stated.
- egress: Premium adds 'One-Click Direct Download', 'No Blog Redirection', 'No Banners & Pop-Up Ads' and 'Maximum Download Speed ... high-priority access to bandwidth'. No byte allowance and no per-GB price is published. | metered: no | source: [2]
- identity: email | detail: Account creation asks for a username, e-mail and password with an image code. Premium is bought by e-mailing the vendor ('Kindly Send Us a Email for Purchase') and paid in 'Bitcoin, USDT (TRC/ERC-20), Ethereum, LiteCoin'; no card processor is listed, so a buyer holding only a card may not be able to pay.
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB per file on free, 10 GB on premium [1]
- limits note: No download volume is published at any tier. The premium page sells speed and ad removal, not gigabytes, which suggests the limit is on the download path rather than on stored bytes.
- binding note: For 10 TiB of stored files the 5 GB free cap forces 2,000 objects; that is a chunking cost, not a blocker. No byte allowance is published, so nothing documents a volume failure at 1 TiB per month.
- interface detail: Upload page plus direct links. No API documentation was found on the pages read; the site markets 'direct links to share files instantly' rather than an API.
- tooling: The z_o_o_m File & Image Uploader lists uploadflix.com with account support, which is the practical upload path for batch work. Downloads are plain HTTP and take a download manager.
- composes with: A free host with unlimited storage and no expiry is the cheapest place to park an archive; the 5 GB per-file cap decides chunking, and premium is only needed to remove the blog interstitial that breaks scripted downloads.
- reliability: The brand runs across at least four hostnames (uploadflix.com, 1uploadflix.net, uploadflix.cc, dl.uploadflix.com) and one of them returned a Cloudflare 522 in a search result during on 2026-11-03, which is the failure mode a parked archive cares about. Premium is sold for crypto only, so a refund is not a practical path.
- notes: UploadFlix is not a Portuguese- or Spanish-language service; it surfaced under Portuguese queries because Brazilian link generators list it. It is documented here because the debrid question - what does the local scene actually use - cannot be answered without the hosts the generators carry.
- evidence note: The feature list, the 5 GB free cap, the 10 GB premium cap, the price and the payment-method list were read from the vendor pages on 2026-11-03. The file expiry length and the download volume are not stated.
- extras:
  - hostnames_seen: uploadflix.com; 1uploadflix.net; uploadflix.cc; dl.uploadflix.com
  - payment_methods_reported: Bitcoin; USDT TRC-20; USDT ERC-20; Ethereum; Litecoin
  - price_status: vendor premium page, read 2026-11-03
- evidence:
  - [1] 2026-10-23: 'Upload files up to 5 GB each without any restrictions', 'Long-term Storage ... without any premium or subscription', 'Generate direct links ... no registration required'
  - [2] 2026-10-23: the nine premium benefits, including 'Upload Up to 10 GB', 'Unlimited Cloud Storage' and 'Very Long-term Files Storage'
  - [3] 2026-10-23: 'Premium Cost: $10/Month Only. 1-Year Premium: $48 (60% Off Limited Time Offer)' and 'Payment Methods: Bitcoin, USDT (TRC/ERC-20), Ethereum, LiteCoin' - indexed text of the vendor page, not the rendered page
  - [4] 2026-10-23: the uploader's changelog entry 'uploadflix.com, uqload.cx' with account support, evidence the host is used by bulk uploaders
  - [3] 2026-11-03: the vendor premium page states USD 10 per month and USD 48 for one year | capture: sha256:7eb8ee0190404d244e80b8ee2fcc39afd7e7b8e9e7a6acc4f5cf17316567dc61 | quote: Premium Cost: $10/Month Only.
  - [3] 2026-11-03: the vendor premium page lists crypto payment methods only | capture: sha256:7eb8ee0190404d244e80b8ee2fcc39afd7e7b8e9e7a6acc4f5cf17316567dc61 | quote: Payment Methods: Bitcoin, USDT (TRC/ERC-20), Ethereum, LiteCoin
  - [5] 2026-11-03: the FAQ says uploaded files expire; no length is given | capture: sha256:90b97519175f38eb3cac91905e8ca4fb8eadbc86b6305c7ce1454ab163c5e1c7 | quote: If you lost your removal code you can simply wait until the file expires so it will be automatically removed from our site.
  - [3] 2026-11-03: premium raises the per-upload limit to 10 GB | capture: sha256:7eb8ee0190404d244e80b8ee2fcc39afd7e7b8e9e7a6acc4f5cf17316567dc61 | quote: ## 5. Upload Up to 10 GB
  - [3] 2026-11-03: premium sells download speed, no byte allowance is stated | capture: sha256:7eb8ee0190404d244e80b8ee2fcc39afd7e7b8e9e7a6acc4f5cf17316567dc61 | quote: Get the best possible download speeds with our high-priority access to bandwidth.
  - [3] 2026-11-03: premium states unlimited storage | capture: sha256:7eb8ee0190404d244e80b8ee2fcc39afd7e7b8e9e7a6acc4f5cf17316567dc61 | quote: Never worry about storage limits. Upload and store as many files as you want with our unlimited cloud storage.
  - [1] 2026-11-03: the free upload limit is 5 GB per file | capture: sha256:c846d9b4b4c153ac036d1e8ba811d24e9b9b8974f0e6b6526420c2e050a1c673 | quote: Upload files up to 5 GB each without any restrictions. Perfect for videos, large media files.
  - [6] 2026-11-03: the registration form asks for username, e-mail, password and an image code | capture: sha256:64ad031058cb5cde2371dcd2fd01500545e4aaf4551e3ea1bda422f135312a67 | quote: Username: E-mail: Password: Retype Password:
- sources:
  - [1] https://www.uploadflix.com/
  - [2] https://1uploadflix.net/buy_premium.html
  - [3] https://1uploadflix.net/buy_premium.html?op=payments
  - [4] https://z-o-o-m.eu/
  - [5] https://www.uploadflix.com/faq.html
  - [6] https://www.uploadflix.com/register.html
