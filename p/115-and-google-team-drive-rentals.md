# 115 and Google team-drive rentals

> Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/115-and-google-team-drive-rentals/ | JSON https://fshy.ajam.dev/api/v1/entity/115-and-google-team-drive-rentals.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 115 and Google team-drive rentals (the resale market)

- `netdisk-pan/115-team-drive-rental` | paid-only | evidence reported | binding request-rate | category resale-market
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-06
- url https://www.nodeseek.com/post-963458-1
- free tier: not a free tier: a rented Google team drive at CNY 20 per month, six months minimum, with unlimited space, a 400,000-file cap and a 750 GB per day upload cap | unit: unlimited | metered on: uploaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 400,000 files per drive, stated by the seller | source: [1]
- retention: the drive lasts as long as the underlying tenant does; the seller states no refund if the plan disappears, and one thread carries a buyer reporting that the drive vanished | source: [2]
- egress: downloads are stated as unlimited by one seller; uploads are capped at 750 GB per day per drive | metered: no | source: [1]
- identity: card | detail: CNY 20 per month, six months minimum, paid to an individual seller; the identity gate is the payment, not a registration
- interface: rest, rclone
- limits:
  - per-object-cap: 400,000 files per drive [1]
  - request-rate (binding): 750 GB per day upload per drive; 2.5 TB per day for a whole rented domain [1]
- binding note: The space is nominally unlimited and the file count is 400,000; what actually bounds a day's work is the 750 GB per day upload cap, and what bounds the arrangement is that the tenant belongs to somebody else.
- tooling: a Google Drive API client or rclone; the rental is a permission on a shared drive, not a new protocol
- composes with: the cheapest route to a pooled tenant that already exists, and the clearest evidence that an 'unlimited' Google quota is a quota being arbitraged by somebody else
- reliability: The underlying tenant is the failure point and the renter does not control it: one thread's own replies describe unlimited Workspace space as a bug-based expansion, and another carries a buyer reporting that the team drive vanished. No refund on a mid-term exit is stated in every listing read.
- notes: Signal documentation rather than a purchase route. Four listings on one forum between 2024-05 and 2026-10 quote CNY 15 to 20 per month for unlimited Google team-drive space with a 400,000-file cap and a 750 GB per day upload cap, and two of the threads argue about whether the space is a genuine plan or an expansion bug. Where a rental market exists, the underlying unlimited quota is being arbitraged, and the intermediary account is what fails.
- evidence note: the date on each evidence row is the day the post was read (2026-10-22); the post's own publication date is carried inside the proved string, because a forum post describes a moment and its age is a property of the claim and not of the reading
- extras:
  - access_mode: paid-pan
  - market: nodeseek.com transaction board
  - listings_seen: 4
  - price_range_cny_month: 15 to 20
  - file_cap: 400000
  - upload_cap_gb_day: 750
- evidence:
  - [1] 2026-10-22: a seller offers '20 元/月，半年起租', '无限空间，单盘最多 40 万个文件', '每天上传额度 750 GB', and a whole rented domain at '每个域每天上传额度 2.5 TB' (posted 2026-10-04)
  - [2] 2026-10-22: the same seller's earlier listing at the same price and the same caps, 110 days before, so the offer is repeatable and not a one-off (posted 2026-07-03)
  - [3] 2026-10-22: a different seller at '月付20块，半年起付' with '文件个数40w个，每天上传流量750G，下载不限', which corroborates both caps independently (posted 2025-06-01)
  - [4] 2026-10-22: a reply argues '200T的workspace都是卡bug扩容的', so at least one buyer believes the unlimited space is an expansion bug rather than a plan (posted 2026-07-13)
- sources:
  - [1] https://www.nodeseek.com/post-963458-1
  - [2] https://www.nodeseek.com/post-805440-1
  - [3] https://www.nodeseek.com/post-353802-1
  - [4] https://www.nodeseek.com/post-805440-2
