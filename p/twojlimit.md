# TwojLimit.pl

> twojlimit.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/twojlimit/ | JSON https://fshy.ajam.dev/api/v1/entity/twojlimit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TwojLimit.pl

- `debrid/twojlimit-pl` | qualifies-with-caveat | evidence documented | binding volume-quota | category Polish multi-hoster debrid, prepaid transfer with a registration credit | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:29:06.363Z (live) | stale on 2026-12-04
- url https://www.twojlimit.pl/cennik
- price PLN 327 per TB (EUR 75 at 4.3695), prepaid
- free tier: 'Otrzymujesz na start nawet 5 GB' on the home page - up to 5 GB of transfer on registration - and the header offers 'Załóż konto i wypróbuj za darmo'; the FAQ names 1 GB of free transfer, credited after the confirmation link of the registration e-mail is clicked. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: 'nawet' (up to) means 5 GB is a ceiling on the welcome credit; the FAQ names 1 GB.
- per-object cap: not stated: a transfer balance, not a per-file cap | source: [1]
- retention: not applicable: a link generator, nothing is stored | source: [1]
- egress: 'Nie ma żadnych ukrytych opłat' and 'Nie musisz kupować drogich kont premium'; transfer packs never expire ('Transfer nie wygasa') and the time packs are listed 'Bez limitu prędkości' (no speed limit). | metered: yes | free allowance: up to 5 GB at registration (1 GB per the FAQ) | price per TB: PLN 319.90 per 1000 GB on the 100 GB transfer pack (PLN 31.99 per 100 GB) | source: [2]
- identity: email | detail: The signup panel asks for login, email and password with a terms checkbox, and the login form is behind a Cloudflare Turnstile widget. Registration is free ('Rejestracja i posiadanie konta jest (i zawsze będzie) bezpłatne') and no card is asked at registration; the free transfer is credited after the confirmation link of the registration e-mail is clicked.
- interface: unknown
- limits:
  - volume-quota (binding): prepaid transfer packs that never expire: 2 GB 2,99 zł, 10 GB 6,99 zł, 100 GB 31,99 zł, 400 GB 108,99 zł; time packs: 30 days 'Do 450 GB' 42,99 zł, 360 days 'Do 5400 GB' 273,99 zł [2]
- limits note: More than 57 hosting services are bundled ('57 kont w cenie jednego'). Time packs grant a daily transfer of 15 GB for the purchased period; transfer packs never expire. No per-host daily cap, concurrency limit or fair-use paragraph is published.
- binding note: At the reported PLN 0.32/GB 1 TiB of monthly transfer is about PLN 327 (EUR 75); the balance runs out long before any rate or shaping limit could apply.
- interface detail: Web application: search a file, press download. No API, CLI or protocol endpoint is documented on the reachable pages.
- tooling: Browser only as far as the site documents; no download-manager plugin or API is named.
- composes with: The 5 GB welcome credit makes it the cheapest way to test whether Polish host coverage matches the sources before paying anything, and the per-GB price keeps it out of the base of the stack.
- reliability: The price list differs from Pobierz.biz and RapidTraffic.pl, whose pricing pages return identical content: the time-pack caps differ and the 400 GB transfer pack is priced differently; whether the three brands share one operator is unverified. The cheapest pack on the vendor price list is 2 GB for 2,99 zł, against 'już od 2 zł' on the home page.
- notes: The third Polish brand next to Pobierz.biz and RapidTraffic.pl, sharing the 100 GB pack price but with different time-pack caps and a different 400 GB price; whether it is one operator with them is unverified.
- evidence note: The welcome credit, the account count, the package prices and the FAQ are vendor-stated pages read on 2026-11-03 (/pricing, /questions and the home page). debrid.pl corroborates the 100 GB price. Anything behind the login is unverified.
- evidence:
  - [1] 2026-10-23: 'Otrzymujesz na start nawet 5 GB', '64 kont w cenie jednego - już od 2 zł', 'Nie ma żadnych ukrytych opłat'
  - [3] 2026-10-23: the package 'transfer 1 × 100 GB' at 31,99 zł, 0,32 zł/GB, in a calculator whose prices are dated 12.10.2026
  - [4] 2026-11-03: the FAQ states 1 GB of free transfer after the confirmation link is clicked | capture: sha256:1965432c0a0c642c7cc768a70aed67821f383e0f85e5fa3bc6cdbebcfb923771 | quote: Po kliknięciu na link potwierdzający, otrzymasz 1 GB darmowego transferu na przetestowanie TwojLimit.pl
  - [2] 2026-11-03: the time packs are listed with no speed limit | capture: sha256:2eb48c39e6abab4cf1beff9f3855d7825b49a9dd959dbc4f1a250eea7b0b2514 | quote: Bez limitu prędkości
  - [2] 2026-11-03: the transfer packs on the vendor price list never expire | capture: sha256:2eb48c39e6abab4cf1beff9f3855d7825b49a9dd959dbc4f1a250eea7b0b2514 | quote: Transfer nie wygasa
  - [4] 2026-11-03: time packs give a daily transfer of 15 GB | capture: sha256:1965432c0a0c642c7cc768a70aed67821f383e0f85e5fa3bc6cdbebcfb923771 | quote: W pakietach czasowych Premium użytkownik otrzymuje dobowy transfer na pobieranie plików (15 GB) przez wykupiony okres czasu.
  - [4] 2026-11-03: registration is free; downloading needs a package | capture: sha256:1965432c0a0c642c7cc768a70aed67821f383e0f85e5fa3bc6cdbebcfb923771 | quote: Rejestracja i posiadanie konta jest (i zawsze będzie) bezpłatne.
  - [5] 2026-11-03: the home page still offers up to 5 GB at the start | capture: sha256:dfea35d1f62df9756fa1523df225f55ce1a50742837c1a76c43620b7805011e4 | quote: nawet 5 GB
  - [4] 2026-11-03: the FAQ states more than 57 hosting services | capture: sha256:1965432c0a0c642c7cc768a70aed67821f383e0f85e5fa3bc6cdbebcfb923771 | quote: Zakładając konto na TwojLimit masz możliwość pobierania z ponad 57 serwisów hostingowych, bez oczekwiania oraz bez limitów prędkości.
  - [3] 2026-11-03: the third-party calculator lists the same 100 GB package at 31,99 zł | capture: sha256:5c659f64a197374c0eadb393aa1096180a9bafce3a68c314c4c2eaf24c5a286d | quote: | 1 | TwojLimit | transfer 1 × 100 GB | 31,99 zł | 31,99 zł | 0,32 zł | [Strona →](https://twojlimit.pl/) |
  - [2] 2026-11-03: the 400 GB transfer pack costs 108,99 zł here | capture: sha256:2eb48c39e6abab4cf1beff9f3855d7825b49a9dd959dbc4f1a250eea7b0b2514 | quote: 108,99 zł
  - [6] 2026-11-03: the 360-day time pack of Pobierz.biz is capped at 7200 GB; the pricing page of RapidTraffic.pl returns the same content (same capture) | capture: sha256:9075e1a624b026f6c23395b058dd7c3d6a797b52a440e565e96a758937edb0e3 | quote: - Do 7200 GB
  - [6] 2026-11-03: the 400 GB transfer pack costs 109,99 zł on Pobierz.biz and RapidTraffic.pl | capture: sha256:9075e1a624b026f6c23395b058dd7c3d6a797b52a440e565e96a758937edb0e3 | quote: 109,99 zł 0.27 zł/GB
  - [5] 2026-11-03: the home page says 'już od 2 zł' | capture: sha256:66cb55d608d42c69ee7ab89fe6b368641f8de9295661fe56906518cba96ea096 | quote: U nas masz 57 kont w cenie jednego - już od 2 zł.
  - [2] 2026-11-03: the cheapest transfer pack is priced 2,99 zł | capture: sha256:2eb48c39e6abab4cf1beff9f3855d7825b49a9dd959dbc4f1a250eea7b0b2514 | quote: 2,99 zł
  - [2] 2026-11-03: the 360-day time pack of this brand is capped at 5400 GB | capture: sha256:2eb48c39e6abab4cf1beff9f3855d7825b49a9dd959dbc4f1a250eea7b0b2514 | quote: Do 5400 GB
- sources:
  - [1] https://www.twojlimit.pl/cennik
  - [2] https://www.twojlimit.pl/pricing
  - [3] https://debrid.pl/
  - [4] https://www.twojlimit.pl/questions
  - [5] https://www.twojlimit.pl/
  - [6] https://www.pobierz.biz/pricing
