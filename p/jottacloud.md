# Jottacloud

> jottacloud.com | Storage; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jottacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/jottacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jottacloud Pro 20 TB

- `storage/jottacloud-pro-20-tb` | qualifies | evidence reported | binding none | category Nordic cloud drive, subscription, unthrottled
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jottacloud.com/en/why-jottacloud/jottacloud-pro
- price $3.20/TB at 20 TB ($64.01/mo); $3.20/TB at 30 TB ($96.08/mo); at 5 TB-equivalent the Pro 10 TB tier is $6.39/TB | parsed USD 3.2/TB-mo
- free tier: 10 / 20 / 30 / 50 TB fixed tiers, 1 user each | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress fee, 'Maximum speed' on both directions. Explicitly no bandwidth limitation, unlike the Unlimited tier. | metered: no
- identity: email | detail: email
- interface: rclone
- limits note: None on transfer; the cap is the fixed quota
- interface detail: rclone native, desktop apps
- tooling: rclone native backend
- composes with: same as Unlimited
- reliability: Same operator as Unlimited but no retroactive-throttle exposure, since speed is guaranteed
- notes: the same as the free tier
- extras:
  - price_verbatim: $3.20/TB at 20 TB ($64.01/mo); $3.20/TB at 30 TB ($96.08/mo); at 5 TB-equivalent the Pro 10 TB tier is $6.39/TB
- evidence:
  - [1] 2026-10-21: 'Pro 10 TB NOK 299 / month', 'Pro 20 TB NOK 599 / month', 'Pro 30 TB NOK 899 / month', 'Pro 50 TB NOK 1499 / month', each 'Maximum speed'
  - [2] 2026-10-21: yearly: Pro 20 TB NOK 5990/year
- sources:
  - [1] https://jottacloud.com/en/why-jottacloud/jottacloud-pro
  - [2] https://jottacloud.com/en/pricing

## Jottacloud (Norway)

- `storage/jottacloud` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category consumer backup / drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jottacloud.com/en/pricing
- price $1.30/TB/mo at 10 TB, $0.65/TB/mo at 20 TB, $0.43/TB/mo at 30 TB (flat $12.99/mo 'Unlimited', throttled above 5 TB) | parsed USD 12.99/mo
- disagrees on verdict: `storage/jottacloud` says qualifies-with-caveat, `storage/jottacloud-2` says fails-quota
- disagrees on verdict: `storage/jottacloud` says qualifies-with-caveat, `storage/jottacloud-free` says fails-egress
- free tier: 5 GB free. 'Unlimited*' Personal at USD 12.99/mo or USD 129.90/yr, with the asterisk being 'upload speed gradually reduced after 5 TB'. Home 1 TB NOK 79/mo, Pro up to 50 TB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress charge. 'No bandwidth limitation' is listed on Home 1 TB, and the Unlimited plan's only stated constraint is upload throttling, not download metering. | metered: no
- identity: email | detail: email
- interface: rest, rclone, cli
- limits:
  - per-ip-shaping (binding): speed throttled above 5 TB, described by HN as a 'harsh inflection' around [1]
- limits note: Per-ip-shaping: upload speed throttled above 5 TB, described by HN as a 'harsh inflection' around 16 TB. Quotas are quoted in decimal TB, not TiB. Rclone about reports 9.095 TiB for a 10 TB plan (forum.rclone.org/t/45928), so the real capacity is ~9% smaller than the marketing number.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Tier 2 rclone backend (md5, ModTime R/W, case-insensitive, metadata RWU). One of the few Tier-2 providers that is also a real commercial backup service. Duplicati lists Jottacloud as a natively supported provider. Official CLI plus rclone+restic documented by HN commenters.
- composes with: The only candidate here whose free-tier ceiling is 'unlimited' at a flat price, so it is the single account that can absorb a whole 20 TB archive without sharding. At the cost of upload speed past 5 TB. Pairs naturally as the durable tier under rclone crypt.
- reliability: Long-running, well-documented provider; the throttle is policy, not breakage. The TB-vs-TiB reporting gap is measured, not speculative.
- notes: the same as the free tier
- extras:
  - price_verbatim: $1.30/TB/mo at 10 TB, $0.65/TB/mo at 20 TB, $0.43/TB/mo at 30 TB (flat $12.99/mo 'Unlimited', throttled above 5 TB)
- evidence:
  - [1] 2026-10-21: '5 GB Free', 'Unlimited* NOK 129 / month ... *Upload speed gradually reduced after 5 TB', 'Home 1 TB NOK 79 / month ... No bandwidth limitation'
  - [2] 2026-10-21: 'You get maximum speed up to 5 TB, after which the speed is gradually reduced'
  - [3] 2026-10-21: USD 129.90/yr Unlimited, USD 79.90/yr Home 1 TB
  - [4] 2026-10-21: native backend, OAuth refresh-token family handling, quota visible via rclone about
  - [5] 2026-10-21: 10 TB plan reports 9.095 TiB
  - [6] 2026-10-21: 'unlimited (in reality after 5TB they start slowing your upload speed)... up to about 16TB, where you hit a harsh inflection'
  - [7] 2026-10-21: Jottacloud listed among natively supported destinations
- sources:
  - [1] https://jottacloud.com/en/pricing
  - [2] https://jottacloud.com/en/why-jottacloud
  - [3] https://www.itechfaqs.com/tools/jottacloud/pricing/
  - [4] https://rclone.org/jottacloud/
  - [5] https://forum.rclone.org/t/jottacloud-report-plans-and-space-on-web-as-terabytes-instead-of-tebibytes/45928
  - [6] https://news.ycombinator.com/item?id=30580044
  - [7] https://github.com/Duplicati/Duplicati

## Jottacloud Unlimited (Personal)

- `storage/jottacloud-unlimited` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category Nordic cloud drive, subscription, storage-VPS economics in disguise
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jottacloud.com/en/pricing/
- price $2.76/TB at 5 TB; $0.69/TB at 20 TB (NOK 129/mo = $13.79 flat, so marginal cost per added TB is $0)
- free tier: Unlimited storage; 1 user. Free 5 GB tier exists. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress fee and no download throttle. Vendor text: 'Reduced upload speed means that uploading files from your device to Jottacloud might take a little longer. Download speed and other use of the service is not changed, and you can still store as much data as you need in your account.' Upload is throttled once >5 TB stored: 'If you store more than 5 TB of data on Jottacloud, your upload speed is automatically reduced. The reduction in upload speed is greater the more data you store in your account.' | metered: no
- identity: email | detail: email
- interface: rclone, cli
- limits:
  - per-ip-shaping (binding): 1.85 MB/s [1]
  - per-ip-shaping (binding): 250 KB/s [1]
- limits note: Constraint type: per-ip-shaping, upload side only. Reported throttle at 6 TB is ~1.85 MB/s per transfer; at 44 TB one Duplicati user measured 250 KB/s. Download path unaffected. Non-commercial licensing on the Personal tier.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: Web + desktop + rclone (native `jottacloud` backend, documented on rclone.org)
- tooling: rclone native backend, supports --fast-list; CLI documented
- composes with: rclone -> local -> any S3/WebDAV target; can front with Cloudflare only by proxying your own origin, not directly
- reliability: No documented mass data-loss event. Throttle policy was changed retroactively in 2021/2022 and the Norwegian Consumer Council flagged it; users were offered refunds. Operational risk is policy drift, not deletion.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.76/TB at 5 TB; $0.69/TB at 20 TB (NOK 129/mo = $13.79 flat, so marginal cost per added TB is $0)
- evidence:
  - [1] 2026-10-21: 'Unlimited* NOK 129 / month NOK 1290 / year ... Unlimited storage ... * Upload speed gradually reduced after 5 TB'
  - [2] 2026-10-21: 'Download speed and other use of the service is not changed'
  - [3] 2026-10-21: native backend, --fast-list supported
  - [4] 2026-10-21: 44 TB account throttled to 250 KB/s upload, download fine
  - [5] 2026-10-21: payment: 'We support VISA and MasterCard' via Stripe; no PayPal, no crypto
- sources:
  - [1] https://jottacloud.com/en/pricing/
  - [2] https://docs.jottacloud.com/en/articles/3271114-reduced-upload-speed
  - [3] https://rclone.org/jottacloud/
  - [4] https://forum.duplicati.com/t/jottacloud-difference-in-upload-speeds-rclone-duplicati/19225
  - [5] https://www.jottacloud.com/en/pricing/

## jottacloud free

- `storage/jottacloud-free` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jottacloud.com/en/pricing
- disagrees on verdict: `storage/jottacloud` says qualifies-with-caveat, `storage/jottacloud-free` says fails-egress
- disagrees on verdict: `storage/jottacloud-2` says fails-quota, `storage/jottacloud-free` says fails-egress
- free tier: None reachable: 5 GB free. The interesting product is 'Unlimited' at NOK 129/mo, which throttles upload after 5 TB. And it is paid. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: egress
  - dead_end.why: 5 GB free. The interesting product is 'Unlimited' at NOK 129/mo, which throttles upload after 5 TB — and it is paid.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB free. The interesting product is 'Unlimited' at NOK 129/mo, which throttles upload after 5 TB — and it is paid.
- sources:
  - [1] https://jottacloud.com/en/pricing

## jottacloud

- `storage/jottacloud-2` | fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:26.511Z (live) | stale on 2026-12-05
- url https://jottacloud.com/en/pricing/
- disagrees on verdict: `storage/jottacloud` says qualifies-with-caveat, `storage/jottacloud-2` says fails-quota
- disagrees on verdict: `storage/jottacloud-2` says fails-quota, `storage/jottacloud-free` says fails-egress
- free tier: none reachable: 5 GB free; the genuinely interesting 'Unlimited' plan is NOK 129/mo and throttles upload after 5 TB. Not free. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: No download cap or egress price is listed on any plan; the Home 1 TB and Home 5 TB plans state no bandwidth limitation, and the Unlimited plan (NOK 129 / month) reduces upload speed gradually after 5 TB. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: documented from the vendor page read on 2026-11-03 (https://jottacloud.com/en/pricing/): the 5 GB free plan, the Home plans without bandwidth limitation and the upload slowdown after 5 TB on the Unlimited plan. Identity, retention and per-object cap were not read.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 5 GB free; the genuinely interesting 'Unlimited' plan is NOK 129/mo and throttles upload after 5 TB. Not free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB free; the genuinely interesting 'Unlimited' plan is NOK 129/mo and throttles upload after 5 TB. Not free.
  - [1] 2026-11-03: the Home 1 TB and Home 5 TB plans state no bandwidth limitation | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: ✔ No bandwidth limitation
  - [1] 2026-11-03: the free plan is 5 GB | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: ✔ 5 GB storage
  - [1] 2026-11-03: the Unlimited plan reduces upload speed after 5 TB; no download cap is stated | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: * Upload speed gradually reduced after 5 TB
  - [1] 2026-11-04: the free plan is 5 GB | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: ✔ 5 GB storage
  - [1] 2026-11-04: the Unlimited plan reduces upload speed after 5 TB | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: * Upload speed gradually reduced after 5 TB
  - [1] 2026-11-04: the Home plans state no bandwidth limitation | capture: sha256:dc898362961859b8494f6add836011bdb27b60ed635e9b5957111e0e0e39677b | quote: ✔ No bandwidth limitation
- sources:
  - [1] https://jottacloud.com/en/pricing/
