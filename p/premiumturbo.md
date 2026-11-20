# Premium Turbo

> premiumturbo.com.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiumturbo/ | JSON https://fshy.ajam.dev/api/v1/entity/premiumturbo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Premium Turbo

- `debrid/premiumturbo` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category debrid resale - Brazilian account shop (price by variant, not published until selection) | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:50.410Z (live) | stale on 2026-11-18
- url https://www.premiumturbo.com.br/produto/conta-premium-real-debrid-oficial/
- free tier: No free tier. 'Conta Premium Real-debrid ( Oficial )' with a duration selector of 30 days / 90 days / 1 year; no price is printed until a variant is chosen, so no number was readable. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: rated '5.00 de 5' from 1 customer review on the page
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance published; 'Envio automático para acesso imediato, segundos após confirmaçao do pagamento' | metered: no | free allowance: not published | source: [1]
- identity: email | detail: Brazilian checkout, WhatsApp support, automatic delivery after payment confirmation | country: Brazil
- interface: rest
- limits:
  - per-ip-shaping (binding): seller-held mailbox behind the account [2]
  - write-gated: price visible only after choosing a duration; one review is the entire rating base [1]
- binding note: The shop is one of the three Brazilian fronts selling the same account shape; nothing about its price can be compared because it publishes none until checkout.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: A single five-star review and a hidden price are the two weakest signals in the Brazilian set.
- notes: A dash is the finding: the duration selector exists but the page prints no price, so a buyer cannot compare it before checkout. The product is otherwise the contasvip shape.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: the 30/90/365-day selector, the 5.00/5 rating from 1 review, and the absence of any printed price
  - [1] 2026-11-03: the rating is 5.00 of 5 from one customer review | capture: sha256:3e11c1fc1af0a0bd5fe81a62e9a4000453c4cf58fe30097c256edb3ec6486c68 | quote: Avaliado como 5.00 de 5, com baseado em 1 avaliação de cliente
  - [1] 2026-11-03: delivery is automatic seconds after payment confirmation | capture: sha256:3e11c1fc1af0a0bd5fe81a62e9a4000453c4cf58fe30097c256edb3ec6486c68 | quote: Envio automático para acesso imediato, segundos após confirmaçao do pagamento!
  - [1] 2026-11-03: the account duration selector offers 30 days, 90 days and 1 year and no price is printed | capture: sha256:3e11c1fc1af0a0bd5fe81a62e9a4000453c4cf58fe30097c256edb3ec6486c68 | quote: 30 dias, 90 dias, 1 Ano
- sources:
  - [1] https://www.premiumturbo.com.br/produto/conta-premium-real-debrid-oficial/
  - [2] https://real-debrid.com/terms
