# Ultra.cc

> ultra.cc | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ultra/ | JSON https://fshy.ajam.dev/api/v1/entity/ultra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ultra.cc — Platinum 28 TB

- `storage/ultra-cc-platinum-28-tb` | qualifies-with-caveat | evidence reported | binding none | category seedbox
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ultra.cc/
- price 28TB: €79.95 -> €2.86/TB/mo (~$3.28). 12TB: €38.95 -> €3.25/TB. 4TB: €13.95 -> €3.49/TB. 1TB: €6.50 -> €6.50/TB | parsed USD 3.22/TB-mo
- free tier: 1 / 2 / 4 / 6 / 8 / 12 / 16 / 22 / 28 TB HDD | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "Unmetered Download" + "50Gbps Shared Upload", but a monthly upload allowance per plan: 2 TB (1TB plan) to 70 TB (28TB plan). Ratio ~2.5x. | metered: yes
- identity: email | detail: email
- interface: sftp, rsync, ssh, rclone
- limits note: Monthly upload allowance; Plex gated below Tin (4 TB)
- interface detail: SSH, SFTP, app installer, Plex/Jellyfin/Emby (from 4 TB up), 50 Gbps shared
- tooling: rclone/rsync
- composes with: Plex included from the 4 TB tier makes it the best media-serving option here
- reliability: NL/CA/SG. Prices seen on the live page are higher than the 2026-08 comparison article's figures (Nickel €38.95 vs €31.95 cited). Treat aggregator prices as stale.
- notes: the same as the free tier
- extras:
  - price_verbatim: 28TB: €79.95 -> €2.86/TB/mo (~$3.28). 12TB: €38.95 -> €3.25/TB. 4TB: €13.95 -> €3.49/TB. 1TB: €6.50 -> €6.50/TB
- evidence:
  - [1] 2026-10-21: live ladder: Lancer 1TB €6.50, Spirit 2TB €10.95, Tin 4TB €13.95, Iron 6TB €20.95, Steel 8TB €26.95, Nickel 12TB €38.95, Bronze 16TB €49.95, Gold 22TB €65.95, Platinum 28TB €79.95
- sources:
  - [1] https://ultra.cc/
