# Databay

> databay.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/databay/ | JSON https://fshy.ajam.dev/api/v1/entity/databay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Databay

- `debrid/databay` | qualifies-with-caveat | evidence documented | binding volume-quota | category residential egress: rotating residential, prepaid GB packages | tier Residential, prepaid package
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:47:01.820Z (live) | stale on 2026-12-26
- url https://databay.com/proxies/residential/pricing
- price USD 0.72/GB at the 1 TB package, i.e. USD 737.28 per TiB
- free tier: No free allowance published; 'Entry allowance 5 GB, Entry rate $2.75/GB, Payable total USD $13.75, Traffic validity 186 days'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The 186-day validity is why this is the one metered product that could be bought in small amounts without losing the purchase at month end.
- per-object cap: not applicable: a byte stream, not an object | source: [1]
- retention: not applicable to the traffic; the purchased GB is valid for 186 days (5 GB package) or 31 days (packages from 10 GB) | source: [1]
- egress: Prepaid packages, each a fixed allowance at a fixed rate: '5 GB+ $13.75 $2.75/GB ... 10 GB $22.50 $2.25/GB ... 50 GB $87.50 $1.75/GB ... 150 GB $210.00 $1.40/GB ... 500 GB $475.00'. The product is 'a shared rotating pool, not a static ISP allocation'. | metered: yes | free allowance: none | price per TB: USD 0.72/GB at the 1 TB package (USD 737.28, valid 31 days); 5 TB is USD 0.65/GB (USD 3,328) | source: [1]
- identity: card | detail: Self-service checkout at app.databay.com with card; no identity document mentioned on the page read.
- interface: rest
- limits:
  - volume-quota (binding): prepaid GB package; the largest read is 5 TB at USD 0.65/GB (USD 3,328), with 1 TB at USD 737.28 [1]
  - request-rate: 'Connection-based rotation; a fresh IP is not guaranteed' and sticky sessions up to 120 minutes [1]
- limits note: Rotation per connection is the wrong shape for a long download: a single HTTP transfer holds one connection, so a rotation policy that only changes on a new connection leaves the transfer on one address, which is what a debrid IP check wants.
- binding note: USD 0.72/GB is the cheapest large-package rate among debrid providers except Rayobyte's disputed headline, and the 1 TB package is still USD 737.28 for 31 days.
- interface detail: HTTP(S) and SOCKS5 rotating pool, country or continent selector, sticky sessions up to 120 minutes on the datacenter product; the residential page states connection-based rotation.
- endpoint: https://app.databay.com/
- tooling: any HTTP/SOCKS5 client
- composes with: Prepaid and valid for 186 days at the entry tier, so it is the metered product a corpus can test once without a monthly commitment; at TiB scale the 1 TB package is USD 737.28 at USD 0.72/GB.
- reliability: 'A fresh IP is not guaranteed for every connection' and sticky sessions 'may end before that requested window' - a mid-transfer address change is the failure mode, and it is the one debrid terms punish as account sharing.
- notes: Entered the sector as a low-rate outlier and stayed because of the 186-day validity, which makes it the only metered vendor here a small test purchase does not waste.
- evidence note: The package table is on the vendor page read. The 1 TB rung is quoted directly at USD 737.28, so the per-TiB figure is the published rate, not a derivation from the 500 GB package.
- extras:
  - ladder: 2.75 / 2.25 / 1.75 / 1.40 / 0.95 USD per GB at 5 / 10 / 50 / 150 / 500 GB
  - validity: 186 days at 5 GB, 31 days from 10 GB
  - rotation: connection-based; sticky up to 120 minutes
- evidence:
  - [1] 2026-10-23: the package ladder with rates and totals: 5 GB $2.75/GB ($13.75), 10 GB $2.25/GB ($22.50), 50 GB $1.75/GB ($87.50), 150 GB $1.40/GB ($210), 500 GB $475; and 'Entry starts at 5 GB' with 186-day validity
  - [1] 2026-11-25: the entry package is still 5 GB for USD 13.75, valid 186 days | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: $13.75for 5 GB of trafficValid 186 days · $2.75/GB
  - [1] 2026-11-25: the 1 TB package is now published at USD 737.28 and USD 0.72/GB | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: 1 TB$737.28. Per GB: $0.72, 73% below the per-GB rate. Valid for: 31 days.
  - [1] 2026-11-25: the 1 TB package is now priced directly, so no derivation is needed | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: 1 TB$737.28. Per GB: $0.72, 73% below the per-GB rate. Valid for: 31 days.
  - [1] 2026-11-25: the rotation policy is unchanged | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: Connection-based rotation; a fresh IP is not guaranteed
  - [1] 2026-11-25: validity is 186 days by the GB and 31 days on packages | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: 186 days for bandwidth bought by the GB; 31 days on packages.
  - [1] 2026-11-25: the trial asks for a card | capture: sha256:2b0c03a6e144ed0427c6e4cd0cf1a405e9defeecb3a695734029d40f80dd4335 | quote: We ask for a card, but you pay nothing during the trial.
- sources:
  - [1] https://databay.com/proxies/residential/pricing
