# Zbigz

> zbigz.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zbigz/ | JSON https://fshy.ajam.dev/api/v1/entity/zbigz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zbigz

- `debrid/zbigz` | fails-quota | evidence documented | binding per-object-cap | category torrent-to-cloud fetcher | tier free-account
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:54:40.000Z (live) | stale on 2026-11-23
- url https://m.zbigz.com/payment
- price free tier; premium price not published on the page read
- free tier: Free account: maximum file size 20 GB, 2 torrents, files kept 7 days, limited download speed, limited storage size, no streaming. A guest gets 20 GB, 1 torrent, limited speed, and nothing is stated about retention. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: the vendor's own plan table; the free row is deliberately blank for several cells
- per-object cap: 'Max file size 20 GB' on both Guest and Free account rows; 'Unlimited' on Premium. | bytes: 20000000000 | source: [1] | note: 20 GB decimal; a 20 GiB torrent is 21.47 GB and therefore over the cap, if the vendor means GB and not GiB
- retention: 'Files kept for 7 days' on the free account; the guest row is blank; Premium is 'Unlimited'. | days: 7 | source: [1]
- egress: Free is 'Download speed Limited' with no number; Premium is 'Download speed Unlimited'. No byte allowance is stated on any row. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: guest use needs nothing: 'ZbigZ can be used absolutely free and without registrations.' A free account is an email and password.
- interface: rest
- limits:
  - per-object-cap (binding): 20 GB per torrent on guest and free accounts [1]
  - pull-count: 2 torrents at once on a free account, 1 as a guest [1]
  - retention-clamped: free files are removed after 7 days [1]
- limits note: the vendor publishes no byte quota and no API rate limit; older reviews report a 150 KB/s free speed cap and a 1 GB free file limit, both contradicted by the current plan table, which was read.
- binding note: A 20 GiB torrent sits just above the 20 GB free cap, so the size check is what fails first, before the 7-day clock or the two-torrent slot count.
- interface detail: HTTPS download from the 'My Files' page; no API is documented anywhere on the site, only a browser UI and a browser extension.
- tooling: browser only; no API, no CLI, no rclone backend. A wrapper would have to drive the web session.
- composes with: the account-free guest route makes it the fastest way to test whether a 20 GB torrent is fetchable at all, before paying anyone; the 7-day retention rules it out as storage.
- reliability: the plan table leaves storage size and guest retention blank, and the site's numbers have changed without any changelog; the interface is dated and there is no support channel named.
- notes: The one free tier among debrid providers whose published per-file cap (20 GB) is within a few percent of the 20 GiB case, and the only one usable with no account at all. Whether a 21.47 GB torrent is rejected depends on GB versus GiB, which the vendor does not say.
- evidence note: the plan comparison table was read on the mobile payment page, which is the only page carrying it (zbigz.com/payment renders only a headline). The 20 GB versus 20 GiB boundary is untested.
- extras:
  - guest_no_account: yes
  - api: none documented
- evidence:
  - [1] 2026-10-23: the Guest / Free account / Premium table: 'Max file size 20 GB | 20 GB | Unlimited', 'Number of torrents 1 | 2 | Unlimited', 'Files kept for - | 7 days | Unlimited'
  - [2] 2026-10-23: 'ZbigZ can be used absolutely free and without registrations. No actions required.'
  - [3] 2026-10-23: reported: premium is unlimited storage and unlimited file size at about $9.99/month; the older 1 GB free cap is contradicted by the vendor table
- sources:
  - [1] https://m.zbigz.com/payment
  - [2] https://zbigz.com/page/faq
  - [3] https://www.rapidseedbox.com/blog/10-top-alternatives-to-seedr-cc
