# DirectTorrent.me

> directtorrent.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/directtorrent/ | JSON https://fshy.ajam.dev/api/v1/entity/directtorrent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DirectTorrent.me

- `debrid/directtorrent-me` | qualifies-with-caveat | evidence documented | binding volume-quota | category torrent-to-direct-link cloud (hosted) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://directtorrent.me/
- free tier: Free plan: LKR 0 forever, 15 GB daily limit, standard speed, email support. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: Paid plans: up to 150 GB per torrent. The free plan states no per-torrent cap. | source: [1]
- retention: unverified: how long fetched files stay available is not stated | source: [1]
- egress: 15 GB daily limit on the free plan; Basic 100 GB daily, Pro 300 GB daily, Unlimited without a daily cap. | metered: yes | free allowance: 15 GB per day | source: [1]
- identity: email | detail: Registration asks for an email address, a username and a password.
- interface: unknown
- limits:
  - volume-quota (binding): free 15 GB/day; Basic 100 GB/day; Pro 300 GB/day; Unlimited [1]
  - per-object-cap: Basic, Pro and Unlimited: up to 150 GB per torrent [1]
- binding note: The daily byte limit is the stated cap on every tier below Unlimited.
- interface detail: Web account: .torrent files, magnet links and Mega.nz URLs become direct download links; streaming in the browser is listed.
- tooling: Browser only on the pages read.
- composes with: A pay-per-torrent option at LKR 1/GB sits beside the subscriptions.
- reliability: No outage observed on the day read.
- notes: Currency is the Sri Lankan rupee (LKR).
- evidence note: First-party home page and registration page; prices in Sri Lankan rupees.
- evidence:
  - [1] 2026-11-03: the free plan is 15 GB daily at standard speed | capture: sha256:915db0662c2e1920e92cd57c813f611afeadbad3ae1498ff65fdf85d49f71bd1 | quote: ### Free LKR 0/forever 15 GB daily * 15 GB daily limit * Standard speed
  - [1] 2026-11-03: the cheapest paid plan is LKR 300 per month for 100 GB daily | capture: sha256:915db0662c2e1920e92cd57c813f611afeadbad3ae1498ff65fdf85d49f71bd1 | quote: ### Basic LKR 300/month 100 GB daily
  - [1] 2026-11-03: paid plans cap one torrent at 150 GB | capture: sha256:915db0662c2e1920e92cd57c813f611afeadbad3ae1498ff65fdf85d49f71bd1 | quote: * Up to 150 GB/torrent
  - [1] 2026-11-03: pay-per-torrent is LKR 1 per GB | capture: sha256:915db0662c2e1920e92cd57c813f611afeadbad3ae1498ff65fdf85d49f71bd1 | quote: Subscribe for regular use OR pay per torrent (LKR 1/GB) for one-time downloads
  - [2] 2026-11-03: registration asks for email, username and password | capture: sha256:3195b9d51d55bbcc340e5c953429b5e71874709a28b4348e0f3c1addcb1595e6 | quote: Email Address Username Password Confirm Password
- sources:
  - [1] https://directtorrent.me/
  - [2] https://directtorrent.me/register
