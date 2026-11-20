# TopSeedBox

> topseedbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/topseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/topseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TopSeedBox

- `debrid/topseedbox-1tb` | trial-only | evidence documented | binding none | category shared seedbox (private-tracker style, rTorrent) | tier 1 TB
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-12-04
- url https://www.topseedbox.com/
- free tier: A free seedbox trial account for 1 to 3 days is offered, but the request form answers 'Out of stock' today; the entry paid plan is 1 TB at EUR 10.95 per month. | unit: mixed | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: The true unit is days (a 1 to 3 day trial); the vocabulary has no days term. The trial request form asks for an email address, a username and a password, and refuses VPN, proxy and Tor requests.
- per-object cap: not applicable: sold by total disk (930 GB on the 1 TB plan); no single-file cap is published | source: [2]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [2]
- egress: 'Unmetered' up/down traffic on a 1Gbps interface; the FAQ says 'No, we do not limit upload and download traffic.' | metered: no | free allowance: unmetered in both directions | source: [2]
- identity: email | detail: The trial form asks for an email address, a username and a password. Payment is by PayPal or Bitcoin. Phone and document requirements are not stated on the pages read. | country: None
- interface: ftp
- limits:
  - per-ip-shaping: 1 Gbps interface, unmetered traffic; public trackers not allowed [2]
- limits note: Plans run 1 TB EUR 10.95 to 8 TB EUR 44.95 a month with 930 GB to 7,440 GB of disk. Public trackers are not allowed.
- binding note: No quota or object cap is published; the trial is out of stock and the paid disk is the planning number.
- interface detail: Torrent, FTP and HTTP file manager on every plan; ruTorrent web client.
- tooling: FTP client, HTTP file manager and ruTorrent; no API or CLI is documented
- composes with: A EUR 10.95 1 TB unmetered seedbox with an FTP pull path; public trackers are not allowed
- reliability: The free trial request form shows 'Out of stock', so the trial is not obtainable today; the unmetered claim carries no fair-use numbers.
- notes: A 7-day money-back guarantee is stated on the FAQ page.
- evidence note: Plans, prices, trial and payment are on the vendor pages read on 2026-11-03. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: 1
  - minimum_term: monthly
  - trial_card_required: no card field on the trial form; trial out of stock
  - trial_restock: out of stock on 2026-11-03
- evidence:
  - [2] 2026-11-03: monthly prices run from EUR 10.95 (1 TB) to EUR 44.95 (8 TB) | capture: sha256:e22f6a2285991dace48a3d4bdcd16f4889d00251660b9ed0a7d5e0f2c611629e | quote: | Monthly | €10. 95 /month | €15. 95 /month | €19. 85 /month | €25. 50 /month | €29. 95 /month | €34. 50 /month | €39. 85 /month | €44. 95 /month |
  - [2] 2026-11-03: the 1 TB plan holds 930 GB of disk | capture: sha256:e22f6a2285991dace48a3d4bdcd16f4889d00251660b9ed0a7d5e0f2c611629e | quote: | Disk Space | 930 GB | 1,860 GB | 2,790 GB | 3,720 GB | 4,650 GB | 5,580 GB | 6,510 GB | 7,440 GB |
  - [2] 2026-11-03: traffic is unmetered on every plan | capture: sha256:e22f6a2285991dace48a3d4bdcd16f4889d00251660b9ed0a7d5e0f2c611629e | quote: | Up/Down Traffic | Unmetered | Unmetered | Unmetered | Unmetered | Unmetered | Unmetered | Unmetered | Unmetered |
  - [1] 2026-11-03: a 1 to 3 day free trial account is offered | capture: sha256:a22da757b92c85b1727c7db361aa32d85a6b6cb79f18ca98bdcdc7e565a748ff | quote: Yes, we do offer free seedbox trial account for 1 - 3 days.
  - [1] 2026-11-03: payment is by PayPal or Bitcoin | capture: sha256:a22da757b92c85b1727c7db361aa32d85a6b6cb79f18ca98bdcdc7e565a748ff | quote: We accept Paypal and BitCoin.
  - [1] 2026-11-03: public trackers are not allowed | capture: sha256:a22da757b92c85b1727c7db361aa32d85a6b6cb79f18ca98bdcdc7e565a748ff | quote: No, We don't allow public tracker.
  - [3] 2026-11-03: the trial request form shows out of stock | capture: sha256:d21b768e28f1c5466633f3d9010041dc01fb0ac9b86d4b1a32414346c9de798e | quote: Out of stock
  - [3] 2026-11-03: the trial form asks for an email address, username and password | capture: sha256:d21b768e28f1c5466633f3d9010041dc01fb0ac9b86d4b1a32414346c9de798e | quote: Email address Username Password Confirm Password Submit trial request
- sources:
  - [1] https://www.topseedbox.com/faq
  - [2] https://www.topseedbox.com/pricing
  - [3] https://www.topseedbox.com/trial_request
