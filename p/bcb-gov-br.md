# Pix

> bcb.gov.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bcb-gov-br/ | JSON https://fshy.ajam.dev/api/v1/entity/bcb-gov-br.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pix (Brazilian instant payment rail)

- `debrid/pix` | fails-identity | evidence documented | binding write-gated | category payment rail (instant bank transfer, Brazil) | tier rail
- needs card no, phone no, ID yes, institution no | verified 2026-11-03T15:29:05.335Z (live) | stale on 2026-12-04
- url https://www.bcb.gov.br/estabilidadefinanceira/pix
- free tier: Not a metered service and not a subscription. The central bank's Pix page states the fee: 'Gratuito para pessoa física e custo baixo para empresa' (free for individuals, low cost for businesses). The amount charged to businesses is not published on the page read. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The fee for individuals is free, per the central bank. The buyer-side behaviour at two checkouts is below.
- per-object cap: not applicable: a payment, not an object. | source: [1]
- retention: not applicable. A Pix charge is presented as a code with an expiry; the checkout pages read here do not publish the lifetime. | source: [2]
- egress: not applicable. | metered: no | source: [1]
- identity: national-id | detail: CPF plus an account at a Brazilian financial institution. The checkout hides the CPF field for foreign IPs and disables Pix, which is the operational proof that the rail is closed to a buyer outside Brazil. | country: Brazil
- interface: rest
- limits:
  - write-gated (binding): a current, savings or prepaid payment account at a Pix participant institution is required. At a foreign IP the Kiwify checkout hides the CPF field and disables Pix and boleto; choosing Brazil in the checkout's country selector brings back the CPF and cellphone fields and Pix [3]
- limits note: Kiwify states the exclusion from the merchant side: 'Quando um comprador acessa o checkout de fora do Brasil, nós escondemos o campo de CPF e desabilitamos o boleto bancário e o Pix.' Hotmart lists Pix under 'Métodos de pagamento exclusivos do Brasil'.
- binding note: Nothing about volume applies. A buyer without a Brazilian account cannot complete the payment at all, which is the gate that fails before any other consideration.
- interface detail: The buyer's surface is a payment code, described by Kiwify as 'um codigo unico de pagamento, podendo ser pago via ... Code ou pela opcao de Pix Copia e Cola'. Settlement is pull-based: the payer's bank app reads the code, so no card details cross the merchant.
- tooling: Any Brazilian bank app or a copy-and-paste code. There is no client the buyer must install and no credential to store, which is why Brazilian resellers prefer it.
- composes with: Pix is the rail that makes the R$ 24.90 reseller listings work: a buyer with no international card pays in seconds into a Brazilian storefront, which then buys the foreign subscription itself. The chain adds a person between the buyer and the service, and that person holds the account.
- reliability: Settlement is instant. The central bank page lists a 'Mecanismo Especial de Devolução do Pix (MED)' and a page for a mistaken Pix or a scam; the rules of that mechanism were not read. A payer travelling abroad can re-select Brazil in the checkout's country selector to get Pix back, per Kiwify, and a seller can force the Brazilian checkout with a URL parameter, so the checkout's gate follows its region setting, not the payer's location.
- notes: A payment rail is not a retrieval service, and this record exists because the debrid question cannot be answered without it: every R$ price among debrid providers is a Pix price, and Pix is the one part of the Brazilian stack a foreign buyer cannot join. The Chinese parallel is Alipay or WeChat Pay; the shape is the same, a domestic clearing rail that local storefronts build on.
- evidence note: Two checkout vendors document the rail's buyer-side gate on their own help pages, and the central bank's Pix page states the fee for individuals. The rulebook (Regulamento do Pix) and its limits were not read.
- extras:
  - buyer_gate: CPF + Brazilian bank account
  - merchant_receipt: Kiwify receives the Pix, not the seller: 'Quem recebe o Pix e a Kiwify e nao voce diretamente'
- evidence:
  - [3] 2026-10-23: 'Quando um comprador acessa o checkout de fora do Brasil, nos escondemos o campo de CPF e desabilitamos algumas funcionalidades como: Boleto bancario, Pix, Parcelamento' and 'os estrangeiros nao precisam de CPF e tambem nao podem pagar via boleto bancario, pix ou parcelado'
  - [2] 2026-10-23: 'O codigo gerado pelo checkout da Kiwify e um codigo unico de pagamento, podendo ser pago via ... Code ou pela opcao de Pix Copia e Cola' - the mechanics of the payment code
  - [4] 2026-10-23: 'Metodos de pagamento exclusivos do Brasil > Pix' - a second, independent checkout vendor classifying Pix as Brazil-only
  - [1] 2026-11-03: the central bank states Pix is free for individuals | capture: sha256:35076e0f1603cbfaf4b2c9f963563ec4d4c313cf82d38aeee5867de37a9c675d | quote: Gratuito para pessoa física e custo baixo para empresa
  - [1] 2026-11-03: the fee for individuals is stated | capture: sha256:35076e0f1603cbfaf4b2c9f963563ec4d4c313cf82d38aeee5867de37a9c675d | quote: Gratuito para pessoa física e custo baixo para empresa
  - [3] 2026-11-03: Kiwify hides the CPF field and disables boleto and Pix for a buyer outside Brazil; installments are no longer listed | capture: sha256:08b2e681e2adf042625e53c79739bd6e4674bbfaba2dea5ac0b43dc19f2a524b | quote: Quando um comprador acessa o checkout de fora do Brasil, nós escondemos o campo de CPF e desabilitamos o boleto bancário e o Pix.
  - [3] 2026-11-03: the Kiwify sentence as it reads now | capture: sha256:08b2e681e2adf042625e53c79739bd6e4674bbfaba2dea5ac0b43dc19f2a524b | quote: Quando um comprador acessa o checkout de fora do Brasil, nós escondemos o campo de CPF e desabilitamos o boleto bancário e o Pix.
  - [1] 2026-11-03: the central bank page lists a return mechanism for Pix | capture: sha256:35076e0f1603cbfaf4b2c9f963563ec4d4c313cf82d38aeee5867de37a9c675d | quote: Mecanismo Especial de Devolução do Pix (MED)
  - [3] 2026-11-03: a seller can force the Brazilian checkout (with ?region=br), so the Pix gate is the checkout's region setting | capture: sha256:08b2e681e2adf042625e53c79739bd6e4674bbfaba2dea5ac0b43dc19f2a524b | quote: Sim, é possível forçar o seu checkout a sempre exibir CPF / Celular / Boleto / Pix / Parcelamento, independente de onde o comprador esteja acessando.
  - [5] 2026-11-03: Pix needs a current, savings or prepaid payment account at a participant institution | capture: sha256:9d5cfc21cbf0c4b6adc22a3e3ae2cf4d2ea2ef6346bacc19663670b51f873b84 | quote: Qualquer pessoa física ou jurídica que tenha uma conta corrente, conta poupança ou conta de pagamento pré-paga em uma instituição participante do Pix.
  - [4] 2026-11-03: Hotmart still lists Pix under the heading of methods exclusive to Brazil | capture: sha256:4ed2204da82ec9428056ce88b845b3bf96f6261a9bc8d7e8513ce43fca14e7eb | quote: Métodos de pagamento exclusivos do Brasil
  - [1] 2026-11-03: the rail's own operator page is now read and states the fee | capture: sha256:35076e0f1603cbfaf4b2c9f963563ec4d4c313cf82d38aeee5867de37a9c675d | quote: Gratuito para pessoa física e custo baixo para empresa
  - [1] 2026-11-03: the central bank page is readable through a pinned route | capture: sha256:35076e0f1603cbfaf4b2c9f963563ec4d4c313cf82d38aeee5867de37a9c675d | quote: Gratuito para pessoa física e custo baixo para empresa
  - [3] 2026-11-03: foreign buyers need no CPF and pay by card at the Kiwify checkout | capture: sha256:08b2e681e2adf042625e53c79739bd6e4674bbfaba2dea5ac0b43dc19f2a524b | quote: Ou seja, os estrangeiros não precisam de CPF e pagam com cartão.
  - [5] 2026-11-03: Pix needs a current, savings or prepaid payment account at a participating institution; the page names no CPF requirement | capture: sha256:f558ace2fce72bcf67ed03879a251e85bf9a53d9232b80ecbfd7d05ea64bd864 | quote: Qualquer pessoa física ou jurídica que tenha uma conta corrente, conta poupança ou conta de pagamento pré-paga em uma instituição participante do Pix.
  - [3] 2026-11-03: choosing Brazil in the checkout's country selector brings back the CPF and cellphone fields and enables boleto, Pix and installments | capture: sha256:d752610a77461506110de17e9996bbffb086d43318fa492a414b01e8976fc6f7 | quote: Dessa forma os campos CPF e celular voltarão a aparecer e será possível pagar via boleto, pix ou parcelar.
  - [3] 2026-11-03: at a foreign IP the Kiwify checkout hides the CPF field and disables boleto and Pix | capture: sha256:d752610a77461506110de17e9996bbffb086d43318fa492a414b01e8976fc6f7 | quote: Quando um comprador acessa o checkout de fora do Brasil, nós escondemos o campo de CPF e desabilitamos o boleto bancário e o Pix.
- sources:
  - [1] https://www.bcb.gov.br/estabilidadefinanceira/pix
  - [2] https://ajuda.kiwify.com.br/pt-br/article/como-funciona-o-pix-1bq7o7y/
  - [3] https://ajuda.kiwify.com.br/pt-br/article/o-checkout-funciona-fora-do-brasil-1cdb1ri/
  - [4] https://suportehotmart.zendesk.com/hc/pt-br/articles/25648853025037-Quais-s%C3%A3o-os-m%C3%A9todos-de-pagamento-dispon%C3%ADveis-para-comprar-na-Hotmart
  - [5] https://www.bcb.gov.br/meubc/faqs/p/quem-pode-fazer-o-pix
