# the.hosting

> the.hosting | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/the-hosting/ | JSON https://fshy.ajam.dev/api/v1/entity/the-hosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## THE.Hosting review-for-days scheme

- `compute/the-hosting-review-for-days-scheme` | paid-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://the.hosting/tr/gift-vps
- free tier: 'Mevcut VPS'yi en az 1 ay i in sipari edin veya uzat n' (order or extend an existing VPS for at least one month), then publish an honest review of THE.Hosting and follow its social accounts to receive 'ek 30, 14 veya 7 g n' (an extra 30, 14 or 7 days) depending on the plan tier. There is no free VPS: the free days are an extension of a paid order. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - write-gated (binding): The scheme is not a free tier at all: step one is to buy a month of VPS, so the 'free' days are a rebate worth at most one month and the first thing that fails is the requirement to pay before anything is granted. [1]
- limits note: The scheme is not a free tier at all: step one is to buy a month of VPS, so the 'free' days are a rebate worth at most one month and the first thing that fails is the requirement to pay before anything is granted.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None: it is a discount on a paid server, not a free resource.
- reliability: no reliability event recorded
- notes: Two adjacent shapes were checked and also fail: Cli>_ (cliopen.com) advertises a starter credit that requires completing billing details and a card verification through Apple, Google or Stripe, and Netlen runs a prize wheel that pays in domain and hosting vouchers against orders. Nothing in the Turkish lane gives an individual a free machine without first paying for one.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: none
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Mevcut VPS'yi en az 1 ay i in sipari edin veya uzat n' (order or extend a current VPS for at least a month) as step 1, and 'size mevcut sanal sunucunuza ek 30, 14 veya 7 g n verelim' (we give you an extra 30, 14 or 7 days on your current virtual server), quoted
  - [2] 2026-10-22: the same mechanism at another provider in the region: 'Bir VPS sipari edin veya mevcut hizmetinizi en az 1 ay uzat n' then review on three sites for 30, 14 or 7 extra days, quoted
- sources:
  - [1] https://the.hosting/tr/gift-vps
  - [2] https://profitserver.net/tr/server4feedback/

## the.hosting (ex-pq.hosting) storage vps

- `storage/the-hosting-storage-vps` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://the.hosting/en/vps-vds-storage
- free tier: None reachable: Flexible-capacity storage at '€0.04 per 1 GB' = €40/TB = $44.94/TB/mo. Ten to twenty times the floor. This is where the PQ Hosting lead actually lands. The €0.03/GB figure circulating in re. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Flexible-capacity storage at '€0.04 per 1 GB' = €40/TB = $44.94/TB/mo. Ten to twenty times the floor. This is where the PQ Hosting lead actually lands — the €0.03/GB figure circulating in…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Flexible-capacity storage at '€0.04 per 1 GB' = €40/TB = $44.94/TB/mo. Ten to twenty times the floor. This is where the PQ Hosting lead actually lands — the €0.03/GB figure circulating in…
  - [2] 2026-10-21: cited as the basis of the rejection: Flexible-capacity storage at '€0.04 per 1 GB' = €40/TB = $44.94/TB/mo. Ten to twenty times the floor. This is where the PQ Hosting lead actually lands — the €0.03/GB figure circulating in re
- sources:
  - [1] https://the.hosting/en/vps-vds-storage
  - [2] https://digiexe.com/blog/pq-hosting-review/

## the.hosting

- `compute/the-hosting` | dead | evidence documented | binding per-ip-shaping | category cloud VM
- needs card unknown, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://the.hosting/en/
- free tier: The selling brand publishes one price floor and no plan card: 'Uniform rental rates across all countries - from 5.77 EUR per month' on the homepage, with KVM, NVMe in RAID 10, 'ports with a speed of 1-10 Gbps', unlimited traffic and presence 'in more than 50 countries'. No page read paired that price with vCPU, RAM or disk: /en/vps renders the marketing copy but its tariff cards are client-side, and /en/vps-configurator renders no numbers. The 12 tariff names are published on the review promotion page: Aluminium, Argentum, Ruthenium, Iridium, Palladium, Osmium, Aurum, Platinum, Rhodium, Mithril, Adamantium, Obsidian. The free test is 3 days and gated on an account, a sales ticket and KYC. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic is stated: 'No Bandwidth Limits' and 'Enjoy complete freedom with unlimited traffic for your project' on the homepage, with no monthly byte figure published anywhere read | metered: no | source: [1]
- identity: national-id | detail: The 3-day test requires four steps, quoted: 'Authorize - Log in or sign up for THE.Hosting', 'Create a request to the sales department with the subject VPS Test', then 'KYC verification - After verification, you will receive a server to test for 3 days.' The page names KYC and does not say which document, which country, or whether a card is also required, so the rung is national-id on the page's own word and not on a document list. Payment methods are not stated on any page read.
- interface: rest
- limits:
  - per-ip-shaping (binding): The only throughput wall the pages publish is the port, quoted as 'The servers run on the ports with a speed of 1-10 Gbps', while traffic is stated as unlimited. No byte counter is published, so the port is what a daytime transfer meets first. Not probed. [1]
- limits note: The only throughput wall the pages publish is the port, quoted as 'The servers run on the ports with a speed of 1-10 Gbps', while traffic is stated as unlimited. No byte counter is published, so the port is what a daytime transfer meets first. Not probed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the order and account flow is a client area at client.the.hosting running BILLmanager, linked from the trial page as billmgr?startform=v2.vds.order.pricelist; no public API is documented on the pages read. A client would be a browser session or a wrapper around that panel. That is a tooling note, not a verdict.
- composes with: nothing to chain: the operator announced permanent discontinuation of all services, disabled ordering and renewals, and said accounts and data will be deleted. A machine that will be erased is not a place to put the archive index or a crawler front end.
- reliability: 2026-05-30 first-party notice: permanent discontinuation of all services, registration, ordering and renewals disabled, accounts and data to be permanently deleted.
- notes: Two pages on the same site disagree and both return 200, which is the finding. The marketing pages (homepage, /en/vps, /en/test-vps, /en/gift-vps) still advertise capacity and a 3-day trial; the news notice dated 2026-05-30 says the business is closing and ordering is disabled. If the wind-down is reversed, this record flips to trial-only with a 3-day test gated on KYC.
- extras:
  - facets.free_tier_kind: trial
- evidence:
  - [2] 2026-10-22: the operator states the shutdown in its own words: 'due to unforeseen and unavoidable force majeure circumstances, The.Hosting is forced to permanently discontinue all its operational services and wind down its activities', and 'All active forms of registration, ordering, and renewals have been disabled. No new services can be purchased.', and 'Once the wind-down process is completed, all accounts and data will be permanently deleted from our systems.'
  - [3] 2026-10-22: the notice is the newest item on the news index and is dated 30.05.2026 in the line above its title; the next item down is dated 23.04.2026, and no item after 30.05.2026 exists
  - [4] 2026-10-22: the trial still advertises itself on a live 200 page: 'We offer you to test VPS/VDS from THE.Hosting for free for 3 days', step 4 'KYC verification' with 'After verification, you will receive a server to test for 3 days.', and the condition 'The test period can be used only once.'
  - [5] 2026-10-22: the 'free VPS' promotion is not free capacity: 'get up to 30 days VPS for free just for an honest review and subscribing to our social networks', and the first condition is 'Order or extend your current VPS for at least 1 month', with 30 days for the Aluminium, Argentum and Ruthenium tariffs, 14 for Iridium to Rhodium, and 7 for Mithril, Adamantium and Obsidian
  - [1] 2026-10-22: the homepage still sells, months after the notice: 'Uniform rental rates across all countries - from 5.77 EUR per month' (the page prints the euro sign; transcribed here as EUR), 'Today THE.Hosting is present in more than 50 countries', and 'No Bandwidth Limits / Enjoy complete freedom with unlimited traffic for your project'
  - [6] 2026-10-22: the product page is still up and still advertises a test period in its own title, 'VPS hosting - VPS/VDS hosting rental - Buy a VPS server with a test period', and states 'The servers run on the ports with a speed of 1-10 Gbps' and 'After ordering and paying for the VPS, it will be provided to you within 15 minutes'
- sources:
  - [1] https://the.hosting/en/
  - [2] https://the.hosting/en/news/notice-of-service-discontinuation-and-account-closure
  - [3] https://the.hosting/en/news/
  - [4] https://the.hosting/en/test-vps
  - [5] https://the.hosting/en/gift-vps
  - [6] https://the.hosting/en/vps
