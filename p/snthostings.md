# SnTHostings

> snthostings.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/snthostings/ | JSON https://fshy.ajam.dev/api/v1/entity/snthostings.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SnTHostings

- `debrid/snthostings-seedbox-starter` | paid-only | evidence documented | binding none | category shared seedbox (managed, Netherlands) | tier Starter 500GB
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-12-04
- url https://snthostings.com/seedbox/10gbps-seedbox/
- free tier: No free tier and no trial is published; the entry plan is Starter 500GB at USD 6.29/month billed monthly. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A 3-day technical guarantee gives a full refund when a fault is on the provider's side in the first 3 days.
- per-object cap: not applicable: sold by total disk (500 GB to 10 TB); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'Up to 10 Gbps shared network' and 'Unlimited bandwidth fair use'; files are pulled over SFTP, FTP or HTTPS. | metered: no | free allowance: unlimited under a fair-use rule; the rule's numbers are not published on the page read | source: [1]
- identity: email | detail: Account plus payment; the login is emailed once payment clears. Payment methods, phone and document requirements were not read: unverified. | country: None
- interface: sftp, ftp
- limits:
  - per-ip-shaping: up to 10 Gbps, shared between tenants; unlimited bandwidth under a fair-use rule [1]
- limits note: Sold by disk: 500 GB, 1 TB, 2 TB, 5 TB, 10 TB, and a custom quote from 20 TB. No byte quota or object cap is published.
- binding note: No quota, object cap or request rate is published; the shared 10 Gbps port and the unstated fair-use rule are the unmeasured risks.
- interface detail: 'SFTP/FTP/HTTPS access' on every 10Gbps seedbox, with ruTorrent, Deluge, qBittorrent, Transmission, SABnzbd and NZBGet pre-installed.
- tooling: SFTP or FTP client, a browser over HTTPS, and the one-click installer for 15+ apps; no API or CLI is documented on the page read
- composes with: A USD 6.29 500 GB seedbox with an SFTP pull path; the fair-use rule on 'unlimited' bandwidth is the unverified part
- reliability: Bandwidth is 'unlimited' under a fair-use rule whose limit is not published; the 10 Gbps port is shared.
- notes: Larger tiers on the same page: Standard 1TB USD 8.99/month, 2TB USD 15.99/month, 5TB USD 34.99/month, 10TB USD 59.99/month; yearly billing is listed at two months free.
- evidence note: Plan, price, protocols and guarantee are on the vendor page read on 2026-11-03. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: up to 10, shared
  - minimum_term: monthly
  - location: Netherlands
  - trial_card_required: no trial exists
- evidence:
  - [1] 2026-11-03: the entry plan is 500 GB at USD 6.29/month billed monthly | capture: sha256:1cdacd0e07b6328d99042af8a9e407f94e96384fe7005b7130da4f52b5332122 | quote: Starter 500GB $6.29/mo billed monthly · cancel anytime
  - [1] 2026-11-03: bandwidth is unlimited under a fair-use rule | capture: sha256:1cdacd0e07b6328d99042af8a9e407f94e96384fe7005b7130da4f52b5332122 | quote: Unlimited bandwidth fair use
  - [1] 2026-11-03: files are reachable over SFTP, FTP and HTTPS | capture: sha256:1cdacd0e07b6328d99042af8a9e407f94e96384fe7005b7130da4f52b5332122 | quote: SFTP/FTP/HTTPS access
  - [1] 2026-11-03: the login is delivered by email after payment | capture: sha256:1cdacd0e07b6328d99042af8a9e407f94e96384fe7005b7130da4f52b5332122 | quote: Instant 60-second setup — login emailed the moment your payment clears.
  - [1] 2026-11-03: a 3-day fault refund applies | capture: sha256:1cdacd0e07b6328d99042af8a9e407f94e96384fe7005b7130da4f52b5332122 | quote: 3-Day Technical Guarantee — full refund if a fault on our end in your first 3 days.
- sources:
  - [1] https://snthostings.com/seedbox/10gbps-seedbox/
