# iLoad USENET

> iload-usenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iload-usenet/ | JSON https://fshy.ajam.dev/api/v1/entity/iload-usenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iLoad USENET

- `debrid/iload-usenet` | trial-only | evidence documented | binding volume-quota | category usenet provider (German-language, volume, flat-rate and prepaid tariffs with a 7-day trial) | tier Volume from 12 GB
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.iload-usenet.com/
- free tier: A free 7-day test access that needs only an email address: 'Testzugang, den du ohne Einschraenkungen eine Woche lang nutzen kannst'; the access closes automatically after 7 days. Its data allowance is not stated. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: The trial runs for 7 days; the unit list has no 'days' term, so the nearest term is none with the period named here.
- per-object cap: source: [2]
- retention: 7.785 days of retention on the home page ('derzeit 7.785 Tagen') | days: 7785 | source: [3]
- egress: Volume tariffs of 12 to 240 GB a month, flat-rate tariffs of 1 to 25 MBit plus an Unlimited tariff, and prepaid volumes | metered: yes | free allowance: 7-day test access | source: [2]
- identity: email | detail: The home page offers 'Jetzt kostenlos testen!' with an email-address field, and the trial page says the access details are sent to the email address. Whether a card or phone is asked for is unverified: behind a sign-up.
- interface: nntp
- limits:
  - volume-quota (binding): 12 to 240 GB each month on the volume tariffs [2]
  - retention-clamped: 7.785 days of retention [3]
- limits note: Volume tariffs from EUR 4.95 a month, flat-rate tariffs from EUR 4.95 a month, prepaid from EUR 4.99; the page's prices are listed with 'ab' (from).
- binding note: The cheapest tariffs are volume-bound (12 GB a month at the entry); the Unlimited flat-rate is a higher tier.
- interface detail: NNTP with free SSL; the vendor ships its own client and search index
- composes with: Three tariff types (volume, flat-rate, prepaid) with an entry price near EUR 5.
- reliability: Backbone is not stated on the pages read.
- notes: The trial allowance and its card requirement are unverified.
- evidence note: Entry prices, the trial and retention are from the vendor pages read on 2026-11-03; the pages are in German.
- evidence:
  - [1] 2026-11-03: the trial access ends after 7 days | capture: sha256:d9b1e52897519106fd3313f2b3d0eefcece5beef5beea600114c448eee27b949 | quote: Der Zugang wird nach 7 Tagen automatisch geschlossen.
  - [3] 2026-11-03: a free test is offered on the home page | capture: sha256:cd7bb84af4a3e202b08950e52d6158c5c5b27e8ac947eb9fd116b92b83793151 | quote: ### Jetzt kostenlos testen!
  - [3] 2026-11-03: the free test form asks for an email address | capture: sha256:cd7bb84af4a3e202b08950e52d6158c5c5b27e8ac947eb9fd116b92b83793151 | quote: E-Mail-Adresse:
  - [3] 2026-11-03: retention is stated as 7.785 days | capture: sha256:cd7bb84af4a3e202b08950e52d6158c5c5b27e8ac947eb9fd116b92b83793151 | quote: die längste Vorhaltezeit von derzeit 7.785 Tagen
  - [2] 2026-11-03: the volume and flat-rate tariffs start at EUR 4.95 a month | capture: sha256:73a194dd3c8433315e4120cb3b5efa138cf69c4fe9e38edfe316354ed29b8592 | quote: ## *€*4,95
  - [2] 2026-11-03: the volume tariffs run from 12 to 240 GB a month | capture: sha256:73a194dd3c8433315e4120cb3b5efa138cf69c4fe9e38edfe316354ed29b8592 | quote: - 12-240 GB jeden Monat
- sources:
  - [1] https://www.iload-usenet.com/trial
  - [2] https://www.iload-usenet.com/prices
  - [3] https://www.iload-usenet.com/
