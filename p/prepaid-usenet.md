# Prepaid-Usenet

> prepaid-usenet.de | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prepaid-usenet/ | JSON https://fshy.ajam.dev/api/v1/entity/prepaid-usenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prepaid-Usenet

- `debrid/prepaid-usenet` | qualifies-with-caveat | evidence documented | binding volume-quota | category usenet provider (German, prepaid non-expiring blocks) | tier Prepaid blocks
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.prepaid-usenet.de/
- free tier: A free 10 GB test account: 'einen kostenlosen 10GB-Testaccount' after email confirmation and an SMS activation code; no cost and no cancellation needed. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The test needs an email address and a phone able to receive an SMS code.
- per-object cap: source: [2]
- retention: Retention of up to over 1800 days | days: 1800 | source: [2]
- egress: Prepaid volume blocks; the volume does not lapse at month end | metered: yes | free allowance: 10 GB test account | source: [2]
- identity: any-phone | detail: Registration sends a confirmation email and then an SMS code that unlocks the test ('erhalten Sie per SMS einen Freischaltcode'); no card is asked for the test and the vendor says it needs no bank or card data for prepaid purchases.
- interface: nntp
- limits:
  - volume-quota (binding): 10 GB test account; paid blocks from 5 GB to 500 GB (third-party index) [1]
  - retention-clamped: up to over 1800 days [2]
- limits note: The vendor pages read show no block price; the 5 GB to 500 GB range and 10 connections are from a third-party index.
- binding note: Every product is a fixed number of GB, 10 GB in the free test.
- interface detail: NNTP with 256-bit SSL (third-party index)
- composes with: The 10 GB test can be topped up in the customer center at any time; an unused account just rests, so the free 10 GB is a standing test of the service.
- reliability: Backbone is not stated on the vendor pages read.
- notes: The free 10 GB is a one-off test, not a recurring allowance; the caveat is the SMS step and that the cheapest paid block price is third-party.
- evidence note: The test, retention and identity are from the vendor pages read on 2026-11-03; block prices are third-party.
- evidence:
  - [1] 2026-11-03: the test account carries 10 GB at no cost | capture: sha256:7b94afe4a9ec52b685a8a1523d8e45ee270c0271ee66b2a1dfb421f070b6811c | quote: Sie haben dann einen kostenlosen 10GB-Testaccount, den Sie mit dem vollen Funktionsumfang von Prepaid-Usenet nutzen können.
  - [1] 2026-11-03: the test needs an email confirmation and then an SMS activation code | capture: sha256:7b94afe4a9ec52b685a8a1523d8e45ee270c0271ee66b2a1dfb421f070b6811c | quote: Nach der E-Mail-Bestätigung erhalten Sie per SMS einen Freischaltcode.
  - [2] 2026-11-03: retention is stated as up to over 1800 days | capture: sha256:3b003ed3d30659531b3db69321cc0b8967d8a59a173469e833a99e7625b74f61 | quote: Wir bieten Ihnen als Usenet-Provider eine Retention, die Vorhaltezeit von Inhalten im Usenet, von bis über 1800 Tagen.
  - [2] 2026-11-03: the test is free with no subscription behind it | capture: sha256:3b003ed3d30659531b3db69321cc0b8967d8a59a173469e833a99e7625b74f61 | quote: Bei Prepaid-Usenet haben wir es nicht nötig Sie in eine Abofalle zu locken, welche sich hinter einem Testzugang versteckt. Testen Sie unseren Zugang kostenlos - ohne Kosten, ohne Kündigung, ohne Wenn und Aber.
  - [2] 2026-11-03: prepaid purchases need no bank, direct-debit or card data | capture: sha256:3b003ed3d30659531b3db69321cc0b8967d8a59a173469e833a99e7625b74f61 | quote: Wir benötigen keine Bankdaten, Lastschriftdaten oder Kreditkarte.
  - [3] 2026-11-03: a third-party index gives the block range 5 GB to 500 GB and 10 connections | capture: sha256:c20dd909187d56863fa88fcd715d0198e4d86a117ccb71e6bbc2baf45b53e981 | quote: Prepaid Usenet is a German provider based exclusively on prepaid data packages with no expiration — no subscription, no minimum term. Blocks from 5 GB to 500 GB, over 1,800 days retention, 10 connections, 256-bit SSL, 100,000+ newsgroups, EU servers, 10 GB demo via SMS. 14-day statutory right of withdrawal.
- sources:
  - [1] https://www.prepaid-usenet.de/registration/1
  - [2] https://www.prepaid-usenet.de/
  - [3] https://www.usenet.org/providers/prepaidusenet
