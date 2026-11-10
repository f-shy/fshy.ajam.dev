# DepositFiles

> depositfiles.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/depositfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/depositfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DepositFiles

- `debrid/depositfiles-com` | qualifies | evidence documented | binding per-ip-shaping | category file host with a paid Gold tier (Ukrainian-founded) | tier Gold
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:13:58.082Z (live) | stale on 2026-11-23
- url https://depositfiles.com/gold/payment.php
- price USD 11.95 per month at the 1-month term; USD 6.25/month at the 1-year term | parsed USD 6.25/mo
- free tier: 'Unlimited file storage time and space' and 'Maximum upload file size - 10 GB'; free downloads are the usual throttled single-connection path the Gold page contrasts with 'no speed limits'. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: Storage is unlimited; the paid tier sells download speed and concurrency, not space.
- per-object cap: Maximum upload file size - 10 GB | bytes: 10737418240 | source: [1] | note: 10 GB decimal as printed by the vendor; the byte value here treats it as 10 GiB.
- retention: 'Unlimited file storage time and space' on the home page; the Ukrainian Wikipedia article states 90 days from last download for a registered user, which is the older rule and not what the vendor page says today | source: [1] | note: The two statements disagree; the vendor's own sentence is recorded and the 90-day figure is not adopted.
- egress: Gold removes the free-tier limits: 'you can have multiple connections', 'no waiting time between downloading the file parts', 'no ADS at all'. No byte quota is published. | metered: no | free allowance: unlimited downloads at free-tier speed | source: [2]
- identity: email | detail: Sign-up with an account; Gold can be bought against the account or as a code. The checkout itself was not read, so a second gate cannot be excluded.
- interface: ftp, rest
- limits:
  - per-ip-shaping (binding): free tier: one connection, wait between parts, speed limited; Gold removes all three [2]
  - per-object-cap: 10 GB maximum upload file size [1]
- limits note: Gold prices are marked '* Indicative price stated. The final price may differ for the selected payment method.'
- binding note: At 1 TiB/month on the free tier the throttle and the single connection are what fail first; Gold removes them and publishes no byte quota, so after payment no constraint in the vocabulary was found.
- interface detail: Web download page; 'Files upload from remote HTTP or FTP servers' and 'Free Depositfiles apps' are advertised on the home page. No public API documentation was read, so the rest token is the weaker one.
- tooling: Browser, vendor apps, remote HTTP/FTP upload. Gold explicitly supports external download managers ('you can use your file manager for downloading').
- composes with: An old, still-selling host with an unlimited free storage tier; it is a place to park an archive, not a debrid - it cannot fetch from other hosts.
- reliability: Every Gold price on the page carries an 'indicative' caveat, so the amount charged can differ by payment method; the site sells through 'Local Resellers' whose terms are not on depositfiles.com.
- notes: The Ukrainian half of the debrid question: a file host founded in Ukraine that still sells to anyone with a card, at USD prices, in 2026. It is not a debrid and cannot fetch from other hosts, so its role in the stack is storage, not retrieval. The Ukrainian founding is a 2015 news fact, not a current registration.
- evidence note: All four Gold prices, the 10 GB upload cap and the Gold feature list are quoted from the live payment page today. The payment-method detail beyond 'Credit Card / PayDirect / Other methods / Local Resellers' is behind redirects and is unverified.
- evidence:
  - [2] 2026-10-23: 1 month 11.95 USD, 2 months 19.95 USD, 6 months 44.95 USD, 1 year 74.95 USD, the per-day figures, the 'indicative price' caveat, and the Gold feature list
  - [1] 2026-10-23: 'Unlimited file storage time and space', 'Maximum upload file size - 10 GB', remote HTTP/FTP upload, and 'Free Depositfiles apps'
  - [3] 2026-10-23: third-party report that the founder is a Ukrainian entrepreneur who refused to move the company to Canada (2015)
- sources:
  - [1] https://depositfiles.com/
  - [2] https://depositfiles.com/gold/payment.php
  - [3] https://news.liga.net/economics/news/osnovatel_fayloobmennika_depositfiles_otkazalsya_pokidat_ukrainu
