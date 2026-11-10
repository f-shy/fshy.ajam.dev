# SonicSeedBox

> sonicseedbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sonicseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/sonicseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SonicSeedBox

- `debrid/sonicseedbox` | qualifies-with-caveat | evidence documented | binding per-object-cap | category shared seedbox with a permanent free tier | tier Sonicers Free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://sonicseedbox.com/
- price USD 0 for 4 GB; paid Basic USD 5.95 for 100 GB = USD 59.50/TB/month | parsed USD 59.5/TB-mo
- free tier: 'Need free seedbox? Try out our free limited feature seedbox.' Plan card: 'Sonicers Free 4 GB - FREE - Once you be a Sonicers, you will be credited 4 GB Storage. You can always upgrade anytime.' | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: the only permanent free seedbox tier found among debrid providers; 4 GB, not a trial
- per-object cap: not applicable; the free tier is capped at 4 GB total, which is smaller than most single video files | source: [1]
- retention: while the account exists; 'limited feature' is not defined further and no inactivity deletion is stated | source: [1]
- egress: 'Unlimited traffic, 10 GBPS Network, for as low as 2.15 Dollar'; torrents are converted to direct HTTP links ('Download converted torrent file by HTTP direct download link provides for you'). No byte allowance is published for any tier. | metered: no | free allowance: unlimited claimed, on a 4 GB free tier | source: [1]
- identity: email | detail: A dashboard account ('Once you be a Sonicers') is required; no phone or document check is stated for the free tier. | country: None
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB total storage on the free tier; a single file larger than the tier cannot be held [1]
- limits note: The 4 GB storage is the binding fact and the vocabulary has no kind for total disk; it is filed as per-object-cap because on this tier object and total coincide.
- binding note: 4 GB holds nothing of value at 1 TiB/month; the free tier is a pipeline test, not capacity.
- interface detail: Retrieval is over generated HTTP direct-download links from the dashboard; remote upload pushes to Google Drive, OneDrive, DropBox and pCloud. No SFTP or FTP is named on the page.
- tooling: Browser dashboard and HTTP direct links; remote upload to Google Drive/OneDrive/DropBox/pCloud; no CLI or API documented
- composes with: A free 4 GB landing pad that turns a magnet into an HTTP link; too small to hold 1 TiB of monthly transfer, but it proves the pipeline before any payment
- reliability: The free tier is 'limited feature' without a definition, so what is disabled is discovered at signup; nothing is charged, so nothing is refunded either.
- notes: This is the only permanent free seedbox in the sector, and 4 GB is two orders of magnitude below a usable working set: 1 TiB of monthly transfer would be 256 cycles. Sustained-rate conversion: unlimited claimed on '10 GBPS Network', but the 4 GB tier cannot hold 1 TiB of monthly transfer regardless of port. Potential constraints: the 4 GB cap, an unstated free-tier traffic cap, or a paywall on HTTP links; only the cap is stated.
- evidence note: The free tier and its 4 GB are stated on the vendor's own home page read. A measured rung needs an account and a real transfer.
- extras:
  - sustained_mbps_from_allowance: unlimited claimed; 10 Gbps network
  - port_gbps: 10
  - setup_fee: none
  - minimum_term: free tier permanent; paid tiers monthly
  - apps: browser dashboard, torrent-to-HTTP conversion, remote upload to Google Drive/OneDrive/DropBox/pCloud
  - trial_card_required: no card for the free tier
  - trial_restock: free tier is standing, not restocked
- evidence:
  - [1] 2026-10-23: 'Sonicers Free 4 GB FREE'; 'Unlimited traffic, 10 GBPS Network, for as low as 2.15 Dollar'; 'Download converted torrent file by HTTP direct download link'; paid tiers USD 3.95/50 GB, 5.95/100 GB, 10.95/350 GB
- sources:
  - [1] https://sonicseedbox.com/
