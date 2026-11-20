# Seed.ST

> seed.st | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seed/ | JSON https://fshy.ajam.dev/api/v1/entity/seed.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seed.ST

- `debrid/seed-st-mini` | paid-only | evidence documented | binding none | category shared seedbox (weekly or monthly slots) | tier mini
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T15:25:55.920Z (live) | stale on 2026-12-04
- url https://seed.st/
- free tier: No free tier and no trial is published; the entry package is mini at USD 2.00 per week or USD 6.00 per month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A weekly price exists on every package.
- per-object cap: not applicable: sold by total disk (200 GB on mini); no single-file cap is published | source: [2]
- retention: for the paid period; no inactivity deletion is stated | source: [2]
- egress: 'Unlimited Bandwidth' and 'Unlimited Active Transfers', with an 8MB/s average upload speed on mini. | metered: no | free allowance: unlimited stated | source: [2]
- identity: card | detail: Order page asks for a username and a password (no email field), then payment through PayPal, the only active payment method; the PayPal account supplies the payer identity. No phone or ID document is asked. | country: None
- interface: ftp, ftps
- limits:
  - per-ip-shaping: 8MB/s average upload on mini; 15MB/s on 100mbit, 30MB/s on 1gbit, 80MB/s on 1gbit-ssd [1]
- limits note: Packages: mini 200 GB USD 6/month, 100mbit from 400 GB USD 10/month, 1gbit 1 TB USD 25/month, max 6 TB USD 50/month. Public trackers are not allowed on mini.
- binding note: No quota or object cap is published; the 200 GB disk and the 8MB/s average upload are the planning numbers.
- interface detail: 'FTP/FTPS/FXP Access' and web-based file access on every account.
- tooling: FTP or FTPS client, FXP between servers, and the web file manager; no API or CLI is documented
- composes with: A USD 2 per week 200 GB box, useful for a short burst of retrieval; mini does not allow public trackers
- reliability: 'Unlimited' bandwidth with no fair-use numbers published; the 8MB/s figure is an average, not a guarantee.
- notes: The home page lists mini $2/wk | $6/mo, 100mbit $3/wk | $10/mo, 1gbit $7/wk | $25/mo and max $15/wk | $50/mo.
- evidence note: Packages, prices and protocols are on the vendor pages read on 2026-11-03. A measured rung needs a slot and a timed transfer.
- extras:
  - minimum_term: one week
  - trial_card_required: no trial exists
- evidence:
  - [2] 2026-11-03: mini is 200 GB with 8MB/s average upload, unlimited bandwidth and FTP/FTPS/FXP | capture: sha256:fdfda292da71ee9b5d5f0e43e30724314762a172686d39d25fd3da11d9632836 | quote: 200GB Drive Space 8MB/s Average Upload Speed Instant Activation Public trackers NOT allowed Unlimited Bandwidth Unlimited Active Transfers FTP/FTPS/FXP Access
  - [2] 2026-11-03: mini is sold weekly at USD 2.00 | capture: sha256:fdfda292da71ee9b5d5f0e43e30724314762a172686d39d25fd3da11d9632836 | quote: $2.00 per week
  - [2] 2026-11-03: mini is sold monthly at USD 6.00 | capture: sha256:fdfda292da71ee9b5d5f0e43e30724314762a172686d39d25fd3da11d9632836 | quote: $6.00 per month
  - [1] 2026-11-03: the largest package is USD 50/month | capture: sha256:a7ccb8b8bd5598cd72136b4bfd803f5710284a19c34b6a4be367b23962ea007a | quote: max $15/wk | $50/mo
  - [2] 2026-11-03: PayPal is the only payment method offered on the order page; the credit card and bitcoin buttons are commented out | capture: sha256:f1ae3094e5946f2f3c9d3d89e7bd36bcb35721718e844b4f56320b359c54f58c | quote: Pay with PayPal
  - [2] 2026-11-03: the new-account dialog of the order page asks for a username, a password and a password confirmation, with no email field | capture: sha256:f1ae3094e5946f2f3c9d3d89e7bd36bcb35721718e844b4f56320b359c54f58c | quote: Enter desired username and password below.
- sources:
  - [1] https://seed.st/
  - [2] https://www.seed.st/seedbox?p=mini
