# IndoLeech

> indoleech.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/indoleech/ | JSON https://fshy.ajam.dev/api/v1/entity/indoleech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IndoLeech

- `debrid/indoleech-com` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud torrent leech (Indonesian: magnet/torrent to direct download with a disk slot) | tier torrent-10g
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://indoleech.com/
- price EUR 17.50 per month for a 1 TB slot (IDR 440,000 through the reseller); IDR 30,000 for the 10 GB slot | parsed USD 19.59/TB-mo
- free tier: A free slot is published: 'Free - 1.0 GB Space, 1 Torrent Run, Unlimited DL, Support RAR, Zip'. Paid tiers are Rp 30,000 (10 GB, 3 runs), Rp 40,000 (20 GB, 5 runs), Rp 50,000 (50 GB, 10 runs), Rp 70,000 (100 GB) per month. The same page serves a euro ladder through ?cur=EUR: EUR 1.75 / 2.33 / 2.92 / 4.08 / 5.83 / 11.67 / 17.50 per month for 10 GB through 1 TB. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: The quota is disk space allocated to the leech, not downloaded bytes; downloads are advertised as unlimited. Two currency ladders exist on the same site.
- per-object cap: not stated as a file cap; the tier's disk space bounds any single torrent | source: [2]
- retention: not stated; files live in the allocated disk slot until deleted | source: [2]
- egress: 'Unlimited DL' on every tier including free; speed is 1 Mbit/s on free and 1 Gbit/s on paid per the reseller's table. | metered: no | free allowance: 1 GB slot, 1 torrent run, 1 Mbit/s | source: [2]
- identity: email | detail: Signup is an account on the site ('Buy Now' leads to /register). A euro price ladder is served at ?cur=EUR, so the checkout is built for buyers outside Indonesia as well; the method is still not published on the pricing page, and the documented Indonesian purchase channel (ViooMax) takes local bank transfer. | country: Indonesia
- interface: rest
- limits:
  - volume-quota (binding): 10 GB disk on the Rp 30,000 tier; 1 GB on free [2]
  - request-rate: 3 active torrent runs on the 10 GB tier; 1 on free [2]
- limits note: The reseller's fuller ladder runs to a 1024 GB slot at Rp 440,000/30 days with 30 active torrents.
- binding note: Disk space per tier is what a monthly transfer of 1 TiB hits first: 10 GB in, download out, delete, repeat. The 3-run concurrency caps the pace, not the total.
- interface detail: Web panel; accepts 'url torrent, file.torrent or magnet link'. The vendor documents IDM and JDownloader use for the resulting files.
- tooling: Browser plus IDM/JDownloader; the reseller publishes a tutorial for IDM. No API documented.
- composes with: A cheap torrent-to-HTTP step in front of any download manager: 10 GB of working space is enough to cycle 1 TiB of monthly transfer through it in chunks, provided the 3 concurrent runs are enough.
- reliability: Free tier is 1 Mbit/s with one run, which is a demonstration rather than a service; paid performance is vendor-stated and unmeasured, and the reseller warns prices move with the exchange rate.
- notes: Indonesia's retrieval market is torrent leech, not multi-host debrid: the stores sell disk slots and concurrent runs. The euro ladder is the strongest signal among debrid providers that an Indonesian service is built to be bought from outside, even though the payment method is still unstated. Trigger condition: the site stops accepting registrations or the price ladder moves beyond IDR 500,000 for 1 TB.
- evidence note: The pricing table was read. The payment rail is inferred from the reseller page rather than read on indoleech.com itself, which is why identity is recorded as email with the rail noted separately.
- extras:
  - free_speed: 1 Mbit/s (per reseller)
  - paid_speed: 1 Gbit/s (per reseller)
  - reseller: vioomax.com
  - eur_ladder: 1.75 / 2.33 / 2.92 / 4.08 / 5.83 / 11.67 / 17.50 per month
  - idr_ladder: 30.000 / 40.000 / 50.000 / 70.000 per month
- evidence:
  - [2] 2026-10-23: tier table: 'Free 1.0 GB Space 1 Torrent Run Unlimited DL'; 'Torrent 10G Rp.30,000 Per Month 10.0 GB Space 3 Torrent Run'; 'Torrent 20G Rp.40,000'; 'Torrent 50G Rp.50,000'; 'Torrent 100G Rp.70,000'
  - [2] 2026-10-23: 'Support url torrent, file.torrent or magnet link' and 'Your Private Cloud Torrent Leech'
  - [3] 2026-10-23: reseller ladder with speed: 'Free 150 MB 1 Mbit/s' up to 'Torrent 1000G 1024 GB 30 Active 1 Gbit/s 440.000' per 30 days
  - [1] 2026-10-23: euro ladder on the same product table: 'Torrent 10G €1.75 Per Month', 'Torrent 1TB €17.50 Per Month 1.0 TB Space 50 Torrent Run'
- sources:
  - [1] https://www.indoleech.com/?cur=EUR
  - [2] https://indoleech.com/
  - [3] https://vioomax.com/indoleech.htm
