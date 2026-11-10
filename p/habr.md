# Habr Payment

> habr.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/habr/ | JSON https://fshy.ajam.dev/api/v1/entity/habr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Habr Payment (payment.habr.com)

- `debrid/payment-habr-com` | fails-identity | evidence documented | binding write-gated | category Russian marketplace of payment intermediaries for foreign services | tier per-seller commission
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:16:27.684Z (live) | stale on 2026-11-23
- url https://payment.habr.com/
- free tier: No free tier. The site sells nothing itself: 'и ничего не продаёт. Вы выбираете продавца, переходите на его сайт и платите там - рублями по СБП, картой российского банка или другим способом, который он предлагает.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The published offers carry commission figures such as 'Комиссия 4-5%' for a Steam top-up.
- per-object cap: not applicable: a payment marketplace | source: [1] | note: unstated
- retention: not applicable | source: [1] | note: unstated
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: Every listing names a Russian rail: 'СБП', 'Карта РФ', sometimes 'Оплата от юрлица'. No foreign-card seller was listed on the page read. | country: Russia
- interface: unknown
- limits:
  - write-gated (binding): every purchase is completed on the seller's site, with the seller's own checks [1]
- limits note: The listings seen are Steam, ruGPT, Chad AI and similar subscriptions; no debrid service was listed on the page read, so its relevance here is the commission benchmark, not a debrid route.
- binding note: No quota or rate applies. The constraint is that only Russian rails are accepted and a seller must approve each payment, which is why the record's verdict is fails-identity for a client outside Russia.
- interface detail: A catalogue of sellers; each listing links out to the seller's own site. No transaction happens on payment.habr.com.
- tooling: Browser. The value is the seller comparison: each row shows the commission and the accepted rails.
- composes with: The comparison layer above Payholder-style intermediaries; it is how a Russian buyer picks which intermediary to use for a foreign subscription, and how a researcher sees the going commission (4-5% at the low end).
- reliability: It is an advertising marketplace - the listings are marked as ads ('Далее' links carry erid tokens) - so a commission figure is the seller's offer, not a measured rate.
- notes: Included because the sector asks for the payment gate itself, and this is the clearest published benchmark for what a Russian pays to reach a foreign service: 4-5% at the cheap end. It does not sell debrid and is not a debrid provider; the record says so rather than implying otherwise.
- evidence note: The 'sells nothing' sentence, the SBP/Карта РФ rails and a 4-5% commission example are quoted from the live page today. No debrid seller was found on it, which limits what it proves about this topic.
- evidence:
  - [1] 2026-10-23: 'и ничего не продаёт ... платите там - рублями по СБП, картой российского банка', 'Комиссия 4-5%' on a Steam offer, and the 'Карта РФ / СБП' rail labels
- sources:
  - [1] https://payment.habr.com/
