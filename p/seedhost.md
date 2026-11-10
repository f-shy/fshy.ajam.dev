# SeedHost.eu

> seedhost.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedhost/ | JSON https://fshy.ajam.dev/api/v1/entity/seedhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SeedHost.eu — HD 24

- `storage/seedhost-eu-hd-24` | qualifies-with-caveat | evidence reported | binding none | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.seedhost.eu/shared-app-hosting/
- price 24TB: €55 -> €2.29/TB/mo (~$2.63). 18TB: €40.50 -> €2.25/TB. 12TB: €27 -> €2.25/TB. 4TB: €9 -> €2.25/TB. 1TB: €3 -> €3.00/TB | parsed USD 2.54/TB-mo
- free tier: 1 / 2 / 3 / 4 / 5 / 7 / 9 / 12 / 15 / 18 / 24 TB HDD | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered per plan, roughly 1x-2x storage: HD 1 1TB->1TB, HD 4 4TB->5TB, HD 12 12TB->22TB, HD 24 24TB->50TB. Store page notes "only outgoing traffic is counted to the limit (UL), incoming (DL) is not counted". Over-limit = throttled, no overage bill. | metered: yes
- identity: email | detail: email
- interface: sftp, ftp, rsync, ssh, rclone
- limits note: Egress byte cap ~2x storage; streaming apps gated below HD 7
- interface detail: SSH/SFTP/FTP, 40 Gbps HDD line, app installer, VNC
- tooling: rclone/rsync over SSH
- composes with: Mount and front; Plex/Emby unlock only from HD 7 up
- reliability: NL, long-running. Constant per-TB rate across the range means no volume discount to chase. The 24 TB tier is only marginally cheaper per TB than HD 4.
- notes: the same as the free tier
- extras:
  - price_verbatim: 24TB: €55 -> €2.29/TB/mo (~$2.63). 18TB: €40.50 -> €2.25/TB. 12TB: €27 -> €2.25/TB. 4TB: €9 -> €2.25/TB. 1TB: €3 -> €3.00/TB
- evidence:
  - [1] 2026-10-21: full ladder parsed from raw HTML: HD1 1TB/1TB/€3, HD2 2/2/€5, HD3 3/3/€7, HD4 4/5/€9, HD5 5/7/€11.25, HD7 7/11/€15.75, HD9 9/16/€20.25, HD12 12/22/€27, HD15 15/30/€33.75, HD18 18/36/€40.50, HD24 24/50/€55
  - [2] 2026-10-21: corroborates storage/traffic pairs and the UL-only counting rule
- sources:
  - [1] https://www.seedhost.eu/shared-app-hosting/
  - [2] https://www.seedhost.eu/client-area/store/shared-hosting
