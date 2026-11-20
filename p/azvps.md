# AZVPS

> azvps.vn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/azvps/ | JSON https://fshy.ajam.dev/api/v1/entity/azvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AZVPS

- `compute/azvps-cheap-2` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier VPS Cheap 2
- needs card no, phone yes, ID no, institution no | verified 2026-11-06T18:03:54.484Z (live) | stale on 2026-12-07
- url https://azvps.vn/vps-gia-re/
- price parsed USD 3.29/mo
- free tier: no free tier; VPS Cheap 1 at 63.750 VND a month is the entry plan | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; no deletion clock is published
- egress: 'Bang thong 200 Mbps' and 'Du lieu truyen Khong gioi han' (unlimited data transfer) | metered: no | free allowance: unlimited | source: [1]
- identity: any-phone | detail: registration at https://portal.azvps.vn/register asks for a full name, an email, a phone number and a password; the phone input carries the required attribute and its dial-code selector lists countries worldwide with VN +84 the default, while tax code and company name are optional ('nếu có'). A 'Đăng ký với Google' button offers an OAuth path; its fields are unverified behind a sign-up. The order flow then needs the account before any payment step: the plan's order page reads 'Bạn cần đăng nhập hoặc tạo tài khoản ở bước tiếp theo.' and names only a billing cycle ('Chu kỳ thanh toán'), no card, transfer or wallet. Hold amount: not published on https://portal.azvps.vn/store/vps/cheap-2, https://azvps.vn/dieu-khoan-su-dung/ or https://azvps.vn/chinh-sach-bao-mat/. Charged or verified: not published on those pages. Prepaid and virtual cards: not published.
- interface: ssh
- limits:
  - per-ip-shaping (binding): unlimited data transfer at 200 Mbps; no fair-use number is published [1]
- binding note: transfer is unlimited and the port is 200 Mbps, so the single vCPU and 2 GB of RAM bind first.
- interface detail: the plan card states 'toan quyen root/Admin' (full root) and automatic provisioning in minutes
- tooling: any SSH client; the vendor's own order panel
- composes with: a 2 GB Vietnamese box on a 200 Mbps port with unlimited transfer; the cheapest Vietnamese row that fits under the line
- reliability: no reliability event recorded
- notes: The 15% is a standing discount shown against a struck price, so 85.000 VND is the price as displayed and 100.000 VND is what it returns to if the discount is withdrawn. The 4 GB rung, VPS Cheap 4, is USD 6.09 and misses the line, so Vietnam's best shape under USD 5 is 2 GB. The legal entity was not established.
- evidence note: the prices are parsed from the vendor's page HTML; registration is read from the sign-up form (name, email, phone); the payment rails sit behind the account and are unverified.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 20
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 3.2917
  - m24h_usd: 3.2917
  - price_arithmetic: 85.000 VND a month after a 15% discount on 100.000 VND, times 0.00003873 USD per VND = USD 3.29 a month.
  - out_of_pocket_usd: 3.2917
  - renewal_usd: 3.8726
  - renewal_note: 100.000 VND is the undiscounted price the 15% is taken from
  - promo: yes
  - over_line: no
  - fx.pair: VND/USD
  - fx.rate: 3.873e-05
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - gib_per_usd: 0.6076
  - locations: Vietnam
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_methods: not published: the order page at https://portal.azvps.vn/store/vps/cheap-2 stops at 'Bạn cần đăng nhập hoặc tạo tài khoản ở bước tiếp theo.' and names no card, transfer or wallet; the terms page names no payment instrument either
- evidence:
  - [1] 2026-10-24: quoted: 'VPS Cheap 2 | 100.000d | -15% | 85.000 | d/thang ... 1 vCPU Platinum | 2 GB RAM | 20 GB SSD NVMe | Bang thong 200 Mbps'
  - [1] 2026-10-24: quoted: 'VPS Cheap 4 | 185.000d | -15% | 157.300 | d/thang ... 2 vCPU | 4 GB RAM | 30 GB SSD NVMe' - the 4 GB rung is USD 6.09, over the line
  - [2] 2026-11-02: the checkout stops at an account step, so the payment rails and any hold sit behind the sign-up | capture: sha256:1952210d2a57b82c22583a55d9e60652a2db9dbd4e37e9da9a256b3b5b9e4d15 | quote: Bạn cần đăng nhập hoặc tạo tài khoản ở bước tiếp theo.
  - [2] 2026-11-02: the order page's own summary stops at an account step, so the rails are behind the sign-up | capture: sha256:1952210d2a57b82c22583a55d9e60652a2db9dbd4e37e9da9a256b3b5b9e4d15 | quote: VAT (10%) 10.000 ₫
  - [2] 2026-11-02: the order flow requires an account before any payment step | capture: sha256:1952210d2a57b82c22583a55d9e60652a2db9dbd4e37e9da9a256b3b5b9e4d15 | quote: Bạn cần đăng nhập hoặc tạo tài khoản ở bước tiếp theo.
  - [2] 2026-11-06: the order page puts an account before any payment step and names no payment instrument | capture: sha256:69f436f041079ef963a46fc57d0a6896b8076893301d0ba36f0ff04b0b307c3b | quote: Bạn cần đăng nhập hoặc tạo tài khoản ở bước tiếp theo.
  - [3] 2026-11-06: the terms page speaks of paying fees but names no card, transfer or wallet | capture: sha256:e1326b912667d9cbd0505f90bf49fcc3586a8b3b249f2178ff19e7d8c33da601 | quote: Khách hàng không thực hiện việc gia hạn và thanh toán các khoản phí quá hạn sử dụng dịch vụ cho AZVPS trong thời hạn 5 ngày
  - [4] 2026-11-06:  | capture: sha256:03b57d1a56f9137134be7d1ce785b14452ddbed1e5357f2afe34098c7709dca0 | quote: Thông tin khách hàng gồm có tên, địa chỉ email, số điện thoại, địa chỉ liên hệ và các thông tin cá nhân khác do khách hàng chủ động cung cấp hoặc được AZVPS thu thập bằng các phương thức hợp lệ khác.
  - [5] 2026-11-06: the sign-up form marks the phone input required, so registration needs a phone number | capture: sha256:d89dcb15fd6e588f023b6a8a98c47286fb99211458c5e4e16f7b96ccbc74f6e8 | quote: <input id="phone" type="tel" name="phone" value="" required maxlength="32"
  - [5] 2026-11-06: the dial-code selector offers country codes worldwide with VN +84 the default, so a phone number is not tied to Vietnam | capture: sha256:0a4bc492ae891d296a46fc4c4d7aa86aa7f7e67a9a7576ecb6730cbd56ef93ed | quote: VN +84 Ả Rập Xê-út (+966) Afghanistan (+93) Ai Cập (+20) Albania (+355) Algeria (+213) Andorra (+376) Angola (+244) Anguilla (+1) Antigua và Barbuda (+1) Áo (+43) Argentina (+54) Armenia (+374) Aruba (+297) Azerbaijan (+994) Ấn Độ (+91) Ba Lan (+48) Bahamas (+1)
- sources:
  - [1] https://azvps.vn/vps-gia-re/
  - [2] https://portal.azvps.vn/store/vps/cheap-2
  - [3] https://azvps.vn/dieu-khoan-su-dung/
  - [4] https://azvps.vn/chinh-sach-bao-mat/
  - [5] https://portal.azvps.vn/register
