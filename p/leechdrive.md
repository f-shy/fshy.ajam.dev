# Leechdrive

> leechdrive.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leechdrive/ | JSON https://fshy.ajam.dev/api/v1/entity/leechdrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leechdrive

- `debrid/leechdrive` | qualifies-with-caveat | evidence documented | binding none | category shared seedbox (small slots) | tier 50GB
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://leechdrive.com/
- price USD 5 for 50 GB = USD 100/TB/month | parsed USD 100/TB-mo
- free tier: No free tier and no trial is published; the cheapest slot is USD 5/month for 50 GB. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: sold by total disk (50 GB, 100 GB, 200 GB); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [2]
- egress: 'All plans come with unmetered bandwidth' and 'With unmetered bandwidth, we do not monitor your data transfers. But if you on a shared server, you will share the network with other users.' Download 1 Gbps, upload 300 Mbps per slot, 10-16 users per server. | metered: no | free allowance: unmetered, bounded by a shared 300 Mbit/s upload | source: [2]
- identity: email | detail: Account plus payment; no free tier. No phone or document check is stated. | country: None
- interface: ftp, ftps
- limits:
  - per-ip-shaping: public-tracker upload capped at 1 MB/s (8 Mbit/s) until ratio 1.0 [2]
  - per-ip-shaping: 300 Mbit/s upload shared by 10-16 users per server [1]
- limits note: Retrieval is unmetered; the shaping applies to seeding on public trackers, and the shared 300 Mbit/s is the ceiling on what one slot can take from a busy server.
- binding note: No byte quota exists, so nothing in the vocabulary fails at 1 TiB/month. The practical limits are the 50 GB disk (20 cycles per TiB) and contention with 10-16 co-tenants, neither of which the vocabulary names.
- interface detail: 'Secure FTP access - All FTP info included in the welcome email'; 'FTP with FXP support'; 'HTTP(S) download site - A private URL to your download folder'.
- tooling: FTP/FTPS clients with FXP support (vendor names FlashFXP); ruTorrent with 30+ plugins; no rsync or API is documented
- composes with: A USD 5 slot that moves files server-to-server over FXP and serves them over HTTP(S); unmetered, so the shared 300 Mbit/s upload and 10-16 co-tenants are what a 1 TiB pull actually fights
- reliability: Public-tracker upload is shaped to 1 MB/s until ratio 1.0, so a fresh account builds ratio slowly; unmetered transfers are shared with 10-16 users per server.
- notes: Exactly USD 5, so it sits on the line rather than under it; the per-TB price is the worst and the 50 GB disk is the reason. Sustained-rate conversion: unmetered claim, so the comparable figure is the 300 Mbit/s shared upload, 37.5 MB/s aggregate across 10-16 users. The disk is first, the share second.
- evidence note: Prices, rates, protocols and the public-tracker shape are on the vendor's own home page and FAQ read. A measured rung needs a slot and a timed transfer.
- extras:
  - sustained_mbps_from_allowance: unmetered; 300 Mbit/s shared upload
  - port_gbps: 1 down / 0.3 up
  - setup_fee: none stated
  - minimum_term: monthly
  - apps: ruTorrent with 30+ plugins, OpenVPN on request, private HTTP(S) download site; no Plex or *arr is stated
  - trial_card_required: no trial exists
  - trial_restock: not applicable
- evidence:
  - [1] 2026-10-23: 50 GB at USD 5/m, 100 GB at USD 7/m, 200 GB at USD 10/m; 1 Gbps download, 300 Mbps upload; 10-16 users per Xeon E3-1220v2 server; 'Unlimited download speed, 1 MB/s (8 Mbps) upload until 1.0 ratio'
  - [2] 2026-10-23: 'Unmetered bandwidth ... we do not monitor your data transfers'; FXP and a private HTTP(S) download URL; unlimited active torrents
- sources:
  - [1] https://leechdrive.com/
  - [2] https://leechdrive.com/docs/extended-faq/
