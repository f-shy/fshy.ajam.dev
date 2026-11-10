# AllDebrid

> alldebrid.es | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alldebrid-2/ | JSON https://fshy.ajam.dev/api/v1/entity/alldebrid-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AllDebrid (Spanish storefront)

- `debrid/alldebrid-es` | qualifies | evidence documented | binding none | category multi-host debrid (EU operator, Spanish-language storefront, EUR) | tier Pago unico 3.99 EUR / 30 dias
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://alldebrid.es/offer/
- price EUR 3.99 per 30 days one-time (USD 4.47 at 1.1205 EUR/USD); EUR 2.99 per 30 days on subscription | parsed USD 3.35/mo
- free tier: A 7-day trial, per the trial card on the same page: '7 dias para probar nuestro servicio', 'Verificacion por SMS', 'Pueden aplicarse algunas limitaciones (uso justo)'. | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: The trial requires SMS phone verification, and the card is rendered client-side so the wording is reported from the page's index rather than read in the extracted body. The trial is not a usable path: it ends in 7 days.
- per-object cap: not applicable: files stay on the third-party host, whose own cap applies. AllDebrid publishes no per-file size on the offer page. | source: [1]
- retention: not applicable: no storage is sold. The offer page says nothing about how long a generated link stays valid. | source: [1]
- egress: No byte allowance and no per-GB price. The page sells bandwidth as a property rather than a quota: 'Disponemos de un gran numero de servidores con un bando de ancha superlativo'. The English storefront states the company caps itself at 50% of infrastructure bandwidth to keep speed for users. | metered: no | source: [1]
- identity: email | detail: Account creation plus email confirmation before subscribing: 'You must confirm your account by email before subscribing to the service'. Payment is 'Credit - Card Tarjeta de credito - Visa / Mastercard' or 'Crypto Bitcoin'. No local Latin American rail appears.
- interface: rest
- limits:
  - per-ip-shaping:  [2]
- limits note: No volume cap is published in EUR terms. The trial's 'uso justo' wording is the only admission that a fair-use ceiling exists.
- binding note: A single user on one connection downloading 1 TiB/month has no published byte cap to hit; the constraint that would fail first is the personal-use clause, and only if the account is shared. Nothing documents a volume failure at this scale.
- interface detail: The API is documented separately at docs.alldebrid.com (v4, REST, JSON). The offer page itself only sells; the credential it issues works against the API.
- tooling: REST API v4, browser plugins, mobile app, WebDAV access to the media folder, and named download managers (IDM, FDM, Mipony, Pyload).
- composes with: A single EUR 3.99 payment covers 46-70 hosts plus torrent conversion with no account-sharing requirement beyond a single account, which makes it the default benchmark every local generator and reseller among debrid providers has to beat on price or on payment access.
- reliability: The Spanish, Italian, German and Portuguese storefronts are the same operator as alldebrid.com, so a localized price is not a local entity. Payment is card or Bitcoin only; a buyer whose card is rejected has no boleto or Pix fallback on this page.
- notes: This is the reference price the local market is measured against, in the language a LatAm buyer would read. The Spanish storefront accepts the same Visa or Mastercard a Mexican or Argentine bank issues, so a foreigner with a card can pay here without any local rail - which is precisely why the R$ 24.90 reseller listings only make sense for buyers with no usable card.
- evidence note: All five prices, two payment methods, and the email confirmation requirement were read on 2026-10-23. The 7-day SMS trial is reported from search engine index snippets.
- extras:
  - fx: EUR to USD at 1.1205, ECB reference rate via Frankfurter for 2026-10-22; local prices kept as stated
  - usd_at_rate.30d_subscription: 3.35
  - usd_at_rate.30d_onetime: 4.47
  - usd_at_rate.90d: 10.07
  - usd_at_rate.180d: 17.92
  - usd_at_rate.300d: 28.00
  - hosts_claimed: 46 on the English storefront price guide, 70+ on the Portuguese guide; the offer page itself gives no count
  - payment_methods: Visa; Mastercard; Bitcoin
- evidence:
  - [1] 2026-10-23: the price ladder: '2.99 EUR / 30 dias' subscription, '3.99 EUR / 30 dias' one-time, 90 days 8.99 EUR, 180 days 15.99 EUR, 300 days 24.99 EUR
  - [1] 2026-10-23: 'Elige tu metodo de pago: Credit - Card, Tarjeta de credito - Visa / Mastercard; Crypto, Bitcoin' and 'You must confirm your account by email before subscribing'
  - [1] 2026-10-23: the subscription terms: 'Using a credit card you will be billed every 30 days automatically', cancellable, versus 'Pago unico ... no recurrente'
  - [2] 2026-10-23: 'La cuenta esta pensada para uso personal unicamente. Solo la persona fisica y propietaria de la cuenta tiene autorizacion' - the clause every resold credential breaks
- sources:
  - [1] https://alldebrid.es/offer/
  - [2] https://alldebrid.es/tos/
