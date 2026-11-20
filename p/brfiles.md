# BRFiles

> brfiles.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/brfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/brfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BRFiles

- `debrid/brfiles` | qualifies-with-caveat | evidence documented | binding volume-quota | category Brazilian file host with paid premium tier (storage and download) | tier Conta Premium
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://brfiles.com/planos/
- price BRL 49.90 per month for 2 TB included = BRL 24.95/TB (USD 4.95/TB at 5.0383) | parsed USD 4.95/TB-mo
- free tier: The premium page states no free allowance. Every benefit it lists is framed as something premium removes: 'Downloads diretos sem espera', 'Site sem propagandas', 'Baixe arquivos de ate 8 GB', which implies a free tier with waiting, ads and a smaller cap. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: The free byte allowance is not on this page and was not read elsewhere on the site.
- per-object cap: 'Baixe arquivos de ate 8 GB' and 'Envie arquivos de ate 8 GB' | bytes: 8000000000 | source: [1]
- retention: 'Seus arquivos nao expiram' (premium). The page gives no day count, so retention is activity-independent while the subscription is live. | source: [1]
- egress: 'Baixe ate 2 TB por mes' on premium, with 'Downloads simultaneos' and 'Velocidade maxima'. Direct downloads, no waiting, no captcha. | metered: yes | free allowance: 2 TB per month | source: [1]
- identity: email | detail: 'Cadastre-se' requires a registration before use; the premium page does not state which fields. Payment methods are behind a 'Formas de Pagamento' footer link that was not read, so card-only versus Pix is unverified.
- interface: rest
- limits:
  - volume-quota (binding): 2 TB per month of downloads [1]
  - per-object-cap: 8 GB per file, upload and download [1]
- limits note: 2 TB of storage is included alongside 2 TB/month of downloads; the page does not say whether unused download allowance carries over.
- binding note: At 1 TiB/month this plan is inside its 2 TB allowance, so it does not fail; at 2 TiB it does. The per-file cap never binds first for an archive of typical video or dataset objects.
- interface detail: The generator-programme page states 'Gere links facilmente usando nossa API' and that a generated link can be sent straight to the customer. The public API documentation is not linked from the premium page.
- tooling: JDownloader and other managers, named on the page as a premium benefit ('Suporte a gerenciadores'). The API is offered to approved link generators, not advertised to retail buyers.
- composes with: This is the cheapest per-terabyte host in the sector at premium rates, and it is also the upstream that Brazilian generators buy from: BRFiles sells traffic at R$ 180/TB to generators while selling 2 TB/month to an end user for R$ 49.90, so buying direct undercuts every generator that resells its files.
- reliability: A single-country host: files are served from Brazilian infrastructure, and the site sells itself on avoiding international servers ('diga adeus aos servidores internacionais'). Files do not expire while premium is active, so a lapse is the loss event.
- notes: BRFiles is a host, not a multi-host: it serves only files uploaded to BRFiles. Its place among debrid providers is structural. It publishes both sides of the generator market - R$ 49.90 retail for 2 TB/month, R$ 180 wholesale per TB of generator traffic - which is the arithmetic that makes an 'unlimited' R$ 39.90 generator impossible above roughly 220 GB/month.
- evidence note: Prices, the 2 TB/month download allowance, the 2 TB of storage, the 8 GB per-file cap and the no-expiry clause were read on the vendor's premium page. Duration labels are inferred from the 'Apenas R$ X por dia' line beside each price; only the 30-day term is stated as a heading.
- extras:
  - fx: BRL to USD at 5.0383, Banco Central do Brasil PTAX dollar sale rate for 2026-10-22; local prices kept as stated
  - price_ladder_brl: 49.90; 89.90; 119.90; 199.90; 349.90
  - duration_inferred_days: 30; 60; 90; 180; 365
  - wholesale_traffic_brl_per_tb: 180.00
  - storage_included: 2 TB
- evidence:
  - [1] 2026-10-23: the price ladder: 'Plano: 1 Mes por R$ 49,90' then R$ 89,90, R$ 119,90, R$ 199,90, R$ 349,90, each with a per-day figure (1.66, 1.50, 1.33, 1.11, 0.96)
  - [1] 2026-10-23: 'Baixe ate 2 TB por mes', 'Tenha 2 TB de armazenamento', 'Baixe arquivos de ate 8 GB', 'Seus arquivos nao expiram'
  - [2] 2026-10-23: 'R$ 180,00 por cada TB de trafego', 'O trafego comprado nunca expira', 'Gere links facilmente usando nossa API', 'Emitimos Nota Fiscal para a venda de trafego' - the wholesale side of the same business
  - [3] 2026-10-23: 'Todos os pagamentos sao recebidos por deposito ou transferencia' and 'O revendedor tem controle total sobre todos os Vouchers comprados' - resale is voucher-based, which is how the Brazilian resellers obtain stock
- sources:
  - [1] https://brfiles.com/planos/
  - [2] https://brfiles.com/geradores-de-links/
  - [3] https://brfiles.com/revendedores/
