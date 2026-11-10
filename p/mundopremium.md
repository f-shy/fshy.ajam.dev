# Mundo Premium

> mundopremium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mundopremium/ | JSON https://fshy.ajam.dev/api/v1/entity/mundopremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mundo Premium

- `debrid/mundopremium` | qualifies | evidence documented | binding volume-quota | category Brazilian voucher reseller for host premium (BRFiles, TakeFile and others) | tier Conta Premium BRFiles Individual
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://mundopremium.com/produto/conta-premium-brfiles-individual/
- price BRL 29.90 to BRL 249.90 depending on term (USD 5.93 to USD 49.60 at 5.0383); the exact per-term grid is behind a variant selector that did not render
- free tier: None. The store sells vouchers only. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the voucher activates BRFiles premium, so BRFiles' own 8 GB per-file cap applies. | source: [1]
- retention: The voucher buys a period of BRFiles premium; the seller prices 30 days up to a year inside 'R$ 29,90 atraves R$ 249,90'. Files then follow BRFiles' own no-expiry rule while premium is active. | source: [1]
- egress: No egress terms of its own: the voucher activates the host's premium, which carries 'Baixe ate 2 TB por mes' at BRFiles. | metered: yes | free allowance: 2 TB per month, from BRFiles | source: [2]
- identity: email | detail: The buyer's own email, login and password are used at the host: 'O periodo premium e resgatado em seu e-mail, login e senha pessoal, voce pode alterar estes dados sempre que desejar.' That sentence is the difference between this product and a resold credential.
- interface: unknown
- limits:
  - volume-quota (binding): the host's 2 TB per month, unchanged by the reseller [2]
- limits note: The seller's own constraint is delivery time: 'Prazo Entrega: Alguns minutos, no maximo 12 horas, apos a confirmacao do pagamento'. A voucher bought in a hurry can arrive after the need.
- binding note: The voucher changes nothing about the host's limits; at 1 TiB/month the BRFiles 2 TB allowance holds, at 2 TiB it does not.
- interface detail: The deliverable is a text voucher code, not an account: 'voce ira receber um Voucher (codigo) com este codigo acessara o site BRFiles.com e criara uma nova conta ou renovara uma conta ja existente'. The code is redeemed in the host's own panel.
- tooling: Nothing to install. The buyer redeems the code at brfiles.com/planos/ and keeps using the host's own site and download managers.
- reliability: Voucher delivery is manual and can take up to 12 hours. A voucher that fails to redeem is a support ticket, not a lockout, because the account remains the buyer's.
- notes: Mundo Premium is the counter-example that makes the debrid main distinction usable. Same product category as the R$ 24.90 Real-Debrid listings - a cheap way to hold premium - but delivered as a voucher into an account the buyer controls. It also sells TakeFile at R$ 289.90 to R$ 1,069.90, so the catalogue covers hosts the multi-hosts do not.
- evidence note: The voucher mechanism, the price range, the delivery window and the buyer-owned-account sentence were read on the product page. The per-duration price grid did not render, so only the range is given.
- extras:
  - fx: BRL to USD at 5.0383, Banco Central do Brasil PTAX dollar sale rate for 2026-10-22; local prices kept as stated
  - usd_range: 5.93 to 49.60
  - delivery: manual, up to 12 hours
  - delivery_model: voucher code redeemed on the host's own site
  - other_hosts_seen: TakeFile; Turbobit
- evidence:
  - [1] 2026-10-23: 'Faixa de preco: R$ 29,90 atraves R$ 249,90' and 'Nao e Gerador de Link. Conta Individual, acesso direto ao BRFiles, sem espera'
  - [1] 2026-10-23: 'voce ira receber um Voucher (codigo) ... e criara uma nova conta ou renovara uma conta ja existente' and 'o periodo premium e resgatado em seu e-mail, login e senha pessoal'
  - [1] 2026-10-23: 'Prazo Entrega: Alguns minutos, no maximo 12 horas, apos a confirmacao do pagamento'
- sources:
  - [1] https://mundopremium.com/produto/conta-premium-brfiles-individual/
  - [2] https://brfiles.com/planos/
