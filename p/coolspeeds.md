# CoolSpeeds

> coolspeeds.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coolspeeds/ | JSON https://fshy.ajam.dev/api/v1/entity/coolspeeds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoolSpeeds

- `debrid/coolspeeds-com` | qualifies-with-caveat | evidence documented | binding volume-quota | category remote file conveyor (posting workstation) with a resold premium-download pool | tier daily disk plan + premium traffic + converter hours
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:04:35.999Z (live) | stale on 2026-11-23
- url https://coolspeeds.com/en
- price USD 36.86 per TiB of premium-pool download, plus USD 34.80/month for the 100 GB disk plan
- free tier: No free tier. 'There is no free trial, but any plan can be paid for 10, 20 or 30 days.' The smallest published plan is 20 GB for 10 days at $5.20. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Three independent billing streams: disk plan, premium traffic, converter hours.
- per-object cap: not applicable: the service downloads into a disk plan, it does not publish a maximum object size | source: [2] | note: The disk plan is the ceiling: 20 GB to 2 TB, chosen per day.
- retention: For the length of the paid plan; the plan can be changed once a day. No post-expiry retention statement found on the pricing page. | source: [2] | note: unstated
- egress: 'Unlimited traffic' on every disk plan. Downloads that need a premium file-host account are bought separately: '$0.36 per 10 GB ... billed strictly by bytes actually downloaded.' | metered: yes | free allowance: unlimited disk-plan traffic; no included premium-pool allowance | price per TB: USD 0.36 per 10 GB of premium-pool download (USD 36.86 per TiB) | source: [1]
- identity: email | detail: An account in the cabinet is required to hold a plan and a traffic balance. The signup form itself was not read; email is the minimum such a cabinet implies and is not confirmed.
- interface: unknown
- limits:
  - per-ip-shaping: download up to 10 Gbit/s, seed up to 16 Mbit/s [1]
  - volume-quota (binding): premium-pool downloads are prepaid in 10 GB packs; no included allowance [1]
  - request-rate: converter billed per actual CPU minute with a user-chosen priority multiplier; higher multiplier costs more [1]
- limits note: The FAQ says premium traffic is only needed 'when a file host requires a premium account and you do not have one'; your own host accounts can be plugged in instead.
- binding note: At 1 TiB a month the disk plan is irrelevant (100 GB is $34.80/month) but the premium pool is $36.86 per TiB, prepaid in 10 GB steps, and every byte is billed. That purchase, not a rate limit, is what is met first. The old documentation page still states '$0.30 per GB'; the live pricing page says $0.36 per 10 GB, and this record keeps the live number.
- interface detail: Browser cockpit at coolspeeds.com/{en,ru}/cabinet.html; ruTorrent 3.x with 19 plugins for torrents; FTP for uploads; a Firefox extension (LeechGrab) routes browser downloads through the vendor's MITM proxy. No public API documented on the pages read.
- tooling: Web UI only as documented; purchase links are plain cabinet URLs (action=s40&days=30), so a plan can be bought by URL. Torrents are handled by the vendor's ruTorrent instance, not by a local client.
- composes with: It replaces a seedbox plus a VPS for the posting workflow: download from a host, repack, upload to 100+ hosts, emit a post. As a pure debrid it is the premium-traffic stream at $0.036/GB.
- reliability: Payment is crypto and WebMoney only, so a plan cannot be bought with a card; the operator has run since 2011 and bills per byte, but the premium pool is a shared resale pool and the documentation already warns that 'bezotkaznaya rabota ... dlya vsekh failoobmennikov ne garantiruetsya' (uninterrupted operation for all file hosts is not guaranteed).
- notes: The cheapest per-GB figure found among debrid providers. The caveat is payment: crypto or WebMoney only, so a user without either cannot buy it at all. Candidate explanations considered for the price gap between the docs page ($0.30/GB) and the live page ($0.36/10 GB): (1) the docs page is a 2021 capture never updated - supported by its image timestamps uploads/images/gallery/2021-02 and by the pricing page being the later artefact; (2) the two pages price different pools; no evidence. The record keeps the live pricing page.
- evidence note: Prices, plan sizes and the payment-method list are quoted from the live English and Russian pricing pages read. A test download through the premium pool would raise this to measured.
- evidence:
  - [1] 2026-10-23: plan sizes and prices (40 GB for 30 days $20.40; 100 GB for 30 days $34.80; 1025 GB for 30 days $36.00), 'Unlimited traffic', '$0.36 per 10 GB', 'seed up to 16 Mbit/s', and the payment list 'Bitcoin, Litecoin, USDT (7 networks ...), WebMoney'
  - [2] 2026-10-23: '19 тарифов по объёму диска и 2 фиксированных месячных. Трафик безлимитный. Тариф можно менять раз в сутки.' and the per-plan dollar prices in the Russian interface
  - [3] 2026-10-23: the premium traffic is bought from external link-unrestricting services, the price there is '0.30$ za GB' (an older figure than the live page), and 'bezotkaznaya rabota dannoy funktsii dlya vsekh failoobmennikov ne garantiruetsya'
  - [4] 2026-10-23: the service downloads either through the account's own premium host accounts or through 'premium traffic' bought from external link-unrestricting services
- sources:
  - [1] https://coolspeeds.com/en
  - [2] https://coolspeeds.com/ru/prices.html
  - [3] https://docs.coolspeeds.com/books/rabota-s-fayloobmennikami/page/skachivanie-faylov-ispolzuya-platnyy-premium-trafik
  - [4] https://docs.coolspeeds.com/books/rabota-s-fayloobmennikami/page/skachivanie-faylov-s-fayloobmennikov
