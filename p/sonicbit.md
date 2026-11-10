# SonicBit

> sonicbit.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sonicbit/ | JSON https://fshy.ajam.dev/api/v1/entity/sonicbit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SonicBit

- `debrid/sonicbit` | qualifies-with-caveat | evidence documented | binding volume-quota | category torrent-to-cloud seedbox and drive | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.sonicbit.net/seedr-alternative
- price USD 14.99 per month for 1 TB | parsed USD 14.99/TB-mo
- free tier: '4 GB FREE forever · No credit card required'. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: A legacy dashboard page also lists the free tier as '4 GB of Storage, Max. torrent download slot: 2, Seeding Speed: 0.5 MB/s'.
- per-object cap: not stated on the pages read | source: [2]
- retention: not stated on the pages read | source: [2]
- egress: Plans are sold by storage, not by transfer; the vendor's comparison table quotes storage tiers only and says nothing about a download allowance. Paid plans add 'Seeding 8 MB/s · ratio 10:1' on the top tier. | metered: no | free allowance: no transfer figure published | source: [2]
- identity: email | detail: 'No credit card required' for the free 4 GB account; an email registration at my.sonicbit.net/register. Payment is by card at upgrade, with a promo code in circulation ('10YEARSONICBIT', up to 60% off).
- interface: sftp, ftp, rest
- limits:
  - volume-quota (binding): 4 GB free; 50 GB $1.99; 100 GB $3.49; 250 GB $6.49; 500 GB $9.99; 1 TB $14.99; 10 TB $59.99 [2]
  - per-ip-shaping: free tier seeding speed 0.5 MB/s, 2 concurrent torrent slots [3]
- limits note: Storage is sold in fixed tiers with no top-up and no published transfer allowance, so a client buys the tier above what it needs or none.
- binding note: 4 GB free fails 1 TiB by a factor of 256 on storage alone, before any transfer question. On the paid side 1 TB at $14.99 still cannot hold a 1 TiB working set, so the tier below 10 TB always binds.
- interface detail: The plan table lists 'Remote access · SFTP / FTP / RPC' on the 1 TB tier, and the site advertises 'AI API' and an apps layer (Plex, Jellyfin, Sonarr, n8n) on top of the drive. The API endpoint itself was not read.
- tooling: rclone-over-SFTP is the obvious mount for the paid tiers; the site states SFTP, FTP and RPC access. No official client was read.
- composes with: The Seedr shape: a torrent is added server-side, the local IP never joins the swarm, and the file arrives over SFTP. At 1 TB for $14.99 it is the cheapest storage-per-dollar seedbox in tested services and it composes with a debrid that cannot seed.
- reliability: The site's own help pages state that paid tiers cap concurrent torrents and that over-quota additions are 'Removed automatically', so a full drive loses the newest torrent rather than refusing it.
- notes: The vendor page is a Seedr comparison written to win the search for 'Seedr alternative', and it names Seedr's own tier prices alongside its own, which makes it usable as a cross-check on both. The 10 TB tier at $59.99 is $5.85 per TB, the cheapest per TB in tested services.
- evidence note: Prices and the free tier are read from the vendor's own comparison page, which states 'Prices checked 15 September 2026'. A mounted SFTP pull would raise egress and interface to measured.
- extras:
  - plans: Free 4 GB; Nano 50 GB $1.99; Vertex 100 GB $3.49; Quantix 250 GB $6.49; Krypher 500 GB $9.99; Voltrix 1 TB $14.99; Xyron 10 TB $59.99
  - prices_checked_on: 2026-09-15 (vendor's own statement)
  - promo_code: 10YEARSONICBIT
  - price_per_tb_at_10tb: USD 5.85
- evidence:
  - [2] 2026-10-23: the full tier table with prices: Nano 50 GB $1.99, Vertex 100 GB $3.49, Quantix 250 GB $6.49, Krypher 500 GB $9.99, Voltrix 1 TB $14.99, Xyron 10 TB $59.99, and 'There's a free 4 GB account'
  - [1] 2026-10-23: '4 GB FREE forever · No credit card required' and the apps layer (Plex, Jellyfin, Sonarr, n8n) on the drive
  - [3] 2026-10-23: the free tier's operational detail: '4 GB of Storage, Max. torrent download slot: 2, Remote Upload & Seeding Speed : 0.5 MB/s, Max. queued ... task: 1'
- sources:
  - [1] https://www.sonicbit.net/
  - [2] https://www.sonicbit.net/seedr-alternative
  - [3] https://dashold.sonicbit.net/
