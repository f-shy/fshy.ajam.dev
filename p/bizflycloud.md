# Bizfly Cloud

> bizflycloud.vn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bizflycloud/ | JSON https://fshy.ajam.dev/api/v1/entity/bizflycloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bizfly Cloud

- `compute/bizfly-cloud` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-02T02:17:33.709Z (live) | stale on 2026-12-03
- url https://bizflycloud.vn/docs/platform_overview/chinh_sach_dung_thu
- free tier: A 3-day free trial of one Cloud Server at up to 2 cores, 2 GB RAM and 60 GB SSD, with resources kept for 7 days after expiry; a separate Simple Storage trial gives 10 GB for 7 days plus 10 GB of cold storage free every month for a year. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: The server trial is three days and the account's resources are deleted seven days after it ends, so nothing survives unless the account is upgraded to paid. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: An email address and a Vietnam mobile number. Bizfly's account-creation guide lists the fields it asks for: '- Địa chỉ email hợp lệ.' and '- Số di động: là số điện thoại mã vùng Việt Nam, có khả năng nhận cuộc gọi và tin nhắn SMS.', a mobile number with the Vietnam country code that can receive calls and SMS. The account is then activated from an email link. That page names no card or payment method at registration. | country: VN
- interface: unknown
- limits:
  - retention-clamped (binding): The server trial is three days and the account's resources are deleted seven days after it ends, so nothing survives unless the account is upgraded to paid. [1]
- limits note: The server trial is three days and the account's resources are deleted seven days after it ends, so nothing survives unless the account is upgraded to paid.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The durable piece is the 10 GB of cold storage free every month for a year, which is a small perpetual-ish allowance; the compute is a three-day look.
- reliability: no reliability event recorded
- notes: The Vietnamese market's free lane is uniformly short: Bizfly's server trial is 3 days, its CDN and email trials 7 days, and only the 10 GB cold storage runs for a year. Viettel IDC advertises a free trial requiring no card but publishes no duration, which is the one Vietnamese lead worth a follow-up. Neither provider states an identity gate beyond a phone or email on the pages read, so the card requirement is genuinely absent here, which is unusual for the region.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Cloud Server - Prebuilt App | 3 ngay | ... So Server: 01 Ram: 2 GB CPU: 2 Core HDD: 100GB hoac SDD: 60GB'; 'Toan bo server, tai nguyen trong tai khoan se duoc luu tru khong qua 7 ngay ke tu ngay het han dung thu'; and for Simple Storage: '10 GB Cold Storage mien phi hang thang trong trong thoi han mot nam', quoted
  - [2] 2026-10-22: the competing Vietnamese offer, Viettel IDC's VPS free trial, states no credit card information is required and the trial is requested per plan, but the duration is not stated on the page, reported
  - [3] 2026-11-02: account creation requires a mobile number with the Vietnam country code that can receive calls and SMS | capture: sha256:ceab6e899c461efd0677d716555dfb638e4b205abadd7121fa4e4ec69f5f7584 | quote: - Số di động: là số điện thoại mã vùng Việt Nam, có khả năng nhận cuộc gọi và tin nhắn SMS.
  - [3] 2026-11-02: a valid email address is the other field the same guide requires at account creation | capture: sha256:ceab6e899c461efd0677d716555dfb638e4b205abadd7121fa4e4ec69f5f7584 | quote: - Địa chỉ email hợp lệ.
- sources:
  - [1] https://bizflycloud.vn/docs/platform_overview/chinh_sach_dung_thu
  - [2] https://www.viettelidc.com.vn/tin-tuc/dang-ky-trai-nghiem-chuong-trinh-vps-free-trial-voi-dich-vu-cloud-server-cua-viettel-idc
  - [3] https://bizflycloud.vn/docs/account/create/
