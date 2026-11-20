# Daniel Contas Vip

> contasvip.com.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/contasvip/ | JSON https://fshy.ajam.dev/api/v1/entity/contasvip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Daniel Contas Vip

- `debrid/contasvip` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category debrid resale - Brazilian account shop | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.166Z (live) | stale on 2026-11-18
- url https://www.contasvip.com.br/produto/conta-premium-real-debrid-30-dias-oficial/
- free tier: No free tier. 'Conta Premium Real-Debrid 30 Dias ( Oficial )' at R$ 25,00 and 'Conta Premium Real-Debrid ( 1 Ano - 365 Dias ) - Oficial' at R$ 150,00 (about R$ 0,41 per day), delivered as login data by email; the 90-day SKU is priced in the notes. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the 30-day product page carries zero reviews; the shop publishes a WhatsApp number for support
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance published | metered: no | free allowance: not published | source: [1]
- identity: email | detail: Brazilian checkout; delivery by email; WhatsApp support. Payment rails not itemised on the product page. | country: Brazil
- interface: rest
- limits:
  - per-ip-shaping (binding): the account's mailbox is the seller's; a new location needs a PIN sent there [2]
- binding note: R$ 25 is roughly the vendor's own month, so price is not what fails; the mailbox behind the account is.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: The '100% satisfaction or your money back' line is a replacement promise from the seller, not a vendor refund: the vendor refunds only an unused account within 7 days.
- notes: R$ 25 for 30 days is roughly the vendor's own month, so the shop is not overcharging; it is selling an account it owns. The 90-day SKU is R$ 49,90, which is about R$ 0,55 per day against R$ 0,83 per day for 30 days at R$ 25,00.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: R$ 25.00 for 30 days, the guarantee sentence, and the delivery-by-email wording
  - [2] 2026-10-23: 
  - [3] 2026-11-03: the 365-day Real-Debrid product is priced R$ 150,00 | capture: sha256:f8a8aa693f818905b3147bcb00de13a46b12820bf83a204a9651cc73205fd770 | quote: R$ 150,00
  - [4] 2026-11-03: the 90-day Real-Debrid product is priced R$ 49,90 | capture: sha256:5ca759bfee56988a60e2f7c26d5a86ad8b92ff9d1f469a8e18c7e80e5f803a4a | quote: R$ 49,90
  - [4] 2026-11-03: the 90-day Real-Debrid SKU is priced R$ 49,90 | capture: sha256:5ca759bfee56988a60e2f7c26d5a86ad8b92ff9d1f469a8e18c7e80e5f803a4a | quote: R$ 49,90
  - [3] 2026-11-03: the 365-day Real-Debrid SKU is priced R$ 150,00 | capture: sha256:f8a8aa693f818905b3147bcb00de13a46b12820bf83a204a9651cc73205fd770 | quote: R$ 150,00
  - [1] 2026-11-03: the 30-day Real-Debrid account is still priced R$ 25,00 | capture: sha256:0ad2a1841d27b614a091e4d443e9ffd2a5f1e0f2898d9baf1889c07b43e938b2 | quote: R$ 25,00
- sources:
  - [1] https://www.contasvip.com.br/produto/conta-premium-real-debrid-30-dias-oficial/
  - [2] https://real-debrid.com/terms
  - [3] https://www.contasvip.com.br/produto/conta-premium-real-debrid-1-ano-365-dias-oficial/
  - [4] https://www.contasvip.com.br/produto/conta-premium-real-debrid-90-dias-oficial/
