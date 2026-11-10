# Zendesk

> zendesk.com | Debrid, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zendesk/ | JSON https://fshy.ajam.dev/api/v1/entity/zendesk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hotmart

- `debrid/hotmart` | qualifies | evidence documented | binding write-gated | category checkout / payment processor used by Brazilian and Spanish-language resellers | tier checkout
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://suportehotmart.zendesk.com/hc/pt-br/articles/25648853025037-Quais-s%C3%A3o-os-m%C3%A9todos-de-pagamento-dispon%C3%ADveis-para-comprar-na-Hotmart
- free tier: Not a service bought from the vendor. Hotmart charges the seller; the buyer pays the product price, with 'taxas especificas que podem ser aplicadas a compras internacionais e de produtos digitais'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a checkout. | source: [1]
- retention: not applicable. | source: [1]
- egress: not applicable. | metered: no | source: [1]
- identity: email | detail: Email plus a card. The global card section asks only for 'numero do cartao, nome do titular, data de vencimento e CVV'.
- interface: rest
- limits:
  - write-gated (binding): method availability is set per product by the seller and varies by buyer country; Pix and boleto are listed as Brazil-only [1]
- limits note: The article states that not all methods reach all buyers: 'cada pais possui taxas especificas que podem ser aplicadas a compras internacionais'.
- binding note: The gate is which methods the seller enabled and which ones the buyer's country allows; a card is the only method that crosses both.
- interface detail: A hosted checkout that adapts by country and converts currency automatically: 'o checkout da Hotmart faz a conversao automatica do valor do seu produto para a moeda do seu comprador'. The seller chooses which methods to enable per product.
- tooling: Browser only, plus subscription and installment products. No client needed.
- composes with: Hotmart is the Spanish- and Portuguese-language checkout most likely to be in front of a reseller that also sells to Spain, Mexico or Argentina, because it settles in more than 180 countries and converts the price. It is the payment path a foreigner is most likely to complete without a Brazilian document.
- reliability: Installments are charged once by Hotmart and split by the buyer's bank, so a refund does not cancel the installments directly with the issuer: 'Depois da aprovacao, nao e possivel cancelar as parcelas diretamente com a operadora.'
- notes: Documented as a rail, not as a provider: its role among debrid providers is to answer whether a foreigner can pay a Brazilian or Spanish reseller. The answer is yes by card, in a converted currency, subject to the seller having enabled a global method for that product.
- evidence note: The method inventory, the 180-country reach, the global card fields and the Pix-is-Brazil-only classification were read in Hotmart's own help article, updated 2026-10-19.
- extras:
  - countries: 180+
  - methods: 20+
  - brazil_only_methods: Pix; boleto
  - article_updated: 2026-10-19
- evidence:
  - [1] 2026-10-23: 'mais de 20 metodos de pagamento, alcancando compradores em mais de 180 paises'
  - [1] 2026-10-23: 'Metodos de pagamento exclusivos do Brasil > Pix', which places Pix on the Brazilian side of the divide
  - [1] 2026-10-23: the global card path and the installment caveat: 'nao e possivel cancelar as parcelas diretamente com a operadora'
- sources:
  - [1] https://suportehotmart.zendesk.com/hc/pt-br/articles/25648853025037-Quais-s%C3%A3o-os-m%C3%A9todos-de-pagamento-dispon%C3%ADveis-para-comprar-na-Hotmart

## Zendesk Guide (help center article attachments)

- `storage/zendesk-guide` | trial-only | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zendesk.com
- free tier: 'Each article has no limit on overall storage or total number of attached files.' Per-file 20 MB. But account-level file storage is separately capped at 10 GB base + 2 GB/agent (Team). The article-level 'no limit' sits inside that account bucket. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unranged-open. Article attachments are served from `support.zendesk.com/hc/article_attachments/<id>` with no auth, no referer check, `Accept-Ranges: bytes`, `Access-Control-Allow-Origin` permissive, `x-amz-replication-status: COMPLETED`, AES256 at rest. | metered: no
- identity: institution
- interface: rest, cli
- limits:
  - per-object-cap (binding): 20 MB per file [1]
- limits note: Per-object-cap: 20 MB per file/image in articles (2 MB for community images). Quota: account file storage 10 GB base + 2 GB/agent. request-rate: Guide API is rate limited; an unauthenticated write probe `POST /api/v2/help_center/articles.json` returned 403 (good. No open write). Retention: archived tickets still count toward storage.
- interface detail: rest
- tooling: Help Center API (`/api/v2/help_center/articles/{id}/attachments.json` returns the public `content_url`). Third-party CLI `tukaelu/zgsync` adds a Guide media subcommand.
- composes with: 20 MB per file x unbounded attachments per article, but the 10 GB account file-storage pool is the wall. Trial-only for a free account, so the multiplier is trial instances, which is a bad trade.
- reliability: The read path is the cleanest in this whole niche. Public, ranged, unauthenticated, no expiry. But Zendesk has no free plan (14-day trial), so it cannot be a free-storage answer, only a pattern to copy.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Each article has no limit on overall storage or total number of attached files.' Per-file 20 MB. But account-level file storage is separately capped at 10 GB base + 2 GB/agent (Team) — the article-level 'no limit' sits inside that account bucket.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: ... — 'Articles: 20MB limit per file or image upload' and 'Each article has no limit on overall storage or total number of attached files'
  - [3] 2026-10-21: default storage '10 GB base' + '2 GB per agent' (Team)
  - [4] 2026-10-21: probe: GET -> 200, 365,146 bytes, image/png, no referer/UA needed (also 200 with `curl/8`), `Range: bytes=0-99` -> 206
  - withheld 2026-10-21: probe: 8 parallel ranged GETs x 45,000 B -> all 206, 360,000 B in 0.63 s
- sources:
  - [1] https://support.zendesk.com/hc/en-us/articles/4408884048794-What-are-the-attachment-limits-and-supported-file-types-in-my-help-center
  - [2] https://support.zendesk.com/hc/en-us/articles/4408884048794-
  - [3] https://support.zendesk.com/hc/en-us/articles/4408835043994-Managing-data-storage-in-your-Zendesk-account
  - [4] https://support.zendesk.com/hc/article_attachments/11203045835930

## streamable (as a durable store)

- `storage/streamable-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://streamable-support.zendesk.com/hc/en-us/articles/35415717293204-Free-Plan-Limits
- free tier: None reachable: Listed as a candidate for completeness but the 90-day auto-deletion is disqualifying on its own. A storage target that erases content on a timer is not storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Listed as a candidate for completeness but the 90-day auto-deletion is disqualifying on its own — a storage target that erases content on a timer is not storage.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Listed as a candidate for completeness but the 90-day auto-deletion is disqualifying on its own — a storage target that erases content on a timer is not storage.
- sources:
  - [1] https://streamable-support.zendesk.com/hc/en-us/articles/35415717293204-Free-Plan-Limits
