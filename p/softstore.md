# SoftStore

> softstore.wixsite.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/softstore/ | JSON https://fshy.ajam.dev/api/v1/entity/softstore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SoftStore (softstore.wixsite.com)

- `debrid/softstore-alldebrid-12m` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Spanish-language reseller of resold AllDebrid credentials (12-month SKU) | tier 12 meses
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://softstore.wixsite.com/softstore/product-page/cuenta-premium-alldebrid-12-meses
- price USD 900.00 as stated by the seller, currency not printed on the page; not metered per TB
- free tier: None. The product is a paid 12-month credential; no trial or free allowance is offered by the seller. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the underlying service is AllDebrid, whose own host and file caps apply. | source: [1]
- retention: 12 months: 'Cuenta Premium AllDebrid, 12 meses'. The page does not say when the 12 months start, so a credential already running when it is sold would deliver less than a year. | days: 365 | source: [1]
- egress: The seller publishes no traffic terms. The credential inherits AllDebrid's terms, which the seller restates only as marketing: 'Maxima velocidad de descarga', 'Descargas sin periodos de espera, sin captchas ni publicidad'. | metered: no | source: [1]
- identity: email | detail: A Wix store order with an email address.
- interface: rest
- limits:
  - per-ip-shaping (binding): the seller's own rule: 'La cuenta es para uso exclusivo en una sola IP' and two devices only if they share the same connection, 'pero su uso no puede ser simultaneo' [1]
- limits note: The seller states the enforcement explicitly: 'de haber anomalias en estos puntos, la cuenta se bloqueara y se suspendera el servicio sin derecho a devolucion o garantia de reactivacion'. That is a one-IP, non-simultaneous credential sold to an unknown number of buyers.
- binding note: Nothing about bytes decides this product; the account dies the first time two buyers open it from different addresses, which the seller's own rule anticipates.
- interface detail: The buyer gets AllDebrid account details and uses AllDebrid's own panel and API. The seller ships no client.
- tooling: AllDebrid's API works because the credential is a real AllDebrid account. The seller names JDownloader, MEGAsync, MiPony and IDM as the intended clients.
- composes with: A 12-month resold credential is the longest single payment among debrid providers, which makes the seller's survival part of the product. It chains with Stremio and torrent add-ons like any AllDebrid account.
- reliability: The credential is registered by the seller, cannot be re-keyed by the buyer, is pinned to one IP, and blocks without refund on a rule breach. The seller's support promise ('Brindamos soporte tecnico ante cualquier anomalia y durante todo el tiempo contratado') is the only recourse for a 12-month term.
- notes: This is the cleanest written statement of the shared-credential model found in either language: the seller names the three things that break it - no re-keying, one IP, no simultaneous use - and prices a 12-month term against them. If '$900.00' is Mexican pesos the product is about USD 48; if it is US dollars it is twenty times the direct annual price.
- evidence note: Price, term, the no-credential-change rule, the single-IP rule and the block-without-refund clause were read on the seller's page. The currency is unverified: the page prints '$900.00' with no currency code and no country, so no USD conversion is offered.
- extras:
  - currency_status: unstated on the page; no conversion attempted
  - possible_readings: MXN 900 at 18.7613 would be USD 47.97; USD 900 would be USD 900.00; ARS 900 at 1550 would be USD 0.58 and is implausible for a 12-month SKU
  - named_clients: JDownloader; MEGAsync; MiPony; IDM
  - store_platform: Wix
- evidence:
  - [1] 2026-10-23: '$900.00 Precio' for 'Cuenta Premium AllDebrid, 12 meses'
  - [1] 2026-10-23: 'No se pueden modificar los datos de registro (Como configuraciones, usuario o contrasena)' and 'La cuenta es para uso exclusivo en una sola IP'
  - [1] 2026-10-23: 'la cuenta se bloqueara y se suspendera el servicio sin derecho a devolucion o garantia de reactivacion' - the enforcement and the absence of recourse
- sources:
  - [1] https://softstore.wixsite.com/softstore/product-page/cuenta-premium-alldebrid-12-meses
