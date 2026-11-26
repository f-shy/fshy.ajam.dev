# Seedboxes.cc

> seedboxes.cc | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedboxes/ | JSON https://fshy.ajam.dev/api/v1/entity/seedboxes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedboxes.cc

- `debrid/seedboxes-cc` | paid-only | evidence documented | binding volume-quota | category shared seedbox (app hosting with torrent clients) | tier Bat Box
- needs card yes, phone yes, ID no, institution no | verified 2026-11-25T09:47:03.625Z (live) | stale on 2026-12-26
- url https://www.seedboxes.cc/
- price EUR 14.35 for 2 TB = EUR 7.18/TB/month (USD ~7.8 at 1.09) | parsed USD 8.09/TB-mo
- free tier: No free tier and no free trial. The only no-cost way in is the refund window: 'All plans come with a - no questions asked - money back guarantee during the first week of your service!' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the first-week refund is a paid trial, not a trial that starts at zero
- per-object cap: not applicable: the plan is sold by total disk (2 TB on Bat Box), not by largest single object; no per-file cap is published | source: [1]
- retention: until the subscription ends; no inactivity deletion is stated | source: [1] | note: not applicable in the debrid sense: the box holds what is put on it while it is paid
- egress: Bat Box includes 10 TB of upload traffic per month on a 50Gbit/50Gbit server uplink; 'After using your monthly traffic quota, upload speed is limited to 10 Mbit/s for the remainder of the month. Download speed remains unlimited.' No overage price is published. | metered: yes | free allowance: 10 TB/month upload (Bat Box); 15 TB Gremlin, 20 TB Vampire, 30 TB Zombie, 40 TB Red Dragon | source: [1]
- identity: email | detail: An account is required and there is no free tier, so a payment method is needed to use the service at all. No identity document or phone verification is stated on the page read. | country: None
- interface: ftp, sftp, ssh
- limits:
  - volume-quota (binding): 10 TB upload per month on the entry Bat Box plan [1]
  - per-ip-shaping: upload limited to 10 Mbit/s after the monthly quota, until reset [1]
- limits note: Entry plan is EUR 14.35/month on the plan page; the order step shows EUR 15.95 for a 1-month Bat Box. The 10 TB monthly upload allowance sets the sustained rate.
- binding note: The 10 TB/month upload counter is reached long before the 50 Gbit port is saturated: 10 TB/month is 30.9 Mbit/s sustained, one 1,600th of the port.
- interface detail: FTP and SFTP are documented in the vendor's own docs and community guides (FileZilla connection guides, multi-part FTP downloading); the Seedbucket web file manager is included on every plan.
- tooling: FileZilla, aria2/lftp per vendor guides; Seedbucket file manager and downloader; no rclone backend is documented
- composes with: A 10 TB/month box feeding a home NAS or a cloud mount; the monthly upload counter, not the 50 Gbit port, decides how much can actually be pulled before 10 Mbit/s shaping
- reliability: After the monthly upload quota the account is shaped to 10 Mbit/s rather than billed; download stays unlimited.
- notes: 10 TB -> 3.86 MB/s -> 30.9 Mbit/s. The page supports the first two as positioning, not as a measured cost.
- evidence note: Pricing, quota and throttle are on the live plan page read on 2026-10-23. A measured rung would need an account and a transfer run, which on 2026-10-23 did not buy.
- extras:
  - sustained_mbps_from_allowance: 30.9
  - port_gbps: 50
  - setup_fee: none stated
  - minimum_term: monthly; one-week refund window
  - apps: 40+ one-click apps including Plex, Emby, Jellyfin; Seedbucket; WireGuard VPN
  - trial_card_required: no trial exists
  - trial_restock: not applicable
- evidence:
  - [1] 2026-10-23: Bat Box EUR 14.35/mo with 2 TB storage and 10 TB upload traffic on a 50Gbit/50Gbit uplink; 'upload speed is limited to 10 Mbit/s for the remainder of the month'; one-week money-back, no free tier
  - [2] 2026-10-23: FTP and SFTP are supported access paths; the docs index lists 'Optimize FTP downloads from your seedbox with multi-part (multi-segmented) downloading'
  - [1] 2026-11-25: Bat Box upload quota is 10 TB/month and upload is shaped to 10 Mbit/s past it; download stays unlimited | capture: sha256:3a6fe708d8de692d8264e287bb6f810356016aab0731e43d7ba43750b7130ee4 | quote: After using your monthly traffic quota, upload speed is limited to 10 Mbit/s for the remainder of the month. Download speed remains unlimited.
  - [1] 2026-11-25: the only no-cost entry is a first-week refund window; no free tier or free trial is stated | capture: sha256:3a6fe708d8de692d8264e287bb6f810356016aab0731e43d7ba43750b7130ee4 | quote: During the first week of your service, you can ask for a refund. That's how confident we are about our seedboxes.
  - [3] 2026-11-25: an account is required before an order can continue; no phone or document gate is published | capture: sha256:ae9d627d72ae85f188146736dc3c331e8ab45d4f3adfb37bfcf3b00209a533e9 | quote: To continue with your order, you need to log in or sign up first
  - [3] 2026-11-25: the 1-month Bat Box order step presents a EUR 15.95 total | capture: sha256:ae9d627d72ae85f188146736dc3c331e8ab45d4f3adfb37bfcf3b00209a533e9 | quote: Total: € 15.95
- sources:
  - [1] https://www.seedboxes.cc/
  - [2] https://docs.seedboxes.cc/
  - [3] https://www.seedboxes.cc/signup?plan=Bat%20Box
