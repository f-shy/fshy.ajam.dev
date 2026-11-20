# Seedit4.me

> seedit4.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedit4/ | JSON https://fshy.ajam.dev/api/v1/entity/seedit4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedit4.me

- `debrid/seedit4-me-sidekick-pro` | paid-only | evidence documented | binding volume-quota | category shared seedbox (managed, Netherlands) | tier Sidekick Pro
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-12-04
- url https://seedit4.me/
- free tier: No free tier and no trial is published on the plan page; the cheapest plan is Sidekick Pro at EUR 11.99 per month including VAT (Chaos, the cheapest 10 Gbit plan, is EUR 19.99 per month). | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A 7-day refund window is stated; conditions apply.
- per-object cap: not applicable: sold by total disk (1500 GB on Sidekick Pro); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: Sidekick Pro has a 2 Gbit incoming and 1 Gbit outgoing link with 5 TB of upload per month; past it 'your upload bandwidth gets throttled to 10Mbps' unless extra traffic is bought. The 'Unmetered' plans start at EUR 16.99 per month. | metered: yes | free allowance: 5 TB upload per month on Sidekick Pro; downloads are not capped | source: [1]
- identity: email | detail: The register page offers sign-up through a Google, Facebook, Twitter or GitHub account; the vendor states it keeps 'an absolute minimum of personal details'. Payment is by PayPal, card, Revolut or crypto. Phone and document requirements are not stated. | country: None
- interface: sftp, ftp, ftps
- limits:
  - volume-quota (binding): 5 TB upload per month on Sidekick Pro, then throttled to 10 Mbps [1]
  - per-ip-shaping: 2 Gbit incoming and 1 Gbit outgoing on the Premium 1Gbit plans; 10 Gbit on the Racer plans [1]
- limits note: Racer 10Gbit plans: Chaos 1500 GB EUR 19.99 with 8 TB upload, Super Villain 4000 GB EUR 39.99 with 20 TB upload. Premium plans: Sidekick Pro 1500 GB EUR 11.99, Hero Pro 2000 GB EUR 17.99. Unmetered plans: Sidekick NL 1500 GB EUR 16.99.
- binding note: At 1 TiB per month nothing fails on the 5 TB upload allowance; the 1500 GB disk and the throttle past 5 TB are the limits.
- interface detail: The vendor lists FTP, FTPS, SFTP and HTTP access with browser-based apps; root access is not included on Sidekick Pro.
- tooling: FTP, FTPS or SFTP client and the vendor dashboard with a one-click app list; no API or CLI is documented
- composes with: A EUR 11.99 1.5 TB seedbox with a 5 TB monthly upload allowance; the Unmetered plans (EUR 16.99 and up) forbid public trackers
- reliability: Upload is capped at 5 TB a month on the cheapest plan; a crypto payment page was marked temporarily unavailable in the vendor's news list.
- notes: The vendor home page lists 7-Day Guarantee as a refund within the first week of service.
- evidence note: Plans, prices and caps are on the vendor home page read on 2026-11-03 through a raw fetch converted to text. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: 1 outgoing on Sidekick Pro
  - minimum_term: monthly; 3, 6 and 12 month prices are listed
  - location: Netherlands
  - trial_card_required: no trial exists
- evidence:
  - [1] 2026-11-03: the cheapest plan is Sidekick Pro at EUR 11.99 per month including VAT | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: Sidekick Pro € 11.99/m VAT inc.
  - [1] 2026-11-03: the entry plans hold 1500 GB of HDD | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: 1500 GB HDD
  - [1] 2026-11-03: Sidekick Pro carries a 5 TB monthly upload allowance | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: 5 TB Upload/Month*
  - [1] 2026-11-03: upload is throttled to 10 Mbps past the allowance | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: your upload bandwidth gets throttled to 10Mbps.
  - [1] 2026-11-03: the cheapest 10 Gbit plan is Chaos at EUR 19.99 per month | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: Chaos € 19.99/m VAT inc.
  - [1] 2026-11-03: payment is by major platforms, cards and crypto | capture: sha256:7948f9fc58250281d88afc792190e15fafd65414af4c71c1b341e7888aea41c5 | quote: Major payment platforms, credit cards and crypto currencies are supported.
  - [2] 2026-11-03: the register page offers sign-up through third-party accounts | capture: sha256:e02dc1e005a4ebae8f39e473db77909f5a8cee14c65a8d0eb8f1cd83e0af4845 | quote: Register Or register via
- sources:
  - [1] https://seedit4.me/
  - [2] https://my.seedit4.me/register
