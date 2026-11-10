# RapidPars

> rapidpars.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rapidpars/ | JSON https://fshy.ajam.dev/api/v1/entity/rapidpars.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RapidPars (رپیدپارس)

- `debrid/rapidpars` | paid-only | evidence documented | binding volume-quota | category premium-link generator / multi-hoster (Iran; private-tracker torrent search, usenet, Iranian download server) | tier unstated
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://www.rapidpars.com/
- free tier: No free allowance is stated on the home page. Access is sold, and the plan table sits behind the account panel; panel.rapidpars.com returned a proxy 530 on the attempt made on 2026-10-23. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: The page does state that payment is online through an Iranian Shaparak gateway ('پرداخت آنلاین با درگاه شتاب').
- per-object cap: not stated on the page read; no per-file cap is published outside the panel. | source: [1]
- retention: not stated on the page read. | source: [1]
- egress: Plans are traffic. The home page promotes downloading through the Iranian server so that the customer's ISP counts the transfer at domestic rates: 'میزان مصرف ترافیک اینترنت شما نیم بها خواهد یافت'. | metered: yes | source: [1]
- identity: email | detail: An account panel plus a Telegram bot. The registration form was not opened, so email as the minimum is inferred from the existence of the panel.
- interface: unknown
- limits:
  - volume-quota (binding): sold as traffic; the plan values are behind the panel and were not read [1]
- limits note: The home page also advertises 'جستجو' against twelve named private trackers, which is a feature a normal debrid service does not offer; it implies the vendor holds tracker accounts of its own.
- binding note: A traffic plan is by construction exhausted at some byte count, but the count is not published, so the binding value is unverified rather than absent.
- interface detail: Web panel plus a Telegram bot (@rapidpars_bot); the page says generated links work in download managers. No WebDAV, API or CLI documentation was found on the pages read.
- tooling: IDM and other download managers against the generated links; a Telegram bot for submitting jobs. No rclone backend; no public API page.
- composes with: For an Iranian client it collapses a private-tracker membership, a usenet provider and a shelf of host accounts into one rial-priced account, and hands the bytes back over domestic half-price traffic.
- reliability: The vendor's own news page carries host-side bans (an Icerbox account suspension is titled on news.rapidpars.com), which is the standard failure of a service that resells other hosts' premium accounts; the Iranian server is also a single point that has been interrupted before.
- notes: Second native Iranian multi-hoster found. Its distinguishing feature is private-tracker search, which most global debrid services do not offer because they do not hold tracker accounts. The panel domain refused network requests twice (HTTP 530), so price and quota stay unverified; that refusal is a property of the probe route, not evidence of death.
- evidence note: The feature set, the Iranian-server claim and the Shaparak payment sentence were read on the home page. The price, the traffic quota and the registration fields are unread, which is why the verdict is paid-only rather than a priced qualification.
- evidence:
  - [1] 2026-10-23: Uploaded/MediaFire/Mega and 'tens of other sites' converted to direct links; an Iranian download server billed at domestic rates; torrent search over IPTorrents, Torrentleech, TorrentDay, AvistaZ and others; usenet; 'پرداخت آنلاین با درگاه شتاب'
  - [2] 2026-10-23: The vendor's changelog and incident posts, including an Icerbox account suspension headline seen in search (headline only, post not read)
- sources:
  - [1] https://www.rapidpars.com/
  - [2] https://news.rapidpars.com/
