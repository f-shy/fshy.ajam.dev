# Iseedfast

> iseedfast.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iseedfast/ | JSON https://fshy.ajam.dev/api/v1/entity/iseedfast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Iseedfast

- `debrid/iseedfast` | qualifies | evidence documented | binding none | category shared seedbox (budget tiers) | tier Basic
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://iseedfast.com/
- price USD 3 for 50 GB = USD 60/TB/month | parsed USD 60/TB-mo
- free tier: No free tier and no trial is published; 'A first box' is USD 3/month for 50 GB, with a 7-day money-back guarantee and no setup fee. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: sold by total storage (50 / 100 / 250 / 600 GB); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'unlimited downloads' and 'No caps' and 'unlimited torrents' on every plan, on an 'up to 1 Gbps' uplink. The page says nothing about an upload or seeding allowance, and nothing about transfer protocol. | metered: no | free allowance: downloads stated unlimited; upload allowance not stated | source: [1]
- identity: email | detail: Account plus payment; no free tier. No phone or document check is stated. | country: None
- interface: unknown
- limits:
  - per-ip-shaping: up to 1 Gbit/s shared, claimed identical on every tier [1]
- limits note: No byte quota, no object cap and no published protocol: the honest reading is that the 50 GB disk is the binding practical limit and the retrieval method is unknown.
- binding note: Nothing in the vocabulary fails at 1 TiB/month on the published terms; the 50 GB disk forces roughly 21 cycles and the unstated retrieval protocol is the real risk.
- interface detail: The site lists ruTorrent, Deluge, qBittorrent, Transmission, Plex, Jellyfin, Sonarr and Radarr as one-click apps but does not name SFTP, FTP, rsync or any other retrieval path anywhere on the home or features page read.
- tooling: Web panel with one-click apps; retrieval client is not documented, so it must be established in the client area before relying on it
- composes with: A USD 3 box that is the cheapest per-month live offer after YourSeedbox; without a published retrieval protocol it is only usable once SFTP is confirmed at signup
- reliability: Unlimited download and unlimited torrents are claims with no published fair-use threshold; the missing retrieval protocol is a support question before purchase, not a defect after it.
- notes: The $3 tier answers 'under USD 5' on price but stores only 50 GB. Sustained-rate conversion: unlimited downloads claimed, so the comparable number is the 1 Gbit/s port, 125 MB/s; 1 TiB/month needs only 3.39 Mbit/s. Potential constraints: a hidden upload cap, an unstated protocol, or oversubscription; the first two are unstated on the page and the third is not observable without an account. cheapseedboxes.com states that EvoSeedbox and Iseedfast are its own seedbox services; they are documented as separate brands because they have separate sites, prices and plan structures.
- evidence note: Prices, port speed, app list and refund window are on the live pages read. Two things keep this below measured: no transfer protocol is published and no slot was bought.
- extras:
  - sustained_mbps_from_allowance: unlimited claimed; 1 Gbit/s port
  - port_gbps: 1
  - setup_fee: none ('No setup fee')
  - minimum_term: monthly, cancel anytime; 7-day refund
  - apps: ruTorrent, Deluge, qBittorrent, Transmission, Plex, Jellyfin, Sonarr, Radarr, one-click
  - trial_card_required: no trial exists
  - trial_restock: not applicable
- evidence:
  - [1] 2026-10-23: Basic USD 3/mo 50 GB, Standard USD 5/mo 100 GB, Advance USD 8/mo 250 GB, Pro USD 15/mo 600 GB; 'Up to 1 Gbps'; 'unlimited downloads'; 'no setup fee'; 7-day money-back
  - [2] 2026-10-23: one-click ruTorrent, Deluge, qBittorrent, Transmission, Plex, Jellyfin, Sonarr, Radarr; no retrieval protocol named
- sources:
  - [1] https://iseedfast.com/
  - [2] https://iseedfast.com/features/
