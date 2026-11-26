# Whatbox

> whatbox.ca | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/whatbox/ | JSON https://fshy.ajam.dev/api/v1/entity/whatbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Whatbox — H3-22

- `storage/whatbox-h3-22` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:25.448Z (live) | stale on 2026-12-10
- url https://whatbox.ca/plans
- price SGD 3.78 per TB per month on the H3-22 (SGD 82 per month for 21.7 TB)
- free tier: 3.9 / 5.9 / 9.9 / 15.8 / 21.7 TB HDD | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: no per-object size cap stated on the plans page or in the FAQ
- retention: Slots and their files are deleted 7 days after expiration without payment. | source: [1] | note: Deletion happens 7 days after expiration without payment.
- egress: Download (ingress to slot) unlimited. Upload (egress from slot) metered 10 TB on H3-4 up to 40 TB on H3-22. FAQ verbatim: "We will limit your upload speed to 100 Megabits per second until your next billing cycle" on overage. | metered: yes
- identity: email | detail: email
- interface: sftp, ftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 100 Megabits per second [2]
- limits note: Upload byte cap; over-cap = 100 Mbps throttle, not a bill
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: SFTP/FTP, 40 Gbps shared, Plex
- tooling: rclone/rsync over SFTP
- composes with: Good archive target, poor fetch target: the capped direction is exactly the serving direction
- reliability: Operating since 2008 in Singapore, Netherlands, and United States locations. Marketing describes unmetered inbound downloads, while outbound upload traffic is metered.
- notes: the same as the free tier
- evidence note: the unlimited-download statement is quoted from the first-party FAQ
- extras:
  - price_verbatim: 21.7TB: $64 -> $2.95/TB/mo. 15.8TB: $50 -> $3.16/TB. 9.9TB: $36 -> $3.64/TB. 3.9TB: $15 -> $3.85/TB
- evidence:
  - [1] 2026-10-21: full ladder read: $15/3.90TB, $22/5.90TB, $36/9.90TB, $50/15.80TB, $64/21.70TB with 10/15/20/30/40 TB upload
  - [2] 2026-10-21: overage throttle to 100 Megabits + 'Downloading files to your slot's hard drive is completely unlimited'
  - [1] 2026-11-10: the H3-22 plan card lists SGD 82 per month, 21.70 TB of storage and 40 TB of upload | capture: sha256:def16285ab09a38d7627a083c9c5384a04c7a90a3892dd22124e841efe3207b0 | quote: 82 SGD monthly [1] 21.70 TB storage [2] 40 TB upload [3] #### Servers in: ~~Singapore~~ ~~Netherlands~~ ~~United States~~ [Buy now](https://whatbox.ca/plans/H3-22)
  - [2] 2026-11-10: a fresh read states the 100 Mbps upload throttle | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: We will limit your upload speed to 100 Megabits per second until your next billing cycle.
  - [2] 2026-11-10: the FAQ states unlimited download to the slot's hard drive | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: Yes! Downloading files to your slot's hard drive is completely unlimited.
  - [2] 2026-11-25: files are deleted 7 days after expiration without payment | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: Slots and their files are deleted 7 days after expiration without payment.
  - [2] 2026-11-25: the deletion clock is 7 days after unpaid expiration | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: Slots and their files are deleted 7 days after expiration without payment.
  - [1] 2026-11-25: the H3-22 card states a storage volume, not an object-size cap | capture: sha256:1fa307a493f2291ed2f993f881a3c52f0b2b17d9245a23961933d91082fb81b9 | quote: 21.70 TB storage [2]
  - [2] 2026-11-25: over-cap upload speed is limited to 100 Megabits per second | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: We will limit your upload speed to 100 Megabits per second until your next billing cycle.
  - [1] 2026-11-25: the H3-22 card states a storage volume with no object cap | capture: sha256:1fa307a493f2291ed2f993f881a3c52f0b2b17d9245a23961933d91082fb81b9 | quote: 21.70 TB storage [2]
  - [2] 2026-11-25: over-cap upload is shaped to 100 Megabits per second | capture: sha256:e9dbae4af4aa4ece795c7604626755d644836fdb60caa63b573faea8bf754f0c | quote: We will limit your upload speed to 100 Megabits per second until your next billing cycle.
- sources:
  - [1] https://whatbox.ca/plans
  - [2] https://whatbox.ca/faq
