# Offcloud lifetime via StackSocial

> pcworld.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pcworld/ | JSON https://fshy.ajam.dev/api/v1/entity/pcworld.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Offcloud lifetime via StackSocial

- `debrid/offcloud-lifetime-via-stacksocial` | dead | evidence reported | binding write-gated | category debrid resale - lifetime deal sold through a bundle marketplace | tier resale
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:59.772Z (live) | stale on 2026-11-18
- url https://shop.pcworld.com/sales/offcloud-unlimited-lifetime-subscription
- free tier: One-off 'lifetime' purchase: US$39.99 and later US$36.19 through StackSocial, and EUR 29.25 on a German deal run posted 2025-09-21 and expired 2025-11-17. PCWorld's shop still lists it as 'Offcloud Lifetime Subscription' with 'Length of access: lifetime'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the seller is a deal marketplace; the service is Offcloud, which still sells a yearly plan at EUR 40
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: the lifetime SKU's own specs: 'Unlimited remote uploads', '50GB of cloud space', '30GB of monthly quota for premium sources'. The monthly 30 GB is the real ceiling behind the word unlimited. | metered: yes | free allowance: 30 GB/month of premium-source traffic | source: [1]
- identity: email | detail: marketplace account plus an Offcloud account; no identity document
- interface: rest
- limits:
  - write-gated (binding): lifetime converted to a one-year membership in January 2026 [2]
  - volume-quota: 30 GB/month for premium sources [1]
  - per-ip-shaping: 3 IP addresses per licence [1]
- binding note: 30 GB/month would bind long before 1 TiB, but the entitlement itself was rewritten first: the constraint that actually ends the deal is the vendor's decision to stop honouring the lifetime.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Buyers report the lifetime was replaced: 'I purchased this service during their last Lifetime StackSocial sale in October 2025. Today in January 2026, they claim that a member of staff passed and they are changing everything' (2026-01-24); 'given a 1 year free premium. Now my account instead of being a lifetime premium' (2026-02-18). A Taiwanese buyer got the same answer from support on 2026-01-21: the old lifetime is invalid and the compensation is one year. Trustpilot's aggregate was 1.7/5 from 86 reviews on 2026-11-03.
- notes: The clearest dated death in the sector: a lifetime debrid bought in October 2025 was converted in January 2026. The vendor did not close, which is worse for the buyer than a closure: the service continues on a plan the buyer did not choose, and Offcloud's terms state no refund is available. Even while it was sold, the 'unlimited' lifetime carried a 30 GB/month premium-source quota. Documented as the offer's verdict; Offcloud's yearly plan is priced in pricing-history/records/offcloud.json and is not re-documented here.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: 'Length of access: lifetime', 'Max number of device(s): 3 IP addresses', '50GB of cloud space', '30GB of monthly quota for premium sources'
  - [3] 2026-10-23: the 1.8/5 score from 86 reviews and two dated reports (2026-01-24, 2026-02-18) that lifetime buyers were moved to a one-year or yearly plan
  - [2] 2026-10-23: 2026-01-21 buyer post plus the same-day follow-up quoting support: the new team runs it, the old lifetime is invalid, the compensation is one year
  - [4] 2026-10-23: the US$36.19 StackSocial run, now marked expired and posted about a year before 2026-10-23
  - [5] 2026-10-23: the last run: '29,25€', posted 2025-09-21, 'Dieser Deal ist abgelaufen am 17. Nov. 2025'
  - [1] 2026-11-03: the reseller's SKU page still lists a 30GB monthly quota for premium sources | capture: sha256:0839b92f861380570031123566417d2e5da7289de000b3bc88d2fca5705af32a | quote: 30GB of monthly quota for premium sources
  - [1] 2026-11-03: the SKU page still lists 3 IP addresses per licence | capture: sha256:0839b92f861380570031123566417d2e5da7289de000b3bc88d2fca5705af32a | quote: Max number of device(s): 3 IP addresses
  - [1] 2026-11-03: the SKU page still lists the length of access as lifetime | capture: sha256:0839b92f861380570031123566417d2e5da7289de000b3bc88d2fca5705af32a | quote: Length of access: lifetime
  - [6] 2026-11-03: the vendor's home page lists Yearly Premium at EUR 40 | capture: sha256:3c5bc39f151febde8beb82cd26606544d2b4552c87a275ecd21174950b6a89d5 | quote: Yearly Premium €40
  - [3] 2026-11-03: a Trustpilot review dated 2026-05-14 reports a lifetime subscription changed to a 1 year subscription without notice | capture: sha256:65aeb3aa7d22e27569f9c4b4a8161a60e4e365e7d90991036ada0632d8cc54a6 | quote: They first give you subscription in name of life time and without notice they change to 1 year subscription this happend in within 1 week.
  - [2] 2026-11-03: support said the new team runs it and the old lifetime plan is invalid | capture: sha256:63b4d82a63ecef67d5a3a3ad58707168688e162e0c6b8ad44279d803bb1ba6ce | quote: 客服回覆說現在新團隊運營 舊的終身方案就是失效了 補 01/21 16:05
  - [3] 2026-11-03: the Trustpilot page for Offcloud shows 1.7 from 86 reviews | capture: sha256:65aeb3aa7d22e27569f9c4b4a8161a60e4e365e7d90991036ada0632d8cc54a6 | quote: 1.7 [Software Company](/categories/software_company)
- sources:
  - [1] https://shop.pcworld.com/sales/offcloud-unlimited-lifetime-subscription
  - [2] https://www.ptt.cc/bbs/Free_box/M.1768979304.A.74C.html
  - [3] https://www.trustpilot.com/review/offcloud.com
  - [4] https://www.ozbargain.com.au/node/926150
  - [5] https://www.mydealz.de/deals/offcloud-lifetime-abo-multihoster-fur-downloads-streaming-ahnlich-wie-real-debrid-2639003
  - [6] https://offcloud.com/
