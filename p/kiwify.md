# Kiwify

> kiwify.com.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kiwify/ | JSON https://fshy.ajam.dev/api/v1/entity/kiwify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kiwify

- `debrid/kiwify` | qualifies | evidence documented | binding write-gated | category checkout / payment processor used by Brazilian resellers | tier checkout
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://ajuda.kiwify.com.br/pt-br/article/o-checkout-funciona-fora-do-brasil-1cdb1ri/
- free tier: Not a service bought from the vendor. Kiwify charges the seller, not the buyer; the buyer's cost is the product price. No fee schedule was read. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a checkout, not a resource. | source: [1]
- retention: not applicable. | source: [1]
- egress: not applicable. | metered: no | source: [1]
- identity: email | detail: Email plus card for a foreign buyer. CPF and mobile are hidden outside Brazil: 'os estrangeiros nao precisam de CPF'.
- interface: rest
- limits:
  - write-gated (binding): for a foreign IP: CPF field hidden, boleto, Pix and installments disabled; card is the only path [1]
- limits note: Currency conversion is available to the seller ('Conversao automatica de moedas'), and international balances settle in USD, so the buyer is charged in a converted amount.
- binding note: A foreign buyer is not blocked, only narrowed to a card. The gate that decides is whether the buyer's card is accepted; the local rails are simply absent.
- interface detail: A hosted checkout page at pay.kiwify.com.br with a URL parameter contract: '?region=br' forces the Brazilian fields (CPF, mobile, boleto, Pix, installments) regardless of the buyer's address.
- tooling: Browser only. The buyer selects a country in the checkout, fills card details, and pays. A Brazilian buyer abroad can switch the selector back to Brazil to restore Pix and boleto.
- composes with: Kiwify is where a Brazilian reseller's R$ 24.90 lands. For a foreign buyer the chain is: checkout card (no CPF) -> seller receives -> seller delivers credentials. The card step is the only one a foreigner can complete.
- reliability: The country gate is IP-based and the buyer can override it with a URL parameter, so a Brazilian abroad keeps Pix; a foreigner cannot obtain it because the CPF field, not the IP, is the real requirement.
- notes: Kiwify is the checkout under a large share of Brazilian digital resellers, including stores that sell streaming and premium accounts. The practical consequence for debrid: a foreigner can buy from a Kiwify storefront with a card and will be charged a converted amount, but cannot use the Pix price that the listing advertises.
- evidence note: The foreign-buyer behaviour, the disabled methods, the country selector and the region parameter were read in the vendor's own help article. The accepted card brands list (Visa, Mastercard, Amex, Elo, Hipercard, Diners, Discover, Aura, JCB) is from a separate Kiwify help article dated 2023 in the index.
- extras:
  - card_brands: Visa; Mastercard; American Express; Elo; Hipercard; Diners; Discover; Aura; JCB
  - foreign_buyer_path: card only
- evidence:
  - [1] 2026-10-23: 'nos escondemos o campo de CPF e desabilitamos algumas funcionalidades como: Boleto bancario, Pix, Parcelamento' - the exact foreign-buyer restriction
  - [1] 2026-10-23: 'Adicione ?region=br na URL do seu checkout' - the override, and the statement that a Brazilian travelling abroad can re-select Brazil to get CPF, boleto, Pix and installments back
  - [2] 2026-10-23: the accepted brands: Visa, Mastercard, American Express, Elo, Hipercard, Diners, Discover, Aura, JCB
- sources:
  - [1] https://ajuda.kiwify.com.br/pt-br/article/o-checkout-funciona-fora-do-brasil-1cdb1ri/
  - [2] https://ajuda.kiwify.com.br/pt-br/article/quais-bandeiras-de-cartao-sao-aceitas-q1xzjq/
