# YourSeedbox

> yourseedbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yourseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/yourseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YourSeedbox

- `debrid/yourseedbox` | qualifies | evidence documented | binding per-object-cap | category shared seedbox (small slots, Dutch market) | tier S100G (annual)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://www.yourseedbox.com/
- price EUR 15.96/year for 200 GB = EUR 79.80/TB/year = EUR 6.65/TB/month | parsed USD 7.44/TB-mo
- free tier: No free tier and no trial is published; the cheapest entry is S100G at EUR 15.96 per year, about EUR 1.33 per month. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: 200 GB per torrent on every plan ('Storage | 200GB / torrent'), which is the per-torrent working set rather than the box's total | bytes: 214748364800 | source: [1] | note: the table prints 200GB/torrent as a row for every tier, so the cap is per object, not per account
- retention: for the life of the subscription; 'We do not keep records or logs' is a logging claim, not a retention limit | source: [1]
- egress: 'Upload traffic: unmetered' and 'Download traffic: unmetered' on a 1Gbit+ network; 'you can download it through FTP(S), HTTP(S) on your house computer'. | metered: no | free allowance: unmetered in both directions | source: [1]
- identity: email | detail: Account plus payment (BitCoin, credit card, iDEAL, Sofort, Bancontact, bank transfer); no free tier. No phone or document check is stated. | country: None
- interface: ftp, ftps
- limits:
  - per-object-cap (binding): 200 GB per torrent [1]
  - per-ip-shaping: 1 Gbit+ shared; 2 active torrents on the entry plan (4/7/10/14 on larger plans) [1]
- limits note: The active-torrent count is the real brake on the entry plan: two at a time, each up to 200 GB, so 1 TiB of monthly transfer is roughly five sequential cycles. The vocabulary has no kind for a simultaneous-torrent cap.
- binding note: At 1 TiB/month the 200 GB-per-torrent working set and the 2-active-torrent count decide throughput; no byte quota exists to fail first.
- interface detail: 'you can download it through FTP(S), HTTP(S) on your house computer'; sharing direct download allowed over HTTPS.
- tooling: FTP/FTPS clients and a browser for HTTP(S); TorrentCLOUD web interface; no API or CLI is documented
- composes with: The cheapest live seedbox found among debrid providers at EUR 1.33/month for a 200 GB working set; unmetered, so 1 TiB of monthly transfer is a matter of cycling torrents, not of quota
- reliability: Two active torrents on the entry plan and 200 GB per torrent; the vendor states no logs, which is unverifiable.
- notes: The annual-only entry is the cheapest live offer debrid verified: EUR 1.33/month. Sustained-rate conversion: unmetered, so the comparable number is the 1 Gbit+ port, 125 MB/s theoretical; at 1 TiB/month the requirement is only 3.39 Mbit/s, so the port is irrelevant and the 2-torrent count is the real constraint. Potential constraints: annual prepayment, the 2-torrent cap, or a hidden fair-use rule; the first two are on the page, the third is not.
- evidence note: Price, caps, protocols and payment methods are on the live vendor page read. A measured rung needs a slot and a timed transfer.
- extras:
  - sustained_mbps_from_allowance: unmetered; 1 Gbit+ port
  - port_gbps: 1+
  - setup_fee: none stated
  - minimum_term: entry is annual (EUR 15.96/year); larger plans monthly with discounts for 3/6/12 months
  - apps: TorrentCLOUD web interface (Transmission backend), FTP(S)/HTTP(S) download; no Plex, *arr or VPN is stated on the page read
  - trial_card_required: no trial exists
  - trial_restock: not applicable
- evidence:
  - [1] 2026-10-23: S100G EUR 15.96/year; S300G EUR 4.30/m; S600G EUR 7.18/m; S900G EUR 10.05/m; S1200G EUR 12.93/m; '200GB / torrent'; 2/4/7/10/14 active torrents; unmetered upload and download; 1Gbit+; FTP(S)/HTTP(S)
- sources:
  - [1] https://www.yourseedbox.com/
