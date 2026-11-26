# Feral Hosting

> feralhosting.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/feralhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/feralhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Feral Hosting — Radon (8 TB)

- `storage/feral-hosting-radon` | qualifies-with-caveat | evidence reported | binding none | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:14.807Z (live) | stale on 2026-11-25
- url https://www.feralhosting.com/pricing
- price 8TB: £60 -> £7.50/TB/mo (~$10.08). 4.5TB: £45 -> £10.00/TB. 1TB: £10 -> £10.00/TB | parsed USD 10.03/TB-mo
- free tier: 1 / 1.5 / 2 / 3 / 4.5 / 8 TB HDD | unit: TB | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: upload quotas are removed from all slots; the network is uncongested 24 / 7 | metered: no
- identity: email | detail: email
- interface: sftp, ftp, rsync, ssh, rclone
- limits note: SSD line: 150, 200, 300, 600 and 800 SSD GB
- interface detail: SSH, SFTP/FTP, full shell, Plex via Docker
- tooling: rclone/rsync/borg over SSH
- composes with: The one famous seedbox with genuinely no upload cap. But the per-TB price is 4-5x the floor.
- reliability: Own ISP and hardware since ~2008. Reputation for not overselling is the reason to pay the premium.
- notes: the same as the free tier
- evidence note: the cited page was read on 2026-11-09
- extras:
  - price_verbatim: 8TB: £60 -> £7.50/TB/mo (~$10.08). 4.5TB: £45 -> £10.00/TB. 1TB: £10 -> £10.00/TB
  - fx.pair: USD/GBP
  - fx.rate: 0.74804
  - fx.date: 2026-10-23
- evidence:
  - [1] 2026-10-21: plan table: Helium £10/1TB, Neon £15/1.5TB, Argon £20/2TB, Krypton £30/3TB, Xenon £45/4.5TB, Radon £60/8TB
  - [1] 2026-10-21: upload-quota FAQ removed entirely (verbatim above)
  - [1] 2026-11-09: the HDD capacity line runs from 1 TB to 8 TB | capture: sha256:d9faca7941e629eb339a36eb4c6d3e09f5c9b834f26e01c7abfa3de6522e4ddc | quote: | Storage | 1 TB | 1.5 TB | 2 TB | 3 TB | 4.5 TB | 8 TB |
  - [1] 2026-11-09: the SSD capacity line runs from 150 GB to 800 GB | capture: sha256:d9faca7941e629eb339a36eb4c6d3e09f5c9b834f26e01c7abfa3de6522e4ddc | quote: | Storage | 150 SSD GB | 200 SSD GB | 300 SSD GB | 600 SSD GB | 800 SSD GB |
  - [1] 2026-11-09: upload quotas are removed from all slots | capture: sha256:d9faca7941e629eb339a36eb4c6d3e09f5c9b834f26e01c7abfa3de6522e4ddc | quote: We run our own ISP meaning upload quotas no longer makes sense for us. So we've removed them from all of our slots and promised to run an uncongested network 24 / 7.
- sources:
  - [1] https://www.feralhosting.com/pricing
