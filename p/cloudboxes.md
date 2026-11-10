# Cloudboxes.io

> cloudboxes.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudboxes/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudboxes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloudboxes.io

- `debrid/cloudboxes-io-gpu-small` | paid-only | evidence documented | binding volume-quota | category shared seedbox and app hosting (GPU transcoding) | tier GPU Small
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:25:52.641Z (live) | stale on 2026-12-04
- url https://cloudboxes.io/
- free tier: No free tier; a 24-hour trial costs EUR 0.30 with the promotion code IWANTATRIAL, and the cheapest plan shown on the page is Small (Premium Shared) from EUR 14.95 per month; the cheapest GPU plan, GPU Small, is from EUR 19.95 per month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A 7 day refund policy is listed.
- per-object cap: not applicable: sold by total disk (2 TiB on GPU Small); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: GPU Small lists '4TB Bandwidth then 100mbit' on 2x10Gbit; the feature list says 'Unlimited Bandwidth'. | metered: yes | free allowance: 4 TB a month, then 100 Mbit | source: [1]
- identity: email | detail: Account plus payment through the vendor's order page. Sign-up fields, payment methods, phone and document requirements were not read: unverified. | country: None
- interface: sftp, ftps, ssh
- limits:
  - volume-quota (binding): 4TB bandwidth a month on GPU Small, then 100 Mbit [1]
- limits note: GPU Medium EUR 34.95 gives 4 TiB with 12 TB bandwidth; Dedicated IP is an optional EUR 5 a month.
- binding note: At 1 TiB per month nothing fails on the 4 TB allowance; past it the link drops to 100 Mbit.
- interface detail: The app list includes SFTP, FTP Secure (Proftpd), File Browser and a Shell Access (SSH) app; root access is listed on the GPU plans.
- tooling: SFTP or FTPS client, rclone and a one-click catalogue of 89 apps (rTorrent, Deluge, Transmission, Jellyfin, Plex); no vendor API or CLI is documented
- composes with: A EUR 19.95 2 TiB box with a 4 TB monthly allowance at 2x10 Gbit; rclone and pyLoad are in the app catalogue
- reliability: The page says 'Unlimited Bandwidth' while each plan lists a monthly bandwidth figure before a 100 Mbit limit.
- notes: The home page also lists NVMe Hybrid boxes from EUR 29.95 per month.
- evidence note: Plans, prices and bandwidth figures are on the vendor home page read on 2026-11-03 through a raw fetch converted to text. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: 2x10
  - minimum_term: monthly
  - trial_card_required: unverified: the trial is a EUR 0.30 paid order
- evidence:
  - [1] 2026-11-03: GPU Small holds 2 TiB of disk | capture: sha256:8833c2707334719772bcc8e8493bdbe1ad03a38206ee8bd6237b2350690bff96 | quote: 2TiB Raid 0 SAS Disk Space
  - [1] 2026-11-03: GPU Small carries a 4 TB bandwidth allowance, then 100 Mbit | capture: sha256:8833c2707334719772bcc8e8493bdbe1ad03a38206ee8bd6237b2350690bff96 | quote: 4TB Bandwidth then 100mbit
  - [1] 2026-11-03: a 24 hour trial costs EUR 0.30 | capture: sha256:8833c2707334719772bcc8e8493bdbe1ad03a38206ee8bd6237b2350690bff96 | quote: use "IWANTATRIAL" promotion code to get a 24 hours trial for 0.30€
  - [1] 2026-11-03: a 7 day refund policy applies | capture: sha256:8833c2707334719772bcc8e8493bdbe1ad03a38206ee8bd6237b2350690bff96 | quote: 7 Day Refund policy
  - [1] 2026-11-03: the Premium Shared plan Small is priced at EUR 14.95 per month, below GPU Small at EUR 19.95 | capture: sha256:6cfb09898f7d5a682633a8c00db7818d1c00198c4196e963e1dfc270f34aa32e | quote: <div class="plan-price">14.95€<small>/mo</small></div>
  - [1] 2026-11-03: GPU Small, the cheapest GPU plan, is EUR 19.95 per month | capture: sha256:6cfb09898f7d5a682633a8c00db7818d1c00198c4196e963e1dfc270f34aa32e | quote: <div class="plan-price">19.95€<small>/mo</small></div>
  - [1] 2026-11-03: a 24 hour trial costs EUR 0.30 with the code IWANTATRIAL under the GPU boxes | capture: sha256:6cfb09898f7d5a682633a8c00db7818d1c00198c4196e963e1dfc270f34aa32e | quote: *Use IWANTATRIAL to get a 24 hour trial for a tiny fee of 0.30€
  - [1] 2026-11-03: the trial offer and prices are as stated | capture: sha256:6cfb09898f7d5a682633a8c00db7818d1c00198c4196e963e1dfc270f34aa32e | quote: *Use IWANTATRIAL to get a 24 hour trial for a tiny fee of 0.30€
- sources:
  - [1] https://cloudboxes.io/
