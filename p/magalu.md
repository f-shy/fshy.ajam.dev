# Magalu Cloud

> magalu.cloud | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/magalu/ | JSON https://fshy.ajam.dev/api/v1/entity/magalu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Magalu Cloud

- `compute/magalu-cloud` | fails-identity | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.magalu.cloud/docs/onboarding/get-credit
- free tier: R$ 100 in promotional credits in the first two months (R$ 50 in month 1, R$ 50 in month 2) after billing activation, and a separate R$ 300 / 30-day trial for Magalu Marketplace sellers. Egress from public IPs, NAT and NAT Gateway is currently priced 'Sem custo' (no charge) in both regions. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: egress SKUs for public IPs, NAT and NAT Gateway are listed at 'Sem custo' per GiB in both br-se1 and br-ne1, and the page states 'no momento, nenhum desses tipos de trafego esta sendo cobrado', quoted | metered: yes | source: [2]
- identity: national-id | detail: a Brazilian tax number plus a credit card: billing data requires 'Nome completo ou razao social', 'CPF ou CNPJ valido', 'Endereco de faturamento' and 'Cartao de credito valido', and the CPF/CNPJ cannot be changed after registration. Adding the card raises a verification charge quoted as 'a R$5.00 to R$9.99 verification charge' ('Adicione um cartao de credito'), which is an authorisation-scale amount rather than a published hold. Whether a debit or prepaid card passes that verification is not stated.
- interface: unknown
- limits:
  - volume-quota (binding): Billing activation requires a valid CPF or CNPJ plus a credit card, so a person without a Brazilian tax number cannot unlock the credit at all. [1]
- limits note: Billing activation requires a valid CPF or CNPJ plus a credit card, so a person without a Brazilian tax number cannot unlock the credit at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 730-hour price of R$ 34.99 on the smallest instance means R$ 100 covers roughly two and a half months of a 1 vCPU / 1 GiB box with free egress, which composes with the free-egress term if a Brazilian tax number exists.
- reliability: no reliability event recorded
- notes: The R$ 300 seller credit is the larger number and it is institution-gated twice: an active Marketplace seller account and a CNPJ. The free-egress term is the real prize here, because it removes the usual per-GiB egress cost on a regional cloud; it is stated as currently free with no commitment, so it can be withdrawn at any time. A Brazilian CPF is obtainable by a resident only; that is what makes this fails-identity rather than qualifies-with-caveat.
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: recurring-credit
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Os R$100 em creditos sao liberados automaticamente apos a ativacao de qualquer recurso: R$50 no 1o mes + R$50 no 2o', and the activation flow requires 'Adicione um cartao de credito' with a R$5.00 to R$9.99 verification charge, quoted
  - [3] 2026-10-22: billing data requires 'Nome completo ou razao social', 'CPF ou CNPJ valido', 'Endereco de faturamento', 'Cartao de credito valido', and the CPF/CNPJ cannot be changed after registration, quoted
  - [2] 2026-10-22: egress SKUs for public IPs, NAT and NAT Gateway are listed at 'Sem custo' per GiB in both br-se1 and br-ne1, and the page states 'no momento, nenhum desses tipos de trafego esta sendo cobrado', quoted
  - [4] 2026-10-22: cheapest BV instance SKU BR4100000100CB0AS0010 is 1 vCPU, 1 GB RAM, 10 GB disk at R$ 34.99 per 730 h, 'valores vigentes em 02/10/2026', quoted
  - [5] 2026-10-22: a separate seller promotion gives 'R$300 em creditos para experimentar a Magalu Cloud por 30 dias', restricted to sellers with sales in the last 12 months contracting on the registered CNPJ, quoted
- sources:
  - [1] https://docs.magalu.cloud/docs/onboarding/get-credit
  - [2] https://docs.magalu.cloud/docs/network/prices
  - [3] https://docs.magalu.cloud/docs/billing/bss/billing-info/billing-information
  - [4] https://docs.magalu.cloud/docs/computing/virtual-machine/instance-types-and-pricing/pricing
  - [5] https://universo.magalu.com/blog/artigo/magalucloud

## magalu cloud object storage (brazil)

- `storage/magalu-cloud-object-storage` | fails-egress | evidence reported | binding none | category rejected-provider
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T01:28:35.784Z (inherited) | stale on 2026-11-18
- url https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/price
- free tier: BRL 100 in promotional credits for Magalu Cloud products once the first credit card is validated, released as BRL 50 in month 1 and BRL 50 in month 2, each tranche expiring on the last day of its month; the Object Storage price page itself prints no free allowance, and usage beyond the credits is charged to the card | unit: credits | metered on: none | read on: 2026-10-30 | source: [1] | note: storage is billed per GiB stored per second and outbound transfer per GiB; regions br-se1 and br-ne1 carry the same prices
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: BRL 0.10 per GiB outbound, charged on data sent to the internet or to Magalu Cloud services in other regions; the same price in br-se1 and br-ne1 | metered: yes
- identity: card | detail: activation has four steps: document data for the invoice, a billing address, a credit card validated by a random charge of BRL 5.00 to 9.99 that is refunded, and entering that amount from the card statement; the credit is released only after the first card validates
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Storage pricing is R$0.10/GiB per month (approximately $20.39/TB/month) and egress is R$0.10/GiB, creating a 1:1 storage to egress cost ratio.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: egress
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: Object Storage is billed pay-as-you-go on actual use; the page prints no free allowance | capture: sha256:bff748b5bfd1141284ce3c9c8fbec547b1728d341f2734956334962e4f8c11f9 | quote: O modelo de cobrança do Object Storage é baseado no uso real do serviço (pay-as-you-go).
  - [1] 2026-10-30: storage is metered per GiB per second and outbound transfer per GiB | capture: sha256:bff748b5bfd1141284ce3c9c8fbec547b1728d341f2734956334962e4f8c11f9 | quote: Você paga apenas pelo que utilizar, em termos de armazenamento (por GiB armazenado por segundo) e de transferência de dados de saída (por GiB transferido).
  - [1] 2026-10-30: outbound data transfer in br-se1 costs BRL 0.10 per GiB | capture: sha256:bff748b5bfd1141284ce3c9c8fbec547b1728d341f2734956334962e4f8c11f9 | quote: | `BR4100000301OUT0011GB` | Tráfego de Dados Outbound Standard | R$ 0,10 |
  - [1] 2026-10-30: Standard storage in br-se1 costs BRL 0.10 per GiB-month (730 h) | capture: sha256:bff748b5bfd1141284ce3c9c8fbec547b1728d341f2734956334962e4f8c11f9 | quote: | `BR41000003000A00101GB` | Standard | R$ 0,000000038052 | R$ 0,000137 | R$ 0,10 |
  - [1] 2026-10-30: the listed prices are those in force on 2026-10-02 | capture: sha256:bff748b5bfd1141284ce3c9c8fbec547b1728d341f2734956334962e4f8c11f9 | quote: Vigência: valores vigentes em 02/10/2026.
  - [2] 2026-11-03: validating the first card grants BRL 100 in credits, in two BRL 50 tranches, for Magalu Cloud products | capture: sha256:8a4f4f0be4311ab327b44aa665f220edf8dd66ef9650ce6ee1d8ba1e89a69182 | quote: A validação bem-sucedida do primeiro cartão cadastrado concede ao usuário R$ 100,00 em créditos, distribuídos em duas parcelas de R$ 50,00, para uso nos produtos Magalu Cloud.
  - [3] 2026-11-03: activation requires adding a credit card | capture: sha256:58a66bebf06a6754111f36c39101c72f4363d34ff9aeab70c20c4f01a4fd6dee | quote: Adicione um cartão de crédito para cobrança.
  - [3] 2026-11-03: the card is validated by a random charge of BRL 5.00 to 9.99 | capture: sha256:58a66bebf06a6754111f36c39101c72f4363d34ff9aeab70c20c4f01a4fd6dee | quote: Por segurança, será feita uma cobrança aleatória entre R$5,00 e R$9,99 para validar seu cartão.
  - [3] 2026-11-03: the BRL 100 is released as BRL 50 in month 1 and BRL 50 in month 2 | capture: sha256:58a66bebf06a6754111f36c39101c72f4363d34ff9aeab70c20c4f01a4fd6dee | quote: Os R$100 em créditos são liberados automaticamente após a ativação de qualquer recurso: R$50 no 1º mês + R$50 no 2º.
  - [2] 2026-11-03: each BRL 50 tranche expires on the last day of its month | capture: sha256:8a4f4f0be4311ab327b44aa665f220edf8dd66ef9650ce6ee1d8ba1e89a69182 | quote: Cada parcela terá validade restrita ao mês de sua concessão, expirando automaticamente no último dia do referido mês.
  - [4] 2026-11-03: credits apply to all Magalu Cloud services | capture: sha256:b21bdd43ccce2b8754fc65fe32baa711751207e62f482b5c695983fc6ab434b2 | quote: Os créditos concedidos podem ser utilizados em todos os serviços disponíveis no Magalu Cloud.
  - [3] 2026-11-03: activation asks for document data for invoicing | capture: sha256:58a66bebf06a6754111f36c39101c72f4363d34ff9aeab70c20c4f01a4fd6dee | quote: Confirme os dados de documento para emissão da nota fiscal.
  - [5] 2026-11-03: a separate startup programme (Magalu.Up) lists BRL 1.000,00 in credits | capture: sha256:c8b1737806e1ea700e1801602d30d58cf59c945e05a64f9284ced5987ca4498f | quote: As startups estão criando suas contas na Magalu Cloud e usando R$ 1.000,00 em créditos, além de contar com consultoria de otimização de infraestrutura e suporte técnico próximo.
- sources:
  - [1] https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/price
  - [2] https://magalu.cloud/termos-legais/termo-de-validacao-de-cartao-e-concessao-de-creditos/
  - [3] https://docs.magalu.cloud/docs/onboarding/get-credit
  - [4] https://help.magalu.cloud/hc/pt-br/articles/7986097641755-Quais-servi%C3%A7os-posso-utilizar-com-os-meus-cr%C3%A9ditos
  - [5] https://magalu.cloud/magalu-up/
