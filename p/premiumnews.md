# Premium News

> premiumnews.de | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiumnews/ | JSON https://fshy.ajam.dev/api/v1/entity/premiumnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Premium News

- `debrid/premium-news` | paid-only | evidence documented | binding retention-clamped | category usenet provider (German, flat rates with short article retention) | tier Silber Funrate
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T15:05:36.061Z (live) | stale on 2026-12-04
- url https://premiumnews.de/
- free tier: No free tier and no trial on the price page read; the entry flat rate is EUR 12.78 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: About 35 days of article retention on the Silber flat rate, with older articles reachable by NZB file up to 600 days; the Gold flat rate is stated at up to 2 years by NZB | days: 35 | source: [1]
- egress: No volume limit and no speed limit on the three flat rates | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Fees are debited from an account each period (the price page speaks of monthly debits); the order form was not opened, so its fields are unverified: behind a sign-up.
- interface: nntp
- limits:
  - retention-clamped (binding): about 35 days on Silber; older articles by NZB file up to 600 days [1]
  - request-rate: 8 simultaneous connections on Silber [1]
- limits note: Monthly: Silber EUR 12.78, Gold EUR 17.90, Platin EUR 30.17; the minimum term is one month, auto-renewing.
- binding note: Volume and speed are unlimited, but the entry plan keeps articles only about 35 days.
- interface detail: NNTP with 256-bit SSL; Silber uses one server address and Gold three
- composes with: Retention of about 35 days on the entry plan makes it a recent-article feed only; deep archives need another provider or an NZB-backed older fetch.
- reliability: Backbone is not stated on the price page read.
- notes: Unlimited volume, priced per month; retention is the weak axis.
- evidence note: Prices and retention are from the vendor price page read on 2026-11-03; the page is in German.
- evidence:
  - [1] 2026-11-03: the entry flat rate is EUR 12.78 a month | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: SILBER FUNRATE € 12,78
  - [1] 2026-11-03: Silber retention is about 35 days, older articles by NZB up to 600 days | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: die Vorhaltezeit der Nachrichten liegt bei ca. 35 Tagen. Ältere Artikel können Sie per NZB Files bis zu 600 Tagen herunter laden.
  - [1] 2026-11-03: 8 connections on Silber | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: • 8 gleichzeitige Verbindungen
  - [1] 2026-11-03: the Gold flat rate is EUR 17.90 a month | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: GOLD FLATRATE € 17,90
  - [1] 2026-11-03: the monthly term is one month minimum | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: Die Mindestlaufzeit des Vertrags ist ein Monat.
  - [1] 2026-11-03: the monthly fee is debited from the customer's account; no free tier or trial is offered on the price page | capture: sha256:acfc4016ca6b824cab3c0254d32f38feec800793791bc756b0ac02a2b9a9d8a1 | quote: Ihr Beitrag wird monatlich von Ihrem Konto abgebucht.
  - [2] 2026-11-03: an order of six steps precedes activation; the order form fields are not on the FAQ page | capture: sha256:a4e005634b54d8c9737636e89a0af430c7fc28ee8cca2eb5ca7eb512a0ac6ad4 | quote: Die Bestellung läuft in sechs einfachen Schritten ab, so dass Sie immer die Kontrolle behalten.
- sources:
  - [1] https://premiumnews.de/preise/
  - [2] https://premiumnews.de/fragen-faq/
