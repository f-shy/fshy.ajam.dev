# Debrid Italia

> debriditalia.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debriditalia/ | JSON https://fshy.ajam.dev/api/v1/entity/debriditalia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debrid Italia

- `debrid/debriditalia` | qualifies-with-caveat | evidence documented | binding volume-quota | category Italian multi-hoster debrid with a 24-host list | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.167Z (live) | stale on 2026-12-04
- url https://www.debriditalia.com/
- price EUR 3,9 per 30 days on the vendor FAQ price list (a reseller page lists EUR 4,50); EUR 1,83 per month at the vendor's EUR 21,90 / 365-day chat promo
- free tier: None. The home page sells only a chat promo: 'CHAT PROMO: 365 DAYS - 21,90 euro', payable by credit card through WhatsApp or by Paysafecard/Bitcoin on request. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not stated: no per-file ceiling is published | source: [1]
- retention: generated links are valid for 72 hours from generation; nothing is stored | source: [1]
- egress: Vendor claims 'unlimited parallel downloads without waiting time'; the status page publishes a daily bandwidth figure for each host and no overall byte allowance. Server-side counter: 'Bandwidth consumption: 46,465.05 TB' across 4 servers. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Registration is required to buy; the signup form was not opened. The promo is transacted over WhatsApp, which is the only channel the vendor names for payment questions.
- interface: unknown
- limits:
  - volume-quota (binding): per-host daily bandwidth on the status page, for example 1fichier.com 30.00 GB, ddownload.com 15.00 GB, alfafile.net 10.00 GB, hotlink.cc 3.50 GB and 4shared.com 50.00 GB; the news page calls the figure per user per day; no overall byte allowance is published [2]
- limits note: The status page lists a daily bandwidth figure for each of the 24 hosts, from 3.50 GB (hotlink.cc) to 50.00 GB (4shared.com); the news page describes such a figure as per user per day ('6.00 GB al giorno per utente'). The home page claims 'unlimited parallel downloads'; no fair-use paragraph and no concurrency figure is published.
- binding note: The binding limit is the per-host daily bandwidth on the status page, from 3.50 GB (hotlink.cc) to 50.00 GB (4shared.com), described by the news page as per user per day; no overall allowance, request rate, per-object cap or concurrency figure is published.
- interface detail: Web application with a Telegram channel (@debriditalia) for announcements; no API, CLI or protocol endpoint is published on the reachable pages.
- tooling: A web downloader page and download managers: the news page names JDownloader as a download manager that works with the service, and the FAQ says the generated link can be used from any download manager software; the Telegram channel carries announcements rather than a bot interface.
- composes with: At EUR 1.83-1.96 per month of prepaid access it is the cheapest way to cover 24 European hosts, and it composes with JDownloader only insofar as the generated link is a plain HTTPS URL.
- reliability: Four servers and an Italian company number (P.I. 02707310807) behind it; payment for the annual promo runs through a WhatsApp chat rather than a card form, so a failed payment has no self-service path.
- notes: This is the cheapest effective monthly price in the sector and it appears in none of the English comparison sites; the reason is language plus payment: the annual deal is sold in an Italian WhatsApp chat, not through a checkout. The 24-host list is roughly a third of AllDebrid's, so the low price buys fewer hosts rather than cheaper bytes. Two price routes disagree (vendor EUR 21.90/year vs reseller EUR 23.90/year); the conservative number is recorded in price_per_tb_month.
- evidence note: The status page, the FAQ price list and the home page statistics are vendor pages read on 2026-11-03; a reseller page lists a different 30-day price. Identity is unverified: no signup page was found and the annual promo is paid through a chat.
- evidence:
  - [1] 2026-10-23: 'CHAT PROMO: 365 DAYS - 21,90 euro'; 'Number of servers: 4'; 'Supported hosters: 24'; 'Registered users: 94.587'; 'unlimited parallel downloads'; P.I. 02707310807
  - [3] 2026-10-23: the price ladder '15 Tage für 2.9 EUR (5.8 EUR pro Monat)', '30 Tage für 4.5 EUR', '365 Tage für 23.9 EUR (1.96 EUR pro Monat)'
  - [1] 2026-11-03: the home page counter reads 46,465.05 TB | capture: sha256:d7e00ca83bef5255dd4e003002690bbdc15da1a5eeea67a4e48f77e9e7b73cf4 | quote: Bandwidth consumption: 46,465.05 TB
  - [2] 2026-11-03: the status page lists a daily bandwidth figure per host, 3.50 GB for hotlink.cc | capture: sha256:3912f355bbf3d8cae19c313a7ed2a908bcbf9ce93af061418d21931875ede2ae | quote: | hotlink.cc | | 0.00 KB / 3.50 GB |
  - [2] 2026-11-03: the status page is the source of the per-host daily figures, 50.00 GB for 4shared.com | capture: sha256:3912f355bbf3d8cae19c313a7ed2a908bcbf9ce93af061418d21931875ede2ae | quote: | 4shared.com | | 0.00 KB / 50.00 GB |
  - [4] 2026-11-03: a host's daily limit is stated per user per day, 6.00 GB for the host announced there | capture: sha256:f08f418823fa0f294342517dbdc64dfbf282c3303e20ca4f8b0665dba1da72fe | quote: Partiamo con 6.00 GB al giorno per utente
  - [2] 2026-11-03: each host has a published daily bandwidth figure, 3.50 GB for hotlink.cc | capture: sha256:3912f355bbf3d8cae19c313a7ed2a908bcbf9ce93af061418d21931875ede2ae | quote: | hotlink.cc | | 0.00 KB / 3.50 GB |
  - [2] 2026-11-03: the status page lists 50.00 GB per day for 4shared.com among the per-host figures | capture: sha256:3912f355bbf3d8cae19c313a7ed2a908bcbf9ce93af061418d21931875ede2ae | quote: | 4shared.com | | 0.00 KB / 50.00 GB |
  - [5] 2026-11-03: a generated link allows 72 hours to complete or resume the download | capture: sha256:ef60fb0178e9affb3e18d69bd7562e624b41e73268230d6d8f7ab57318302c81 | quote: you’ve got 72 hours to complete your download
  - [4] 2026-11-03: the vendor says a premium account works through its downloader page or a download manager such as JDownloader | capture: sha256:f08f418823fa0f294342517dbdc64dfbf282c3303e20ca4f8b0665dba1da72fe | quote: usando la nostra pagina downloader oppure un download manager come JDownloader
  - [5] 2026-11-03: the vendor FAQ price list gives 3,9 euros for 30 days and 23,90 euros for 365 days | capture: sha256:ef60fb0178e9affb3e18d69bd7562e624b41e73268230d6d8f7ab57318302c81 | quote: 2,9 Euros for 15 days, 3,9 Euros for 30 days, 7,9 Euros for 70 days, 13,50 Euros for 180 days e 23,90 Euros for 365 days
  - [5] 2026-11-03: the vendor FAQ publishes a price list | capture: sha256:ef60fb0178e9affb3e18d69bd7562e624b41e73268230d6d8f7ab57318302c81 | quote: 2,9 Euros for 15 days, 3,9 Euros for 30 days, 7,9 Euros for 70 days, 13,50 Euros for 180 days e 23,90 Euros for 365 days
  - [5] 2026-11-03: the vendor publishes its own price list; the status page publishes the per-host daily figures | capture: sha256:ef60fb0178e9affb3e18d69bd7562e624b41e73268230d6d8f7ab57318302c81 | quote: 2,9 Euros for 15 days, 3,9 Euros for 30 days, 7,9 Euros for 70 days, 13,50 Euros for 180 days e 23,90 Euros for 365 days
  - [1] 2026-11-03: the chat promo for 365 days is still EUR 21,90 | capture: sha256:d7e00ca83bef5255dd4e003002690bbdc15da1a5eeea67a4e48f77e9e7b73cf4 | quote: CHAT PROMO: 365 DAYS - 21,90 euro
  - [3] 2026-11-03: a third-party table states that the service offers no Usenet downloads | capture: sha256:5ba545b85dae84ae02eb7b3f15b03a7e441d6fb5f230e34de33e388de28a7aa3 | quote: | Usenet Downloads | Nein |
  - [1] 2026-11-03: the home page sells only the chat promo for 365 days at EUR 21,90 and shows no free tier | capture: sha256:d7e00ca83bef5255dd4e003002690bbdc15da1a5eeea67a4e48f77e9e7b73cf4 | quote: CHAT PROMO: 365 DAYS - 21,90 euro
- sources:
  - [1] https://www.debriditalia.com/
  - [2] https://debriditalia.com/status.php
  - [3] https://www.myfilehoster.de/multihoster/debriditalia
  - [4] https://debriditalia.com/news.php
  - [5] https://debriditalia.com/faq.php
