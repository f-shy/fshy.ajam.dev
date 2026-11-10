# Rapideo

> rapideo.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rapideo/ | JSON https://fshy.ajam.dev/api/v1/entity/rapideo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rapideo

- `debrid/rapideo-net` | qualifies-with-caveat | evidence documented | binding volume-quota | category Polish multi-hoster debrid, time-plus-volume packages | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://www.rapideo.net/
- price EUR 10.99 per 600 GB / 30 days (EUR 18.32/TB); EUR 76.99 per 7200 GB / 360 days (EUR 10.69/TB) | parsed USD 20.5/TB-mo
- free tier: 'Register for free and get 1 GB to start' and '1 GB free to start'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The 1 GB is a registration credit, not a monthly allowance.
- per-object cap: not stated: packages are capped by total volume ('up to 600 GB'), not by file size | source: [2]
- retention: not applicable: a link generator, nothing is stored | source: [2]
- egress: Time and volume sold together: a package is a period with a ceiling ('30 days up to 600 GB', '360 days up to 7200 GB'). Traffic packages are sold separately at 31 groszy per GB. | metered: yes | free allowance: 1 GB at registration | price per TB: EUR 10.99 per 30 days up to 600 GB (1.83 groszy/GB); EUR 76.99 per 360 days up to 7200 GB (1.07 groszy/GB) | source: [2]
- identity: email | detail: Registration form on the home page asks for a login, an email and a password, and a terms checkbox. No card at registration; the 1 GB credit is granted on signup.
- interface: unknown
- limits:
  - volume-quota (binding): 30-day package ceiling 600 GB; 360-day package ceiling 7200 GB [2]
- limits note: The package ceiling is the product itself; there is no separate fair-use paragraph and no concurrency figure on the pricing page.
- binding note: 600 GB in 30 days is 0.6 TB against 1 TiB of monthly transfer, so the package stops at 60 percent of the requirement; two consecutive packages would be needed and the site does not say whether they queue.
- interface detail: Web application plus 'Apps' for Smart TV; the site also runs a companion 'generator premium - lista hostingów' page. No API is documented.
- tooling: Browser, Smart TV apps and a host-list generator page; no JDownloader plugin or CLI is named on the reachable pages.
- composes with: A 30-day 600 GB package covers a single heavy week and then stops, so it composes with a monthly host subscription only as an overflow: a Polish package buys one burst and the always-on account stays elsewhere.
- reliability: Operating since 2009 and reporting 818,728 users, with a Trustpilot profile linked from the home page; the volume ceiling is what stops a heavy month, not speed.
- notes: The Polish market is priced per gigabyte, not per month, and Rapideo is the only one of the five that also sells a timed package. At 1 TiB/month the 30-day ceiling falls short by 40 percent; the 360-day package reaches EUR 10.69/TB, which is under HIGHWAY's EUR 16/TB and over AllDebrid's effective zero. Two currencies in one record: the vendor quotes EUR on the Polish page, so no conversion is needed.
- evidence note: Vendor pages read give the free credit, the host count (64), the operating history and every package price with its ceiling. What would raise it: a package bought and 600 GB pulled, which would also test whether the ceiling is enforced per calendar or per rolling 30 days.
- evidence:
  - [1] 2026-10-23: '1 GB free to start', 'We support 64 hostings', 'continuously since 2009', 'We have been trusted by 818728 users'
  - [2] 2026-10-23: the package ladder: 7 days up to 140 GB EUR 5.49; 30 days up to 600 GB EUR 10.99; 90 days up to 1800 GB EUR 27.49; 180 days up to 3600 GB EUR 43.99; 360 days up to 7200 GB EUR 76.99; traffic packages from 31 groszy/GB
- sources:
  - [1] https://www.rapideo.net/
  - [2] https://www.rapideo.net/cennik
