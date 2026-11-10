# Fast Down

> fast-down.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fast-down/ | JSON https://fshy.ajam.dev/api/v1/entity/fast-down.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fast Down

- `debrid/fast-down` | paid-only | evidence documented | binding per-object-cap | category file host (premium subscription, XFileSharing script) | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:25:53.695Z (live) | stale on 2026-12-04
- url https://down.fast-down.com/premium.html
- price USD 11.95 per 30 days for 1 TB of storage | parsed USD 11.95/TB-mo
- free tier: unverified: the free quota was not printed on the pages read; the upload form shows a 10240 Mb per-file limit. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The premium page lists 'Maximum Download Speed, Direct Download, No Waiting & No Captcha, 1 TB Storage' as what the paid plan adds.
- per-object cap: Max file size is 10240 Mb | bytes: 10737418240 | source: [1] | note: bytes = 10240 x 1024^2, read as megabytes on the upload form.
- retention: unverified: no retention period printed on the FAQ or premium page | source: [2]
- egress: Premium adds maximum download speed, direct download, no waiting and no captcha; no byte allowance is printed. | metered: no | free allowance: unstated | source: [3]
- identity: anonymous | detail: The upload form is on the homepage beside Login and Sign Up; the payment page lists Bitcoin, Bitcoin Cash, Litecoin, Ethereum, Webmoney and Premium.us.
- interface: unknown
- limits:
  - per-object-cap (binding): 10240 Mb per file on the upload form [1]
  - volume-quota: 1 TB storage on every paid plan [3]
- binding note: The only published number that bounds a transfer is the 10240 Mb file cap; the download volume is unpublished.
- interface detail: Web upload with remote URL upload (up to 10 URLs), copy files and a torrent leech tab.
- tooling: Browser only as read.
- composes with: Paid plans are payable in cryptocurrency, so a pull needs no card; the daily download volume is not printed.
- reliability: The torrent leech tab shows 'No live torrent server available at the moment'.
- notes: Plans: 30 days $11.95; 90 days $20.95; 180 days $44.95; 365 days $74.95; 730 days $139.99.
- evidence note: Homepage, FAQ and premium page read on 2026-11-03; the free allowance and retention are not published on them.
- extras:
  - plans: 30 days $11.95; 90 days $20.95; 180 days $44.95; 365 days $74.95; 730 days $139.99
- evidence:
  - [1] 2026-11-03: the upload form caps a file at 10240 Mb | capture: sha256:cc48902f13f9751dc386066afe285e75cef7151ef968cf711cbdbbc280356844 | quote: Max file size is 10240 Mb
  - [3] 2026-11-03: what a premium plan includes, with 1 TB storage | capture: sha256:2ce8adabb737e21ae9f508ae6ee3f0bfd2809a1a444c3b99b7f9a2ac3cc78ca8 | quote: Maximum Download Speed, Direct Download (can be activated from My Account), No Waiting & No Captcha, 1 TB Storage.
  - [3] 2026-11-03: the 30-day plan costs $11.95 | capture: sha256:2ce8adabb737e21ae9f508ae6ee3f0bfd2809a1a444c3b99b7f9a2ac3cc78ca8 | quote: $11.95
  - [1] 2026-11-03: the upload form caps a file at 10240 Mb; no free download or storage quota is printed on the page | capture: sha256:8aa20578ea78f67b7eb66ca306ce169b7656892ec3dd4eccf573a53ad321e56f | quote: Max file size is 10240 Mb
  - [3] 2026-11-03: the premium page lists No Waiting & No Captcha as what a paid plan adds, which implies a non-premium download path exists; no page states a paid-only service | capture: sha256:12d58106d4b1e7cdd99edfd024b59b0a25d15173ab8bcefd76e5fc21dcf7fdfd | quote: Maximum Download Speed, Direct Download (can be activated from My Account), No Waiting & No Captcha, 1 TB Storage.
- sources:
  - [1] https://down.fast-down.com/
  - [2] https://down.fast-down.com/faq.html
  - [3] https://down.fast-down.com/premium.html
