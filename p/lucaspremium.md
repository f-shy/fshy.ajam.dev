# Lucas Contas Premium

> lucaspremium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lucaspremium/ | JSON https://fshy.ajam.dev/api/v1/entity/lucaspremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lucas Contas Premium

- `debrid/lucaspremium` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Brazilian reseller of resold Real-Debrid credentials (single product SKU, BRL) | tier Conta Oficial 30 dias
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://lucaspremium.com/conta-premium-real-debrid-30-dias-oficial/
- price BRL 24.90 per 30 days (USD 4.94 at 5.0383); not metered per TB | parsed USD 4.94/mo
- free tier: None. The store sells fixed-term credentials; there is no free or trial product for Real-Debrid. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the underlying service is Real-Debrid, whose own host and file caps apply. The reseller adds none. | source: [1]
- retention: 30 days: 'Conta Oficial do Real-debrid Por 30 dias'. After that the credential expires unless renewed through the same seller. | days: 30 | source: [1]
- egress: The reseller publishes no traffic terms. The account carries whatever Real-Debrid grants, and Real-Debrid's own account-sharing enforcement applies to a credential that several buyers may hold. | metered: no | source: [1]
- identity: email | detail: A store account and an email address are enough to order: 'Envio Imediato - Entrega automatica em Segundos'. No CPF is requested on the product page; payment methods are not listed there, so the Pix path is unverified.
- interface: rest
- limits:
  - per-ip-shaping (binding): Real-Debrid's own simultaneous-session rule; the reseller publishes none, and a resold credential is used from more than one address by construction [1]
- limits note: The product page makes no promise about concurrency, IP or password. The only consumer protection named is 'Garantia 7 dias Satisfacao ou seu dinheiro de volta', which is shorter than the 30 days sold.
- binding note: The account is sold to multiple buyers from one registration, so the first failure at any real volume is the service noticing simultaneous sessions from different addresses, not a byte quota.
- interface detail: The buyer receives Real-Debrid login credentials by email - 'voce recebera por email os dados, para utilizar direto no site do Real-debrid'. Everything after that is Real-Debrid's own web panel and API, not the reseller's.
- tooling: Real-Debrid's API and the usual add-ons work with the credential, because it is a real Real-Debrid account. The buyer does not control the recovery email.
- composes with: This is a payment rail, not a capability: it converts Pix-era Brazilian payment into a Real-Debrid session. It chains with any Stremio or torrent add-on exactly as a direct subscription would, with one extra failure point between the buyer and the service.
- reliability: The buyer holds credentials registered by somebody else and cannot recover them: the recovery email is the seller's, the password can be rotated by the seller at any time, and Real-Debrid's own terms treat use from several addresses as grounds for a block. The 7-day guarantee is the entire recourse, against a 30-day product.
- notes: The word 'Oficial' in the listing means 'a genuine Real-Debrid account' as opposed to a cracked or trial one; it does not mean the buyer becomes the account holder. Three other Brazilian storefronts - contasvip.com.br at R$ 25,00, mercadocontas.com.br at R$ 24,90 and premiumturbo.com.br with 30/90/365-day variants - carry the same product copy and the same guarantee sentence, which is the signature of one wholesale source behind several storefronts.
- evidence note: Price, term, delivery method, guarantee length and the email-credentials sentence were read on the vendor's product page. The payment methods and whether the same account is sold to several buyers are not stated there and remain unverified.
- extras:
  - fx: BRL to USD at 5.0383, Banco Central do Brasil PTAX dollar sale rate for 2026-10-22; local prices kept as stated
  - usd_30d: 4.94
  - usd_365d: 28.78
  - direct_price_reported: Real-Debrid 30 days at EUR 4.00, listed identically by three third-party price guides; real-debrid.com itself was not read
  - same_copy_storefronts: contasvip.com.br; mercadocontas.com.br; premiumturbo.com.br
- evidence:
  - [1] 2026-10-23: 'R$ 24,90', 'Conta Oficial do Real-debrid Por 30 dias', 'Envio Imediato Entrega automatica em Segundos', 'Garantia 7 dias'
  - [1] 2026-10-23: 'Apos a confirmacao do pagamento voce recebera por email os dados, para utilizar direto no site do Real-debrid' - the buyer gets credentials, not a subscription in their own name
  - [2] 2026-10-23: 'Conta Premium Real-Debrid ( 1 Ano - 365 Dias ) - Oficial' at R$ 145,00, the annual SKU from the same seller
  - [3] 2026-10-23: a Spanish-language user report of the enforcement side: 'si detectan que se usa simultaneamente desde 2 o mas IP diferentes os mandan correo de aviso y es motivo de baneo' - reported, not verified against Real-Debrid's own text
- sources:
  - [1] https://lucaspremium.com/conta-premium-real-debrid-30-dias-oficial/
  - [2] https://lucaspremium.com/conta-premium-real-debrid-1-ano-365-dias-oficial/
  - [3] https://forocoches.com/foro/showthread.php?p=474640043
