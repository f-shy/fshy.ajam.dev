# Whatbox

> whatbox.ca | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/whatbox/ | JSON https://fshy.ajam.dev/api/v1/entity/whatbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Whatbox — H3-22

- `storage/whatbox-h3-22` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://whatbox.ca/plans
- price 21.7TB: $64 -> $2.95/TB/mo. 15.8TB: $50 -> $3.16/TB. 9.9TB: $36 -> $3.64/TB. 3.9TB: $15 -> $3.85/TB | parsed USD 2.95/TB-mo
- free tier: 3.9 / 5.9 / 9.9 / 15.8 / 21.7 TB HDD | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Download (ingress to slot) unlimited. Upload (egress from slot) metered 10 TB on H3-4 up to 40 TB on H3-22. FAQ verbatim: "We will limit your upload speed to 100 Megabits per second until your next billing cycle" on overage. | metered: yes
- identity: email | detail: email
- interface: sftp, ftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 100 Mbps [1]
- limits note: Upload byte cap; over-cap = 100 Mbps throttle, not a bill
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: SFTP/FTP, 40 Gbps shared, Plex
- tooling: rclone/rsync over SFTP
- composes with: Good archive target, poor fetch target: the capped direction is exactly the serving direction
- reliability: Operating since 2008 in Singapore, Netherlands, and United States locations. Marketing describes unmetered inbound downloads, while outbound upload traffic is metered.
- notes: the same as the free tier
- extras:
  - price_verbatim: 21.7TB: $64 -> $2.95/TB/mo. 15.8TB: $50 -> $3.16/TB. 9.9TB: $36 -> $3.64/TB. 3.9TB: $15 -> $3.85/TB
- evidence:
  - [1] 2026-10-21: full ladder read: $15/3.90TB, $22/5.90TB, $36/9.90TB, $50/15.80TB, $64/21.70TB with 10/15/20/30/40 TB upload
  - [2] 2026-10-21: overage throttle to 100 Megabits + 'Downloading files to your slot's hard drive is completely unlimited'
- sources:
  - [1] https://whatbox.ca/plans
  - [2] https://whatbox.ca/faq
