# eBay

> ebay.be | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ebay/ | JSON https://fshy.ajam.dev/api/v1/entity/ebay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## eBay (seller ax-metals)

- `debrid/ebay-real-debrid-accounts` | fails-identity | evidence reported | binding per-ip-shaping | category debrid resale - shared-account listing on a general marketplace | tier resale
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:57.797Z (live) | stale on 2026-11-18
- url https://www.befr.ebay.be/itm/110738621113
- free tier: No free tier. 'REAL-DEBRID - 20 JOURS - COMPTE PREMIUM - 82 HÉBERGEURS', EUR 3.99, 'Plus de 10 disponibles', sold by ax-metals (3,497 feedback, '100% d'évaluations positives'). | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: 20 days for EUR 3.99 is about EUR 0.20/day against the vendor's EUR 0.13/day at 30 days, and the listing header says 'COMPTE' (account), not voucher
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance published on the listing; the vendor's premium is what is being resold | metered: no | free allowance: not published | source: [1]
- identity: card | detail: eBay account and payment; the goods are account credentials sent by message | country: France
- interface: rest
- limits:
  - per-ip-shaping (binding): more than ten units available on one listing ('Plus de 10 disponibles'); the shared-account model puts one login behind them [1]
- binding note: This is the exact pattern the vendor's terms name: one login, many holders, connections recorded. A 20-day term is short enough that the seller may not care whether it survives.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: The page is a sold-item page: 'Vente réussie le lun. 12 sept. à 18:51. Le vendeur a remis en vente cet objet ou un objet similaire.' The date has no year, so the page does not show a current offer. Its item specifics read 'Laufzeit : 34 Tage' and list the hosts Netload, Rapidshare, Hotfile, Fileserve and Uploaded, which does not match the 20-day, 82-host title.
- notes: The lease is 20 days because that is roughly how long a multi-buyer login lasts. A single account fanned out to more than ten buyers is the strongest case among debrid providers for the vendor's 'connections are recorded' clause, and the buyer has no route to the mailbox when the reset arrives.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: EUR 3.99 for 20 days, seller ax-metals with 3,497 feedback and 100% positive, 'Plus de 10 disponibles', and the relist note
  - [2] 2026-10-23: 
  - [3] 2026-10-23: a 2026-05-28 buyer report that Real-Debrid reset the password and disabled all add-ons after connections from different countries
  - [1] 2026-11-03: the page is a sold-item page with a sale date that has no year | capture: sha256:81b059a5186b4677a5e05c7a02231e32358d6dcb48c0d9c488b650b9262006cc | quote: Vente réussie le lun. 12 sept. à 18:51. Le vendeur a remis en vente cet objet ou un objet similaire.
  - [1] 2026-11-03: the item specifics list hosts that do not match the '82 HÉBERGEURS' title, and a term of 34 days against the 20-day title | capture: sha256:81b059a5186b4677a5e05c7a02231e32358d6dcb48c0d9c488b650b9262006cc | quote: Multi-Hoster : Netload, Rapidshare, Hotfile, Fileserve, Uploaded
  - probe:www.befr.ebay.be 2026-11-03: a direct request to the listing answers HTTP 403 on 2026-11-03 | capture: sha256:1b123bca8db01a452b16e564f21baf9400e826645f4d3d4504b9b50160162338 | quote: "status": 403
  - [1] 2026-11-03: the title, price of 3,99 EUR and seller feedback text are as recorded | capture: sha256:81b059a5186b4677a5e05c7a02231e32358d6dcb48c0d9c488b650b9262006cc | quote: REAL-DEBRID - 20 JOURS - COMPTE PREMIUM - 82 HÉBERGEURS
- sources:
  - [1] https://www.befr.ebay.be/itm/110738621113
  - [2] https://real-debrid.com/terms
  - [3] https://troypointinsider.com/t/real-debrid-changed-my-password-due-to-multiple-connections/188885
