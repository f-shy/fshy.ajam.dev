# Mercado Contas

> mercadocontas.com.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mercadocontas/ | JSON https://fshy.ajam.dev/api/v1/entity/mercadocontas.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mercado Contas

- `debrid/mercadocontas` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category debrid resale - Brazilian account shop (clone of the Daniel Contas Vip template) | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:50.405Z (live) | stale on 2026-11-18
- url https://www.mercadocontas.com.br/produto/conta-premium-real-debrid-30-dias-oficial/
- free tier: No free tier. 30 days R$ 24.90, SKU RB030, sold as 'Conta Oficial' delivered as login data by email. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the page carries the same description, the same guarantee sentence and the same 2023 product image filename (15172081967_6d525702a8) as contasvip.com.br
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance published; vendor premium resold | metered: no | free allowance: not published | source: [1]
- identity: email | detail: Brazilian checkout, delivery by email | country: Brazil
- interface: rest
- limits:
  - per-ip-shaping (binding): seller-held mailbox; new-location PIN goes to the seller [2]
- binding note: Same shape as contasvip at ten centavos less (R$24,90 against R$ 25,00); the binding constraint is the identity behind the login, not the price.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Two storefronts with identical copy and a shared image file are one supplier with two fronts; a warranty from either is the same warranty.
- notes: Recorded separately from contasvip because the two are separate sellers with separate checkout, and a reader comparing Brazilian shops will meet both. The clone observation is the finding: the 'oficial' label is a template, not a licence.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: R$ 24.90, SKU RB030, the guarantee sentence, and the delivery-by-email wording
  - [3] 2026-10-23: the identical description and the same image filename, which is what makes the two shops one template
  - [3] 2026-11-03: the sister storefront prices the same product at R$ 25,00 with the same description | capture: sha256:0ad2a1841d27b614a091e4d443e9ffd2a5f1e0f2898d9baf1889c07b43e938b2 | quote: R$ 25,00
  - [1] 2026-11-03: the login data is delivered by email after payment is approved | capture: sha256:2090616dd8e6005ad2bbfed06798f5b0b7b6b4daf4bf8993883fbc081d640e26 | quote: Após a confirmação do pagamento voçê receberá por email os dados
  - [1] 2026-11-03: the 30-day Real-Debrid account (SKU RB030) is priced R$24,90 | capture: sha256:2090616dd8e6005ad2bbfed06798f5b0b7b6b4daf4bf8993883fbc081d640e26 | quote: R$24,90
- sources:
  - [1] https://www.mercadocontas.com.br/produto/conta-premium-real-debrid-30-dias-oficial/
  - [2] https://real-debrid.com/terms
  - [3] https://www.contasvip.com.br/produto/conta-premium-real-debrid-30-dias-oficial/
