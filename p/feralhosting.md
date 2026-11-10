# Feral Hosting

> feralhosting.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/feralhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/feralhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Feral Hosting — Radon (8 TB)

- `storage/feral-hosting-radon` | qualifies-with-caveat | evidence reported | binding none | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.feralhosting.com/pricing
- price 8TB: £60 -> £7.50/TB/mo (~$10.08). 4.5TB: £45 -> £10.00/TB. 1TB: £10 -> £10.00/TB | parsed USD 10.03/TB-mo
- free tier: 1 / 1.5 / 2 / 3 / 4.5 / 8 TB HDD; SSD line 150 GB-1.6 TB | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Verbatim FAQ: "We run our own ISP meaning upload quotas no longer makes sense for us. So we've removed them from all of our slots". Truly unmetered both directions, 20 Gbit/s, fair-use with weekend peak throttling. | metered: no
- identity: email | detail: email
- interface: sftp, ftp, rsync, ssh, rclone
- limits note: Storage quota; over-quota tolerated 'a little bit'; weekend peak shaping
- interface detail: SSH, SFTP/FTP, full shell, Plex via Docker
- tooling: rclone/rsync/borg over SSH
- composes with: The one famous seedbox with genuinely no upload cap. But the per-TB price is 4-5x the floor.
- reliability: Own ISP and hardware since ~2008. Reputation for not overselling is the reason to pay the premium.
- notes: the same as the free tier
- extras:
  - price_verbatim: 8TB: £60 -> £7.50/TB/mo (~$10.08). 4.5TB: £45 -> £10.00/TB. 1TB: £10 -> £10.00/TB
  - fx.pair: USD/GBP
  - fx.rate: 0.74804
  - fx.date: 2026-10-23
- evidence:
  - [1] 2026-10-21: plan table: Helium £10/1TB, Neon £15/1.5TB, Argon £20/2TB, Krypton £30/3TB, Xenon £45/4.5TB, Radon £60/8TB
  - [1] 2026-10-21: upload-quota FAQ removed entirely (verbatim above)
- sources:
  - [1] https://www.feralhosting.com/pricing
