# Locaweb

> locaweb.com.br | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/locaweb/ | JSON https://fshy.ajam.dev/api/v1/entity/locaweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Locaweb

- `compute/locaweb-vps` | fails-identity | evidence documented | binding none | category VPS | tier VPS 1 GB Linux
- needs card no, phone yes, ID yes, institution no | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-24
- url https://www.locaweb.com.br/vps/
- price parsed USD 4.74/mo
- free tier: no free tier; R$ 15,90 a month on a 24-month contract, renewing at R$ 23,92 a month | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: the server persists while the contract runs; the advertised monthly price assumes a 24-month commitment paid up front | source: [1]
- egress: Transferência Ilimitada (unlimited transfer) on every Linux plan in the table | metered: no | free allowance: unlimited | source: [1]
- identity: national-id | detail: a CPF is a mandatory field at checkout, alongside full name, RG, address and phone: 'Dados solicitados no momento da compra: 1. Nome completo / Razão social 2. CPF / CNPJ 3. RG 4. Endereço 5. Telefone 6. E-mail'. The checkout form itself has 'CPF 000.000.000-00' and 'Data de nascimento' as required personal… | country: BR
- interface: ssh, rest
- limits:
  - volume-quota: no traffic quota stated; transfer is unlimited [1]
- binding note: nothing in the allowance binds; the CPF demand at checkout is what actually stops a foreign registrant
- interface detail: root SSH; the vendor's web console; a REST API where documented
- tooling: any SSH client
- composes with: 2 vCPUs, 1 GB and a 40 GB SSD with unlimited transfer in Brazil for R$ 23,92 on renewal, and a CPF at checkout
- reliability: no reliability event recorded
- notes: R$ 23,92 renewing / 5.04284 = USD 4.74, under the line even after the promotion ends, and R$ 15,90 on the 24-month term is USD 3.15. The CPF is a tax number rather than a photographed document, but it is issued only to Brazilian residents and the checkout requires RG as well, so it is recorded as national-id.
- evidence note: plan price, shape, renewal and the unlimited-transfer term from the vendor's own VPS page today; the CPF requirement from the vendor's own customer-data help page
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 1
  - shape.disk_gib: 40
  - billing_model: monthly within a 24-month contract
  - term: 24 months prepaid
  - m10h_usd: 4.74
  - m24h_usd: 4.74
  - price_arithmetic: renewal R$ 23,92 / 5.04284 BRL per USD = USD 4.74; promo R$ 15,90 / 5.04284 = USD 3.15, paid as 24 x 15,90 = R$ 381,60 up front
  - renewal_usd: 4.74
  - first_term_usd: 3.15
  - fx.pair: USD/BRL
  - fx.rate: 5.04284
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS that bills whether it runs or not
  - english: no; Portuguese only
  - payment_methods: Brazilian card or boleto; not read in detail
- evidence:
  - [1] 2026-10-24: quoted: 'VPS 1 GB Linux ... R$ 29,90 47% OFF R$ 15,90/mês - 2 vCPUs - 40 GB de disco SSD - Transferência Ilimitada' and 'Valor equivalente mensal para contratação por 24 meses, por R$ 15,90. Renovação: R$ 23,92/mês.'
  - [2] 2026-10-24: quoted: 'Dados solicitados no momento da compra: 1. Nome completo / Razão social 2. CPF / CNPJ 3. RG 4. Endereço 5. Telefone 6. E-mail'
- sources:
  - [1] https://www.locaweb.com.br/vps/
  - [2] https://www.locaweb.com.br/ajuda/wiki/tudo-sobre-dados-cadastrais-e-de-cobranca-central-do-cliente/
