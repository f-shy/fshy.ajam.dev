# Ko-fi Shop

> ko-fi.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ko-fi/ | JSON https://fshy.ajam.dev/api/v1/entity/ko-fi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ko-fi Shop

- `storage/ko-fi-shop` | fails-quota | evidence reported | binding per-object-cap | category Creator tipping + digital shop
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ko-fi.com/shop
- free tier: Free: 25 GB total asset storage, 2 GB per shop item. Standard/Gold: 200 GB total, 5 GB per item. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per item | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No bandwidth quota published. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): 5 GB per item [1]
- limits note: per-account-cap (not per-object): 25 GB free / 200 GB paid. per-object 2 GB / 5 GB.
- interface detail: Web; no public upload API.
- tooling: Web only.
- composes with: 25 GB free total is a fixed bucket, so it does not scale by sharding accounts cheaply (each needs a separate email + PayPal/Stripe). 200 GB on a paid tier is real but small.
- reliability: Third-party summaries disagree wildly on the free per-file number (100 MB vs 2 GB vs 10 MB). The help-centre figure quoted here is the vendor's own.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 25 GB total asset storage, 2 GB per shop item. Standard/Gold: 200 GB total, 5 GB per item.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Free users get up to 25GB of Ko-fi Shop asset storage. Standard users (previously called Contributors) get up to 200GB'; 'Free users can upload up to 2GB of files per shop item. Standard users ... up to 5GB per shop item'
  - [3] 2026-10-21: 200, product types incl. 'access to files'
- sources:
  - [1] https://help.ko-fi.com/hc/en-us/articles/360009712917-Ko-fi-Shop-Sell-digital-physical-products
  - [2] https://help.ko-fi.com/hc/en-us/articles/360009712917
  - [3] https://ko-fi.com/shop
