# NoPremium.pl

> nopremium.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nopremium/ | JSON https://fshy.ajam.dev/api/v1/entity/nopremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NoPremium.pl

- `debrid/nopremium-pl` | qualifies-with-caveat | evidence documented | binding volume-quota | category Polish multi-hoster debrid, prepaid transfer plus premium accounts | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://www.nopremium.pl/
- price PLN 363 per TB (EUR 83 at 4.3695), prepaid, no expiry stated
- free tier: 'Szybka rejestracja - 1 GB na start!' - one gigabyte of transfer on registration, then transfer is bought. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not stated: the unit is a transfer balance or a premium account, not a file size | source: [1]
- retention: not applicable: a link generator, nothing is stored | source: [1]
- egress: Two products: a transfer balance ('Najtańszy pakiet transferu 2GB kosztuje tylko 2.99 zł') and premium host accounts bought through the same account. No speed cap is stated. | metered: yes | free allowance: 1 GB at registration | price per TB: PLN 38.99 per 110 GB (reported); entry package PLN 2.99 per 2 GB | source: [1]
- identity: email | detail: Registration asks for a login and an email; the 1 GB credit is granted on signup. No card at registration.
- interface: unknown
- limits:
  - volume-quota (binding): transfer balance, entry package 2 GB for 2,99 zł; 110 GB for 38,99 zł (reported) [2]
- limits note: The vendor page gives two different host counts in the same document ('65 hostingów' in the H1 and '64 serwisów w jednym koncie' two paragraphs later); the discrepancy is recorded rather than resolved.
- binding note: At PLN 0.354/GB (38,99 / 110) 1 TiB of monthly transfer is about PLN 363, or EUR 83 at 4.3695; the balance is what stops the download, and the 1 GB registration credit is 0.1 percent of one day's stated need.
- interface detail: Web interface plus a plugin family: Stremio add-on, Android app, Amazon Fire TV, Samsung and LG Smart TV, Synology, QNAP, Kodi, FanFilm, Chrome and Firefox extensions, JDownloader2 and pyLoad. No public REST API is documented, though the plugins imply one exists.
- tooling: The widest client list of any Polish service among debrid providers: JDownloader2 and pyLoad plugins, Kodi and Stremio, two NAS packages and three TV platforms.
- composes with: The JDownloader and pyLoad plugins mean a headless box can use it without a browser, which is the one thing the pay-per-GB Poles do better than the €3-10 subscription services that ship no client at all.
- reliability: Prepaid balance with a 1 GB free start; the vendor advertises a GeoTrust certificate as its security claim, and the host count contradicts itself between the title and the body.
- notes: Cheapest free start in the Polish set after TwojLimit (1 GB vs 5 GB), and the only one with JDownloader2 and pyLoad plugins. Not a monthly subscription: at 15-30 TB/month the prepaid model costs EUR 1,200-2,500 a month, which is why the Polish services cannot be the base of the stack.
- evidence note: The 1 GB credit, the 2,99 zł entry package and the plugin list are vendor-stated and read. The 110 GB / 38,99 zł package is third-party (debrid.pl's calculator), so the per-TB figure carries that caveat.
- evidence:
  - [1] 2026-10-23: 'Szybka rejestracja - 1 GB na start!', '65 hostingów Premium', 'Najtańszy pakiet transferu 2GB kosztuje tylko 2.99 zł', and the plugin list
  - [2] 2026-10-23: the package 'transfer 1 × 110 GB' at 38,99 zł, priced 12.10.2026 by a Polish comparison calculator
- sources:
  - [1] https://www.nopremium.pl/
  - [2] https://debrid.pl/
