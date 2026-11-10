# fshare's 4share.vn

> 4share.vn | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/4share/ | JSON https://fshy.ajam.dev/api/v1/entity/4share.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 4Share.vn

- `debrid/4share-vn` | fails-identity | evidence documented | binding volume-quota | category file host (Vietnamese: storage and backup, sold by 30-day package) | tier 30-day
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.4share.vn/bang-gia
- price VND 59,000 per 30 days for 50 GB stored | parsed USD 45.7/TB-mo
- free tier: No free allowance is published on the price page; the single package on sale is 'Gói 30 ngày 59.000đ, Hiệu lực 30 ngày, Dung lượng lưu trữ 50 GB'. | unit: none | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: The page also shows 'Xin lỗi bạn, Dịch vụ đang nâng cấp, vui lòng liên hệ hướng dẫn sử dụng!' above the price table, so the package may not be purchasable today.
- per-object cap: not stated on the price page | source: [1]
- retention: not stated on the price page; the package is 30 days of validity | days: 30 | source: [1] | note: 30 days is the package term, not a retention guarantee.
- egress: The page sells storage quota, not traffic; no byte allowance for downloads is published. The vendor markets in-country speed: 'Máy chủ đặt tại Việt Nam - không phụ thuộc cáp quang biển'. | metered: no | free allowance: none published | source: [1]
- identity: card | detail: Payment is by Vietnamese wallet or domestic gateway only: 'Thanh toán qua MoMo hoặc BảoKim (thẻ ATM / QR / chuyển khoản)'. A BảoKim ATM card is a domestic Vietnamese debit card; no Visa/MasterCard or PayPal rail is named. | country: Vietnam
- interface: rest
- limits:
  - volume-quota (binding): 50 GB stored per 30-day package [1]
- limits note: 50 GB of storage and no published download allowance; the constraint that matters is the size of the package, not a rate.
- binding note: A 50 GB package cannot hold 1 TiB of monthly transfer of anything; storage is the first wall and no larger tier is published on this page.
- interface detail: Web upload/download with resume support; the vendor names IDM explicitly ('dùng được với IDM và các trình quản lý truyền file').
- tooling: Browser plus IDM-style download managers for resume; no API or rclone backend documented on the pages read.
- composes with: 4share is the domestic Vietnamese mirror that get-link shops still advertise ('4share.vn 80 GB' daily on LinksVIP) while the host itself has moved to selling backup storage; treat it as an upstream that may disappear, not as a retrieval service.
- reliability: The price page carries an upgrade notice today, and the get-link shop that still lists 4share as a supported host is the only working route to it from outside; the vendor sells silence about downtime, not an SLA.
- notes: Included because every Vietnamese get-link shop still advertises it, and because the host itself has quietly become a backup product with domestic-only payment. The finding is that the brand outlives the service. Trigger condition: 4share publishes a card rail or a retrieval API.
- evidence note: Price page fetched raw. The payment sentence is on the same page. Whether the 30-day package can actually be bought during the upgrade is unknown and is what would change the verdict.
- extras:
  - still_advertised_by: linksvip.net (80 GB/day row), getlink.vn (150+ host list)
  - positioning: storage and backup, not retrieval
- evidence:
  - [1] 2026-10-23: 'Gói 30 ngày 59.000đ', 'Dung lượng lưu trữ 50 GB'; 'Thanh toán qua MoMo hoặc BảoKim (thẻ ATM / QR / chuyển khoản)'; 'Xin lỗi bạn, Dịch vụ đang nâng cấp'
  - [2] 2026-10-23: positioning changed to backup: 'Dịch vụ Lưu trữ & Backup dữ liệu', 'Máy chủ đặt tại Việt Nam', resume with IDM
- sources:
  - [1] https://www.4share.vn/bang-gia
  - [2] https://www.4share.vn/

## fshare's 4share.vn sibling

- `storage/fshare-s-4share-vn-sibling` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://4share.vn/bang-gia
- free tier: None reachable: 4share.vn is mid-pivot to a paid backup product: the pricing page says 'Dịch vụ đang nâng cấp' and the only purchasable plan is 50 GB / 30 days for 59,000 VND, paid via MoMo or BảoKim. A do. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 4share.vn is mid-pivot to a paid backup product: the pricing page says 'Dịch vụ đang nâng cấp' and the only purchasable plan is 50 GB / 30 days for 59,000 VND, paid via MoMo or BảoKim — a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 4share.vn is mid-pivot to a paid backup product: the pricing page says 'Dịch vụ đang nâng cấp' and the only purchasable plan is 50 GB / 30 days for 59,000 VND, paid via MoMo or BảoKim — a…
- sources:
  - [1] https://4share.vn/bang-gia
