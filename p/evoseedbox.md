# EvoSeedbox

> evoseedbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/evoseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/evoseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EvoSeedbox

- `debrid/evoseedbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category shared seedbox with app stack | tier entry (150 GB)
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://evoseedbox.com/pricing/
- price USD 5 for 150 GB = USD 33.33/TB/month | parsed USD 33.33/TB-mo
- free tier: No free tier and no free trial: 'No contracts, 7-day money-back' is the only risk-free path. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the entry plan is USD 5/month, which is the line the sector asks about, not below it
- per-object cap: not applicable: sold by total storage, 150 GB on the entry plan up to 8 TB; no single-file cap is published | source: [2]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'unlimited downloads · metered upload bandwidth'; the FAQ says 'The monthly allowance (2-20 TB depending on plan) applies to traffic leaving the box - your FTP downloads and seeding.' Grabbing torrents into the box is unlimited; the allowance is stated as a range across plans, not per plan in the readable text. | metered: yes | free allowance: 2 TB to 20 TB per month depending on plan (range as stated; the entry plan's own figure was not in the page text) | source: [1]
- identity: email | detail: Account plus payment; no free tier, so a card or PayPal is needed. No phone or document check is stated. | country: None
- interface: ftp, sftp, rsync
- limits:
  - volume-quota (binding): 2-20 TB/month upload by plan; the allowance covers FTP downloads and seeding [1]
  - per-ip-shaping: 10 Gbps port shared per server; no per-account rate is published [2]
  - volume-quota (binding): metered upload, 2-20 TB per month depending on plan; downloads unmetered [1]
  - per-object-cap: bounded by the plan's disk: 'torrent boxes and Plex seedboxes up to 8TB' [1]
- limits note: The cheapest plan's own upload figure is the one number this record could not read: the FAQ gives the range and says most users never reach it. At 1 TiB/month the requirement is 3.39 Mbit/s sustained, which fits every plan in the range.
- binding note: The monthly upload allowance is the only byte counter; 2 TB at the bottom of the range is 6.17 Mbit/s sustained, so 1 TiB of monthly transfer uses half of the smallest allowance.
- interface detail: 'Move whole libraries in minutes over FTP, SFTP, rsync or Google Drive'; a PWA and native app drive the box.
- tooling: FTP/SFTP/rsync clients and Google Drive import; 50+ one-click apps including rclone; no published API
- composes with: A $5 150 GB box with a 2 TB-ish upload allowance; pulling 1 TiB a month fits under the allowance, so the 150 GB disk is what forces cycling rather than the counter
- reliability: The vendor discloses that upload is metered and downloads are not; the per-plan allowance is not individually stated in the page text, so a buyer learns it at checkout.
- notes: At USD 5 the entry plan is exactly the boundary, not under it, and the per-TB price is the worst. It qualifies on absolute price and on the 7-day refund, not on value per TB. Sustained-rate conversion: 2 TB/month = 6.17 Mbit/s; 1 TiB/month = 3.39 Mbit/s. The disk is the practical limit and the allowance is the priced one. cheapseedboxes.com states that EvoSeedbox and Iseedfast are its own seedbox services; they are recorded as separate brands because they have separate sites, prices and plan structures. The cheapest app-inclusive seedbox found at USD 5, but the number that matters - how much disk and how much upload the USD 5 buys - is the one the page would not give up. Treat USD 5 as the entry price and the quota as unverified until the plan cards are read in a browser.
- evidence note: Entry price, port speed, protocols, refund window and the 2-20 TB range are on the live pages read on 2026-10-23. The entry plan's exact allowance is inferred from the range; a checkout page confirms the threshold.
- extras:
  - sustained_mbps_from_allowance: 6.17 at 2 TB/month
  - port_gbps: 10
  - setup_fee: none stated
  - minimum_term: monthly, no contract; 7-day refund
  - apps: Plex, Jellyfin, Emby, Sonarr, Radarr, Prowlarr, Bazarr, Overseerr, ruTorrent, rclone, Syncthing, Tautulli, Vaultwarden, 50+ total
  - trial_card_required: no trial exists
  - trial_restock: not applicable
  - apps_listed: Plex, Jellyfin, Emby, Sonarr, Radarr, Prowlarr, Bazarr, Overseerr, ruTorrent, rclone, Syncthing, Tautulli + 40 more
  - location: Netherlands only
- evidence:
  - [1] 2026-10-23: 'from $5/mo', 10 Gbps port, 'unlimited downloads', 'metered upload bandwidth', '7-day money-back', '2-20 TB depending on plan' in the FAQ
  - [2] 2026-10-23: storage range 'from 150 GB up to 8 TB'; 'Move whole libraries in minutes over FTP, SFTP, rsync or Google Drive'; Netherlands-only hosting; 100+ one-click apps
  - [1] 2026-10-23: 'Seedbox plans from $5/mo ... up to 8TB', 'All plans: 10 Gbps network · unlimited downloads · metered upload bandwidth', the 2-20 TB upload allowance, the 50+ app list including Plex/Jellyfin/Emby/Sonarr/Radarr/Prowlarr, Netherlands-only hosting, 7-day money-back
  - [3] 2026-10-23: 'Plex is a one-click app ... runs 24/7 on our 10Gbps network', '160+ active Plex servers on our fleet', 'From $5/month'
- sources:
  - [1] https://evoseedbox.com/pricing/
  - [2] https://evoseedbox.com/
  - [3] https://evoseedbox.com/plex-seedbox/
