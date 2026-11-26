# Getlink.vn

> getlink.vn | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getlink/ | JSON https://fshy.ajam.dev/api/v1/entity/getlink.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Getlink.vn

- `debrid/getlink-vn` | fails-identity | evidence documented | binding volume-quota | category multi-host premium link generator plus torrent leech (Vietnamese) | tier premium-m1
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:51.631Z (live) | stale on 2026-12-26
- url https://getlink.vn/host/get-link-torrent.php
- price VND 149,000 per 30 days for 10 GB/day (about VND 497,000 per TiB at the monthly cap) | parsed USD 5.77/mo
- free tier: No free allowance; the price page lists SPRO 99k at VND 99,000 for 30 days with 30 GB / 30 days, alongside PREMIUM M1 at VND 149,000 for 30 days with 10 GB/day. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The 99k banner resolves to the SPRO 99k tier at VND 99,000 for 30 GB over 30 days; the record prices PREMIUM M1 at VND 149,000 for 10 GB/day.
- per-object cap: not stated; the quota is a daily byte allowance, not a per-file cap | source: [2]
- retention: not applicable: a direct link is returned, the file is not stored for the caller | source: [2]
- egress: Daily byte allowance per tier, unused volume rolls over: 'Dung lượng không dùng hết được cộng dồn sang hôm sau'. M1 is 10 GB/day (300 GB/month) with a 40 GB first day; VIP 12 is 50 GB/day with 200 GB first day. Bandwidth is quoted at 1000 Mbps to 10 Gbps. | metered: yes | free allowance: none | source: [2]
- identity: country-phone | detail: The order form labels the phone number optional and the email required: 'Số điện thoại: (Không bắt buộc) ... Email nhận tài khoản\*:' ... payment by bank transfer or e-wallet, with a QR scanned 'trên App của 52 ngân hàng và ví Momo, ZaloPay, Viettel Money'. | country: Vietnam
- interface: rest
- limits:
  - volume-quota (binding): 10 GB/day on PREMIUM M1, 20 GB/day on M24; 25-50 GB/day on VIP tiers [2]
  - volume-quota (binding): first-day bonus 40-200 GB depending on tier [1]
- limits note: 150+ hosts supported; the vendor name-checks Rapidgator, Alfafile, FileFactory and K2S as the headline four.
- binding note: 10 GB/day is 300 GB/month, under a third of the 1 TiB monthly volume; the top tier's 50 GB/day is the only one that clears 34 GB/day.
- interface detail: Web panel: paste a host link or a magnet, receive a direct link. A free Vietnamese proxy is bundled with every tier ('Miễn phí Proxy Việt Nam').
- endpoint: https://getlink.vn
- tooling: Browser panel plus IDM; torrent and magnet leech is a first-class tab rather than an add-on; no API or rclone backend documented.
- composes with: The free Vietnamese proxy is the distinctive part: it lets a client outside Vietnam pull a link that is geo-shaped to Vietnamese networks, which is what the FPT/VNPT/Viettel-hosted servers are for. Chains with any download manager.
- reliability: Account details are emailed after a QR payment clears, so a failed or mistyped transfer leaves no order record; bandwidth claims (1000 Mbps to 10 Gbps, 2500+ TB/month capacity) are vendor-stated and unmeasured.
- notes: Same market as LinksVIP, opposite payment answer: Getlink.vn quotes a lower per-GB price and bundles a Vietnamese proxy, but takes only Vietnamese rails. The pair is the cleanest demonstration that the gate is payment, not capability. Trigger condition: a card rail appears.
- evidence note: The price page, the order page and the payment instructions were read. The payment rail is the load-bearing claim and comes from the order page's own text, not a third party.
- extras:
  - servers: 15+ Vietnamese 10Gbps at FPT/VNPT/Viettel; 25+ foreign 10Gbps at Singapore, US, Japan, Canada, France, Germany
  - capacity_claim: 2500+ TB per month, 15000+ active accounts (vendor-stated, unmeasured)
  - tiers: PREMIUM M1/M3/M6/M12/M24 plus VIP 1/3/6/12 and Super VIP
- evidence:
  - [2] 2026-10-23: tier table: 'PREMIUM M1 30 ngày 149,000 VNĐ, Dung lượng 10GB/ngày, 40Gb cho ngày đầu'; 'VIP 12 365 ngày 2,999,000 VNĐ, 50GB/ngày'; 'Hỗ trợ Rapidgator, Alfafile, FileFactory, K2S & 150+ Filehost'; 'Proxy Việt Nam'
  - [3] 2026-10-23: payment rail: 'Mua tài khoản Get link PRE - M1 bằng chuyển khoản ngân hàng hoặc Ví điện tử'; QR 'trên App của 52 ngân hàng và ví Momo, ZaloPay, Viettel Money'; 'Bạn vui lòng điền số điện thoại và email'
  - [1] 2026-10-23: price table restated and the '99.000đ' entry banner
  - [2] 2026-11-25: M1 is VND 149,000 for 30 days with 10 GB/day and a 40 GB first day | capture: sha256:2d61bc40483f15db63441c70b71932c7612a1ea26a02b034053ba971d7355205 | quote: ## PREMIUM M1 ... 30 ngày sử dụng ... 149,000 VNĐ ... Dung lượng ... 10GB/ngày ... 40Gb cho ngày đầu ... Hỗ trợ Rapidgator, Alfafile, FileFactory, K2S & [150+ Filehost](https://getlink.vn/host/150-host-get-link.php) ... Miễn phí ... Proxy Việt Nam
  - [1] 2026-11-25: the SPRO 99k tier is VND 99,000 for 30 days with 30 GB in total | capture: sha256:0611709a507860aee78e4e4b2c3f73eb523b35f097ce022f3833cf0dcaa21444 | quote: 99,000 VNĐ ... 30GB/30 ngày
  - [1] 2026-11-25: the 99k banner is a named SPRO tier with a 30 GB / 30 days allowance | capture: sha256:0611709a507860aee78e4e4b2c3f73eb523b35f097ce022f3833cf0dcaa21444 | quote: ## SPRO 99k ... 30 ngày sử dụng ... 99,000 VNĐ ... Dung lượng ... 30GB/30 ngày
  - [3] 2026-11-25: the order form takes phone and email and settles through bank apps or domestic wallets | capture: sha256:745ddc5c2b73dae5d2fb3723c94e4ae20a0c53d4cb89b6d3a0ab65d9e4a962b7 | quote: Mua tài khoản Get link PRE - M1 bằng chuyển khoản ngân hàng hoặc Ví điện tử ... Bạn vui lòng điền số điện thoại và email vào form dưới đây để getlink.vn có cơ sở xác thực giao dịch. ... trên App của 52 ngân hàng và ví Momo, ZaloPay, Viettel Money
  - [2] 2026-11-25: unused volume rolls over; first-day bonus ranges from 40 GB on M1 to 200 GB on VIP 12 | capture: sha256:2d61bc40483f15db63441c70b71932c7612a1ea26a02b034053ba971d7355205 | quote: *Lưu ý: Dung lượng không dùng hết được cộng dồn sang hôm sau theo Chính sách dung lượng. ... 40Gb cho ngày đầu ... 2,999,000 VNĐ (Tiết kiệm 40%) ... 50GB/ngày 200Gb cho ngày đầu
  - [3] 2026-11-25: the form marks phone optional, email required, and names the domestic wallet and bank apps | capture: sha256:745ddc5c2b73dae5d2fb3723c94e4ae20a0c53d4cb89b6d3a0ab65d9e4a962b7 | quote: Số điện thoại: (Không bắt buộc) ... Email nhận tài khoản\*: ... Thanh toán qua hình thức trên được miễn phí chuyển tiền từ hầu hết các ngân hàng, được hỗ trợ quét QR trên App của 52 ngân hàng và ví Momo, ZaloPay, Viettel…
- sources:
  - [1] https://getlink.vn/buy/mua-get-link.php
  - [2] https://getlink.vn/host/get-link-torrent.php
  - [3] https://getlink.vn/buy/mua-tai-khoan-get-link-premium-M1.php
