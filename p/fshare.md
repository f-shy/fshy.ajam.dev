# Fshare

> fshare.vn | Debrid, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fshare/ | JSON https://fshy.ajam.dev/api/v1/entity/fshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fshare Directlink

- `debrid/fshare-directlink` | qualifies-with-caveat | evidence documented | binding volume-quota | category traffic bundle (Vietnamese: prepaid download traffic that anyone can redeem without an account) | tier directlink
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.fshare.vn/payment/service/package-directlink
- price VND 600,000 per 1 TB of redeemed traffic (no expiry)
- free tier: No free tier: traffic is bought up front. 'Dung lượng Traffic 200GB / 1000GB / 3000GB ... Giá bán 150.000 VNĐ / 600.000 VNĐ' (the 3000 GB price did not render on either read). | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The unit is redeemed traffic, not stored bytes and not time.
- per-object cap: not stated | source: [1]
- retention: 'Không giới hạn thời gian sử dụng' - the traffic balance does not expire | source: [1] | note: No expiry is the distinctive part: the bundle is a balance, not a subscription.
- egress: Traffic is consumed by other people's downloads of the link: 'dung lượng sẽ trừ dần đến hết tuỳ theo dung lượng file chia sẻ và số lượt người tải file'. Recipients download at high speed 'không cần đăng nhập tài khoản'. | metered: yes | free allowance: none | price per TB: VND 600,000 per 1000 GB | source: [1]
- identity: country-phone | detail: Purchased through the same Fshare checkout as VIP and Fcode, which offers only Vietnamese rails (MoMo, ShopeePay, VNPAY, FPT Pay, SMS to 9029, domestic bank transfer). A recipient of the link needs nothing; the buyer is gated. | country: Vietnam
- interface: rest
- limits:
  - volume-quota (binding): 200 GB or 1000 GB of redeemed traffic per bundle [1]
- limits note: No time limit at all; the entire constraint is the traffic balance.
- binding note: The bundle is pure volume, so 1 TiB/month needs one 1000 GB bundle per month; nothing else binds because there is no clock.
- interface detail: Create a Directlink URL in the Fshare account; anyone with the URL downloads without signing in.
- tooling: Browser; the generated link is a plain HTTP URL that any download manager or scraper can fetch, which is what makes it usable as a distribution path.
- composes with: The only Vietnamese product found that prices bandwidth directly rather than time: one VND 600,000 bundle is a 1 TB distribution allowance that never expires, so it composes with any client that needs to serve files to third parties rather than to itself.
- reliability: Traffic is consumed by strangers downloading the link, so a link posted publicly can burn a bundle in hours; there is no per-recipient cap and no refund of consumed traffic.
- notes: Volume-based distribution plan distinct from time-based personal VIP subscriptions. Traffic balances do not expire.
- evidence note: Page read twice (extract and raw); two of three prices are quotable and the third did not render. The purchase rail is inferred from the Fshare checkout pages read separately, which is why identity is country-phone rather than measured.
- extras:
  - price_200gb: VND 150,000
  - price_1000gb: VND 600,000
  - price_3000gb: did not render
- evidence:
  - [1] 2026-10-23: 'Gói Directlink cho phép bạn tạo link tải nhanh cho file để chia sẻ với dung lượng lớn (3000GB)'; 'người nhận được link có thể tải file với tốc độ cao, không cần đăng ký tài khoản'
  - [1] 2026-10-23: price table: 'Dung lượng Traffic 200GB 1000GB 3000GB ... Giá bán 150.000 VNĐ 600.000 VNĐ' and 'Không giới hạn thời gian sử dụng'
- sources:
  - [1] https://www.fshare.vn/payment/service/package-directlink

## Fshare

- `debrid/fshare-vn` | fails-identity | evidence documented | binding none | category file host (Vietnamese: storage, direct download, Fcode per-download codes) | tier vip
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.fshare.vn/fcode
- price VND 90,000 per 30 days (VIP, 300 GB/day cap); VND 20,000 per 50 GB Fcode | parsed USD 3.49/mo
- free tier: No free byte allowance is published on the pages read. The vendor sells access two ways: VIP from VND 3,000/day ('Siêu tiết kiệm, chỉ từ 3.000Đ/ ngày (VIP 30 ngày/ 90.000Đ)') and Fcode, a per-download code: '20.000 VND Cho 10 lượt tải/12h/50GB dung lượng tải' when bought through MoMo/ShopeePay/FPT Pay/VNPAY. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: A free account exists and is what get-link shops resell access to; the site itself promotes VIP and Fcode as the paid paths. No free-tier quota sentence was found.
- per-object cap: not stated on the pages read | source: [2]
- retention: not stated on the pages read; VIP includes '300GB lưu trữ trong đó có 50GB lưu trữ đảm bảo (file không bị xóa)' | source: [2] | note: The 50 GB is guaranteed storage inside the VIP quota, not a retention period.
- egress: VIP: 'tải dữ liệu với tốc độ tối đa lên đến 300GB mỗi ngày' (up to 300 GB per day at full speed). Fcode buys a 50 GB / 12 h bucket or a 4 h single download. | metered: yes | free allowance: 300 GB/day on VIP; 50 GB per Fcode | source: [2]
- identity: country-phone | detail: Every published rail is Vietnamese: 'Mua Fcode bằng MoMo/ShopeePay/FPT Pay/VNPAY' or SMS 'FCODE gửi 8700 (Áp dụng cho các mạng Viettel, Mobifone, Vinaphone)'; VIP is also sold by domestic bank transfer to a named account. No card, PayPal or crypto rail appears on the Fcode or VIP pages. | country: Vietnam
- interface: rest
- limits:
  - volume-quota: 300 GB/day download on VIP [2]
  - volume-quota: 50 GB per Fcode; 10 downloads per 12 h [1]
  - per-object-cap: no single-file cap published on the pages read [1]
- limits note: Fcode validity is short by construction: 12 hours for the 50 GB wallet-code bucket, 4 hours for the single SMS purchase.
- binding note: At 1 TiB/month the requirement is 34 GB/day and the VIP allowance is 300 GB/day, so no throughput constraint binds. What stops a registrant outside the country is payment, recorded in identity_cost.
- interface detail: Public API host api.fshare.vn (the vendor's own payment and package pages live there); web download; Fshare Tool for Windows/macOS; mobile apps.
- endpoint: https://api.fshare.vn
- tooling: api.fshare.vn plus community Python clients published on PyPI (get-fshare, getlink_fshare) and several GitHub tools; no official rclone backend observed; the vendor's own Fshare Tool is the supported desktop path.
- composes with: A Fshare VIP account is the upstream that a Vietnamese get-link shop resells, so paying Fshare directly replaces the shop; the 300 GB/day egress is 8.8x the 34 GB/day 1 TiB of monthly transfer needs, which makes Fshare throughput sufficient and the payment rail the only real obstacle.
- reliability: Fcode delivery depends on a live QR scan inside a Vietnamese wallet app or an SMS from a Vietnamese carrier; a code that is not copied within the 12 h window is lost, and get-link shops report the Fshare get-link path itself as unstable.
- notes: The Vietnamese host at the centre of the local get-link economy. Read directly rather than through a comparison site. The storage plan (1 TB-100 TB, VND 450,000 per 3 months for 1 TB per FPT's page) is a separate product and is not what the get-link shops resell. Trigger condition: Fshare publishes a card or international rail for Fcode.
- evidence note: Five vendor pages were read on 2026-10-23 (Fcode, VIP package, VIP benefits blog, api package page, 4share is separate). Buying a Fcode from outside Vietnam confirms the payment claim at measured; that purchase is what the record says cannot be done.
- extras:
  - fpt_reseller_page: https://fpt.vn/vi/khach-hang-ca-nhan/san-pham-dich-vu/dich-vu-online/fshare.html lists Storage 1TB at VND 450,000/3 months and VND 1,500,000/year
  - vip_storage: 300GB total, of which 50GB guaranteed
  - sms_gateway: 9029 via Viettel, Mobifone, Vinaphone
- evidence:
  - [1] 2026-10-23: '20.000 VND Cho 10 lượt tải/12h/50GB dung lượng tải khi mua Fcode bằng MoMo/ShopeePay/FPT Pay/VNPAY', '15.000 VNĐ cho 1 lượt tải/4h khi mua Fcode bằng SMS', 'FCODE gửi 8700 (Áp dụng cho các mạng Viettel, Mobifone, Vinaphone)'
  - [2] 2026-10-23: VIP traffic cap and price: 'tải dữ liệu với tốc độ tối đa lên đến 300GB mỗi ngày'; 'Chỉ từ 3.000 đồng/ngày ... 300GB dung lượng mỗi ngày'
  - [3] 2026-10-23: 'Siêu tiết kiệm, chỉ từ 3.000Đ/ ngày (VIP 30 ngày/ 90.000Đ)'; 'Dung lượng lưu trữ: 300GB (gồm 50GB đảm bảo và 250GB lưu trữ có thời hạn)'
  - [4] 2026-10-23: SMS VIP package: 'VIP 4 ngày - 15.000đ không giới hạn lượt tải', syntax 'BX FSHARE NAP15 FS gửi 9029' for Vinaphone/Mobifone and 'BX 15000 FSHARE FS gửi 9029' for Viettel
  - [5] 2026-10-23: the host warns against the get-link layer and names why the shops are unreliable: 'người dùng sẽ bị giới hạn dung lượng dữ liệu tải, số lượng lượt tải trong ngày ... tốc độ tải không ổn định, dữ liệu khi tải xuống bị đứt quãng'
- sources:
  - [1] https://www.fshare.vn/fcode
  - [2] https://blog.fshare.vn/dac-quyen-vip-fshare.html
  - [3] https://www.fshare.vn/payment/service/package-vip
  - [4] https://api.fshare.vn/payment/package/?type=vip
  - [5] https://blog.fshare.vn/canh-bao-nhung-tac-hai-va-nguy-co-xay-ra-khi-getlinks-fshare-tu-cac-website-khong-dang-tin-cay.html

## Fshare / FshareStorage (fshare.vn, FPT Telecom)

- `storage/fshare-fsharestorage` | fails-quota | evidence reported | binding per-ip-shaping | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fshare.vn
- free tier: Free tier: 50 GB of 'dung lượng không đảm bảo' (non-guaranteed capacity). From 2027-01-01 the platform rebrands to FshareStorage, guaranteed capacity rises 50 GB -> 100 GB, and the free account tier is discontinued entirely. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Free accounts terminated 2027-01-01; data on any free account surviving to that date is kept a maximum of 30 days. | days: 30 | source: [1] | note: not stated
- egress: Download speed capped at 500 KB/s on Free ('Tốc độ tải xuống với 500KB/s'), which is per-ip-shaping in practice. VIP is 300 GB and sold from 3,000 VND/day. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-ip-shaping (binding): 500 KB/s [1]
- limits note: per-ip-shaping: 500 KB/s download on Free. 50 GB non-guaranteed storage. Free accounts terminated 2027-01-01; data on any free account surviving to that date is kept a maximum of 30 days.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Web + Windows/sync client. No public API, no rclone backend. FPT is the parent ISP.
- composes with: 50 GB x N FPT accounts, all of it non-guaranteed. But this is a closing door, not an opening one: free accounts stop existing in ~2 months.
- reliability: The single most important thing about Fshare is the dated announcement: the free tier is being killed on 2027-01-01 and free-tier data gets a 30-day guillotine regardless of download activity. Anything built on it has a hard expiry date two months out.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Free tier: 50 GB of 'dung lượng không đảm bảo' (non-guaranteed capacity). From 2027-01-01 the platform rebrands to FshareStorage, guaranteed capacity rises 50 GB -> 100 GB, and the free account tier is discontinued entirely.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Dịch vụ sẽ dừng cung cấp tài khoản miễn phí từ ngày 01/01/2027', free-account data 'tối đa 30 ngày', guaranteed capacity 'từ 50GB lên 100GB'
  - [1] 2026-10-21: 'dung lượng miễn phí là 50GB', 'Tốc độ tải xuống với 500KB/s', 'KHÔNG giới hạn DUNG LƯỢNG tập tin TẢI LÊN'
- sources:
  - [1] https://blog.fshare.vn/voi-goi-free-fshare-ban-se-nhan-duoc-cac-dac-quyen-gi.html
  - [2] https://blog.fshare.vn/thong-bao-ve-viec-nang-cap-dich-vu-fshare-tu-ngay-01012027.html
