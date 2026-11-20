# Dem-Gold

> dem-gold.ru | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dem-gold/ | JSON https://fshy.ajam.dev/api/v1/entity/dem-gold.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dem-Gold

- `debrid/dem-gold` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category debrid resale - Russian account shop (account, not key) | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.167Z (live) | stale on 2026-11-18
- url https://dem-gold.ru/catalog/real-debrid
- free tier: No free tier. 'Премиум-аккаунт Real Debrid на 90 дней (RD N°3)' 855 RUB; 'Премиум-аккаунт Real Debrid на 180 дней (RD N°4)' 1 520 RUB; instant delivery to email. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the product is titled 'premium account', not 'voucher' - the buyer receives credentials, not a code to redeem on their own account
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: the listing restates the vendor's features ('более 80 популярных серверов файлового хостинга'); no byte allowance is published by the shop | metered: no | free allowance: not published | source: [1]
- identity: email | detail: order by email; Russian rails (the site advertises a hotline and WhatsApp/Telegram support). The account's own email is the seller's. | country: Russia
- interface: rest
- limits:
  - per-ip-shaping (binding): one holder per account; the seller created the account and keeps its mailbox, so a location change needs the seller [2]
- binding note: The account is delivered with the seller's mailbox behind it; the vendor's location check sends its PIN there, so the buyer's first new-network login depends on the seller answering.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Buyer reviews on the page are short and positive (2025-08-10 to 2026-05-07), which is the seller's own wall, not an independent rating.
- notes: Vendor baseline, third-party: comparative listings lists Real-Debrid at EUR 3 / 15 days, EUR 4 / 30 days, EUR 9 / 90 days, EUR 16 / 180 days. real-debrid.com/premium returned 403 to read (exa, browserless, contextdev) and to fetch, so the vendor's own table was not read on 2026-11-03. If 1520 RUB is close to EUR 16 at the current rate, this is the only shop found selling at roughly the vendor's own price - because it is selling a hand-made account, not a voucher. The caveat is the mailbox: the buyer cannot reset the password or pass the vendor's new-location PIN without the seller.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: 90-day 855 RUB and 180-day 1520 RUB listings, 'Премиум-аккаунт' wording, and dated buyer comments on the page
  - [3] 2026-10-23: the 180-day product page at 1520 RUB and four buyer comments dated 2025-08-10 to 2025-08-27 plus one 2026-05-07 testimonial on the category page
  - [2] 2026-10-23: 
  - [1] 2026-11-03: the 90-day Real Debrid premium account is listed at 855 руб on the category page, unchanged | capture: sha256:d9e545b3a756eed774e7d799e01e668ef455817b4ae9fa41bf90c7cf28f47da8 | quote: 855 руб
  - [3] 2026-11-03: the 180-day product page is live and still titled as a premium account at 1520 руб | capture: sha256:0c8a765920e6acff18b931aa25251e7fd7cb8d44539eb4713f32fd01ec5d6e06 | quote: Премиум-аккаунт Real Debrid на 180 дней (RD N°4)
- sources:
  - [1] https://dem-gold.ru/catalog/real-debrid
  - [2] https://real-debrid.com/terms
  - [3] https://dem-gold.ru/products/premium-akkaunt-real-debrid-na-180-dnej
