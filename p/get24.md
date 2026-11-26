# GeT24

> get24.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/get24/ | JSON https://fshy.ajam.dev/api/v1/entity/get24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GeT24

- `debrid/get24` | paid-only | evidence documented | binding volume-quota | category multi-hoster (premium link generator) | tier lite
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:53.124Z (live) | stale on 2026-12-26
- url https://get24.org/pricing
- price PLN 29.99/month Lite, PLN 39.99/month Pro (USD 7.69 and USD 10.26 at 3.899348 PLN/USD on 2026-10-23) | parsed USD 7.64/mo
- free tier: No free tier. 'After the expiration period, the account returns to free mode' - free mode carries no transfer, and the only plans are paid: Test 24h, Pro and Lite. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The host list marks individual hosts 'Free' or 'Pro'; that is a host class, not a plan. Free mode's actual allowance is not published.
- per-object cap: not applicable: links only, no storage | source: [2]
- retention: not applicable: no storage product; the pricing page says account expiry 'does not delete data or history' | source: [1]
- egress: 'I do not limit speed - you will reach the maximum of your connection. Our servers in the EU have a total capacity of 120 Gbps.' Transfer is capped per day instead: 35 GB/day on both paid plans. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Checkout in PLN by card, wire or crypto ('Global · Wire · Card · Crypto'). Account creation details were not readable without an order flow.
- interface: rest
- limits:
  - volume-quota (binding): 35 GB/day on Pro and Lite; 35 GB total on the 24-hour test; Pro covers 157 hosts and Lite 120 of 157 [1]
  - per-object-cap: none published; the FAQ says a link is checked before quota is spent [1]
- limits note: Lite covers 120 of 157 hosts and excludes Pro hosts; Pro covers all 157. Both paid plans carry the same 35 GB daily transfer.
- binding note: 35 GB/day is 1.05 TB/month, which just clears 1 TiB, so the daily counter is what binds; on Lite the tighter constraint is the 39 missing hosts, not the bytes.
- interface detail: JDownloader 2, pyLoad, IDM and an open REST API are listed on the home page; a web panel is available.
- tooling: JDownloader 2, pyLoad, IDM. No API documented publicly.
- composes with: 35 GB/day is 1.05 TB/month, enough for the 1 TiB monthly volume, but at PLN 29.99 (USD 7.69) it is above the debrid USD 5 bar and adds a Polish-currency payment step.
- reliability: Hosts carry a 'Maintenance' state in the on-page list; quota is shared across every device on the account, so parallel downloads spend the same 35 GB/day.
- notes: A Polish service with PLN-only pricing, which is why it does not surface in English comparisons. It clears 100 GiB/month on paper (35 GB/day) but misses the USD 5 bar. Currency conversion from the exchangerate-api USD base read on 2026-10-23.
- evidence note: Prices and transfer quotas are quoted from the vendor's pricing page. The free-mode allowance and the account fields are unverified.
- extras:
  - hosts.lite: 122
  - hosts.pro: 161
  - daily_transfer: 35 GB
  - backbone: 120 Gbps EU
- evidence:
  - [1] 2026-10-23: 'Test 24h 9.99 PLN - Transfer: 35 GB - Hosts: 161'; 'Pro 39.99 PLN / mo - Transfer: 35 GB / day - Hosts: 161'; 'Lite 29.99 PLN / mo - Transfer: 35 GB / day - Hosts: 122 of 161'; 'No. Every plan is a one-time payment. After the expiration period, the account returns to free mode'
  - [2] 2026-10-23: 'Active services 154', 'Files 115 hosts', and per-host counters such as 'Copycase 0.00 / 35 GB' showing the daily counter shape
  - [1] 2026-11-25: the paid plans allow 35 GB per day | capture: sha256:1cae4cdc26e31ab92bbf5625b5272e2321a4faa65c65b019399143960119068a | quote: - Transfer: 35 GB / day
  - [1] 2026-11-25: Lite covers 120 of 157 hosts | capture: sha256:1cae4cdc26e31ab92bbf5625b5272e2321a4faa65c65b019399143960119068a | quote: - Hosts: 120 of 157
  - [3] 2026-11-25: the home page lists an open REST API and three downloader integrations | capture: sha256:3d2deaf462c27e16db6de289cec44a39cdf664164d1b8a183c3a6d194d49cbdc | quote: Native support for JDownloader 2, pyLoad, IDM, and open REST API for building your own solutions.
  - [1] 2026-11-25: Pro covers 157 hosts and Lite 120 | capture: sha256:1cae4cdc26e31ab92bbf5625b5272e2321a4faa65c65b019399143960119068a | quote: Pro gives full access to all 157 hosts, including services marked as "Pro". Lite supports 120 hosts at a lower price.
  - [1] 2026-11-25: all devices share the same daily transfer | capture: sha256:1cae4cdc26e31ab92bbf5625b5272e2321a4faa65c65b019399143960119068a | quote: There is no device limit, but download sessions share your daily transfer.
- sources:
  - [1] https://get24.org/pricing
  - [2] https://get24.org/debrid
  - [3] https://get24.org/
