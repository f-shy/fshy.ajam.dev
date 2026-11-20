# SeedBoxBay

> seedboxbay.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedboxbay/ | JSON https://fshy.ajam.dev/api/v1/entity/seedboxbay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SeedBoxBay

- `debrid/seedboxbay` | qualifies-with-caveat | evidence documented | binding none | category shared seedbox (budget slots) | tier Minimal rTorrent Seedbox
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://seedboxbay.com/
- price USD 5 for 100 GB = USD 50/TB/month | parsed USD 50/TB-mo
- free tier: No free tier and no trial is published; the entry box is 'For $5 Per Month Only' with 100 GB and unlimited bandwidth. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: sold by total disk (100 GB / 500 GB / 1000 GB); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'Every SeedBox comes with a UNLIMITED BLAZING FAST 1GBPS connections. Download, Seed as much as you can! No limits on bandwidth, PERIOD.' The entry tier lists 'Unlimited Bandwidth' and 'SFTP & File Manager'. | metered: no | free allowance: unlimited claimed | source: [1]
- identity: email | detail: Account plus payment; a promo code ('ROCKET') is advertised for new customers. No phone or document check is stated. | country: None
- interface: sftp
- limits:
  - per-ip-shaping: 1 Gbps shared per server; no per-account rate published [1]
- limits note: No byte quota and no object cap; 'unlimited' is a claim, and the entry tier's 100 GB disk is the number a buyer can actually plan around.
- binding note: Nothing in the vocabulary fails at 1 TiB/month on the published terms; the 100 GB disk forces ten cycles and the unstated fair-use rule is the risk.
- interface detail: 'SFTP & File Manager' on the entry tier; upper tiers add root access and a dedicated IP. No rsync or API is named.
- tooling: SFTP client plus the file manager; ruTorrent WebUI; no CLI or API documented
- composes with: A USD 5 100 GB box with an SFTP pull path; the 100 GB disk is the practical limit and the 'unlimited' claim is unverifiable without an account
- reliability: 'Unlimited bandwidth, PERIOD' with no fair-use clause published; oversubscription on a shared 1 Gbps port is not observable before purchase.
- notes: Exactly USD 5 for 100 GB, the same price as Leechdrive's 50 GB, so it is the better of the two on capacity and the worse on published detail (no FAQ, no fair-use page). Sustained-rate conversion: unlimited claimed on 1 Gbps, 125 MB/s theoretical; 1 TiB/month needs 3.39 Mbit/s. Potential constraints: a fair-use cap, per-server contention, or storage-only limits; the first is not published and cannot be confirmed without buying.
- evidence note: Entry price, storage, protocol and the unlimited claim are on the live vendor page read. A measured rung needs a slot and a timed transfer.
- extras:
  - sustained_mbps_from_allowance: unlimited claimed; 1 Gbps port
  - port_gbps: 1
  - setup_fee: none stated
  - minimum_term: monthly
  - apps: ruTorrent WebUI, rTorrent; Plex tiers at USD 10 and USD 20 include root access and a dedicated IP
  - trial_card_required: no trial exists
  - trial_restock: not applicable
- evidence:
  - [1] 2026-10-23: 'Minimal rTorrent Seedbox ... 100GB Storage ... Unlimited Bandwidth ... SFTP & File Manager ... For $5 Per Month Only'; USD 10/500 GB and USD 20/1000 GB tiers with root access and dedicated IP
- sources:
  - [1] https://seedboxbay.com/
