# Payholder.ru

> payholder.ru | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/payholder/ | JSON https://fshy.ajam.dev/api/v1/entity/payholder.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Payholder.ru

- `debrid/payholder-ru` | fails-identity | evidence documented | binding write-gated | category payment intermediary (pays foreign services for Russian and Belarusian customers) | tier per-payment commission, from RUB 290 per service
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:16:08.502Z (live) | stale on 2026-11-23
- url https://payholder.ru/
- free tier: No free tier: the service charges per payment, with a floor of 'от 290 р.' on the service list. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: 'Оплата производится по актуальному курсу и без комиссий' is the vendor's own claim, which contradicts the 'от 290 р.' floor unless the floor is a minimum order rather than a fee.
- per-object cap: not applicable: a payment, not an object | source: [2] | note: unstated
- retention: not applicable | source: [2] | note: unstated
- egress: not applicable: the customer pays in rubles and the intermediary pays the foreign service; no traffic is involved | metered: no | source: [2]
- identity: card | detail: Russian payment methods only: SBP and a Russian bank card on the gift-card page ('Способ оплаты СБП Карта РФ'), and a Russian current account for the business arm. No foreign card path is offered. | country: Russia (and Belarus, per the vendor)
- interface: unknown
- limits:
  - write-gated (binding): every order is confirmed by a manager before it is paid, so the turnaround is human [3]
- limits note: The vendor serves 'России и Беларуси' and a separate business site for legal entities; the rail is rubles from a Russian bank account or SBP.
- binding note: There is no rate or byte limit - the constraint is that a human confirms each payment and the payer needs a Russian rail. For a client outside Russia the service is unusable, which is why the verdict is fails-identity rather than a quota failure.
- interface detail: Web order form plus a manager who confirms the payment; a personal cabinet at lk.payholder.ru and a Telegram bot (@Payholders_Bot).
- tooling: Browser and Telegram. The order is processed by a person ('Оставляете заявку на payholder.ru ... специалист уточняет детали') rather than by an API.
- composes with: The bridge that makes a foreign debrid usable from Russia: pay Payholder in RUB, it pays Real-Debrid or the foreign shop, the account is credited. It is the inverse of a CIS service closed to foreigners - here the foreign service is closed to Russians and Payholder is the workaround.
- reliability: A third-party review site questions whether the service is a scam; the vendor answers with a refund promise ('Гарантируем возврат денежных средств в случае неуспешной оплаты'). Unverified either way - recorded as a claim, not as a finding.
- notes: The clearest evidence that the wall runs in both directions. A Russian cannot pay Real-Debrid directly, so a Russian intermediary exists; a foreigner cannot use that intermediary, so the two markets have separate payment paths and no single card works on both sides. The vc.ru guides date from 2026 and the service list is live; the exact fee schedule is not published, only a floor.
- evidence note: The service list, the 'от 290 р.' floor, the Russia/Belarus scope and the SBP/Карта РФ rails are quoted from live pages today. The Real-Debrid use case is reported by two vc.ru guides, not by Payholder's own service list as read.
- evidence:
  - [2] 2026-10-23: 'Посредник для оплаты зарубежных сервисов из России и Беларуси', 'Оплата производится по актуальному курсу и без комиссий', and 'Гарантируем возврат денежных средств'
  - [4] 2026-10-23: the payment methods offered are 'СБП' and 'Карта РФ' - a Russian rail only
  - [3] 2026-10-23: third-party guide titled 'Как оплатить подписку Real-Debrid из России и Беларуси через Payholder', describing the manager-confirmed order flow
  - [1] 2026-10-23: the per-service floor 'от 290 р.' repeated across the catalogue
- sources:
  - [1] https://payholder.ru/service-oplata
  - [2] https://payholder.ru/
  - [3] https://vc.ru/services/2758428-oplata-podpiski-real-debrid-cherez-payholder
  - [4] https://payholder.ru/gift-card
